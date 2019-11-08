def convert_temperatures(t: float,source: str,target: str) ->  float:

    if source == 'Celsius':
        celsius = t
    elif source == 'Kelvin':
        celsius = t - 273.15
    elif source == 'Fahrenheit':
        celsius = (t - 32) * 5/9
    elif source == 'Rankine':
        celsius = (t -491.67) * 5/9
    elif source == 'Delisle':
        celsius = 100 - t * 2/3
    elif source == 'Newton':
        celsius = t * 100/33 
    elif source == 'Reaumur':
        celsius = t * 5/4
    elif source == 'Romer':
        celsius = (t - 7.5) * 40/21
    if target == 'Celsius':
        return celsius
    elif target == 'Kelvin':
        return celsius + 273.15
    elif target == 'Fahrenheit':
        return celsius * 5/9 + 32
    elif target == 'Rankine':
        return (celsius + 273.15) * 9/5
    elif target == 'Delisle':
        return (100 - celsius) * 3/2
    elif target == 'Newton':
        return celsius * 33 /100
    elif target == 'Reamur':
        return celsius * 4/5
    elif target == 'Romer':
        return celsius * 21 /40 + 7.5

    
        
        
