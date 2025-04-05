import streamlit as st

st.title("Unit Converter App")
st.markdown("##### Convert between different units of measurement.")
st.write("Welcome! If you need to convert units, you're in the right place 🙌")

# Dropdown for categories
category = st.selectbox("Select a category", [
    "Length", "Weight", "Time", "Temperature", "Area", "Volume", 
    "Speed", "Pressure", "Energy", "Power", "Data Storage", 
    "Currency", "Angle", "Frequency", "Electricity", "Magnetism", 
    "Sound", "Light", "Radiation", "Chemistry", "Physics", "Mathematics"
])

# Dynamically show unit options based on category
if category == "Length":
    unit = st.selectbox("Select a unit", ["Kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters"])
elif category == "Weight":
    unit = st.selectbox("Select a unit", ["Kilograms to pounds", "Pounds to kilograms", "Grams to ounces", "Ounces to grams"])
elif category == "Time":
    unit = st.selectbox("Select a unit", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hours", "Hours to minutes",
        "Hours to days", "Days to hours",
        "Days to weeks", "Weeks to days"
    ])
elif category == "Temperature":
    unit = st.selectbox("Select a unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
elif category == "Area":
    unit = st.selectbox("Select a unit", ["Square meters to square feet", "Square feet to square meters", "Hectares to acres", "Acres to hectares"])
elif category == "Volume":
    unit = st.selectbox("Select a unit", [
        "Liters to gallons", "Gallons to liters",
        "Milliliters to fluid ounces", "Fluid ounces to milliliters",
        "Cubic meters to cubic feet", "Cubic feet to cubic meters"
    ])
elif category == "Speed":
    unit = st.selectbox("Select a unit", ["km/h to mph", "mph to km/h", "m/s to km/h", "km/h to m/s"])
elif category == "Pressure":
    unit = st.selectbox("Select a unit", ["Pascals to psi", "psi to Pascals", "Atmospheres to Pascals", "Pascals to Atmospheres"])
elif category == "Energy":
    unit = st.selectbox("Select a unit", ["Joules to calories", "Calories to joules", "kWh to Joules", "Joules to kWh"])
elif category == "Power":
    unit = st.selectbox("Select a unit", ["Watts to horsepower", "Horsepower to watts", "kW to BTU/h", "BTU/h to kW"])
elif category == "Data Storage":
    unit = st.selectbox("Select a unit", [
        "Bytes to kilobytes", "Kilobytes to bytes",
        "Kilobytes to megabytes", "Megabytes to kilobytes",
        "Megabytes to gigabytes", "Gigabytes to megabytes",
        "Gigabytes to terabytes", "Terabytes to gigabytes"
    ])
elif category == "Currency":
    unit = st.selectbox("Select a unit", ["USD to EUR", "EUR to USD", "USD to GBP", "GBP to USD"])
elif category == "Angle":
    unit = st.selectbox("Select a unit", ["Degrees to radians", "Radians to degrees", "Degrees to gradians", "Gradians to degrees"])
elif category == "Frequency":
    unit = st.selectbox("Select a unit", ["Hertz to kilohertz", "Kilohertz to hertz", "Megahertz to gigahertz", "Gigahertz to megahertz"])
elif category == "Electricity":
    unit = st.selectbox("Select a unit", ["Volts to millivolts", "Millivolts to volts", "Amps to milliamps", "Milliamps to amps"])
elif category == "Magnetism":
    unit = st.selectbox("Select a unit", ["Tesla to gauss", "Gauss to tesla", "Oersted to ampere/meter", "Ampere/meter to oersted"])
elif category == "Sound":
    unit = st.selectbox("Select a unit", ["Decibels to bels", "Bels to decibels", "Sound pressure level (dB to Pa)", "Pa to dB"])
elif category == "Light":
    unit = st.selectbox("Select a unit", ["Lumens to lux", "Lux to lumens", "Candela to lumen", "Lumen to candela"])
elif category == "Radiation":
    unit = st.selectbox("Select a unit", ["Sievert to rem", "Rem to sievert", "Gray to rad", "Rad to gray"])
elif category == "Chemistry":
    unit = st.selectbox("Select a unit", ["Moles to molecules", "Molecules to moles", "Molarity to molality", "Molality to molarity"])
elif category == "Physics":
    unit = st.selectbox("Select a unit", ["Newtons to pound-force", "Pound-force to newtons", "Joules to electronvolts", "Electronvolts to joules"])
elif category == "Mathematics":
    unit = st.selectbox("Select a unit", ["Decimal to binary", "Binary to decimal", "Decimal to hexadecimal", "Hexadecimal to decimal"])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0)

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084
    
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        elif unit == "Grams to ounces":
            return value * 0.035274
        elif unit == "Ounces to grams":
            return value / 0.035274
    
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        elif unit == "Days to weeks":
            return value / 7
        elif unit == "Weeks to days":
            return value * 7
    
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
    
    elif category == "Area":
        if unit == "Square meters to square feet":
            return value * 10.764
        elif unit == "Square feet to square meters":
            return value / 10.764
        elif unit == "Hectares to acres":
            return value * 2.471
        elif unit == "Acres to hectares":
            return value / 2.471
    
    elif category == "Volume":
        if unit == "Liters to gallons":
            return value * 0.264172
        elif unit == "Gallons to liters":
            return value / 0.264172
        elif unit == "Milliliters to fluid ounces":
            return value * 0.033814
        elif unit == "Fluid ounces to milliliters":
            return value / 0.033814
        elif unit == "Cubic meters to cubic feet":
            return value * 35.3147
        elif unit == "Cubic feet to cubic meters":
            return value / 35.3147
    
    elif category == "Speed":
        if unit == "km/h to mph":
            return value * 0.621371
        elif unit == "mph to km/h":
            return value / 0.621371
        elif unit == "m/s to km/h":
            return value * 3.6
        elif unit == "km/h to m/s":
            return value / 3.6
    
    elif category == "Pressure":
        if unit == "Pascals to psi":
            return value * 0.000145038
        elif unit == "psi to Pascals":
            return value / 0.000145038
        elif unit == "Atmospheres to Pascals":
            return value * 101325
        elif unit == "Pascals to Atmospheres":
            return value / 101325
    
    elif category == "Energy":
        if unit == "Joules to calories":
            return value * 0.239006
        elif unit == "Calories to joules":
            return value / 0.239006
        elif unit == "kWh to Joules":
            return value * 3600000
        elif unit == "Joules to kWh":
            return value / 3600000
    
    elif category == "Power":
        if unit == "Watts to horsepower":
            return value * 0.00134102
        elif unit == "Horsepower to watts":
            return value / 0.00134102
        elif unit == "kW to BTU/h":
            return value * 3412.14
        elif unit == "BTU/h to kW":
            return value / 3412.14
    
    elif category == "Data Storage":
        if unit == "Bytes to kilobytes":
            return value / 1024
        elif unit == "Kilobytes to bytes":
            return value * 1024
        elif unit == "Kilobytes to megabytes":
            return value / 1024
        elif unit == "Megabytes to kilobytes":
            return value * 1024
        elif unit == "Megabytes to gigabytes":
            return value / 1024
        elif unit == "Gigabytes to megabytes":
            return value * 1024
        elif unit == "Gigabytes to terabytes":
            return value / 1024
        elif unit == "Terabytes to gigabytes":
            return value * 1024
    
    elif category == "Currency":
        # Note: Currency rates fluctuate, these are approximate values
        if unit == "USD to EUR":
            return value * 0.93  # Approximate rate as of 2023
        elif unit == "EUR to USD":
            return value / 0.93
        elif unit == "USD to GBP":
            return value * 0.79  # Approximate rate as of 2023
        elif unit == "GBP to USD":
            return value / 0.79
    
    elif category == "Angle":
        if unit == "Degrees to radians":
            return value * (3.14159265359 / 180)
        elif unit == "Radians to degrees":
            return value * (180 / 3.14159265359)
        elif unit == "Degrees to gradians":
            return value * (10 / 9)
        elif unit == "Gradians to degrees":
            return value * (9 / 10)
    
    elif category == "Frequency":
        if unit == "Hertz to kilohertz":
            return value / 1000
        elif unit == "Kilohertz to hertz":
            return value * 1000
        elif unit == "Megahertz to gigahertz":
            return value / 1000
        elif unit == "Gigahertz to megahertz":
            return value * 1000
    
    elif category == "Electricity":
        if unit == "Volts to millivolts":
            return value * 1000
        elif unit == "Millivolts to volts":
            return value / 1000
        elif unit == "Amps to milliamps":
            return value * 1000
        elif unit == "Milliamps to amps":
            return value / 1000
    
    elif category == "Magnetism":
        if unit == "Tesla to gauss":
            return value * 10000
        elif unit == "Gauss to tesla":
            return value / 10000
        elif unit == "Oersted to ampere/meter":
            return value * 79.5775
        elif unit == "Ampere/meter to oersted":
            return value / 79.5775
    
    elif category == "Sound":
        if unit == "Decibels to bels":
            return value / 10
        elif unit == "Bels to decibels":
            return value * 10
        elif unit == "Sound pressure level (dB to Pa)":
            return 20 * 10 ** (value / 20)
        elif unit == "Pa to dB":
            return 20 * math.log10(value / 20)
    
    elif category == "Light":
        if unit == "Lumens to lux":
            return value  # Assuming 1 lux = 1 lumen/m² (needs area for accurate conversion)
        elif unit == "Lux to lumens":
            return value  # Needs area for accurate conversion
        elif unit == "Candela to lumen":
            return value * 12.57  # Approximation for isotropic source
        elif unit == "Lumen to candela":
            return value / 12.57
    
    elif category == "Radiation":
        if unit == "Sievert to rem":
            return value * 100
        elif unit == "Rem to sievert":
            return value / 100
        elif unit == "Gray to rad":
            return value * 100
        elif unit == "Rad to gray":
            return value / 100
    
    elif category == "Chemistry":
        if unit == "Moles to molecules":
            return value * 6.02214076e23
        elif unit == "Molecules to moles":
            return value / 6.02214076e23
        elif unit == "Molarity to molality":
            return value  # Needs density for accurate conversion
        elif unit == "Molality to molarity":
            return value  # Needs density for accurate conversion
    
    elif category == "Physics":
        if unit == "Newtons to pound-force":
            return value * 0.224809
        elif unit == "Pound-force to newtons":
            return value / 0.224809
        elif unit == "Joules to electronvolts":
            return value * 6.242e18
        elif unit == "Electronvolts to joules":
            return value / 6.242e18
    
    elif category == "Mathematics":
        if unit == "Decimal to binary":
            return bin(int(value))[2:]
        elif unit == "Binary to decimal":
            return int(str(value), 2)
        elif unit == "Decimal to hexadecimal":
            return hex(int(value))[2:]
        elif unit == "Hexadecimal to decimal":
            return int(str(value), 16)

# Button to trigger conversion
if st.button("Convert"):
    try:
        result = convert_units(category, value, unit)
        if category == "Mathematics" and isinstance(result, str):
            st.success(f"The converted value is: {result}")
        else:
            st.success(f"The converted value is: {result:.4f}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")