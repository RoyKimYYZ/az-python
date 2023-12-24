import subprocess
import json

def run_az_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Error executing command: {result.stderr.strip()}")

# Define the Azure CLI command to list resource groups and output as JSON
az_cli_command = "az group list --output json"

# Execute the Azure CLI command
az_cli_output = run_az_command(az_cli_command)

# Parse the JSON output
resource_groups = json.loads(az_cli_output)

# Loop through the resource groups and store information in a list of dictionaries
resource_group_objects = []
for resource_group in resource_groups:
    resource_group_object = {
        'Name': resource_group['name'],
        'Location': resource_group['location'],
        'ProvisioningState': resource_group['properties']['provisioningState']
    }
    resource_group_objects.append(resource_group_object)

# Display the properties of the resource groups
for resource_group_object in resource_group_objects:
    print(f"Name: {resource_group_object['Name']}")
    print(f"Location: {resource_group_object['Location']}")
    print(f"Provisioning State: {resource_group_object['ProvisioningState']}")
    print("------------------------------")

# Example: Querying specific information from the objects
specific_resource_group_name = 'YourResourceGroupName'
specific_resource_group = next((rg for rg in resource_group_objects if rg['Name'] == specific_resource_group_name), None)

if specific_resource_group:
    print(f"Details for Resource Group '{specific_resource_group_name}':")
    print(f"Location: {specific_resource_group['Location']}")
    print(f"Provisioning State: {specific_resource_group['ProvisioningState']}")
else:
    print(f"Resource Group '{specific_resource_group_name}' not found.")
