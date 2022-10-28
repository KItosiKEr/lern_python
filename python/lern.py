f = {'frame':1, 'gas' :5}
print(f['gas'])



royale = {'name' :{'last_n' : 'некит' ,'first_n' :'hhh'} ,'molo' :{'kolom': 'чё' , 'pol': 'jooj'} , 'number' :{'first_num':'0557914181' , 'secend_num':'0556394798'} }
print (royale['name'] ['first_n'] )
print(royale['molo'] ['pol'])
print(royale['number'] ['first_num'])

#множества,варианты записи
a = set("hello")
print(a)

b = {2}
print(b) 

def funk (x , y):
    return x + y
print(funk(23,88))


#выявление ошибок try-except
x = int (input ())
y = int (input ())
try:
          res = x / y
except ZeroDivisionError:
     res = 'do not divide by '
print(res)

g = open("lern.py/python.txt", "w")
print(g.write ("hello"))