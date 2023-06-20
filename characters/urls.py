from django.urls import path

from .views import get_random_character, CharacterListView

urlpatterns = [
    path("characters/random/", get_random_character, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list"),
]

app_name = "character"
