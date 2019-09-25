# Qiy Node API

This document describes the Qiy Node API - the API for [Qiy Nodes][Definitions Qiy Node], in layman's terms: a digital identity for [Individuals][Definitions Individual] and/or [Service Providers][Definitions Service Provider] to provide and/or consume digital services.

In technical terms a Qiy Node provides a point of access for the [Qiy Trust Network][Definitions Qiy Trust Network] that can be used to allows individuals to provide [Relying Parties][Definitions Relying Party] access to [Resources][Definitions Resource] protected by [Data Providers][Definitions Data Provider], for example using [POST /FeedsEndpoint/{feedId}].

Individuals acquire Qiy Nodes [when they use Qiy-based end-user applications][hlao 5.1.2 Creating Qiy Nodes for Individuals].

Service Providers are provided with at least three Qiy Nodes by their [Access Provider][Definitions Access Provider]; one for the production environment, one for the acceptance environment and one for the development environment.

Software developers use the api to build [Qiy Node Clients][Definitions Qiy Node Client] (as provided interface) or [Qiy Node Implementations][Definitions Qiy Node Implementation] (as requirement for implementation).


# Servers

The api is provided in a development environment, the acceptance environment and the production environment.
In addition, a proxy server for the develoment environment is provided to ease discovery, experimentation, and evaluation.

The server urls are:

| Server Name      | Server url                                                          |
| ---------------- | ------------------------------------------------------------------- |
| Proxy            | https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/proxy |
| Dev2             | https://dev2-user.testonly.digital-me.nl/user                       |
| Acceptance       | https://user.dolden.net/user                                        |


The server url of the Production environment is provided in the entry-transition phase, when a [Qiy Application] goes live.

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


# API

## Api info

An [app authenticated][API Basics Authentication App Authentication] [GET /api][API Get Api] can be used to get the [api version][API Basics Versions] and the current address of the [Node Create Endpoint][API Basics Dynamic Endpoint Addresses Node Create Endpoint].

# Nodes

## Request creation of Qiy Node

This [Node Create Endpoint](#node-create-endpoint)-call can be used to [request the creation of a Qiy Node][Nodes Request creation of Qiy Node].


## Get endpoint addresses

A [user authenticated][API Basics Authentication User Authentication] [GET /api][API Get Api] can be used to get the [current addresses of the dynamic path endpoints][API Basics Dynamic Endpoint Addresses].


## Set event callback endpoints

This [Event Callbacks Endpoint](#event-callbacks-endpoint)-request can be used to [define the addresses of the event callback endpoints][Nodes Set event callback endpoints].


## Get event callback endpoints

This [Event Callbacks Endpoint](#event-callbacks-endpoint)-request can be used to [get the addresses of the event callback endpoints][Nodes Get event callback endpoints].


## Start listening to events

This [Events Endpoint](#events-endpoint)-call can be used to [start listening][Nodes Start listening to events] to [Qiy Node events](#events).

It starts a long-living session with a heartbeat to keep the session open. 
Every 10 seconds a line with the text ':ping' will be sent. If this is not received for more than that time, something has gone wrong.

The [Qiy Test Tool][Qiy Test Tool] can be used to monitor the events of a Qiy Node using the 'qiy_nodes/<node_name>/events'-path, see for example [https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/events](https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/events).

## Get node settings

This Node Settings Endpoint-call returns the node settings.


## Set node settings

This Node Settings Endpoint-call sets the node settings.


## Delete Qiy Node

This Self Endpoint-call can be used to delete a Qiy Node.


# Services

## Get service catalogue

This Service Catalogue Endpoint-call gets the Service Catalogue.


## Set service catalogue

This Service Catalogue Endpoint-call sets the Service Catalogue including the uri and the method of Service Endpoints.


# Connections

## Relying Party/Data Provider

### Request connect token

This Connect Token Create Endpoint-call can be used to request a connect token: a json object with the members 'identifier', 'tmpSecret' and 'target'. When the call was succesfull, a 200-OK will be returned with the Connect Token Url in the Location header of the response.


### Register connect token

This Connect Token Create Endpoint-call registers a connect token: a json object with the members 'identifier', 'tmpSecret' and 'target'. The call returns the Connect Token Url in the Location header of the response.


### State Handled Callback

This callback on the [State Handled Callback Endpoint][API Basics Documentation Service Provider Setup Endpoints State Handled Endpoint] can be used to detect a new connection.


## Individual

### Request connection

This asynchronous Connection Create Endpoint-call can be used to request a connection using a Connect Token: a json object with the members 'identifier', 'tmpSecret' and 'target'.

The creation of the connection can be followed using events, for details see /API Basics/Documentation/Qiy Node Client/Connections:

If and when the connection has been established, at least two State Handled Events will be fired; one for the Qiy Node Client that requested the connection and one for the Qiy Node Client that requested or registered the Connect Token. The event will also be fired for any other Qiy Node Client that is connected to one of the involved Qiy Nodes. Also, two State Handled Callbacks will be fired for the Qiy Nodes, but only if the State Handled Callback Endpoint has been set, see Set event callback endpoints.

Alternatively, the list of connections can be gotten. Here a connection should be present with the 'activeFrom' property should have the value of the current time (in milliseconds from the epoch), 'pid' should be a Base 64 encoded value, 'state' should be 'connected'.


### Connected to Router Event

The Connected to Router Event can be used to monitor the creation of a connection.


### Persistent Id Event

The Persistent Id Event is an event that is created upon creation of a connection.


### State Handled Event

This event is fired when a connection has been created.


## Get connection

This Connection Endpoint-call returns connection details.


## Get connect token

This call returns the details of a Connect Token.


## List connect tokens

This Connect Token List Endpoint-call lists the connect tokens.


## List connections

This Connections List Endpoint-call can be used to list connections.


# Messages

## Send message

This Mailbox Endpoint-call can be used to send a message over a connection with another Qiy User.


## List messages

This Mailbox Endpoint-call lists messages.


# Feeds

## Relying Party

### Request for feed

A Relying Party uses this Connection Feeds Endpoint-call to request for a feed.

Optionally, a Feed Request Callback body parameter can be included in the 'input'-member of the body json object as a base64-encoded byte array.


A Relying Party can use this Data Reference Received-v2-callback on the Data Reference Received-v2 Endpoint to receive new feed id's.

A Relying Party can use the [Data Reference Received Event-v2][API Basics Events Data Reference Received Event-v2] to detect a new feed.

### Access feed

A Relying Party uses this Feeds Endpoint-call to access a single feed.

The body may include operation request parameters encoded as a base-64 encoded byte array as described in the Qiy Scheme change proposal on free parameters.


### Access feeds

A Relying Party can use this Feeds Endpoint-call to access one or more feeds.


### List feeds

This Feeds Endpoint-request can be used to list the feed's of a Qiy Node or of a connection for all or a set of protocols (operation types), see [List feeds request].


## Data Provider

### Feed Request Callback

A Data Provider receives this Service Endpoint-callback when an Individual has set him as the source of a feed.


### Access feed callback

A Data Provider receives this Service Endpoint-callback after an access feed-request.


## Individual

### User Action Message Event

An End User App can use the User Action Message Event to detect the receipt of a feed request.


### Get user action message

A Qiy Node Client can use this call to get the details of a received message that requires user interaction using a userActionMessageUrl extracted from a User Action Message Event.


### Set feed

An End User App uses this call to set a Data Provider as the source for a feed request.


### Add feed

An End User App uses this call to add a Data Provider as a source for a feed request.


# Annex A Dynamic Endpoint Addresses

This annex describes the Dynamic Endpoint Addresses

## Action Messages List Endpoint

This endpoint can be used for [List action messages]. The current address of the endpoint is returned in the "amList"-member of the response of [Get endpoint addresses].

## Connect Token Create Endpoint

This endpoint can be used to [request][Request connect token] or [register][Register connect token] [Connect Tokens][Definitions Connect Token]. The current address of the endpoint is returned in the "ctCreate"-member of the response of Get endpoint addresses.

## Connect Token List Endpoint

This endpoint can be used for [List connect tokens]. The current address of the endpoint is returned in the "ctList"-member of the response of [Get endpoint addresses].

## Connection Create Endpoint

This endpoint can be used for [Request connection]. The current address of the endpoint is returned in the "scan"-member of the response of [Get endpoint addresses].

## Connection Endpoint

This endpoint can be used for [Get connection]. The endpoint urls are returned by [Request connection] and [List connections].

## Connection Feeds Endpoint

This endpoint can be used by a Relying Party to request an Individual for a feed to access a protected resource, see [Request for feed].

The current address of the endpoint is returned in a "feeds"-endpoint of a connection, see [Get connection] or [List connections].

## Connections List Endpoint

This endpoint can be used for [List connections]. The current address of the endpoint is returned in the "connections"-member of the response of [Get endpoint addresses].

## Events Endpoint

This endpoint can be used for [Start listening to events]. The current address of the endpoint is returned in the "events"-member of the response of [Get endpoint addresses].

## Event Callbacks Endpoint

This endpoint can be used to [set][Set event callback endpoints] or [get][Get event callback endpoints] the addresses of the Event Callback Endpoints.
The current addresses of the Event Callbacks Endpoint is returned in the "eventCallbacks"-member of the response of [Get endpoint addresses].

## Feeds Endpoint

A Relying Party uses this endpoint to [list][List feeds] or [access one][Access feed] or [more][Access feeds] feeds of an Individual (connection) or of himself (a Qiy Node).

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

This server-sent event is fired when a Request for feed fails.

## Data Reference Received-v2 Event

This server-sent event is generated by a Qiy Node of a Relying Party when it has received a new feed.

## Data Request Forwarded Event

This server-sent event is fired when a feed is being accessed.

## Data Request Fulfilled Event

This server-sent event is fired when a feed has been accessed succesfully.

## Data Request Failure Event

This server-sent event is fired when a feed could not be accessed succesfully.

## Data Request Not Forwarded Event

This server-sent event is fired when and if a feed cannot be accessed.

## Pending Peer Data Reference Event

This server-sent event can be fired when a feed is being accessed.

## Unexpected Data Reference Event

This server-sent event can be fired when a feed is being accessed.

## Persistent Id Event

This event can be used to monitor the creation of a connection.

## Routing Failure Event

This event is fired after a request for a connection and signals that a connection could not be established.

## Shared Secret Received Event

This event is fired after a request for a connection upon creating connection.

## Shared Secret Sent Event

This event is fired after a request for a connection upon creating connection.

## State Handled Event

This event is fired when a connection has been created, see GET State Handled Event for an example.

## User Action Message Event

This event is fired by a Qiy Node when it receives a message that requires interaction with the End User, and can be used by an End User application to detect that a feed request has been received.

Example event

```
event: USER_ACTION_MESSAGE data: {
   'type': 'USER_ACTION_MESSAGE',
   'connectionUrl': 'https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e',
   'extraData': 'https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4'
}
```


[Access feed]: #access-feed
[Access feed request]: http://127.0.0.1:8000/openapi-doc.html#/feed/Access_feed
[Access feeds]: #access-feeds
[Access feeds request]: http://127.0.0.1:8000/openapi-doc.html#/feed/Access_feeds
[Annex A Dynamic Endpoint Addresses]: #annex-a-dynamic-endpoint-addresses
[Annex B Events]: #annex-b-events
[API Basics]: https://qiy.api.digital-me.nl/?version=latest#a5c62ac8-8f2c-4d57-b970-42ff89253670
[API Basics Registration]: https://qiy.api.digital-me.nl/?version=latest#699276ef-e0b7-4ff8-852d-a5b2e175b4e3
[API Basics Service Desk]: https://qiy.api.digital-me.nl/?version=latest#9060bf32-11d2-4736-add3-629b52491c70
[API Basics Versions]: #versions
[API Basics Authentication]: #authentication
[API Basics Authentication App Authentication]: #app-authentication
[API Basics Authentication User Authentication]: #user-authentication
[API Basics Authentication Transport Authentication]: #transport-authentication
[API Basics Dynamic Endpoint Addresses]: #dynamic-endpoint-addresses
[API Basics Dynamic Endpoint Addresses Action Messages List Endpoint]: #action-messages-list-endpoint
[API Basics Dynamic Endpoint Addresses Connect Token Create Endpoint]: #connect-token-create-endpoint
[API Basics Dynamic Endpoint Addresses Connect Token List Endpoint]: #connect-token-list-endpoint
[API Basics Dynamic Endpoint Addresses Connection Create Endpoint]: #connection-create-endpoint
[API Basics Dynamic Endpoint Addresses Connection Endpoint]: #connection-endpoint
[API Basics Dynamic Endpoint Addresses Connection Feeds Endpoint]: #connection-feeds-endpoint
[API Basics Dynamic Endpoint Addresses Connections List Endpoint]: #connections-list-endpoint
[API Basics Dynamic Endpoint Addresses Events Endpoint]: #events-endpoint
[API Basics Dynamic Endpoint Addresses Event Callbacks Endpoint]: #event-callbacks-endpoint
[API Basics Dynamic Endpoint Addresses Feeds Endpoint]: #feeds-endpoint
[API Basics Dynamic Endpoint Addresses Mailbox Endpoint]: #mailbox-endpoint
[API Basics Dynamic Endpoint Addresses Node Create Endpoint]: #node-create-endpoint
[API Basics Dynamic Endpoint Addresses Node Settings Endpoint]: #node-settings-endpoint
[API Basics Dynamic Endpoint Addresses Reference Endpoint]: #reference-endpoint
[API Basics Dynamic Endpoint Addresses References Endpoint]: #references-endpoint
[API Basics Dynamic Endpoint Addresses Self Endpoint]: #self-endpoint
[API Basics Dynamic Endpoint Addresses Service Catalogue Endpoint]: #service-catalogue-endpoint
[API Basics Servers]: #servers
[API Basics Servers Mock Server]: https://qiy.api.digital-me.nl/?version=latest#fd504a4c-7781-413d-8968-d1c1f788f063
[API Basics Events]: https://qiy.api.digital-me.nl/?version=latest#ecbb4a43-d2a8-47bb-8f04-dd2afaa835a7
[API Basics Events Connected to Router Event]: https://qiy.api.digital-me.nl/?version=latest#d8724e2f-00cc-4af1-9408-01b1aaf91ed5
[API Basics Events Connected to Router Failed Event]: https://qiy.api.digital-me.nl/?version=latest#e88698cb-4dc5-42c1-b058-7fbba0760203
[API Basics Events Data Reference Failure Event]: https://qiy.api.digital-me.nl/?version=latest#5d7d300b-60ed-4712-9f79-ddd77b964462
[API Basics Events Data Reference Received-v2 Event]: https://qiy.api.digital-me.nl/?version=latest#dfc3e6e2-f328-4544-981d-21d40ede9bca
[API Basics Events Data Request Forwarded Event]: https://qiy.api.digital-me.nl/?version=latest#371747bf-ca06-47e0-9f91-8550934a37fd
[API Basics Events Data Request Fulfilled Event]: https://qiy.api.digital-me.nl/?version=latest#3e840f08-e911-4921-a010-3f06d9dd22e4
[API Basics Events Data Request Failure Event]: https://qiy.api.digital-me.nl/?version=latest#b4f28c11-3e1d-4aeb-b9a9-5d61cd7bc476
[API Basics Events Data Request Not Forwarded Event]: https://qiy.api.digital-me.nl/?version=latest#fa3f006c-130d-401f-ac27-3c919f54bb01
[API Basics Events Pending Peer Data Reference Event]: https://qiy.api.digital-me.nl/?version=latest#dbf4f11b-7d40-4451-8fa6-b7a3e3c63d61
[API Basics Events Unexpected Data Reference Event]: https://qiy.api.digital-me.nl/?version=latest#fac3b016-dc57-4b54-b1f6-3b5522ac6354
[API Basics Events Persistent Id Event]: https://qiy.api.digital-me.nl/?version=latest#1b178fe0-6ab5-4a75-892d-8d1fc34bdb84
[API Basics Events Routing Failure Event]: https://qiy.api.digital-me.nl/?version=latest#ec2f9731-b6a1-4c1a-81af-37e4c3c167f4
[API Basics Events Shared Secret Received Event]: https://qiy.api.digital-me.nl/?version=latest#71b0b918-1351-4d58-9669-e762adbf2d7a
[API Basics Events Shared Secret Sent Event]: https://qiy.api.digital-me.nl/?version=latest#85e76326-9a63-4f15-bc50-391f4d12313a
[API Basics Events State Handled Event]: https://qiy.api.digital-me.nl/?version=latest#14fa0afe-c913-4553-bd65-4bd387937b9a
[API Basics Events User Action Message Event]: https://qiy.api.digital-me.nl/?version=latest#a111e666-c46a-4747-9d42-26048ae06863
[API Basics Documentation]: https://qiy.api.digital-me.nl/?version=latest#0c70eba9-67e2-4757-acbe-956fd011c3d9
[API Basics Documentation Qiy Scheme]: https://qiy.api.digital-me.nl/?version=latest#aa085ade-104b-4d3a-ad9f-eb6078a698e7
[API Basics Documentation Qiy Scheme Qiy Trust Network]: https://qiy.api.digital-me.nl/?version=latest#2056c146-b848-4abc-a01c-fe96b13e6263
[API Basics Documentation Qiy Scheme Qiy Trust Network Access Provider]: https://qiy.api.digital-me.nl/?version=latest#f61281c8-b3cc-4ccf-9ade-03ad70d02f1d
[API Basics Documentation Qiy Scheme Qiy Trust Network Application Provider]: https://qiy.api.digital-me.nl/?version=latest#2e64cb8d-81d6-4cee-9dae-206698d8165f
[API Basics Documentation Qiy Scheme Qiy User]: https://qiy.api.digital-me.nl/?version=latest#77c0a106-20c1-4f94-a4a7-4f8a414ea90e
[API Basics Documentation Qiy Scheme Qiy User Individual]: https://qiy.api.digital-me.nl/?version=latest#df6d36d5-92b1-4478-a00e-141d2e75d9d8
[API Basics Documentation Qiy Scheme Qiy User Service Provider]: https://qiy.api.digital-me.nl/?version=latest#3792d188-f50e-4354-b22d-fc1baed73ea4
[API Basics Documentation Qiy Scheme Qiy User Service Provider Relying Party]: https://qiy.api.digital-me.nl/?version=latest#5a6bf7c4-3458-4e9d-852a-f9602d758d7a
[API Basics Documentation Qiy Scheme Qiy User Service Provider Data Provider]: https://qiy.api.digital-me.nl/?version=latest#b1ef5038-3e0b-46de-a2f7-fb1d827d1cea
[API Basics Documentation End User App]: https://qiy.api.digital-me.nl/?version=latest#157485cd-667a-431d-8bc0-d1b305462da9
[API Basics Documentation End User App Setup]: https://qiy.api.digital-me.nl/?version=latest#ea34f3a8-21c4-43e8-909e-9d9cfbfea7d9
[API Basics Documentation End User App Subscribe]: https://qiy.api.digital-me.nl/?version=latest#46388a12-cbb4-4436-81d1-7fe03d56ecc4
[API Basics Documentation End User App Orchestrate]: https://qiy.api.digital-me.nl/?version=latest#20dd0dbb-ab28-4f61-b2eb-82f24f5bfab1
[API Basics Documentation Service Provider]: https://qiy.api.digital-me.nl/?version=latest#0b4a0cd4-b250-4946-a4ed-cf73335c00a0
[API Basics Documentation Service Provider Setup]: https://qiy.api.digital-me.nl/?version=latest#17709317-2d9c-42e0-ba13-26e90c17b9c5
[API Basics Documentation Service Provider Setup Service Catalogue]: https://qiy.api.digital-me.nl/?version=latest#4396d190-ef54-41c5-82ac-081d49e09ad8
[API Basics Documentation Service Provider Setup Endpoints]: https://qiy.api.digital-me.nl/?version=latest#d381fd7a-eebc-411f-bcce-a6a8ec2e0b8c
[API Basics Documentation Service Provider Setup Endpoints Service Endpoint]: https://qiy.api.digital-me.nl/?version=latest#a7dc0161-80ea-42c4-96d3-16b50dfb1163
[API Basics Documentation Service Provider Setup Endpoints Event Callback Endpoints]: https://qiy.api.digital-me.nl/?version=latest#37435aca-83d4-4184-94de-a953ef46d282
[API Basics Documentation Service Provider Setup Endpoints Event Callback Endpoints State Handled Endpoint]: https://qiy.api.digital-me.nl/?version=latest#37435aca-83d4-4184-94de-a953ef46d282
[API Basics Documentation Service Provider Setup Endpoints Event Callback Endpoints Data Reference Received-v2 Endpoint]: https://qiy.api.digital-me.nl/?version=latest#37435aca-83d4-4184-94de-a953ef46d282
[API Basics Documentation Qiy Node Client]: https://qiy.api.digital-me.nl/?version=latest#37435aca-83d4-4184-94de-a953ef46d282
[API Basics Documentation Qiy Node Client Qiy Node]: https://qiy.api.digital-me.nl/?version=latest#3c5dc895-11b2-4a05-a22a-45a38a31378b
[API Basics Documentation Qiy Node Client Qiy Node Settings]: https://qiy.api.digital-me.nl/?version=latest#37435aca-83d4-4184-94de-a953ef46d282
[API Basics Documentation Qiy Node Client Qiy Node Qiy Node Credential]: https://qiy.api.digital-me.nl/?version=latest#d7e4a275-f661-4b68-97d0-10cd30f483e6
[API Basics Documentation Qiy Node Client Connections]: https://qiy.api.digital-me.nl/?version=latest#14cee758-ed05-4ade-abf8-241eec772976
[API Basics Documentation Qiy Node Client Connect Tokens]: https://qiy.api.digital-me.nl/?version=latest#b4a02618-81bd-4600-b2f6-b87a14e4189b
[API Basics Documentation Qiy Node Client Connect Tokens Create Connect Token]: https://qiy.api.digital-me.nl/?version=latest#b18ab891-66e6-418c-b92d-d2349c9c1fa7
[API Basics Documentation Qiy Node Client Connect Tokens Online Connect Token]: https://qiy.api.digital-me.nl/?version=latest#067148f5-0d2e-4869-a814-ac1732828e3b
[API Basics Documentation Qiy Node Client Connect Tokens Offline Connect Token]:https://qiy.api.digital-me.nl/?version=latest#92d2d504-4e2c-4244-8960-3bebd90b8e90 
[API Basics Documentation Qiy Node Client Connect Tokens On-Connected Actions]: https://qiy.api.digital-me.nl/?version=latest#d47b630f-2c37-45eb-a91f-d82794b08811
[API Basics Documentation Qiy Node Client Feeds]: https://qiy.api.digital-me.nl/?version=latest#bed9f049-8da6-495f-84b9-ccc44e29e0a5
[API Basics Documentation Qiy Node Client Events]: https://qiy.api.digital-me.nl/?version=latest#4978ab24-b193-40c1-858f-58622673d13b
[API Basics Documentation Qiy Node Client Messages]: https://qiy.api.digital-me.nl/?version=latest#d128578f-2fb7-41ec-b777-da7f2341d274
[API]: https://qiy.api.digital-me.nl/?version=latest#076c9660-4323-42f1-b087-6cad8e484c3a
[API Get Api]: https://qiy.api.digital-me.nl/?version=latest#27416893-7da4-411f-8847-88103d17dc86
[Connections]: https://qiy.api.digital-me.nl/?version=latest#466096f2-591f-4ee9-af4e-a7c68ceb6571
[Connections Relying Party/Data Provider]: https://qiy.api.digital-me.nl/?version=latest#a97bc6a5-4612-4fb9-b4e7-5dbb243c26e6
[Connections Relying Party/Data Provider Request connect token]: https://qiy.api.digital-me.nl/?version=latest#aeca4ebb-74b7-4fc5-8980-ca8079f4a733
[Connections Relying Party/Data Provider Register connect token]: https://qiy.api.digital-me.nl/?version=latest#715a0d40-b856-4a7a-8471-e1e11a285043
[Connections Relying Party/Data Provider State Handled Callback]: https://qiy.api.digital-me.nl/?version=latest#5faa39a4-6151-403b-8d2d-8f3844d42f34
[Connections Individual]: https://qiy.api.digital-me.nl/?version=latest#ff280da1-0704-4a83-ab50-78b1ea73ed0a
[Connections Individual Request connection]: https://qiy.api.digital-me.nl/?version=latest#0c7c8ee9-1818-4837-860c-8485af7c3754
[Connections Individual Connected to Router Event]: https://qiy.api.digital-me.nl/?version=latest#f8536243-7457-455f-8f94-f1d135cf514e
[Connections Individual Persistent Id Event]: https://qiy.api.digital-me.nl/?version=latest#e8a176a8-e89e-42cf-bac4-e70e45cba62d
[Connections Individual State Handled Event]: https://qiy.api.digital-me.nl/?version=latest#c8295ab7-a7a8-4378-8f0d-274cbe7153e1
[Connections Get connection]: https://qiy.api.digital-me.nl/?version=latest#71d55402-d235-4df6-bdcc-2a17b66b8449
[Connections Get connect token]: https://qiy.api.digital-me.nl/?version=latest#c8b4b003-e8ec-4fb2-bafa-f37f0c4d2925
[Connections List connect tokens]: https://qiy.api.digital-me.nl/?version=latest#669c1d26-94fa-460b-a2ad-e899ccb91d2b
[Connections List connections]: https://qiy.api.digital-me.nl/?version=latest#1ddd2cbf-5a25-422f-a650-28f551dce88c
[Consents]: https://qiy.api.digital-me.nl/?version=latest#3f42e884-3ffa-4387-8896-05e7226d5a9f
[Definitions Access Provider]: ../Definitions.md#access-provider
[Definitions API Key]: #app-authentication
[Definitions Application Provider]: ../Definitions.md#application-provider
[Definitions Connect Token]: ../Definitions.md#connect-token
[Definitions Data Provider]: ../Definitions.md#data-provider
[Definitions Individual]: ../Definitions.md#individual
[Definitions Relying Party]: ../Definitions.md#relying-party
[Definitions Resource]: ../Definitions.md#resource
[Definitions Service Catalogue]: ../Definitions.md#service-catalogue
[Definitions Service Provider]: ../Definitions.md#service-provider
[Definitions Transport Authentication]: ../Definitions.md#transport-authentication
[Definitions Qiy Node]: ../Definitions.md#qiy-node
[Definitions Qiy Node Client]: ../Definitions.md#qiy-node-client
[Definitions Qiy Node Credential]: #qiy-node-credential
[Definitions Qiy Node Implementation]: ../Definitions.md#qiy-node-implementation
[Definitions Qiy Application]: ../Definitions.md#qiy-application
[Definitions Qiy Scheme]: ../Definitions.md#qiy-scheme
[Definitions Qiy Trust Network]: ../Definitions.md#qiy-trust-network
[Delete Qiy Node]: #delete-qiy-node
[Delete Qiy Node request]: http://127.0.0.1:8000/openapi-doc.html#/lifecycle/Delete_Qiy_Node
[DigitalMe]: https://digital-me.nl/
[Feeds]: https://qiy.api.digital-me.nl/?version=latest#acd5667e-984f-4c24-b065-09a233fc876f
[Feeds Relying Party]: https://qiy.api.digital-me.nl/?version=latest#946ef50b-e186-444c-a2a8-243597a81987
[Feeds Relying Party fiKks]: https://qiy.api.digital-me.nl/?version=latest#3811d8af-3dce-421e-8d3e-cf38963ad1c6
[Feeds Relying Party fiKks Access feed - fikks - encrypted]: https://qiy.api.digital-me.nl/?version=latest#824e400f-a8f2-4493-8aee-bbdbeed6be7a
[Feeds Relying Party fiKks Access feed - fikks - not encrypted]: https://qiy.api.digital-me.nl/?version=latest#079824bd-f173-4429-b092-61036694e4e8
[Feeds Relying Party Request for feed]: https://qiy.api.digital-me.nl/?version=latest#1d4a8c44-2ac7-4910-a1bd-8f8e3c760eff
[Feeds Relying Party Data Reference Received-v2 Callback]: https://qiy.api.digital-me.nl/?version=latest#b43825af-0a03-494e-a1f3-1d2f4a1c6d78
[Feeds Relying Party Data Reference Received-v2 Event]: https://qiy.api.digital-me.nl/?version=latest#ee14f78b-3f21-4e69-b824-03819a70dddb
[Feeds Relying Party Access feed]: https://qiy.api.digital-me.nl/?version=latest#c6b99339-789f-4867-9a72-203f3605de30
[Feeds Relying Party Access feeds]: https://qiy.api.digital-me.nl/?version=latest#cdba9430-3f07-4926-bdec-7fd244e3f44e
[Feeds Relying Party List feed ids]: https://qiy.api.digital-me.nl/?version=latest#80ed2172-944c-4a07-8b06-ccdfbada32bb
[Feeds Data Provider]: https://qiy.api.digital-me.nl/?version=latest#ef99bb75-5d6c-4e6e-afd7-6a81f6f5e802
[Feeds Data Provider Feed Request Callback]: https://qiy.api.digital-me.nl/?version=latest#e9332b0f-de0b-472d-82fd-7fcf36335c39
[Feeds Data Provider Access feed callback]: https://qiy.api.digital-me.nl/?version=latest#58021703-b84e-43ec-8fe8-0408503c42d8
[Feeds Individual]: https://qiy.api.digital-me.nl/?version=latest#d6ad7f53-7e6f-4e11-8273-b45469039e3c
[Feeds Individual User Action Message Event]: https://qiy.api.digital-me.nl/?version=latest#f693e165-1484-4f72-8e1f-9dff7ab13b25
[Feeds Individual Get user action message]: https://qiy.api.digital-me.nl/?version=latest#122a0a4b-f6fc-4180-b970-d07db11667c9
[Feeds Individual Set feed]: https://qiy.api.digital-me.nl/?version=latest#00faf2fd-c7c7-4d5d-b4d8-19f7a8cc55b1
[Feeds Individual Add feed]: https://qiy.api.digital-me.nl/?version=latest#d628b6d5-057f-4ce9-9a01-2c13e785cda0
[Get /api]: https://127.0.0.1:8000/openapi.html
[Get connection]: #get-connection
[Get connection request]: http://127.0.0.1:8000/openapi-doc.html#/connection/Get_connection
[Get endpoint addresses]: #get-endpoint-addresses
[Get endpoint addresses request]: http://127.0.0.1:8000/openapi-doc.html#/api/api
[Get event callback endpoints]: #get-event-callback-endpoints
[Get event callback endpoints request]: http://127.0.0.1:8000/openapi-doc.html#/node/get_event_callback_endpoints
[Get node settings]: #get-node-settings
[Get node settings request]: http://127.0.0.1:8000/openapi-doc.html#/node/Get_node_settings
[Get service catalogue]: #get-service-catalogue
[Get service catalogue request]: http://127.0.0.1:8000/openapi-doc.html#/service/Get_service_catalogue
[Getting help]: https://qiy.api.digital-me.nl/?version=latest#9acb0133-e012-4f49-a1e9-51283b8402c9
[hlao 5.1.2 Creating Qiy Nodes for Individuals]: ../High-Level%20Architectural%20Overview.md#512-creating-qiy-nodes-for-individuals
[List action messages]: #list-action-messages
[List action messages request]: http://127.0.0.1:8000/openapi-doc.html#/action_message/List_action_messages
[List connect tokens]: #list-connect-tokens
[List connect tokens request]: http://127.0.0.1:8000/openapi-doc.html#/connect_token/List_connect_tokens
[List connections]: #list-connections
[List connections request]: http://127.0.0.1:8000/openapi-doc.html#/connection/List_connections
[List feeds]: #list-feeds
[List feeds request]: http://127.0.0.1:8000/openapi-doc.html#/feed/List_feeds
[List messages]: #list-messages
[List messages request]: http://127.0.0.1:8000/openapi-doc.html#/message/List_messages
[Messages]: https://qiy.api.digital-me.nl/?version=latest#b0169810-fd5c-4422-95a1-0beb2fc77a3e
[Messages Send message]: https://qiy.api.digital-me.nl/?version=latest#a58badea-0b4c-4c85-8254-96bab05892fa
[Messages List messages]: https://qiy.api.digital-me.nl/?version=latest#45ada0ae-c416-4348-81b1-44f7b2a9e44f
[Nodes]: https://qiy.api.digital-me.nl/?version=latest#62279de6-0df7-497a-9a1e-cddc17bbbc63
[Nodes Request creation of Qiy Node]: https://qiy.api.digital-me.nl/?version=latest#806d07bb-f6eb-47f8-bc07-71119440fc0d
[Nodes Get endpoint addresses]: https://qiy.api.digital-me.nl/?version=latest#0bdb3ea3-0e8c-4f6d-8a92-8230d1be9a02
[Nodes Set event callback endpoints]: https://qiy.api.digital-me.nl/?version=latest#2887a3e0-5e5c-40ea-83b7-e40ce6cf5333
[Nodes Get event callback endpoints]: https://qiy.api.digital-me.nl/?version=latest#d0750a63-eee1-41ef-b093-ad0ef8c720e3
[Nodes Start listening to events]: https://qiy.api.digital-me.nl/?version=latest#abd171d1-4aee-4e8c-a599-00914f277d62
[Nodes Get node settings]: https://qiy.api.digital-me.nl/?version=latest#7bb9f259-c23d-4038-8cba-237671b167a7
[Nodes Set node settings]: https://qiy.api.digital-me.nl/?version=latest#07e66599-8dff-4ed4-9a9f-4773fb5515d7
[Nodes Delete Qiy Node]: https://qiy.api.digital-me.nl/?version=latest#5c60f3f0-ea95-40f7-9487-3664d9a4b293
[POST /FeedsEndpoint/{feedId}]: https://127.0.0.1:8000/openapi.html
[POST /ConnectionCreateEndpoint]: https://127.0.0.1:8000/openapi.html
[Qiy Test Tool dm]: https://qiy-test-tool-dpyt.cloud.digital-me.nl/
[Qiy Test Tool pa]: https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/proxy
[Register connect token]: #register-connect-token
[Register connect token request]: http://127.0.0.1:8000/openapi-doc.html#/connect_token/Request_or_register_connect_token
[Request connect token]: #request-connect-token
[Request connect token request]: http://127.0.0.1:8000/openapi-doc.html#/connect_token/Request_or_register_connect_token
[Request connection]: #request-connection
[Request connection request]: http://127.0.0.1:8000/openapi-doc.html#/connection/Request_connection
[Request creation of Qiy Node]: #request-creation-of-qiy-node
[Request creation of Qiy Node request]: http://127.0.0.1:8000/openapi-doc.html#/lifecycle/Request_creation_of_qiy-node
[Request for feed]: #request-for-feed
[Request for feed request]: http://127.0.0.1:8000/openapi-doc.html#/feed/Request_for_feed
[Relations]: https://qiy.api.digital-me.nl/?version=latest#4f4c5a3e-388c-48ff-b847-6c11c3738254
[Request connection request]: http://127.0.0.1:8000/openapi-doc.html#/connection/Request_connection
[Send message]: #send-message
[Send message request]: http://127.0.0.1:8000/openapi-doc.html#/message/Send_message
[Services]: https://qiy.api.digital-me.nl/?version=latest#ab572b83-bd18-4a8e-85be-b549a0ac6758
[Services Get service catalogue]: https://qiy.api.digital-me.nl/?version=latest#91f6b195-9c43-4c95-9618-57631714343b
[Services Set service catalogue]: https://qiy.api.digital-me.nl/?version=latest#d29ddd91-cdcf-48af-abe4-42cd6d54694b
[Set service catalogue]: #set-service-catalogue
[Set service catalogue request]: http://127.0.0.1:8000/openapi-doc.html#/service/Set_service_catalogue
[Set event callback endpoints]: #set-event-callback-endpoints
[Set event callback endpoints request]: http://127.0.0.1:8000/openapi-doc.html#/node/set_event_callback_endpoints
[Set node settings]: #set-node-settings
[Set node settings request]: http://127.0.0.1:8000/openapi-doc.html#/node/Set_node_settings
[Start listening to events]: #start-listening-to-events
[Start listening to events request]: http://127.0.0.1:8000/openapi-doc.html#/connect_token/Start_listening_to_events
[Subscriptions]: https://qiy.api.digital-me.nl/?version=latest#ec0ab04d-ab6e-4a9c-9b45-e6b75b583bff
[Transport Layer]: ../High-Level%20Architectural%20Overview.md#8-the-transport-layer

