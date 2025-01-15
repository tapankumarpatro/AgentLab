import json
from phi.tools import Toolkit


class UnitConverter(Toolkit):
    def __init__(
        self,
        length: bool = True,
        weight: bool = True,
        temperature: bool = True,
        volume: bool = False,
        area: bool = False,
        enable_all: bool = False,
    ):
        super().__init__(name="unit_converter")

        # Register functions in the toolkit
        if length or enable_all:
            self.register(self.meters_to_feet)
            self.register(self.feet_to_meters)
            self.register(self.kilometers_to_miles)
            self.register(self.miles_to_kilometers)
        
        if weight or enable_all:
            self.register(self.kg_to_pounds)
            self.register(self.pounds_to_kg)
            self.register(self.grams_to_ounces)
            self.register(self.ounces_to_grams)
        
        if temperature or enable_all:
            self.register(self.celsius_to_fahrenheit)
            self.register(self.fahrenheit_to_celsius)
            self.register(self.celsius_to_kelvin)
            self.register(self.kelvin_to_celsius)
        
        if volume or enable_all:
            self.register(self.liters_to_gallons)
            self.register(self.gallons_to_liters)
        
        if area or enable_all:
            self.register(self.square_meters_to_square_feet)
            self.register(self.square_feet_to_square_meters)

    # Length conversions
    def meters_to_feet(self, meters: float) -> str:
        """Convert meters to feet.
        
        Args:
            meters (float): Length in meters
            
        Returns:
            str: JSON string with the result in feet
        """
        feet = meters * 3.28084
        return json.dumps({"feet": feet})

    def feet_to_meters(self, feet: float) -> str:
        """Convert feet to meters.
        
        Args:
            feet (float): Length in feet
            
        Returns:
            str: JSON string with the result in meters
        """
        meters = feet / 3.28084
        return json.dumps({"meters": meters})

    def kilometers_to_miles(self, km: float) -> str:
        """Convert kilometers to miles.
        
        Args:
            km (float): Distance in kilometers
            
        Returns:
            str: JSON string with the result in miles
        """
        miles = km * 0.621371
        return json.dumps({"miles": miles})

    def miles_to_kilometers(self, miles: float) -> str:
        """Convert miles to kilometers.
        
        Args:
            miles (float): Distance in miles
            
        Returns:
            str: JSON string with the result in kilometers
        """
        km = miles / 0.621371
        return json.dumps({"kilometers": km})

    # Weight conversions
    def kg_to_pounds(self, kg: float) -> str:
        """Convert kilograms to pounds.
        
        Args:
            kg (float): Weight in kilograms
            
        Returns:
            str: JSON string with the result in pounds
        """
        pounds = kg * 2.20462
        return json.dumps({"pounds": pounds})

    def pounds_to_kg(self, pounds: float) -> str:
        """Convert pounds to kilograms.
        
        Args:
            pounds (float): Weight in pounds
            
        Returns:
            str: JSON string with the result in kilograms
        """
        kg = pounds / 2.20462
        return json.dumps({"kilograms": kg})

    def grams_to_ounces(self, grams: float) -> str:
        """Convert grams to ounces.
        
        Args:
            grams (float): Weight in grams
            
        Returns:
            str: JSON string with the result in ounces
        """
        ounces = grams * 0.035274
        return json.dumps({"ounces": ounces})

    def ounces_to_grams(self, ounces: float) -> str:
        """Convert ounces to grams.
        
        Args:
            ounces (float): Weight in ounces
            
        Returns:
            str: JSON string with the result in grams
        """
        grams = ounces / 0.035274
        return json.dumps({"grams": grams})

    # Temperature conversions
    def celsius_to_fahrenheit(self, celsius: float) -> str:
        """Convert Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in Celsius
            
        Returns:
            str: JSON string with the result in Fahrenheit
        """
        fahrenheit = (celsius * 9/5) + 32
        return json.dumps({"fahrenheit": fahrenheit})

    def fahrenheit_to_celsius(self, fahrenheit: float) -> str:
        """Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit
            
        Returns:
            str: JSON string with the result in Celsius
        """
        celsius = (fahrenheit - 32) * 5/9
        return json.dumps({"celsius": celsius})

    def celsius_to_kelvin(self, celsius: float) -> str:
        """Convert Celsius to Kelvin.
        
        Args:
            celsius (float): Temperature in Celsius
            
        Returns:
            str: JSON string with the result in Kelvin
        """
        kelvin = celsius + 273.15
        return json.dumps({"kelvin": kelvin})

    def kelvin_to_celsius(self, kelvin: float) -> str:
        """Convert Kelvin to Celsius.
        
        Args:
            kelvin (float): Temperature in Kelvin
            
        Returns:
            str: JSON string with the result in Celsius
        """
        celsius = kelvin - 273.15
        return json.dumps({"celsius": celsius})
