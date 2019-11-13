'''You are given two lists, rat_1 and rat_2, that contain the daily weights of two rats over a period of ten days. Assume the rats never have exactly the same weight. Write statements to do the following:'''




rat_1 = [2,4]
rat_2 = [1,3]
""" We are assuming the rats never have the same weight"""

#1 If the weight of rat 1 is greater than that of rat 2 on day 1, print "Rat 1 weighed more than rat 2 on day 1."; otherwise, print "Rat 1 weighed less than rat 2 on day 1.".”

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1")
    #2 “If rat 1 weighed more than rat 2 on day 1 and if rat 1 weighs more than rat 2 on the last day, print "Rat 1 remained heavier than Rat 2."; otherwise, print "Rat 2 became heavier than Rat 1.”
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than rat 2")
    elif rat_1[-1] < rat_2[-1]:
        print("Rat 2 became havier than Rat 1")

elif rat_1[0] < rat_2[0]:
    print("Rat 1 weighed less than rat 2 on day 1")


#3 “If your solution to the previous exercise used nested if statements, then do it without nesting, or vice versa.”

if rat_1[0] > rat_2[0] and  rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than rat 2")
if rat_1[0] > rat_2[0] and rat_1[-1] < rat_2[-1]:
    print("Rat 2 became havier than Rat 1")

    
