'''Variables rat_1_weight and rat_2_weight contain the weights of two rats at the beginning of an experiment. Variables rat_1_rate and rat_2_rate are the rate that the rats’ weights are expected to increase each week (for example, 4 percent per week).

Assume that the two rats have the same initial weight, but rat 1 is expected to gain weight at a faster rate than rat 2. Using a while loop, calculate how many weeks it would take for rat 1 to be 10 percent heavier than rat 2.'''

#Using a while loop, calculate how many weeks it would take for the weight of the first rat to become 25 percent heavier than it was originally.

rat_1_weight = [1.25,1.35,1.45,2]
week = 1
while rat_1_weight[week]/rat_1_weight[0]-1 < 0.25 :
    week += 1

print(week)

#Assume that the two rats have the same initial weight, but rat 1 is expected to gain weight at a faster rate than rat 2. Using a while loop, calculate how many weeks it would take for rat 1 to be 10 percent heavier than rat 2.

#Assuming we know the weights of the rats each week

rat1 = [1,1.4,1.6,1.7,1.8]
rat2 = [1,1.3,1.4,1.4,1.4]

week = 0
while rat1[week] < rat2[week] + 0.1*rat2[week]:
    week+=1
print(week)
