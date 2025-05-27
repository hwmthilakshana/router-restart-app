import requests
from requests.auth import HTTPBasicAuth

def restart_router(ip, username, password):
    url = f"http://{ip}/reboot.cgi"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            return "? Router reboot command sent."
        else:
            return f"? Failed. Status code: {response.status_code}"
    except Exception as e:
        return f"?? Error: {str(e)}"
