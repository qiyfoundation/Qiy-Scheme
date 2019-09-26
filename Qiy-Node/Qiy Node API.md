# Qiy Node API

This document describes the Qiy Node API.

Software developers use the api for Qiy-based solutions (as provided interface) or [Qiy Node Implementations][Definitions Qiy Node Implementation] (as requirement for implementation).



# Qiy Node

A [Qiy Node][Definitions Qiy Node] can be viewed as a digital identity for [Individuals][Definitions Individual] and/or organizations ([Service Providers][Definitions Service Provider]).
Qiy Nodes can be used in solutions that enable Individuals to provide [Relying Parties][Definitions Relying Party] access to personal data that are protected by [Data Providers][Definitions Data Provider].

Individuals acquire Qiy Nodes [when they start using Qiy-based end-user applications][Creating Qiy Nodes for Individuals].

Service Providers are provided with at least three Qiy Nodes by their [Access Provider][Definitions Access Provider]; one for the production environment, one for the acceptance environment and one for the development environment.


# Resource Access Management

The Qiy Node API main feature is Resource Access Management;
it can be used by a [controller] (eg Individual) to provide a [client] (eg Relying Party) access to a [Service] from a [Service Endpoint] protected by the [Server] (eg Data Provider) using [Feeds], for example as follows:
* The server announces the available Service, see [Set service catalogue].
* The controller connects with the server, see [Request connection].
* The server identifies the controller (out of bounds).
* The controller connects with the client, see [Request connection].
* The client requests the controller for a feed, see [Request for feed].
* The controller accepts the feed and sets the server as the source, see [Set feed source].
* The server uses the feed to access the service, see [Access feed].


# API Servers

The api is provided in a development environment, the acceptance environment and the production environment.
In addition, a proxy server for the develoment environment is provided to ease discovery, experimentation, and evaluation.

The server urls are:

| Server Name      | Server url                                                          |
| ---------------- | ------------------------------------------------------------------- |
| Proxy            | https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/proxy |
| Dev2             | https://dev2-user.testonly.digital-me.nl/user                       |
| Acceptance       | https://user.dolden.net/user                                        |


The server url of the Production environment is provided in the entry-transition phase, when a [Qiy Application][Definitions Qiy Application] goes live.

## Proxy server

The proxy server provides an easy means to access the development environment for taking care of the authentication.
The proxy server cannot be used to create Qiy Nodes, please use the [Qiy Test Tool][Qiy Test Tool pa] instead.
Afterwards, Qiy Nodes can be accessed via their '/qiy_nodes/<node_name>/proxy'-endpoint:

* App authentication is provided when an 'Authorization'-header parameter is provided in the request.
* App authentication and user authentication is provided when an 'Authorization-node-QTN'-header parameter is provided in the request. 
* App authentication, user authentication and transport authentication is provided when a 'password'-header parameter is provided in the request. 

The values of the 'Autorization-node-QTN'-header parameter and the 'password'-header parameters are always ignored.
The value of the 'Autorization'-header parameter is reused when basic authentication is used and ignored otherwise.

## Service Desk

The api provides access to the [Qiy Trust Network][Definitions Qiy Trust Network] which is provided by its [Access Providers][Definitions Access Provider].
Please contact the Service Desk of your Access Provider for your requests. 

The Service Desk of the Access Provider [DigitalMe] is available during regular CE(S)T office hours and can be contacted by e-mail or phone:

    service _at_ digital-me _dot_ nl
    +31 (0) 411-616565


# Versions

The api is versioned using [Semantic Versioning 2.0.0](https://semver.org) and follows the rules described in [Qiy Scheme Releases](../Qiy%20Scheme%20Releases.md).
The version of the api described in the Qiy Node API, this document, is the same as the version of the [Qiy Scheme][Definitions Qiy Scheme] that it is part of.

In addition, the following rules apply for [Qiy Node Implementations][Definitions Qiy Node Implementation]:

* Two major versions must be supported in the production environment: one primary version and one secondary version.
* The major versions should be supported in an acceptance environment.
* The secondary version must be supported for at least 6 months.
* One development version may be supported in a development environment.
* The development version may change at any time.

The version of the api that is supported must be returned by [Get /api].


# Authentication

## App Authentication

[Qiy Applications][Definitions Qiy Application] are required to authenticate requests using an [API Key][Definitions API Key] implemented using basic authentication, see for example [GET /api].

Two API Keys are provided by Access Providers: one for the Production environment and one for the other environments.

## User Authentication

User Authentication ensures that a Qiy Node is only accessed by its rightfull owner.

Most requests must be user authenticated using a signed token that can only be calculated using a [Qiy Node Credential][Definitions Qiy Node Credential] as described below.
The token is passed in the 'Authorization-node-QTN'-header parameter, see for example [POST /FeedsEndpoint/{feedId}].

### Python

In Python, the authorization header parameter can be calculated with the package 'pyOpenSSL'. Using a pem-file with the primary key of the Qiy Node it can be generated as follows:

```
from OpenSSL.crypto import sign
from base64 import b64encode
import OpenSSL

def authHeader(qiy_node_id, unix_time_in_msecs, body):
        tosign="{0}{1}{2}".format(qiy_node_id, unix_time_in_msecs, body)
        print("tosign: '{0}'".format(tosign))
        with open(<File with private key in pem format>,"r") as f:
                buffer=f.read()
        key=OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM,buffer)
        signature=b64encode(sign(
                key
                ,tosign
                ,"sha256")
                ).decode()
        return "QTF {0} {1}:{2}".format(qiy_node_id, unix_time_in_msecs, signature)
```

### Bash

The authorization header parameter can be generated with this Bash script:

```
#!/usr/bin/env bash

set -eu

#########################
# Test input to make things reproducable
#########################
UUID="bd89bab6-9d28-48ae-ba90-c3ed6472f502"
NONCE="1497006092128"
INPUT=""

#########################
# Cacluate the actual signature
#########################
authHeader() {
    local -r NONCE=$(date +%s%3N)
    local -r TOSIGN="${UUID}${NONCE}${1:-}"
    local -r SIG=$(printf "%s" "${TOSIGN}" | openssl dgst -sha256 -sign ${UUID}_private.pem | base64 -w0)
    AUTH_HEADER="QTF ${UUID} ${NONCE}:${SIG}"
}

#########################
# Convert private key to PEM
#########################
genPem() {
    local -r dashes="-----"
    local -r private_key='<MAKE SURE TO REPLACE THIS TEXT WITH THE PRIVATE KEY BEFORE USING THIS SCRIPT>'
    printf "%sBEGIN RSA PRIVATE KEY%s\n%s\n%sEND RSA PRIVATE KEY%s\n" "${dashes}" "${dashes}" "${private_key}" "${dashes}" "${dashes}" > ${UUID}_private.pem
}

#########################
# Do actual work
#########################
genPem
authHeader "${INPUT}"
echo -e "Given \n  input = [${INPUT}], \n  nonce = [${NONCE}] and \n  ID    = [${UUID}] \nWhen I calculate the Authorization header\nThen the value should be: \n  [${AUTH_HEADER}]"
```

## Transport Authentication

Some requests require [Transport Authentication][Definitions Transport Authentication] in order to access the [Transport Layer]. Authentication can be achieved by providing the Transport Password, a uuid, in the 'password'-header parameter, see for example [POST /ConnectionCreateEndpoint].


# Dynamic Endpoint Addresses

The Qiy Node Api uses [dynamic endpoint addresses][Annex A Dynamic Endpoint Addresses] most of which can be obtained using [GET /api]. The addresses can be cached, but should be refreshed every day.


# Events

The Qiy Node API provides a number of [Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events)-events which can be catched with [Start listening to events](#start-listening-to-events), see [Annex B Events].


# Callbacks

The events can also be catched using callbacks. Also, the Qiy Node API provides some additional callbacks for servers, see [Annex C Callbacks].


# API

## Api info

An App Authenticated [GET /api] can be used to get the api version and the current address of the [Node Create Endpoint].


# Nodes

## Request creation of Qiy Node

This [Node Create Endpoint]-call can be used to request the [creation of a Qiy Node][Creating Qiy Nodes for Individuals], see [Request creation of Qiy Node request].


## Get endpoint addresses

[GET /api] can be used to get the current addresses of the [Dynamic Endpoint Addresses].


## Set event callback endpoints

This [Event Callbacks Endpoint]-request can be used to define the addresses of the [Event Callback Endpoints], see [Set event callback endpoints request].


## Get event callback endpoints

This [Event Callbacks Endpoint](#event-callbacks-endpoint)-request can be used to get the addresses of the event callback endpoints, see [Get event callback endpoints request].


## Start listening to events

After [connecting][Request connection] to servers and clients, controllers use this [Events Endpoint](#events-endpoint)-call to catch requests for feed in [User Action Message Events], see [Start listening to events request].

The request starts a long-living session with a heartbeat to keep the session open. 
Every 10 seconds a line with the text ':ping' will be sent. If this is not received for more than that time, something has gone wrong.

The [Qiy Test Tool][Qiy Test Tool pa] can be used to monitor the events of a Qiy Node using the 'qiy_nodes/<node_name>/events'-path, see for example [https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/events](https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/events).

## Get node settings

This [Node Settings Endpoint]-call returns the node settings, see [Get node settings request].


## Set node settings

This [Node Settings Endpoint]-call can be used to change the node settings, see [Set node settings request].


## Delete Qiy Node

This [Self Endpoint]-call can be used to delete a Qiy Node, see [Delete Qiy Node request].


# Services

## Get service catalogue

This [Service Catalogue Endpoint]-call can be used to get the details of the [Service Catalogue][Definitions Service Catalogue] and of the [Service Endpoint(s)][Service Endpoint] of a Qiy Node, see [Get service catalogue request].


## Set service catalogue

A server uses this [Service Catalogue Endpoint]-call to publish the provided services using his [Service Catalogue][Definitions Service Catalogue] and related [Service Endpoint(s)][Service Endpoint], see [Set service catalogue request].

Afterwards, [Feed Request Callbacks] and [Access Feed Callbacks] are received for these services.

# Connections

## Client/Server

### Request connect token

This [Connect Token Create Endpoint]-call can be used to request a [Connect Token][Definitions Connect Token], see [Request connect token request].

The request results in a [State Handled Event] and/or [State Handled Callback] with a matching connection url whenever the connect token was used to create a [Connection][Definitions Connection].

### Register connect token

This [Connect Token Create Endpoint]-call can be used to register a [Connect Token][Definitions Connect Token], see [Register connect token request].

The request results in a [State Handled Event] and/or [State Handled Callback] with a matching connection url whenever the connect token was used to create a [Connection][Definitions Connection].


The Connect Token is a json-object with three members which can be created as follows:

    * id: This is a label and can be any string.
    * target: The format of this member is returned in the "target-template"-member of the response of [Get endpoint addresses], where '~id~' should be a uuid.
    * tmpSecret: This member is a string: an array of 16 random bytes which is base64-encoded.

In Java the tmpSecret can be generated as follows:

```
SecureRandom RANDOM = new SecureRandom();
byte[] tmpSecret = new byte[16];
RANDOM.nextBytes(tmpSecret);
String tmpSecretString = Base64.getEncoder().encodeToString(tmpSecret);
```

## Controller

### Request connection

Controllers use this [Connection Create Endpoint]-call to initiate a connection, see [Request connection request].

The state of the connection can be monitored using [List connections] or [Get connection], but a [State Handled Event] and/or [State Handled Callback] with a matching connection url will be fired when the connection has been established.

The request uses a [Connect Token][Definitions Connect Token] that has been registered or requested by a client or a server, see [Request connect token] or [Register connect token].


## Get connection

This [Connection Endpoint]-call returns the details of a connection, see [Get connection request].


## Get connect token

This [Connect Token Endpoint]-call returns the details of a [Connect Token][Definitions Connect Token], see [Get connect token request].


## List connect tokens

This [Connect Token List Endpoint]-call lists the connect tokens, see [List connect tokens request].


## List connections

This [Connection List Endpoint]-call can be used to list connections, see [List connections request].


# Messages

## Send message

This [Messages Endpoint]-call can be used to send a message to a connected Qiy Node, see [Send message request].


## List messages

This [Messages Endpoint]-call lists messages, see [List messages request].


# Feeds

## Client

### Request for feed

A client uses this [Connection Feeds Endpoint]-call to initiate a feed, see [Request for feed request].
Optionally, a body parameter can be included in the 'input'-member of the body json object as a base64-encoded byte array.

The request returns an inactive feed, the status of which can be monitored using [List feeds].
A [Data Reference Received-v2 Event] and a [Data Reference Received-v2 Callback] will be fired when the feed has been established. 


### Access feed

A client uses this [Feeds Endpoint]-call to access a single feed, see [Access feed request].
The body may include operation request parameters encoded as a base-64 encoded byte array.


### Access feeds

A client uses this [Feeds Endpoint]-call to access one or more feeds, see [Access feeds request].


### List feeds

This [Feeds Endpoint]-request can be used to list the feeds of a Qiy Node or of a connection for all or a set of [Service Types][Definitions Service Type] (also known as 'protocols'), see [List feeds request].


## Server

A server receives a [Feed Request Callback] when a controller has set him as the source of a feed, see [Add feed source] or [Set feed source].

A server receives an [Access Feed Callback] after an [Access feed] or [Access feeds].

## Controller

### Get user action message

An End User App receives a [User Action Message Event] when a connected client has asked for a feed to access one of his resources, see [Request for feed].
The event contains an [Action Message Endpoint]-address that can be used with this call to get the details of the action message, see [Get user action message].

### List action messages

A controller uses this [Action Message List Endpoint]-call to get all open requests for feeds, see [List action messages request].

### Set feed source

When a controller has received an access request in a [User Action Message Event], he extracts the details of the request using a [Get action message], which lists the possible sources and related action urls.

Controllers use [Set feed source request] to accept the request and set a source for the feed.


### Add feed source

When a controller has received an access request in a [User Action Message Event], he extracts the details of the request using a [Get action message], which lists the possible sources and related action urls.

Controllers use [Add feed source request] to accept the request and set or add a source for the feed.


# Annex A Dynamic Endpoint Addresses

This annex describes the Dynamic Endpoint Addresses

## Action Endpoint

This endpoint can be used for [Set feed source] and [Add feed source].
The current address of the endpoint is returned in the action messages returned by [List action messages] and [Get action message].

## Action Message Endpoint

This endpoint can be used for [Get action message].
The current address of the endpoint is returned by [List action messages] and included in [User Action Message Event].

## Action Message List Endpoint

This endpoint can be used for [List action messages]. The current address of the endpoint is returned in the "amList"-member of the response of [Get endpoint addresses].

## Connect Token Create Endpoint

This endpoint can be used to [request][Request connect token] or [register][Register connect token] [Connect Tokens][Definitions Connect Token]. The current address of the endpoint is returned in the "ctCreate"-member of the response of Get endpoint addresses.

## Connect Token Endpoint

This endpoint can be used for [Get connect token].
The endpoint address (connect token url) is returned by [Request connect token], [Register connect token], and [List connect tokens] (in links.self).

## Connect Token List Endpoint

This endpoint can be used for [List connect tokens]. The current address of the endpoint is returned in the "ctList"-member of the response of [Get endpoint addresses].

## Connection Create Endpoint

This endpoint can be used for [Request connection]. The current address of the endpoint is returned in the "scan"-member of the response of [Get endpoint addresses].

## Connection Endpoint

This endpoint can be used for [Get connection]. The endpoint urls are returned by [Request connection] and [List connections].

## Connection Feeds Endpoint

This endpoint can be used for [Request for feed].

The current address of the endpoint is returned in the "links.feeds"-member of the response of [Get connection] or [List connections].

## Connection List Endpoint

This endpoint can be used for [List connections]. The current address of the endpoint is returned in the "connections"-member of the response of [Get endpoint addresses].

## Events Endpoint

This endpoint can be used for [Start listening to events]. The current address of the endpoint is returned in the "events"-member of the response of [Get endpoint addresses].

## Event Callbacks Endpoint

This endpoint can be used to [set][Set event callback endpoints] or [get][Get event callback endpoints] the addresses of the [Event Callback Endpoints].
The current addresses of the Event Callbacks Endpoint is returned in the "eventCallbacks"-member of the response of [Get endpoint addresses].

## Feeds Endpoint

A client uses this endpoint to [list][List feeds] or [access one][Access feed] or [more][Access feeds] feeds of a single controller or all connected controllers.

The address of the endpoint for a connection is returned in the "feeds"-member of the response of [List connections] and/or [Get connection].
The address of the endpoint for a Qiy Node is returned in the "feeds"-member of the response of [Get endpoint addresses].

## Messages Endpoint

This endpoint can be used for [Send message] and [List messages]. 
The current address of the endpoint is returned in a "mbox"-member of the response of [List connections] or [Get connection].

## Manage References Endpoint

This endpoint is deprecated.
The current address of the endpoint is returned in the "manRef"-member of the response of [List connections] or [Get connection].

## Node Create Endpoint

This endpoint can be used for [Request creation of Qiy Node].
The current address of the endpoint is returned by [Get /api].

## Node Settings Endpoint

This endpoint can be used for [Get node settings] and [Set node settings].
The current address of the endpoint is returned in the "nodeSettings"-member of the response of [Get endpoint addresses].

## Reference Endpoint

This endpoint is deprecated.

## References Endpoint

This endpoint is deprecated.

## Self Endpoint

This endpoint can be used for [Delete Qiy Node].
The endpoint address is returned in the 'self'-property of [Get endpoint addresses].

## Service Endpoint

This endpoint is provided by a server to serve feeds, see [Feed request callback].
It can be read and set with [Set service catalogue] and [Get service catalogue] respectively.

Note: This endpoint have to be whitelisted by the Access Provider before it can be used.

## Service Access Endpoint

This endpoint is provided by a server to serve resources, see [Access Feed Callback].
Its address is [Service Endpoint] appended with 'resolve'. 

## Service Catalogue Endpoint

This endpoint can be used to [get][Get service catalogue] or [set][Set service catalogue] the contents of a [Service Catalogue][Definitions Service Catalogue].
The current address of the endpoint is returned in the "serviceCatalog"-member of the response of [Get endpoint addresses].

## Target Template Endpoint

This endpoint can be used to [create off line connect tokens](#offline-connect-tokens).
The current address of the endpoint is returned in the "target-tempate"-member of the response of [Get endpoint addresses].


# Annex B Events

This section describes the Qiy Node events.

## Connected to Router Event

This event is fired after a request for a connection and can be used to monitor the creation of a connection.

## Connected to Router Failed Event

This event is fired after a request for a connection and signals that a connection could not be established.

## Data Reference Failure Event

This event is fired when a [Request for feed] fails.

## Data Reference Received-v2 Event

This event is fired when a source is set or added for a feed, see [Request for feed], [Add feed source] or [Set feed source].

## Data Request Forwarded Event

This event is fired after an [Access feed] if and when the access request is forwarded to a server.

## Data Request Fulfilled Event

This event is fired after an [Access feed] if and when a feed has been accessed succesfully.

## Data Request Failure Event

This event is fired after an [Access feed] if and when a feed could not be accessed succesfully.

## Data Request Not Forwarded Event

This event is fired after an [Access feed] if and when a access request cannot be forwarded to a server.

## Pending Peer Data Reference Event

This event can be fired after an [Access feed].

## Unexpected Data Reference Event

This event can be fired after an [Access feed].

## Persistent Id Event

This event can be used to monitor the creation of a connection.

## Routing Failure Event

This event is fired after [Get connection] and signals that a connection could not be established.

## Shared Secret Received Event

This event is fired after [Get connection] upon setting up a connection.

## Shared Secret Sent Event

This event is fired after [Get connection] upon setting up a connection.

## State Handled Event

This event is fired after [Get connection] when a connection has been established.

## User Action Message Event

This event is fired if and when a user action message is received, see for example [Set feed source].

Example event

```
event: USER_ACTION_MESSAGE data: {
   'type': 'USER_ACTION_MESSAGE',
   'connectionUrl': 'https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e',
   'extraData': 'https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4'
}
```

# Annex C Callbacks

This annex describes the callbacks of the Qiy Node API.

## Event Callbacks

This section describes the Qiy Node API Event Callbacks.

### Event Callback Endpoints

This section describes the Event Callback Endpoints.

#### Data Reference Received-v2 Callback Endpoint

This [Event Callback Endpoint] can be used as an alternative for the [Data Reference Received-v2 Event].
It can be configured using [Set event callback endpoints].

#### State Handled Callback Endpoint

This [Event Callback Endpoint] can be used as an alternative for the [State Handled Event].
It can be configured using [Set event callback endpoints].

### Data Reference Received-v2 Callback

This [Data Reference Received-v2 Callback Endpoint]-callback is fired when a source is set for a feed, see [Request for feed], [Set feed source] and [Add feed source].

### State Handled Callback

This [State Handled Callback Endpoint]-callback is executed when a Connect Token has been used to create a connection, see [Register connect token] or [Request connect token].


## Server Callbacks

### Feed Request Callback

A server receives this [Service Endpoint]-callback when an controller has set him as the source of a feed, see [Set feed source] or [Add feed source].

### Access Feed Callback

A server receives this [Service Access Endpoint]-callback after an [Access feed].


[Access feed]: #access-feed
[Access feed request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/Access_feed
[Access Feed Callback]: #access-feed-callback
[Access Feed Callbacks]: #access-feed-callback
[Access feeds]: #access-feeds
[Access feeds request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/Access_feeds
[Add feed source]: #add-feed-source
[Add feed source request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/Add_feed_source
[Action Endpoint]: #action-endpoint
[Action Message Endpoint]: #action-message-endpoint
[Action Message List Endpoint]: #action-message-list-endpoint
[Annex A Dynamic Endpoint Addresses]: #annex-a-dynamic-endpoint-addresses
[Annex B Events]: #annex-b-events
[Annex C Callbacks]: #annex-c-callbacks
[Client]: https://fdriesenaar.github.io/openapi-doc.html#/client
[Connect Token Create Endpoint]: #connect-token-create-endpoint
[Connect Token Endpoint]: #connect-token-endpoint
[Connect Token List Endpoint]: #connect-token-list-endpoint
[Connection Create Endpoint]: #connection-create-endpoint
[Connection Endpoint]: #connection-endpoint
[Connection Feeds Endpoint]: #connection-feeds-endpoint
[Connection List Endpoint]: #connection-list-endpoint
[Controller]: https://fdriesenaar.github.io/openapi-doc.html#/controller
[controller]: https://fdriesenaar.github.io/openapi-doc.html#/controller
[Creating Qiy Nodes for Individuals]: ../High-Level%20Architectural%20Overview.md#512-creating-qiy-nodes-for-individuals
[Data Reference Received-v2 Event]: #data-reference-received-v2-event
[Data Reference Received-v2 Callback]: #data-reference-received-v2-callback
[Data Reference Received-v2 Callback Endpoint]: #data-reference-received-v2-callback-endpoint
[Definitions Access Provider]: ../Definitions.md#access-provider
[Definitions API Key]: #app-authentication
[Definitions Application Provider]: ../Definitions.md#application-provider
[Definitions Connect Token]: ../Definitions.md#connect-token
[Definitions Connection]: ../Definitions.md#connection
[Definitions Data Provider]: ../Definitions.md#data-provider
[Definitions Individual]: ../Definitions.md#individual
[Definitions Relying Party]: ../Definitions.md#relying-party
[Definitions Resource]: ../Definitions.md#resource
[Definitions Service Catalogue]: ../Definitions.md#service-catalogue
[Definitions Service Access Endpoint]: ../Definitions.md#service-access-endpoint
[Definitions Service Endpoint]: ../Definitions.md#service-endpoint
[Definitions Service Provider]: ../Definitions.md#service-provider
[Definitions Service Type]: ../Definitions.md#service-type
[Definitions Transport Authentication]: ../Definitions.md#transport-authentication
[Definitions Qiy Node]: ../Definitions.md#qiy-node
[Definitions Qiy Node Client]: ../Definitions.md#qiy-node-client
[Definitions Qiy Node Credential]: #qiy-node-credential
[Definitions Qiy Node Implementation]: ../Definitions.md#qiy-node-implementation
[Definitions Qiy Application]: ../Definitions.md#qiy-application
[Definitions Qiy Scheme]: ../Definitions.md#qiy-scheme
[Definitions Qiy Trust Network]: ../Definitions.md#qiy-trust-network
[Delete Qiy Node]: #delete-qiy-node
[Delete Qiy Node request]: https://fdriesenaar.github.io/openapi-doc.html#/node/Delete_Qiy_Node
[DigitalMe]: https://digital-me.nl/
[Dynamic Endpoint Addresses]: #dynamic-endpoint-addresses
[Events]: #events
[Event Callback Endpoint]: #event-callback-endpoints
[Event Callback Endpoints]: #event-callback-endpoints
[Event Callbacks Endpoint]: #event-callbacks-endpoint
[Feed Request Callback]: #feed-request-callback
[Feed Request Callbacks]: #feed-request-callback
[Feeds]: https://fdriesenaar.github.io/openapi-doc.html#/feeds
[Feeds Endpoint]: #feeds-endpoint
[Get /api]: https://fdriesenaar.github.io/openapi.html
[Get action message]: #get-action-message
[Get action message request]: https://fdriesenaar.github.io/openapi-doc.html#/action_message/Get_action_message
[Get connect token]: #get-connect-token
[Get connect token request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Get_connect_token
[Get connection]: #get-connection
[Get connection request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Get_connection
[Get endpoint addresses]: #get-endpoint-addresses
[Get endpoint addresses request]: https://fdriesenaar.github.io/openapi-doc.html#/api/api
[Get event callback endpoints]: #get-event-callback-endpoints
[Get event callback endpoints request]: https://fdriesenaar.github.io/openapi-doc.html#/configuration/get_event_callback_endpoints
[Get node settings]: #get-node-settings
[Get node settings request]: https://fdriesenaar.github.io/openapi-doc.html#/node/Get_node_settings
[Get service catalogue]: #get-service-catalogue
[Get service catalogue request]: https://fdriesenaar.github.io/openapi-doc.html#/server/Get_service_catalogue
[Get user action message]: #get-user-action-message
[Getting help]: https://qiy.api.digital-me.nl/?version=latest#9acb0133-e012-4f49-a1e9-51283b8402c9
[List action messages]: #list-action-messages
[List action messages request]: https://fdriesenaar.github.io/openapi-doc.html#/action_message/List_action_messages
[List connect tokens]: #list-connect-tokens
[List connect tokens request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/List_connect_tokens
[List connections]: #list-connections
[List connections request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/List_connections
[List feeds]: #list-feeds
[List feeds request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/List_feeds
[List messages]: #list-messages
[List messages request]: https://fdriesenaar.github.io/openapi-doc.html#/message/List_messages
[Messages Endpoint]: #messages-endpoint
[Node Create Endpoint]: #node-create-endpoint
[Node Settings Endpoint]: #node-settings-endpoint
[POST /FeedsEndpoint/{feedId}]: https://fdriesenaar.github.io/openapi.html
[POST /ConnectionCreateEndpoint]: https://fdriesenaar.github.io/openapi.html
[Qiy Test Tool dm]: https://qiy-test-tool-dpyt.cloud.digital-me.nl/
[Qiy Test Tool pa]: https://qiytesttool.pythonanywhere.com/
[Register connect token]: #register-connect-token
[Register connect token request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Request_or_register_connect_token
[Request connect token]: #request-connect-token
[Request connect token request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Request_or_register_connect_token
[Request connection]: #request-connection
[Request connection request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Request_connection
[Request creation of Qiy Node]: #request-creation-of-qiy-node
[Request creation of Qiy Node request]: https://fdriesenaar.github.io/openapi-doc.html#/node/Request_creation_of_qiy-node
[Request for feed]: #request-for-feed
[Request for feed request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/Request_for_feed
[Request connection request]: https://fdriesenaar.github.io/openapi-doc.html#/connection/Request_connection
[Self Endpoint]: #self-endpoint
[Send message]: #send-message
[Send message request]: https://fdriesenaar.github.io/openapi-doc.html#/message/Send_message
[Server]: https://fdriesenaar.github.io/openapi-doc.html#/server
[Service Access Endpoint]: #service-access-endpoint
[Service Catalogue Endpoint]: #service-catalogue-endpoint
[Service Endpoint]: #service-endpoint
[Services]: https://qiy.api.digital-me.nl/?version=latest#ab572b83-bd18-4a8e-85be-b549a0ac6758
[Set feed source]: #set-feed-source
[Set feed source request]: https://fdriesenaar.github.io/openapi-doc.html#/feed/Set_feed_source
[Set service catalogue]: #set-service-catalogue
[Set service catalogue request]: https://fdriesenaar.github.io/openapi-doc.html#/service/Set_service_catalogue
[Set event callback endpoints]: #set-event-callback-endpoints
[Set event callback endpoints request]: https://fdriesenaar.github.io/openapi-doc.html#/configuration/set_event_callback_endpoints
[Set node settings]: #set-node-settings
[Set node settings request]: https://fdriesenaar.github.io/openapi-doc.html#/node/Set_node_settings
[Start listening to events]: #start-listening-to-events
[Start listening to events request]: https://fdriesenaar.github.io/openapi-doc.html#/controller/Start_listening_to_events
[State Handled Event]: #state-handled-event
[State Handled Callback]: #state-handled-callback
[State Handled Callback Endpoint]: #state-handled-callback-endpoint
[Subscriptions]: https://qiy.api.digital-me.nl/?version=latest#ec0ab04d-ab6e-4a9c-9b45-e6b75b583bff
[Transport Layer]: ../High-Level%20Architectural%20Overview.md#8-the-transport-layer
[User Action Message Event]: #user-action-message-event
[User Action Message Events]: #user-action-message-event
