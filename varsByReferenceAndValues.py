# RULE TO LIVE BY:

# Immutable Data Types are int, float, strings, bools, sets
    # If a var is immutable, it doesn't matter if we use an = to copy to another var
    # The value cannot chqange. We can change it anywhere and the other variables will
    # not be affected

# Mutable data types= list, dict, sets, objects
    # if a var is mutable, if you copy with an = sign, then anywhere you change it will change
    # it everywhere
    # x = []
    # y = x
    # x.append(1)
    # you have changed y
    # x = []
    # y = x.copy() #y and x are not totally independent

# To make a copy that will not change the original, use the copy() method
# This copies the value, not the pointer. This will make it independent 

# #id will give us a unique integer to represent this bit of code
# x = 3
# y = x #we are pointing y at x until the value of one changes
# print(id(x)) # same value as line below b/c 3 is immutable
# print(id(y)) # same value as line above b/c 3 is immutable
# x += 1 #will make x 4
# print(id(x)) # values have diverged
# print(id(y))
# x -= 1 #will make x 3 again
# print(id(x)) # uses initial location in memory b/c 3 is already stored there
# print(id(y))

# z = 3
# print(id(x))
# print(id(y))
# print(id(z))


# x = []
# print(id(x))
# x.append(1)
# print(id(x))
# y = x
# print(id(y))
# x.append(2)
# y.append('hello')
# print(id(x))
# print(id(y))

def fight(monster):
    #based on when we talked about scope (local,global)
    # will this thing be changeable?
    monster.append(5)
    print(id(monster))

enemies = [1,2,3]
print((id(enemies)))
fight(enemies) # we are passing a global to a function
print((id(enemies.copy())))
print((enemies))
