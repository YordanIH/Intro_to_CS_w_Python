with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))
        
