"""
Tests for Users API endpoints
"""
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('user:create')

class PublicUserApiTests(TestCase):
    """Users Public Api tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test if users are created successfully"""
        data = {
            'email':'test@example.com',
            'password':'mrshanas',
            'name':'Test User'
        }
        res = self.client.post(CREATE_USER_URL,data)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)

