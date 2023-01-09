class Api:
	api_key: str
	api_endpoint: str

	def call(path: str, params: dict):
		return NotImplementedError
