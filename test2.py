import pickle

lang = "rust"
file = lang+".txt"
num = 0

with open(file,"r") as f:
    temp = f.read()
temp = temp.split('\n')
print(temp)

f = open(file,"wb")
pickle.dump(temp,f)
pickle.dump(num,f)
f.close()


f = open(file,"rb")
temp = pickle.load(f)
a = pickle.load(f)
f.close()
print(temp)
print(a)
