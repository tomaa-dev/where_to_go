import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загружает данные из json-файла'


    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)


    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        place_data = response.json()
        place_title = place_data['title']
        coordinates = place_data.get('coordinates', {})

        place, created = Place.objects.get_or_create(
            title=place_title,
            defaults={
                "description_short": place_data.get('description_short', ''),
                "description_long": place_data.get('description_long', ''),
                "lng": coordinates.get('lng', 0),
                "lat": coordinates.get('lat', 0),
            }
        )

        if created:
            images_urls = place_data.get('imgs')
            for index, url in enumerate(images_urls):
                img_response = requests.get(url)
                filename = url.split('/')[-1]
                place.images.create(
                    position=index,
                    image=ContentFile(img_response.content, name=filename)
                )
        else:
            return
