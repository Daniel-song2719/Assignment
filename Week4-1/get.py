import requests
import webbrowser

search = '18A Nguyễn Thị Minh Khai'
queryString = {'q' : search}
searchEngine = 'https://www.google.com/maps/?hl=ko'
r = requests.get(searchEngine, params=queryString)
 
print(r.url)
webbrowser.open(r.url)

