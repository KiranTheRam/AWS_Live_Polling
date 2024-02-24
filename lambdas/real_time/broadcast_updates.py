import boto3
import json

dynamodb = boto3.resource('dynamodb')
client = boto3.client('apigatewaymanagementapi', endpoint_url='https://{apiId}.execute-api.{region}.amazonaws.com/{stage}')

def lambda_handler(event, context):
    table = dynamodb.Table('WebSocketConnections')
    scan = table.scan()
    connections = scan['Items']

    payload = {'action': 'broadcastUpdate', 'data': event['detail']}

    for connection in connections:
        connection_id = connection['connectionId']
        try:
            client.post_to_connection(
                ConnectionId=connection_id,
                Data=json.dumps(payload)
            )
        except client.exceptions.GoneException:
            # Handle disconnected clients
            table.delete_item(Key={'connectionId': connection_id})

    return {'statusCode': 200, 'body': 'Message broadcasted'}
