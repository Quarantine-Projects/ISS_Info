import requests
import json

def iss_people_in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code == 200:
        data = json.dumps(response.json(), sort_keys=True)
        output = json.loads(data)
    else:
        return response.status_code
    return output

def iss_current_loc():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        data = json.dumps(response.json())
        output = json.loads(data)
    else:
        return response.status_code
    return output

def iss_passes(lat,lon,alt=None,n=None):
    parameters = {
    "lat": lat,
    "lon": lon,
    "alt": alt,
    "n": n
    }
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    if response.status_code == 200:
        data = json.dumps(response.json())
        output = json.loads(data)
    else:
        return response.status_code
    return output
