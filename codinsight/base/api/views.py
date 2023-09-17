from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room

@api_view(['GET'])
def getRoutes(req):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
# safe allow this to be more than python dictionary. 

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) 
    # many means the variable passed into the Serializer could be multiple objects.
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) 
    
    return Response(serializer.data)
