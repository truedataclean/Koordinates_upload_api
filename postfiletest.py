
import requests

domain = 'sandbox-2gxknc.koordinates.com'
lds_page_type = 'layers'
layer_id = 120847            
ver_id = 403582            
api_key = 'key 3cbfe455f0ca4cacb40b066810ec6fbc'


# files = {
#     "NZ443202": ("NZ443202.zip", open("C:\\Temp\\chart\\NZ443202.zip", "rb"), "application/x-zip"),
#     "source": (None, '{"title": "NZ443202", "name": "NZ443202", "type": "upload", "group": 3875}', "application/json"),
# }

# files = {
#     "upload_test": ("NZ443202.tif", open("C:\\Temp\\chart\\NZ443202.tif", "rb"), "image/tiff"),
#     "source": (None, '{"title": "NZ443202", "name": "NZ443202", "type": "upload", "group": 3875}', "application/json"),
# }

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


# post_url = f"https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/261179/"
post_url = f"https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/"

# payload = (
#     f"----b0017bc3bab14fed95910bfcc4a1ddd8\r\n"
#     f"Content-Disposition: form-data; name=\"NZ443202\"; filename=\"C:\\Temp\\chart\\NZ443202.zip\"\r\n"
#     "Content-Type: application/x-zip\r\n\r\n"
#     "(binary data not shown)\r\n"
#     "--b0017bc3bab14fed95910bfcc4a1ddd8\r\n"
#     f"Content-Disposition: form-data; name=\"source""\r\n"
#     "Content-Type: application/json\r\n\r\n"
#     "{\r\n"
#     "    \"name\": \"points-of-interest\",\r\n"
#     "    \"type\": \"upload\",\r\n"
#     "    \"group\": 3875\r\n"
#     "}\r\n"
#     f"--b0017bc3bab14fed95910bfcc4a1ddd8--\r\n"
# )


#     response = requests.post(url, json=payload, headers=headers)
#     return response

# # usage
# post_response = post_request(post_url, payload, headers)
# print(post_response.status_code)
# print(post_response.json())


###############################

def post_request(url, files, headers):
    response = requests.post(url, files=files, headers=headers)
    return response

post_response = post_request(post_url, files, headers)

# print(post_response.status_code)
print(post_response.json())

############################################################