import requests
import json
url = 'https://test.cashfree.com/api/v2/cftoken/order'
# myobj = {'orderId': 'order0001'}

# x = requests.post(url, data = myobj)

# print(x.text)
headers = {'x-client-id': '83488cf107b44fbaf54461cd388438',"Content-Type":"application/json", "x-client-secret":"70418e3b9c135089c4713933e8339b140ab994a9"}
myobj = {"orderId":200,"orderAmount":200,"orderCurrency":"INR"}
r = requests.post(url, headers=headers, data=json.dumps(myobj))
print(r.json())