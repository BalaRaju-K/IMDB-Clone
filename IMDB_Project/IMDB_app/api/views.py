from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from IMDB_app.models import StreamPlatforms, WatchList, Review
from IMDB_app.api.serializers import StreamPlatformsSerializer, WatchListSerializer, ReviewSerializer
from IMDB_app.api.permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from IMDB_app.api.pagination import MovieListPagination
from IMDB_app.api.throttling import ReviewCreateThrottle, ReviewListThrottle
 
class ReviewUser(generics.ListAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username')    
        return Review.objects.filter(Review_user__username=username)

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movielist=pk)
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        four = self.request.user
        review_queryset = Review.objects.filter(movielist=movie, Review_user=four)
        
        if review_queryset.exists():
            raise ValidationError('You have already given a Review')
        
        if movie.number_reviews == 0:
            movie.avg_reviews = serializer.validated_data['rating']
        else:
            movie.avg_reviews = (movie.avg_reviews * movie.number_reviews + serializer.validated_data['rating']) / (movie.number_reviews + 1)
        
        movie.number_reviews += 1
        movie.save()
        return serializer.save(movielist=movie, Review_user=four)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope ='review-detail'

class WatchListNew(generics.ListAPIView):
    queryset = WatchList.objects.all().order_by('avg_reviews')
    serializer_class = WatchListSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = MovieListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['platform__name', 'title']
    ordering_fields = ['avg_reviews']

class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListUpdate(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movies)
            return Response(serializer.data)

        except WatchList.DoesNotExist:
            return Response(
                {"error": f"WatchList with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
            movies.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except WatchList.DoesNotExist:
            return Response(
                {"error": f"WatchList with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)

class StreamPlatformsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        platform = StreamPlatforms.objects.all()
        serializer = StreamPlatformsSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformsUpdate(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movies = StreamPlatforms.objects.get(pk=pk)
            serializer = StreamPlatformsSerializer(movies)
            return Response(serializer.data)
        except StreamPlatforms.DoesNotExist:
            return Response(
                {"error": f"StreamPlatform with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            movies = StreamPlatforms.objects.get(pk=pk)
            serializer = StreamPlatformsSerializer(movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except StreamPlatforms.DoesNotExist:
            return Response(
                {"error": f"StreamPlatform with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movies = StreamPlatforms.objects.get(pk=pk)
            movies.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except StreamPlatforms.DoesNotExist:
            return Response(
                {"error": f"StreamPlatform with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)

