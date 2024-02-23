import json
import boto3

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('Polls')

    try:
        # Scan the table (consider using query and pagination in production)
        response = table.scan()

        # Extract items from the response
        polls = response['Items']

        # Return the list of polls
        return {
            'statusCode': 200,
            'body': json.dumps(polls)
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error retrieving polls')
        }

