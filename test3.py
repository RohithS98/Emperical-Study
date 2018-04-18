import pickle
import requests

lang = "scala"
file = lang+".txt"
key = "match"

query = "https://api.github.com/search/code?q="+key+"+in:file+language:"+lang+"+repo:"

f = open(file,"rb")
temp = pickle.load(f)
a = pickle.load(f)
f.close()
print(temp[a])
req = requests.get(query+temp[a])
jr = req.json()
#print(jr)
print(len(jr['items']))

t = temp[a].split('/')
fn = t[1]+".txt"
with open(fn,"w") as f:
    for i in range(30):
        f.write(jr["items"][i]["git_url"])
        f.write('\n')
f.close()
'''
https://api.github.com/search/code?q=match+in:file+language:scala+repo:apache/spark
'''
