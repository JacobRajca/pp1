temperature = int(input('Enter temperature in Celsius: ')) #collect temperature from keyboard
temperatureInK = temperature + 273.15 #calculate from Celsius to Kelvin (Celsius + 273.15)
temperatureInF = (temperature*(9/5))+32 #calculate from Celsius to Fahrenheit
print(f"Your temperature is {temperature}°C, which is equal to {temperatureInK} Kelvins and {temperatureInF}°F")