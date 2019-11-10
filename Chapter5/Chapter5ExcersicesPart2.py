Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ph=2
>>> if ph < 3.0:
	print(ph, "is VERY acidic! Be careful.")
elif ph < 7.0:
	print(ph, "is acidic.
	      
SyntaxError: EOL while scanning string literal
>>> if ph < 3.0:
	print(ph, "is VERY acidic! Be careful.")
elif ph < 7.0:
	print(ph, "is acidic.")

	
2 is VERY acidic! Be careful.
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 6.4
>>> if ph < 7.0:
	print("It's acidic!")
elif ph < 4.0:
	print("It's a strong acid!")

	
It's acidic!
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 3.6
>>> if ph < 7.0:
	print("It's acidic!")
elif ph < 4.0:
	print("It's a strong acid!")

	
It's acidic!
>>> if ph < 7.0:
	print("It's acidic!")
if ph < 4.0:
	print("It's a strong acid!")
	
SyntaxError: invalid syntax
>>> if ph < 7.0:
	print("It's acidic!")
	if ph < 4.0:
	print("It's a strong acid!")
	
SyntaxError: expected an indented block
>>> if ph < 7.0:
	print("It's acidic!")
	if ph < 4.0:
		print("It's a strong acid!")

		
It's acidic!
It's a strong acid!
>>> young = age < 45
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    young = age < 45
NameError: name 'age' is not defined
>>> age =23
>>> young = age < 45
>>> heavy = bmi >= 22.0
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    heavy = bmi >= 22.0
NameError: name 'bmi' is not defined
>>> bmi = 23
>>> heavy = bmi >= 22.0
>>> if young ​and not heavy:
​    risk = ​'low'​
​elif​ young ​and​ ​heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ not heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ ​heavy:
​    risk = ​'high'
SyntaxError: invalid character in identifier
>>> 



sk = ​'low'​
​elif​ young ​and​ ​heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ not heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ ​heavy:
​    risk = ​'high'
KeyboardInterrupt
>>> ​​if young ​and​ not heavy:
​    risk = ​'low'​
​elif​ young ​and​ ​heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ not heavy:
​    risk = ​'medium'​
​​elif​ ​not​ young ​and​ ​heavy:
​    risk = ​'high'
SyntaxError: invalid character in identifier
>>> if young and not heavy:
 risk = 'low'
elif young and heavy:
 risk = 'medium'
elif not young and not heavy:
 risk = 'medium'
elif not young and heavy:
 risk = 'high'

 
>>> risk
'medium'
>>> 
