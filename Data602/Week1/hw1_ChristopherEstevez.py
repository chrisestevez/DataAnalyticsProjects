#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
     ''''    NewList = []
         while input:
           min = input[0]
           for x in input:
             if x < min:
              min = x
         NewList.append(min)
         input.remove(min) '''''

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
    for i, myval in enumerate(input):
        if value == myval:
            return True
        elif value <> myval:
            return False


#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    return value in input

if __name__ == "__main__":	
   L = [5,3,6,3,13,5,6]

print sortwithloops(L) #[3, 3, 5, 5, 6, 6, 13]
print sortwithoutloops(L) #[3, 3, 5, 5, 6, 6, 13]
print searchwithloops(L,5) #true
print searchwithloops(L,11) #false
print searchwithoutloops(L,5) #true
print searchwithoutloops(L,11) #false

