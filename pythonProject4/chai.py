from config import CHAI_TOKEN, CHAR_ID
from characterai import pycai

char = CHAR_ID
client = pycai.Client(CHAI_TOKEN)
me = client.get_me()


def new_chat(char_id):
    with client.connect() as chat:
        new1, answer1 = chat.new_chat(
            char_id, me.id
        )
        return new1, answer1


new, answer = new_chat(CHAR_ID)


def send_msg(msg, chat_id):
    with client.connect() as chat:
        while True:
            text = msg

            message = chat.send_message(
                char, chat_id, text
            )

            return message.text
