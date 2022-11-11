import urllib.request, urllib.parse, urllib.error
import json
import ssl


def alert_API_key():
    
    print('The program works with an API key, please enter your API key in server.py -> get_API_key()')
    if input('okay?: (Y/n) ') == 'Y': return True
    else: return False


def get_API_key():

    API_key = '' # Here your API key
    return API_key


def initialize_connection(API_key):
    
    url_service = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Returns a new context with secure default settings
    settings = ssl.create_default_context()
    settings.check_hostname = False
    settings.verify_mode = ssl.CERT_NONE
    
    return url_service, settings


# Search the string (place) in the data base of Google Maps and return the coordinate of that place.
def search_place(string_place, API_key, url_service, settings):

    information = {}
    information['address'] = string_place
    
    if API_key is not False: information['key'] = API_key
    geocode_url = url_service + urllib.parse.urlencode(information)

    HTTP_protocol_client = urllib.request.urlopen(geocode_url, context = settings)    
    final_data = HTTP_protocol_client.read().decode()
    
    try:
        results = json.loads(final_data)
    except:
        results = None
        
    if not results or 'status' not in results or results['status'] != 'OK':
        print('==== Falla ====')
        print(final_data)
    
    return results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng']