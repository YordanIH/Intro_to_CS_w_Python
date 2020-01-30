>>> from example05 import Atom
>>> from example06 import Molecule
>>> ammonia = Molecule("AMMONIA")
>>> ammonia.add(Atom(1, "N", 0.257, -0.363, 0.0))
>>> ammonia.add(Atom(2, "H", 0.257, 0.727, 0.0))
>>> ammonia.add(Atom(3, "H", 0.771, 0.727, 0.890))
>>> ammonia.add(Atom(4, "H", 0.771, -0.727, -0.890))
>>> ammonia.translate(0, 0, 0.2)
>>> ammonia
Molecule("AMMONIA",Atom(1, "N", 0.257, -0.363, 0.2), Atom(2, "H", 0.257, 0.727, 0.2), Atom(3, "H", 0.771, 0.727, 1.09), Atom(4, "H", 0.771, -0.727, -0.69)))