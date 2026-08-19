import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = 'Загружает данные из json-файла'


    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)


    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()

        place_data = response.json()
        place_title = place_data['title']
        coordinates = place_data.get('coordinates', {})

        place, created = Place.objects.get_or_create(
            title=place_title,
            defaults={
                "short_description": place_data.get('description_short', ''),
                "long_description": place_data.get('description_long', ''),
                "lng": coordinates.get('lng'),
                "lat": coordinates.get('lat'),
            }
        )

        if created:
            images_urls = place_data.get('imgs')
            for index, url in enumerate(images_urls):
                img_response = requests.get(url)
                img_response.raise_for_status()

                filename = url.split('/')[-1]
                place.images.create(
                    position=index,
                    image=ContentFile(img_response.content, name=filename)
                )
        else:
            return
