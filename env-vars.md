
# PowerShell
```
echo $Env:PATH
$env:Path-split';
$Env:AZURE_SUBSCRIPTION_ID

Get-ChildItem Env:
Get-ChildItem Env:<name>
(Get-Childitem Env:<name>).Value
(Get-Childitem Env:<name>).Value


Get-ChildItem Env:<name>
[System.Environment]::SetEnvironmentVariable("AZ_TENANT_ID", "", [System.EnvironmentVariableTarget]::User)

```
dir env:

# Windows Command prompt
**list env variables**
```
set
```
**set env variable**
```
set AZURE_SUBSCRIPTION_ID=<sub_id_guid>
```


