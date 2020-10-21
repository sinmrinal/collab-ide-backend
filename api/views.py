from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
import json
from . import run


@api_view(['POST'])
def boilerPlate(request):
    '''
    Returns Boilerplate Code for requested language.
    Expected to recieve language request in format: {Language: Language Name}.
    '''
    try:
        with open('./api/boilerPlate.json') as file:
            boilerPlateCode = json.load(file)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'details': 'Couldn\'t found boilerplate Codes'})

    if 'language' in request.data:
        if request.data['language'] in boilerPlateCode:
            data = {'language': request.data['language'],
                    'boilerPlate': boilerPlateCode[request.data['language']]}
            return Response(status=status.HTTP_200_OK, data=data)
        else:
            return Response(status=status.HTTP_417_EXPECTATION_FAILED, data={'details': 'Language not supported.'})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'details': 'Didn\'t recieve any language in request.'})


@api_view(['POST'])
def compile(request):
    '''
    Expects a language, input and code to run.
    Responds with Output of the code.
    '''
    if 'language' not in request.data:
        output = 'Select a language!'
    else:
        if request.data['language'] == 'Python':
            output = run.Python(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Java':
            output = run.Java(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'C++':
            output = run.Cpp(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'C':
            output = run.C(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Dart':
            output = run.Dart(code=request.data['code'], inputString=request.data['input'])
        elif request.data['language'] == 'Golang':
            output = run.Golang(code=request.data['code'], inputString=request.data['input'])
        else:
            output = request.data
    
    return Response(status=status.HTTP_200_OK, data={'output': output})
