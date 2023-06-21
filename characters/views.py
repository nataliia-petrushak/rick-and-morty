from random import choice

from django.db.models import QuerySet
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Character
from .serializers import CharacterSerializer


@extend_schema(
    responses={status.HTTP_200_OK: CharacterSerializer},
)
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get random character from Rick & Marty world"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)

    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter by name insensitive contains",
                required=False,
                type=str,
            )
        ],
    )
    def get(self, request, *args, **kwargs) -> Response:
        """List characters with filter by name"""
        return super().get(request, *args, **kwargs)
