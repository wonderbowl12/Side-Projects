# Twilio-Weather

Simple program that uses a weather API, creates a message, and sends it to you through text. 
Requires you to have a twilio account (free trial works) and a working phone number with texting enabled. 
The program also works without needing twilio, however, you would need to comment line 45 and change "print(message)" to "print(bodytest)".
>(message = twilioCli.messages.create(body=bodytest, from_=myTwilio, to=myNumber)). 


## API Used
http://api.openweathermap.org/

## Example input and output

>What city do you want the weather for? 
>**San Francisco**

>**Output** It is sunny with clear skies today. The temperature is 66 F with a max of 78 F and a min of 73 F





