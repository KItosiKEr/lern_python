e = open("python.txt" , "w")
e.write('hello')
e.close()

with open ('text.txt','wt', encoding='utf-8') as infile:
    num = int(input())
    line =str('1/' +str(num )+ '='+str(1/num))
    print(line)
    infile.write(line)
