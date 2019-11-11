"""Variable kingdoms refers to the list [’Bacteria’, ’Protozoa’, ’Chromista’, ’Plantae’, ’Fungi’, ’Animalia’].
Using kingdoms and either slicing or indexing with positive indices, write expressions that produce the following:

The first item of kingdoms
The last item of kingdoms
The list [’Bacteria’, ’Protozoa’, ’Chromista’]
The lst [’Chromista’, ’Plantae’, ’Fungi’]
The list [’Fungi’, ’Animalia’]
The empty list
Repeat the previous exercise using negative indices."""

kingdoms = ['Bacteria','Protozoa','Chromista','Plantae','Fungi','Animalia']
#The first item of kingdoms
print(kingdoms[-6])
#The last item of kingdoms
print(kingdoms[-1])
#The list [’Bacteria’, ’Protozoa’, ’Chromista’]
print(kingdoms[-6:-3])
#The lst [’Chromista’, ’Plantae’, ’Fungi’]
print(kingdoms[-4:-1])
#The list [’Fungi’, ’Animalia’]
print(kingdoms[-2:])
#The empty list
print(kingdoms[-2:0])
