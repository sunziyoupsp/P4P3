import math


class Planet:
    def __init__(self,distance,radius,mass):
        self.distance = distance
        self.radius = radius
        self.mass = mass
    
    def getVolume(self):
        return round(4/3 * math.pi * (self.radius ** 3),2)
    
    def getSurfaceArea(self):
        return round(4 * math.pi * self.radius ** 2, 2)
    
    def getDensity(self):
        return round(self.mass / self.getVolume(),10)

Mars = Planet(45,198,1000)
Venus = Planet(35,134,893)

print("Mar's distance is", Mars.distance)
print("Mar's radius is", Mars.radius)
print("Mar's mass is", Mars.mass)
print("Mar's volume is", Mars.getVolume())
print("Mar's surface area is", Mars.getSurfaceArea())
print("Mar's density is", Mars.getDensity())
print()
print("Venus's distance is", Venus.distance)
print("Venus's radius is", Venus.radius)
print("Venus's mass is", Venus.mass)
print("Venus's volume is", Venus.getVolume())
print("Venus's surface area is", Venus.getSurfaceArea())
print("Venus's density is", Venus.getDensity())