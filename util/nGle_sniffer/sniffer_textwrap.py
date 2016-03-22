from websocket import create_connection
import base64
import json

server = "wss://beta-session-ap-northeast-1-zinny.nzincorp.com/session"

data = [
    "auth://v2/zd3/createToken",
    {
        "txNo": 75409245
    },
    {
        "appId": "test03",
        "appSecret": "67fcd4ed73ead0f278ba43e7d5c72afd292ebead",
        "appVer": "0.1.0",
        "sdkVer": "2.12.0",
        "os": "android",
        "market": "appStore",
        "deviceId": "850ABE8CC42A824348813A28BCA426A8EBB3205399782E3C07883DF30CDFD1BC",
        "serialNo": "1234567890"
    }
]


data = json.dumps(data)
# encoded = base64.b64encode(data)
# send_data = server + "?request=" + encoded
# print send_data

# ws = create_connection(send_data)
# ws.send('')

ws = create_connection(server)
ws.send(data)

result =  ws.recv()
print "Received '%s'" % result
ws.close()