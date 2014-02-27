import random
import math
import time
import urllib2

def s4():
    result = (1 + random.random())*65536
    result = math.floor(result)
    result = "%x" % result
    return result[1:] 

def create_token():
    token = ""
    for i in range(8):
        token += s4()
    return token

def send_reg(username,password,token,code):
    data = {"username":username,"password":password,
            "password2":password,"captcha":code,"token":token,
            "client_id":1014,"ru":"http://mail.sogou.com/2gmail/login.jsp"
            }
    import urllib
    data = urllib.urlencode(data)
    content = urllib2.urlopen("https://account.sogou.com/web/reguser",data)
    response = content.read()
    print response

if __name__ == "__main__":
    token = create_token()
    url = "https://account.sogou.com/captcha?token=%s&t=%d" % (
           token,int(time.time()*1000))
    import os
    os.system(r"C:\Users\shujy\AppData\Local\Google\Chrome\Application\chrome.exe " + url)
    code = raw_input("press the code:\n")
    username = "baseak2ak283"
    password = "abc123"
    send_reg(username,password,token,code)
    raw_input("press")