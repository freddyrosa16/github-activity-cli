import requests


def main():
    url = "https://api.github.com/users/freddyrosa16/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")


if "__main__" == __name__:
    main()
