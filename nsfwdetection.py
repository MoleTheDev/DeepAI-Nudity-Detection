import requests
import json
	
def detect(api_key, img, link, output):
	if api_key != "":
		if img != "" and link == False:
			r = requests.post(
				"https://api.deepai.org/api/nsfw-detector",
    		files={
     		   'image': open(img, 'rb'),
  		  },
   		 headers={'api-key': api_key}
			)
			if output == True:
				return r.json()
			else:
				return ""
		
		if link != "" and img == False:
			r = requests.post(
				"https://api.deepai.org/api/nsfw-detector",
    		data={
        		'image': link,
  		  },
   		 headers={'api-key': api_key}
			)
			
			if output == True:
				return r.json()
			else:
				return ""
	if api_key == "":
			return "API Key is empty."
				
