"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main advantages to object oriented design are abstraction, 
   encapsulation and polymorphism. Abstraction is when the 'guts' of the code is
    obscured so that users can use it without having to know how it works.
    Encapsulation is good for organizing data and methods so that they are close
    to one another in the code base. Polymorphism gives 

2. What is a class?
    
    A class is a data structure that contains the attributes and methods that
    relate to the class.

3. What is an instance attribute?
    
    An instance attribute is a piece of information about an instance of a class 
    that is not inheritied from the class definition itself.

4. What is a method?

    A method is a function definied within a class that can act on instances of
    that class.

5. What is an instance in object orientation?
    
    An instance is the realization of a class definition. I like to think of the
    analogy where the class is the cake recipe and the instance is the cake you
    bake from that recipe. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is defined for all instances of that class. An instance
   attribute is only defined for a particular instance. Instance attributes might
   be used in one-off scenarios; for example, if only one instance of a class should
   have a color it could be defined as an instance attribute. Class attributes might be
   used to set default attributes that each instance should have.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A class that can store info about a Student"""

    def __init__(self, first_name, last_name, address_line_1):
        """Initialize a student with three attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.address_line_1 = address_line_1

    def __repr__(self):
        return 'First name: {first_name}, Last name: {last_name}, Address line 1: {address_line_1'.format(
            first_name=first_name, last_name=last_name, address_line_1=address_line_1)

class Question(object):
    """Can store Q/A pairs"""
    def __init__(self, question, answer):
        """Initialize Q/A pair"""
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """prints the question to the console and checks the users answer"""
        input = raw_input(self.question + ' > ')
        return input == self.answer

    def __repr__(self):
        return 'Q: {} A: {}'.format(self.question, self.answer)

class Exam(object):
    """Can store test name and question set"""
    questions = set([])

    def __init__(self, name):
        """Initialize test"""
        self.name = name

    def add_question(self, question, answer):
        """Creates question object and adds it to questions list"""
        question_answer_obj = Question(question, answer)
        self.questions.add(question_answer_obj)

    def administer(self):
        """Asks each question and tracks correct answers"""
        num_q = len(self.questions)
        count_correct = 0

        for question in self.questions:
            if question.ask_and_evaluate():
               count_correct += 1

        score = (float(count_correct) / float(num_q)) * 100
        return score

    def __repr__(self):
        num_q = len(self.questions)
        return '{name} has {num_q} questions.'.format(name=self.name, num_q=num_q)

class Quiz(Exam):
    """Quiz inherits from Exam and is pass fail"""
    def __init__(self):
        """Initializes exam as quiz"""
        super(Quiz, self).__init__('Quiz')

    def adminter(self):
        """Adminsters exam as pass/fail quiz"""
        quiz_score = super(Quiz, self).adminter()
        if quiz_score > 50.0:
            return 1
        else:
            return 0

    def __repr__(self):
        num_q = len(self.questions)
        return '{name} has {num_q} questions'.format(name=self.name, num_q)


class StudentExam(object):
    """Stores student, exam and score information"""
    score = 100.0 # default A
    def __init__(self, student, exam):
        """Takes student and exam as objects"""
        self.student = student
        self.exam = exam   

    def take_test(self):
        """Administer the test"""
        self.score = self.exam.administer()
        print self.score

    def __repr__(self):
        return self.student, self.exam.name, self.score

class StudentQuiz(StudentExam):
    """Stores student, quiz and score info"""
    score = 1 # default A
    def __init__(self):
        """Initialize student quiz,  Exam passed will be quiz"""
        super(StudentQuiz, self).__init__()

    def take_test(self):
        """calls take test from parent, score depends on exam type passed"""
        super(StudentQuiz, self).take_test()

    def __repr__(self):
        return "Subclass of StudentExam. Is pass/fail"


def example():
    """test for the above classes"""
    exam = Exam('Final')
    exam.add_question('Is Canada a country?', 'Yes')
    exam.add_question('Is 2 + 2 = 4?', 'Yes')
    student = Student('Natasha', 'Mitchko', '529 28th st')
    student_exam = StudentExam(student, exam)
    print '__________ \n'
    print 'Begin Exam'
    print '__________ \n'
    student_exam.take_test()

example()















