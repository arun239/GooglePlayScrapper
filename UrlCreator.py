import requests
import json

from bs4 import BeautifulSoup

""" Utility Script """

HTTPS_PREFIX = "https://"
HTTP_PREFIX = "http://"

HOSTNAME = "localhost"
API_URL = ""
API_URL2 = ""

GOOGLE_HOST_NAME = "play.google.com/"
GOOGLE_PLAY_STORE_URL_SUFFIX = "store/apps/details?id="

#GET_PACKAGE_NAMES = requests.get(HOSTNAME+API_URL)

class UrlCreater:
	@staticmethod
	def get_play_store_url(package_name):
		return HTTPS_PREFIX + GOOGLE_HOST_NAME + GOOGLE_PLAY_STORE_URL_SUFFIX + package_name
		
	@staticmethod	
	def get_all_packages_url():
		return HTTP_PREFIX + HOSTNAME + API_URL
		
	
	@staticmethod
	def get_package_info_url():
		return HTTP_PREFIX + HOSTNAME + API_URL2

	@staticmethod
	def get_post_package_info_url():
		return HTTP_PREFIX + HOSTNAME + API_URL2
		
# if __name__ == "__main__":
	# package_names = '{"package_name": ["com.friendlymonster.snookerdemo", "org.mozilla.firefox"]}'
	# data = json.loads(package_names)
	# for package in data['package_name']:
		#print(package)
		# play_store_url = UrlCreater.get_play_store_url(package)
		# print(play_store_url)
	


		


	
	





