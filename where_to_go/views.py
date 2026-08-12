from django.shortcuts import render
from django.templatetags.static import static


def where_to_go(request):
    places_geojson = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": static('/places/moscow_legends.json')
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": static('/places/roofs24.json')
          }
        }
      ]
    }
    context = {
        'places_geojson': places_geojson
    }
    return render(request, 'index.html', context=context)