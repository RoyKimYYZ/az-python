# https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-python?tabs=windows

import os
import json
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsResource

credential = AzureCliCredential()

resource_client = ResourceManagementClient(credential, os.environ["AZURE_SUBSCRIPTION_ID"])

resource_group_name = "demoGroup"
storage_account_name = "demostore"

# Provision the resource group.
rg_result = resource_client.resource_groups.create_or_update(
    resource_group_name, {"location": "eastus"}
)

print("rg_result")
print(rg_result)
print('\n')

tags = {
    "Dept": "Finance",
    "env": "dev"
}

tag_resource = TagsResource(
    properties={'tags': tags}
)

resource_client.tags.begin_create_or_update_at_scope(rg_result.id, tag_resource)

# resource = resource_client.resources.get_by_id(
#     f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{storage_account_name}",
#     "2022-09-01"
# )

# resource_client.tags.begin_create_or_update_at_scope(resource.id, tag_resource)

print(f"Tags {tag_resource.properties.tags} were added to resource with ID: {rg_result.id}")