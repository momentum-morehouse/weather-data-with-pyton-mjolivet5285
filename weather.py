import requests
import matplotlib
print ("libraries imported")

#Grambling State 32° 31' 39.54" N, -92° 42' 50.54" W
#Beaumont,TX 30° 4' 55.1532'' N, 94° 7' 7.0932'' W
#Denver, CO 39° 44' 31.3548'' N, 104° 59' 29.5116'' W
#lodja DRC  3°31′27″S, 23°35′47″E
#Abidjan Ivory Coast 5° 18' 34.78" N, -4° 00' 45.58" W
#Banjul Gambia 13° 27' 9.86" N, -16° 34' 40.91" W
#WAU South Sudan 7.7011° N 27.9897° E
#Juarez, Chihuahua, Mexico 31° 44' 18.8916'' N, 106° 29' 13.2540'' W
#Medellin, Antioquia, Colombia 31° 44' 18.8916'' N, 106° 29' 13.2540'' W
#Morehouse, GA 33.7473° N, 84.4155° W


location = [("32° 31' 39.54N, -92° 42' 50.54W","30° 4' 55.1532N, 94° 7' 7.0932W","39° 44' 31.3548N, 104° 59' 29.5116W","3°31′27S, 23°35′47E","5° 18' 34.78N, -4° 00' 45.58W","13° 27' 9.86N, -16° 34' 40.91W","7.7011° N 27.9897° E","31° 44' 18.8916N, 106° 29' 13.2540W","31° 44' 18.8916N, 106° 29' 13.2540W","33.7473° N, 84.4155° W")]
print(location[(0])