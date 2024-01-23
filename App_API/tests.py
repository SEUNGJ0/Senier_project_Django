import requests
import json
post_data_1 = {
    'feed_date': '2024-01-23',
    'feed_time': '09:00',
    'feed_amount' : '80',
    'remain_amount' : '5',
    'feed_index' : 'true',
    'pet_name' : '9'
}
post_data_2 = {
    'feed_date': '2024-01-23',
    'feed_time': '13:00',
    'feed_amount' : '80',
    'remain_amount' : '5',
    'feed_index' : 'true',
    'pet_name' : '9'
}
post_data_3 = {
    'feed_date': '2024-01-23',
    'feed_time': '19:00',
    'feed_amount' : '80',
    'remain_amount' : '0',
    'feed_index' : 'true',
    'pet_name' : '9'
}
def post_test(api_url, post_data, headers):
    response = requests.post(api_url, data=json.dumps(post_data) ,headers=headers)
    # 응답 처리
    if response.status_code == 201:  # 201은 생성 성공을 나타냅니다.
        data = response.json()
        print('Success:', data)
    else:
        print('Error:', response.status_code, response.text)

auth_url = "http://127.0.0.1:8000/api/auth"
api_url = 'http://127.0.0.1:8000/api/daily-feeding'
response = requests.post(auth_url, data={'username':'kuksj0312@naver.com', 'password':'1562'})
myToken = response.json()['token']
headers = {'Content-Type': 'application/json' ,'Authorization': 'Token '+myToken}
post_test(api_url, post_data_1 ,headers)
post_test(api_url, post_data_2 ,headers)
post_test(api_url, post_data_3 ,headers)