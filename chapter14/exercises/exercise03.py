class Member:
    """ A member of a university. """
    def __init__(self, name:str, address: str, email:str) -> None:
        """Create a new member named name, with home address and email address."""

        self.name = name
        self.address = address
        self.email = email

    def __str__(self) -> str:
        """Return a string representation of this Member.

        >>> member = Member('Paul', 'Ajax', 'pgries@cs.torronto.edu')
        >>> member.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu'
        """

        return '''{}\n{}\n{}'''.format(self.name, self.address, self.email)

    def __repr__(self):
        """ (Member) -> str
        Return a concise string representation of this Member.
        >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
        >>> member.__repr__()
        "Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')"
        """

        return "Member('{}','{}','{}')".format(self.name, self.address, self.email)

class Faculty(Member):
    """ A faculty member at a university. """
    def __init__(self, name: str, address: str, email: str, faculty_num: str, courses_teaching: list) -> None:
        """Create a new faculty named name , with home address , email address, faculty number faculty_num, and empty list of courses."""

        super().__init__(name,address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = courses_teaching
    
    def __str__(self) -> str:
        """Return a string representation of this Faculty.

        >>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        >>> faculty.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nCourses: '
        """
        member_string = super().__str__()

        return '''{}\n{}\nCourses: {}'''.format(
            member_string,
            self.faculty_number, ' '.join(self.courses_teaching))

    def __repr__(self):
        """ (Faculty) -> str
        Return a concise string representation of this Faculty.
        >>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu',
        '1234')
        >>> faculty.__repr__()
        "Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', 1234, [])"
        """ 
        return "Faculty('{}','{}','{}',{},[{}])".format(self.name, self.address, self.email, self.faculty_number, ','.join(self.courses_teaching))  


class Student(Member):
    """A student member at a university"""

    def __init__(self, name: str, address: str, email: str, student_num: str) -> None:
        """Create a new student named name, with home address, email address, student number student num, an empty list of courses taken,
        and an empty list of current courses.
        """

        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
#a)
    def __str__(self):
        """ (Student) -> str
        Return a string representation of this Student.
        >>> student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu',
        '1234')
        >>> student.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nPrevious courses:
        \\nCurrent courses: '
        """ 
        member_string=super().__str__()

        return """{}\n {}\nPrevious Course: {}\nCurrent Courses:{}""".format(member_string, self.student_number,' '.join(self.courses_taken),' '.join(self.courses_taking))
#b)
    def __repr__(self):
        """ (Faculty) -> str
        Return a concise string representation of this Faculty.
        >>> student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu',
        '1234')
        >>> student.__repr__()
        "Studen"""

        return "Student('{}','{}','{}',{},[{}],[{}])".format(self.name, self.address, self.email, self.student_number,','.join(self.courses_taken),','.join(self.courses_taking))


