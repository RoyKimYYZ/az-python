# az-python
Python code with respect to Azure and AI scenarios for learning, sharing and proof of concepts.

**References

https://learn.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-resource-group

https://azure.github.io/azure-sdk-for-python/




## Uinsg GitHub Actions Workflow

## Prerequisites
1. create or use existing Azure Entra (fromerly Azure AD) service principal name (spn) that has contributor role on the subscription or existing resource group to deploy into.
2. store SPN credentials (client id and client secret) as a GitHub repository secret

### Workflow Logic:
1. Manual user trigger with user input.
2. A workflow job that runs on ubuntu
3. Checkout the repository
4. Login in with the desired azure subscription with stored service principal secret credentials
5. Setup Python with desired version
6. Install python packages and dependencies that is required by my python code.
7. Build my Python code into a package as an command line tool
8. Call the command line tool and pass in the argument values from the workflow input fields.
