class PlayStoreDataTagAndProps:
	
	PARENT_TAG = "parent_tag"
	EXTENDED_PROP = "extended_prop"
	
	attributes_to_extract = {
		"title": {PARENT_TAG : "div", EXTENDED_PROP : {"class" : "id-app-title"}},
		"rating": {PARENT_TAG : "div", EXTENDED_PROP : {"class": "score"}},
		"reviewNum": {PARENT_TAG : "span", EXTENDED_PROP : {"class": "reviews-num"}},
		"numOfDownloads": {PARENT_TAG : "div", EXTENDED_PROP : {"itemprop": "numDownloads"}}
	}
	
	@staticmethod
	def get_all_attributes_to_extract():
		return PlayStoreDataTagAndProps.attributes_to_extract
	
	@staticmethod
	def get_parent_tag_for_title():
		return "div"
	
	@staticmethod	
	def get_properties_for_title():
		return {"class" : "id-app-title"}