from collections import Counter, namedtuple, defaultdict, deque

my_string = "aaaabbbccc"
count_dict = Counter(my_string)
print(count_dict)

# Prints one most common element
print(count_dict.most_common(1))

# Would give most repeated element of a string
print(count_dict.most_common(1)[0][0])

""" 
 namedtuple, Python’s namedtuple() is a factory function available in collections. It allows you to create tuple subclasses with named fields.
 You can access the values in a given named tuple using the dot notation and the field names.
"""
Point = namedtuple("Point", "x,y")
pt = Point(1, 2)
print(pt)

Course = namedtuple("Course", "course_name, course_id")
Student = namedtuple("Student", "name,age,gender,course")

course_1 = Course("Engineering", 1)
course_2 = Course("Art and Humanities", 2)
student_1 = Student("Bharat", 32, "Male", course_1)
student_2 = Student("Ram", 32, "Male", course_2)

print(student_2.name, student_2.age, student_2.gender, student_2.course.course_id, student_2.course.course_name)

# OrderedDict, from python 3.7, normal dictionary also remembers the sequence
normal_dict = {1: 1, 2: 4, 6: 36, 3: 9, 4: 16, 5: 25, 7: 49}
for key in normal_dict.keys():
    print(key)

# defaultdict, dictionary with default value

my_default_dict = defaultdict(int)
my_default_dict['a'] = 1
my_default_dict['b'] = 2
print(my_default_dict['a'])
print(my_default_dict['c'])

# deque, double ended queue

my_deque = deque()
my_deque.append('a')
my_deque.append('b')
my_deque.append('c')
my_deque.appendleft('x')
my_deque.append('y')
print(my_deque)

my_deque.extend(['d', 'e', 'f'])
print(my_deque)
my_deque.rotate(1)
print(my_deque)
my_deque.rotate(-1)  # Rotates to the left
print(my_deque)
