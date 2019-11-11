"""Variable appointments refers to the list [’9:00’, ’10:30’, ’14:00’, ’15:00’, ’15:30’].
An appointment is scheduled for 16:30, so ’16:30’ needs to be added to the list.”

"""

#Variable appointments refers to the list [’9:00’, ’10:30’, ’14:00’, ’15:00’, ’15:30’]. An appointment is scheduled for 16:30, so ’16:30’ needs to be added to the list.”
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments.append('16:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']

#Instead of using append, use the + operator to add ’16:30’ to the end of the list that appointments refers to.
>>> appointments.pop()
'16:30'
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments = appointments+['16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']

