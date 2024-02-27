import requests

def getUserCount():
    users = 0
    # Making a GET request
    url = 'https://api.resonite.com/sessions'
    try:
        response = requests.get(url).json()
        # Sum up the activeUsers from json
        for entry in response:
            users += entry.get("activeUsers", 0)
        print("Total active users:", users)
        return users
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    except ValueError as e:
        print("JSON decoding failed:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


    
