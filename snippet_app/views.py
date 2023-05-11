from rest_framework import generics
from .models import Snippet, Tag
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SnippetItemListCreate(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = SnippetSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = SnippetSerializer(queryset, many=True, context={'request': request})
        return Response({'count': queryset.count(), 'snippets': serializer.data})

class SnippetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    authentication_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]
    serializer_class = SnippetSerializer


    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)

        if response.status_code == 204:
            snippets = Snippet.objects.filter(created_user=request.user)
            return Response(SnippetSerializer(snippets, many=True).data)

        return response









    