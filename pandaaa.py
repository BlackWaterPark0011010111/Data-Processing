import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford", 'Mercedes'],
#   'passings': [3, 7, 2, 6]
# }

# df = pd.DataFrame(mydataset,index = ["BMW", "Ford", "Mercedes"])

# #print(df)

# print(df.loc[[ "BMW"]])
# print(df.loc[[ "BMW"]])


mydata = pd.read_csv('cities.csv')
print(mydata)
#print(mydata.to_string())#use the whole list
#print(mydata.loc[[0,33]])
print(mydata.info())#сколько всего и чего именно было использовано
#new_df = mydata.dropna()#remove empty files
#print(new_df.to_string())
##print(new_df.info())




# meanVal = mydata['LonS'].mean()
# print(meanVal)

# medianVal = mydata['LonS'].median()
# print(medianVal)

# modeVal = mydata['LonS'].mode()
# print(modeVal)

# mydata['LonS'].fillna(medianVal, inplace=True)
# print(mydata.to_string())
# print(mydata.info())



# nums = [4,1,2,8,7,5,3,9,6]
# print(sorted(nums))
# print(nums)

# dict = {'a':2,'b':4,'c':3}
# #print(sorted(  dict1))
# #print(sorted(dict1.values()))

# #print(sorted(dict1, reverse=True))

# dict1 = [
#   {"name": "John", "age": 31},

#   {"name": "Mary", "age": 46},

#   {"name": "Lucy", "age": 25}
#    ]


list = [

    {'brand' :'bmw', 'stock':300},
    {'brand': 'audi', 'stock':300},
    {'brand' :'mers', 'stock':300}

]

sortee = sorted(list,key = lambda items:items['brand'])
print(sortee)
####ТОЖЕ САМОЕ ТОЛЬКО С ОБЫЧНОЙ ФУНКЦИЕЙ
def soort(item):
    return item['stock']