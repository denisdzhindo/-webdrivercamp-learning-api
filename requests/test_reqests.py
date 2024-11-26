import requests

#r = requests.get('https://xkcd.com/353/') # ger requests
# print(r)

# print(dir(r))
# print(help(r)) # everything of this object
# print(r.text) # HTML of the website

# r = requests.get(' https://imgs.xkcd.com/comics/python.png') # png image from that website
# print(r.content) # content of that png image

# with open('comic.png', 'wb') as f:  # downloaded the website png picture
    # f.write(r.content)

# print(r.status_code)
# print(r.ok) # this return True for anything below 400 responds, so if client/server error - returns False
# print(r.headers)

''' 
# get
payload = {'page': 2, 'count': 25} # add parameters to url
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text) # print got requests
print(r.url)
'''

'''
# post
payload = {'username': 'denis', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text) # prints the request
# print(r.json()) # prints JSON dict
r_dict = r.json()
print(r_dict)
print(r_dict['form'])
'''

# http://httpbin.org/#/HTTP_Methods get Auth/Get url /basic-auth/{user}/{passwd}
# Prompts the user for authorization using HTTP Basic Auth
# https://httpbin.org/basic-auth/denis/testing - run this url and get auth name/pass

'''
r = requests.get('https://httpbin.org/basic-auth/denis/testing', auth=('denis', 'testing'))
print(r.text)

r = requests.get('https://httpbin.org/basic-auth/denis/testing', auth=('deniss', 'testing'))
print(r) # prints 401 error - unauthorized user
'''

# r = requests.get('https://httpbin.org/delay/6', timeout=3) # make timeout if a page is not loading
# print(r)


