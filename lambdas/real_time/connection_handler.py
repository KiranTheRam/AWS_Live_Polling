import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
    table = dynamodb.Table('WebSocketConnections')

    # Store the new connection
    table.put_item(Item={'connectionId': connection_id})

    return {'statusCode': 200, 'body': 'Connected'}
