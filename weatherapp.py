import requests
import json
#-------setting up inputs
import csv
import sys

#--changes will be made to search() to fit geocoding method.--

#input number you want to search
number = input('Enter number to find\n')
#reading from csv file
def search():
    cityInput = input("City name? (Capital required): ")
    stateInput = input("Please type in the city of the state? (Capital required): ")
    reader = csv.reader(open('us-area-code-cities.csv', encoding="utf8"))
    #better way to store these
    location = []
    ###
    latlong = []
    locLen = 0
    for row in reader:
        #print(row)
        if row[1] == cityInput:
            if row[2] == stateInput:
                #return the lat/long of the cities in a list
                #create a dictionary that holds the values
                location.append({'City': row[1], 'State': row[2]})
                latlong.append(row[4])
                latlong.append(row[5])
                return latlong
    if not latlong: 
        print("(user input) does not exist please check spelling of city name")
        return "Error"


#incomplete geocoding function from api to break off of csv file
def geoCode():
    apiRequest = "https://geocoding.geo.census.gov/geocoder/locations/address?street=4600+Silver+Hill+Rd&city=Washington&state=DC&zip=20233&benchmark=Public_AR_Census2020&format=json"
    #print(request)
    response = requests.get(apiRequest)
    #to check status code
    print(response.status_code)
    #to check returned json ,S
    #print(json.dumps(response.json(), indent=4, sort_keys = True))

#TODO 10/12/23
#setup formating for 5 day forcast from the json above.




#setting up grabbed user inputs
class weatherInput:
    def __init__(self, zipCode):
        self.zipCode = zipCode


#TODO: Fix with geocoding
#driver should later be able to take a zip code and find it that way instead of searching through csv file for a city name
def driver():
    #userAreaCode = input('Enter your Area/ZIP Code \n')
    #test = weatherInput(userAreaCode)
    #print(test.zipCode)
    #-------------------
    #start for later code formatting, should be getting values here instead of search() func
    #startInput = input('Enter your city name.')
    apiCalls('deprecatedName')

def apiCalls(apiInput):
    userSearch = search()
    if userSearch == "Error":
        print("err, please check your spelling.")
    else:
        print(userSearch)
        request = "https://api.openweathermap.org/data/2.5/forecast?lat=" + userSearch[0] +"&lon="+userSearch[1]+"&appid="
        #print(request)
        response = requests.get(request)
        #to check status code
        print(response.status_code)
        #to check returned json ,
        print(json.dumps(response.json(), indent=4, sort_keys = True))

driver()
#geoCode()