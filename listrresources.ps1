# No import module statements as Az PowerShell is installed.

# Connect to your Azure account (if not already connected)  
Connect-AzAccount # -TenantId 
$subscriptionId = ''
  
Set-AzContext -SubscriptionId $subscriptionId # -TenantId ''
Get-AzContext
$resourceGroupName = "demoGroup"
$storageAccountName = "strgrk3920345"  # Must be globally unique
$location = "East US"  
$accountType = 'Standard_LRS'  # Standard_LRS, Standard_GRS, Standard_RAGRS, Premium_LRS
# Create a new storage account
$strgResult = New-AzStorageAccount -ResourceGroupName $resourceGroupName `
    -AccountName $storageAccountName -Location $location -SkuName $accountType
# Get all resources in the specified resource group  
$resources = Get-AzResource -ResourceGroupName $resourceGroupName  
$resources.Id
# Initialize an empty hashtable to store the results  
$resourceData = @{}  
# Loop through the resources and store the data in the hashtable  
foreach ($resource in $resources) {  
    $resourceData[$resource.Name] = @{  
        'ResourceType' = $resource.ResourceType  
        'Location'     = $resource.Location  
    }  
}  
# Display the resource data stored in the hashtable  
$resourceData 