from twilio.rest import Client
import requests
import sys

# Twilio information
accountSID = '...'
authToken = '...'
twilioCli = Client(accountSID, authToken)
myNumber = '...'
myTwilio = '...'

# Grabbing JSON data
try:
    city = input('What city do you want the weather for? ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=212ed8bcccde8a2e843d021fafa10620'.format(city)
    rb = requests.get(url).json()
    # Temperature
    temperature = int(rb['main']['feels_like'])
    temp = str(int((temperature - 273) * (9 / 5) + 32)) + ' F'
    # Weather
    genre = ['rainy', 'cloudy', 'smoky', 'clear', 'sunny', 'misty']
    advices = ['How nice.', 'Bring a coat or something.', 'Bring some sunglasses.', 'Stay inside maybe?']
    weather = rb['weather'][0]['main']
    # Description
    descrip = rb['weather'][0]['description']
    # Max and Min weather
    max = str(int((rb['main']['temp_max'] - 273) * (9 / 5) + 32)) + ' F'
    min = str(int((rb['main']['temp_min'] - 273) * (9 / 5) + 32)) + ' F'
    # Creating the messages
    template = 'It is {} with ' + descrip + ' in {} today. The temperature is ' + temp + ' with a max of ' + max + ' and a min of ' + min + '.'

    global bodytest
    if weather == 'Clouds':
        bodytest = template.format('cloudy', city, advices[1])
    elif weather == 'Rain':
        bodytest = template.format('raining', city, advices[3])
    elif weather == 'Smoke':
        bodytest = template.format('smokey', city, '3')
    elif weather == 'Sunny':
        bodytest = template.format(weather, city, advices[2])
    else:
        bodytest = template.format(weather, city, advices[0])
    # Sending message

    message = twilioCli.messages.create(body=bodytest, from_=myTwilio, to=myNumber)
    print(bodytest)

except:
    print("Error", sys.exc_info()[0], 'occured, please try again.\n')