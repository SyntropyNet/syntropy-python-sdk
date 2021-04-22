![Tests](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/Tests/badge.svg)
![PyPi](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/PyPi/badge.svg)

# Syntropy SDK
Syntropy SDK for Python allows you to manage Syntropy Networks using simple Python interface.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 0.1.4
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 3.6+

## Installation & Usage
### pip install

Install the SDK simply using pip:

```sh
pip install syntropy_sdk
```

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/SyntropyNet/syntropy-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/SyntropyNet/syntropy-python-sdk.git`)

Then import the package:
```python
import syntropy_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import syntropy_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then use the following as a reference:

```python
import syntropy_sdk as sdk
from syntropy_sdk.exceptions import ApiException
from syntropy_sdk.utils import WithRetry
from pprint import pprint

# Configure API
config = sdk.Configuration()
config.host = "url to the Syntropy Stack"
config.api_key["Authorization"] = "your api authorizaton token"
api = sdk.ApiClient(config)
platform_api = sdk.PlatformApi(api)

try:
    network_id = 123  # A valid network ID
    api_response = WithRetry(platform_api.platform_network_info)(network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformApi->platform_network_info: %s\n" % e)


# Create a network with connections
try:
    body = {
        "network_name": "My Network",
        "network_type": sdk.NetworkType.POINT_TO_POINT,  # Only POINT_TO_POINT types supported.
        "network_disable_sdn_connections": True,
        "network_metadata": {
            "network_created_by": sdk.NetworkGenesisType.SDK,
            "network_type": "P2P",
        },
    }
    api_response = WithRetry(platform_api.platform_network_create())

    network_id = api_response["data"]["network_id"]

    body = {
        "network_id": network_id,
        "agent_ids": [
            0, 1,  # Valid agent IDs
            1, 2,
            2, 4,
        ],
        "network_update_by": sdk.NetworkGenesisType.SDK,
    }
    connections = platform_api.platform_connection_create(body=body)["data"]
except ApiException as e:
    print("Exception when creating a network: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiKeysApi* | [**create_api_key**](docs/ApiKeysApi.md#create_api_key) | **POST** /auth/api-key | 
*ApiKeysApi* | [**delete_api_key**](docs/ApiKeysApi.md#delete_api_key) | **DELETE** /auth/api-key/{api_key_id} | 
*ApiKeysApi* | [**get_api_key**](docs/ApiKeysApi.md#get_api_key) | **GET** /auth/api-key | 
*AuthApi* | [**add_contact**](docs/AuthApi.md#add_contact) | **POST** /auth/authorization/contact | 
*AuthApi* | [**auth**](docs/AuthApi.md#auth) | **GET** /auth/authorization | 
*AuthApi* | [**auth_access_token_list**](docs/AuthApi.md#auth_access_token_list) | **GET** /auth/authorization/access-token | 
*AuthApi* | [**auth_access_token_login**](docs/AuthApi.md#auth_access_token_login) | **POST** /auth/authorization/access-token/login | 
*AuthApi* | [**auth_access_token_permissions_list**](docs/AuthApi.md#auth_access_token_permissions_list) | **GET** /auth/authorization/permissions/access-token | 
*AuthApi* | [**auth_access_token_user_create**](docs/AuthApi.md#auth_access_token_user_create) | **POST** /auth/authorization/access-token | 
*AuthApi* | [**auth_access_token_user_delete**](docs/AuthApi.md#auth_access_token_user_delete) | **DELETE** /auth/authorization/access-token/{id} | 
*AuthApi* | [**auth_create_user**](docs/AuthApi.md#auth_create_user) | **POST** /auth/authorization/create-user | 
*AuthApi* | [**auth_external_login**](docs/AuthApi.md#auth_external_login) | **POST** /auth/authorization/external/login | 
*AuthApi* | [**auth_logout**](docs/AuthApi.md#auth_logout) | **POST** /auth/authorization/logout | 
*AuthApi* | [**auth_show_user**](docs/AuthApi.md#auth_show_user) | **GET** /auth/authorization/user | 
*AuthApi* | [**auth_verify_email**](docs/AuthApi.md#auth_verify_email) | **GET** /auth/authorization/verify-email/{code} | 
*AuthApi* | [**update_settings**](docs/AuthApi.md#update_settings) | **PUT** /auth/authorization/settings | 
*AuthApi* | [**validate_captcha**](docs/AuthApi.md#validate_captcha) | **POST** /auth/authorization/validate-captcha | 
*AuthApi* | [**validate_captcha_0**](docs/AuthApi.md#validate_captcha_0) | **POST** /auth/authorization/validate-limit | 
*AuthApi* | [**validate_user_credentials**](docs/AuthApi.md#validate_user_credentials) | **POST** /auth/authorization/validate-user | 
*ApiKeysApi* | [**api_key_create**](docs/ApiKeysApi.md#api_key_create) | **POST** /api/api-keys | 
*ApiKeysApi* | [**api_key_destroy**](docs/ApiKeysApi.md#api_key_destroy) | **DELETE** /api/api-keys/{id} | 
*ApiKeysApi* | [**api_key_index**](docs/ApiKeysApi.md#api_key_index) | **GET** /api/api-keys | 
*ApiKeysApi* | [**api_key_show**](docs/ApiKeysApi.md#api_key_show) | **GET** /api/api-keys/{id} | 
*ApiKeysApi* | [**api_key_update**](docs/ApiKeysApi.md#api_key_update) | **PATCH** /api/api-keys/{id} | 
*PlatformApi* | [**platform_admin_agent_config**](docs/PlatformApi.md#platform_admin_agent_config) | **GET** /api/platform/admin/agent/{agent_id}/config | 
*PlatformApi* | [**platform_agent_config**](docs/PlatformApi.md#platform_agent_config) | **GET** /api/platform/agent/{agent_id}/config | 
*PlatformApi* | [**platform_agent_coordinates**](docs/PlatformApi.md#platform_agent_coordinates) | **POST** /api/platform/agents/coordinates | 
*PlatformApi* | [**platform_agent_create**](docs/PlatformApi.md#platform_agent_create) | **POST** /api/platform/agents | 
*PlatformApi* | [**platform_agent_destroy**](docs/PlatformApi.md#platform_agent_destroy) | **DELETE** /api/platform/agents/{agent_id} | 
*PlatformApi* | [**platform_agent_group_destroy**](docs/PlatformApi.md#platform_agent_group_destroy) | **DELETE** /api/platform/network/agent-groups/{group_id} | 
*PlatformApi* | [**platform_agent_group_update**](docs/PlatformApi.md#platform_agent_group_update) | **PUT** /api/platform/network/agent-groups/{group_id} | 
*PlatformApi* | [**platform_agent_id_name_pairs**](docs/PlatformApi.md#platform_agent_id_name_pairs) | **GET** /api/platform/agents/filters | 
*PlatformApi* | [**platform_agent_index**](docs/PlatformApi.md#platform_agent_index) | **GET** /api/platform/agents | 
*PlatformApi* | [**platform_agent_provider_index**](docs/PlatformApi.md#platform_agent_provider_index) | **GET** /api/platform/agent-providers | 
*PlatformApi* | [**platform_agent_provider_show**](docs/PlatformApi.md#platform_agent_provider_show) | **GET** /api/platform/agent-providers/{id} | 
*PlatformApi* | [**platform_agent_service_destroy**](docs/PlatformApi.md#platform_agent_service_destroy) | **POST** /api/platform/agent-services-delete | 
*PlatformApi* | [**platform_agent_service_index**](docs/PlatformApi.md#platform_agent_service_index) | **GET** /api/platform/agent-services | 
*PlatformApi* | [**platform_agent_service_subnet_update**](docs/PlatformApi.md#platform_agent_service_subnet_update) | **POST** /api/platform/agent-services-subnets | 
*PlatformApi* | [**platform_agent_tag_index**](docs/PlatformApi.md#platform_agent_tag_index) | **GET** /api/platform/agent-tags | 
*PlatformApi* | [**platform_agent_update**](docs/PlatformApi.md#platform_agent_update) | **PATCH** /api/platform/agents/{agent_id} | 
*PlatformApi* | [**platform_agents_destroy**](docs/PlatformApi.md#platform_agents_destroy) | **POST** /api/platform/agents/remove | 
*PlatformApi* | [**platform_api_key_create**](docs/PlatformApi.md#platform_api_key_create) | **POST** /api/platform/api-keys | 
*PlatformApi* | [**platform_api_key_destroy**](docs/PlatformApi.md#platform_api_key_destroy) | **DELETE** /api/platform/api-keys/{api_key_id} | 
*PlatformApi* | [**platform_api_key_index**](docs/PlatformApi.md#platform_api_key_index) | **GET** /api/platform/api-keys | 
*PlatformApi* | [**platform_config**](docs/PlatformApi.md#platform_config) | **GET** /api/platform/agent/{agent_id}/wg-config | 
*PlatformApi* | [**platform_connection_agent_destroy**](docs/PlatformApi.md#platform_connection_agent_destroy) | **DELETE** /api/platform/connections/agents/{agent_id} | 
*PlatformApi* | [**platform_connection_agents_destroy**](docs/PlatformApi.md#platform_connection_agents_destroy) | **POST** /api/platform/connections/agents/remove | 
*PlatformApi* | [**platform_connection_create**](docs/PlatformApi.md#platform_connection_create) | **POST** /api/platform/connections | 
*PlatformApi* | [**platform_connection_create_mesh**](docs/PlatformApi.md#platform_connection_create_mesh) | **POST** /api/platform/connections/mesh | 
*PlatformApi* | [**platform_connection_create_p2p**](docs/PlatformApi.md#platform_connection_create_p2p) | **POST** /api/platform/connections/point-to-point | 
*PlatformApi* | [**platform_connection_destroy**](docs/PlatformApi.md#platform_connection_destroy) | **POST** /api/platform/connections/remove | 
*PlatformApi* | [**platform_connection_destroy_deprecated**](docs/PlatformApi.md#platform_connection_destroy_deprecated) | **DELETE** /api/platform/connections/{connection_id} | 
*PlatformApi* | [**platform_connection_index**](docs/PlatformApi.md#platform_connection_index) | **GET** /api/platform/connections | 
*PlatformApi* | [**platform_connection_service_show**](docs/PlatformApi.md#platform_connection_service_show) | **GET** /api/platform/connection-services | 
*PlatformApi* | [**platform_connection_service_update**](docs/PlatformApi.md#platform_connection_service_update) | **POST** /api/platform/connection-services | 
*PlatformApi* | [**platform_connection_subnet_destroy**](docs/PlatformApi.md#platform_connection_subnet_destroy) | **POST** /api/platform/connection-services-delete | 
*PlatformApi* | [**platform_logs_read_timestamp**](docs/PlatformApi.md#platform_logs_read_timestamp) | **POST** /api/platform/logs-reads-timestamp | 
*PlatformApi* | [**platform_network_agent_create**](docs/PlatformApi.md#platform_network_agent_create) | **POST** /api/platform/network/{network_id}/agents/add | 
*PlatformApi* | [**platform_network_agent_create_deprecated**](docs/PlatformApi.md#platform_network_agent_create_deprecated) | **POST** /api/platform/network/{network_id}/agents | 
*PlatformApi* | [**platform_network_agent_destroy**](docs/PlatformApi.md#platform_network_agent_destroy) | **DELETE** /api/platform/networks/{network_id}/agents/{agent_id} | 
*PlatformApi* | [**platform_network_agent_group_create**](docs/PlatformApi.md#platform_network_agent_group_create) | **POST** /api/platform/network/{network_id}/agent-groups/{group_name} | 
*PlatformApi* | [**platform_network_agent_remove**](docs/PlatformApi.md#platform_network_agent_remove) | **POST** /api/platform/networks/{network_id}/agents/remove | 
*PlatformApi* | [**platform_network_agent_remove_deprecated**](docs/PlatformApi.md#platform_network_agent_remove_deprecated) | **DELETE** /api/platform/networks/{network_id}/agents | 
*PlatformApi* | [**platform_network_create**](docs/PlatformApi.md#platform_network_create) | **POST** /api/platform/networks | 
*PlatformApi* | [**platform_network_destroy**](docs/PlatformApi.md#platform_network_destroy) | **DELETE** /api/platform/networks/{network_id} | 
*PlatformApi* | [**platform_network_index**](docs/PlatformApi.md#platform_network_index) | **GET** /api/platform/networks | 
*PlatformApi* | [**platform_network_info**](docs/PlatformApi.md#platform_network_info) | **GET** /api/platform/network/{network_id}/info | 
*PlatformApi* | [**platform_network_network_agent_destroy_deprecated**](docs/PlatformApi.md#platform_network_network_agent_destroy_deprecated) | **POST** /api/platform/network/{network_id}/agents/delete | 
*PlatformApi* | [**platform_network_topology**](docs/PlatformApi.md#platform_network_topology) | **GET** /api/platform/networks/topology | 

## Documentation For Models

 - [AccessTokenData](docs/AccessTokenData.md)
 - [AccessTokenOrder](docs/AccessTokenOrder.md)
 - [AccessTokenReadData](docs/AccessTokenReadData.md)
 - [AccessTokenWriteData](docs/AccessTokenWriteData.md)
 - [AnyOfApiKeyCreateRequestApiKeyValidUntil](docs/AnyOfApiKeyCreateRequestApiKeyValidUntil.md)
 - [AnyOfApiKeyDtoApiKeyCreatedAt](docs/AnyOfApiKeyDtoApiKeyCreatedAt.md)
 - [AnyOfApiKeyDtoApiKeyUpdatedAt](docs/AnyOfApiKeyDtoApiKeyUpdatedAt.md)
 - [AnyOfApiKeyDtoApiKeyValidUntil](docs/AnyOfApiKeyDtoApiKeyValidUntil.md)
 - [AnyOfApiKeyObjectApiKeyCreatedAt](docs/AnyOfApiKeyObjectApiKeyCreatedAt.md)
 - [AnyOfApiKeyObjectApiKeyUpdatedAt](docs/AnyOfApiKeyObjectApiKeyUpdatedAt.md)
 - [AnyOfApiKeyObjectApiKeyValidUntil](docs/AnyOfApiKeyObjectApiKeyValidUntil.md)
 - [AnyOfVerifyMFARequestCode](docs/AnyOfVerifyMFARequestCode.md)
 - [ApiKeyCreateRequest](docs/ApiKeyCreateRequest.md)
 - [ApiKeyDto](docs/ApiKeyDto.md)
 - [ApiKeyObject](docs/ApiKeyObject.md)
 - [ApiResponseApiKeyDtoArray_](docs/ApiResponseApiKeyDtoArray_.md)
 - [ApiResponseApiKeyObject_](docs/ApiResponseApiKeyObject_.md)
 - [AuthSource](docs/AuthSource.md)
 - [AzureUserTokenDto](docs/AzureUserTokenDto.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [CheckMFAForNewSocialAccountRequest](docs/CheckMFAForNewSocialAccountRequest.md)
 - [CheckMFAForNewSocialAccountResponse](docs/CheckMFAForNewSocialAccountResponse.md)
 - [CodeGenerationResponse](docs/CodeGenerationResponse.md)
 - [ConfirmMFARequest](docs/ConfirmMFARequest.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [DisableMFARequest](docs/DisableMFARequest.md)
 - [DisableMFAUsingBackupRequest](docs/DisableMFAUsingBackupRequest.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [MFABackupCode](docs/MFABackupCode.md)
 - [MFACode](docs/MFACode.md)
 - [MfaCodeType](docs/MfaCodeType.md)
 - [PermissionObject](docs/PermissionObject.md)
 - [UserDataResponse](docs/UserDataResponse.md)
 - [UserSettingsObject](docs/UserSettingsObject.md)
 - [VerifyMFARequest](docs/VerifyMFARequest.md)
 - [AdminAgentConfig](docs/AdminAgentConfig.md)
 - [AgentConnectionObject](docs/AgentConnectionObject.md)
 - [AgentConnectionResponseConnectionPerformanceArrayArray_](docs/AgentConnectionResponseConnectionPerformanceArrayArray_.md)
 - [AgentConnectionStatus](docs/AgentConnectionStatus.md)
 - [AgentConnectionSubnetsDeletionObject](docs/AgentConnectionSubnetsDeletionObject.md)
 - [AgentCoordinatesObject](docs/AgentCoordinatesObject.md)
 - [AgentFiltersObject](docs/AgentFiltersObject.md)
 - [AgentGroupObject](docs/AgentGroupObject.md)
 - [AgentInterfaceBwObject](docs/AgentInterfaceBwObject.md)
 - [AgentInterfaceMetadata](docs/AgentInterfaceMetadata.md)
 - [AgentInterfaceObject](docs/AgentInterfaceObject.md)
 - [AgentInterfacesMetadata](docs/AgentInterfacesMetadata.md)
 - [AgentLockedFields](docs/AgentLockedFields.md)
 - [AgentMessagePayload](docs/AgentMessagePayload.md)
 - [AgentMessageType](docs/AgentMessageType.md)
 - [AgentNetworkObject](docs/AgentNetworkObject.md)
 - [AgentObject](docs/AgentObject.md)
 - [AgentPathObject](docs/AgentPathObject.md)
 - [AgentProviderObject](docs/AgentProviderObject.md)
 - [AgentProviderOrderString](docs/AgentProviderOrderString.md)
 - [AgentServiceObject](docs/AgentServiceObject.md)
 - [AgentServiceTypes](docs/AgentServiceTypes.md)
 - [AgentServicesDeletionObject](docs/AgentServicesDeletionObject.md)
 - [AgentServicesUpdateChangesObject](docs/AgentServicesUpdateChangesObject.md)
 - [AgentServicesUpdateObject](docs/AgentServicesUpdateObject.md)
 - [AgentSuccessResponse](docs/AgentSuccessResponse.md)
 - [AgentTagObject](docs/AgentTagObject.md)
 - [AgentVersion](docs/AgentVersion.md)
 - [AgentsObject](docs/AgentsObject.md)
 - [AgentsPairObject](docs/AgentsPairObject.md)
 - [AnyOfAgentMessagePayload](docs/AnyOfAgentMessagePayload.md)
 - [AnyOfPlatformResponseErrorItemValue](docs/AnyOfPlatformResponseErrorItemValue.md)
 - [AnyOfVppCallableObject](docs/AnyOfVppCallableObject.md)
 - [AnyOfWgCallableObject](docs/AnyOfWgCallableObject.md)
 - [AnyOfinlineResponse204](docs/AnyOfinlineResponse204.md)
 - [ApiKeyObject](docs/ApiKeyObject.md)
 - [AutoPingPayload](docs/AutoPingPayload.md)
 - [BehaviorType](docs/BehaviorType.md)
 - [BiStatistics](docs/BiStatistics.md)
 - [BiStatisticsEdgesPost](docs/BiStatisticsEdgesPost.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [ChangePathObject](docs/ChangePathObject.md)
 - [ChangePathObjectData](docs/ChangePathObjectData.md)
 - [ChangePathObjectDataCosts](docs/ChangePathObjectDataCosts.md)
 - [ColorObject](docs/ColorObject.md)
 - [ConnectionCreationBody](docs/ConnectionCreationBody.md)
 - [ConnectionCreationBodyMesh](docs/ConnectionCreationBodyMesh.md)
 - [ConnectionCreationBodyP2p](docs/ConnectionCreationBodyP2p.md)
 - [ConnectionPerformance](docs/ConnectionPerformance.md)
 - [ConstraintEnum](docs/ConstraintEnum.md)
 - [ContentObject](docs/ContentObject.md)
 - [ContextType](docs/ContextType.md)
 - [DefaultString](docs/DefaultString.md)
 - [IdNumber](docs/IdNumber.md)
 - [InlineResponse204](docs/InlineResponse204.md)
 - [InterfaceObject](docs/InterfaceObject.md)
 - [InterfaceType](docs/InterfaceType.md)
 - [Ipv4](docs/Ipv4.md)
 - [LanguageObject](docs/LanguageObject.md)
 - [Latitude](docs/Latitude.md)
 - [LinkObject](docs/LinkObject.md)
 - [LinkTag](docs/LinkTag.md)
 - [LogsReadTimestampEntityTypes](docs/LogsReadTimestampEntityTypes.md)
 - [LogsReadTimestampObject](docs/LogsReadTimestampObject.md)
 - [Longitude](docs/Longitude.md)
 - [MetadataNetworkType](docs/MetadataNetworkType.md)
 - [NetworkAgentObject](docs/NetworkAgentObject.md)
 - [NetworkAgentPayload](docs/NetworkAgentPayload.md)
 - [NetworkGenesisType](docs/NetworkGenesisType.md)
 - [NetworkInfoObject](docs/NetworkInfoObject.md)
 - [NetworkMetadata](docs/NetworkMetadata.md)
 - [NetworkObject](docs/NetworkObject.md)
 - [NetworkTopologyObject](docs/NetworkTopologyObject.md)
 - [OrderString](docs/OrderString.md)
 - [PlatformAgentStatus](docs/PlatformAgentStatus.md)
 - [PlatformAgentTypeLocal](docs/PlatformAgentTypeLocal.md)
 - [PlatformAgentsBodyObject](docs/PlatformAgentsBodyObject.md)
 - [PlatformAgentsErrorBody](docs/PlatformAgentsErrorBody.md)
 - [PlatformAgentsErrorResponse](docs/PlatformAgentsErrorResponse.md)
 - [PlatformAgentsErrorResponseHits](docs/PlatformAgentsErrorResponseHits.md)
 - [PlatformAgentsHitObject](docs/PlatformAgentsHitObject.md)
 - [PlatformAgentsHitObjectSource](docs/PlatformAgentsHitObjectSource.md)
 - [PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3AstringData](docs/PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3AstringData.md)
 - [PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3Astring_](docs/PlatformResponse5BLinkTagPublic5D3F3Astring5BLinkTagSdn15D3F3Astring5BLinkTagSdn25D3F3Astring5BLinkTagSdn35D3F3Astring_.md)
 - [PlatformResponseAdminAgentConfig_](docs/PlatformResponseAdminAgentConfig_.md)
 - [PlatformResponseAgentConnectionObjectArray_](docs/PlatformResponseAgentConnectionObjectArray_.md)
 - [PlatformResponseAgentCoordinatesObjectArray_](docs/PlatformResponseAgentCoordinatesObjectArray_.md)
 - [PlatformResponseAgentFiltersObject_](docs/PlatformResponseAgentFiltersObject_.md)
 - [PlatformResponseAgentObjectArray_](docs/PlatformResponseAgentObjectArray_.md)
 - [PlatformResponseAgentObject_](docs/PlatformResponseAgentObject_.md)
 - [PlatformResponseAgentProviderObjectArray_](docs/PlatformResponseAgentProviderObjectArray_.md)
 - [PlatformResponseAgentProviderObject_](docs/PlatformResponseAgentProviderObject_.md)
 - [PlatformResponseAgentServiceObjectArray_](docs/PlatformResponseAgentServiceObjectArray_.md)
 - [PlatformResponseAgentSuccessResponse_](docs/PlatformResponseAgentSuccessResponse_.md)
 - [PlatformResponseAgentTagObjectArray_](docs/PlatformResponseAgentTagObjectArray_.md)
 - [PlatformResponseApiKeyObjectArray_](docs/PlatformResponseApiKeyObjectArray_.md)
 - [PlatformResponseApiKeyObject_](docs/PlatformResponseApiKeyObject_.md)
 - [PlatformResponseErrorItem](docs/PlatformResponseErrorItem.md)
 - [PlatformResponseNetworkInfoObject_](docs/PlatformResponseNetworkInfoObject_.md)
 - [PlatformResponseNetworkObjectArray_](docs/PlatformResponseNetworkObjectArray_.md)
 - [PlatformResponseNetworkObject_](docs/PlatformResponseNetworkObject_.md)
 - [PlatformResponseNetworkTopologyObjectArray_](docs/PlatformResponseNetworkTopologyObjectArray_.md)
 - [PlatformResponseSuccessBoolean_](docs/PlatformResponseSuccessBoolean_.md)
 - [PlatformResponseSuccessbooleanData](docs/PlatformResponseSuccessbooleanData.md)
 - [PlatformResponseVoid_](docs/PlatformResponseVoid_.md)
 - [Port](docs/Port.md)
 - [ProviderObject](docs/ProviderObject.md)
 - [PublicAppInfoObject](docs/PublicAppInfoObject.md)
 - [PublicLanguageObject](docs/PublicLanguageObject.md)
 - [PublicLanguagesObject](docs/PublicLanguagesObject.md)
 - [PublicLinkObject](docs/PublicLinkObject.md)
 - [PublicLinksLangCodeObject](docs/PublicLinksLangCodeObject.md)
 - [PublicLinksObject](docs/PublicLinksObject.md)
 - [PublicTranslationObject](docs/PublicTranslationObject.md)
 - [PublicTranslationsLangCodeObject](docs/PublicTranslationsLangCodeObject.md)
 - [PublicTranslationsObject](docs/PublicTranslationsObject.md)
 - [PublicVersionsObject](docs/PublicVersionsObject.md)
 - [RegionObject](docs/RegionObject.md)
 - [ResetServerObject](docs/ResetServerObject.md)
 - [RestartAgentObject](docs/RestartAgentObject.md)
 - [RouteObject](docs/RouteObject.md)
 - [S3ObjectListItem](docs/S3ObjectListItem.md)
 - [S3ObjectListItemOwner](docs/S3ObjectListItemOwner.md)
 - [S3SendData](docs/S3SendData.md)
 - [ServerAgentStatus](docs/ServerAgentStatus.md)
 - [ServerObject](docs/ServerObject.md)
 - [ServerSrSoftware](docs/ServerSrSoftware.md)
 - [SettingReadObject](docs/SettingReadObject.md)
 - [SettingWriteObject](docs/SettingWriteObject.md)
 - [SettingsTypes](docs/SettingsTypes.md)
 - [ShowSdnConnections](docs/ShowSdnConnections.md)
 - [SkipNumber](docs/SkipNumber.md)
 - [SrPathObject](docs/SrPathObject.md)
 - [SrPolicyObject](docs/SrPolicyObject.md)
 - [Status](docs/Status.md)
 - [TakeNumber](docs/TakeNumber.md)
 - [TopologyObject](docs/TopologyObject.md)
 - [TranslationObject](docs/TranslationObject.md)
 - [TsoaPartialAgentConnectionObject_](docs/TsoaPartialAgentConnectionObject_.md)
 - [TsoaPartialAgentInterfaceBwObject_](docs/TsoaPartialAgentInterfaceBwObject_.md)
 - [TsoaPartialAgentInterfaceObject_](docs/TsoaPartialAgentInterfaceObject_.md)
 - [TsoaPartialAgentNetworkObject_](docs/TsoaPartialAgentNetworkObject_.md)
 - [TsoaPartialAgentObject_](docs/TsoaPartialAgentObject_.md)
 - [TsoaPartialAgentPathObject_](docs/TsoaPartialAgentPathObject_.md)
 - [TsoaPartialAgentProviderObject_](docs/TsoaPartialAgentProviderObject_.md)
 - [TsoaPartialApiKeyObject_](docs/TsoaPartialApiKeyObject_.md)
 - [TsoaPartialColorObject_](docs/TsoaPartialColorObject_.md)
 - [TsoaPartialContentObject_](docs/TsoaPartialContentObject_.md)
 - [TsoaPartialInterfaceObject_](docs/TsoaPartialInterfaceObject_.md)
 - [TsoaPartialLanguageObject_](docs/TsoaPartialLanguageObject_.md)
 - [TsoaPartialLinkObject_](docs/TsoaPartialLinkObject_.md)
 - [TsoaPartialNetworkObject_](docs/TsoaPartialNetworkObject_.md)
 - [TsoaPartialProviderObject_](docs/TsoaPartialProviderObject_.md)
 - [TsoaPartialRegionObject_](docs/TsoaPartialRegionObject_.md)
 - [TsoaPartialRouteObject_](docs/TsoaPartialRouteObject_.md)
 - [TsoaPartialServerObject_](docs/TsoaPartialServerObject_.md)
 - [TsoaPartialTopologyObject_](docs/TsoaPartialTopologyObject_.md)
 - [TsoaPartialTranslationObject_](docs/TsoaPartialTranslationObject_.md)
 - [TsoaPartialTunnelObject_](docs/TsoaPartialTunnelObject_.md)
 - [TsoaPartialUserSrObject_](docs/TsoaPartialUserSrObject_.md)
 - [TsoaPartialVersionObject_](docs/TsoaPartialVersionObject_.md)
 - [TsoaPartialVpnObject_](docs/TsoaPartialVpnObject_.md)
 - [TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_](docs/TsoaPickAgentAgentIdOrAgentLocationLatOrAgentLocationLon_.md)
 - [TsoaPickAgentAgentLocationCountry_](docs/TsoaPickAgentAgentLocationCountry_.md)
 - [TsoaPickAgentAgentNameOrAgentId_](docs/TsoaPickAgentAgentNameOrAgentId_.md)
 - [TsoaPickAgentAgentVersion_](docs/TsoaPickAgentAgentVersion_.md)
 - [TunnelObject](docs/TunnelObject.md)
 - [UpdateStatusBody](docs/UpdateStatusBody.md)
 - [UpdateStatusBodySubnetsToUpdate](docs/UpdateStatusBodySubnetsToUpdate.md)
 - [UserAdminObject](docs/UserAdminObject.md)
 - [UserAgentCreateObject](docs/UserAgentCreateObject.md)
 - [UserAgentPatchObject](docs/UserAgentPatchObject.md)
 - [UserApiKeyCreateObject](docs/UserApiKeyCreateObject.md)
 - [UserNetworkObject](docs/UserNetworkObject.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSrDirection](docs/UserSrDirection.md)
 - [UserSrObject](docs/UserSrObject.md)
 - [VersionObject](docs/VersionObject.md)
 - [VersionType](docs/VersionType.md)
 - [VisibilityType](docs/VisibilityType.md)
 - [VpnObject](docs/VpnObject.md)
 - [VppCallableObject](docs/VppCallableObject.md)
 - [VppCallableObjectArgs](docs/VppCallableObjectArgs.md)
 - [VppCallableObjectArgs1](docs/VppCallableObjectArgs1.md)
 - [VppCallableObjectArgs10](docs/VppCallableObjectArgs10.md)
 - [VppCallableObjectArgs11](docs/VppCallableObjectArgs11.md)
 - [VppCallableObjectArgs12](docs/VppCallableObjectArgs12.md)
 - [VppCallableObjectArgs13](docs/VppCallableObjectArgs13.md)
 - [VppCallableObjectArgs14](docs/VppCallableObjectArgs14.md)
 - [VppCallableObjectArgs15](docs/VppCallableObjectArgs15.md)
 - [VppCallableObjectArgs16](docs/VppCallableObjectArgs16.md)
 - [VppCallableObjectArgs2](docs/VppCallableObjectArgs2.md)
 - [VppCallableObjectArgs3](docs/VppCallableObjectArgs3.md)
 - [VppCallableObjectArgs4](docs/VppCallableObjectArgs4.md)
 - [VppCallableObjectArgs5](docs/VppCallableObjectArgs5.md)
 - [VppCallableObjectArgs6](docs/VppCallableObjectArgs6.md)
 - [VppCallableObjectArgs7](docs/VppCallableObjectArgs7.md)
 - [VppCallableObjectArgs8](docs/VppCallableObjectArgs8.md)
 - [VppCallableObjectArgs9](docs/VppCallableObjectArgs9.md)
 - [WgAddPeer](docs/WgAddPeer.md)
 - [WgAddPeerArgs](docs/WgAddPeerArgs.md)
 - [WgAddPeerMetadata](docs/WgAddPeerMetadata.md)
 - [WgAddPeerMetadataAllowedIpsInfo](docs/WgAddPeerMetadataAllowedIpsInfo.md)
 - [WgCallableObject](docs/WgCallableObject.md)
 - [WgCreateInterface](docs/WgCreateInterface.md)
 - [WgCreateInterfaceArgs](docs/WgCreateInterfaceArgs.md)
 - [WgCreateInterfaceMetadata](docs/WgCreateInterfaceMetadata.md)
 - [WgKeypairObject](docs/WgKeypairObject.md)
 - [WgPublicKey](docs/WgPublicKey.md)
 - [WgRemoveInterface](docs/WgRemoveInterface.md)
 - [WgRemoveInterfaceArgs](docs/WgRemoveInterfaceArgs.md)
 - [WgRemovePeer](docs/WgRemovePeer.md)
 - [WgRemovePeerArgs](docs/WgRemovePeerArgs.md)
 - [WhereString](docs/WhereString.md)

## Documentation For Authorization
In order to use this SDK you must have a valid API Authorization token.
This token can be obtained either by using `AuthApi.local` method or using the UI.
This token should be passed to the configuration object like so:

```Python
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
```

## jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


