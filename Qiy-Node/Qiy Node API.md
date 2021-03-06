# Qiy Node API

This document describes the Qiy Node API.

The Qiy Node API enables a client to access protected described resources of a server via a controller using feeds, see [Definition of Resource Access Management](../Definitions.md#resource-access-management). 

This can be used for example by a [Relying Party][Definitions Relying Party] to access [Personal Data][Definitions Personal Data] of an [Individual][Definitions Individual] from a [Data Provider][Definitions Data Provider] under control of the [Individual][Definitions Individual].

Software developers use the api for Qiy-based solutions (as provided interface) or [Qiy Node Implementations][Definitions Qiy Node Implementation] (as requirement for implementation).


# Qiy Node

A [Qiy Node][Definitions Qiy Node] can be viewed as a digital identity for [Individuals][Definitions Individual] and/or organizations ([Service Providers][Definitions Service Provider]).
Qiy Nodes can be used in solutions that enable Individuals to provide [Relying Parties][Definitions Relying Party] access to personal data that are protected by [Data Providers][Definitions Data Provider].

Individuals acquire Qiy Nodes when they start using Qiy-based end-user
applications, see [High-Level Architectural Overview 4.3 Qiy Node].

Service Providers are provided with at least three Qiy Nodes by their [Access Provider][Definitions Access Provider]; one for the production environment, one for the acceptance environment and one for the development environment.


# Resource Access Management

The Qiy Node API main feature is Resource Access Management;
it can be used by a [controller] (eg Individual) to provide a [client] (eg Relying Party) access to a [Described Resource][Definitions Described Resource] (to provide a [Service][Definitions Service]) from a [Service Endpoint] protected by the server (eg Data Provider) using [Feeds], for example using the following scenario:
* The server announces the available [Service][Definitions Service], see [Set service catalogue].
* The controller connects with the server, see [Request connection].
* The server identifies the controller (out of bounds).
* The controller connects with the client, see [Request connection].
* The client requests the controller for a feed, see [Request for feed].
* The controller receives the request via a [Request for feed event] or using [List requests for feed].
* The controller accepts the feed and sets the server as the source, see [Set feed source].
* The server receives a feed request and creates a feed, see [Server Request for Feed].
* The client uses the feed to access the service, see [Access feed].
* The server receives a [Service Request] and returns a response that is passed to the client.


# Servers

The api is provided in a development environment, the acceptance environment and the production environment.
In addition, a proxy server for the develoment environment is provided to ease discovery, experimentation, and evaluation.

The server urls are:

| Server Name      | Server url                                                                          |
| ---------------- | ----------------------------------------------------------------------------------- |
| Proxy            | [https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/proxy/v1][Proxy Url] |
| Dev2             | [https://dev2-user.testonly.digital-me.nl/user/v1][Dev2 Url]                        |
| Acceptance       | [https://user.dolden.net/user/v1][Acceptance Url]                                   |
| Production       | [https://user.digital-me.nl/user/v1][Production Url]                                |


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

The major version of the api must be included in the server url and the full version (MAJOR.MINOR.PATCH) that is supported must be returned by [Get /api].


# Authentication

## App Authentication

[Qiy Applications][Definitions Qiy Application] are required to authenticate requests but [GET /api] using an [API Key][Definitions API Key] implemented using basic authentication.

Two API Keys are provided by Access Providers: one for the Production environment and one for the other environments.
In production, the API Key must be updated periodically using rolling updates or immediately if it has or may have been compromised.
This should also be the case for the other environments.

## User Authentication

User Authentication ensures that a Qiy Node is only accessed by its rightfull owner.

Most requests must be user authenticated using a signed token that can only be calculated using a [Qiy Node Credential] as described below.
The token is passed in the 'Authorization-node-QTN'-header parameter, see for example [POST /FeedsEndpoint/{feedId}].

### Python

The authorization header parameter can be calculated with the package 'pyOpenSSL'. 
Using a pem-file with the primary key of the Qiy Node as generated with the code provided with [Qiy Node Credential] it can be generated as follows:

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

Some requests require [Transport Authentication][Definitions Transport Authentication] in order to access the [Transport Layer]. Authentication can be achieved by providing the [Transport Password] in the 'password'-header parameter, see for example [POST /ConnectionCreateEndpoint].


# Dynamic Endpoint Addresses

The Qiy Node Api uses [dynamic endpoint addresses][Annex A Dynamic Endpoint Addresses] most of which can be obtained using [Get endpoint addresses]. The addresses can be cached, but should be refreshed every day.


# Events

The Qiy Node API provides a number of [Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events)-events which can be catched with [Start listening to events](#start-listening-to-events), see [Annex B Events].


# Callbacks

The events can also be catched using callbacks. Also, the Qiy Node API provides some additional callbacks for servers, see [Annex C Callbacks].


# API

## Api info

An unauthorized [GET /api] can be used to get the api version and the current address of the [Node Create Endpoint].


# Nodes

## Request creation of Qiy Node

This [Node Create Endpoint]-call can be used to request the [creation of a Qiy Node][Creating Qiy Nodes for Individuals], see [Request creation of Qiy Node request].


## Get endpoint addresses

An app authenticated and user authenticated [GET /api] can be used to get the current [Endpoint Addresses][Dynamic Endpoint Addresses].


## Set event callback endpoints

This [Event Callbacks Endpoint]-request can be used to define the addresses of the [Event Callback Endpoints], see [Set event callback endpoints request].


## Get event callback endpoints

This [Event Callbacks Endpoint](#event-callbacks-endpoint)-request can be used to get the addresses of the event callback endpoints, see [Get event callback endpoints request].


## Start listening to events

After [connecting][Request connection] to servers and clients, controllers use this [Events Endpoint](#events-endpoint)-call to catch [requests for feed events][Request for feed event], see also [Start listening to events request].

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

Afterwards, [Server Request for Feed] and [Access Feed Callbacks] are received for these services.

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
    * target: The format of this member is returned in the "target-template"-member of the response of [Get endpoint addresses], where '~id~' should be a [uuid].
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

This [Connection]-call returns the details of a connection, see [Get connection request].


## Get connect token

This [Connect Token]-call returns the details of a [Connect Token][Definitions Connect Token], see [Get connect token request].


## List connect tokens

This [Connect Token List Endpoint]-call lists the connect tokens, see [List connect tokens request].


## List connections

This [Connection List Endpoint]-call can be used to list connections, see [List connections request].


# Messages

This chapter describes the [Message] requests.
Please refer to [Message] for the schema.

## Send message

This [Messages Endpoint]-call can be used to send a message to a connected Qiy Node, see [Send message request].


## List messages

This [Messages Endpoint]-call lists messages, see [List messages request].


# Feeds

This chapter describes the [Feed] requests.
Please refer to [Feed] for the schema.

## Client

### Request for feed

A client uses this [Connection Feeds Endpoint]-call to initiate a feed, see [Request for feed request].
Optionally, a body parameter can be included in the 'input'-member of the body json object as a base64-encoded byte array.

The request returns an inactive feed, the status of which can be monitored using [List feeds].
A [Data Reference Received-v2 Event] and a [Client Feed Request Callback] will be fired when the feed can be used or has been changed. 


### Access feed

A client uses this [Feeds Endpoint]-call to access a single feed, see [Access feed request].
The body may include operation request parameters encoded as a base-64 encoded byte array.


### Access feeds

A client uses this [Feeds Endpoint]-call to access one or more feeds, see [Access feeds request].


### List feeds

This [Feeds Endpoint]-request can be used to list the feeds of a Qiy Node or of a connection for all or a set of [Service Types][Definitions Service Type] (also known as 'protocols'), see [List feeds request].


## Server

A server receives a [Server Request for Feed] when a controller has set him as the source of a feed, see [Add feed source] or [Set feed source].

A server receives an [Access Feed Callback] after an [Access feed] or [Access feeds].

## Controller

### Request for feed event

An End User App receives this event when a connected client has requested for a feed, see [Controller request for feed event].
The event carries an [User Action Message Url][User Action Message] in the extraData property which is used in a [Get request for feed details] to get the details of the request. 

### Get request for feed details

The controller uses this request to get the details of a feed request, see [Get request for feed details request].

The request for feed contains two lists of [Action Urls][Action], one by pid and one by connection url, which can be used to set or add the respective Server as a feed source, see [Set feed source] and/or [Add feed source].

### List requests for feed

A controller uses this [User Action Message List Endpoint]-call to get all open requests for feeds, see [List requests for feed request].

### Set feed source

Controllers use [Set feed source request] to accept a request for feed and set a source for the feed.

### Add feed source

Controllers use [Add feed source request] to accept a request for feed and add a source to the feed.


# Annex A Dynamic Endpoint Addresses

This annex describes the Dynamic Endpoint Addresses

## User Action Message List Endpoint

This endpoint can be used to list [User Action Messages][User Action Message], currently used for [List requests for feed].
The current address of the endpoint is returned in the "amList"-member of the response of [Get endpoint addresses].

## Connect Token Create Endpoint

This endpoint can be used to [request][Request connect token] or [register][Register connect token] [Connect Tokens][Definitions Connect Token]. The current address of the endpoint is returned in the "ctCreate"-member of the response of Get endpoint addresses.

## Connect Token List Endpoint

This endpoint can be used for [List connect tokens]. The current address of the endpoint is returned in the "ctList"-member of the response of [Get endpoint addresses].

## Connection Create Endpoint

This endpoint can be used for [Request connection]. The current address of the endpoint is returned in the "scan"-member of the response of [Get endpoint addresses].

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

This endpoint can be used for [Delete Qiy Node]. The endpoint address is returned in the 'self'-property of [Get endpoint addresses].

## Service Endpoint

This endpoint is provided by a server to serve feeds, see [Server Request for Feed].
It can be read and set with [Set service catalogue] and [Get service catalogue] respectively.

Note: This endpoint have to be whitelisted by the Access Provider before it can be used.

## Service Access Endpoint

This endpoint is provided by a server to serve resources, see [Service Request].
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

This event is fired if and when a [User Action Message] is received, see for example [Request for feed event].

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

#### Client Feed Request Callback Endpoint

This [Event Callback Endpoint] can be used to receive a callback as an alternative for the [Data Reference Received-v2 Event].
It can be configured using [Set event callback endpoints].

#### State Handled Callback Endpoint

This [Event Callback Endpoint] can be used as an alternative for the [State Handled Event].
It can be configured using [Set event callback endpoints].

### Client Feed Request Callback

This [Client Feed Request Callback Endpoint]-callback is fired when a source is set for a feed, see [Client Feed Request Callback request], [Request for feed], [Set feed source] and [Add feed source].

The body of the callback carries the same load as the [Data Reference Received-v2 Event], see for example thess examples:

```
{
    "type": "DATA_REFERENCE_RECEIVED2",
    "connectionUrl": "https://qiy-test-tool-dpyt.cloud.digital-me.nl/qiy_nodes/qiy_node_api/proxy/v1/pid1sp1connectionUrl",
    "extraData": {
        "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
        "value": "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ=="
    }
}
```

```
{
    "type":"DATA_REFERENCE_RECEIVED2", 
    "connectionUrl":"https://dev2-user.testonly.digital-me.nl/user/connections/user/pt_usernode_fksH_de/d3b58af4-2883-4cef-b203-41e117549906", 
    "extraData":"BZWEKR63P2FEJZXYLGBN3XNWCBZU6FZG" 
}
```


### State Handled Callback

This [State Handled Callback Endpoint]-callback is executed when a Connect Token has been used to create a connection, see [Register connect token] or [Request connect token].


## Server Callbacks

### Server Request for Feed

A server receives this [Service Endpoint]-call when a controller has set him as the source of a feed, see [Server Request for Feed request]

#### Server Request for Feed Example

This python code-snippet can be used to simulate a Server Request for Feed:

```
import requests
url = 'https://qiy-test-tool-dpyt.cloud.digital-me.nl/qiy_nodes/qiy_node_api/proxy/v1/dp1serviceEndpointUrl'
payload = "{\r\n  \"connection\": \"https://dev1-user.testonly.digital-me.nl/user/connections/user/96cd5389-6def-4f6f-b3a9-b613a66ec522/ad4ac9cb-62e1-43ad-8495-9ac426b229c2\",\r\n  \"pid\": \"G5grIomOi7aBEV9nYE5Vlg==\",\r\n  \"message\": {\r\n    \"serialNr\": 6,\r\n    \"text\": \"Requesting 'test data'\",\r\n    \"protocol\": \"https://github.com/qiyfoundation/fiKks/tree/master/schema/v1\",\r\n    \"inbound\": true,\r\n    \"sent\": false,\r\n    \"thirdPartyRef\": \"4D0OqePJ1yKD41Q9qmixVnVFLWcJHFT1hhKDKG9FmeI=\"\r\n  },\r\n  \"mbox\": \"https://dev1-user.testonly.digital-me.nl/user/mbox/user/96cd5389-6def-4f6f-b3a9-b613a66ec522/ad4ac9cb-62e1-43ad-8495-9ac426b229c2\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)
```

The call could return the following body:

```
{
  "id": "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ=="
}
```

### Service Request

A server receives this [Service Access Endpoint]-callback after an [Access feed] or [Access feeds]; despite its name it can combine service requests for different feeds, see [Service Request request].

The body of the callback request may also contain access requests for more then one feed. 
Also, an optional input parameter may be passed with the feed access request in the 'input'-member encoded as a base65-encoded byte array.

```
{
	"SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==": {
		"input": "Im9wdGlvbmFsIGZlZWQgYWNjZXNzIHJlcXVlc3QgYm9keSBlbmNvZGVkIGFzIGEgYmFzZTY0IGVuY29kZWQgYnl0ZSBhcnJheSI="
	},
	"TkF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBQR==": {
		"input": "IkFub3RoZXIgb3B0aW9uYWwgZmVlZCBhY2Nlc3MgcmVxdWVzdCBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig=="
	}
}
```


#### Service Request Example

This python code-snippet can be used to simulate a Service Request:
```
import requests
url = 'https://qiy-test-tool-dpyt.cloud.digital-me.nl/qiy_nodes/qiy_node_api/proxy/v1/dp1serviceEndpointUrl/resolve'
payload = """{
	"SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==": {
		"input": "Im9wdGlvbmFsIGZlZWQgYWNjZXNzIHJlcXVlc3QgYm9keSBlbmNvZGVkIGFzIGEgYmFzZTY0IGVuY29kZWQgYnl0ZSBhcnJheSI="
	},
	"TkF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBQR==": {
		"input": "IkFub3RoZXIgb3B0aW9uYWwgZmVlZCBhY2Nlc3MgcmVxdWVzdCBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig=="
	}
}
"""
headers = {
  'Content-Type': 'application/json'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)
```

The call could return the following body:

```
{
                    "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==": {
                        "output": "ewogICAgIlNqRjFSRkJOYW0xNFJteEVjVzhyT1Zkek5rcEhkMVJaYUZkQlBRPT0iOiB7CiAgICAgICAgIm91dHB1dCI6ICJ7CiAgICAiYWN0aXZpdGllcy1oZWFydCI6IFsKICAgICAgICB7CiAgICAgICAgICAgICJjdXN0b21IZWFydFJhdGVab25lcyI6IFtdLAogICAgICAgICAgICAiZGF0ZVRpbWUiOiAidG9kYXkiLAogICAgICAgICAgICAiaGVhcnRSYXRlWm9uZXMiOiBbCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImNhbG9yaWVzT3V0IjogMTM4LjgzNTEsCiAgICAgICAgICAgICAgICAgICAgIm1heCI6IDg2LAogICAgICAgICAgICAgICAgICAgICJtaW4iOiAzMCwKICAgICAgICAgICAgICAgICAgICAibWludXRlcyI6IDY1LAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIk91dCBvZiBSYW5nZSIKICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImNhbG9yaWVzT3V0IjogMzA5Ljk2ODI0LAogICAgICAgICAgICAgICAgICAgICJtYXgiOiAxMjAsCiAgICAgICAgICAgICAgICAgICAgIm1pbiI6IDg2LAogICAgICAgICAgICAgICAgICAgICJtaW51dGVzIjogMTc3LAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIkZhdCBCdXJuIgogICAgICAgICAgICAgICAgfQogICAgICAgICAgICBdLAogICAgICAgICAgICAidmFsdWUiOiAiMTAyLjI4IgogICAgICAgIH0KICAgIF0sCiAgICAiYWN0aXZpdGllcy1oZWFydC1pbnRyYWRheSI6IHsKICAgICAgICAiZGF0YXNldCI6IFsKICAgICAgICAgICAgewogICAgICAgICAgICAgICAgInRpbWUiOiAiMTI6MDA6MDAiLAogICAgICAgICAgICAgICAgInZhbHVlIjogMTExCiAgICAgICAgICAgIH0sCiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICJ0aW1lIjogIjEyOjAxOjAwIiwKICAgICAgICAgICAgICAgICJ2YWx1ZSI6IDk3CiAgICAgICAgICAgIH0KICAgICAgICBdLAogICAgICAgICJkYXRhc2V0SW50ZXJ2YWwiOiAxLAogICAgICAgICJkYXRhc2V0VHlwZSI6ICJtaW51dGUiCiAgICB9Cn0=",
                        "metadata": {
                            "content-type": "application/json"
                        },
                        "error": null
                    },
                    "TkF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBQR==": {
                        "output": "ewogICAgIlNqRjFSRkJOYW0xNFJteEVjVzhyT1Zkek5rcEhkMVJaYUZkQlBRPT0iOiB7CiAgICAgICAgIm91dHB1dCI6ICJ7CiAgICAiYWN0aXZpdGllcy1oZWFydCI6IFsKICAgICAgICB7CiAgICAgICAgICAgICJjdXN0b21IZWFydFJhdGVab25lcyI6IFtdLAogICAgICAgICAgICAiZGF0ZVRpbWUiOiAidG9kYXkiLAogICAgICAgICAgICAiaGVhcnRSYXRlWm9uZXMiOiBbCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImNhbG9yaWVzT3V0IjogMTQwLjgzNTEsCiAgICAgICAgICAgICAgICAgICAgIm1heCI6IDcwLAogICAgICAgICAgICAgICAgICAgICJtaW4iOiAyMCwKICAgICAgICAgICAgICAgICAgICAibWludXRlcyI6IDY2LAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIk91dCBvZiBSYW5nZSIKICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImNhbG9yaWVzT3V0IjogMzAwLjk2ODI0LAogICAgICAgICAgICAgICAgICAgICJtYXgiOiAxMTAsCiAgICAgICAgICAgICAgICAgICAgIm1pbiI6IDg3LAogICAgICAgICAgICAgICAgICAgICJtaW51dGVzIjogMTY3LAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogIkZhdCBCdXJuIgogICAgICAgICAgICAgICAgfQogICAgICAgICAgICBdLAogICAgICAgICAgICAidmFsdWUiOiAiMTAyLjI4IgogICAgICAgIH0KICAgIF0sCiAgICAiYWN0aXZpdGllcy1oZWFydC1pbnRyYWRheSI6IHsKICAgICAgICAiZGF0YXNldCI6IFsKICAgICAgICAgICAgewogICAgICAgICAgICAgICAgInRpbWUiOiAiMTM6MDA6MDAiLAogICAgICAgICAgICAgICAgInZhbHVlIjogMTIxCiAgICAgICAgICAgIH0sCiAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICJ0aW1lIjogIjEzOjAxOjAwIiwKICAgICAgICAgICAgICAgICJ2YWx1ZSI6IDkwCiAgICAgICAgICAgIH0KICAgICAgICBdLAogICAgICAgICJkYXRhc2V0SW50ZXJ2YWwiOiAxLAogICAgICAgICJkYXRhc2V0VHlwZSI6ICJtaW51dGUiCiAgICB9Cn0=",
                        "metadata": {
                            "content-type": "application/json"
                        },
                        "error": null
                    }
}

```



# Schemas

The schemas are defined in [openapi.json].

## Action

Actions are used to set or add a feed source, see [Set feed source] and/or [Add feed source].

## Connect Token

Connect Tokens can be used to create [Connections] between Qiy Nodes and are identified with a [Connect Token Url], see [Get connect token], [Request connect token], [Register connect token], and [List connect tokens].

## Connection

Connections can be created between Qiy Nodes using [Connect Tokens] and are identified with a Connection Url.
See also [Get connection], [Request connection] and [List connections].

## Feed

See [openapi.json]#components/schemas/qiy-node-credential

## Message

See [openapi.json]#components/schemas/message

## Qiy Node Credential

A Qiy Node Credential consists of:
* an [RSA Private Key]
* a [Qiy Node Id], a [uuid],
* a [Transport Password], a [uuid]

For details, please refer to [openapi.json]#components/schemas/qiy-node-credential.


In Python, an [RSA Private Key] can be generated and saved as follows:

```
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives import serialization

private_key = generate_private_key(
        backend=default_backend(),
        public_exponent=65537,
        key_size=2048
        )

with open(pem_filename, "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption())
        )
```

## User Action Message

User Action Messages are used for request for feed events, see [Request for feed event].


[Acceptance Url]: https://user.dolden.net/user/v0/api
[Access feed request]: https://fdriesenaar.github.io/Client/openapi.html#/Feed%20access%20requests/Access%20feed
[Access feed]: #access-feed
[Access feeds request]: https://fdriesenaar.github.io/Client/openapi.html#/Feed%20access%20requests/Access%20feeds
[Access feeds]: #access-feeds
[Action]: #action
[Add feed source request]: https://fdriesenaar.github.io/Controller/openapi.html#/Feed%20sources/Add%20feed%20source
[Add feed source]: #add-feed-source
[Annex A Dynamic Endpoint Addresses]: #annex-a-dynamic-endpoint-addresses
[Annex B Events]: #annex-b-events
[Annex C Callbacks]: #annex-c-callbacks
[Client Feed Request Callback Endpoint]: #client-feed-request-callback-endpoint
[Client Feed Request Callback request]: https://fdriesenaar.github.io/Client/openapi.html#/Feeds/Request%20for%20feed%20callback
[Client Feed Request Callback]: #client-feed-request-callback
[Connect Token Create Endpoint]: #connect-token-create-endpoint
[Connect Token Endpoint]: #connect-token-endpoint
[Connect Token List Endpoint]: #connect-token-list-endpoint
[Connect Token]: #connect-token
[Connect Tokens]: #connect-token
[Connection Create Endpoint]: #connection-create-endpoint
[Connection Endpoint]: #connection-endpoint
[Connection Feeds Endpoint]: #connection-feeds-endpoint
[Connection List Endpoint]: #connection-list-endpoint
[Controller request for feed event]: https://fdriesenaar.github.io/Controller/openapi.html#/Requests%20for%20feed/Request%20for%20feed%20event
[Controller]: https://fdriesenaar.github.io/Controller/openapi.html
[Creating Qiy Nodes for Individuals]: ../High-Level%20Architectural%20Overview.md#512-creating-qiy-nodes-for-individuals
[Data Reference Received-v2 Event]: #data-reference-received-v2-event
[Definitions API Key]: #app-authentication
[Definitions Access Provider]: ../Definitions.md#access-provider
[Definitions Application Provider]: ../Definitions.md#application-provider
[Definitions Connect Token]: ../Definitions.md#connect-token
[Definitions Connection]: ../Definitions.md#connection
[Definitions Data Provider]: ../Definitions.md#data-provider
[Definitions Described Resource]: ../Definitions.md#described-resource
[Definitions Individual]: ../Definitions.md#individual
[Definitions Personal Data]: ../Definitions.md#personal-data
[Definitions Qiy Application]: ../Definitions.md#qiy-application
[Definitions Qiy Node Client]: ../Definitions.md#qiy-node-client
[Definitions Qiy Node Credential]: ../Definitions.md#qiy-node-credential
[Definitions Qiy Node Implementation]: ../Definitions.md#qiy-node-implementation
[Definitions Qiy Node]: ../Definitions.md#qiy-node
[Definitions Qiy Scheme]: ../Definitions.md#qiy-scheme
[Definitions Qiy Trust Network]: ../Definitions.md#qiy-trust-network
[Definitions Relying Party]: ../Definitions.md#relying-party
[Definitions Resource]: ../Definitions.md#resource
[Definitions Service Access Endpoint]: ../Definitions.md#service-access-endpoint
[Definitions Service Catalogue]: ../Definitions.md#service-catalogue
[Definitions Service Endpoint]: ../Definitions.md#service-endpoint
[Definitions Service Provider]: ../Definitions.md#service-provider
[Definitions Service Type]: ../Definitions.md#service-type
[Definitions Service]: ../Definitions.md#service
[Definitions Transport Authentication]: ../Definitions.md#transport-authentication
[Delete Qiy Node request]: https://fdriesenaar.github.io/openapi.html#/Qiy%20Nodes/Delete%20Qiy%20Node
[Delete Qiy Node]: #delete-qiy-node
[Dev2 Url]: https://dev2-user.testonly.digital-me.nl/user/v0/api
[DigitalMe]: https://digital-me.nl/
[Dynamic Endpoint Addresses]: #dynamic-endpoint-addresses
[Event Callback Endpoint]: #event-callback-endpoints
[Event Callback Endpoints]: #event-callback-endpoints
[Event Callbacks Endpoint]: #event-callbacks-endpoint
[Events]: #events
[Feed]: #feed
[Feeds Endpoint]: #feeds-endpoint
[Feeds]: #feeds
[Get /api]: https://fdriesenaar.github.io/openapi.html#/api/api
[Get connect token request]: https://fdriesenaar.github.io/openapi.html#/Connect%20tokens/Get%20connect%20token
[Get connect token]: #get-connect-token
[Get connection request]: https://fdriesenaar.github.io/openapi.html#/Connections/Get%20connection
[Get connection]: #get-connection
[Get endpoint addresses]: #get-endpoint-addresses
[Get event callback endpoints request]: https://fdriesenaar.github.io/openapi.html#/Event%20callback%20endpoints/Get%20event%20callback%20endpoints
[Get event callback endpoints]: #get-event-callback-endpoints
[Get node settings request]: https://fdriesenaar.github.io/openapi.html#/Qiy%20Nodes/Get%20node%20settings
[Get node settings]: #get-node-settings
[Get request for feed details request]: https://fdriesenaar.github.io/Controller/openapi.html#/Requests%20for%20feed/Get%20request%20for%20feed%20details
[Get service catalogue request]: https://fdriesenaar.github.io/Server/openapi.html#/Service%20catalogue/Get
[Get service catalogue]: #get-service-catalogue
[Getting help]: https://qiy.api.digital-me.nl/?version=latest#9acb0133-e012-4f49-a1e9-51283b8402c9
[High-Level Architectural Overview 4.3 Qiy Node]: ../High-Level%20Architectural%20Overview.md#43-qiy-node
[List connect tokens request]: https://fdriesenaar.github.io/openapi.html#/Connect%20tokens/List%20connect%20tokens
[List connect tokens]: #list-connect-tokens
[List connections request]: https://fdriesenaar.github.io/openapi.html#/Connections/List%20connections
[List connections]: #list-connections
[List feeds request]: https://fdriesenaar.github.io/Client/openapi.html#/Feeds/List%20feeds
[List feeds]: #list-feeds
[List messages request]: https://fdriesenaar.github.io/openapi.html#/Messages/List%20messages
[List messages]: #list-messages
[List requests for feed request]: https://fdriesenaar.github.io/Controller/openapi.html#/Requests%20for%20feed/List%20requests%20for%20feeds
[List requests for feed]: #list-requests-for-feed
[Message]: #message
[Messages Endpoint]: #messages-endpoint
[Messages]: #messages
[Node Create Endpoint]: #node-create-endpoint
[Node Settings Endpoint]: #node-settings-endpoint
[POST /ConnectionCreateEndpoint]: https://fdriesenaar.github.io/openapi.html
[POST /FeedsEndpoint/{feedId}]: https://fdriesenaar.github.io/openapi.html
[Production Url]: https://user.digital-me.nl/user/v0/api
[Proxy Url]: https://qiytesttool.pythonanywhere.com/qiy_nodes/qiy_node_api/proxy/v0/api
[Qiy Node Credential]: #qiy-node-credential
[Qiy Node Id]: #qiy-node-credential
[Qiy Test Tool dm]: https://qiy-test-tool-dpyt.cloud.digital-me.nl/
[Qiy Test Tool pa]: https://qiytesttool.pythonanywhere.com/
[RSA Private Key]: ../Definitions.md#rsa-private-key
[Register connect token request]: https://fdriesenaar.github.io/openapi.html#/Connect%20tokens/Request%20or%20register%20connect%20token
[Register connect token]: #register-connect-token
[Request connect token request]: https://fdriesenaar.github.io/openapi.html#/Connect%20tokens/Request%20or%20register%20connect%20token
[Request connect token]: #request-connect-token
[Request connection request]: https://fdriesenaar.github.io/openapi.html#/Connections/Request%20connection
[Request connection]: #request-connection
[Request creation of Qiy Node request]: https://fdriesenaar.github.io/openapi.html#/Qiy%20Nodes/Request%20creation%20of%20Qiy%20Node
[Request creation of Qiy Node]: #request-creation-of-qiy-node
[Request for feed event]: #request-for-feed-event
[Request for feed request]: https://fdriesenaar.github.io/Client/openapi.html#/Requests%20for%20feeds/Request%20for%20feed
[Request for feed]: #request-for-feed
[Self Endpoint]: #self-endpoint
[Send message request]: https://fdriesenaar.github.io/openapi.html#/Messages/Send%20message
[Send message]: #send-message
[Server Request for Feed request]: https://fdriesenaar.github.io/Server/openapi.html#/Requests%20for%20feeds/Request%20for%20feed
[Server Request for Feed]: #server-feed-request
[Server Request for Feeds]: #server-feed-request
[Service Access Endpoint]: #service-access-endpoint
[Service Catalogue Endpoint]: #service-catalogue-endpoint
[Service Endpoint]: #service-endpoint
[Service Request request]: https://fdriesenaar.github.io/Server/openapi.html#/Service%20requests/Service%20request
[Service Request]: #services-request
[Service Requests]: #service-request
[Services]: https://qiy.api.digital-me.nl/?version=latest#ab572b83-bd18-4a8e-85be-b549a0ac6758
[Set event callback endpoints request]: https://fdriesenaar.github.io/openapi.html#/Event%20callback%20endpoints/Set%20event%20callback%20endpoints
[Set event callback endpoints]: #set-event-callback-endpoints
[Set feed source request]: https://fdriesenaar.github.io/Controller/openapi.html#/Feed%20source/Set%20feed%20source
[Set feed source]: #set-feed-source
[Set node settings request]: https://fdriesenaar.github.io/openapi.html#/Qiy%20Nodes/Set%20node%20settings
[Set node settings]: #set-node-settings
[Set service catalogue request]: https://fdriesenaar.github.io/Server/openapi.html#/Service%20catalogue/Set
[Set service catalogue]: #set-service-catalogue
[Start listening to events request]: https://fdriesenaar.github.io/openapi.html#/Events/Start%20listening%20to%20events
[Start listening to events]: #start-listening-to-events
[State Handled Callback Endpoint]: #state-handled-callback-endpoint
[State Handled Callback]: #state-handled-callback
[State Handled Event]: #state-handled-event
[Subscriptions]: https://qiy.api.digital-me.nl/?version=latest#ec0ab04d-ab6e-4a9c-9b45-e6b75b583bff
[Transport Layer]: ../High-Level%20Architectural%20Overview.md#8-the-transport-layer
[Transport Password]: #qiy-node-credential
[User Action Message Event]: #user-action-message-event
[User Action Message Events]: #user-action-message-event
[User Action Message List Endpoint]: #user-action-message-list-endpoint
[User Action Message]: #user-action-message
[controller]: https://fdriesenaar.github.io/Controller/openapi.html
[openapi.json]: openapi.json
[uuid]: ../Definitions.md#uuid
