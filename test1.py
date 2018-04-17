import requests

lang = "scala"
tempurl = "https://api.github.com/search/repositories?q=+language:"
tempurl += lang+"&sort=stars&order=desc&per_page=50"

req = requests.get(tempurl)
print(req)
jr = req.json()
print(len(jr["items"]))
with open(lang+".txt","w") as f:
    for i in range(50):
        f.write(jr["items"][i]["full_name"])
        f.write('\n')
    
