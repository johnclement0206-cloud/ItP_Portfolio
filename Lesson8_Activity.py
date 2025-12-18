# Made by: John Clement J. Ibrahim
# Date: 10/14/2025
# Course: Cybersecurity, 4th Level (Group 1)

class AstronomicalObject:
    def __init__(self, name, obj_type, discovered_by, discovery_year, distance_light_years, mass_solar, diameter_km, constellation, visibility_from_earth, notable_feature):
        self.name = name #str
        self.obj_type = obj_type #str
        self.discovered_by = discovered_by #str
        self.discovery_year = discovery_year #float
        self.distance_light_years = distance_light_years #float
        self.mass_solar = mass_solar #float
        self.diameter_km = diameter_km #float
        self.constellation = constellation #str
        self.visibility_from_earth = visibility_from_earth #str
        self.notable_feature = notable_feature #str

    def display(self): #prints information in an organized manner, uses f strings
        print(f"Astronomical Object: {self.name}\n"
              f"  Type: {self.obj_type}\n"
              f"  Discovered by: {self.discovered_by}\n"
              f"  Discovery Year: {self.discovery_year}\n"
              f"  Distance from Earth (ly): {self.distance_light_years}\n"
              f"  Mass (in solar masses): {self.mass_solar}\n"
              f"  Diameter (km): {self.diameter_km}\n"
              f"  Constellation: {self.constellation}\n"
              f"  Visible from Earth: {self.visibility_from_earth}\n"
              f"  Notable Feature: {self.notable_feature}\n")

objects = [ #list of all data
    AstronomicalObject("Betelgeuse", "Red Supergiant Star", "John Flamsteed", 1767, 642.5, 11.6, 1400000000, "Orion", "Yes", "Will go supernova"),
    AstronomicalObject("Andromeda Galaxy", "Spiral Galaxy", "Abd al-Rahman al-Sufi", 964, 2537000, 1.230e12, 220000, "Andromeda", "Yes", "Nearest major galaxy to Milky Way"),
    AstronomicalObject("Jupiter", "Gas Giant Planet", "Known since antiquity", "-", 0.000082317, 317.8, 142984, "Zodiacal constellations", "Yes", "Largest planet in Solar System"),
    AstronomicalObject("Cygnus X-1", "Black Hole", "Tom Bolton", 1971, 6070, 15, "-", "Cygnus", "No", "First confirmed black hole"),
    AstronomicalObject("Halley's Comet", "Comet", "Edmond Halley", 1705, 0.000578, 2.2e-14, 11, "Varying", "Yes (periodically)", "Most famous periodic comet"),
    AstronomicalObject("Proxima Centauri", "Red Dwarf Star", "Robert Innes", 1915, 4.2465, 0.123, 200000, "Centaurus", "No", "Closest star to Solar System"),
    AstronomicalObject("Sagittarius A*", "Supermassive Black Hole", "Bruce Balick & Robert Brown", 1974, 26150, 4.1e6, "-", "Sagittarius", "No", "At center of Milky Way"),
    AstronomicalObject("Supernova 1987A", "Supernova Remnant", "Ian Shelton", 1987, 168000, "-", 1.9e13, "Dorado", "Yes (with telescope)", "First visible supernova in nearly 400 years"),
    AstronomicalObject("Vega", "Main Sequence Star", "Known since antiquity", "-", 25.04, 2.135, 2362000, "Lyra", "Yes", "Reference star for magnitude scale"),
    AstronomicalObject("Ceres", "Dwarf Planet", "Giuseppe Piazzi", 1801, 0.000265, 0.00015, 939, "Asteroid Belt", "Yes (with telescope)", "Largest object in asteroid belt"),
]

for obj in objects: #loop to print out each individual object in the array
    obj.display()
