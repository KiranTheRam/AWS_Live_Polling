import json
import boto3
import uuid
from datetime import datetime

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Parse the request body
    try:
        body = json.loads(event['body'])
    except:
        return {'statusCode': 400, 'body': json.dumps('Invalid request body')}

    question = body.get('question')
    options = body.get('options')

    if not question or not options or len(options) == 0:
        return {
            'statusCode': 400,
            'body': json.dumps('Poll question and options are required.')
        }

    # Generate a unique ID for the poll
    poll_id = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    # Prepare the item to insert into DynamoDB
    item = {
        'pollId': poll_id,
        'question': question,
        'options': options,
        'createdAt': created_at,
    }

    # Insert the item into the DynamoDB table
    table = dynamodb.Table('Polls')
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Poll created successfully', 'pollId': poll_id})
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error creating poll')
        }

