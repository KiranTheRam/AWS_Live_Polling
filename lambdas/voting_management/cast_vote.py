import json
import boto3
from datetime import datetime
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    poll_id = body.get('pollId')
    selected_option = body.get('selectedOption')
    user_id = body.get('userId')  # Ensure you have authenticated the user's identity

    if not poll_id or not selected_option:
        return {'statusCode': 400, 'body': json.dumps('Poll ID and selected option are required.')}

    votes_table = dynamodb.Table('Votes')

    try:
        vote_id = str(uuid4())
        now = datetime.now().isoformat()

        vote_item = {
            'voteId': vote_id,
            'pollId': poll_id,
            'selectedOption': selected_option,
            'userId': user_id,
            'timestamp': now
        }

        votes_table.put_item(Item=vote_item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Vote cast successfully', 'voteId': vote_id})
        }

    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Error casting vote')}

