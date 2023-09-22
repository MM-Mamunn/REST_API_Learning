import requests
import json
URL ="http://127.0.0.1:8000/aicreate/"

data={
    'teacher_name' : 'mejbah',
    'course_name' : 'Deep_learning',
    'course_duration' :'3',
    'seat' : 20 
}

json_data = json.dumps(data)
r = requests.post(url = URL,data = json_data)
data = r.json()
print(data)