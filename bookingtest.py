import requests
import base64

url = 'https://restful-booker.herokuapp.com/booking/2'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
}
data = {
    "firstname": "Lebron",
    "lastname": "James",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2020-10-20",
        "checkout": "2020-11-21"
    },
    "additionalneeds": "Massage session"
}

response = requests.put(url, json=data, headers=headers)

print(response.status_code)
print(response.json())