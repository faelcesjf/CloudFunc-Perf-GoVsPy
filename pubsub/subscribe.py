from google.cloud import pubsub_v1
from google.oauth2 import service_account

def callback(message):
    print(f"Recebida a mensagem: {message}")
    print(f"Conteúdo da mensagem: {message.data.decode('utf-8')}")
    message.ack()

def subscribe_messages(project_id, subscription_id, key_path):
    credentials = service_account.Credentials.from_service_account_file(key_path)
    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    print(f"Escutando mensagens na assinatura {subscription_path}...")
    future = subscriber.subscribe(subscription_path, callback)

    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()
