# Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

'''
This function converts temperature kelvin to celsius, or celsius to kelvin.
:Param 'temperature': celsius or kelvin | integer or float
:Return 'temperature': celsius or kelvin | float
'''

# Contoh penggunaan fungsi
temperature_kelvin = 300
temperature_celsius = kelvin_to_celsius(temperature_kelvin)
print(f"{temperature_kelvin} Kelvin = {temperature_celsius} Celsius")

temperature_celsius = 78.0
temperature_kelvin = celsius_to_kelvin(temperature_celsius)
print(f"{temperature_celsius} Celsius = {temperature_kelvin} Kelvin")




# Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
# Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin.
# Panggil function yang pertama jika diperlukan.

def convert_from_fahrenheit(temperature, unit):

	'''
	This function to converts temperature from Fahrenheit to Celsius or Kelvin.
	:Param 'temperature': temperature in Fahrenheit | float
        :Param 'unit': "celsius" or "kelvin" | string
	:Return 'temperature': converts temperature to kelvin or celsius | float
	'''

    if unit.lower() == "celsius":
        celsius = (temperature - 32) * 5/9
        return celsius
    elif unit.lower() == "kelvin":
        celsius = (temperature - 32) * 5/9
        kelvin = celsius + 273.15
        return kelvin
    else:
        print("Error. Masukkan suhu 'celsius' atau 'kelvin'.")


# Contoh penggunaan fungsi

temperature_fahrenheit = 99
celsius_temperature = convert_from_fahrenheit(temperature_fahrenheit, "celsius")
print(f"{temperature_fahrenheit} Fahrenheit = {celsius_temperature} Celsius")

temperature_fahrenheit = 47.43
kelvin_temperature = convert_from_fahrenheit(temperature_fahrenheit, "kelvin")
print(f"{temperature_fahrenheit} Fahrenheit = {kelvin_temperature} Kelvin")




# Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
# Berikan argumen untuk memastikan bahwa outputnya adalah celcius atau kelvin.

def convert_from_fahrenheit(temperature, target_unit):

	'''
	This function to converts temperature from Fahrenheit to Celsius or Kelvin.
        :Param 'temperature': temperature in Fahrenheit | float
        :Param 'target_unit': temperature, "celsius" or "kelvin" | string
	:Returns 'temperature': converts temperature to kelvin or celsius | float
	'''

    if target_unit.lower() == "celsius":
        celsius = (temperature - 32) * 5/9
        return celsius
    elif target_unit.lower() == "kelvin":
        celsius = (temperature - 32) * 5/9
        kelvin = celsius + 273.15
        return kelvin
    else:
        print("Error. Masukkan suhu 'celsius' atau 'kelvin'.")

# Contoh penggunaan fungsi

temperature_fahrenheit = 123
celsius_temperature = convert_from_fahrenheit(temperature_fahrenheit, "celsius")
print(f"{temperature_fahrenheit} Fahrenheit = {celsius_temperature} Celsius")

temperature_fahrenheit = 97.33
kelvin_temperature = convert_from_fahrenheit(temperature_fahrenheit, "kelvin")
print(f"{temperature_fahrenheit} Fahrenheit = {kelvin_temperature} Kelvin")