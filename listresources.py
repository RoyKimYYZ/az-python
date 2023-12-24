from azure.identity import AzureCliCredential  
from azure.mgmt.resource import ResourceManagementClient  
from azure.mgmt.storage import StorageManagementClient
import os

# Connect to your Azure account  
credential = AzureCliCredential()  
resource_group_name = 'demoGroup'  
STORAGE_ACCOUNT_NAME = "strgrk3920345" 
LOCATION = "East US"
# Provision the storage account, starting with a management object.
storage_client = StorageManagementClient(credential, os.environ["AZURE_SUBSCRIPTION_ID"])
storage_client.storage_accounts.begin_create(resource_group_name, STORAGE_ACCOUNT_NAME,
    { "location" : LOCATION, "kind": "StorageV2", "sku": {"name": "Standard_LRS"} }
)
# Initialize the Resource Management Client  
resource_client = ResourceManagementClient(credential, os.environ["AZURE_SUBSCRIPTION_ID"])  
# Get all resources in the specified resource group  
resources = resource_client.resources.list_by_resource_group(resource_group_name)  
# Initialize an empty dictionary to store the results  
resource_data = {}  
# Loop through the resources and store the data in the dictionary  
for resource in resources:  
    resource_data[resource.name] = {  
        'ResourceType': resource.type,  
        'Location': resource.location  
    }  
# Display the resource data stored in the dictionary  
print(resource_data) 