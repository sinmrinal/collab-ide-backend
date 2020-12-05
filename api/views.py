import json
from uuid import uuid4

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import execute
from .models import RoomInfo


@api_view(['GET'])
def boiler_plate(request, language: str) -> Response:
    """
    Expected to receive language request in format: {Language: Language Name}.
    Returns Boilerplate Code for requested language.
    :param request: WSGIRequest
    :param language: str
    :return: HttpResponse
    """
    try:
        with open('./api/boilerPlate.json') as file:
            boiler_plate_code = json.load(file)
    except OSError:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={'details': 'Boilerplate codes unavailable.'})

    if language in boiler_plate_code:
        data = {'language': language,
                'boilerPlate': boiler_plate_code[language]}
        return Response(status=status.HTTP_200_OK, data=data)
    else:
        return Response(status=status.HTTP_417_EXPECTATION_FAILED, data={'boilerPlate': 'Language not supported.'})


@api_view(['POST'])
def compile_code(request) -> Response:
    """
    Expects a language, input and code to execute.
    Responds with Output of the code.
    :param request: WSGIRequest
    :return: HttpResponse
    """
    if 'language' not in request.data:
        output = 'Select a language!'
    else:
        if request.data['language'] == 'Python':
            output = execute.python(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'Java':
            output = execute.java(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'CPP':
            output = execute.cpp(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'C':
            output = execute.c(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'Dart':
            output = execute.dart(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'Go':
            output = execute.golang(code=request.data['code'], input_string=request.data['input'])
        elif request.data['language'] == 'Rust':
            output = execute.rust(code=request.data['code'], input_string=request.data['input'])
        else:
            output = "Select a language first."

    return Response(status=status.HTTP_200_OK, data={'output': output})


@api_view(['POST'])
def create_room(request):
    """
    Creates new room with given name and creator name.
    Returns Newly created room details.
    :param request: WSGIRequest
    :return: HttpResponse
    """
    data = request.data
    if 'roomName' and 'admin' in data:
        room_name = data['roomName']
        admin = data['admin']
        room = RoomInfo()
        room.ID = uuid4()
        room.name = room_name
        room.created_by = admin
        room.joined_by = admin
        room.save()
        response = {'ID': room.ID, 'name': room.name, 'created_by': room.created_by}
        return Response(status=status.HTTP_201_CREATED, data=response)
    else:
        return Response(status=status.HTTP_417_EXPECTATION_FAILED, data=data)


@api_view(['POST'])
def join_room(request) -> Response:
    """
    Checks if room is available with given ID.
    Returns Room details.
    :param request: WSGIRequest
    :return: HttpResponse
    """
    data = request.data
    if 'roomID' and 'name' in data:
        room_id = data['roomID']
        name = data['name']
        room_detail = RoomInfo.objects.filter(ID=room_id)
        if room_detail:
            room_detail = room_detail.get()
            users = str(room_detail.joined_by) + f",{name}"
            RoomInfo.objects.filter(ID=room_id).update(joined_by=users)
            response = {'ID': room_detail.ID, 'name': room_detail.name, 'created_by': room_detail.created_by,
                        'joined_by': [i for i in users.split(",")]}
            return Response(status=status.HTTP_200_OK, data=response)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT, data={"error": "Room of this is is not available."})
    else:
        return Response(status=status.HTTP_417_EXPECTATION_FAILED, data=data)
