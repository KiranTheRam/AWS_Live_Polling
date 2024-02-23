import json
import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    try:
        # Assuming the poll ID is passed in the event body or as a path parameter
        # For API Gateway proxy integration, use 'pathParameters' or 'queryStringParameters'
        poll_id = event['pathParameters']['pollId']

        response = dynamodb.delete_item(
            TableName='Polls',
            Key={
                'pollId': {'S': poll_id}
            }
        )

        # Check the response for successful deletion
        # Note: delete_item does not throw an error if the item does not exist
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Poll deleted successfully'})
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error deleting poll')
        }

