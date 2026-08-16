from django.core.management.base import BaseCommand
import requests
from places.models import Place, PlaceImage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Загружает данные из json-файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        place_data = response.json()
        place_title = place_data['title']

        place, created = Place.objects.get_or_create(
            title=place_title,
            defaults={
                "description_short": place_data.get('description_short', ''),
                "description_long": place_data.get('description_long', ''),
                "lng": float(place_data['coordinates']['lng']),
                "lat": float(place_data['coordinates']['lat']),
            }
        )

        images_urls = place_data.get('imgs')
        for i, url in enumerate(images_urls):
            img_response = requests.get(url)
            filename = url.split('/')[-1]
            image = PlaceImage(place=place, position=i)
            image.place_image.save(filename, ContentFile(img_response.content), save=True)