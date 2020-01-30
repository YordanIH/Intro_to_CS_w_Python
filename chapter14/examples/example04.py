>>> from member import Member
>>> from member import Faculty
>>> from member import Student
>>> paul = Faculty('Paul Gries', 'Ajax', 'pgries@cs.toronto.edu', '1234')
>>> paul.name
'Paul Gries'
>>> paul.email
'pgries@cs.toronto.edu'
>>> paul.faculty_number
'1234'
>>> jen = Student('Jen Campbell', 'Toronto', 'campbell@cs.toronto.edu', '4321')
>>> jen.name
'Jen Campbell'
>>> jen.email
'campbell@cs.toronto.edu'
>>> jen.student_number
'4321'
>>> str(paul)
'Paul Gries\nAjax\npgries@cs.toronto.edu'
>>> print(paul)
Paul Gries
Ajax
pgries@cs.toronto.edu

"""
 def __str__(self) -> str:
       # Return a string representation of this Faculty.

        #>>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        #>>> faculty.__str__()
        #'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nCourses: '
    
        member_string = super().__str__()

        return '''{}\n{}\nCourses: {}'''.format(
            member_string,
            self.faculty_number, ' '.join(self.courses_teaching))
        """

>>> paul = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
>>> str(paul)
'Paul\nAjax\npgries@cs.toronto.edu\n1234\nCourses: '
>>> print(paul
... )
Paul
Ajax
pgries@cs.toronto.edu
1234
Courses: 