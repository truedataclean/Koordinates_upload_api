import koordinates

client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='3cbfe455f0ca4cacb40b066810ec6fbc')


# client = koordinates.Client(host='sandbox-2gxknc.koordinates.com', token='a1b6d384db6a42348a85ebf579cc904b')

# upload = koordinates.sources.UploadSource()
# upload.group = 3875
# upload.title = "NZ443202"
# upload.add_file("C:\\Temp\\chart\\NZ443202.tif")
# # upload.add_file("C:\\Temp\\chart\\NZ443202.xml")
# upload = client.sources.create(upload)


# layer = client.layers.get(120847).get_version(403581)
# layer = layer.start_update()

# koordinates.metadata.MetadataManager(layer.url, "C:\\Temp\\chart\\NZ443202.xml")

layer = client.layers.get(120847)
print(layer.url)
