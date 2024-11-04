# weather_app/analyze_weather.py

def calculate_average_temperature(weather_data):
    """Calculate the average temperature from weather data of multiple cities."""
    total_temp = 0
    count = 0

    for city, data in weather_data.items():
        if data["temperature"] != "N/A":
            total_temp += data["temperature"]
            count += 1

    if count == 0:
        return None  # Return None if no valid temperatures were found

    return total_temp / count


def check_weather_trend(city_weather_data):
    """Analyze and return a weather trend message based on conditions."""
    condition = city_weather_data["condition"]

    if condition == "Sunny":
        return "The weather is clear. Enjoy your day!"
    elif condition == "Rainy":
        return "It looks rainy. Don't forget your umbrella!"
    elif condition == "Cloudy":
        return "It's cloudy. It might rain later."
    else:
        return "Weather data unavailable."
