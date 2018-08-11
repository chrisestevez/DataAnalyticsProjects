import timeit


setup = '''
import numpy
import copy
import random

#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):

    for j in xrange(0, len(input) - 1):
        for i in xrange(0, len(input) - 1):
            if(input[i]> input[i+1]):
                test = input[i]
                input[i]= input[i+1]
                input[i+1]=test
    return input
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop

def sortwithoutloops(input):
    return sorted(input)

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions

def searchwithloops(input, value):
    result = False
    for i in input:
        if i == value:
            result = True
            break
    return result
# 4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input

def SortNumpy(input):
    return numpy.sort(input)

def SearchNumpy(input, value):
    return value in input

#http://stackoverflow.com/questions/4172131/create-random-list-of-integers-in-python

List = [random.randint(0, 9999) for r in xrange(500)]

NumpArray = numpy.array(List)

rand = random.randrange(0,9999)

'''

if __name__ == "__main__":	
    #reduced execution to 1000 and range to 500 due to execution time

    n = 1000

print "-----------------------Sorting---------------------"
t = timeit.Timer("x=copy.copy(List); sortwithloops(x)", setup=setup)
print 'Sort With loops     :', t.timeit(n), " seconds"

t = timeit.Timer("x=copy.copy(List); sortwithoutloops(x)", setup=setup)
print 'Sort with no loops   :', t.timeit(n), " seconds"

t = timeit.Timer("x=copy.copy(NumpArray); SortNumpy(x)", setup=setup)
print 'Sort with Numpy      :', t.timeit(n), " seconds"


print "-----------------------Search----------------------"

t = timeit.Timer("x=copy.copy(List);y = copy.copy(rand); searchwithloops(x,y)", setup=setup)
print 'Search With loops    :', t.timeit(n), " seconds"

t = timeit.Timer("x=copy.copy(List);y = copy.copy(rand); searchwithoutloops(x,y)", setup=setup)
print 'Search with no loops :', t.timeit(n), " seconds"

t = timeit.Timer("x=copy.copy(NumpArray);y = copy.copy(rand); SearchNumpy(x,y)", setup=setup)
print 'Search with Numpy    :', t.timeit(n), " seconds"

'''
print sortwithloops(L) #[3, 3, 5, 5, 6, 6, 13]
print sortwithoutloops(L) #[3, 3, 5, 5, 6, 6, 13]
print searchwithloops(L,5) #true
print searchwithloops(L,11) #false
print searchwithoutloops(L,5) #true
print searchwithoutloops(L,11) #false

'''
