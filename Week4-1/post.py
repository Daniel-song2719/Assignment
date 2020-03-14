import requests, json

github_url = "https://api.github.com/user/repos"

data = json.dumps({'name' : 'test', "discription" : 'some test repo'})
r = requests.post(github_url, data=data, auth= ('', ''))


print(r.json)