
import googlemaps
from datetime import datetime

# just a note, for looking up directions the maps only consider commercial vehicles 
# and no provision is made of yet for low bridge restrictions under 13 feet or 11 1/2 feet

# the following code chooses which channel of the API to use: beta or weekly, quarterly... etc
# <script async
#    src="https://maps.googleapis.com/maps/api/js?v=beta
#        &key=YOUR_API_KEY&callback=initMap">
# </script>

# or choose the direct version number 3.49
# <script async
#     src="https://maps.googleapis.com/maps/api/js?v=3.49
#         &key=YOUR_API_KEY&callback=initMap">
# </script>

# deployment from Castle is working around the clock to implement the hotfix
# want to steer clear of American Thanksgiving

# update, still needed to install runtimeInstaller in order for the maps to load
# when doing Route Modelling, the webView2 runs 6 instances with 1 instance of Trux open
# will need to open a ticket concerning performance


gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('160055 Jordensen Dr, Mississauga, ON')

# Look up an address with reverse geocoding
# as usual, lattitude comes first, then longitude
reverse_geocode_result = gmaps.reverse_geocode((43.674224, -79.801452))

# Request directions via public transit
# using public transit, test directions cross continent
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


