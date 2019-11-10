Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> cccccckvuiuelebftvjubbevblnkngfndhcnuufbgknj
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    cccccckvuiuelebftvjubbevblnkngfndhcnuufbgknj
NameError: name 'cccccckvuiuelebftvjubbevblnkngfndhcnuufbgknj' is not defined
>>> def average(x: int,y: int,z: int):
	""" This function takes three values from 0 to 100 and gives their average.E.g. average(20,30,40)
	>>>30"""
	return (x+y+z)/3

>>> average(2.3,4,5)
3.766666666666667
>>> average(20,30,40)
30.0
>>> def top_three_average(x,y,z,w):
	"""this function gives the average of the top three grades.
The grades should be from 0 to 100 inclusive.
top_three_average(34,45,23,13)
>>>51







KeyboardInterrupt
>>> min(34,23,12)
12
>>> id(12)
4517354480
>>> def top_three_average(x,y,z,w):
	"""this function gives the average of the top three grades.The grades should be from 0 to 100 inclusive.top_three_average(34,45,23,13)>>>51"""
	return (x+y+z+w-min(x,y,z,w))/3

>>> top_three_average(50,60,70,80)
70.0
>>> def top_three_average(x,y,z,w): ->int
	"""this function gives the average of the top three grades.The grades should be from 0 to 100 inclusive.top_three_average(34,45,23,13)>>>51"""
	return (x+y+z+w-min(x,y,z,w))/3
SyntaxError: invalid syntax
>>> def top_three_average(x,y,z,w) ->int:
	"""this function gives the average of the top three grades.The grades should be from 0 to 100 inclusive.top_three_average(34,45,23,13)>>>51"""
	return (x+y+z+w-min(x,y,z,w))/3

>>> top_three_average(50,60,70,80)
70.0
>>> def top_three_avg(grade1, grade2, grade3, grade4):
 """ (number, number, number, number) -> number
 Return the average of the top three of grades grade1, grade2,
 grade3, and grade4.
 >>> top_three_avg(50, 60, 70, 80)
 70
 """
 # Here is one solution that does not use average_grade from Q6.
 total = grade1 + grade2 + grade3 + grade4
 top_three = total - min(grade1, grade2, grade3, grade4)
 return top_three / 3

>>> top_three_average(50,60,70,80)
70.0
>>> def weeks_elapsed(day1,day2):
​ 	    ​""" (int, int) -> int​
​day1 and day2 are days in the same year. Return the number of full weeks​
​that have elapsed between the two days.​
​ >>> weeks_elapsed(3, 20)​
​    2​
>>> weeks_elapsed(20, 3)​
2​
​>>> weeks_elapsed(8, 5)​
​ 	
​ 	​    >>> weeks_elapsed(40, 61)​
​ 	
​ 	​    """​
return abs(day1-day2)//7
SyntaxError: invalid character in identifier
>>> def weeks_elapsed(day1,day2):
							​""" (int, int) -> int​
​day1 and day2 are days in the same year. Return the number of full weeks​
​that have elapsed between the two days.​
​ >>> weeks_elapsed(3, 20)​
​    2​
>>> weeks_elapsed(20, 3)​
2​
​>>> weeks_elapsed(8, 5)​
​
​ 	​    >>> weeks_elapsed(40, 61)​
​
​ 	​    """​
return abs(day1-day2)//7
SyntaxError: invalid character in identifier
>>> def weeks_elapsed(day1,day2):
	def weeks_elapsed(day1,day2):
								​""" (int, int) -> int​
	​day1 and day2 are days in the same year. Return the number of full weeks​
	​that have elapsed between the two days.​
	​ >>> weeks_elapsed(3, 20)​
	​    2​
	>>> weeks_elapsed(20, 3)​
	2​
	​>>> weeks_elapsed(8, 5)​
	​
	​ 	​    >>> weeks_elapsed(40, 61)​
	​
	​ 	​    """​
	return abs(day1-day2)//7
KeyboardInterrupt
>>> def weeks_elapsed(day1,day2):
	return abs(day1-day2)//7

>>> weeks_elapsed(3,20)
2
>>> weeks_elapsed(20,2)
2
>>> weeks_elapsed(8,5)
0
>>> weeks_elapsed(40,61)
3
>>> def square(num):
	""" (number) -> number
	Return the square of num.
	>>>square(3)
	9
	"""
	return num**2

>>> square(3)
9
>>> square(-3)
9
>>> 
