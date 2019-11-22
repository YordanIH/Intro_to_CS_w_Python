with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()
print(planets)
for planet in reversed(planets):
    print(planet.strip())
for planet in sorted(planets):
    print(planet.strip())
    

