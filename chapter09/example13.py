#Looping over nested lists
elements = [['li', 'Na', 'K'], ['F','Cl', 'Br']]
for inner_list in elements:
    for item in inner_list:
        print(item)

#Looping over Ragged List

info = [['Isaac Newton',1643,1727],['Charles Darwin',1809,1882],['Alan Turing',1912,1954,'alan@bletchley.uk']]
print(info)
for item in info:
    print(len(item))


drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],["8:45", "12:44", "14:52", "22:17"],["8:55","11:11", "12:34","13:46","15:52","17:08", "21:15"],["9:15","11:14", "16:28"],["10:01","13:33","16:45", "19:00"],["9:34", "11:16", "15:52","20:37"],["9:01", "12:24", "18:51", "23:13"]]
for day in drinking_times_by_day:
    for drinking_time in day:
        print(drinking_time, end=' ')
    print()
