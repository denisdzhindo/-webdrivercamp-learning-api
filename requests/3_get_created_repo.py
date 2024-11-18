import requests
from pprint import pprint

def get_created_repo(url):
    token = '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'
    headers = {'Authorization': f'token {token}'}
    r = requests.get(url, headers=headers)
    repo = r.json()
    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'denisdzhindo'
    return repo

if __name__ == '__main__':

    owner = 'denisdzhindo'
    repo_name = 'repo-created-with-api'
    repo_url = f'https://api.github.com/repos/{owner}/{repo_name}'
    get_created_repo(repo_url)




