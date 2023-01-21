from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Message
from app.serializers import MessageSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting notes'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def uploadMessage(request):
    data = request.data
    message = Message.objects.create(
        message=data
    )
    serializer = MessageSerializer(message, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def deleteMessage(request,pk):

    newMessage = {
        'message': 'This message is deleted',
        'deleted': True
    }

    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, message=newMessage['message'], partial=True)

    if(serializer.is_valid()):
        serializer.save()

    return Response('Message deleted')