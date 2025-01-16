from django.urls import path
from IMDB_app.api.views import WatchListAV, WatchListUpdate, StreamPlatformsAV, StreamPlatformsUpdate, ReviewList, ReviewCreate, ReviewDetail, WatchListNew, ReviewUser
urlpatterns = [
    path('watchlist/', WatchListAV.as_view(), name="WatchListAV"),
    path('watchlist/<int:pk>', WatchListUpdate.as_view(), name="WatchListUpdate"),
    
    path('watchlistnew/', WatchListNew.as_view(), name="WatchListNew"),
    
    path('stream/', StreamPlatformsAV.as_view(), name="StreamPlatformsAV"),
    path('stream/<int:pk>', StreamPlatformsUpdate.as_view(), name="StreamPlatformsUpdate"),
    
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='ReviewList'),
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='reviewCreate'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='ReviewDetail'),
    
    path('stream/reviews/<str:username>/', ReviewUser.as_view(), name='ReviewUser'),
]
