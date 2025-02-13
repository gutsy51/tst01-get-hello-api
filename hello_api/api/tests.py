from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTests(TestCase):
    """Test API Hello GET request."""

    def test_hello_view(self):
        """Test hello view with name and message."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name=Name&message=Message')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello Name! Message!'})

    def test_hello_view_no_params(self):
        """Test hello view without any params."""
        client = Client()
        response = client.get(reverse('hello-api'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello World!'})
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_hello_view_no_message(self):
        """Test hello view with only message param."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name=Name')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello Name!'})
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_hello_view_no_name(self):
        """Test hello view with only name param."""
        client = Client()
        response = client.get(reverse('hello-api') + '?message=Message')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello World! Message!'})
        self.assertEqual(response['Content-Type'], 'application/json')
