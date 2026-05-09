from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model  = Player
        fields = ['id', 'name', 'position', 'shirt_number', 'team', 'team_name']


class TeamSerializer(serializers.ModelSerializer):
    # Punto extra: muestra cuántos jugadores tiene el equipo
    total_players = serializers.SerializerMethodField()
    players       = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model  = Team
        fields = ['id', 'name', 'city', 'category', 'total_players', 'players']

    def get_total_players(self, obj):
        return obj.players.count()