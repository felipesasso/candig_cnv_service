import requests


class testHeader():
    def __init__(self, headers):
        self.headers = headers

    def headers(self):
        return self.headers


def get_headers():
    request_handle = requests.Session()
    creds = {"username": "candig_dev", "password": "password"}
    token = request_handle.post("http://ga4ghdev01.bcgsc.ca:8008/auth/token", json=creds)
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               "content-type": "application/json",
               "federation": "false",
               "Authorization": "Bearer " + token.json()['id_token']
               }

    return headers


goodHeader = testHeader(get_headers())


badHeader = testHeader({
        "Content-Type": "application/json",
        "Host": "ga4ghdev01.bcgsc.ca:8890",
        "User-Agent": "python-requests/2.22.0",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsI",
        "Federation": "true"
    })

access_list = {
    ("candig_dev", "http://ga4ghdev01.bcgsc.ca:8080/auth/realms/CanDIG"): {
        "TF4CN": 4,
        "PROFYLE": 3,
        "TEST0": 0,
        "TEST1": 1,
        "TEST2": 2,
        "TEST3": 3,
        "TEST4": 4
    }
}