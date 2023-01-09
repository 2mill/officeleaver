import os
import json
from datetime import datetime, timedelta
from officeleaver.apis.citymapper import CityMapper

# Cache building

token = os.getenv("CITYMAPPER_TEST_TOKEN")
if not os.path.exists('./tests/cache'):
	os.mkdir('./tests/cache')

if not os.path.exists('./tests/cache/parsings.json'):
	client = CityMapper(token)
	ENF_OFFICE = [str(41.879905), str(-87.630802)]
	WRIGLEY_FIELD = [str(41.9484), str( -87.655800)]
	leave_time = datetime.now().astimezone() + timedelta(minutes=10)
	params = {
		'start': ','.join(ENF_OFFICE),
		'end':  ','.join(WRIGLEY_FIELD),
		'time': leave_time.isoformat()
	}
	res = client.call(CityMapper.Paths.transit, params)

	data = res.json()
	with open('./tests/cache/parsings.json', 'w') as f:
		json.dump(data, f)



data = open('./tests/cache/parsings.json')

data = json.load(data)

def test_get_routes():
	assert data.get('routes') != None
