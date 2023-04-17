lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = 0
    while(count<len(iterable)):
        yield start, iterable[count]
        start += 1
        count += 1

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
    
for i, lesson in my_enumerate(['a', 'b', 'c']):
    print("Lesson {}: {}".format(i, lesson))
    
for i, lesson in my_enumerate(['a', 'b', 'c'], 6):
    print("Lesson {}: {}".format(i, lesson))
    
for i, lesson in my_enumerate('python', 2):
    print("Lesson {}: {}".format(i, lesson))



def chunker(iterable, size):
    # Implement function here
    count = 0
            
    while(count < len(iterable)):
        begin = count
        count += size
        yield iterable[begin:count]

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
    
for chunk in chunker('python programming', 5):
    print(list(chunk))
    
