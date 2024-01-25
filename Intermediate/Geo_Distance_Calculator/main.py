from geopy import Nominatim
from geopy.distance import geodesic
from dataclasses import dataclass

@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude
    
def get_coordinates(address: str):
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(address)

    if location:
        return Coordinates(location.latitude, location.longitude)
    
def calculate_distance(origin: Coordinates , destination: Coordinates):
    if origin and destination:
        return geodesic(origin.coordinates(), destination.coordinates()).km
    
def get_distance(origin, destination):
    origin = get_coordinates(origin)
    destination = get_coordinates(destination)

    if distance := calculate_distance(origin, destination):
        print(f'{origin} --> {destination} is {distance:.2f} km')
        return distance
    else:
        print("Invalid address")
        return None

def shipping_cost(distance):
    if distance <= 100:
        return distance * 3.5
    elif distance <= 500:
        return distance * 4.0
    elif distance <= 1000:
        return distance * 4.5
    elif distance > 1000:
        return distance * 5.0
    else:
        return None

def main():
    origin = "Chennai, Tamil Nadu, India"
    destination = "Mumbai, Maharashtra, India"
    distance = get_distance(origin, destination)
    cost = shipping_cost(distance)
    print(f"Shipping cost from {origin.split(', ')[0]} to {destination.split(', ')[0]} is {cost:.2f} INR")
    
if __name__ == "__main__":
    main()