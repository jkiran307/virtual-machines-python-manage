import adal
import os
from msrestazure.azure_active_directory import AdalAuthentication
from azure.mgmt.resource import ResourceManagementClient

# Service Principal
tenant = 'AZURE_TENANT_ID'
client_id = 'AZURE_CLIENT_ID'
password = 'AZURE_CLIENT_SECRET'

# Public Azure - default values
authentication_endpoint = 'https://login.microsoftonline.com/'
azure_endpoint = 'https://management.azure.com/'

context = adal.AuthenticationContext(authentication_endpoint+tenant)
credentials = AdalAuthentication(
    context.acquire_token_with_client_credentials,
    azure_endpoint,
    client_id,
    password
)
subscription_id = 'AZURE_SUBSCRIPTION_ID'

resource_client = ResourceManagementClient(
    credentials,
    subscription_id,
    base_url=azure_endpoint
)

client = ResourceManagementClient(credentials, subscription_id)

resource_group_params = {'location':'Southindia'}

# Creating resource group

client.resource_groups.create_or_update('azure-sample-group', resource_group_params)

try:
  client.resource_groups.create_or_update('azure-sample-group', resource_group_params)
except:
  print("Resource Group already present")
