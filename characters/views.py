from random import choice

from django.views import generic
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Character
from .serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)

    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generic.)
