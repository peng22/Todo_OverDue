from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date
from rest_framework.test import APIClient
from .models import Task
# Create your tests here.
class PostApiTestCase(TestCase):
    def setUp(self):
        self.u1 = get_user_model().objects.create_user(
                username="test", password="password"
                )
        self.u2 = get_user_model().objects.create_user(
                username="test2@example.com", password="password2"
                )
        posts = [
            Task.objects.create(
                owner=self.u1,
                due_date=date.today(),
                name="Task 1 Name",
                status="assigned",
            ),
            Task.objects.create(
                owner=self.u2,
                due_date=date.today(),
                name="Task 2 Name",
                status="assigned",
                ),

        ]
        self.post_lookup = {p.id: p for p in posts}
        # override test client
        self.client = APIClient()
        self.client.login(username='test', password='password')

    def test_post_list(self):
        resp = self.client.get("/tasks/")
        data = resp.json()
        self.assertEqual(len(data), 1)
