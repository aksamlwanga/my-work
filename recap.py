print("hello world")
message="hello' world"
# slicing 
print (message[2:])
# calling methods to a variable  
# method include find ,count,lower,replace for strings

print (message.upper())

# learning on how to use a method 
# print(dir(message))
# wanting to learn a specific method then you can use the code below

# print(help(str.lower))
# power operator **, mult * ,add + ,div / ,int div //
print (6**2)
print(3*2+2)
print(3*(2+2))
x=2
x*=-10.33
# print(help(int)) 

# creating lists
course=['his','fddd','dfd']
print(course[-2])
# grab put of the list course[:2],course[1:3]
# methods used in list insert ,append ,extend,remove,pop,reverse,sort,sort(reverse=True),sorted,min,max,sum,index,in operator,enumerate,join ,split  
course.insert(0,2)
print(course)

# tuple are immutable and cant change their values once define ()
# sets use the set brackets and dot allow duplicates ,methods include intersection ,.union 
# creating empty lists,set,set
# e=[],empty=list(),emyt=(),tuple(),set()


# dictionary in 
aksam={'aksam':'23','ske':'w'}
print (aksam)
aksam['phone']=6688999
# print(aksam['phone'])
# print(aksam.get('phone')) method update,del ,pop,len,keys,values,items 

# we have entered if statent
if 2>3:
    print (true)
elif 3>2:
    print(12)    
else:
    print (False)
    # use the following for for >,=,==,!= ,and ,or .
    # , not, is looks at memory location id 
    # none false 0 will evaluate to false and any empty variable  
    #   welcome to functions in python
    # def  is the key world used to define a function
# loops in python
nums=[1,2,3,4,5]
for num in nums:
    if num==4:
        # continue and break in loops 
        for letter in "abcd":
           print(num,letter)
        for i in range(10):
            print(i)
        z=0
        while z<5:
            print(z)
            z+=1


# function definition 
def hello():
     print(123)
 #function call 
hello()
hello()
hello()
def hello():
    return 'aksam is good in cod'
print(hello())

# passing an argument to function 

def hello(great):
    return '{} function .'.format(great)
print(hello('aksam'))
# further more *args and **kwargs args are tuples and kwargs is a set dictionary
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
# student_info('math','art',nask='sdd',sjj=22)
courses=['math','art']
info={'nsmr':'sksk','age':22}
student_info(*courses,**info)
import antigravity