with open("D:\Python\Pythone(12-1-25)\data.txt") as f:
    text = f.readlines()

print(text)    
    
data = []
for line in text:
     line = line.replace(" ", "_").lower()   
     data.append(line)                


with open("D:\Python\Pythone(12-1-25)\output2.txt",'w')as f:
    f.write("".join(data))