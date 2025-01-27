import requests


def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data = response.json()
    # print(data)

    if data["success"] and "data" in data:
        user_data = data["data"]
        userID = user_data["id"]
        username = user_data["name"]
        email = user_data["email"]
        return userID, username, email


def main():
    data = fetch_api()
    # print(data[0], data[1]["title"])
    userId, username, email= fetch_api()
    print(f"UserID: {userId} \nEmail: {email}")
    for i in username:
        print(f"{username[i]}", end=" ")
        # print(f"{i}: {username[i]}")

if __name__ == "__main__":
    main()