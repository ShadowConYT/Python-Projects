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

def main():
    origin = "Chennai, Tamil Nadu, India"
    destination = "Mumbai, Maharashtra, India"
    get_distance(origin, destination)
    
if __name__ == "__main__":
    main()