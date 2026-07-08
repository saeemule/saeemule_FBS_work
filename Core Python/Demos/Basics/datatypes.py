####Text
#1. str
var = 'First"bit" Solutions'
print(type(var))
var = "Firstbit's Solutions"
print(type(var))
var = '''This is First Line.
This is second line.'''
print(type(var))

var = """This is First Line.
This is second line."""


print(type(var))


####Sequential
#1. List
var = [10,20,30,40]
print(type(var))
#2. tuple
var = (10,20,30,40)
var = 10,20,30,40  #tuple
print(type(var))
#3. range
var = range(1,100000)

print(type(var))



###Set type
#1. Set
var={10,20,30,40}
print(type(var))
#2. frozenset
var = frozenset({10,20,30,40})
print(type(var))

###Mapping
#1. dist
var ={'id':101, 'name':'Apurva','sal':30000}
print(type(var))

####other
#1. bool
var =True
print(type(var))
#2. NOnetype
var= None

print(type(var))
