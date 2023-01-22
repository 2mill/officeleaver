from typing import Optional, Union
import requests
from requests import Response
class Api:
	api_key: str
	api_endpoint: str
	def __init__(self, api_key: str, api_endpoint: str) -> None:
		self.api_key = api_key
		self.api_endpoint = api_endpoint
	def traveltimes(self, start:float, end:float, traveltime_types: Optional[list]):
		params = {
			"start": start,
			"end": end,
			"traveltime_types": ",".join(traveltime_types)
		}
	def _reqwest(self, path: str, params: dict) -> dict:
		headers = { 'Citymapper-Partner-Key': self.api_key }
		res: Response = requests.get(
			'{}/{}'.format(self.api_endpoint, path),
			params=params,
			headers=headers
		)
