#“Using a loop, sum the numbers in the range 2 to 22 (inclusive), and then calculate the average.”
sum = 0
for i in range(2,23):
    sum += i 
print("The sum is :", sum)
print("The average is :", sum/len(range(2,23)))

