import requests


def main():
    url = "https://api.github.com/users/freddyrosa16/events"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Request failed:", response.status_code)
        return 

    events = response.json()

    print("Output: ")
    for event in events:
        event_type = event["type"]
        repo = event["repo"]["name"]

        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            print(f"Pushed {len(commits)} commits(s) to {repo}")

        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type")
            print(f"Created a {ref_type} in {repo}")

        elif event_type == "WatchEvent":
            print(f"Starred {repo}")

        elif event_type == "ForkEvent":
            print(f"Forked {repo}")

        elif event_type == "IssuesEvent":
            action = event["payload"].get("action")
            print(f"Issues {action} in {repo}")
        else:
            print(f"{event_type} in {repo}")


if __name__ == "__main__":
    main()
