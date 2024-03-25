from google.cloud import pubsub_v1
from google.oauth2 import service_account
import json

def load_json_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"O arquivo {file_path} não é um JSON válido.")
        return []

def publish_messages(project_id, topic_id, data_file, key_path):
     credentials = service_account.Credentials.from_service_account_file(key_path)
     publisher = pubsub_v1.PublisherClient(credentials=credentials)

     topic_path = publisher.topic_path(project_id, topic_id)

     messages = load_json_from_file(data_file)
     total_messages = len(messages)
     print(f"Total de mensagens: {total_messages}")

     for message in messages:
         if isinstance(message, str):
             message_json = message
         else:
             message_json = json.dumps(message)

         try:
             message_future = publisher.publish(topic_path, data=message_json.encode('utf-8'))
             print(f"Mensagem publicada: {message_future.result()}")
         except Exception as e:
             print(f"Ocorreu um erro ao publicar a mensagem: {e}")

