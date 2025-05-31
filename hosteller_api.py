import requests

def get_room_otp(ezee_booking_id):
    url = "https://api.thehosteller.com/api/graphql"
    headers = {
        "accept": "*/*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "null",
        "content-type": "application/json",
        "origin": "https://www.thehosteller.com",
        "referer": "https://www.thehosteller.com/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    }

    payload = {
        "query": """
        query getRoomDoorOtpNew($ezeeBookingID: ID) {
            getRoomDoorOtpNew(ezeeBookingID: $ezeeBookingID) {
                roomOtp
                success
                message
                roomNo
            }
        }""",
        "variables": {
            "ezeeBookingID": ezee_booking_id
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["data"]["getRoomDoorOtpNew"]

