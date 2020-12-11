from django.test import TestCase, Client
from django.urls import reverse
from .database import database


class DatabaseTests(TestCase):
    def test_homepage_status_code(self):
        client = Client()
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_view(self):
        client = Client()
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_add_status_code(self):
        client = Client()
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_view(self):
        client = Client()
        response = self.client.get(reverse('add'))
        self.assertTemplateUsed(response, 'add.html')
        
    def test_search_status_code(self):
        client = Client()
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
    
    def test_search_view(self):
        client = Client()
        response = self.client.get(reverse('search'))
        self.assertTemplateUsed(response, 'search.html')
    """
    def test_map_status_code(self):
        client = Client()
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)

    def test_map_view(self):
        client = Client()
        response = self.client.get(reverse('map'))
        self.assertTemplateUsed(response, 'map.html')
    """
    def test_comAge_status_code(self):
        client = Client()
        response = self.client.get(reverse('comAge'))
        self.assertEqual(response.status_code, 200)

    def test_comAge_view(self):
        client = Client()
        response = self.client.get(reverse('comAge'))
        self.assertTemplateUsed(response, 'comAge.html')

    def test_topAndLowestRated(self):
        db = database(reset=False)
        self.assertEqual(len(db.topAndLowestRated()), 100)

    def test_bestHits(self):
        db = database(reset=False)
        self.assertEqual(len(db.bestHits()), 10)

    def test_teamAverageRating(self):
        db = database(reset=False)
        self.assertEqual(len(db.teamAverageRating()), 10)


# Create your tests here.
