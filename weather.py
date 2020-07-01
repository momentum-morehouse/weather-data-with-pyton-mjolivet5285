import requests

location = [(32.5266111,-92.72111,'Grambling State'),(30.0347413, -94.0837193,'5285,Tx'),(39.7596001, -105.0051894,'5 points, CO'),(-3.5158183, 23.565759,'lodja,DRC'),(5.3487761, -4.1197526,'Abidjan Ivory Coast'),(13.4523699, -16.5892536,'Banjul Gambia'),(7.7021853,27.9569428,'WAU, South Sudan'),(31.4522961,-106.8464473,'Juarez,Chihuahua,Mexico'),(6.2443695,-75.6512523,'Medellin,Antioquia,Colombia'),(33.7450668, -84.4159317,'Morehouse, GA')]
#Grambling 32° 31' 39.54" N, -92° 42' 50.54" W
#5285,TX 30° 4' 55.1532'' N, 94° 7' 7.0932'' W
#5 points, CO 39° 44' 31.3548'' N, -105.0051894'' W
#lodja DRC  3°31′27″S, 23°35′47″E
#Abidjan Ivory Coast 5° 18' 34.78" N, -4° 00' 45.58" W
#Banjul Gambia 13° 27' 9.86" N, -16° 34' 40.91" W
#WAU South Sudan 7.7011° N 27.9897° E
#Juarez, Chihuahua, Mexico 31° 44' 18.8916'' N, 106° 29' 13.2540'' W
#Medellin, Antioquia, Colombia 6.2443695, -75.6512523
#Morehouse, GA 33.7473° N, 84.4155° W

key = "OPEkCl6kVz1sIOhKeGcpPTv5ZyIZ80NA"


def create_placelist(place_list):
  places = []
  for city in place_list:
    place = (city[0], city[1], city[2])
    places.append(place)
  print(places)
  return places


places = create_placelist(location)
  

def get_weather(locations):

  url='https://api.climacell.co/v3/weather/realtime'

  for location in locations:

    payload = {
      "apikey": key, 
      "lat": location[0],
      "lon": location[1]
    }

    response = requests.get(url, params=payload).json()

    print(location[2],response["precipitation"])

get_weather(places)