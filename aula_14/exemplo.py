import boto3
import json

# Criar o cliente SNS
sns_client = boto3.client('sns', region_name='us-west-1')

# Criar a mensagem JSON
message = {
    "nome": "Luciano",
    "aula": "aula13"
}

# Publicar a mensagem no tópico SNS
response = sns_client.publish(
    TopicArn='arn:aws:sns:us-west-1:222634369390:MeuTopico',
    Message=json.dumps(message)
)

print(response)