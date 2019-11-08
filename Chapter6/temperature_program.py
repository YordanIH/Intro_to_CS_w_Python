def convert_to_celsius(fahrenheit: float) -> float:
    """
    >>> convert_to_celsius(75)
     23.88888888888889
    """
    return fahrenheit - 32.0 * 5.0 / 9.0

def above_freezing(celsius: float ) -> bool:
    return celsius > 0

if __name__== "__main__":
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print("It is above freezing. ")
    else:
        print("It is below freezing. ")
