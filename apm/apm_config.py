import os


def config():
    print("chamou")
    server_url = 'http://localhost:8200'
    if os.environ.get('SERVER_URL') != None:
        server_url = os.environ.get('SERVER_URL')

    app_name = 'Team-Pony-client'
    if os.environ.get('APP_NAME') != None:
        app_name = os.environ.get('APP_NAME')

    service_name = 'Jeremy'
    if os.environ.get('SERVICE_NAME') != None:
        service_name = os.environ.get('SERVICE_NAME')

    config = {
        'APP_NAME': app_name,
        'DEBUG': True,
        'SERVER_URL': server_url,
        'TRACES_SEND_FREQ': 5,
        'SERVICE_NAME': service_name,
        'FLUSH_INTERVAL': 1,
        'MAX_QUEUE_SIZE': 1,
    }
    return config