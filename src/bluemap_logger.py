import requests
import time
from datetime import datetime

def get_response(url):
    chat_messages = []

    r = requests.get(url)
    data = r.json()

    for _, value in data['chat-markers']['markers'].items():
        chat_messages.append((value['label']))
    return chat_messages

def monitor_chat():
    url = input("[*] markers.json url:\n[>] ")
    print("[*] waiting for new messages\n")
    last_messages = get_response(url)

    while True:
        current_messages = get_response(url)

        if current_messages != last_messages:
            for message in current_messages:
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] {message}")
                with open("chat-log.txt", "a") as file:
                    file.write(f"[{timestamp}] {message}\n")
                last_messages = current_messages
        time.sleep(0.3)
