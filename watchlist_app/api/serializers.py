from dataclasses import field
from pyexpat import model
from unicodedata import name
from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchlistSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watchlist
        fields = "__all__"
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many= True, read_only = True)
    #this watchlist came from db where related name has been used
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
    # def get_len_name(self, object): 
    #     return len(object.name)
 
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value   
    
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description must not be the same")
    #     else:
    #         return data
 
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description must not be the same")
    #     else:
    #         return data