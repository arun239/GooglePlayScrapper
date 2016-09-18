import requests
import json
from UrlCreator import * 

class NetworkManager:
	@staticmethod
	def get_all_package_names():
		#json_date = requests.get(UrlCreater.get_all_packages_url())
		#TODO: Remove Mocking data
		json_data = '{"package_name": ["com.friendlymonster.snookerdemo", "org.mozilla.firefox"]}'
		packages_info_dict = json.loads(json_data)
		return packages_info_dict["package_name"]
	
	@staticmethod
	def get_package_info():
		#json_data = requests.get(UrlCreater.get_package_info_url())
		return json.loads(json_data)
		
	
	@staticmethod
	def post_package_info(pack_info):
		#requests.post(UrlCreater.get_post_package_info_url(), data = json.dumps(pack_info))
		print(pack_info)