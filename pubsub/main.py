from publish import publish_messages
from subscribe import subscribe_messages

def main():
    project_id = "containers-362511"
    subscription_id = "dec-sub"
    topic_id = "dec"
    data_file = "data.json"
    key_path = "gcp_service_account.json"
    
    #publish_messages(project_id, topic_id, data_file, key_path)
    subscribe_messages(project_id, subscription_id, key_path)

if __name__ == '__main__':
    main()
    
    
    

