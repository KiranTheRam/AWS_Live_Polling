import json
import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Extract the pollId from the event object. Adjust this line based on how you're invoking the Lambda function
    poll_id = event['queryStringParameters']['pollId']

    try:
        response = dynamodb.get_item(
            TableName='Polls',
            Key={
                'pollId': {'S': poll_id}
            }
        )

        # Check if the item exists
        item = response.get('Item', None)
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Poll not found'})
            }

        # Convert the DynamoDB item to JSON
        poll_details = {k: list(v.values())[0] for k, v in item.items()}

        return {
            'statusCode': 200,
            'body': json.dumps(poll_details)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error retrieving poll details')
        }

