import requests

#BASE_URL = "http://13.219.132.102:8080" qa
BASE_URL = "http://35.172.4.222:8080"

login_data = {
    "User_mail": "allanprod3",  
    "password": "1234"                
}

#login_response = requests.post(f"http://52.203.72.116:8080/login", json=login_data) qa
login_response = requests.post(f"http://100.25.74.174:8080/login", json=login_data)

if login_response.status_code != 200:
    print("Error al hacer login:", login_response.status_code, login_response.json())
    exit()

token = login_response.json().get("token")
print("Token:", token)

# endpoint edit
update_data = {
    "Name": "Video 2",
    "Lastname": "Production 2"
    #"Password": "1234"
}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

update_response = requests.patch(f"{BASE_URL}/update-user", json=update_data, headers=headers)

print("Status:", update_response.status_code)
print("Response:", update_response.json())
