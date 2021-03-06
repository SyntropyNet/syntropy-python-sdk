![Tests](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/Tests/badge.svg)
![PyPi](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/PyPi/badge.svg)

# Syntropy SDK
Syntropy SDK for Python allows you to manage Syntropy Networks using simple Python interface.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 0.1.2
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
*AuthApi* | [**auth_delete_account**](docs/AuthApi.md#auth_delete_account) | **GET** /api/auth/delete-account/{code} | 
*AuthApi* | [**auth_geoip**](docs/AuthApi.md#auth_geoip) | **GET** /api/auth/{ip}/geoip | 
*AuthApi* | [**auth_local_login**](docs/AuthApi.md#auth_local_login) | **POST** /api/auth/local/login | 
*AuthApi* | [**auth_logout**](docs/AuthApi.md#auth_logout) | **POST** /api/auth/logout | 
*AuthApi* | [**auth_provider_attach**](docs/AuthApi.md#auth_provider_attach) | **POST** /api/auth/provider/attach | 
*AuthApi* | [**auth_provider_detach**](docs/AuthApi.md#auth_provider_detach) | **POST** /api/auth/provider/detach | 
*AuthApi* | [**auth_provider_login**](docs/AuthApi.md#auth_provider_login) | **POST** /api/auth/provider/login | 
*AuthApi* | [**auth_provider_register**](docs/AuthApi.md#auth_provider_register) | **POST** /api/auth/provider/register | 
*AuthApi* | [**auth_register**](docs/AuthApi.md#auth_register) | **POST** /api/auth/register | 
*AuthApi* | [**auth_reset_password**](docs/AuthApi.md#auth_reset_password) | **POST** /api/auth/reset-password | 
*AuthApi* | [**auth_send_delete_account_link**](docs/AuthApi.md#auth_send_delete_account_link) | **POST** /api/auth/send-delete-account-link | 
*AuthApi* | [**auth_send_reset_password_link**](docs/AuthApi.md#auth_send_reset_password_link) | **POST** /api/auth/send-reset-password-link | 
*AuthApi* | [**auth_send_verify_email_link**](docs/AuthApi.md#auth_send_verify_email_link) | **POST** /api/auth/send-verify-email-link | 
*AuthApi* | [**auth_user**](docs/AuthApi.md#auth_user) | **GET** /api/auth/user | 
*AuthApi* | [**auth_user_change_email**](docs/AuthApi.md#auth_user_change_email) | **POST** /api/auth/user/change-email | 
*AuthApi* | [**auth_user_change_password**](docs/AuthApi.md#auth_user_change_password) | **POST** /api/auth/user/change-password | 
*AuthApi* | [**auth_user_delete**](docs/AuthApi.md#auth_user_delete) | **POST** /api/auth/user/delete | 
*AuthApi* | [**auth_verify_email**](docs/AuthApi.md#auth_verify_email) | **GET** /api/auth/verify-email/{code} | 
*AuthApi* | [**auth_verify_email_deprecated**](docs/AuthApi.md#auth_verify_email_deprecated) | **POST** /api/auth/verify-email | 
*AuthApi* | [**update_settings**](docs/AuthApi.md#update_settings) | **PUT** /api/auth/settings | 
*PlatformApi* | [**platform_agent_destroy**](docs/PlatformApi.md#platform_agent_destroy) | **DELETE** /api/platform/agents/{agent_id} | 
*PlatformApi* | [**platform_agent_group_destroy**](docs/PlatformApi.md#platform_agent_group_destroy) | **DELETE** /api/platform/network/agent-groups/{group_id} | 
*PlatformApi* | [**platform_agent_group_update**](docs/PlatformApi.md#platform_agent_group_update) | **PUT** /api/platform/network/agent-groups/{group_id} | 
*PlatformApi* | [**platform_agent_id_name_pairs**](docs/PlatformApi.md#platform_agent_id_name_pairs) | **GET** /api/platform/agents/id-name-pairs | 
*PlatformApi* | [**platform_agent_index**](docs/PlatformApi.md#platform_agent_index) | **GET** /api/platform/agents | 
*PlatformApi* | [**platform_agent_provider_index**](docs/PlatformApi.md#platform_agent_provider_index) | **GET** /api/platform/agent-providers | 
*PlatformApi* | [**platform_agent_provider_show**](docs/PlatformApi.md#platform_agent_provider_show) | **GET** /api/platform/agent-providers/{id} | 
*PlatformApi* | [**platform_agent_service_destroy**](docs/PlatformApi.md#platform_agent_service_destroy) | **POST** /api/platform/agent-services-delete | 
*PlatformApi* | [**platform_agent_service_index**](docs/PlatformApi.md#platform_agent_service_index) | **GET** /api/platform/agent-services | 
*PlatformApi* | [**platform_agent_service_subnet_update**](docs/PlatformApi.md#platform_agent_service_subnet_update) | **POST** /api/platform/agent-services-subnets | 
*PlatformApi* | [**platform_agent_tag_index**](docs/PlatformApi.md#platform_agent_tag_index) | **GET** /api/platform/agent-tags | 
*PlatformApi* | [**platform_agent_update**](docs/PlatformApi.md#platform_agent_update) | **PATCH** /api/platform/agents/{agent_id} | 
*PlatformApi* | [**platform_api_key_create**](docs/PlatformApi.md#platform_api_key_create) | **POST** /api/platform/api-keys | 
*PlatformApi* | [**platform_api_key_destroy**](docs/PlatformApi.md#platform_api_key_destroy) | **DELETE** /api/platform/api-keys/{api_key_id} | 
*PlatformApi* | [**platform_api_key_index**](docs/PlatformApi.md#platform_api_key_index) | **GET** /api/platform/api-keys | 
*PlatformApi* | [**platform_api_key_update**](docs/PlatformApi.md#platform_api_key_update) | **PATCH** /api/platform/api-keys/{api_key_id} | 
*PlatformApi* | [**platform_config**](docs/PlatformApi.md#platform_config) | **GET** /api/platform/admin/agent/{agent_id}/config | 
*PlatformApi* | [**platform_connection_agent_destroy**](docs/PlatformApi.md#platform_connection_agent_destroy) | **DELETE** /api/platform/connections/agents/{agent_id} | 
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

 - [AdminAgentConfig](docs/AdminAgentConfig.md)
 - [AdminChangePasswordObject](docs/AdminChangePasswordObject.md)
 - [AgentConfigInfoNetwork](docs/AgentConfigInfoNetwork.md)
 - [AgentConfigInfoNetworkPUBLIC](docs/AgentConfigInfoNetworkPUBLIC.md)
 - [AgentConnectionObject](docs/AgentConnectionObject.md)
 - [AgentConnectionResponseConnectionPerformanceArrayArray_](docs/AgentConnectionResponseConnectionPerformanceArrayArray_.md)
 - [AgentConnectionStatus](docs/AgentConnectionStatus.md)
 - [AgentConnectionSubnetsDeletionObject](docs/AgentConnectionSubnetsDeletionObject.md)
 - [AgentGroupObject](docs/AgentGroupObject.md)
 - [AgentInterfaceBwObject](docs/AgentInterfaceBwObject.md)
 - [AgentInterfaceObject](docs/AgentInterfaceObject.md)
 - [AgentLockedFields](docs/AgentLockedFields.md)
 - [AgentMessagePayload](docs/AgentMessagePayload.md)
 - [AgentMessageType](docs/AgentMessageType.md)
 - [AgentNameIdPair](docs/AgentNameIdPair.md)
 - [AgentNetworkObject](docs/AgentNetworkObject.md)
 - [AgentObject](docs/AgentObject.md)
 - [AgentPathObject](docs/AgentPathObject.md)
 - [AgentProviderObject](docs/AgentProviderObject.md)
 - [AgentServiceObject](docs/AgentServiceObject.md)
 - [AgentServiceTypes](docs/AgentServiceTypes.md)
 - [AgentServicesDeletionObject](docs/AgentServicesDeletionObject.md)
 - [AgentServicesUpdateObject](docs/AgentServicesUpdateObject.md)
 - [AgentServicesUpdateObjectChanges](docs/AgentServicesUpdateObjectChanges.md)
 - [AgentSuccessResponse](docs/AgentSuccessResponse.md)
 - [AgentTagObject](docs/AgentTagObject.md)
 - [AgentsObject](docs/AgentsObject.md)
 - [AgentsPairObject](docs/AgentsPairObject.md)
 - [AnyOfAgentMessagePayload](docs/AnyOfAgentMessagePayload.md)
 - [AnyOfPlatformAgentMessagePayload](docs/AnyOfPlatformAgentMessagePayload.md)
 - [AnyOfPlatformAgentsHitObjectSourceSeverity](docs/AnyOfPlatformAgentsHitObjectSourceSeverity.md)
 - [AnyOfPlatformResponseErrorItemValue](docs/AnyOfPlatformResponseErrorItemValue.md)
 - [AnyOfSettingsTypes](docs/AnyOfSettingsTypes.md)
 - [AnyOfVppCallableObject](docs/AnyOfVppCallableObject.md)
 - [AnyOfWgCallableObject](docs/AnyOfWgCallableObject.md)
 - [AnyOfbodyCmd](docs/AnyOfbodyCmd.md)
 - [AnyOfinlineResponse204](docs/AnyOfinlineResponse204.md)
 - [ApiKeyObject](docs/ApiKeyObject.md)
 - [AuthInfo](docs/AuthInfo.md)
 - [AuthUserObject](docs/AuthUserObject.md)
 - [AutoAttach](docs/AutoAttach.md)
 - [AutoPingPayload](docs/AutoPingPayload.md)
 - [BehaviorType](docs/BehaviorType.md)
 - [BiStatistics](docs/BiStatistics.md)
 - [BiStatisticsEdgesPost](docs/BiStatisticsEdgesPost.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [ChangeEmailObject](docs/ChangeEmailObject.md)
 - [ChangePasswordObject](docs/ChangePasswordObject.md)
 - [ChangePathObject](docs/ChangePathObject.md)
 - [ChangePathObjectData](docs/ChangePathObjectData.md)
 - [ChangePathObjectDataCosts](docs/ChangePathObjectDataCosts.md)
 - [ColorObject](docs/ColorObject.md)
 - [ConnectionCreationBody](docs/ConnectionCreationBody.md)
 - [ConnectionCreationBodyMesh](docs/ConnectionCreationBodyMesh.md)
 - [ConnectionCreationBodyP2p](docs/ConnectionCreationBodyP2p.md)
 - [ConnectionPerformance](docs/ConnectionPerformance.md)
 - [ConstraintEnum](docs/ConstraintEnum.md)
 - [ContainerInfo](docs/ContainerInfo.md)
 - [ContentObject](docs/ContentObject.md)
 - [ContextType](docs/ContextType.md)
 - [DeleteUserObject](docs/DeleteUserObject.md)
 - [GeoIpObject](docs/GeoIpObject.md)
 - [GetInfoData](docs/GetInfoData.md)
 - [InlineResponse204](docs/InlineResponse204.md)
 - [InterfaceObject](docs/InterfaceObject.md)
 - [InterfaceType](docs/InterfaceType.md)
 - [LanguageObject](docs/LanguageObject.md)
 - [LinkObject](docs/LinkObject.md)
 - [LinkTag](docs/LinkTag.md)
 - [LogsReadTimestampEntityTypes](docs/LogsReadTimestampEntityTypes.md)
 - [LogsReadTimestampObject](docs/LogsReadTimestampObject.md)
 - [MailBodyTemplates](docs/MailBodyTemplates.md)
 - [MetadataNetworkType](docs/MetadataNetworkType.md)
 - [NetworkAgentObject](docs/NetworkAgentObject.md)
 - [NetworkAgentPayload](docs/NetworkAgentPayload.md)
 - [NetworkGenesisType](docs/NetworkGenesisType.md)
 - [NetworkInfoData](docs/NetworkInfoData.md)
 - [NetworkInfoObject](docs/NetworkInfoObject.md)
 - [NetworkMetadata](docs/NetworkMetadata.md)
 - [NetworkObject](docs/NetworkObject.md)
 - [NetworkTopologyObject](docs/NetworkTopologyObject.md)
 - [NetworkType](docs/NetworkType.md)
 - [PlatformAgentMessagePayload](docs/PlatformAgentMessagePayload.md)
 - [PlatformAgentMessagePayloadData](docs/PlatformAgentMessagePayloadData.md)
 - [PlatformAgentMessageType](docs/PlatformAgentMessageType.md)
 - [PlatformAgentStatus](docs/PlatformAgentStatus.md)
 - [PlatformAgentSuccessResponse](docs/PlatformAgentSuccessResponse.md)
 - [PlatformAgentsBodyObject](docs/PlatformAgentsBodyObject.md)
 - [PlatformAgentsErrorBody](docs/PlatformAgentsErrorBody.md)
 - [PlatformAgentsErrorResponse](docs/PlatformAgentsErrorResponse.md)
 - [PlatformAgentsErrorResponseHits](docs/PlatformAgentsErrorResponseHits.md)
 - [PlatformAgentsHitObject](docs/PlatformAgentsHitObject.md)
 - [PlatformAgentsHitObjectSource](docs/PlatformAgentsHitObjectSource.md)
 - [PlatformResponseAdminAgentConfig_](docs/PlatformResponseAdminAgentConfig_.md)
 - [PlatformResponseAgentConnectionObjectArray_](docs/PlatformResponseAgentConnectionObjectArray_.md)
 - [PlatformResponseAgentNameIdPairArray_](docs/PlatformResponseAgentNameIdPairArray_.md)
 - [PlatformResponseAgentObjectArray_](docs/PlatformResponseAgentObjectArray_.md)
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
 - [PlatformResponsePlatformAgentSuccessResponse_](docs/PlatformResponsePlatformAgentSuccessResponse_.md)
 - [PlatformResponseSuccessBoolean_](docs/PlatformResponseSuccessBoolean_.md)
 - [PlatformResponseSuccessbooleanData](docs/PlatformResponseSuccessbooleanData.md)
 - [PlatformResponseVoid_](docs/PlatformResponseVoid_.md)
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
 - [ResetPasswordObject](docs/ResetPasswordObject.md)
 - [ResetServerObject](docs/ResetServerObject.md)
 - [ResponseObject](docs/ResponseObject.md)
 - [RestartAgentObject](docs/RestartAgentObject.md)
 - [RouteObject](docs/RouteObject.md)
 - [S3ObjectListItem](docs/S3ObjectListItem.md)
 - [S3ObjectListItemOwner](docs/S3ObjectListItemOwner.md)
 - [S3SendData](docs/S3SendData.md)
 - [SendResetPasswordLinkObject](docs/SendResetPasswordLinkObject.md)
 - [SendVerifyEmailLinkObject](docs/SendVerifyEmailLinkObject.md)
 - [ServerAgentStatus](docs/ServerAgentStatus.md)
 - [ServerObject](docs/ServerObject.md)
 - [ServerSrSoftware](docs/ServerSrSoftware.md)
 - [SettingReadObject](docs/SettingReadObject.md)
 - [SettingWriteObject](docs/SettingWriteObject.md)
 - [SettingsTypes](docs/SettingsTypes.md)
 - [ShowSdnConnections](docs/ShowSdnConnections.md)
 - [SocialProviderObject](docs/SocialProviderObject.md)
 - [SocialProviderType](docs/SocialProviderType.md)
 - [SocialProviderTypeObject](docs/SocialProviderTypeObject.md)
 - [SocialProvidersIdsObject](docs/SocialProvidersIdsObject.md)
 - [SrPathObject](docs/SrPathObject.md)
 - [SrPolicyObject](docs/SrPolicyObject.md)
 - [Status](docs/Status.md)
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
 - [TsoaPartialUserAdminObject_](docs/TsoaPartialUserAdminObject_.md)
 - [TsoaPartialUserSrObject_](docs/TsoaPartialUserSrObject_.md)
 - [TsoaPartialVersionObject_](docs/TsoaPartialVersionObject_.md)
 - [TsoaPartialVpnObject_](docs/TsoaPartialVpnObject_.md)
 - [TunnelObject](docs/TunnelObject.md)
 - [UdpAndUtcPorts](docs/UdpAndUtcPorts.md)
 - [UpdateStatusBody](docs/UpdateStatusBody.md)
 - [UpdateStatusBodySubnetsToUpdate](docs/UpdateStatusBodySubnetsToUpdate.md)
 - [UpdateType](docs/UpdateType.md)
 - [UserAdminObject](docs/UserAdminObject.md)
 - [UserAgentPatchObject](docs/UserAgentPatchObject.md)
 - [UserApiKeyCreateObject](docs/UserApiKeyCreateObject.md)
 - [UserApiKeyUpdateObject](docs/UserApiKeyUpdateObject.md)
 - [UserLoginObject](docs/UserLoginObject.md)
 - [UserNetworkObject](docs/UserNetworkObject.md)
 - [UserRegisterObject](docs/UserRegisterObject.md)
 - [UserRegisterViaProviderObject](docs/UserRegisterViaProviderObject.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSrDirection](docs/UserSrDirection.md)
 - [UserSrObject](docs/UserSrObject.md)
 - [VerifyEmailObject](docs/VerifyEmailObject.md)
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
 - [WgCallableObject](docs/WgCallableObject.md)
 - [WgCreateInterface](docs/WgCreateInterface.md)
 - [WgCreateInterfaceArgs](docs/WgCreateInterfaceArgs.md)
 - [WgCreateInterfaceMetadata](docs/WgCreateInterfaceMetadata.md)
 - [WgKeypairObject](docs/WgKeypairObject.md)
 - [WgRemoveInterface](docs/WgRemoveInterface.md)
 - [WgRemoveInterfaceArgs](docs/WgRemoveInterfaceArgs.md)
 - [WgRemovePeer](docs/WgRemovePeer.md)
 - [WgRemovePeerArgs](docs/WgRemovePeerArgs.md)

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


