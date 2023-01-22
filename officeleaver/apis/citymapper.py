from officeleaver.apis.api import Api
from typing import Optional
from enum import Enum
import requests
from datetime import datetime, timedelta
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




class TravelMode(Enum):
	walk = "walk"
	transit = "transit"
	self_piloted = "self_piloted"
	on_demand = "on_demand"


class Instruction:
	class InstructionType(Enum):
		depart = "depart"
		turn = "turn"
		enter_roundabout = "enter_roundabout"
		exit_roundabout = "exit_roundabout"
	class TypeDirection(Enum):
		straight = "straight"
		uturn = "uturn"
		left = "left"
		slight_left = "slight_left"
		sharp_left = "sharp_left"
		right = "right"
		slight_right = "slight_right"
		sharp_right = "sharp_right"
	arrive = "arrive"
	path_index: int
	distance_meters: int
	time_second: int
	description_text: str
	description_format: str
	type: InstructionType
	type_direction: TypeDirection

class PathAnnotation:
	start_index: int
	end_index: int
	should_walk: Optional[bool]

class VehicleType(Enum):
	bike = "bike"
	bus = "bus"
	bus_rapid_transit = "bus_rapid_transit"
	car = "car"
	ebike = "ebike"
	escooter = "escooter"
	# TODO add the rest.... https://docs.external.citymapper.com/api/#section/Leg

class Service:
	id: str
	name: str
	vehicle_types: Optional[list[VehicleType]]
	brand: Optional[object]
	images: Optional[list[object]]
	color: Optional[str]
	background_color: Optional[str]
	text_color: Optional[str]
	third_party_app: Optional[object]


class Leg:
	travel_mode: TravelMode
	duration_seconds: Optional[str]
	path: str # TODO make Google Polyline utility?
	instructions: Optional[list[Instruction]]
	vehicle_types: Optional[list[VehicleType]]
	services: Optional[list[Service]]
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
