import pickle
import requests

lang = "scala"
file = lang+".txt"
key = "match"

query = "https://api.github.com/search/code?q="+key+"+in:file+language:"+lang+"+per_page=100+repo:"

f = open(file,"rb")
temp = pickle.load(f)
a = pickle.load(f)
f.close()
print(temp[a])
req = requests.get(query+temp[a])
jr = req.json()
print(jr)
print(len(jr['items']))

with open(temp[a]+".txt","w") as f:
    for i in range(100):
        f.write(jr["items"][i]["full_name"])
        f.write('\n')

'''
https://api.github.com/search/code?q=match+in:file+language:scala+per_page=100+repo:apache/spark
'''
