import requests

def delete_repo(url):
    token = ''
    header = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github+json'}
    r = requests.delete(url, headers=header)
    print(f'Response status code: {r.status_code}')

if __name__ == '__main__':

    owner = 'denisdzhindo'
    repo_name = 'repo-created-with-api'
    my_url = f'https://api.github.com/repos/{owner}/{repo_name}'


    delete_repo(my_url)

