
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('160055 Jordensen Dr, Mississauga, ON')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((43.674224, -79.801452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


