import requests

domain = 'sandbox-2gxknc.koordinates.com'
# lds_page_type = 'layers'
# layer_id = 120847            
# ver_id = 403582            
api_key = ''


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
import koordinates

client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='')

layer = client.layers.get(120847).get_version(403582)
layer = layer.start_update()

print(layer.url)





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

update datasource url
response = put_request(put_url, payload, headers)
print(response.status_code)
print(response.json())
###############################################


layer_version = client.layers.get(120847).get_version(403714)
layer_version.publish()


import requests
domain = 'sandbox-2gxknc.koordinates.com'
lds_page_type = 'layers'
layer_id = 120847             #120777
ver_id = 403582             #400661
api_key = ''

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

import koordinates

client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='')

layer = client.layers.get(120847)
api_key = ''

headers = {
    "Authorization": f"{api_key}",
}

export = koordinates.Export()
# export.crs = "EPSG:4326"
# export.formats = {
#                 "raster": "image/tiff;subtype=geotiff"
#     }
# export.add_item(layer)

# # export.download("C:\\Temp\\chart\\")
# client.exports.create(export)
# print(export.download_url)

# # export.get_formats(layer)
# # format = koordinates.exports.ExportManager.get_formats

exports = client.exports.list()
for export in exports:
    print(export)
pr = exports[0]
dw = pr.download_url
print(dw)


import requests


url = dw
r = requests.get(url, allow_redirects=True, headers=headers, verify=False)
filename = 'test.zip'
open(filename, 'wb').write(r.content)

import koordinates

client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='')

# # print the 10 most recently created layers
# # for layer in client.layers.order_by('created_at')[:50]:
# #    print(layer)
   
# # for layer in client.layers.list():
# #     print(layer.title)
    
    
# layer = client.layers.get(51420)
# print(layer)



# from datetime import datetime
 
# # get current date and time
# current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# print("Current date & time : ", current_datetime)
 
# # convert datetime obj to string
# str_current_datetime = str(current_datetime)
 
# # create a file object along with extension
# file_name = str_current_datetime+".csv"
# file = open(file_name, 'w')
 
# print("File created : ", file.name)
# file.close()

# import time
# timestr = time.strftime("_%Y-%m-%d_%H-%M-%S")
# print (timestr)




# upload = koordinates.sources.UploadSource()
# upload.group = 3875
# upload.title = "DP Test"
# upload.add_file("C:\\Temp\\chart\\NZ443201.zip")
# # upload.add_file("C:\\Temp\\chart\\NZ443201.tif","NZ443201.tif",content_type="image/tiff")
# upload = client.sources.create(upload)


# datasource = koordinates.sources.SourceManager(client)
# print(datasource.get_datasource(260270,9527826))


# layer = client.layers.get(120316)
# ##layer(id=120316)
# print(layer.data.datasources)
# # datasources = layer.data.datasources
# # print(datasources)


# data = koordinates.layers.LayerData(datasources=[9527826])
# print(data.datasources)


# upload = koordinates.sources.UploadSource()
# upload.group = 3875
# upload.title = "DP Test"
# upload.add_file("C:\\Temp\\chart\\NZ443202.zip")
# upload = client.sources.create(upload)

# layer = client.layers.get(120777)
# print(layer.data.datasources)

# layer = client.layers.get(120316)
# layer = client.layers.get(120777)
# # print(layer.data.datasources)
# version = layer.list_versions()
# for i in version:
#     print(i)


# layer = client.layers.get(120316)
# ds = layer.data.datasources
# print(ds)



# layer = koordinates.Layer()
# layer.title = "A Test Layer"
# layer.group = 3875
# layer.data = koordinates.layers.LayerData(datasources=[9788836])
# layer = client.layers.create(layer)
# # print(layer.url)


# # datasource = koordinates.sources.SourceManager(client)
# # print(datasource.get(261055)) #,datasource_id=9788836

# publish = koordinates.publishing.Publish()
# publish.add_layer_item(layer)
# # publish.add_table_item(table)
# publish.strategy = publish.PUBLISH_STRATEGY_TOGETHER
# publish = client.publishing.create(publish)
# print(publish.url)


# layer = koordinates.Layer()
# layer.title = "DP Upload Test Layer"
# layer.group = 3875
# layer.data = koordinates.layers.LayerData(datasources=[9788836])
# layer = client.layers.create(layer)

# publish = koordinates.publishing.Publish()
# publish.add_layer_item(layer)
# publish.strategy = publish.PUBLISH_STRATEGY_TOGETHER
# publish = client.publishing.create(publish)
# print(publish.url)


# layer = client.layers.get(120813)
# layer.set_metadata("C:\\Temp\\chart\\NZ443202.xml")
# layer.start_update()
# print(layer.url)

# layer = client.layers.get(120823)
# layer.set_metadata("C:\\Temp\\chart\\NZ443202.xml", 403253)
# # layer.start_import()

# Test Layer with Metadata ##########################################################
# upload = koordinates.sources.UploadSource()
# upload.group = 3875
# upload.title = "NZ443202"
# upload.add_file("C:\\Temp\\chart\\NZ443202.tif")
# # upload.add_file("C:\\Temp\\chart\\NZ443202.xml")
# upload = client.sources.create(upload)
#####################################################################################

# layer = koordinates.Layer()
# layer.title = "DP Upload Test Layer"
# layer.group = 3875
# layer.data = koordinates.layers.LayerData(datasources=[9830506])
# layer = client.layers.create(layer)


# layer = client.layers.get(120839)
# print(layer.url)



# # koordinates.layers.LayerManager.set_metadata(self= None,layer_id=120839, version_id=403253, fp="C:\\Temp\\chart\\NZ443202.xml") #, 403253
# koordinates.layers.Layer.set_metadata(layer, "C:\\Temp\\chart\\NZ443202.xml", 403253) #, 403253



# layer = client.layers.get(120839)

# publish = koordinates.publishing.Publish()
# publish.add_layer_item(layer)
# publish.strategy = publish.PUBLISH_STRATEGY_TOGETHER
# publish = client.publishing.create(publish)
# print(publish.url)

# layer = client.layers.get(120839).get_version(403290)
# koordinates.metadata.MetadataManager(layer.url, "C:\\Temp\\chart\\NZ443202.xml")
# layer = layer.start_update()

# print(layer.url)

# layer_version = client.layers.get(120839).get_version(403290) #9830520
# layer_version.publish()



# source = client.sources.get(id=261122)
# datasource = client.sources.get_datasource(source.id,9830520)
# upload = koordinates.sources.UploadSource()
# print(datasource.url)

# upload.group = 3875
# upload.update_existing = True
# upload.title = "NZ443202"
# upload.add_file("C:\\Temp\\chart\\NZ443202.tif")
# # upload.add_file("C:\\Temp\\chart\\NZ443202.xml")
# upload.save()
# # upload = client.sources.create(upload)


# upload = koordinates.sources.UploadSource()
# upload.get_datasource(9830520)

# upload.add_file("C:\\Temp\\chart\\NZ443202.tif")
# upload.save()


# source = client.sources.get(id=261122)
# # print(source)

# ds = koordinates.sources.DatasourceManager.get(source.id,9830520)
# print(ds.url)

#https://sandbox-2gxknc.koordinates.com/manage/data/layers/120847/update/

# layer = client.layers.get(120847)
# layer.data = koordinates.layers.LayerData(datasources=[9830520])
# layer = layer.start_update()

# layer = client.layers.get(120847)
# print(layer.data.datasources)

# layer_version = client.layers.get(120847).get_version(403336) #9830520
# layer_version.publish()


# layer = client.layers.get(120847)
# print(layer.data.datasources)
# layer.data = koordinates.layers.LayerData(datasources=[9830520])
# print(layer.data.datasources)
# versions = layer.list_versions()
# for version in versions:
#     print(version)

# layer = layer.start_update()

# layer = client.layers.get(120847)
# print(layer.data.datasources)




# datasource = koordinates.sources.SourceManager(client)
# print(datasource.get_datasource(261122,9830520))

# layer = client.layers.get(120317)
# print(layer.data.datasources)
# layer.data = koordinates.layers.LayerData(datasources=[9830520])
# print(layer.data.datasources)
# layer = layer.start_update()


# layer = client.layers.get(120317)
# versions = layer.list_versions()
# for version in versions:
#     print(version)

# layer_version = client.layers.get(120317).get_version(403347)
# layer_version.publish()



# upload = koordinates.sources.UploadSource()
# # print(upload.get_datasource(9830520))
# # upload.id = 261118
# upload.title = "NZ443202"
# upload.group = 3875
# upload.add_file("C:\\Temp\\chart\\NZ443202.tif")
# upload.add_file("C:\\Temp\\chart\0\NZ443202.xml")
# # # upload.save()
# upload = client.sources.create(upload)


# draft = client.layers.get_draft(120847)
# print(draft.get_draft_version)


# layer_version = client.layers.get(120847).get_version(403582)
# ds = layer_version.data.datasources
# datasource = "https://sandbox-2gxknc.koordinates.com/services/api/v1/sources/261179/datasources/9830764/"
# print(ds)

# layer = client.layers.get(120847)
# layer.data = koordinates.layers.LayerData(datasources=[9830764])

# layer_version = client.layers.get(120847).get_version(403582)
# ds = layer_version.data.datasources
# print(ds)
