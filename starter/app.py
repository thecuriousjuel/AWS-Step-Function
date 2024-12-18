import json

def lambda_handler(event, context):
    region = event.get("region")
    application_name = event.get("application")
    print(f"event={event}")
    
    response = {
        "isList": False,
        "isString": False
        "runApplication1": False
        "runApplication2": False
    }

    if isinstance(region, list):
        response["isList"] = True
    elif isinstance(region, str):
        response["isString"] = True
    else:
        raise Exception("Region is not a list of string(s) or a single string.")

    if application_name == "runApplication1":
        response["runApplication1"] = True
    elif application_name == "runApplication2":
        response["runApplication2"] = True

    return response
