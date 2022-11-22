from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class taskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class markedComplete(APIView):
    def get(self, request):
        tasks = Task.objects.get()
        serializer = TaskSerializer(tasks)
        for task in serializer.data:
            if task.status == 'complete':
                print(task)
                return Response(task)



# class completedTask(generics.ListAPIView):
#     serializer_class = TaskSerializer
#
#     def get_queryset(self):
#         status = self.request.status
#         return Task.objects.filter(status=status)


class deleteTask(APIView):
    def delete(self, request, pk):
        tasks = Task.objects.get(pk=pk)
        tasks.delete()
        return Response("Task Deleted")
