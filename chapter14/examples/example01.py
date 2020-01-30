
>>> isinstance('abc',str)
True
>>> isinstance(55.2,str)
False

>>> help(object)

>>> isinstance(55.2,object)
True
>>> isinstance('abc',object)
True
>>> isinstance(str, object)
True
>>> isinstance(max, object)
True
>>> help(int)

>>> help(SyntaxError)

>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

>>> class Book:
...     """Infomation about a book."""
... 
>>> type(str)
<class 'type'>
>>> type(Book)
<class 'type'>
>>> dir(Book)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> set(dir(Book)) - set(dir(object))
{'__weakref__', '__module__', '__dict__'}
>>> ruby_book = Book()
>>> ruby_book.title = 'Programming Ruby'

>>> ruby_book.authors = ['Thomas', 'Fowler', 'Hunt']

>>> ruby_book.title
'Programming Ruby'
>>> ruby_book.authors
['Thomas', 'Fowler', 'Hunt']
>>> help(Book)

>>> str.capitalize('browning')
'Browning'
>>> 'browning'.capitalize()
'Browning'

>>> class Book:
...     """Information about a book."""
...     def num_authors(self) -> int:
...             """Return the number of authors of this book.""" 
...             return len(self.authors]
>>> ruby_book = Book()
>>> ruby_book.title = 'Programming Ruby'
>>> ruby_book.authors = ['Thomas', 'Fowler', 'Hunt']
>>> Book.num_authors(ruby_book)
3
>>> ruby_book.num_authors()
3
>>> 