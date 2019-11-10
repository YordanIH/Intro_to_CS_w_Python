'''Variable kingdoms refers to the list [’Bacteria’, ’Protozoa’, ’Chromista’, ’Plantae’, ’Fungi’, ’Animalia’]. Using kingdoms and either slicing or indexing with positive indices, write expressions that produce the following:

The first item of kingdoms
The last item of kingdoms
The list [’Bacteria’, ’Protozoa’, ’Chromista’]
The list [’Chromista’, ’Plantae’, ’Fungi’]
The list [’Fungi’, ’Animalia’]
The empty list”
'''
kingdoms = ['Bacteria','Protozoa','Chromista','Plantae','Fungi','Animalia']
#The first item of kingdoms
print(kingdoms[0])
#The last item of kingdoms
print(kingdoms[5])
#The list [’Bacteria’, ’Protozoa’, ’Chromista’]
print(kingdoms[:3])
#The list [’Chromista’, ’Plantae’, ’Fungi’]
print(kingdoms[2:5])
#The empty list”
print(kingdoms[1:0])

