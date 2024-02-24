import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    poll_id = event['pathParameters']['pollId']

    if not poll_id:
        return {'statusCode': 400, 'body': json.dumps('Poll ID is required.')}

    votes_table = dynamodb.Table('Votes')

    try:
        # Scan operation for demonstration; consider using Query with an Index in production
        response = votes_table.scan(
            FilterExpression='pollId = :pollId',
            ExpressionAttributeValues={':pollId': poll_id}
        )

        votes = response['Items']
        results = {}  # Dictionary to hold the count of votes for each option

        for vote in votes:
            selected_option = vote['selectedOption']
            results[selected_option] = results.get(selected_option, 0) + 1

        return {
            'statusCode': 200,
            'body': json.dumps({'pollId': poll_id, 'results': results})
        }

    except Exception as e:
        print(e)
        return {'statusCode': 500, 'body': json.dumps('Error retrieving vote results')}
