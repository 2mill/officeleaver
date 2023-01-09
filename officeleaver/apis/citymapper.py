from officeleaver.apis.api import Api
import requests
class CityMapper(Api):
	api_key: str
	api_endpoint = 'https://api.external.citymapper.com/api/1/'
	headers: dict
	def __init__(self, token: str, endpoint:str = None):
		self.api_key = token
		if endpoint: self.endpoint = endpoint

		self.headers = {
			'Citymapper-Partner-Key': self.api_key
		}

	class Paths:
		transit = r'directions/transit'

	def call(self, path: str, params: dict) -> requests.Response:
		return requests.get(f'{CityMapper.api_endpoint}/{path}', params=params, headers=self.headers)

	def __str__() -> str:
		return "CityMapper API"

class Service:
	id: str
	name: str
	vehicle_types: list[str]
	brand: dict
	# this needs to be added later.
	# images
	# color: str
	# background_color: str
	# text_color: str
	def __init__(self, id, name, vehicle_type, brand) -> None:
		self.id = id
		self.name = name
		self.vehicle_types = vehicle_type,
		self.brand = brand
class Leg:
	duration: str
	travel_mode: str
	departure_time: str
	services: list[Service]
	travel_mode_icons = {
		'walk': '🚸',
		'transit': '🚇'
	}
	def __init__(self, duration:str, travel_mode: str, departure_time:str, services: list[dict] = None) -> None:
		self.duration = str(duration)
		self.travel_mode = travel_mode
		self.departure_time = departure_time
		self.services: list[Service] = []
		self.primary_service = services.pop()

		if services:
			for service in services:
				self.services.append(
					Service(
						service['id'],
						service['name'],
						service['vehicle_types'],
						service['brand']
					)
				)

	def __str__(self) -> str:
		travel_mode_icon = self.travel_mode_icons.get(self.travel_mode)
		travel_mode_verb = {
			'walk': 'WALK',
			'transit': f"TAKE"



		}

		if not travel_mode_icon:
			travel_mode_icon = '❔'



		return f"{self.travel_mode.upper()}"
		# return f"{travel_mode_icon} for {int(self.duration) // 60} minutes"
class Route:
	duraction: str
	accuracy: str
	legs: list[Leg]


# BAD CODE, DO NO USE RIGHT NOW
def get_legs(routes: list[Route]):
	for route in routes:
		legs: list[Leg] = []
		leg_start: Leg = None
		for i, leg in enumerate(route['legs']):
			temp_leg = Leg(leg['duration_seconds'], leg['travel_mode'], leg['updatable_detail']['leg_departure_time'], leg.get['services'])
			if not i:
				leg_start = temp_leg

			legs.append(temp_leg)



		def diff_mins_now(later: datetime) -> timedelta:
			return later - datetime.now(tz=later.tzinfo)
		diff = diff_mins_now(datetime.fromisoformat(leg_start.departure_time))

		print(f"Leave in {diff.seconds // 60} minutes")
		print(' ➡ '.join([ str(leg) for leg in legs ]))
