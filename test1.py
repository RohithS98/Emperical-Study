import requests

lang = "java"
tempurl = "https://api.github.com/search/repositories?q=+language:"
tempurl += lang+"&sort=stars&order=desc&per_page=100"

req = requests.get(tempurl)
print(req)
jr = req.json()
print(len(jr["items"]))
with open(lang+".txt","w") as f:
    for i in range(100):
        f.write(jr["items"][i]["full_name"])
        f.write('\n')
