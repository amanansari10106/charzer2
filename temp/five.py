import hashlib
import hmac
import base64

@app.route('/notify_url/', methods=["POST"])
def notify_url_process():

 postData = {
  "orderId" : 200, 
  "orderAmount" : 200, 
  "referenceId" : request.form['referenceId'], 
  "txStatus" : request.form['txStatus'], 
  "paymentMode" : request.form['paymentMode'], 
  "txMsg" : request.form['txMsg'], 
  "txTime" : request.form['txTime'], 
 }

 signatureData = postData["orderId"] + postData["orderAmount"] + postData["referenceId"] + postData["txStatus"] + postData["paymentMode"] + postData["txMsg"] + postData["txTime"]

 message = bytes(signatureData).encode('utf-8')
 #get secret key from your config
 secret = bytes(secretKey).encode('utf-8')
 signature = base64.b64encode(hmac.new(secret, 
   message,digestmod=hashlib.sha256).digest())