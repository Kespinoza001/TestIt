import requests


def get_web_data(zip=None, city=None):
  baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
# api id for the site
apiid = "36b07b8d5230d52c7b4da0d20f4de5c8" 
# check if the user gave the zip code or the city name
if zip is not None:
# us at the end id for usa country , change it as required
  baseUrl += "&zip="+str(zip)+",us"
else:
  baseUrl += "&q="+str(city)+",us"
# Finally append the api id
baseUrl += "&appid="+str(apiid)
# Make get requests using the requests module
r = requests.get(baseUrl)
# return the response
return r
# Show data in a readable format

def display(resp):
# This means the request was successful
  if resp.status_code == 200:
    data = resp.json()
print(f"""{data['name']} Weather Forecast:
Type: {data['weather'][0]['description']}
Wind Speed : {data['wind']['speed']} miles/hr
Visibility : {data['visibility']} m
Min. Temp : {data['main']['temp_min']} F
Max Temp : {data['main']['temp_max']} F
""")
print("Request Failed, Error : ", resp.status_code)

def main():
  while True:
# ask the user for his/her choice
    choice = int(
input("How do you want to search ? :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))
if choice == 1:
# ask for zip code
  try:
# ask for zip code
    zCode = int(input("Enter zip code : "))
# get data from the website
except = get_web_data(zCode, None)
display(resp)
except Exception as ex:
print("Error : ", ex)
elif choice == 2:
try:
cname = input("Enter city name : ")
# Make call to get get_data
resp = get_web_data(None, cname)
display(resp)
except Exception as ex:
print("Error : ", ex)
elif choice == 3:
break
else:
print("Invalid Choice..\n")

if __name__ == "__main__":
main()