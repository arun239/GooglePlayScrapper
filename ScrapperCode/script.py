import requests
from NetworkManager import *
from PlayStoreDataTagAndProps import * 
from UrlCreator import *

from bs4 import BeautifulSoup

"""url = prefix_url + package_name + suffix_url

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")"""




class PlayStoreScrapper:
	_soup = None
	_parser = "html.parser"
	
	def __init__(self, url):
		r = requests.get(url)
		self._soup = BeautifulSoup(r.content, self._parser)
	
	
	def get_data_for_attributes(self, tagname: str, properties: dict):
		textual_value = None
		try:
			textual_value = self._soup.find_all(tagname, properties)[0].text
		except:
			pass
		
		return textual_value
		
	def extract_package_info(self):
		attribute_dict = PlayStoreDataTagAndProps.get_all_attributes_to_extract()
		result_dict = {}
		for key, value in attribute_dict.items():
			attribute_value = self.get_data_for_attributes(value[PlayStoreDataTagAndProps.PARENT_TAG], value[PlayStoreDataTagAndProps.EXTENDED_PROP])
			if attribute_value is not None:
				result_dict[key] = attribute_value
			else:
				print ("WTF: Can't extract attribute value for " + key)
			
		return result_dict
		

if __name__ == "__main__":
	package_name_list = NetworkManager.get_all_package_names()
	
	for pacakage_name in package_name_list:
		url = UrlCreater.get_play_store_url(pacakage_name)
		play_store_scrapper = PlayStoreScrapper(url)
		package_info_dict = play_store_scrapper.extract_package_info()
		NetworkManager.post_package_info(package_info_dict)
		
		# appTitle = soup.find_all(PlayStoreDataTagAndProps.get_parent_tag_for_title(), PlayStoreDataTagAndProps.get_properties_for_title())#
		# print(appTitle[0].text)

		# rating = soup.find_all("div", {"class": "score"})
		# print(rating[0].text)

		# reviewNum = soup.find_all("span", {"class": "reviews-num"})
		# print(reviewNum[0].text)

		# numOfDownloads = soup.find_all("div", {"itemprop": "numDownloads"})
		# print(numOfDownloads[0].text.replace(' ',''))
	
		
	
	
	





