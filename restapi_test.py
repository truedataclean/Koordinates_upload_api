import requests
domain = 'sandbox-2gxknc.koordinates.com'
lds_page_type = 'layers'
layer_id = 120847             #120777
ver_id = 403582             #400661
api_key = 'key 3cbfe455f0ca4cacb40b066810ec6fbc'

# layer_url = f"https://{domain}/services/api/v1/{lds_page_type}/{layer_id}/versions/{ver_id}/"
        
#         # layer_url = f"https://{self.domain}/services/api/v1/layers/{self.layer_id}/versions/{self.ver_id}/"
#         # Request layer details
# layer_resp = requests.get(layer_url, headers={"Authorization": f"{api_key}"}, timeout=10)
# print(layer_resp)
# layer_details = layer_resp.json()

# source_summary = layer_details["data"]['source_summary']
# print(source_summary)

# data_sources = layer_details["data"]['datasources']
# print(data_sources)

# layer_description = layer_details["data"]['source_summary']['descriptions'][0]
# print(layer_description)

# source_id = 261118
# dSource_url = f"https://{domain}/services/api/v1/sources/{source_id}/datasources"
# ds_resp = requests.get(dSource_url, headers={"Authorization": f"{api_key}"}, timeout=10)
# print(ds_resp)
# ds_details =ds_resp.json()
# # sourcedet = source_details
# # print(sourcedet['datasources'])
# print(ds_details)




# put_url = f"https://{domain}/services/api/v1/layers/{layer_id}/versions/{ver_id}/"
put_url = f"https://sandbox-2gxknc.koordinates.com/services/api/v1/layers/120847/versions/403582/"

payload = {
    "data": {
        "datasources": [
            "https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/261179/datasources/9830764/"
        ]
    }
}

headers = {
"Content-Type": "application/json",
"Authorization": f"{api_key}",
    }


#Dreft ID check
# draft_id_url = f"https://{domain}/services/api/v1.x/layers/{layer_id}/versions/?page_size=1"
# print('draft_id url: ' ,draft_id_url)

###############################################
def put_request(url, payload, headers):
    response = requests.put(url, json=payload, headers=headers)
    return response

# update datasource url
response = put_request(put_url, payload, headers)
print(response.status_code)
print(response.json())
###############################################




