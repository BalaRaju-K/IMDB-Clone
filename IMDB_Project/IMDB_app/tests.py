from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from IMDB_app import models

class StreamPlatformsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'token' + self.token.key)
        self.stream = models.StreamPlatforms.objects.create(name = 'Netflix',
            about = 'The world of NetFlix',
            website = 'https://www.netflix.com')
     
    def test_streamPlatform_create(self):
        url = reverse('StreamPlatformsAV')
        data = {
            'name': 'Netflix',
            'about' : 'The world of NetFlix',
            'website': 'https://www.netflix.com'
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_streamPlatformList(self):
        response = self.client.get(reverse('StreamPlatformsAV'))    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamPlatform_detail(self):        
        response = self.client.get(reverse('StreamPlatformsUpdate', args=[self.stream.id, ]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'token' + self.token.key)
        self.stream = models.StreamPlatforms.objects.create(name = 'Netflix',
            about = 'The world of NetFlix',
            website = 'https://www.netflix.com')
        self.movie= models.WatchList.objects.create(
            title = 'Spidy',
            description = 'Sony',
            platform = self.stream,
            avg_reviews = 4.5,
            number_reviews = 100,
            active = True
        )
     
    def test_watchlist_create(self):
        url = reverse('WatchListAV')
        data = {
            'title': 'Spidy',
            'description' : 'Sony',
            'platform': self.stream,
            'active' : True
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('WatchListAV'))    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_detail(self):        
        response = self.client.get(reverse('WatchListUpdate', args=[self.movie.id, ]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.stream = models.StreamPlatforms.objects.create(name = 'Netflix',
            about = 'The world of NetFlix',
            website = 'https://www.netflix.com')
        self.movie = models.WatchList.objects.create(
            title="Test Movie",
            description="A test movie description",
            platform= self.stream,
            active=True
        )
        # This self.movies2 and self.review both together is created before testing (detail, update, delete).
        self.movie2 = models.WatchList.objects.create(
            title="Test Movie2",
            description="A test movie description222",
            platform= self.stream,
            active=True
        )
        self.review = models.Review.objects.create(
            Review_user=self.user,
            rating=4,
            comment="Great movie!",
            active=True,
            movielist=self.movie2,
        )
    
    def test_review_creation(self):
        data = {
            "Review_user": self.user,
            "rating": 5,
            "comment": "Amazing movie!",
            "active": True,
            "movielist": self.movie.id 
        }
        response = self.client.post(reverse('reviewCreate', args=[self.movie.id]), data)
        self.assertEqual(response.status_code, 201)
    
    def test_review_list(self):
        response = self.client.get(reverse('ReviewList', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)

    def test_review_detail(self):
        response = self.client.get(reverse('ReviewDetail', args=[self.review.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_review_update(self):
        data = {
            "rating": 3,
                "comment": "Changed my mind. It's average.",
                "active": True
            }
        response = self.client.put(reverse('ReviewDetail', args=[self.review.id]), data)
        self.assertEqual(response.status_code, 200)
    
    def test_review_delete(self):
        response = self.client.delete(reverse('ReviewDetail', args=[self.review.id]))
        self.assertEqual(response.status_code, 204)
    
    def test_Review_User(self):
        response = self.client.get('/movies/stream/?username'+ self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
class WatchListNewTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # Create a StreamPlatform
        self.stream = models.StreamPlatforms.objects.create(
            name="Netflix",
            about="Streaming platform",
            website="https://www.netflix.com"
        )
        
        # Create WatchLists
        self.movie1 = models.WatchList.objects.create(
            title="Movie 1",
            description="Description for movie 1",
            platform=self.stream,
            avg_reviews=4.5,
            active=True
        )
        self.movie2 = models.WatchList.objects.create(
            title="Movie 2",
            description="Description for movie 2",
            platform=self.stream,
            avg_reviews=3.0,
            active=True
        )
    
    def test_watchlist_retrieval(self):
        response = self.client.get(reverse('WatchListNew'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Assuming pagination shows all results

    def test_watchlist_search_filter(self):
        response = self.client.get(reverse('WatchListNew'), {'search': 'Netflix'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(movie['title'] == 'Movie 1' for movie in response.data['results']))

    def test_watchlist_ordering(self):
        response = self.client.get(reverse('WatchListNew'), {'ordering': 'avg_reviews'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if movies are ordered by avg_reviews
        avg_reviews = [movie['avg_reviews'] for movie in response.data['results']]
        self.assertEqual(avg_reviews, sorted(avg_reviews))
