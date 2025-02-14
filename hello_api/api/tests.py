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

    def test_hello_view_empty_params(self):
        """Test hello view with empty name and message params."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name=&message=')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello !'})

    def test_hello_view_whitespace_params(self):
        """Test hello view with whitespace in name and message params."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name=  Name  &message=  Message  ')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello   Name  !   Message  !'})

    def test_hello_view_html_tags(self):
        """Test hello view with HTML tags in name and message params."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name=<script>Name</script>&message=<b>Message</b>')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello <script>Name</script>! <b>Message</b>!'})

    def test_hello_view_long_params(self):
        """Test hello view with long name and message params."""
        long_name = 'A' * 1000
        long_message = 'B' * 1000
        client = Client()
        response = client.get(reverse('hello-api') + f'?name={long_name}&message={long_message}')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': f'Hello {long_name}! {long_message}!'})

    def test_hello_view_missing_param_values(self):
        """Test hello view with missing values for name and message params."""
        client = Client()
        response = client.get(reverse('hello-api') + '?name&message')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello !'})

    def test_hello_view_invalid_params(self):
        """Test hello view with invalid params."""
        client = Client()
        response = client.get(reverse('hello-api') + '?invalid_name=Name&invalid_message=Message')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Hello World!'})

    def test_hello_view_post_request(self):
        """Test hello view with POST request."""
        client = Client()
        response = client.post(reverse('hello-api'), {'name': 'Name', 'message': 'Message'})
        self.assertEqual(response.status_code, 403)  # Method Not Allowed
