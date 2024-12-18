import json

def lambda_handler(event, context):
    param = event.get("action")
    print(f"event={event}")
    return {
        "application": "v.1"
        }
