from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def where_to_go(request):
    places = Place.objects.all()
    
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": f"place_{place.id}",
                "detailsUrl": reverse('place_detail_api', args=[place.id])
            }
        })

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        'places_geojson': places_geojson
    }
    return render(request, 'index.html', context=context)


def place_detail_api(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)

    image_urls = [img.image.url for img in place.images.all()]

    place_data = {
        "title": place.title,
        "imgs": image_urls,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(
        place_data, 
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )