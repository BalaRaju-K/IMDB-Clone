from rest_framework import serializers
from IMDB_app.models import StreamPlatforms, WatchList, Review

class ReviewSerializer(serializers.ModelSerializer):
    Review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('movielist',)
        #fields = '__all__'
        
class WatchListSerializer(serializers.ModelSerializer):
    #movies = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformsSerializer(serializers.ModelSerializer):
    channel = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatforms
        fields = '__all__'


            