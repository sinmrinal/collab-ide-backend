from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
import json
from . import execute


@api_view(['GET'])
def boilerPlate(request, language):
    '''
    Returns Boilerplate Code for requested language.
    Expected to recieve language request in format: {Language: Language Name}.
    '''
    try:
        with open('./api/boilerPlate.json') as file:
            boilerPlateCode = json.load(file)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'details': 'Couldn\'t found boilerplate Codes'})

    if language in boilerPlateCode:
        data = {'language': language,
                'boilerPlate': boilerPlateCode[language]}
        return Response(status=status.HTTP_200_OK, data=data)
    else:
        return Response(status=status.HTTP_417_EXPECTATION_FAILED, data={'boilerPlate': 'Language not supported.'})


@api_view(['POST'])
def compile(request):
    '''
    Expects a language, input and code to execute.
    Responds with Output of the code.
    '''
    if 'language' not in request.data:
        output = 'Select a language!'
    else:
        if request.data['language'] == 'Python':
            output = execute.Python(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Java':
            output = execute.Java(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'C++':
            output = execute.Cpp(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'C':
            output = execute.C(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Dart':
            output = execute.Dart(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Golang':
            output = execute.Golang(code=request.data['code'], inputString=request.data['input'])
        else:
            output = request.data
    
    return Response(status=status.HTTP_200_OK, data={'output': output})


async def websocket_view(socket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(message)