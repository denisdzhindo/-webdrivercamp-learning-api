import requests

r = requests.get('https://xkcd.com/353/')
print(r)

# print(dir(r))
# print(help(r)) # everything of this object
# print(r.text) # html of the website

r = requests.get(' https://imgs.xkcd.com/comics/python.png') # png image from that website
# print(r.content) # content of that png image

with open('comic.png', 'wb') as f:
    f.write(r.content)


