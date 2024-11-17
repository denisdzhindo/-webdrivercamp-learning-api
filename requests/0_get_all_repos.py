import requests

def get_repos(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        count = data.get('total_count', 0)  # Get the total count of repositories
        list_ = data.get('items', [])  # Get the list of repositories under 'items'

        list_of_items_sorted = sorted(list_, key=lambda item: item['full_name'].lower())

        return list_of_items_sorted, count, response.status_code
    else:
        print(f"Error: {response.status_code}")
        return [], 0, response.status_code  # Return empty list and zero count in case of an error


if __name__ == "__main__":

    wlp_url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"
    list_of_items, total_count, status_code = get_repos(wlp_url)

    for element in list_of_items:
        user = element['owner']['login']  # Get the owner username
        repo = element['name']  # Get the repository name
        print(f"{user:15}", repo)

    print(f"\nResponse status code: {status_code}")
    print(f"Total count of found items: {total_count}")
