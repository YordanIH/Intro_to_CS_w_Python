#a)
class Country:

    def __init__(self, name: str, population: int, area: int):
        """ (Country, str, int, int)
        A new Country named name with population people and area area.
        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.name
        'Canada'
        >>> canada.population
        34482779
        >>> canada.area
        9984670
        """ 

        self.name = name
        self.population = population
        self.area = area

#b)
    def is_larger(self, other):
        """
        >>> from exercise01 import Country>>> usa = Country('United States of America', 313914040, 9826675)
        >>> canada = Country('Canada', 34482779, 9984670)>>> canada.is_larger(usa)True
        >>> usa.is_larger(canada)
        False
        """
        return self.area > other.area
#c)
    def population_density(self):
        """>>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.population_density()
        3.4535722262227995
        """
        return  self.population / self.area

#d)
    def __str__(self):
        """>>> canada = Country('Canada', 34482779, 9984670)
        >>> print(canada)
        Canada has a population of 34482779 and is 9984670 square km
        """
        return "{0} has a population of {1} and is {2} square km".format(self.name,self.population,self.area)

#e)
    def __repr__(self):
        """>>> canada = Country('Canada', 34482779, 9984670)
        >>> canada
        Country('Canada',34482779,9984670)
        >>> [canada]
        [Country('Canada',34482779,9984670)]
        """

        return "Country('{0}',{1},{2})".format(self.name, self.population, self.area)    