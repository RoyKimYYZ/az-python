# Import the needed management objects from the libraries. 
# The azure libraries were installed with pip install cmd. Also refer to requirements.txt
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient
import os, random
import click

@click.command()
@click.option("--resourcegroupname")
@click.option("--filename")
@click.option("--subscriptionid")
@click.option("--askcleanup", default=False, is_flag=True)
def create_az_storage(resourcegroupname, filename, subscriptionid, askcleanup):

    # Acquire a credential object using CLI-based authentication.
    # Checks if the Azure CLI is logged in. 
    # If the CLI is logged in, it uses the credentials obtained by the CLI.
    # If the Azure CLI is not logged in, it might prompt the user to log in or 
    # perform device code authentication.
    credential = AzureCliCredential()


    # Retrieve subscription id as an environment variable. Ensure to set it up before hand.
    os.environ['AZURE_SUBSCRIPTION_ID'] = subscriptionid
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    print(subscription_id)
    # print(os.environ.get('AZURE_SUBSCRIPTION_ID'))
    # print(os.getenv('AZURE_SUBSCRIPTION_ID'))


    # Obtain the management object for resources.
    resource_client = ResourceManagementClient(credential, subscription_id)

    RESOURCE_GROUP_NAME = resourcegroupname
    LOCATION = "eastus"

    rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
        { "location": LOCATION })
    print(f"Provisioned resource group {rg_result.name}")

    # Provision the storage account, starting with a management object.
    storage_client = StorageManagementClient(credential, subscription_id)
    STORAGE_ACCOUNT_NAME = f"pythonazurestorage{random.randint(1,100000):05}"
    # You can replace the storage account here with any unique name. A random number is used
    # by default, but note that the name changes every time you run this script.
    # The name must be 3-24 lower case letters and numbers only.

    # Check if the account name is available. Storage account names must be unique across
    # Azure because they're used in URLs.
    availability_result = storage_client.storage_accounts.check_name_availability(
        { "name": STORAGE_ACCOUNT_NAME }
    )

    availability_result

    if not availability_result.name_available:
        print(f"Storage name {STORAGE_ACCOUNT_NAME} is already in use. Try another name.")
        exit()

    # The name is available, so provision the account
    poller = storage_client.storage_accounts.begin_create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME,
        {
            "location" : LOCATION,
            "kind": "StorageV2",
            "sku": {"name": "Standard_LRS"}
        }
    )

    # Long-running operations return a poller object; calling poller.result()
    # waits for completion.
    account_result = poller.result()
    print(f"Provisioned storage account {account_result.name}")


    # Retrieve the account's primary access key and generate a connection string.
    keys = storage_client.storage_accounts.list_keys(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME)
    # Good to store these in a safe place such as key vault
    print(f"Primary key for storage account: {keys.keys[0].value}")

    # Connection string to the storage account
    conn_string = f"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName={STORAGE_ACCOUNT_NAME};AccountKey={keys.keys[0].value}"
    print(f"Connection string: {conn_string}")

    # Provision the blob container in the storage account (this call is synchronous)
    CONTAINER_NAME = "blob-container-01"
    container = storage_client.blob_containers.create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {})
    # The fourth argument is a required BlobContainer object, but because we don't need any
    # special values there, so we just pass empty JSON.
    print(f"Provisioned blob container {container.name}")

    blob_name = filename
    local_file_path = filename
    # Create a BlobServiceClient using the storage blob client library
    blob_service_client = BlobServiceClient.from_connection_string(conn_string)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(blob_name)

    # reference file path and upload blob
    with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)
    print(f"File '{local_file_path}' uploaded to the blob container '{CONTAINER_NAME}' as '{blob_name}'.")

    # The option to clean up and delete storage account resources
    if ( askcleanup == True ):
        user_input = input("Delete resource group y/n? ")
        if ( user_input == "y" ):
            resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)

if __name__ == "__main__":
    create_az_storage()