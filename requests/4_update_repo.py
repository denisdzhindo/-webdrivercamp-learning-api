import requests

def update_repo(url, token, new_description):
    headers = {
        'Authorization': f'token {token}',
        'Accept':'application/vnd.github.v3+json'}
    data = {
        'description': new_description
    }
    r = requests.patch(url, headers=headers, json=data)
    if r.status_code == 200:
        print(f'Response status code: {r.status_code}'
              f'\nSuccessfully updated repo')
    else:
        print(f'\nResponse status code: {r.status_code}'
              f'\nFailed to update {repo_name} description'
              f'\nResponse: {r.json()}')

if __name__ == '__main__':

    my_token = ''
    my_new_description = 'I know Python  Requests'
    owner = 'denisdzhindo'
    repo_name = 'repo-created-with-api'
    my_url = f'https://api.github.com/repos/{owner}/{repo_name}'

    update_repo(my_url, my_token, my_new_description)
