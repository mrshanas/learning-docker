"""
Test for User model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test for creating users with emails"""
        email = "shanas@example.com"
        password = "mrshanas"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for checking if emails are normalized"""
        sample_emails = [
            ['test1@Example.com','test1@example.com'],
            ['shanas@EXAMPLE.COM','shanas@example.com'],
            ['user@eXample.COM','user@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email,'mrshanas'
            )
            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raises_error(self):
        """Test that raises ValueError if user is created without email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','mrshanas')

    def test_create_superuser_successfully(self):
        """Test for creating superusers"""
        superuser = get_user_model().objects.create_superuser(
            'mrshanas@example.com',
            'mrshanas'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)