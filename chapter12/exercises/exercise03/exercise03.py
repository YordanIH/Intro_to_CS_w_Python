#Count the number of lines and sum each value and 
# divide it to the number of years

def hopedale_average(file_with_values) -> float:
    """ (str) -> float
    Return the average number of pelts produced per year for the data in
    Hopedale
    file named filename.
    """ 
    with open(file_with_values, 'r') as hopedale_file:

    #Read heading
        hopedale_file.readline()
        #Read comment line until we reach first piece of data
        data = hopedale_file.readline().strip()
        while data.startswith('#'):
            data = hopedale_file.readline().strip()
    
        pelts_list=[]
        pelts_list.append(int(data))

        for data in hopedale_file:
            pelts_list.append(int(data.strip()))
        print(pelts_list)
        print(len(pelts_list))

        return sum(pelts_list) / len(pelts_list)

print(hopedale_average('hopedale_file.txt'))
