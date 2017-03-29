from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('myuser-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)})
