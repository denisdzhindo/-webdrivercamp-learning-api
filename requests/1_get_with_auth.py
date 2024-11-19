import requests

def get_with_auth(url, token):
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print(f"\nResponse status code: {r.status_code}")
        data = r.json()
        list_of_headers = []
        for item in data:
            list_of_headers.append(item.get('name', None))
        return list_of_headers
    else:
        print(f"Error code: {r.status_code}")
        return []

my_url = "https://api.github.com/user/repos"
my_token = ''
my_headers_list = get_with_auth(my_url, my_token)
print(f"Total repos: {len(my_headers_list)}\n\nResponse headers:\n{"\n".join(my_headers_list)}")




