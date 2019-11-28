import requests


data = {
	"first": "one",
	"second": "two"
}

r = requests.post("http://127.0.0.1:5000/", data=data)

print(r.status_code)
