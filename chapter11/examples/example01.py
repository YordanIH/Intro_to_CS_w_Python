#introducing sets
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'i', 'u', 'o', 'a', 'e'}
>>> vowels
{'i', 'u', 'o', 'a', 'e'}
>>> vowels
{'i', 'u', 'o', 'a', 'e'}
>>> vowels = {'a', 'e', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'i', 'u', 'o', 'a', 'e'}
>>> {'a', 'e', 'i', 'o', 'u'}=={'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
True
>>> type(vowels)
<class 'set'>
>>> type({1,2,3})
<class 'set'>
>>> set()
set()
>>> type(set())
<class 'set'>
>>> set([2,3,2,5])
{2, 3, 5}
>>> set(2,3,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 argument, got 3
>>> vowels={'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
>>> vowels
{'i', 'u', 'o', 'a', 'e'}
>>> set(vowels)
{'i', 'e', 'o', 'u', 'a'}
>>> set({5, 3, 1})
{1, 3, 5}
>>> set(range(5))
{0, 1, 2, 3, 4}