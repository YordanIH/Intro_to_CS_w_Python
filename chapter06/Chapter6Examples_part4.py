Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py
Enter the temperature in degrees Fahrenheit: 500
It is above freezing. 
>>> import doctest
>>> doctest.testmod()
**********************************************************************
File "/Users/yhalachev/Desktop/Intro to CS with Python/Chapter 6/temperature_program.py", line 3, in __main__.convert_to_celsius
Failed example:
    convert_to_celsius(75)
Expected:
     23.88888888888889
Got:
    57.22222222222222
**********************************************************************
1 items had failures:
   1 of   1 in __main__.convert_to_celsius
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
>>> 
