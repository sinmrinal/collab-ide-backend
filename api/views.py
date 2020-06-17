from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
import json


@api_view(['POST'])
def boilerPlate(request):
    print(request.user)

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
            data = {'language': request.data['language'], 'boilerPlate': boilerPlateCode[request.data['language']]}
            return Response(status=status.HTTP_200_OK, data=data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'details': 'Language not supported.'})
    else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'details': 'Didn\'t recieve any language in request.'})

@api_view(['POST'])
def compile(request):
    '''
    '''
