from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient

import os
os.environ["AZURE_SUBSCRIPTION_ID"]

# Initialize the Azure credentials and clients
credentials = DefaultAzureCredential()
resource_client = ResourceManagementClient(credentials, os.environ["AZURE_SUBSCRIPTION_ID"])
subscription_client = SubscriptionClient(credentials)

# Get a list of all subscriptions
subscriptions = subscription_client.subscriptions.list()

# Iterate through each subscription and list resource groups
for subscription in subscriptions:
    print(f"Subscription ID: {subscription.subscription_id}")
    resource_client._config.subscription_id = subscription.subscription_id
    resource_groups = resource_client.resource_groups.list()
    for rg in resource_groups:
        print(f"Resource Group Name: {rg.name}, Location: {rg.location}")

