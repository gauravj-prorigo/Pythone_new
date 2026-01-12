with open('D:\Python\Pythone(12-1-25)\data.txt') as f: 
 data=[]
 for x in f:
    x = x.lower().strip()
    data.append(x)

with open('D:\Python\Pythone(12-1-25)\output.txt','w') as f: 
    f.write("\n".join(data))