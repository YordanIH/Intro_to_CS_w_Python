Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> result=abs(x)==x
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    result=abs(x)==x
NameError: name 'x' is not defined
>>> def different(a,b):
	return a==b

>>> different(10,10)
True
>>> different(10,9)
False
>>> float(population)=input("What is the populaton: ")
SyntaxError: cannot assign to function call
>>> population=float(float(population)=input("What is the populaton: "))
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> populaiton=input("What is the population: ")
What is the population: 200000000
>>> population
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    population
NameError: name 'population' is not defined
>>> population
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    population
NameError: name 'population' is not defined
>>> populaiton
'200000000'
>>> population=float(input("What is the population: "))
What is the population: jlkj
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    population=float(input("What is the population: "))
ValueError: could not convert string to float: 'jlkj'
>>> population=float(input("What is the population: "))
What is the population: 20,000,000
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    population=float(input("What is the population: "))
ValueError: could not convert string to float: '20,000,000'
>>> ValueError: could not convert string to float: '20,000,000'File "<pyshell#17>", line 1, in <module>
SyntaxError: invalid syntax
>>> population=float(input("What is the population: "))
What is the population: 20000000
>>> land_area=float(input("What is the land area: "))
What is the land area: 10 000
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    land_area=float(input("What is the land area: "))
ValueError: could not convert string to float: '10 000'
>>> land_area=float(input("What is the land area: "))
What is the land area: 10000
>>> if population<10000000:
	print populaiton
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(populaiton)?
>>> if population<10000000:
	print(populaiton)

	
>>> population=float(input("What is the population: "))
What is the population: 5000000
>>> if population<10000000:
	print(populaiton)

	
200000000
>>> if population<10000000:
	print(population)

	
5000000.0
>>> population=20000000
>>> if 10000000<population and population < 35000000:
	print(population)

	
20000000
>>> if 10000000<population< 35000000:
	print(population)

	
20000000
>>> population= 15365543
>>> if 10000000<population< 35000000:
	print(population)

	
15365543
>>> population=100000000
>>> land_area=1000
>>> if population/land_area > 100:
	print(Densely populated)
	
SyntaxError: invalid syntax
>>> if population/land_area > 100:
	print("Densely populated")

	
Densely populated
>>> if population/land_area > 100:
	print("Densely populated")
else:
	print("Sparsely populated")

	
Densely populated
>>> population=10000
>>> land_area=1000000
>>> if population/land_area > 100:
	print("Densely populated")
else:
	print("Sparsely populated")

	
Sparsely populated
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 5/Convert _temp.py
>>> convert_temperatures(100,"Celsius","Celsius")
100
>>> convert_temperatures(100,"Celsius","Kelvin")
373.15
>>> convert_temperatures(100,"Kelvin","Celsius")
-173.14999999999998
>>> convert_temperatures(100,"Kelvin","Celsius")
-173.14999999999998
>>> -173.14999999999998
