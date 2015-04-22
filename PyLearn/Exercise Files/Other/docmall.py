
import urllib.request
import requests as req



'''
account = "DMSERVICE"
user = "jwhelan"
password = "pas2468DM?"
appid = "q8wmfdj47fdkcx01"
url = r"https://dmapi.documentmall.com/dmapi/"
login ="login.do"
port = "443"
'''

#x = urllib.request.urlopen('https://dmapi.documentmall.com/dmapi/login.do')
#print(x.read)
url = "https://dmapi.documentmall.com/dmapi/login.do"
values = { "account":"DMSERVICE","username":"jwhelan","password":"pas2468DM?","appid":"q8wmfdj47fdkcx01"}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
s = urllib.requests.session()
print(respData)




