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
    Expected to recieve language requet in format: {Language: Language Name}.
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
    '''
    try:
        data = request.data

        if data['language'] == 'Python':
            output = run.Python(code=data['code'], inputString=data['input'])
        elif data['language'] == 'Java':
            output = run.Java(code=data['code'], inputString=data['input'])
        elif data['language'] == 'Cpp':
            output = run.Cpp(code=data['code'], inputString=data['input'])
        elif data['language'] == 'C':
            output = run.C(code=data['code'], inputString=data['input'])
        elif data['language'] == 'Dart':
            output = run.Dart(code=data['code'], inputString=data['input'])
        elif data['language'] == 'Golang':
            output = run.Golang(code=data['code'], inputString=data['input'])
    except Exception as e:
        output = e
    finally:
        return Response(status=status.HTTP_200_OK, data={'output': output})
