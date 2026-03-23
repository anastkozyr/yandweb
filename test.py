from requests import get, post

print(get('http://localhost:8010/api/jobs').json())
print(get('http://localhost:8010/api/jobs/3').json())
print(get('http://localhost:8010/api/jobs/500').json())
print(get('http://localhost:8010/api/jobs/qwerty').json())

print(post('http://localhost:8010/api/jobs',
           json={'id': 3, 'job': 'installing a long-distance communication antenna', 'team_leader': 1, 'work_size': 5,
                 'collaborators': '6, 3', 'category': 3, 'is_finished': True}).json())

print(post('http://localhost:8010/api/jobs',
           json={'job': 'installing a long-distance communication antenna', 'team_leader': 1, 'work_size': 5,
                 'collaborators': '6, 3', 'is_finished': True}).json())

print(post('http://localhost:8010/api/jobs',
           json={'job': 'installing a long-distance communication antenna', 'team_leader': 1,  'category': 3, 'work_size': 5,
                 'is_finished': True}).json())


