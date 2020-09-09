t=(10,73,84,928,83,73)
print(type(t))
print(t[0])
print(t[-1])
print(t[1])
print(t[1:4])
t[0]= 7777 # This will through error
t.append(100) # n/a
t.remove(10) # n/a
t=(10) # This will be integer
t=(10,) # this will be considered as tuple  