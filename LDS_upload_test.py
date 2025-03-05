import requests

domain = 'sandbox-2gxknc.koordinates.com'
# lds_page_type = 'layers'
# layer_id = 120847            
# ver_id = 403582            
api_key = 'key 3cbfe455f0ca4cacb40b066810ec6fbc'


##Source upload
files = {
    "upload_test_1": ("NZ443201.tif", open("C:\\Temp\\chart\\NZ443201.tif", "rb"), "image/tiff"),
    "upload_test_2": ("NZ443201.xml", open("C:\\Temp\\chart\\NZ443201.xml", "rb"), "application/xml"),
    "upload_test_3": ("NZ443202.tif", open("C:\\Temp\\chart\\NZ443202.tif", "rb"), "image/tiff"),
    "upload_test_4": ("NZ443202.xml", open("C:\\Temp\\chart\\NZ443202.xml", "rb"), "application/xml"),
    "source": (None, '{"title": "Upload_multi", "name": "NZ4432", "type": "upload", "group": 3875}', "application/json"),
}

headers = {
    "Authorization": f"{api_key}",
}

# put_url = f"https://{domain}/services/api/v1/layers/{layer_id}/versions/{ver_id}/"
post_url = f"https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/"

def post_request(url, files, headers):
    response = requests.post(url, files=files, headers=headers)
    return response

##Upload source
post_response = post_request(post_url, files, headers)
print(post_response.json())


##Layer update
# import koordinates

# client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='3cbfe455f0ca4cacb40b066810ec6fbc')

# layer = client.layers.get(120847).get_version(403582)
# layer = layer.start_update()

# print(layer.url)





put_url = f"https://sandbox-2gxknc.koordinates.com/services/api/v1/layers/120847/versions/403714/"

payload = {
    "data": {
        "datasources": [
            "https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/261267/datasources/9831273/"
        ]
    }
}

headers = {
"Content-Type": "application/json",
"Authorization": f"{api_key}",
    }

###############################################
def put_request(url, payload, headers):
    response = requests.put(url, json=payload, headers=headers)
    return response

# update datasource url
# response = put_request(put_url, payload, headers)
# print(response.status_code)
# print(response.json())
###############################################


# layer_version = client.layers.get(120847).get_version(403714)
# layer_version.publish()