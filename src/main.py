import json

data = {
"type": "call_result",
"lead": {
"id": 123456788,
"name": "Организация 1",
"comment": "",
"post": "",
"city": "",
"business": "",
"homepage": "",
"emails": ["user@example.com"],
"inn": "",
"kpp": "",
"created_at": "30.01.2019 09:29:30",
"updated_at": "30.01.2019 10:04:26",
"deleted_at": "",
"parent_lead_id": "",
"tags": [],
"phones": "+7900000000"
},
"contact": {
"id": 123456789,
"name": "Контакт",
"comment": "",
"post": "",
"city": "",
"business": "",
"homepage": "",
"emails": [],
"inn": "",
"kpp": "",
"created_at": "30.01.2019 09:29:31",
"updated_at": "30.01.2019 09:29:31",
"deleted_at": "",
"parent_lead_id": 123456788,
"tags": [],
"address": "",
"phones": "+79000000001"
},
"call": {
"id": 987654321,
"phone": "+7900000000",
"source": "+74997097462",
"direction": "out",
"params": {},
"lead_id": 123456788,
"organization_id": 123456788,
"user_id": 123456787,
"started_at": "30.01.2019 10:03:50",
"connected_at": "30.01.2019 10:04:27",
"ended_at": "30.01.2019 10:06:08",
"reason": "201 ended by remote side",
"duration": 101,
"scenario_id": 12345,
"result_id": 54321,
"incoming_phone": "",
"recording_url": "https://api.skorozvon.ru/api/calls/987654321.mp3",
"call_type": "outgoing",
"region": "Оренбургская область",
"local_time": "12:52",
"call_project_id": "12345678",
"call_project_title": "call project title",
"scenario_result_group_id": "12345678",
"scenario_result_group_title": "scenario title"
},
"call_result": {
"result_id": 54321,
"result_name": "Результат звонка",
"comment": "Комментарий к звонку"
}
}



with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)