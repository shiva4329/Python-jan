# Escape Sequences:
            # \  -- escapes the immediate char, if ' or " converts into string
            # \\ -- removes the immediate slash and keeps the first slash
            # \n -- next line
            # \t -- tab sapce

# \'Python'\

print('\\\'Python\\\'')

# 'Rama' is a \\Good\\ boy

print('\'Rama\'')
print('\'Rama\' is a \\\\Good\\\\ boy')
# print('\\\\')

# how to print ---> \\Delhi\\ is a Capital of \\'\India\'\\

print('\\\\Delhi\\\\ is a Capital of \\\\\'\\India\\\'\\\\')

# Hw ---> \\It's\\ 'my' Country\\\\ 


# \n ---> nextline

print('python java')

print('python\njava')

print('python\nc++\njava\nRuby')
print('python\n\n\nc++\njava\nRuby')
print('\n')

# \t tab-space ---> 5 spaces == 1 tab

print('python java')
print('python\tjava')
print('python\t\t\t\tjava')


# sep ---> seperates the string using user defined literal (,/.)
# o/p = python,java
# o/p = python_java
# o/p = pythonjava
# o/p = python+java
x = 'python'
y = 'java'

print(x,y)
print(x,y,sep=',')
print(x,y,sep='_')
print(x,y,sep='')
print(x,y,sep='+')

# end ---> seperate the multiple prints with literal

x = 'python'
y = 'java'
z = 'c++'

print(x,end=',')
print(y,end=',')
print(z)