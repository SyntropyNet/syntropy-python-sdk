![Tests](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/Tests/badge.svg)
![PyPi](https://github.com/SyntropyNet/syntropy-python-sdk/workflows/PyPi/badge.svg)

# Syntropy SDK
Syntropy SDK for Python allows you to manage Syntropy Networks using simple Python interface.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 0.4.3

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
config.host = "url to the Syntropy Stack API"
config.api_key["api-key"] = "your api key"
api = sdk.ApiClient(config)

agents_api = sdk.AgentsApi(api)
try:
    api_response = WithRetry(agents_api.v1_network_agents_get)()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->v1_network_get: %s\n" % e)


# Create connections
connections_api = sdk.ConectionsApi(api)
try:
    body = sdk.V1NetworkConnectionsCreateP2PRequest(
        agent_pairs=[
            sdk.V1NetworkConnectionsCreateP2PRequestAgentPairs(agent_2_id=1, agent_1_id=0),
            sdk.V1NetworkConnectionsCreateP2PRequestAgentPairs(agent_2_id=2, agent_1_id=1),
            sdk.V1NetworkConnectionsCreateP2PRequestAgentPairs(agent_2_id=4, agent_1_id=2),
        ],
    )

    connections = connections_api.v1_network_connections_create_p2_p(body=body).data
except ApiException as e:
    print("Exception when creating a network: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.syntropystack.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**v1_network_agents_coordinates_search**](docs/AgentsApi.md#v1_network_agents_coordinates_search) | **POST** /v1/network/agents/coordinates/search | Search Agent location coordinates
*AgentsApi* | [**v1_network_agents_create**](docs/AgentsApi.md#v1_network_agents_create) | **POST** /v1/network/agents | Create Agent
*AgentsApi* | [**v1_network_agents_delete**](docs/AgentsApi.md#v1_network_agents_delete) | **DELETE** /v1/network/agents/{agent_id} | Delete Agent
*AgentsApi* | [**v1_network_agents_filters_search**](docs/AgentsApi.md#v1_network_agents_filters_search) | **POST** /v1/network/agents/filters/search | Search Agent filters
*AgentsApi* | [**v1_network_agents_get**](docs/AgentsApi.md#v1_network_agents_get) | **GET** /v1/network/agents | Get Agents
*AgentsApi* | [**v1_network_agents_logs_errors_search**](docs/AgentsApi.md#v1_network_agents_logs_errors_search) | **POST** /v1/network/agents/logs/errors/search | Search Agent error logs
*AgentsApi* | [**v1_network_agents_logs_reads_timestamp_search**](docs/AgentsApi.md#v1_network_agents_logs_reads_timestamp_search) | **POST** /v1/network/agents/logs-reads-timestamp | Save log read timestamp
*AgentsApi* | [**v1_network_agents_logs_search**](docs/AgentsApi.md#v1_network_agents_logs_search) | **POST** /v1/network/agents/logs/search | Search Agent logs
*AgentsApi* | [**v1_network_agents_providers_get**](docs/AgentsApi.md#v1_network_agents_providers_get) | **GET** /v1/network/agents/providers | Get Agent providers
*AgentsApi* | [**v1_network_agents_remove**](docs/AgentsApi.md#v1_network_agents_remove) | **POST** /v1/network/agents/remove | Delete Agents
*AgentsApi* | [**v1_network_agents_search**](docs/AgentsApi.md#v1_network_agents_search) | **POST** /v1/network/agents/search | Search Agents
*AgentsApi* | [**v1_network_agents_services_delete**](docs/AgentsApi.md#v1_network_agents_services_delete) | **DELETE** /v1/network/agents/services/{agent_service_subnet_id} | Delete Agent service
*AgentsApi* | [**v1_network_agents_services_get**](docs/AgentsApi.md#v1_network_agents_services_get) | **GET** /v1/network/agents/services | Get Agent services.
*AgentsApi* | [**v1_network_agents_services_remove**](docs/AgentsApi.md#v1_network_agents_services_remove) | **POST** /v1/network/agents/services/remove | Delete Agent services
*AgentsApi* | [**v1_network_agents_services_update**](docs/AgentsApi.md#v1_network_agents_services_update) | **PATCH** /v1/network/agents/services/bulk | Update Agent services
*AgentsApi* | [**v1_network_agents_settings_get**](docs/AgentsApi.md#v1_network_agents_settings_get) | **GET** /v1/network/agents/settings | Get Agent settings
*AgentsApi* | [**v1_network_agents_settings_update**](docs/AgentsApi.md#v1_network_agents_settings_update) | **PATCH** /v1/network/agents/settings | Update Agent settings
*AgentsApi* | [**v1_network_agents_tags_get**](docs/AgentsApi.md#v1_network_agents_tags_get) | **GET** /v1/network/agents/tags | Get Agent tags
*AgentsApi* | [**v1_network_agents_update**](docs/AgentsApi.md#v1_network_agents_update) | **PATCH** /v1/network/agents/{agent_id} | Updates Agent
*AgentsApi* | [**v1_network_agents_wg_config_get_one**](docs/AgentsApi.md#v1_network_agents_wg_config_get_one) | **GET** /v1/network/agents/wg-config/{agent_id} | Get Agent Wg config
*AnalyticsApi* | [**v1_network_a_bandwidth_get**](docs/AnalyticsApi.md#v1_network_a_bandwidth_get) | **GET** /v1/network/a/bandwidth | Get bandwidth
*AnalyticsApi* | [**v1_network_a_iface_active_change_get**](docs/AnalyticsApi.md#v1_network_a_iface_active_change_get) | **GET** /v1/network/a/iface-active-change | Get active iface changes
*AnalyticsApi* | [**v1_network_a_latency_get**](docs/AnalyticsApi.md#v1_network_a_latency_get) | **GET** /v1/network/a/latency | Get latency
*AnalyticsApi* | [**v1_network_a_packet_loss_get**](docs/AnalyticsApi.md#v1_network_a_packet_loss_get) | **GET** /v1/network/a/packet-loss | Get packet loss
*AnalyticsApi* | [**v1_network_a_statuses_search**](docs/AnalyticsApi.md#v1_network_a_statuses_search) | **POST** /v1/network/a/statuses/search | Search statuses
*AnalyticsApi* | [**v1_network_a_statuses_warnings_search**](docs/AnalyticsApi.md#v1_network_a_statuses_warnings_search) | **POST** /v1/network/a/statuses/warnings/search | Search status warnings
*AuditApi* | [**v1_network_audit_search**](docs/AuditApi.md#v1_network_audit_search) | **POST** /v1/network/audit/logs/search | Search audit logs
*AuthApi* | [**v1_network_auth_access_token_login**](docs/AuthApi.md#v1_network_auth_access_token_login) | **POST** /v1/network/auth/access-token/login | Login (Access token)
*AuthApi* | [**v1_network_auth_access_tokens_create**](docs/AuthApi.md#v1_network_auth_access_tokens_create) | **POST** /v1/network/auth/access-tokens | Create Access token
*AuthApi* | [**v1_network_auth_access_tokens_delete**](docs/AuthApi.md#v1_network_auth_access_tokens_delete) | **DELETE** /v1/network/auth/access-tokens/{access_token_id} | Delete Access token
*AuthApi* | [**v1_network_auth_access_tokens_get**](docs/AuthApi.md#v1_network_auth_access_tokens_get) | **GET** /v1/network/auth/access-tokens | Get Access tokens
*AuthApi* | [**v1_network_auth_access_tokens_permissions_get**](docs/AuthApi.md#v1_network_auth_access_tokens_permissions_get) | **GET** /v1/network/auth/access-tokens/permissions | Get Access token permissions
*AuthApi* | [**v1_network_auth_api_keys_create**](docs/AuthApi.md#v1_network_auth_api_keys_create) | **POST** /v1/network/auth/api-keys | Create API key
*AuthApi* | [**v1_network_auth_api_keys_delete**](docs/AuthApi.md#v1_network_auth_api_keys_delete) | **DELETE** /v1/network/auth/api-keys/{api_key_id} | Delete API key
*AuthApi* | [**v1_network_auth_api_keys_get**](docs/AuthApi.md#v1_network_auth_api_keys_get) | **GET** /v1/network/auth/api-keys | Get API keys
*AuthApi* | [**v1_network_auth_logout**](docs/AuthApi.md#v1_network_auth_logout) | **POST** /v1/network/auth/logout | Logout
*AuthApi* | [**v1_network_auth_mfa_confirm**](docs/AuthApi.md#v1_network_auth_mfa_confirm) | **POST** /v1/network/auth/mfa/confirm | Confirm MFA
*AuthApi* | [**v1_network_auth_mfa_disable**](docs/AuthApi.md#v1_network_auth_mfa_disable) | **POST** /v1/network/auth/mfa/disable | Disable MFA
*AuthApi* | [**v1_network_auth_mfa_disable_using_backup**](docs/AuthApi.md#v1_network_auth_mfa_disable_using_backup) | **POST** /v1/network/auth/mfa/disable-using-backup | Disable MFA (backup)
*AuthApi* | [**v1_network_auth_mfa_generate**](docs/AuthApi.md#v1_network_auth_mfa_generate) | **GET** /v1/network/auth/mfa/generate | Generate MFA
*AuthApi* | [**v1_network_auth_settings_update**](docs/AuthApi.md#v1_network_auth_settings_update) | **PATCH** /v1/network/auth/user/settings | Update User settings
*AuthApi* | [**v1_network_auth_user_get**](docs/AuthApi.md#v1_network_auth_user_get) | **GET** /v1/network/auth/user | Get User info
*AuthApi* | [**v1_network_auth_user_invitations_get**](docs/AuthApi.md#v1_network_auth_user_invitations_get) | **GET** /v1/network/auth/user/invitations | Get invitations for authenticated user
*AuthApi* | [**v1_network_auth_users_get**](docs/AuthApi.md#v1_network_auth_users_get) | **GET** /v1/network/auth/users | Get workspace users
*AuthApi* | [**v1_network_auth_users_remove**](docs/AuthApi.md#v1_network_auth_users_remove) | **POST** /v1/network/auth/users/remove | Remove users from workspace
*AuthApi* | [**v1_network_auth_users_role_update**](docs/AuthApi.md#v1_network_auth_users_role_update) | **PATCH** /v1/network/auth/users/{user_id}/role | Update user role in the workspace
*AuthApi* | [**v1_network_auth_verify_email**](docs/AuthApi.md#v1_network_auth_verify_email) | **POST** /v1/network/auth/verify-email/{code} | Verify email
*AuthApi* | [**v1_network_auth_workspace_create**](docs/AuthApi.md#v1_network_auth_workspace_create) | **POST** /v1/network/auth/workspaces | Create workspace
*AuthApi* | [**v1_network_auth_workspace_delete**](docs/AuthApi.md#v1_network_auth_workspace_delete) | **DELETE** /v1/network/auth/workspaces/{workspace_id} | Delete workspace
*AuthApi* | [**v1_network_auth_workspace_get**](docs/AuthApi.md#v1_network_auth_workspace_get) | **GET** /v1/network/auth/workspaces | Get workspaces
*AuthApi* | [**v1_network_auth_workspace_update**](docs/AuthApi.md#v1_network_auth_workspace_update) | **PATCH** /v1/network/auth/workspaces/{workspace_id} | Update workspace
*AuthApi* | [**v1_network_auth_workspaces_invitations_accept**](docs/AuthApi.md#v1_network_auth_workspaces_invitations_accept) | **POST** /v1/network/auth/workspaces/invitations/{invitation_id}/accept | Accept workspace invitation
*AuthApi* | [**v1_network_auth_workspaces_invitations_create**](docs/AuthApi.md#v1_network_auth_workspaces_invitations_create) | **POST** /v1/network/auth/workspaces/invitations | Create workspace invitation
*AuthApi* | [**v1_network_auth_workspaces_invitations_decline**](docs/AuthApi.md#v1_network_auth_workspaces_invitations_decline) | **POST** /v1/network/auth/workspaces/invitations/{invitation_id}/decline | Decline workspace invitation
*AuthApi* | [**v1_network_auth_workspaces_invitations_get**](docs/AuthApi.md#v1_network_auth_workspaces_invitations_get) | **GET** /v1/network/auth/workspaces/invitations | Get workspace invitations
*AuthApi* | [**v1_network_auth_workspaces_invitations_remove**](docs/AuthApi.md#v1_network_auth_workspaces_invitations_remove) | **POST** /v1/network/auth/workspaces/invitations/remove | Delete workspace invitations
*AuthApi* | [**v1_network_auth_workspaces_leave**](docs/AuthApi.md#v1_network_auth_workspaces_leave) | **POST** /v1/network/auth/workspaces/leave | Leave workspace
*ConnectionsApi* | [**v1_network_connections_create_mesh**](docs/ConnectionsApi.md#v1_network_connections_create_mesh) | **POST** /v1/network/connections/mesh | Create Connections Mesh
*ConnectionsApi* | [**v1_network_connections_create_p2_p**](docs/ConnectionsApi.md#v1_network_connections_create_p2_p) | **POST** /v1/network/connections/point-to-point | Create P2P Connections
*ConnectionsApi* | [**v1_network_connections_delete**](docs/ConnectionsApi.md#v1_network_connections_delete) | **DELETE** /v1/network/connections/{agent_connection_group_id} | Delete Connection
*ConnectionsApi* | [**v1_network_connections_get**](docs/ConnectionsApi.md#v1_network_connections_get) | **GET** /v1/network/connections | Get Connections
*ConnectionsApi* | [**v1_network_connections_remove**](docs/ConnectionsApi.md#v1_network_connections_remove) | **POST** /v1/network/connections/remove | Delete Connections
*ConnectionsApi* | [**v1_network_connections_search**](docs/ConnectionsApi.md#v1_network_connections_search) | **POST** /v1/network/connections/search | Search Connections
*ConnectionsApi* | [**v1_network_connections_services_delete**](docs/ConnectionsApi.md#v1_network_connections_services_delete) | **DELETE** /v1/network/connections/services/{agent_connection_subnet_id} | Delete Connection service
*ConnectionsApi* | [**v1_network_connections_services_get**](docs/ConnectionsApi.md#v1_network_connections_services_get) | **GET** /v1/network/connections/services | Get Connection services
*ConnectionsApi* | [**v1_network_connections_services_remove**](docs/ConnectionsApi.md#v1_network_connections_services_remove) | **POST** /v1/network/connections/services/remove | Delete Connection services
*ConnectionsApi* | [**v1_network_connections_services_update**](docs/ConnectionsApi.md#v1_network_connections_services_update) | **PATCH** /v1/network/connections/services | Update Connection services
*ConnectionsApi* | [**v1_network_connections_update**](docs/ConnectionsApi.md#v1_network_connections_update) | **PATCH** /v1/network/connections | Update Connections
*NetworkApi* | [**v1_network_get**](docs/NetworkApi.md#v1_network_get) | **GET** /v1/network | Get Network view
*NotificationApi* | [**v1_network_notification_user_contact_update**](docs/NotificationApi.md#v1_network_notification_user_contact_update) | **POST** /v1/network/notification/user-contact | Update User contact
*RulesApi* | [**rules_connection_point_to_tag_update**](docs/RulesApi.md#rules_connection_point_to_tag_update) | **PATCH** /v1/network/rules/connections/point-to-tag | Upsert point-to-tag
*RulesApi* | [**v1_network_rules_connections_point_to_tag_create**](docs/RulesApi.md#v1_network_rules_connections_point_to_tag_create) | **POST** /v1/network/rules/connections/point-to-tag | Create point-to-tag
*RulesApi* | [**v1_network_rules_connections_point_to_tag_get_one**](docs/RulesApi.md#v1_network_rules_connections_point_to_tag_get_one) | **GET** /v1/network/rules/connections/point-to-tag/{agent_id} | Get point-to-tag
*RulesApi* | [**v1_network_rules_connections_point_to_tag_search**](docs/RulesApi.md#v1_network_rules_connections_point_to_tag_search) | **POST** /v1/network/rules/connections/point-to-tag/search | Search point-to-tag Rules
*RulesApi* | [**v1_network_rules_search**](docs/RulesApi.md#v1_network_rules_search) | **POST** /v1/network/rules/search | Search Rules
*RulesApi* | [**v1_rules_connection_point_to_tag_remove**](docs/RulesApi.md#v1_rules_connection_point_to_tag_remove) | **POST** /v1/network/rules/connections/point-to-tag/remove | Remove point-to-tag
*SDNAgentsApi* | [**v1_network_sdn_agents_get**](docs/SDNAgentsApi.md#v1_network_sdn_agents_get) | **GET** /v1/network/sdn-agents/ips | Get SDN Agent ips

## Documentation For Models

 - [AData](docs/AData.md)
 - [ADataResponse](docs/ADataResponse.md)
 - [AccessTokenOrder](docs/AccessTokenOrder.md)
 - [AgentConnectionSubnetStatuses](docs/AgentConnectionSubnetStatuses.md)
 - [AgentFilterAgentStatus](docs/AgentFilterAgentStatus.md)
 - [AgentLockedFields](docs/AgentLockedFields.md)
 - [AgentLogLabels](docs/AgentLogLabels.md)
 - [AgentLogLog](docs/AgentLogLog.md)
 - [AgentLogSource](docs/AgentLogSource.md)
 - [AgentProvider](docs/AgentProvider.md)
 - [AgentProviderNameAndId](docs/AgentProviderNameAndId.md)
 - [AgentProviderOrderString](docs/AgentProviderOrderString.md)
 - [AgentServiceSubnetIdAndIp](docs/AgentServiceSubnetIdAndIp.md)
 - [AgentServiceTypes](docs/AgentServiceTypes.md)
 - [AgentServicesUpdateChanges](docs/AgentServicesUpdateChanges.md)
 - [AgentStatus](docs/AgentStatus.md)
 - [AgentTag](docs/AgentTag.md)
 - [AgentType](docs/AgentType.md)
 - [AgentTypeParam](docs/AgentTypeParam.md)
 - [AgentWgConfig](docs/AgentWgConfig.md)
 - [AnyOfV1AgentOrderItems](docs/AnyOfV1AgentOrderItems.md)
 - [AuditLog](docs/AuditLog.md)
 - [AuthSource](docs/AuthSource.md)
 - [ConnectionsPointtotagBody](docs/ConnectionsPointtotagBody.md)
 - [CoordinatesSearchBody](docs/CoordinatesSearchBody.md)
 - [DefaultString](docs/DefaultString.md)
 - [GetUserInvitationResponse](docs/GetUserInvitationResponse.md)
 - [IdNumber](docs/IdNumber.md)
 - [Ipv4](docs/Ipv4.md)
 - [LatencyDiff](docs/LatencyDiff.md)
 - [LatencyRatio](docs/LatencyRatio.md)
 - [Latitude](docs/Latitude.md)
 - [LogsReadTimestampEntityType](docs/LogsReadTimestampEntityType.md)
 - [Longitude](docs/Longitude.md)
 - [MFABackupCode](docs/MFABackupCode.md)
 - [MFACode](docs/MFACode.md)
 - [NetworkInfoAgentConnectionGroupAgent](docs/NetworkInfoAgentConnectionGroupAgent.md)
 - [OneOfV1ConnectionOrderItems](docs/OneOfV1ConnectionOrderItems.md)
 - [OneOfV1NetworkAgentsSettingsUpdateRequest](docs/OneOfV1NetworkAgentsSettingsUpdateRequest.md)
 - [OrderString](docs/OrderString.md)
 - [Permission](docs/Permission.md)
 - [Role](docs/Role.md)
 - [SkipNumber](docs/SkipNumber.md)
 - [TakeNumber](docs/TakeNumber.md)
 - [User](docs/User.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserTheme](docs/UserTheme.md)
 - [UserWithRole](docs/UserWithRole.md)
 - [UserWorkspace](docs/UserWorkspace.md)
 - [V1AAgentPair](docs/V1AAgentPair.md)
 - [V1AStatus](docs/V1AStatus.md)
 - [V1AStatusAgentStatus](docs/V1AStatusAgentStatus.md)
 - [V1AStatusWarning](docs/V1AStatusWarning.md)
 - [V1Agent](docs/V1Agent.md)
 - [V1AgentCoordinates](docs/V1AgentCoordinates.md)
 - [V1AgentCreateItem](docs/V1AgentCreateItem.md)
 - [V1AgentErrorLog](docs/V1AgentErrorLog.md)
 - [V1AgentErrorLogSource](docs/V1AgentErrorLogSource.md)
 - [V1AgentFilter](docs/V1AgentFilter.md)
 - [V1AgentFilters](docs/V1AgentFilters.md)
 - [V1AgentFiltersAgentName](docs/V1AgentFiltersAgentName.md)
 - [V1AgentLog](docs/V1AgentLog.md)
 - [V1AgentLogSeverity](docs/V1AgentLogSeverity.md)
 - [V1AgentLogSort](docs/V1AgentLogSort.md)
 - [V1AgentOrder](docs/V1AgentOrder.md)
 - [V1AgentService](docs/V1AgentService.md)
 - [V1AgentSettings](docs/V1AgentSettings.md)
 - [V1AgentSettingsReroutingThreshold](docs/V1AgentSettingsReroutingThreshold.md)
 - [V1AgentTag](docs/V1AgentTag.md)
 - [V1AuthAccessToken](docs/V1AuthAccessToken.md)
 - [V1AuthAccessTokenLoginItem](docs/V1AuthAccessTokenLoginItem.md)
 - [V1AuthAccessTokenPermissions](docs/V1AuthAccessTokenPermissions.md)
 - [V1AuthAccessTokensCreateItem](docs/V1AuthAccessTokensCreateItem.md)
 - [V1AuthApiKey](docs/V1AuthApiKey.md)
 - [V1AuthApiKeysCreateItem](docs/V1AuthApiKeysCreateItem.md)
 - [V1AuthMfaConfirm](docs/V1AuthMfaConfirm.md)
 - [V1AuthMfaGenerate](docs/V1AuthMfaGenerate.md)
 - [V1AuthUser](docs/V1AuthUser.md)
 - [V1Connection](docs/V1Connection.md)
 - [V1ConnectionAgent](docs/V1ConnectionAgent.md)
 - [V1ConnectionCreatedBy](docs/V1ConnectionCreatedBy.md)
 - [V1ConnectionFilter](docs/V1ConnectionFilter.md)
 - [V1ConnectionOrder](docs/V1ConnectionOrder.md)
 - [V1ConnectionService](docs/V1ConnectionService.md)
 - [V1ConnectionServiceAgent](docs/V1ConnectionServiceAgent.md)
 - [V1ConnectionServiceAgentService](docs/V1ConnectionServiceAgentService.md)
 - [V1ConnectionServiceAgentServiceAgentServiceSubnets](docs/V1ConnectionServiceAgentServiceAgentServiceSubnets.md)
 - [V1ConnectionServiceSubnet](docs/V1ConnectionServiceSubnet.md)
 - [V1ConnectionStatus](docs/V1ConnectionStatus.md)
 - [V1ConnectionUpdateChange](docs/V1ConnectionUpdateChange.md)
 - [V1ErrorResponse](docs/V1ErrorResponse.md)
 - [V1ErrorResponseErrors](docs/V1ErrorResponseErrors.md)
 - [V1Network](docs/V1Network.md)
 - [V1NetworkAStatusesSearchRequest](docs/V1NetworkAStatusesSearchRequest.md)
 - [V1NetworkAStatusesSearchRequestFilter](docs/V1NetworkAStatusesSearchRequestFilter.md)
 - [V1NetworkAStatusesSearchResponse](docs/V1NetworkAStatusesSearchResponse.md)
 - [V1NetworkAStatusesWarningsSearchRequest](docs/V1NetworkAStatusesWarningsSearchRequest.md)
 - [V1NetworkAStatusesWarningsSearchRequestFilter](docs/V1NetworkAStatusesWarningsSearchRequestFilter.md)
 - [V1NetworkAStatusesWarningsSearchRequestOrder](docs/V1NetworkAStatusesWarningsSearchRequestOrder.md)
 - [V1NetworkAStatusesWarningsSearchResponse](docs/V1NetworkAStatusesWarningsSearchResponse.md)
 - [V1NetworkAgent](docs/V1NetworkAgent.md)
 - [V1NetworkAgentsCoordinatesSearchResponse](docs/V1NetworkAgentsCoordinatesSearchResponse.md)
 - [V1NetworkAgentsCreateRequest](docs/V1NetworkAgentsCreateRequest.md)
 - [V1NetworkAgentsCreateResponse](docs/V1NetworkAgentsCreateResponse.md)
 - [V1NetworkAgentsFiltersSearchResponse](docs/V1NetworkAgentsFiltersSearchResponse.md)
 - [V1NetworkAgentsGetResponse](docs/V1NetworkAgentsGetResponse.md)
 - [V1NetworkAgentsLogsErrorsSearchRequest](docs/V1NetworkAgentsLogsErrorsSearchRequest.md)
 - [V1NetworkAgentsLogsErrorsSearchResponse](docs/V1NetworkAgentsLogsErrorsSearchResponse.md)
 - [V1NetworkAgentsLogsReadsTimestampSearchRequest](docs/V1NetworkAgentsLogsReadsTimestampSearchRequest.md)
 - [V1NetworkAgentsLogsSearchRequest](docs/V1NetworkAgentsLogsSearchRequest.md)
 - [V1NetworkAgentsLogsSearchResponse](docs/V1NetworkAgentsLogsSearchResponse.md)
 - [V1NetworkAgentsProvidersGetResponse](docs/V1NetworkAgentsProvidersGetResponse.md)
 - [V1NetworkAgentsRemoveRequest](docs/V1NetworkAgentsRemoveRequest.md)
 - [V1NetworkAgentsSearchRequest](docs/V1NetworkAgentsSearchRequest.md)
 - [V1NetworkAgentsSearchResponse](docs/V1NetworkAgentsSearchResponse.md)
 - [V1NetworkAgentsServicesGetResponse](docs/V1NetworkAgentsServicesGetResponse.md)
 - [V1NetworkAgentsServicesRemoveRequest](docs/V1NetworkAgentsServicesRemoveRequest.md)
 - [V1NetworkAgentsServicesUpdateRequest](docs/V1NetworkAgentsServicesUpdateRequest.md)
 - [V1NetworkAgentsServicesUpdateRequestSubnetsToUpdate](docs/V1NetworkAgentsServicesUpdateRequestSubnetsToUpdate.md)
 - [V1NetworkAgentsSettingsGetResponse](docs/V1NetworkAgentsSettingsGetResponse.md)
 - [V1NetworkAgentsSettingsUpdateRequest](docs/V1NetworkAgentsSettingsUpdateRequest.md)
 - [V1NetworkAgentsTagsGetResponse](docs/V1NetworkAgentsTagsGetResponse.md)
 - [V1NetworkAgentsUpdateRequest](docs/V1NetworkAgentsUpdateRequest.md)
 - [V1NetworkAgentsWgConfigGetOneResponse](docs/V1NetworkAgentsWgConfigGetOneResponse.md)
 - [V1NetworkAuditSearchRequest](docs/V1NetworkAuditSearchRequest.md)
 - [V1NetworkAuditSearchResponse](docs/V1NetworkAuditSearchResponse.md)
 - [V1NetworkAuthAccessTokenLoginRequest](docs/V1NetworkAuthAccessTokenLoginRequest.md)
 - [V1NetworkAuthAccessTokenLoginResponse](docs/V1NetworkAuthAccessTokenLoginResponse.md)
 - [V1NetworkAuthAccessTokensCreateRequest](docs/V1NetworkAuthAccessTokensCreateRequest.md)
 - [V1NetworkAuthAccessTokensCreateResponse](docs/V1NetworkAuthAccessTokensCreateResponse.md)
 - [V1NetworkAuthAccessTokensGetResponse](docs/V1NetworkAuthAccessTokensGetResponse.md)
 - [V1NetworkAuthAccessTokensPermissionsGetResponse](docs/V1NetworkAuthAccessTokensPermissionsGetResponse.md)
 - [V1NetworkAuthApiKeysCreateRequest](docs/V1NetworkAuthApiKeysCreateRequest.md)
 - [V1NetworkAuthApiKeysCreateResponse](docs/V1NetworkAuthApiKeysCreateResponse.md)
 - [V1NetworkAuthApiKeysGetResponse](docs/V1NetworkAuthApiKeysGetResponse.md)
 - [V1NetworkAuthMfaConfirmRequest](docs/V1NetworkAuthMfaConfirmRequest.md)
 - [V1NetworkAuthMfaConfirmResponse](docs/V1NetworkAuthMfaConfirmResponse.md)
 - [V1NetworkAuthMfaDisableRequest](docs/V1NetworkAuthMfaDisableRequest.md)
 - [V1NetworkAuthMfaDisableUsingBackupRequest](docs/V1NetworkAuthMfaDisableUsingBackupRequest.md)
 - [V1NetworkAuthMfaGenerateResponse](docs/V1NetworkAuthMfaGenerateResponse.md)
 - [V1NetworkAuthUserGetResponse](docs/V1NetworkAuthUserGetResponse.md)
 - [V1NetworkAuthUserInvitationsGetResponse](docs/V1NetworkAuthUserInvitationsGetResponse.md)
 - [V1NetworkAuthUsersGetResponse](docs/V1NetworkAuthUsersGetResponse.md)
 - [V1NetworkAuthUsersRemoveRequest](docs/V1NetworkAuthUsersRemoveRequest.md)
 - [V1NetworkAuthUsersRoleUpdateRequest](docs/V1NetworkAuthUsersRoleUpdateRequest.md)
 - [V1NetworkAuthWorkspaceCreateRequest](docs/V1NetworkAuthWorkspaceCreateRequest.md)
 - [V1NetworkAuthWorkspaceCreateResponse](docs/V1NetworkAuthWorkspaceCreateResponse.md)
 - [V1NetworkAuthWorkspaceGetResponse](docs/V1NetworkAuthWorkspaceGetResponse.md)
 - [V1NetworkAuthWorkspaceUpdateRequest](docs/V1NetworkAuthWorkspaceUpdateRequest.md)
 - [V1NetworkAuthWorkspacesInvitationsCreateRequest](docs/V1NetworkAuthWorkspacesInvitationsCreateRequest.md)
 - [V1NetworkAuthWorkspacesInvitationsCreateResponse](docs/V1NetworkAuthWorkspacesInvitationsCreateResponse.md)
 - [V1NetworkAuthWorkspacesInvitationsGetResponse](docs/V1NetworkAuthWorkspacesInvitationsGetResponse.md)
 - [V1NetworkAuthWorkspacesInvitationsRemoveRequest](docs/V1NetworkAuthWorkspacesInvitationsRemoveRequest.md)
 - [V1NetworkConnectionGroup](docs/V1NetworkConnectionGroup.md)
 - [V1NetworkConnectionsCreateMeshRequest](docs/V1NetworkConnectionsCreateMeshRequest.md)
 - [V1NetworkConnectionsCreateMeshRequestAgentIds](docs/V1NetworkConnectionsCreateMeshRequestAgentIds.md)
 - [V1NetworkConnectionsCreateP2PRequest](docs/V1NetworkConnectionsCreateP2PRequest.md)
 - [V1NetworkConnectionsCreateP2PRequestAgentPairs](docs/V1NetworkConnectionsCreateP2PRequestAgentPairs.md)
 - [V1NetworkConnectionsGetResponse](docs/V1NetworkConnectionsGetResponse.md)
 - [V1NetworkConnectionsRemoveRequest](docs/V1NetworkConnectionsRemoveRequest.md)
 - [V1NetworkConnectionsSearchRequest](docs/V1NetworkConnectionsSearchRequest.md)
 - [V1NetworkConnectionsSearchResponse](docs/V1NetworkConnectionsSearchResponse.md)
 - [V1NetworkConnectionsServicesGetResponse](docs/V1NetworkConnectionsServicesGetResponse.md)
 - [V1NetworkConnectionsServicesRemoveRequest](docs/V1NetworkConnectionsServicesRemoveRequest.md)
 - [V1NetworkConnectionsServicesUpdateRequest](docs/V1NetworkConnectionsServicesUpdateRequest.md)
 - [V1NetworkConnectionsUpdateRequest](docs/V1NetworkConnectionsUpdateRequest.md)
 - [V1NetworkGetResponse](docs/V1NetworkGetResponse.md)
 - [V1NetworkNotificationContactUpdateRequest](docs/V1NetworkNotificationContactUpdateRequest.md)
 - [V1NetworkRulesConnectionsPointToTagCreateResponse](docs/V1NetworkRulesConnectionsPointToTagCreateResponse.md)
 - [V1NetworkRulesConnectionsPointToTagGetOneResponse](docs/V1NetworkRulesConnectionsPointToTagGetOneResponse.md)
 - [V1NetworkRulesConnectionsPointToTagSearchRequest](docs/V1NetworkRulesConnectionsPointToTagSearchRequest.md)
 - [V1NetworkRulesConnectionsPointToTagSearchResponse](docs/V1NetworkRulesConnectionsPointToTagSearchResponse.md)
 - [V1NetworkRulesSearchRequest](docs/V1NetworkRulesSearchRequest.md)
 - [V1NetworkRulesSearchRequestFilter](docs/V1NetworkRulesSearchRequestFilter.md)
 - [V1NetworkRulesSearchResponse](docs/V1NetworkRulesSearchResponse.md)
 - [V1NetworkSdnAgentsGetResponse](docs/V1NetworkSdnAgentsGetResponse.md)
 - [V1RulesPointToTag](docs/V1RulesPointToTag.md)
 - [V1RulesPointToTagCreateItem](docs/V1RulesPointToTagCreateItem.md)
 - [V1RulesPointToTagFilter](docs/V1RulesPointToTagFilter.md)
 - [V1RulesSearchItem](docs/V1RulesSearchItem.md)
 - [V1SdnPaths](docs/V1SdnPaths.md)
 - [V1SkipNumber](docs/V1SkipNumber.md)
 - [V1TakeNumber](docs/V1TakeNumber.md)
 - [V1UpdateAgentRoutingSettings](docs/V1UpdateAgentRoutingSettings.md)
 - [V1UpdateAgentRoutingSettingsReroutingThreshold](docs/V1UpdateAgentRoutingSettingsReroutingThreshold.md)
 - [V1UpdateAgentRoutingSettingsReset](docs/V1UpdateAgentRoutingSettingsReset.md)
 - [WhereString](docs/WhereString.md)
 - [Workspace](docs/Workspace.md)
 - [WorkspaceInvitation](docs/WorkspaceInvitation.md)
 - [WorkspaceInvitationResponse](docs/WorkspaceInvitationResponse.md)
 - [WorkspaceName](docs/WorkspaceName.md)
 - [WorkspaceRoleName](docs/WorkspaceRoleName.md)

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

support@syntropynet.com
