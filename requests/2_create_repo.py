import requests
from pprint import pprint

def create_repo(url):
    token = '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'
    headers = {'Authorization': f'token {token}'}
    data = {'name': 'repo-created-with-api','private': True,'has_wiki': False}
    r = requests.post(url, headers=headers, json=data)
    print("Response status code:", r.status_code)
    json_object = r.json()
    json_object.popitem()
    return json_object

if __name__ == '__main__':

    my_url = 'https://api.github.com/user/repos'
    repo = create_repo(my_url)
    pprint(repo)