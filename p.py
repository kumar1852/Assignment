# Import requests package

import requests
import sys
# Assign URL to variable: url

url = 'http://www.omdbapi.com/?apikey=72bc447a&t='+sys.argv[1]

# Package the request, send the request and catch the response: k

k = requests.get(url)
# r = 'Rotten'
# iPrint the text of the response

#print(k.text)

# Decode the JSON data into a dictionary: json_data
json_data = k.json()

# Print each key-value pair in json_data

for key,v  in json_data.items():
#	if key == r:		
	#	print(key +':', json_data[key])
       if key == 'Ratings':      
     	# print key
      	 #print v[1]
	 print v[1].get('Source') + ':' +  v[1].get('Value')
         #print v[1].get('Value')
         
    
