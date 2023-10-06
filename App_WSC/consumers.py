# consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from App_Main.models import Pet_info, Pet_diet_set

class SensorConsumer(AsyncWebsocketConsumer):
    # 쿼리문 추출 동기 함수
    @database_sync_to_async
    def get_pet_diet_set(self, Pet_owner_id):
        with open('Feed_Amount.json', 'r') as f:
            json_data = json.load(f)

        # 전달받은 Pet_owner_id로 펫 정보 가져옴
        pet_info = Pet_info.objects.get(pet_owner = Pet_owner_id)
        # 펫 정보와 일치하는 펫 식단 설정 정보를 추출 및 리턴
        pet_diet_set = Pet_diet_set.objects.get(pet_name = pet_info)
        pet_diet_info_dict = {
            'pet_name' : str(pet_diet_set.pet_name),
            'pet_feed_amount' : str(pet_diet_set.pet_feed_amount),
            'pet_feed_time_B' : str(pet_diet_set.pet_feed_time_B)[:5],
            'pet_feed_time_L' : str(pet_diet_set.pet_feed_time_L)[:5],
            'pet_feed_time_D' : str(pet_diet_set.pet_feed_time_D)[:5],
            'pet_feed_amount_now' : json_data['feed_amount']
        }
        feed_amount = {'feed_amount':''}
        with open('Feed_Amount.json', 'w', encoding="utf-8") as file:
            json.dump(feed_amount,file)
        return pet_diet_info_dict

    # connect : 사용자와 websocket 연결이 맺어졌을때 호출
    async def connect(self):
        print('Connect...')
        await self.accept()

    # disconnect : 사용자와 websocket 연결이 끊겼을때 호출
    async def disconnect(self, close_code):
        print('Disconnect...')
        pass

    # receive : 사용자가 메시지를 보내면 호출
    async def receive(self, text_data):
        # pet_feed_data JSON파일을 수신받아서 딕셔너리로 변환하여 사용.
        pet_feed_dict = json.loads(text_data)
        Pet_owner = pet_feed_dict['owner']
        with open("Pet_feed.json",'w') as file:
            file.write(json.dumps(pet_feed_dict, ensure_ascii=False, indent=4))

        if Pet_owner == 'kuksj0312@naver.com':
            # admin의 User id == 1
            Pet_owner_id = 1
            
        pet_diet_info = await self.get_pet_diet_set(Pet_owner_id)        
        # pet_diet_info 딕셔너리를 Json 파일로 변환하여 클라이언트에 전송, ensure_ascii : 한글 깨짐 방지, indent : 예쁘게 보냄
        await self.send(json.dumps(pet_diet_info, ensure_ascii=False, indent=4))