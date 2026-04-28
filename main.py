import requests


def main():
    print("Output:")
    url = "https://api.github.com/users/freddyrosa16/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for event in data:
            event_type = event["type"]
            repo_name = event["repo"]["name"]

            if event == "PushEvent":
                commit_count = event["payload"].get("size", 0)
                print(f"Pushed {commit_count} commits to {repo_name}")
    else:
        print(f"Error: {response.status_code}")


if "__main__" == __name__:
    main()
