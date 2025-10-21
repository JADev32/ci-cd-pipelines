import json

def lambda_handler(event, context):
    # TODO implement
    print("¡Hola desde el código v1!") # Mensaje inicial
    return {
        'statusCode': 200,
        'body': json.dumps('¡Hola desde Lambda v1!')
    }