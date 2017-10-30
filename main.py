########### Python 2.7 #############
import json
import urllib
import requests
img_local_path = 'C:\\Users\\jiayi\\Desktop\\test.jpg'
# Replace the subscription_key string value with your valid subscription key.
subscription_key = your key
url_base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect' # 在微软账号申请的免费API用这个
# url_base = 'https://api.cognitive.azure.cn/face/v1.0/detect'#在azure申请的用这个
# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
data = open(img_local_path, 'rb')
# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,hair,makeup',
})

conn = requests.post(url_base, headers=headers, data=data,params=params)
data = conn._content
print 'data',data
# 'data' contains the JSON data. The following formats the JSON data for display.
parsed = json.loads(data)[0]['faceAttributes']
gender = parsed['gender']
age = parsed['age']
# conn.close()
print gender,age,parsed
