import pandas as pan

dict = {
'a' : 1,
'b' :2,
'c' :[11,22,3,345,]

} 

print('static coding', dict['c'][1])

def foorloop(position=0):# func - added a default value to the arg
    for  key,value in dict.items():
        if type(dict[key]) == type([]): #lists only 
            print('dynamic coding',dict[key][position])
        print(type(dict[key]), value)


def read(x):
    print('something ', x)
    
read(dict['c'])

list = [1,2,3,4,5,6,7,8,9,10]
print(str(list))
print(type(str(list)))

list = [1,2,3,4,5,6,7,8,9,10]
# list2=[f'{str(x)}0' for x in list]
list2=[]
# def four():

# if x in list:
#     print(x, +'0')

for x in list: #looping through a list
    x = str(x)
    list2.append(f'{x}0') #adding new values to lists

print(list2)

dict.update({'d':4}) #adding new items to a dictionary
dict['e']=['a','z','x'] #adding new item to dictionary

print(dict)
foorloop(2) #callback


# #to compare 
# #to assign 



# a= 4=='4'
# print(a)