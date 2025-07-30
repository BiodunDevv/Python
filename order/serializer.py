from rest_framework import serializers
from .models import Player,positions,gender_choices



class HomeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 18 or value > 65:
            raise serializers.ValidationError("Age must be between 18 and 65.")
        return value
    
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be from the domain 'example.com'.")
        return value
    

class PlayerSerializer(serializers.ModelSerializer):


    name = serializers.CharField()
    age = serializers.IntegerField()
    club = serializers.CharField()
    jersey_number = serializers.IntegerField()
    position = serializers.ChoiceField(choices=[position[0] for position in positions])
    height = serializers.DecimalField(max_digits=3, decimal_places=1, write_only=True)
    gender = serializers.ChoiceField(choices=[gender[0] for gender in gender_choices], write_only=True)
    is_academy = serializers.BooleanField(default=False, write_only=True)
    bio = serializers.CharField(required=False, write_only=True)

    def validate_age(self, value):
        if value < 18 or value > 50:
            raise serializers.ValidationError("Age must be between 18 and 50.")
        return value

    class Meta:
        model = Player
        fields = ['id', 'name', 'age', 'club', 'jersey_number', 'position', 'height', 'gender', 'is_academy', 'bio']


class SinglePlayerSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    age = serializers.IntegerField()
    club = serializers.CharField()
    jersey_number = serializers.IntegerField()
    position = serializers.ChoiceField(choices=[position[0] for position in positions])
    height = serializers.DecimalField(max_digits=3, decimal_places=1)
    gender = serializers.ChoiceField(choices=[gender[0] for gender in gender_choices])
    is_academy = serializers.BooleanField(default=False)
    bio = serializers.CharField(required=False)

    def validate_age(self, value):
        if value < 18 or value > 50:
            raise serializers.ValidationError("Age must be between 18 and 50.")
        return value

    class Meta:
        model = Player
        fields = ['id', 'name', 'age', 'club', 'jersey_number', 'position', 'height', 'gender', 'is_academy', 'bio']