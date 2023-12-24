
$SUB_ID = Get-ChildItem Env:AZURE_SUBSCRIPTION_ID
Get-ChildItem Env:AZURE_RESOURCE_GROUP
$SUB_ID
# Define the Azure CLI command to list resource groups and output as JSON
$azCliCommand = "az group list --output json"

# Execute the Azure CLI command and capture the output
$azCliOutput = Invoke-Expression -Command $azCliCommand

# Convert the JSON output to PowerShell objects
$resourceGroups = $azCliOutput | ConvertFrom-Json

# Loop through the resource groups and store information in PowerShell objects
$resourceGroupObjects = foreach ($resourceGroup in $resourceGroups) {
    [PSCustomObject]@{
        Name = $resourceGroup.Name
        Location = $resourceGroup.Location
        ProvisioningState = $resourceGroup.ProvisioningState
    }
}

# Display the properties of the resource groups
$resourceGroupObjects | Format-Table -AutoSize

# Example: Querying specific information from the objects
$specificResourceGroup = $resourceGroupObjects | Where-Object { $_.Name -eq 'demoGroup' }

if ($specificResourceGroup) {
    Write-Host "Details for Resource Group 'YourResourceGroupName':"
    Write-Host "Location: $($specificResourceGroup.Location)"
    Write-Host "Provisioning State: $($specificResourceGroup.ProvisioningState)"
} else {
    Write-Host "Resource Group 'YourResourceGroupName' not found."
}
