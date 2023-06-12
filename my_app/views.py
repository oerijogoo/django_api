from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from my_app.models import Todo

class TodoView(APIView):
    def post(self, request):
        data = request.data.dict()
        todo = Todo(task=data['task'], completed=data['completed'])
        todo.save()
        return Response(200)

    def get(self, request):
        items = [(x.task, x.completed) for x in Todo.objects.all()]
        return Response(items)
