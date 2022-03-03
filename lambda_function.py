import urllib3 
import json
http = urllib3.PoolManager() 
def lambda_handler(event, context): 
    url = "https://hooks.slack.com/services/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"    
    msg = {
        "channel": "aws-notifications",
        "username": "WEBHOOK_USERNAME",
        "text": event['Records'][0]['Sns']['Message'],
        "icon_emoji" : ""
    }
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })