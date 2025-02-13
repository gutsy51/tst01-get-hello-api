from rest_framework.views import APIView
from rest_framework.response import Response


class APIHello(APIView):
    """Hello {name} API-view."""

    @staticmethod
    def get(request):
        """Return "Hello, {name}! {message}!" ("Helo World!" by default)."""
        name = request.GET.get('name', 'World')
        message = request.GET.get('message', None)
        response_text = f'Hello {name}!' + (f' {message}!' if message else '')
        return Response({'message': response_text})
