from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer


class BlogDetails(APIView):
    def get(self, request, pk=None):
        if pk:  # If pk is provided, retrieve a specific blog
            print(pk)
            try:
                blog = Blog.objects.get(pk=pk)
            except Blog.DoesNotExist:
                return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:
            # If no pk is provided, retrieve all blogs
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data(), status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            blog = BlogSerializer(pk=pk)
        except:
            return Response({ "error": "Blog not found" }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogSerializer(blog, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
