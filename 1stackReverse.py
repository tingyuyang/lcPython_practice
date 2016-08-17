# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
# Header check: https://github.com/tingyuyang/lcPython_practice/blob/master/1stack.py

def revstring(mystr):
    # your code here
    s= Stack()
    for i in range(len(mystr)): # for char in mystr 
        s.push(mystr[i])        #s.push(char)
    result=""
    while not s.isEmpty():
        result=result+s.pop()
    return result
