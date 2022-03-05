import requests

API_KEY= "0eee8616c1bfc8dc57e312f3e79a9c3d"
BASE_URL= "http://api.openweathermap.org/data/2.5/weather"
city=input("Enter the City Name: ")

request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code==200:
    data=response.json()
    weather=data['weather'][0]['description']
    print("Weather: ", weather)

    temp=round(data["main"]['temp'] -273.15 ,2)
    print("Temperature:", temp, "celsius")

    humidity=data['main']['humidity']
    print("Humidity: ", humidity, '%')

    windsp=data['wind']['speed']
    drn=data['wind']['deg']
    print('windspeed: ', windsp, 'km/hour towords', drn, 'degree')


    #print(data)

else:
    print("An error occurred.")