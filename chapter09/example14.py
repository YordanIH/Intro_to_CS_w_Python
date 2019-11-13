#Looping untill a condition is reached

rabbits = 3
while rabbits >0:
    print(rabbits)
    rabbits = rabbits -1

#bacteria double their numbers
time = 0
population = 1000 # 1000 bacteria to start with 
growth_rate = 0.21 # 21% grwoth per minute
while population < 2000:
     population = population + population * growth_rate
     print(round(population))
     time = time + 1
print("It took", time, "minutest for the backetria to double.")
print("The final population was", round(population), "backteria.")