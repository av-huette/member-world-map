import csv_helper as csv_h
import geo_helper as geo_h
from user_inputs import get_number_of_csvs
from itertools import chain
import time
from threading import Thread

locations = []


def main():
    # Get inputs from user
    num_csvs = get_number_of_csvs()
    geolocator = geo_h.get_geocoder()

    # Collect csv files
    csvs = []
    for i in range(num_csvs):
        csvs.append(csv_h.read_csv())

    # Get geolocation from CSVs
    fetch_locations(csvs, geolocator)
    merged = list(chain(*locations))
    print('Total locations found: ' + str(len(merged)))

    # Apply locations to map
    geo_h.create_map(merged)


def fetch_locations(csvs: [], geolocator: geo_h.Geocoder) -> None:
    """
    Convert addresses from CSVs to geolocation and add to list using multiple threads.
    """
    print('Fetching locations...\n')
    start = time.time()
    threads = []
    chunks = csv_h.chunk_csvs(csvs)
    for chunk in chunks:
        threads.append(Thread(target=get_locations, args=(chunk, geolocator)))
    for thread in threads:
        thread.start()
        time.sleep(1)  # otherwise Bing couldn't handle amount of requests...
    for thread in threads:
        thread.join()
    end = time.time()
    print('Elapsed time: ' + str((end - start)) + ' seconds.\n')


def get_locations(address_chunk: [], geocoder: geo_h.Geocoder) -> None:
    """
    Convert addresses from CSVs to geolocation and add to list.
    """
    res = geo_h.map_addresses_to_geolocation(address_chunk, geocoder)
    locations.append(res)


if __name__ == "__main__":
    main()
