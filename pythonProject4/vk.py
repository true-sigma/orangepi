
# imports
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_TOKEN, CHAR_ID
import chai

# vk session init
vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
vk.account.setOnline(voip=False)


vk_chat = {
    # "vk id": "chat id"
}


def attachment_handler(att):
    output = f""
    return output


def main():
    for event in longpoll.listen():

        vk.account.setOnline(voip=False)

        if event.type == VkEventType.MESSAGE_NEW:
            vk_user_id = event.user_id
            message = event.text

            if event.to_me:
                vk.messages.set_activity(user_id=vk_user_id, type='typing')

                if vk_user_id in vk_chat:

                    if event.attachments:
                        att1 = attachment_handler(event.attachments)
                        print(att1)
                        char_response = chai.send_msg(msg=att1, chat_id=vk_chat[vk_user_id])

                    else:
                        char_response = chai.send_msg(msg=message, chat_id=vk_chat[vk_user_id])

                    vk.messages.send(user_id=vk_user_id, message=char_response, random_id=0)

                else:
                    chai_answer = chai.new_chat(CHAR_ID)
                    char_chat_id = chai_answer[0].chat_id
                    vk_chat[vk_user_id] = char_chat_id

                    if event.attachments:
                        att1 = attachment_handler(event.attachments)
                        print(att1)

                        char_response = chai.send_msg(msg=att1, chat_id=char_chat_id)

                    else:
                        char_response = chai.send_msg(msg=message, chat_id=char_chat_id)

                    vk.messages.send(user_id=vk_user_id, message=char_response, random_id=0)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        main()
