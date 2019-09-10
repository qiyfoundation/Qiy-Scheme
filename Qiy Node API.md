# Qiy Node

This document describes the Qiy Node API.

# API Basics

## Registration

Service Providers and Application Providers can register with an Access Provider:

* both receive an API Key
* Service Providers can whitelist endpoints and receive a Qiy Node Credential.

## Service Desk

Please contact the Service Desk for your requests. The Service Desk is available during regular CEST office hours and can be contacted by e-mail or phone:

    service@digital-me.nl
    +31 (0) 411-616565

## Versions

This api is versioned using Semantic Versioning 2.0.0 and follows this specification. In addition, the following rules apply:

    DigitalMe supports two major versions in the production environment: one primary version and one secondary version.
    DigitalMe will support a secondary version for at least 6 months.
    DigitalMe supports one development version in a development environment.
    A development version may change at any time.

The current version of the api is returned by Get /api.

## Authentication

### App Authentication

In the next version, Qiy Applications are required to authenticate requests using an API Key implemented using basic authentication.

An e-mail address provided by the application provider will be used to maintain the API Keys. Please use this e-mail address to e-mail the Service Desk your API Key request.

### User Authentication

All requests but the request to create a Qiy Node and the Api Request MUST be user authenticated using a signed token that can only be calculated using a Qiy Node Credential.

The token can be passed in the 'Authorization'-header parameter, but MUST be passed in the 'Authorization-node-QTN'-header parameter when App Authentication is used.
Python

In Python, the authorization header parameter can be calculated with the package 'pyOpenSSL'. Using a pem-file with the primary key of the Qiy Node it can be generated as follows:

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

Bash

The authorization header parameter can be generated with this Bass script:

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

### Password Header Parameter

Some request have a mandatory 'password'-header parameter, because they use the Transport Layer which requires authentication with a Transport Password.

## Dynamic Endpoint Addresses

The Qiy Node Api uses dynamic endpoint addresses most of which can be obtained using GET /api and Get endpoint addresses. The addresses can be cached, but should be refreshed every day.

### Action Messages List Endpoint

This endpoint can be used to list action messages. The current address of the endpoint is returned in the "amList"-member of the response of Get endpoint addresses.

### Connect Token Create Endpoint

This endpoint can be used to request or register Connect Tokens. The current address of the endpoint is returned in the "ctCreate"-member of the response of Get endpoint addresses.

### Connect Token List Endpoint

This endpoint can be used to list Connect Tokens. The current address of the endpoint is returned in the "ctList"-member of the response of Get endpoint addresses.

### Connection Create Endpoint

The Connection Create Endpoint can be used to create a connection. The current address of the endpoint is returned in the "scan"-member of the response of Get endpoint addresses.

### Connection Endpoint

This endpoint can be used to get the details of a connection. The endpoint urls are returned by Request connection and List connections.

### Connection Feeds Endpoint

This endpoint can be used by a Relying Party to request for a feed.

The current address of the endpoint is returned in a "feeds"-endpoint of a connection.

### Connections List Endpoint

The Connections List Endpoint can be used to list connections. The current address of the endpoint is returned in the "ctList"-member of the response of Get endpoint addresses.

### Events Endpoint

The Events Endpoint can be used to receive events. The current address of the endpoint is returned in the "events"-member of the response of Get endpoint addresses.

### Event Callbacks Endpoint

This Endpoint can be used to set or get the addresses of the Event Callback endpoints. The current address of the endpoint is returned in the "eventCallbacks"-member of the response of Get endpoint addresses.

### Feeds Endpoint

A Relying Party uses this endpoint to list or access one or more feeds of an Individual (connection) or of himself (a Qiy Node).

The address of the endpoint for a connection is returned in the "feeds"-member of the response of List connections and/or Get connection. The address of the endpoint for a Qiy Node is returned in the "feeds"-member of the response of Get endpoint addresses.

### Mailbox Endpoint

This endpoint can be used to send and receive messages. The current address of the endpoint is returned in a "mbox"-member of the response of List connections or Get connection.

### Node Create Endpoint

This endpoint can be used to request the creation of a Qiy Node. The current address of the endpoint is returned by Get /api.

### Node Settings Endpoint

This endpoint can be used to get and set settings of a Qiy Node. The current address of the endpoint is returned in the "nodeSettings"-member of the response of Get endpoint addresses

### Reference Endpoint

This endpoint can be used to tbd. The current address of the endpoint is returned in the "ref"-member of the response of Get endpoint addresses.

### References Endpoint

This endpoint is deprecated. The current address of the endpoint is returned in the "refs"-member of the response of Get endpoint addresses.

### Self Endpoint

This endpoint can be used to delete a Qiy Node. The endpoint address is returned in the 'self'-property of Get endpoint addresses.

### Service Catalogue Endpoint

This endpoint can be used to get or set the contents of a Service Catalogue. The current address of the endpoint is returned in the "serviceCatalog"-member of the response of Get endpoint addresses.

## Servers

The Qiy Node service runs in a Mock environment, a development environment, the acceptance environment and the production environment. The server urls are:
DTAP environment 	Server url
Mock 	 - See the url variable in the Postman 'Mock Server' environment - 
Dev2
    	https://dev2-user.testonly.digital-me.nl/user
    
Acceptance
    	https://user.dolden.net/user
    

The server url of the Production environment will be given during the entry-transition phase, when your Qiy Trust Based solution will go live.

Ensure that the following system settings are configurable to allow for smooth switching between the environments:

* server url
* Qiy Node Id
* Qiy Node private key
* Transport password
* API key

## Events

### Connected to Router Event

This event is fired after a request for a connection and can be used to monitor the creation of a connection.

### Connected to Router Failed Event

This event is fired after a request for a connection and signals that a connection could not be established.

### Data Reference Failure Event

This server-sent event is fired when a Request for feed fails.

### Data Reference Received-v2 Event

This server-sent event is generated by a Qiy Node of a Relying Party when it has received a new feed.

### Data Request Forwarded Event

This server-sent event is fired when a feed is being accessed.

### Data Request Fulfilled Event

This server-sent event is fired when a feed has been accessed succesfully.

### Data Request Failure Event

This server-sent event is fired when a feed could not be accessed succesfully.

### Data Request Not Forwarded Event

This server-sent event is fired when and if a feed cannot be accessed.

### Pending Peer Data Reference Event

This server-sent event can be fired when a feed is being accessed.

### Unexpected Data Reference Event

This server-sent event can be fired when a feed is being accessed.

### Persistent Id Event

This event can be used to monitor the creation of a connection.

### Routing Failure Event

This event is fired after a request for a connection and signals that a connection could not be established.

### Shared Secret Received Event

This event is fired after a request for a connection upon creating connection.

### Shared Secret Sent Event

This event is fired after a request for a connection upon creating connection.

### State Handled Event

This event is fired when a connection has been created, see GET State Handled Event for an example.

### User Action Message Event

This event is fired by a Qiy Node when it receives a message that requires interaction with the End User, and can be used by an End User application to detect that a feed request has been received.
Example event

event: USER_ACTION_MESSAGE data: {
   'type': 'USER_ACTION_MESSAGE',
   'connectionUrl': 'https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e',
   'extraData': 'https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4'
}

## Documentation

### Qiy Scheme

The Qiy Scheme of the Qiy Foundation is a means to give individuals control over their data while creating value for organisations, see https://www.qiyfoundation.org.

#### Qiy Trust Network

The Qiy Trust Network is the operational part of the Qiy Scheme which enables its users to securely and privately connect and interact.

##### Access Provider

An Access Provider is an organisation that provides Service Providers access to the Qiy Trust Network.

##### Application Provider

An Application Provider is an organisation that provides software and/or applications to Qiy Users that can be used to access the Qiy Trust Network.

#### Qiy User

A Qiy User is a user of the Qiy Trust Network.

##### Individual

An Individual is a Qiy User that accesses the Qiy Trust Network as a natural person.

##### Service Provider

A Service Provider is a Qiy User that uses the Qiy Trust Network to provide services to Individuals.

###### Relying Party

A Relying Party is a Service Provider that uses services provided by other Service Providers. They can do so using Feed requests.

###### Data Provider

A Data Provider is a Service Provider that provides personal data services. They provide data subjects control over personal data using feeds, see Service Orchestration.

### End User App

An End User App is a Qiy Node Client which enables an Individual to subscribe to and orchestrate (data) services.

#### Setup

An End User App can only access the Qiy Trust Network under the following preconditions:

    The End User App uses a valid Access Provider Token.
    The End User App correctly authenticates Qiy Node requests.
    The End User App must allow End Users to use a new Qiy Node or reuse an existing one.

#### Subscribe

An Individual can subscribe to a service as follows:

    Conclude an subscription agreement (out-of-scope).
    Connect with the Service Provider.

#### Orchestrate

When an Individual has subscribed to a Service provided by a Relying Party, the latter may request for a feed. The End User App can process these requests as follows:

    [Wait for User Action Message Event][Feeds Wait for User Action Message Event] to receive feed requests.
    Extract the userActionMessageUrl from the 'extraData'-field of the event and use it to [fetch the user action message][Feeds Get user action message] with possible Data Providers.
    Extract the feed request containing the possible Data Providers and related actionUrls.
    Present the options to the End User and capture the result, e.g. the selected Data Providers.
    [Add the data providers][Feeds Add feed] or [change the data providers][Feeds Set feeds] using the related actionUrls.

After these steps, feeds will be automatically created and provided to the Relying Party.

### Service Provider

#### Setup

Before a Service Provider can provide services via Qiy he has to make the following preparations:

    Describe the services and make these descriptions publicly available.
    Setup a State Handled Endpoint.
    (only for Data Providers:) Setup Service Endpoint(s).
    (only for Relying Parties:) Setup Data Reference Received-v2 Endpoint.
    Prepare the Computer systems to correctly produce authenticated requests.
    Contact the Access Provider DigitalMe to whitelist the endpoints and receive a Qiy Node Credential and an API Key.
    Configure the computer system for the Qiy Node.
    Publish the Service Catalogue with Qiy.

##### Service Catalogue

A Service Provider publishes the (data) service types it supports in his Service Catalogue, which consists of an array of urls for Service Type Descriptions with additional details, for example for the associated [Feed Request Endpoints][API Basics Documentation Service Provider Setup Endpoints Feed Request Endpoint], see Get service catalogue.

A Service Type Description can contain a list of urls for the description of the Operation Types of the service which are used in as value of the protocol-member in [Feed Requests][Feeds Request for feed]. If the Service Type Description does not contain Operation Type Urls, the Service Type Description Url can be used instead.

##### Endpoints

###### Event Callback Endpoints

* State Handled Endpoint

This event callback endpoint for State Handled Events is a Technology Service which can be used to detect that a connection has been created using callbacks. The address of the endpoint can be defined with Set event callback endpoints.

* Data Reference Received-v2 Endpoint

This event callback endpoint is a Technology Service which can be setup and used by a Relying Party to obtain new feed id's.

The address of the endpoint can be defined with Set event callback endpoint.

###### Service Endpoint

A Data Provider uses this backend endpoint to serve requests for feed callback requests and feed access callback requests.

The Data Provider provides the uri of the endpoint using set service catalogue.

### Qiy Node Client

A Qiy Node Client is any Application Service that accesses a Qiy Node. This section addresses topics that are relevant for developers of both End User Apps and computer systems of Service Providers.

#### Qiy Node

A Qiy Node is an access point for the Qiy Trust Network and can be maintained and used with node calls. Qiy Nodes are provided by DigitalMe to Service Providers on registration. End User Apps can create Qiy Nodes by generating a Qiy Node credential and request the creation of a Qiy Node as described in section 3.1 Create Qiy Node of the DigitalMe Qiy Node specification.

##### Settings

A Qiy Node can have diferent settings which can be maintained with the get and set node setting calls.

##### Qiy Node Credential

A Qiy Node credential consists of:

    A Qiy Node Id
    An RSA key pair
    A Transport Password

* Qiy Node Primary Key

One element of the Qiy Node Credential is the primary key.
Python

In Python, the primary key can be created with the package 'cryptography'. The key can be created and persisted as follows:

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

* Qiy Node Public Key

In python, the public key can be obtained using the package 'pyOpenSSL'. Given the pem-file, this goes as follows:

import OpenSSL

with open("data/"+target_short_node_id+".pem" , "r") as f:
    buffer = f.read()
private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, buffer)
public_key=OpenSSL.crypto.dump_publickey(
    OpenSSL.crypto.FILETYPE_ASN1,
    private_key)

#### Connections

Individuals can connect and interact with other Individuals and Service Providers using connections between the related Qiy Nodes.

Connections can be created between an invitor and an invitee using Connect Tokens as follows:

    The invitor [requests][Connections Request connect token] or creates and [registers][Connections Register connect token] a Connect Token.
    The invitor invites the invitee to connect with the Connect Token out-of-band.
    The invitee [requests a connection using the connect token][Connections Request connection].
    The invitor receives a [State Handled Callback][Connections State Handled Callback] notifying that the connect token has been used to create a connection.
    The invitee receives a [State Handled Event][Connections State Handled Event] notifying that the connection has been established.

#### Connect Tokens

A Connect Token can be used to create connections between Qiy Users, for example an Individual and a Service Provider. The connect token may be created by either of the two, but when connecting to a Service Provider it must always be [registered][Connections Register connect token] or otherwise [requested][Connections Request connect token] by the Service Provider.

##### Create Connect Token

A Connect Token is a json-object with three members which can be created as follows:

    id: This is a label and can be any string.
    target: The format of this member is returned in the "target-template"-member of the response of Get endpoint addresses, where '~id~' should be a uuid.
    tmpSecret: This member is a string: an array of 16 random bytes which is base64-encoded.

In Java the tmpSecret can be generated as follows:

SecureRandom RANDOM = new SecureRandom();
byte[] tmpSecret = new byte[16];
RANDOM.nextBytes(tmpSecret);
String tmpSecretString = Base64.getEncoder().encodeToString(tmpSecret);

##### Online Connect Tokens

An Online Connect Token is a connect token that has been created by the Qiy Trust Network when executing [Request Connect Token][Connections Request connect token].

##### Offline Connect Tokens

An Offline Connect Token is a Connect Token that has been created by a Qiy Node Client and registered later using [Register connect token][Connections Register connect token].

##### On-Connected Actions

An On-Connected Actions is an action such as the execution of a http-request that can be defined for a Connect Token and that is executed whenever the token has been used to create a connection.

#### Feeds

Feeds can be used by a Relying Party to access personal data (consume subscribed services) of an individual from (provided by) a Data Provider.
##### Relying Party

A Relying Party (RP) can do so as follows:

    The RP requests an Individual for a feed using a request for feed.
    The RP receives a callback with (or polls for) a feed id.
    The RP uses the feed id in a feed access-request to acquire the data (issue a service operation request).

##### End User App

The feed-flow of an End User App is described tbd.

##### Data Provider

The feed-flow for a Data Provider (DP) is as follows:

    The DP sets up and uses a Service Endpoint to receive and process requests for feeds and return feed id's.
    The DP sets up and uses the same Service Endpoint to receive and process feed access requests.

#### Events

A Qiy Node supports a number of events. The Qiy Client can receive the events using a Server-Sent Events-listener, see Start listening to events, or using callbacks.

#### Messages

Qiy Users can use connections to send and receive messages.

# API

## GET Api
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/api

GET /api can be used to get the api version and the current address of the Node Create Endpoint.

NB: App Authentication is OPTIONAL in this version, but will be MANDATORY in v1.
HEADERS
x-mock-response-code
get_api


Example Request
Api - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/api"

Example Response
200 - OK

{
  "links": {
    "create": "https://user.digital-me.nl/nodes/"
  },
  "serverTime": 1537352486551,
  "id": "68235db3-a391-42ab-964e-de7773640e5b",
  "currentVersion": "1.0.44"
}

# Nodes
## POST Request creation of Qiy Node
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/nodeCreateEndpointUrl

This Node Create Endpoint-call can be used to request the creation of a Qiy Node.

A 201-Created will be returned when the Qiy Node has been created.
HEADERS
Content-Type
application/json
x-mock-response-name
Mock Request creation of Qiy Node - OK
BODY raw

{
	"alias": "pt_usernode_qnc_test_de", 
	"id": "pt_usernode_qnc_test_de", 
	"publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0TK8dMRxvXp66teemQe/tzUi26LBWfkO0pWGqyzmnNO6ISALt+rgEPl5mhqztAU4xI9iE/L9dCzC3snb2OQT+2/IaV9ilt1UAmZhyuogPeTKykPRFR2oT51wWoIuG4hD0x6iBhFCorn087Te99oS1RwS1RR5wFjIs/ol3ldawZ29xemsskmPEWJ/QpfpauBxvSbZEXRy15cAWnWO9yVzizUszwNjP8Ca0/K7NKa+lOtp09egO12SBMfX871AI44wWkZqPsr+O5cpo8Srw+90dbETA1Ypno3lpel2lBMQaf0+Srmjd/bJs9dlaXCTljoLt2uvOmriDSI6eSJZ7FxH4wIDAQAB", 
	"password": "9b449623-f361-425b-bca8-8c23c159e4c0",
	"nodeSettings": {
		"askDappre": "no",
		"usePersistentId": "yes"
	}
}



Example Request
Create Qiy Node - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/nodeCreateEndpointUrl" \
  --header "Content-Type: application/json" \
  --header "AP-Token: {{apToken}}" \
  --data "{
	\"alias\": \"pt_usernode_qnc_test_de\", 
	\"id\": \"pt_usernode_qnc_test_de\", 
	\"publicKey\": \"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0TK8dMRxvXp66teemQe/tzUi26LBWfkO0pWGqyzmnNO6ISALt+rgEPl5mhqztAU4xI9iE/L9dCzC3snb2OQT+2/IaV9ilt1UAmZhyuogPeTKykPRFR2oT51wWoIuG4hD0x6iBhFCorn087Te99oS1RwS1RR5wFjIs/ol3ldawZ29xemsskmPEWJ/QpfpauBxvSbZEXRy15cAWnWO9yVzizUszwNjP8Ca0/K7NKa+lOtp09egO12SBMfX871AI44wWkZqPsr+O5cpo8Srw+90dbETA1Ypno3lpel2lBMQaf0+Srmjd/bJs9dlaXCTljoLt2uvOmriDSI6eSJZ7FxH4wIDAQAB\", 
	\"password\": \"9b449623-f361-425b-bca8-8c23c159e4c0\",
	\"nodeSettings\": {
		\"askDappre\": \"no\",
		\"usePersistentId\": \"yes\"
	}
}
"

## GET Get endpoint addresses
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/api

Get current addresses of the dynamic path endpoints.
HEADERS
x-mock-response-name
Mock Get endpoint addresses - OK


Example Request
Get endpoint addresses - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/api" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}"

Example Response
200 - OK

{
  "currentVersion": "1.0.66-SNAPSHOT",
  "serverTime": 1565172386740,
  "id": "mgd_dev2",
  "links": {
    "scan": "https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_dev2",
    "connections": "https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_dev2",
    "feeds": "https://dev2-user.testonly.digital-me.nl/user/mgd_dev2/feeds",
    "ctCreate": "https://dev2-user.testonly.digital-me.nl/user/connecttokens/mgd_dev2",
    "ct-create": "https://dev2-user.testonly.digital-me.nl/user/connecttokens/mgd_dev2",
    "self": "https://dev2-user.testonly.digital-me.nl/user/owners/id/mgd_dev2",

## PUT Set event callback endpoints
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventCallbacksEndpointUrl

This Event Callbacks Endpoint-request can be used to define the addresses of the event callback endpoints.
HEADERS
Content-Type
application/json
BODY raw

{
	"DATA_REFERENCE_RECEIVED2": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/dataReferenceReceivedCallbackEndpointUrl",
	"STATE_HANDLED": "stateHandledCallbackEndpointUrl"
}



Example Request
Set event callback endpoints - OK

curl --location --request PUT "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventCallbacksEndpointUrl" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}" \
  --data "{
	\"DATA_REFERENCE_RECEIVED2\": \"http://localhost:10443/test\",
	\"STATE_HANDLED\": \"http://localhost:10443/test\"
}"

## GET Get event callback endpoints
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventCallbacksEndpointUrl

This Event Callbacks Endpoint-request can be used to get the addresses of the event callback endpoints.
HEADERS
Accept
application/json


Example Request
Get event callback endpoints - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventCallbacksEndpointUrl" \
  --header "Accept: application/json"

Example Response
200 - OK

{
  "DATA_REFERENCE_RECEIVED2": "http://localhost:10443/test",
  "STATE_HANDLED": "http://localhost:10443/test"
}

## GET Start listening to events
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventsEndpointUrl

This Events Endpoint-call can be used to start listening to Qiy Node events.

It starts a long-living session with a heartbeat to keep the response open. Every 10 seconds a 'ping' comment will be sent. If this is not received for more than that time, something has gone wrong.
HEADERS
x-mock-response-name
Mock Start listening to events - ping


Example Request
Start listening to events - ping

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventsEndpointUrl" \
  --header "x-mock-response-name: Mock Start listening to events - ping"

Example Response
200 - OK

: ping

## GET Get node settings
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_nodeSettings

This Node Settings Endpoint-call returns the node settings.
HEADERS
x-mock-response-name
Mock Get node settings - OK


Example Request
Get node settings - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_nodeSettings" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}"

Example Response
200 - OK

{
  "askDappre": "no",
  "usePersistentId": "yes"
}

## PUT Set node settings
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_nodeSettings

This Node Settings Endpoint-call sets the node settings.
HEADERS
Content-Type
application/json
x-mock-response-name
Mock Set node settings - OK
BODY raw

{
	"askDappre": "no",
	"usePersistentId": "yes"
}



Example Request
Set node settings - OK

curl --location --request PUT "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_nodeSettings" \
  --header "Content-Type: application/json" \
  --header "x-mock-response-name: Mock Set node settings - OK" \
  --data "{
	\"askDappre\": \"no\",
	\"usePersistentId\": \"yes\"
}"

# DEL Delete Qiy Node
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_self

This Self Endpoint-call can be used to delete a Qiy Node.
HEADERS
password
{{transportPassword}}
x-mock-response-name
Mock Delete Qiy Node - OK


Example Request
Delete Qiy Node - OK

curl --location --request DELETE "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_self" \
  --header "password: {{transportPassword}}" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}"

# Services
## GET Get service catalogue
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_serviceCatalog?internal=False

This Service Catalogue Endpoint-call gets the Service Catalogue.
HEADERS
x-mock-response-name
Mock Get Service Catalogue - OK
PARAMS
internal
False

If False or None, only external services will be gotten.



Example Request
Get Service Catalogue - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_serviceCatalog?internal=False" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}"

Example Response
200 - OK

{
  "{{serviceTypeUrl}}": {
    "type": "external",
    "uri": "{{feedRequestEndpointUrl}}",
    "method": "POST"
  }
}

## PUT Set service catalogue
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_serviceCatalog

This Service Catalogue Endpoint-call sets the Service Catalogue including the uri and the method of Service Endpoints.
HEADERS
Content-Type
application/json
x-mock-response-name
Mock Set service catalogue - OK
BODY raw

{
  "{{serviceTypeUrl}}": {
    "type": "external",
    "uri": "{{feedRequestEndpointUrl}}",
    "method": "POST"
  }
}



Example Request
Set service catalogue - OK

curl --location --request PUT "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_serviceCatalog" \
  --header "Content-Type: application/json" \
  --header "x-mock-response-name: Mock Set service catalogue - OK" \
  --data "{
  \"{{serviceTypeUrl}}\": {
    \"type\": \"external\",
    \"uri\": \"{{feedRequestEndpointUrl}}\",
    \"method\": \"POST\"
  }
}"

# Connections

## Relying Party/Data Provider
POST Request connect token
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_ctCreate

This Connect Token Create Endpoint-call can be used to request a connect token: a json object with the members 'identifier', 'tmpSecret' and 'target'. When the call was succesfull, a 200-OK will be returned with the Connect Token Url in the Location header of the response.
HEADERS
Content-Type
application/json
password
{{transportPassword}}
x-mock-response-name
Mock Request connect token - OK
Accept
application/json
BODY raw

{
    "expires": 2349020398,
	"useBudget": 1
}



Example Request
Request connect token - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_ctCreate" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}" \
  --header "Content-Type: application/json" \
  --header "password: {{transportPassword}}" \
  --data "{
    \"expires\": 2349020398,
    \"useBudget\": 1
}"

Example Response
200 - OK

{
  "expires": 2349020398,
  "useBudget": 1,
  "json": {
    "identifier": "Service Provider",
    "tmpSecret": "7nzMAI61N6b5dPCCYD4IgQ==",
    "target": "https://issuer.dolden.net/issuer/routes/webhook/5e581908-06d3-4ad0-9f14-8ec85b9b9fb4"
  }
}

POST Register connect token
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_ctCreate

This Connect Token Create Endpoint-call registers a connect token: a json object with the members 'identifier', 'tmpSecret' and 'target'. The call returns the Connect Token Url in the Location header of the response.
HEADERS
Content-Type
application/json
password
{{transportPassword}}
x-mock-response-name
Mock Register connect token - OK
BODY raw

{
    "expires": 2349020398,
	"useBudget": 1,
	"json": {
		"identifier": "Service Provider 1",
		"tmpSecret": "9paMAI61N6b5dPCCYD4IiS==",
		"target": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1connectTokenOffline2target"
	}
}



Example Request

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_ctCreate" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}" \
  --header "Content-Type: application/json" \
  --header "password: {{transportPassword}}" \
  --data "{
	\"useBudget\": 1,
	\"json\": {
		\"identifier\": \"Service Provider\",
		\"tmpSecret\": \"7nzMAI61N6b5dPCCYD4IgQ==\",
		\"target\": \"https://issuer.dolden.net/issuer/routes/webhook/5e581908-06d3-4ad0-9f14-8ec85b9b9fb4\"
	}
}"

POST State Handled Callback
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/stateHandledCallbackEndpointUrl

This callback on the [State Handled Callback Endpoint][API Basics Documentation Service Provider Setup Endpoints State Handled Endpoint] can be used to detect a new connection.
HEADERS
x-mock-response-name
Mock State Handled Callback - OK
BODY raw

{
  "type": "STATE_HANDLED",
  "connectionUrl": "https://dev1-user.testonly.digital-me.nl/user/connections/user/509f79f8-6562-49cd-bb24-4163557d7e59/3b5151e3-adc7-403a-a31a-8bd504e2c8ae",
  "extraData": {
    "newUri": "https://dev1-user.testonly.digital-me.nl/user/connections/user/509f79f8-6562-49cd-bb24-4163557d7e59/ce5b2dd5-1bdd-41aa-b0ad-d0afa2e9a3cb",
    "connectToken": "https://dev1-user.testonly.digital-me.nl/user/connecttokens/509f79f8-6562-49cd-bb24-4163557d7e59/7ced41dc-76ff-469e-9fa0-3f34c73d0a2b",
    "PID": "9GqX94/EoOcD47hCvBQ+eg=="
  }
}



Example Request
State Handled Callback - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/stateHandledCallbackEndpointUrl" \
  --header "x-mock-response-name: Mock State Handled Callback - OK" \
  --data "{
  \"type\": \"STATE_HANDLED\",
  \"connectionUrl\": \"https://dev1-user.testonly.digital-me.nl/user/connections/user/509f79f8-6562-49cd-bb24-4163557d7e59/3b5151e3-adc7-403a-a31a-8bd504e2c8ae\",
  \"extraData\": {
    \"newUri\": \"https://dev1-user.testonly.digital-me.nl/user/connections/user/509f79f8-6562-49cd-bb24-4163557d7e59/ce5b2dd5-1bdd-41aa-b0ad-d0afa2e9a3cb\",
    \"connectToken\": \"https://dev1-user.testonly.digital-me.nl/user/connecttokens/509f79f8-6562-49cd-bb24-4163557d7e59/7ced41dc-76ff-469e-9fa0-3f34c73d0a2b\",
    \"PID\": \"9GqX94/EoOcD47hCvBQ+eg==\"
  }
}"

## Individual
POST Request connection
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1connectionCreateEndpointUrl

This asynchronous Connection Create Endpoint-call can be used to request a connection using a Connect Token: a json object with the members 'identifier', 'tmpSecret' and 'target'.

The creation of the connection can be followed using events, for details see /API Basics/Documentation/Qiy Node Client/Connections:

If and when the connection has been established, at least two State Handled Events will be fired; one for the Qiy Node Client that requested the connection and one for the Qiy Node Client that requested or registered the Connect Token. The event will also be fired for any other Qiy Node Client that is connected to one of the involved Qiy Nodes. Also, two State Handled Callbacks will be fired for the Qiy Nodes, but only if the State Handled Callback Endpoint has been set, see Set event callback endpoints.

Alternatively, the list of connections can be gotten. Here a connection should be present with the 'activeFrom' property should have the value of the current time (in milliseconds from the epoch), 'pid' should be a Base 64 encoded value, 'state' should be 'connected'.
HEADERS
Content-Type
application/json
x-mock-response-name
Mock Request connection - OK
BODY raw

{
    "identifier": "Service Provider 1",
    "tmpSecret": "9paMAI61N6b5dPCCYD4IiS==",
    "target": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1connectTokenOffline2target"
}



Example Request
Request connection - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_scan" \
  --header "Content-Type: application/json" \
  --data "{
    \"identifier\": \"Service Provider 1\",
    \"tmpSecret\": \"9paMAI61N6b5dPCCYD4IiS==\",
    \"target\": \"https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1connectTokenOffline2target\"
}"

GET Connected to Router Event
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1eventsEndpointUrl

The Connected to Router Event can be used to monitor the creation of a connection.
HEADERS
Accept
text/event-stream
x-mock-response-name
Mock Connected to Router Event - OK


Example Request
Connected to Router Event - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventsEndpointUrl" \
  --header "Accept: text/event-stream"

Example Response
-

event: CONNECTED_TO_ROUTER data: {
  "type":"CONNECTED_TO_ROUTER",
  "connectionUrl":"https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_citizen_dev2/bb4f7e57-2b72-48d0-a317-7c7203505389"
}

GET Persistent Id Event
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1eventsEndpointUrl

The Persistent Id Event is an event that is created upon creation of a connection.
HEADERS
Accept
text/event-stream
x-mock-response-name
Mock Persistent Id Event - OK


Example Request

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventsEndpointUrl" \
  --header "Accept: text/event-stream"

Example Response
-

event: PID data: {
  "type":"PID",
  "connectionUrl":"https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_citizen_dev2/bb4f7e57-2b72-48d0-a317-7c7203505389",
  "extraData":{
    "new-uri":"https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_citizen_dev2/e3d7e3f7-e5f8-44d9-89d8-f9ecbbd56bd1",
    "pid":"KjwFO9FzDrAC7Cd8YDJj8w=="
  }
}

GET State Handled Event
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1eventsEndpointUrl

This event is fired when a connection has been created.
HEADERS
Accept
text/event-stream
x-mock-response-name
Mock State Handled Event - OK


Example Request
State Handled Event - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/eventsEndpointUrl" \
  --header "Accept: text/event-stream"

Example Response
200 - OK

event: STATE_HANDLED data: {
  "type":"STATE_HANDLED",
  "connectionUrl":"https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_citizen_dev2/e3d7e3f7-e5f8-44d9-89d8-f9ecbbd56bd1",
  "extraData":{
    "newUri":"https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_citizen_dev2/e3d7e3f7-e5f8-44d9-89d8-f9ecbbd56bd1",
    "PID":"KjwFO9FzDrAC7Cd8YDJj8w=="
  }
}

## GET Get connection
{{connectionEndpointUrl}}

This Connection Endpoint-call returns connection details.


Example Request
Get connection - OK

curl --location --request GET "{{connectionEndpointUrl}}" \
  --header "Authorization: QTF pt_usernode_qnc_test_de 1519064940667:qtLYGGLWtsBELt9YWh/MBwqofyMNiTzUZypYeA+VjbOWt6LWdG1Fp3xZHlfPHADZUlBgvyWGyirCEqg8qBYiJXJsXaZDz5t+qQSZx0Euod7aMaSDPIUqeicujiKJAQLEyQYb5g9nJFXswKus6gq1DlXU807eGLkf8LYMrRMLijLcXnSbu7iW0ZZgnNwVS3+9NOTBLTwhy166DO7Th7IGz/4FxWq7ba90Hhp24PzYvskaC8FCEj1iNs4T8uu6KWvazN3xZL40WLUFK9m5FjJP4epaCwjqJSOtmhovqkEu++ML3K7Us5rPM9toshPZwut5VYEJFkMBSMsoTK5xdz7Qrw==" \
  --header "AP-Token: {{apToken}}"

Example Response
200 - OK

{
  "activeFrom": 1551796945000,
  "links": {
    "feeds": "https://dev2-user.testonly.digital-me.nl/user/mgd_dev2/connections/016706d0-b3c1-4104-b6de-aacdf33230c0/feeds",
    "mbox": "https://dev2-user.testonly.digital-me.nl/user/mbox/user/mgd_dev2/016706d0-b3c1-4104-b6de-aacdf33230c0",
    "references": "https://dev2-user.testonly.digital-me.nl/user/references/mgd_dev2/016706d0-b3c1-4104-b6de-aacdf33230c0",
    "self": "https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_dev2/016706d0-b3c1-4104-b6de-aacdf33230c0"
  },
  "pid": "aAQt41QqCvJuy8DMBayDCQ==",
  "state": "connected"
}

## GET Get connect token
{{connectTokenUrl}}

This call returns the details of a Connect Token.

When succesfull, a 200-OK will be returned with the details in the body of the response.
HEADERS
Accept
application/json


Example Request
Get connect token - OK

curl --location --request GET "{{sp1connectToken1url}}" \
  --header "Accept: application/json"

Example Response
200 - OK

{
  "expires": 2349020398,
  "name": "example token",
  "note": "Just an example",
  "useBudget": 1,
  "json": {
    "identifier": "Service Provider",
    "tmpSecret": "7nzMAI61N6b5dPCCYD4IgQ==",
    "target": "https://issuer.dolden.net/issuer/routes/webhook/5e581908-06d3-4ad0-9f14-8ec85b9b9fb4"
  }
}

## GET List connect tokens
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1connectTokenListEndpointUrl

This Connect Token List Endpoint-call lists the connect tokens.
HEADERS
Accept
application/json
x-mock-response-name
Mock List connect tokens - OK


Example Request
List connect tokens

curl --location --request GET "{{connectTokenEndpointUrl}}"

Example Response
-

[
  {
    "created": 1542882407000,
    "json": {
      "identifier": "mgd_dev2",
      "target": "https://dev2-issuer.testonly.digital-me.nl/issuer/routes/webhook/2fe11d37-ee84-45f9-b07c-629c11532407",
      "tmpSecret": "tOCChOFtQiflrMGBPQfy8w=="
    },
    "lastUsed": 1542882800000,
    "links": {
      "self": "https://dev2-user.testonly.digital-me.nl/user/connecttokens/mgd_dev2/e95feef5-3fd4-4bcd-bb12-024633af8a40",

## GET List connections
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1connectionsListEndpointUrl

This Connections List Endpoint-call can be used to list connections.
HEADERS
Accept
application/json
x-mock-response-name
Mock List connections - OK


Example Request
List connections - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/get_api_response_links_connections"

Example Response
-

{
  "result": [
    {
      "state": "expired",
      "activeFrom": 1544686272000,
      "activeUntil": 1544693472000,
      "pid": "vjQK/rOw6CoSuWPZy6K93w==",
      "links": {
        "parent": "https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_dev2/7f4dd669-9381-40e1-8f6e-4c9904476d8a",
        "self": "https://dev2-user.testonly.digital-me.nl/user/connections/user/mgd_dev2/465571a1-d7e6-4d03-ae4b-f1a78b1463f3",
        "feeds": "https://dev2-user.testonly.digital-me.nl/user/mgd_dev2/connections/465571a1-d7e6-4d03-ae4b-f1a78b1463f3/feeds",

# Relations

tbd

# Subscriptions

tbd

# Messages
## POST Send message
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionMbox

This Mailbox Endpoint-call can be used to send a message over a connection with another Qiy User.
HEADERS
password
{{transportPassword}}
Content-Type
application/json
BODY raw

{
	"protocol": "https://example.com/qiy/node/message",
	"refSerialNr": -1,
	"text": "Hello world!",
	"payload": "SGVsbG8gV29ybGQh"
}



Example Request
Send message - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionMbox" \
  --header "password: {{transportPassword}}" \
  --header "Content-Type: application/json" \
  --data "{
    \"protocol\": \"https://example.com/qiy/node/message\",
    \"refSerialNr\": -1,
    \"text\": \"Hello world!\",
    \"payload\": \"SGVsbG8gV29ybGQh\"
}"

## GET List messages
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionMbox?since=0

This Mailbox Endpoint-call lists messages.
HEADERS
password
{{transportPassword}}
Accept
application/json
PARAMS
since
0


Example Request
List messages - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionMbox?since=0" \
  --header "password: {{transportPassword}}" \
  --header "Accept: application/json"

Example Response
200 - OK

{
  "result": [
    {
      "inbound": false,
      "payload": "eyJwdWJsaWNLZXkiOiJNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXU0cXNYMmlISzE0MzhXZjRCcGxiMjBqYXdjN0U3Mng0MTMwUW9QaE9MajByM0VSTi8wSmpjK3FoaU1QQVBEVCtTa1NQbmdGckN2RTRhR0pIOWIwdm8rWVkvcW1FbVFzdGw0d2s5cEFHTnVJdHh0TStab0RoTHdkRHBETTc0QkE4aFZ3cXJHQVA5UUovNktibFFLbXRPT09NY0tTUXB0RXNFQ3NFQytMZThpTkJhU2ozRnBMbWpHUWkxYjZXMG1UMU1aYzVFUjRTOFVmN2hkajhpS0JRc3hFcjdZUThqZ2FXdE1rakZOU0tZemt2Vi9zU3FtL2t0akh4Q21MUk5yRXdvaDBvZ1V1S1FEMnJuK1piWXovalBMWjRZOFd4Q3d2Wi9jVjFkMDc5Wk16S0hYWVBLT3J1RnJOWTZjZng5STRsckEyVHdsSXpOQVd5RHQzN1ZsQ2xEUUlEQVFBQiIsInBlcnNpc3RlbnRJZCI6ImxOMUxEN2lBSGZ2bDVvTWRCZ0k4VWc9PSIsInByb3RvY29scyI6WyJodHRwczovL3Byb3RvY29scy5xaXkubmwvaW52aXRlcy92LjEuMC4wIiwiaHR0cHM6Ly9wcm90b2NvbHMucWl5Lm5sL2NsZWFudXAvbWVzc2FnZXMvdi4xLjAuMCIsImh0dHBzOi8vcHJvdG9jb2xzLnFpeS5ubC9zdGF0ZS92LjEuMC4wIiwiaHR0cHM6Ly9naXRodWIuY29tL3FpeWZvdW5kYXRpb24vZmlLa3MvdHJlZS9tYXN0ZXIvc2NoZW1hL3YxIiwiaHR0cHM6Ly9wcm90b2NvbHMucWl5Lm5sL2RhdGEtcmVmZXJlbmNlL3BlZXIvdi4xLjAuMCIsImh0dHBzOi8vcHJvdG9jb2xzLnFpeS5ubC9yZWZlcmVuY2UtbWFuYWdlbWVudC8xLjAuMCJdLCJuYW1lIjoibWdkX2RldjIifQ==",
      "processed": false,
      "protocol": "https://protocols.qiy.nl/domain-details/v.1.0.0",
      "serialNr": 1,
      "sent": true,
      "text": "Our details"
    },

# Consents

tbd

# Feeds

## Relying Party

fiKks

Example of an encrypted PaymentsDueList:

<?xml version="1.0" encoding="UTF-8"?>
<!--Voorbeeld van een versleutelde openstaande factuur waarvan de vervaldatum nog niet is gepasseerd.-->
<!--Betaalwijze automatische incasso.-->
<xenc:EncryptedData xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" Type="http://www.w3.org/2001/04/xmlenc#Element">
  <xenc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
  <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#">
    <xenc:EncryptedKey xmlns:xenc="http://www.w3.org/2001/04/xmlenc#">
      <xenc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p"/>
      <xenc:CipherData>
        <xenc:CipherValue>ANlVWhxP62DScbyueRjY4LzHwL2xlL44hFfhbT0/qRtKCiSUgFwWigsewos7qHj6APsBjHv+AA8j&#13;
OP5cA8BO3w0oBquAqGxjFAfqKoAGWCWEZ29xKH6zIy7wRsyC8yO46Clljvgp27q9a9AhLEs5XfeF&#13;
g0eDb/73AWV/z+okzGQ=</xenc:CipherValue>
      </xenc:CipherData>
    </xenc:EncryptedKey>
  </ds:KeyInfo>
  <xenc:CipherData>
    <xenc:CipherValue>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</xenc:CipherValue>
  </xenc:CipherData>
</xenc:EncryptedData>

secret key: "secret_key123456" iv: "1234567890123456"

Input parameter before base64-encoding:

<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">
    <ds:KeyValue>
        <ds:RSAKeyValue>
            <ds:Modulus>6sNhgtNVksGD4ZK1rW2iiGO11O/BzEIZazovnMK37y3RVvvjmv1z44uA505gyyUTziCntHV9tONm&#13; 
                J11bH4koqqJQFZPXuKAyuu9eR3W/pZ4EGBMMIVH2aqSOsPMTI5K9l2YOW8fAoEZQtYVWsCrygOyc&#13;
                tBiamJZRJ+AKFZCIY5E=</ds:Modulus>
            <ds:Exponent>AQAB</ds:Exponent>
        </ds:RSAKeyValue>
    </ds:KeyValue> 
</ds:KeyInfo>

Decrypted xml:

<PaymentDueList xmlns="urn:qiyfoundation.org:names:fikks:schema:xsd:PaymentDueList" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:qiyfoundation.org:names:fikks:schema:xsd:PaymentDueList https://raw.githubusercontent.com/qiyfoundation/fiKks/master/schema/v1/xsd/PaymentDueList-1.0.xsd">
        <Invoice>
        <cbc:ID>1</cbc:ID>
        <cbc:IssueDate>2017-12-01</cbc:IssueDate>
        <cbc:Note>ZieZo zorgverzekering premie december 2017.</cbc:Note>
        <cbc:CurrencyCode>EUR</cbc:CurrencyCode>
        <cac:AccountingSupplierParty>
                <cac:Party>
                <cac:PartyIdentification>
                        <cbc:ID schemeAgencyID="NL" schemeAgencyName="KVK">06088185</cbc:ID>
</cac:PartyIdentification>
<cac:PartyName>
    <cbc:Name>Zilveren Kruis Zorgverzekeringen N.V.</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
                <cbc:StreetName>Postbus 444</cbc:StreetName>
                <cbc:CityName>Leiden</cbc:CityName>
                <cbc:PostalZone>2300AK</cbc:PostalZone>
                <cac:Country>
                <cbc:IdentificationCode>NL</cbc:IdentificationCode>
                <cbc:Name>Nederland</cbc:Name>
            </cac:Country>
        </cac:PostalAddress>
        <cac:PartyLegalEntity>
                <cbc:CompanyID>06088185</cbc:CompanyID>
        </cac:PartyLegalEntity>
        <cac:Contact>
                <cbc:Telephone>+31 71 751 00 52 </cbc:Telephone>
        </cac:Contact>
        </cac:Party>
    </cac:AccountingSupplierParty>
    <cac:PaymentMeans>
            <cbc:ID>1</cbc:ID>
            <cbc:PaymentMeansCode listID="UN/ECE 4461" listName="Payment Means" listURI="http://docs.oasis-open.org/ubl/os-UBL-2.0-update/cl/gc/default/PaymentMeansCode-2.0.gc">49</cbc:PaymentMeansCode>
            <cbc:PaymentDueDate>2017-12-15</cbc:PaymentDueDate>
            <cbc:InstructionNote>000123456789</cbc:InstructionNote>
            <cac:PayeeFinancialAccount>
            <cbc:ID schemeName="IBAN">NL51RABO0XXXXX678</cbc:ID>
            <cac:FinancialInstitutionBranch>
                    <cac:FinancialInstitution>
                    <cbc:ID schemeName="BIC">RABONL2U</cbc:ID>
            </cac:FinancialInstitution>
        </cac:FinancialInstitutionBranch>
        </cac:PayeeFinancialAccount>
    </cac:PaymentMeans>
    <cac:PaymentTerms>
            <cbc:ID>1</cbc:ID>
            <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
            <cbc:Note>Het factuuredrag wordt automatisch van uw rekening afgeschreven.</cbc:Note>
            <cbc:PaymentDueDate>2017-12-15</cbc:PaymentDueDate>
            <cac:SettlementPeriod>
            <cbc:StartDate>2017-12-10</cbc:StartDate>
            <cbc:EndDate>2017-12-15</cbc:EndDate>
        </cac:SettlementPeriod>
        <cac:ValidityPeriod>
                <cbc:EndDate>2017-12-31</cbc:EndDate>
        </cac:ValidityPeriod>
    </cac:PaymentTerms>
    <cac:LegalMonetaryTotal>
            <cbc:LineExtensionAmount currencyID="EUR">122.20</cbc:LineExtensionAmount>
            <cbc:TaxExclusiveAmount currencyID="EUR">122.20</cbc:TaxExclusiveAmount>
            <cbc:TaxInclusiveAmount currencyID="EUR">122.20</cbc:TaxInclusiveAmount>
            <cbc:PayableAmount currencyID="EUR">122.20</cbc:PayableAmount>
    </cac:LegalMonetaryTotal>
    </Invoice>
</PaymentDueList>

aes encrypted key in b64:

uE4BeFaIaBjoRQWUPdzzlhnVdQVsijVawcIkurMykWAMbc7rDx8iLACIHTv9uEuhm8MJCfgsMy7eTynpZaLxfYIeQ8FVMUVX3Am2Y9ytEXca3tKMQpw7MPcOX14XjOgvNT5Ld/PRG9j914+/rT5Sh00sE8xogxf2OH/5Urjzf7I=

public key:

MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDqw2GC01WSwYPhkrWtbaKIY7XU78HMQhlrOi+cwrfvLdFW++Oa/XPji4DnTmDLJRPOIKe0dX2042YnXVsfiSiqolAVk9e4oDK6715Hdb+lngQYEwwhUfZqpI6w8xMjkr2XZg5bx8CgRlC1hVawKvKA7Jy0GJqYllEn4AoVkIhjkQIDAQAB

public key - base64 encoded:

TUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FEcXcyR0MwMVdTd1lQaGtyV3RiYUtJWTdYVTc4SE1RaGxyT2krY3dyZnZMZEZXKytPYS9YUGppNERuVG1ETEpSUE9JS2UwZFgyMDQyWW5YVnNmaVNpcW9sQVZrOWU0b0RLNjcxNUhkYitsbmdRWUV3d2hVZlpxcEk2dzh4TWprcjJYWmc1Yng4Q2dSbEMxaFZhd0t2S0E3SnkwR0pxWWxsRW40QW9Wa0loamtRSURBUUFC

private key:

MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOrDYYLTVZLBg+GSta1toohjtdTvwcxCGWs6L5zCt+8t0Vb745r9c+OLgOdOYMslE84gp7R1fbTjZiddWx+JKKqiUBWT17igMrrvXkd1v6WeBBgTDCFR9mqkjrDzEyOSvZdmDlvHwKBGULWFVrAq8oDsnLQYmpiWUSfgChWQiGORAgMBAAECgYEA396xfjBJykj/mnxtA5UpCScMnqKEDGR8GOTDwpltDYiDuI873PEVMkg2BF2ZsB8LY+WAB3aDCZxQLfm4i7ogK8Py/UUnW4ZY98RFCGwVLxsWDoNgB5cEDbPomc1UmNALfO9DE10GD3uuLXuqHGy5wCVxvXEw1xdkocFPmIzsjgECQQD+345dPHMQXNG3G43FG3pkhImulSyQRk7tITdLT+eqoXNfie6ZVymFm+dpPBrp6BSsgdpSuzuuleZdM4De79hdAkEA680Q4UEV7GzsYIPzjrOGY9Dq9kwt0DCtxeLd+RrFQomrtxUg5GDkdbzlAi8x7sMxh5n8oNluLJDx68M0wdQ0xQJBAN6dMOGq3O2bxOjkPi29VGfbg85jKStS3bks2/kB790Pa5A1D5wLj47Nn5BBGVjYhsYuHR1JwFU7RJx/Ub5nS1kCQGC8Qf6G+v2BOf/mYhba43kzjhD485qDPeb+yV2Wc/J2FDIJwvKuJUt/8NtSjUOMZFdi/tbmHGLAG99Ct/QEoJkCQETBfCMVF4v5oOcI6kPlr2NEc5ipyEhiLnGEhTZEtY9q95UVscHO0AmnmoRtTIK5xsUtImIDXTN9R3xL1HSzzLw=

POST Access feed - fikks - encrypted
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/duePaymentsRpFeedsEndpointUrl/VHN1N3JwSTBVbXBCQ3IvYnFZT0J1bng4ZEF3PQ==
HEADERS
Accept
application/xml
Content-Type
application/xml
x-mock-response-name
Mock Access feed - fikks - encrypted - OK
BODY raw

<?xml version="1.0" encoding="UTF-8"?>
<ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:KeyValue>
        <ds:RSAKeyValue>
            <ds:Modulus>6sNhgtNVksGD4ZK1rW2iiGO11O/BzEIZazovnMK37y3RVvvjmv1z44uA505gyyUTziCntHV9tONmJ11bH4koqqJQFZPXuKAyuu9eR3W/pZ4EGBMMIVH2aqSOsPMTI5K9l2YOW8fAoEZQtYVWsCrygOyctBiamJZRJ+AKFZCIY5E=</ds:Modulus>
            <ds:Exponent>AQAB</ds:Exponent>
        </ds:RSAKeyValue>
    </ds:KeyValue>
</ds:KeyInfo>



Example Request
Access feed - fikks - encrypted - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/duePaymentsRpFeedsEndpointUrl/VHN1N3JwSTBVbXBCQ3IvYnFZT0J1bng4ZEF3PQ==" \
  --header "Content-Type: application/xml" \
  --header "Accept: application/xml" \
  --data "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\">
    <ds:KeyValue>
        <ds:RSAKeyValue>
            <ds:Modulus>6sNhgtNVksGD4ZK1rW2iiGO11O/BzEIZazovnMK37y3RVvvjmv1z44uA505gyyUTziCntHV9tONmJ11bH4koqqJQFZPXuKAyuu9eR3W/pZ4EGBMMIVH2aqSOsPMTI5K9l2YOW8fAoEZQtYVWsCrygOyctBiamJZRJ+AKFZCIY5E=</ds:Modulus>
            <ds:Exponent>AQAB</ds:Exponent>
        </ds:RSAKeyValue>
    </ds:KeyValue>
</ds:KeyInfo>"

Example Response
200 - OK

<?xml version="1.0" encoding="UTF-8"?>
<!--Voorbeeld van een versleutelde openstaande factuur waarvan de vervaldatum nog niet is gepasseerd.-->
<!--Betaalwijze automatische incasso.-->
<xenc:EncryptedData xmlns:xenc="http://www.w3.org/2001/04/xmlenc#" Type="http://www.w3.org/2001/04/xmlenc#Element">
  <xenc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
  <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#">
    <xenc:EncryptedKey xmlns:xenc="http://www.w3.org/2001/04/xmlenc#">
      <xenc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p"/>
      <xenc:CipherData>
        <xenc:CipherValue>ANlVWhxP62DScbyueRjY4LzHwL2xlL44hFfhbT0/qRtKCiSUgFwWigsewos7qHj6APsBjHv+AA8j&#13;
OP5cA8BO3w0oBquAqGxjFAfqKoAGWCWEZ29xKH6zIy7wRsyC8yO46Clljvgp27q9a9AhLEs5XfeF&#13;

POST Access feed - fikks - not encrypted
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/duePaymentsRpFeedsEndpointUrl/VHN1N3JwSTBVbXBCQ3IvYnFZT0J1bng4ZEF3PQ==
HEADERS
Accept
application/xml


Example Request
Access feed - fikks - not encrypted - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/duePaymentsRpFeedsEndpointUrl/VHN1N3JwSTBVbXBCQ3IvYnFZT0J1bng4ZEF3PQ==" \
  --header "Accept: application/xml"

Example Response
200 - OK

<?xml version="1.0" encoding="UTF-8"?>
<!-- speciale response... Deze is gewijzigd! En weer! -->
<!--Voorbeeld van een openstaande factuur waarvan de vervaldatum nog niet is gepasseerd.-->
<!--Betaalwijze automatische incasso.-->
<PaymentDueList xmlns="urn:qiyfoundation.org:names:fikks:schema:xsd:PaymentDueList"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="urn:qiyfoundation.org:names:fikks:schema:xsd:PaymentDueList https://raw.githubusercontent.com/qiyfoundation/fiKks/master/schema/v1/xsd/PaymentDueList-1.0.xsd"
	xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
	xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
	<Invoice>
		<cbc:ID>1</cbc:ID>

POST Request for feed
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionFeeds

A Relying Party uses this Connection Feeds Endpoint-call to request for a feed.

Optionally, a Feed Request Callback body parameter can be included in the 'input'-member of the body json object as a base64-encoded byte array.

When successfull this will end in a [Data Reference Received Event-v2][API Basics Events Data Reference Received Event-v2]. Failure will be either a HTTP error status code or a [Data Reference Failure Event][API Basics Events Data Reference Failure].
HEADERS
password
{{transportPassword}}
Content-Type
application/json
Accept
application/json
BODY raw

{
  "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
  "text": "Requesting feed.",
  "input": "Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig=="
}



Example Request
Request for feed - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionFeeds" \
  --header "password: {{transportPassword}}" \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --data "{
  \"protocol\": \"https://github.com/qiyfoundation/fiKks/tree/master/schema/v1\",
  \"text\": \"Requesting feed.\",
  \"input\": \"Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig==\"
}"

Example Response
201 - Created

{
  "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
  "feedId": "3J2UVSFIAH6X77HXR4MVHBVNG46GWT3M"
}

POST Data Reference Received-v2 Callback
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1dataReferenceReceivedv2CallbackUrl?

A Relying Party can use this Data Reference Received-v2-callback on the Data Reference Received-v2 Endpoint to receive new feed id's.
PARAMS
BODY raw

{
  "type": "DATA_REFERENCE_RECEIVED2",
  "connectionUrl": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionUrl",
  "extraData": {
    "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
    "value": "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ=="
  }
}



Example Request
Data Reference Received-v2 Callback - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1dataReferenceReceivedv2CallbackUrl" \
  --header "Content-Type: application/json" \
  --data "{
  \"type\": \"DATA_REFERENCE_RECEIVED2\",
  \"connectionUrl\": \"https://dev1-user.testonly.digital-me.nl/user/connections/user/pqc_test_d4_relying_party/a646bcd3-a844-4774-8068-55ea8b4b2669\",
  \"extraData\": {
    \"protocol\": \"https://github.com/qiyfoundation/fiKks/tree/master/schema/v1\",
    \"value\": \"SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==\"
  }
}"

GET Data Reference Received-v2 Event
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1eventsEndpointUrl

A Relying Party can use the [Data Reference Received Event-v2][API Basics Events Data Reference Received Event-v2] to detect a new feed.
HEADERS
Accept
text/event-stream


Example Request
Data Reference Received Event-v2 - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1eventsEndpointUrl" \
  --header "Accept: text/event-stream"

Example Response
-


event: DATA_REFERENCE_RECEIVED2 data: {
    "type": "DATA_REFERENCE_RECEIVED2",
    "connectionUrl": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid1sp1connectionUrl",
    "extraData": {
        "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
        "value": "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ=="
    }
}

POST Access feed
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1feedsEndpointUrl/SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==

A Relying Party uses this Feeds Endpoint-call to access a single feed.

The body may include operation request parameters encoded as a base-64 encoded byte array as described in the Qiy Scheme change proposal on free parameters.
HEADERS
Content-Type
text/plain
BODY raw

Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig==



Example Request
Access feed - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1feedsEndpointUrl/SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==" \
  --header "Content-Type: text/plain" \
  --data "Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig=="

Example Response
200 - OK

{
  "activities-heart": [
    {
      "customHeartRateZones": [],
      "dateTime": "today",
      "heartRateZones": [
        {
          "caloriesOut": 138.8351,
          "max": 86,
          "min": 30,
          "minutes": 65,

POST Access feeds
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1feedsEndpointUrl

A Relying Party can use this Feeds Endpoint-call to access one or more feeds.

The json body may include 'input'-members for operation request parameters encoded as a base-64 encoded byte array as described in the Qiy Scheme change proposal on free parameters.

When successfull, the data is returned in the response of the body in a format as this:

{ "{{feed_id1}}": { "content-type": "application/xml", "output": "" }, "{{feed_id2}}": { "content-type": "application/json", "output": "" } }
HEADERS
Content-Type
application/json
Accept
application/json
BODY raw

{
	"{{feed_id1}}": {
		"input": "<optional json member with base-64 encrypted byte array>"
	},
	"{{feed_id2}}": {
		"input": "<optional json member with base-64 encrypted byte array>"
	}
}



Example Request
Access feeds

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/sp1feedsEndpointUrl" \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --data "{
	\"{{feed_id1}}\": {
		\"input\": \"<optional json member with base-64 encrypted byte array>\"
	},
	\"{{feed_id2}}\": {
		\"input\": \"<optional json member with base-64 encrypted byte array>\"
	}
}"

GET List feed id's
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl?operation=https://github.com/qiyfoundation/fiKks/tree/master/schema/v1

This Feeds Endpoint-request can be used to list the feed's with feed details of a Qiy Node or a connection for all or a set of protocols (operation types).
HEADERS
Accept
application/json
PARAMS
operation
https://github.com/qiyfoundation/fiKks/tree/master/schema/v1

This parameter can be provided more then once.



Example Request
List feed id's

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl" \
  --header "Accept: application/json"

Example Response
200 - OK

{
  "QZJ5MOWNEXARVTTBWMYZAO7ISYOQQOAU": {
    "connection": "https://dev2-user.testonly.digital-me.nl/user/connections/user/fp_rp_dev2/43c5c576-c0d0-4fdd-8593-a57dacdb1a2f",
    "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
    "lastUpdated": 1565083591687,
    "created": 1565083591605,
    "status": "Created"
  },
  "CE22UFPUKSW77IA26A2OKHVKEA3RU6ES": {
    "connection": "https://dev2-user.testonly.digital-me.nl/user/connections/user/fp_rp_dev2/43c5c576-c0d0-4fdd-8593-a57dacdb1a2f",
    "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",

## Data Provider
POST Feed Request Callback
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/dp1serviceEndpointUrl

A Data Provider receives this Service Endpoint-callback when an Individual has set him as the source of a feed.
HEADERS
Content-Type
application/json
Accept
application/json
BODY raw

{
  "connection": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid3dp1connectionUrl",
  "pid": "1IqX94/EoOcD47hCvBQ+gi==",
  "message": {
    "serialNr": 6,
    "text": "Requesting 'test data'",
    "protocol": "https://github.com/qiyfoundation/fiKks/tree/master/schema/v1",
    "inbound": true,
    "sent": false,
    "thirdPartyRef": " 4D0OqePJ1yKD41Q9qmixVnVFLWcJHFT1hhKDKG9FmeI="
  },
  "mbox": "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/pid3dp1connectionMbox"
}



Example Request
Feed Request Callback - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/dp1serviceEndpointUrl" \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --data "{
  \"connection\": \"https://dev1-user.testonly.digital-me.nl/user/connections/user/96cd5389-6def-4f6f-b3a9-b613a66ec522/ad4ac9cb-62e1-43ad-8495-9ac426b229c2\",
  \"pid\": \"G5grIomOi7aBEV9nYE5Vlg==\",
  \"message\": {
    \"serialNr\": 6,
    \"text\": \"Requesting 'test data'\",
    \"protocol\": \"https://github.com/qiyfoundation/fiKks/tree/master/schema/v1\",
    \"inbound\": true,
    \"sent\": false,
    \"thirdPartyRef\": \"4D0OqePJ1yKD41Q9qmixVnVFLWcJHFT1hhKDKG9FmeI=\"
  },
  \"mbox\": \"https://dev1-user.testonly.digital-me.nl/user/mbox/user/96cd5389-6def-4f6f-b3a9-b613a66ec522/ad4ac9cb-62e1-43ad-8495-9ac426b229c2\"
}"

Example Response
-

{
  "id": "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ=="
}

POST Access feed callback
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/dp1serviceEndpointUrl/resolve

A Data Provider receives this Service Endpoint-callback after an access feed-request.
HEADERS
Content-Type
application/json
Accept
application/json
BODY raw

{
	"SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==": {
		"input": "Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig=="
	}
}



Example Request
Access feed callback - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/dp1serviceEndpointUrl/resolve" \
  --header "Content-Type: application/json" \
  --data "{
	\"SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==\": {
		\"input\": \"Im9wdGlvbmFsIG9wZXJhdGlvbiBib2R5IGVuY29kZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBieXRlIGFycmF5Ig==\"
	}
}"

Example Response
200 - OK

{
    "SjF1RFBNam14RmxEcW8rOVdzNkpHd1RZaFdBPQ==": {
        "output": "{
    "activities-heart": [
        {
            "customHeartRateZones": [],
            "dateTime": "today",
            "heartRateZones": [
                {
                    "caloriesOut": 138.8351,
                    "max": 86,

## Individual
GET User Action Message Event
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1eventsEndpointUrl

An End User App can use the User Action Message Event to detect the receipt of a feed request.
HEADERS
Accept
text/event-stream
x-mock-response-name
Mock User Action Message Event - OK


Example Request
User Action Message Event - OK

curl --location --request GET "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1eventsEndpointUrl" \
  --header "Accept: text/event-stream"

Example Response
-

event: USER_ACTION_MESSAGE data: {
   'type': 'USER_ACTION_MESSAGE',
   'connectionUrl': 'https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e',
   'extraData': 'https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4'
}

GET Get user action message
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1action1messageUrl

A Qiy Node Client can use this call to get the details of a received message that requires user interaction using a userActionMessageUrl extracted from a User Action Message Event.
HEADERS
Accept
application/json


Example Request
200 OK

curl --location --request GET "{{actionMessageUrl}}" \
  --header "Accept: application/json"

Example Response
200 - OK

{
  "result": [
    {
      "connection": "https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e",
      "created": 1562059030644,
      "links": {
        "self": "https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4",
        "handle": "https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/handle/wip_feed_ind/4/e33b7dcc-a1f1-4195-893d-97698f0e4d8e"
      },
      "message": {
        "serialNr": 5,

POST Set feed
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1action1option1url

An End User App uses this call to set a Data Provider as the source for a feed request.


Example Request
Set feed - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1action1option1url"

PUT Add feed
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1action1option1url

An End User App uses this call to add a Data Provider as a source for a feed request.


Example Request
Add feed - OK

curl --location --request PUT "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/in1action1option1url"

# End-to-end encryption (draft)
## POST Request for feed
{{connectionFeedsEndpointUrl}}

tbd
HEADERS
password
{{transportPassword}}
BODY raw

{
  "protocol": https://github.com/qiyfoundation/fiKks/tree/master/schema/v1,
  "text": "Requesting feed.",
  "input": "<optional json member for Feed Request Callback body parameter; a base64 encoded byte array>"
}



Example Request
Request for feed

curl --location --request POST "{{connectionFeedsEndpointUrl}}" \
  --header "password: {{transportPassword}}" \
  --data "{
  \"protocol\": https://github.com/qiyfoundation/fiKks/tree/master/schema/v1,
  \"text\": \"Requesting feed.\",
  \"input\": \"<optional json member for Feed Request Callback body parameter; a base64 encoded byte array>\"
}"

## POST Access feed
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl/{{feed_id}}

tbd
BODY raw

"<optional operation parameter(s) encoded as a base64 encoded byte array>"



Example Request
Access feed - OK

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl{{feed_id}}"

Example Response
200 - OK

{
  "activities-heart": [
    {
      "customHeartRateZones": [],
      "dateTime": "today",
      "heartRateZones": [
        {
          "caloriesOut": 138.8351,
          "max": 86,
          "min": 30,
          "minutes": 65,

## POST Access feeds
https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl

tbd
HEADERS
Content-Type
application/json
BODY raw

{
	"{{feed_id1}}": {
		"input": "<optional json member with base-64 encrypted byte array>"
	},
	"{{feed_id2}}": {
		"input": "<optional json member with base-64 encrypted byte array>"
	}
}



Example Request
Access feeds

curl --location --request POST "https://4b86023e-8e5e-4c82-a844-ffe548890819.mock.pstmn.io/feedsEndpointUrl" \
  --header "Content-Type: application/json" \
  --data "{
	\"{{feed_id1}}\": {
		\"input\": \"<optional json member with base-64 encrypted byte array>\"
	},
	\"{{feed_id2}}\": {
		\"input\": \"<optional json member with base-64 encrypted byte array>\"
	}
}"

# Getting help

Please contact the [Service Desk](#service-desk).

