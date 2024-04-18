from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer

# Create your views here
class TodoListView(APIView):
    def post(self,request, *args, **kwargs):
         serializer = TodoSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def get(self, request, id=None):
      if id: 
         get_serializer = get_object_or_404(Todo, id=id)
         serializer = TodoSerializer(get_serializer)
         return Response(serializer.data)
      else:
          queryset = Todo.objects.all()
          read_serializer = TodoSerializer(queryset, many=True)
          return Response(read_serializer.data) 
        
    
    def patch(self, request, id):
        todo_item = get_object_or_404(Todo, id=id)
        update_serializer = TodoSerializer(todo_item, data=request.data, partial=True)
        if update_serializer.is_valid():
          update_serializer.save()
          return Response(update_serializer.data)
        return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
         todo_item = get_object_or_404(Todo, id=id)
         todo_item.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
          
       
          