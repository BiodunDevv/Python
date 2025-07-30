from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.response import Response
from order.serializer import HomeSerializer, PlayerSerializer, SinglePlayerSerializer
from order.models import Player
from django.shortcuts import get_object_or_404

# Create your views here.

class HomeView(generics.GenericAPIView):
    serializer_class = HomeSerializer

    def get(self, request):
        return Response({"message": "You're welcome to Crave Corner!"}, status=200)
    
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Welcome to Crave Corner!", "data": serializer.data}, status=201)
        

class PlayerView(generics.GenericAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        players = Player.objects.all()
        return players
    
    def get(self, request):
        player_list = self.get_queryset()
        serializer = self.serializer_class(player_list, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        #To avoid duplicate entries, check if a player with the same name and club already exists
        if Player.objects.filter(name=serializer.validated_data['name'], club=serializer.validated_data['club']).exists():
            return Response({"error": "Player with this name and club already exists."}, status=400)
        
        serializer.save()
        return Response({"message": "Player created successfully!", "data": serializer.data}, status=201)
    
class SinglePlayerView(generics.GenericAPIView):
    serializer_class = SinglePlayerSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        player = get_object_or_404(Player, id=id)
        return player
    
    def get(self, request, id):
        player = self.get_queryset()
        serializer = self.serializer_class(player)
        return Response(serializer.data, status=200)
    

    def patch(self, request, id):
        player = self.get_queryset()
        serializer = self.serializer_class(instance=player, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Player updated successfully!", "data": serializer.data}, status=200)

    def delete(self, request, id):
        player = self.get_queryset()
        player.delete()
        return Response({"message": "Player deleted successfully!"}, status=204)