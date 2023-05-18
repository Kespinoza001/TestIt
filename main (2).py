# import required libraries
import requests
import json

# define the main function
def main():
    # display welcome message
    print("Welcome to the weather forecast program!")
    
    # define a flag for validation
    valid_input = False
    
    # continue to loop until valid input is provided
    while not valid_input:
        # prompt the user to enter a city name or zip code
        user_input = input("Please enter a city name or zip code: ")
        
        # check if the input is a zip code
        if user_input.isnumeric() and len(user_input) == 5:
            # set the flag to true and call the get_weather_data function
            valid_input = True
            get_weather_data(zip_code=user_input)
            
        # check if the input is a city name
        elif user_input.isalpha():
            # set the flag to true and call the get_weather_data function
            valid_input = True
            get_weather_data(city_name=user_input)
            
        # if the input is invalid, display an error message
        else:
            print("Invalid input. Please enter a valid city name or zip code.")

# define a function to get weather data based on zip code or city name
def get_weather_data(zip_code=None, city_name=None):
    # set up the URL for the API request
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # add the zip code or city name to the URL
    if zip_code is not None:
        url = f"{base_url}zip={zip_code}&appid=YOUR_APP_ID"
    else:
        url = f"{base_url}q={city_name}&appid=YOUR_APP_ID"
        
    try:
        # make the API request and parse the response
        response = requests.get(url)
        data = json.loads(response.text)
        
        # extract the relevant weather data
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        # display the weather forecast to the user
        print(f"The weather forecast for {city_name or zip_code} is:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature} Kelvin")
        print(f"Humidity: {humidity}%")
        
    except:
        # display an error message if the API request fails
        print("Sorry, an error occurred while retrieving weather data.")

# call the main function
if __name__ == "__main__":
    main()