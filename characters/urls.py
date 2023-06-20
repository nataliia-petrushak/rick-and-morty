from django.urls import path

from .views import get_random_character

urlpatterns = [
    path("characters/random/", get_random_character, name="character-random")
]

app_name = "character"
