import geopy.geocoders as Geocoder
from user_inputs import get_geocoder_from_user
from os import getcwd
import folium


def map_addresses_to_geolocation(addr_array: [], geocoder: Geocoder) -> []:
    """
    Maps array of string addresses to geopy geolocation.
    """
    # Create one string for each entry
    addresses = []
    for addr in addr_array:
        str_addr = ''
        for part in addr:
            try:
                str_addr += part + ' '
            except:
                # When part is 'NaN'
                str_addr += ' '
        addresses.append(str_addr)
    locations = []

    # Get geolocation from string
    for addr in addresses:
        locations.append(geocoder.geocode(addr))

    # Clear not found locations
    filtered_locations = []
    for i in range(0, len(locations)):
        loc = locations[i]
        if loc is not None:
            filtered_locations.append(loc)

    print('\nFound ' + str(len(filtered_locations)) + ' of ' + str(len(locations)) + ' locations.\n')
    return filtered_locations


def create_map(locations: []) -> None:
    """
    Create map with locations.
    """
    m = folium.Map(tiles='CartoDB Positron')
    for loc in locations:
        folium.Marker(location=[loc.latitude, loc.longitude]) \
            .add_to(m)
    m.save('out/world_map.html')


def get_geocoder() -> Geocoder:
    """
    Get geocoder type from user input.
    """
    string = get_geocoder_from_user()
    if string == 'bing':
        api_key = get_api_key_from_file()
        Geocoder.options.default_timeout = None  # Maybe critical
        geolocator = Geocoder.Bing(api_key=api_key)
    else:
        geolocator = Geocoder.Nominatim(user_agent="member_world_map")
    return geolocator


def get_api_key_from_file() -> str:
    """
    Reads API key from file.
    """
    file_name = getcwd() + '/api_key.txt'
    with open(file_name) as f:
        return f.readline()
