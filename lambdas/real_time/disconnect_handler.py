import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
    table = dynamodb.Table('WebSocketConnections')

    # Remove the connection
    table.delete_item(Key={'connectionId': connection_id})

    return {'statusCode': 200, 'body': 'Disconnected'}
