import openai
from dotenv import load_dotenv
load_dotenv()
import os
import requests
openai.api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def prepCoordinates(prompt):
    message = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"You are a tourguide for the city of Ann Arbor, Michigan. Your job is to take the users prompt and output the location that is the subject in that prompt. Do not included anything else other than the location, Ann Arbor, MI. IF You do not know what the location is in Ann Arbor, still output the location, Ann Arbor, MI.'"},
            {"role":"user", "content":"Find me parking spots near Ross. ONLY OUTPUT location, Ann Arbor, MI"},
            {"role":"assistant", "content":"Ross School of Business, Ann Arbor, MI"},
            {"role":"user", "content":"spots near Diag, ONLY OUTPUT location, Ann Arbor, MI"},
            {"role":"assistant", "content":"The Diag, Ann Arbor, MI"},
            {"role":"user", "content":"spots near the big house, ONLY OUTPUT location, Ann Arbor, MI"},
            {"role":"assistant", "content":"Michigan Stadium, Ann Arbor, MI"},
            {"role":"user", "content":"near Aventura"},
            {"role":"assistant", "content":"Aventura, Ann Arbor, MI"},
            {"role":"user", "content":"Joes"},
            {"role":"assistant", "content":"Joes, Ann Arbor, MI"},
            {"role":"user", "content":prompt}
        ],
    )
    print(message.choices[0].message.content)
    return message.choices[0].message.content
def findCoordinates(location):
    params = {
        'key': API_KEY,
        'address': location
    }
    print(location)
    baseUrl  = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(baseUrl, params=params).json()
    response.keys()
    print(response)
    if response['results'][0]['address_components'][0]['long_name'] == "Ann Arbor":
        return False
    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lng = geometry['location']['lng']
        return (lat, lng)
    else:
        return None

