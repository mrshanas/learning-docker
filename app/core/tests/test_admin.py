from django.urls import reverse
from django.test import Client,TestCase
from django.contrib.auth import get_user_model

class AdminTests(TestCase):
    """Admin site tests"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mrshanas.com',
            password='mrshanas'
        )
        self.client.force_login(self.admin_user)


    def test_admin_display_users(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res,'email')
        self.assertEqual(res.status_code,200)