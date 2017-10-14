import datetime
import json
import os
import requests

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
STATUS_FILE = os.path.join(DIR_PATH, 'statuses', 'stat_{}.json')
INFO_FILE = os.path.join(DIR_PATH, 'infos', 'info_{}.json')

def grab_station_status(datetime_chunk):
    url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status'
    print('Grabbing station status')
    resp = requests.get(url)
    with open(STATUS_FILE.format(datetime_chunk), 'w') as file_open:
        json.dump(resp.json(), file_open)

def grab_station_information(date_chunk):
    url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information'
    print('Grabbing station information')
    resp = requests.get(url)
    with open(INFO_FILE.format(date_chunk), 'w') as file_open:
        json.dump(resp.json(), file_open)

if __name__ == '__main__':
    datetime_chunk = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    date_chunk = datetime.datetime.now().strftime('%Y%m%d')
    grab_station_status(datetime_chunk)
    if not os.path.exists(INFO_FILE.format(date_chunk)):
        grab_station_information(date_chunk)