import json
import os

files = os.listdir('.')
files = [file for file in files if file.startswith('uuid')]

for file in files:
	try:
		data = json.load(open(file))

		boss = data['ADM_01']['1']['answer'].encode('utf-8').replace('/', '_')
		lastname = data['ADM_01']['2']['answer'].encode('utf-8').replace('/', '_')
		firstname = data['ADM_01']['3']['answer'].encode('utf-8').replace('/', '_')
		os.rename(file, '{}-{}-{}.json'.format(boss, lastname, firstname))
	except Exception as exc:
		print('In file {} get {}'.format(file, exc))