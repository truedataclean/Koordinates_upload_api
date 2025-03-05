# /c:/Projects/Git/LDS_UPLOAD/src/upload/__init__.py
# Koordinates upload process
# 1. Read the data from the source
# 2. Upload the data to the source and data source
# 3. Backup the data from LDS
#    3.1. Create export
#    3.2. Download export
# 4. Update the data to the LDS
# 5. Log the process
# 6. Send a notification
# 7. Monitor the process
# 8. Handle the errors
# 9. Manage the process
# 10. Control the process
# 11. Test the process
# 12. Document the process
# 13. Review the process
# 14. Improve the process
# 15. Maintain the process
# 16. Archive the process
# 17. Backup the process
# 18. Restore the process
# 19. Secure the process
# 20. Schedule the process
# 21. Automate the process
# 22. Optimize the process
# 23. Standardize the process
# 24. Scale the process
# 25. Share the process
# 26. Collaborate the process
# 27. Integrate the process
# 28. Deploy the process
# 29. Monitor the process
# 30. Report the process
# 31. Analyze the process
# 32. Visualize the process
# 33. Predict the process
# 34. Plan the process
# 35. Design the process
# 36. Develop the process
# 37. Implement the process

import yaml
import koordinates
import requests
import os



def read_config(config_path="config.yaml"):
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            file.close()  
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file not found: {e}")
    
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

    try:
        layer_id = config["LDS_LAYER_ID"]
        File_PATH = config["File_PATH"]
        backup = config["Backup_PATH"]
        lds_host = config['LDSConnection']['host']
        lds_key = config['LDSConnection']['token']

    except KeyError as e:
        raise KeyError(f"Missing configuration key: {e}")

    return layer_id, File_PATH, lds_host, lds_key, backup

def export_layer(layer_id,client):
    export = koordinates.Export()
    export.crs = "EPSG:4326"
    export.formats = {
                    "raster": "image/tiff;subtype=geotiff"
        }
    export.add_item(layer_id)

    client.exports.create(export)
    print(export.download_url)

    # Download the export
    exports = client.exports.list()
    for export in exports:
        print(export)
    pr = exports[0]
    dw = pr.download_url
    print(dw)

def main():
    print("Welcome to the LDS Upload Project!")

    # Read database credentials and user input from config.yaml
    layer_id, File_PATH, lds_host, lds_key, backup = read_config()

    print(layer_id, File_PATH, lds_host, lds_key, backup)   

    # kOORDINATES API
    client = koordinates.Client(host=lds_host, token=lds_key)

    # Get layer for update layer
    layer = client.layers.get(layer_id)

    print(layer)

    api_key = 'key '+lds_key

    headers = {
        "Authorization": f"{api_key}",
    }

    
    # Export the layer for backup
    dw = export_layer(layer_id,client)

    # Download the export to the file
    url = dw
    r = requests.get(url, allow_redirects=True, headers=headers, verify=False)
    filename = 'test.zip'
    open(filename, 'wb').write(r.content)













if __name__ == "__main__":
    main()