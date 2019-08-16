#    uses Sublime Text  # youtube.com/watch?v=3dt4OGnU5sM

nums = [1,2,3,4,5,6,7,8,9,10]

# easiest loop
# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
#print my_list  # this form of print only usable in python2
print (my_list)

my_list2 = [n for n in nums]
print (my_list2)

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
#print my_list  # this form of print only usable in python2
print (my_list)

my_list2 = [n*n for n in nums]
print (my_list2)

# Using a map + lambda
my_list = map(lambda n: n*m, nums)
print(my_list)  # WTF prints out: <map object at 0x106dd0d50>

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

#my_list2 = [n for even(n) in nums]
my_list2 = [n for n in nums if n%2 == 0]
print (my_list2)
