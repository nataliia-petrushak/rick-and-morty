import requests
from django.conf import settings
from django.db import IntegrityError

from .models import Character


def scrape_characters() -> list[Character]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_CHARACTERS_URL
    characters = []

    while next_url_to_scrape is not None:
        character_response = requests.get(next_url_to_scrape).json()
        for character in character_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
            )
        next_url_to_scrape = character_response["info"]["next"]
    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print(f"Character with api_id: {character.api_id} is already exist in DB!")


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
