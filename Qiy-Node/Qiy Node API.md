# Qiy Node API

This document describes the [Qiy Node][Definitions Qiy Node] API - the API that is to be provided by [Qiy Node Implementations][Definitions Qiy Node Implementation].

# API Basics

## Registration

[Service Providers][Definitions Service Provider] and [Application Providers][Definitions Application Provider] can register with an [Access Provider][Definitions Access Provider]:

* both receive an [API Key][Definitions API Key]
* [Service Providers][Definitions Service Provider] can whitelist endpoints and receive a [Qiy Node Credential][Definitions Qiy Node Credential].

## Service Desk

Please contact the Service Desk of your [Access Provider][Definitions Access Provider] for your requests. The Service Desk of the [Access Provider][Definitions Access Provider] DigitalMe is available during regular CE(S)T office hours and can be contacted by e-mail or phone:

    service@digital-me.nl
    +31 (0) 411-616565

## Versions

The api is versioned using Semantic Versioning 2.0.0 and follows this specification. 
The version of the api described in the Qiy Node API, this document, is the same as the version of the [Qiy Scheme][Definitions Qiy Scheme] that it is part of.

In addition, the following rules apply for [Qiy Node Implementations][Definitions Qiy Node Implementation]:

    Two major versions must be supported in the production environment: one primary version and one secondary version.
    The major versions should be supported in an acceptance environment.
    The secondary version must be supported for at least 6 months.
    One development version may be supported in a development environment.
    The development version may change at any time.

The version of the api that is supported must be returned by [Get api info][API Get Api].

## Authentication

### App Authentication

Qiy Applications are required to authenticate requests using an [API Key][Definitions API Key] implemented using basic authentication.

An e-mail address provided by the application provider will be used to maintain the [API Keys][Definitions API Key]. Please use this e-mail address to e-mail the [Service Desk](#service-desk) your [API Key][Definitions API Key] request.

### User Authentication

All requests but the request to create a Qiy Node and the Api Request MUST be user authenticated using a signed token that can only be calculated using a [Qiy Node Credential][Definitions Qiy Node Credential].

The token MUST be passed in the 'Authorization-node-QTN'-header parameter.

#### Python

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

#### Bash

The authorization header parameter can be generated with this Bass script:

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

### Transport Authentication

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

This endpoint is deprecated.

### References Endpoint

This endpoint is deprecated.

### Self Endpoint

This endpoint can be used to delete a Qiy Node. The endpoint address is returned in the 'self'-property of Get endpoint addresses.

### Service Catalogue Endpoint

This endpoint can be used to get or set the contents of a Service Catalogue. The current address of the endpoint is returned in the "serviceCatalog"-member of the response of Get endpoint addresses.

## Servers

The Qiy Node service runs in a a development environment, the acceptance environment and the production environment. The server urls are:

| DTAP environment | Server url                                    |
| ---------------- | --------------------------------------------- |
| Dev2             | https://dev2-user.testonly.digital-me.nl/user |
| Acceptance       | https://user.dolden.net/user                  |
    

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

```
event: USER_ACTION_MESSAGE data: {
   'type': 'USER_ACTION_MESSAGE',
   'connectionUrl': 'https://dev1-user.testonly.digital-me.nl/user/connections/user/wip_feed_ind/e33b7dcc-a1f1-4195-893d-97698f0e4d8e',
   'extraData': 'https://dev1-user.testonly.digital-me.nl/user/mbox/user/action/wip_feed_ind?amid=4'
}
```

## Documentation

#### Setup

An End User App can only access the Qiy Trust Network under the following preconditions:

    The End User App uses a valid Access Provider Token.
    The End User App correctly authenticates Qiy Node requests.
    The End User App must allow End Users to use a new Qiy Node or reuse an existing one.

#### Subscribe

An Individual can subscribe to a service as follows:

    Conclude an subscription agreement (out-of-scope).
    Connect with the [Service Provider][Definitions Service Provider].

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

Before a [Service Provider][Definitions Service Provider] can provide services via Qiy he has to make the following preparations:

    Describe the services and make these descriptions publicly available.
    Setup a State Handled Endpoint.
    (only for Data Providers:) Setup Service Endpoint(s).
    (only for Relying Parties:) Setup Data Reference Received-v2 Endpoint.
    Prepare the Computer systems to correctly produce authenticated requests.
    Contact the [Access Provider][Definitions Access Provider] DigitalMe to whitelist the endpoints and receive a [Qiy Node Credential][Definitions Qiy Node Credential] and an [API Key][Definitions API Key].
    Configure the computer system for the Qiy Node.
    Publish the Service Catalogue with Qiy.

##### Service Catalogue

A [Service Provider][Definitions Service Provider] publishes the (data) service types it supports in his Service Catalogue, which consists of an array of urls for Service Type Descriptions with additional details, for example for the associated [Feed Request Endpoints][API Basics Documentation Service Provider Setup Endpoints Feed Request Endpoint], see Get service catalogue.

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

##### Settings

A Qiy Node can have diferent settings which can be maintained with the get and set node setting calls.

##### Qiy Node Credential

A Qiy Node credential consists of:

    A Qiy Node Id
    An RSA key pair
    A Transport Password

* Qiy Node Primary Key

One element of the [Qiy Node Credential][Definitions Qiy Node Credential] is the primary key.

* Python

In Python, the primary key can be created with the package 'cryptography'. The key can be created and persisted as follows:

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

* Qiy Node Public Key

In python, the public key can be obtained using the package 'pyOpenSSL'. Given the pem-file, this goes as follows:

```
import OpenSSL

with open("data/"+target_short_node_id+".pem" , "r") as f:
    buffer = f.read()
private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, buffer)
public_key=OpenSSL.crypto.dump_publickey(
    OpenSSL.crypto.FILETYPE_ASN1,
    private_key)
```

#### Connections

Individuals can connect and interact with other Individuals and [Service Providers][Definitions Service Provider] using connections between the related Qiy Nodes.

Connections can be created between an invitor and an invitee using Connect Tokens as follows:

    The invitor [requests][Connections Request connect token] or creates and [registers][Connections Register connect token] a Connect Token.
    The invitor invites the invitee to connect with the Connect Token out-of-band.
    The invitee [requests a connection using the connect token][Connections Request connection].
    The invitor receives a [State Handled Callback][Connections State Handled Callback] notifying that the connect token has been used to create a connection.
    The invitee receives a [State Handled Event][Connections State Handled Event] notifying that the connection has been established.

#### Connect Tokens

A Connect Token can be used to create connections between Qiy Users, for example an Individual and a [Service Provider][Definitions Service Provider]. The connect token may be created by either of the two, but when connecting to a [Service Provider][Definitions Service Provider] it must always be [registered][Connections Register connect token] or otherwise [requested][Connections Request connect token] by the [Service Provider][Definitions Service Provider].

##### Create Connect Token

A Connect Token is a json-object with three members which can be created as follows:

    id: This is a label and can be any string.
    target: The format of this member is returned in the "target-template"-member of the response of Get endpoint addresses, where '~id~' should be a uuid.
    tmpSecret: This member is a string: an array of 16 random bytes which is base64-encoded.

In Java the tmpSecret can be generated as follows:

```
SecureRandom RANDOM = new SecureRandom();
byte[] tmpSecret = new byte[16];
RANDOM.nextBytes(tmpSecret);
String tmpSecretString = Base64.getEncoder().encodeToString(tmpSecret);
```

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

## Api info

An [app authenticated][API Basics Authentication App Authentication] [GET /api][API Get Api] can be used to get the [api version][API Basics Versions] and the current address of the [Node Create Endpoint][API Basics Dynamic Endpoint Addresses Node Create Endpoint].

# Nodes

## Request creation of Qiy Node

This Node Create Endpoint-call can be used to request the creation of a Qiy Node.


## Get endpoint addresses

A [user authenticated][API Basics Authentication User Authentication] [GET /api][API Get Api] can be used to get the [current addresses of the dynamic path endpoints][API Basics Dynamic Endpoint Addresses].


## Set event callback endpoints

This Event Callbacks Endpoint-request can be used to define the addresses of the event callback endpoints.


## Get event callback endpoints

This Event Callbacks Endpoint-request can be used to get the addresses of the event callback endpoints.


## Start listening to events

This Events Endpoint-call can be used to start listening to Qiy Node events.

It starts a long-living session with a heartbeat to keep the response open. Every 10 seconds a 'ping' comment will be sent. If this is not received for more than that time, something has gone wrong.


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


# Relations

tbd

# Subscriptions

tbd

# Messages

## Send message

This Mailbox Endpoint-call can be used to send a message over a connection with another Qiy User.


## List messages

This Mailbox Endpoint-call lists messages.


# Consents

tbd

# Feeds

## Relying Party

### fiKks

Example of an encrypted PaymentsDueList:

```
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
```

secret key: "secret_key123456" iv: "1234567890123456"

Input parameter before base64-encoding:

```
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
```

Decrypted xml:

```
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
```

aes encrypted key in b64:

```
uE4BeFaIaBjoRQWUPdzzlhnVdQVsijVawcIkurMykWAMbc7rDx8iLACIHTv9uEuhm8MJCfgsMy7eTynpZaLxfYIeQ8FVMUVX3Am2Y9ytEXca3tKMQpw7MPcOX14XjOgvNT5Ld/PRG9j914+/rT5Sh00sE8xogxf2OH/5Urjzf7I=
```

public key:

```
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDqw2GC01WSwYPhkrWtbaKIY7XU78HMQhlrOi+cwrfvLdFW++Oa/XPji4DnTmDLJRPOIKe0dX2042YnXVsfiSiqolAVk9e4oDK6715Hdb+lngQYEwwhUfZqpI6w8xMjkr2XZg5bx8CgRlC1hVawKvKA7Jy0GJqYllEn4AoVkIhjkQIDAQAB
```

public key - base64 encoded:

```
TUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FEcXcyR0MwMVdTd1lQaGtyV3RiYUtJWTdYVTc4SE1RaGxyT2krY3dyZnZMZEZXKytPYS9YUGppNERuVG1ETEpSUE9JS2UwZFgyMDQyWW5YVnNmaVNpcW9sQVZrOWU0b0RLNjcxNUhkYitsbmdRWUV3d2hVZlpxcEk2dzh4TWprcjJYWmc1Yng4Q2dSbEMxaFZhd0t2S0E3SnkwR0pxWWxsRW40QW9Wa0loamtRSURBUUFC
```

private key:

```
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOrDYYLTVZLBg+GSta1toohjtdTvwcxCGWs6L5zCt+8t0Vb745r9c+OLgOdOYMslE84gp7R1fbTjZiddWx+JKKqiUBWT17igMrrvXkd1v6WeBBgTDCFR9mqkjrDzEyOSvZdmDlvHwKBGULWFVrAq8oDsnLQYmpiWUSfgChWQiGORAgMBAAECgYEA396xfjBJykj/mnxtA5UpCScMnqKEDGR8GOTDwpltDYiDuI873PEVMkg2BF2ZsB8LY+WAB3aDCZxQLfm4i7ogK8Py/UUnW4ZY98RFCGwVLxsWDoNgB5cEDbPomc1UmNALfO9DE10GD3uuLXuqHGy5wCVxvXEw1xdkocFPmIzsjgECQQD+345dPHMQXNG3G43FG3pkhImulSyQRk7tITdLT+eqoXNfie6ZVymFm+dpPBrp6BSsgdpSuzuuleZdM4De79hdAkEA680Q4UEV7GzsYIPzjrOGY9Dq9kwt0DCtxeLd+RrFQomrtxUg5GDkdbzlAi8x7sMxh5n8oNluLJDx68M0wdQ0xQJBAN6dMOGq3O2bxOjkPi29VGfbg85jKStS3bks2/kB790Pa5A1D5wLj47Nn5BBGVjYhsYuHR1JwFU7RJx/Ub5nS1kCQGC8Qf6G+v2BOf/mYhba43kzjhD485qDPeb+yV2Wc/J2FDIJwvKuJUt/8NtSjUOMZFdi/tbmHGLAG99Ct/QEoJkCQETBfCMVF4v5oOcI6kPlr2NEc5ipyEhiLnGEhTZEtY9q95UVscHO0AmnmoRtTIK5xsUtImIDXTN9R3xL1HSzzLw=
```

#### Access feed - fikks - encrypted

tbd

#### Access feed - fikks - not encrypted

tbd

### Request for feed

A Relying Party uses this Connection Feeds Endpoint-call to request for a feed.

Optionally, a Feed Request Callback body parameter can be included in the 'input'-member of the body json object as a base64-encoded byte array.


### Data Reference Received-v2 Callback

A Relying Party can use this Data Reference Received-v2-callback on the Data Reference Received-v2 Endpoint to receive new feed id's.


### Data Reference Received-v2 Event

A Relying Party can use the [Data Reference Received Event-v2][API Basics Events Data Reference Received Event-v2] to detect a new feed.

### Access feed

A Relying Party uses this Feeds Endpoint-call to access a single feed.

The body may include operation request parameters encoded as a base-64 encoded byte array as described in the Qiy Scheme change proposal on free parameters.


### Access feeds

A Relying Party can use this Feeds Endpoint-call to access one or more feeds.


### List feeds

This Feeds Endpoint-request can be used to list the feed's with feed details of a Qiy Node or a connection for all or a set of protocols (operation types).


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


# Getting help

Please contact the [Service Desk](#service-desk).


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
[Nodes]: https://qiy.api.digital-me.nl/?version=latest#62279de6-0df7-497a-9a1e-cddc17bbbc63
[Nodes Request creation of Qiy Node]: https://qiy.api.digital-me.nl/?version=latest#806d07bb-f6eb-47f8-bc07-71119440fc0d
[Nodes Get endpoint addresses]: https://qiy.api.digital-me.nl/?version=latest#0bdb3ea3-0e8c-4f6d-8a92-8230d1be9a02
[Nodes Set event callback endpoints]: https://qiy.api.digital-me.nl/?version=latest#2887a3e0-5e5c-40ea-83b7-e40ce6cf5333
[Nodes Get event callback endpoints]: https://qiy.api.digital-me.nl/?version=latest#d0750a63-eee1-41ef-b093-ad0ef8c720e3
[Nodes Start listening to events]: https://qiy.api.digital-me.nl/?version=latest#abd171d1-4aee-4e8c-a599-00914f277d62
[Nodes Get node settings]: https://qiy.api.digital-me.nl/?version=latest#7bb9f259-c23d-4038-8cba-237671b167a7
[Nodes Set node settings]: https://qiy.api.digital-me.nl/?version=latest#07e66599-8dff-4ed4-9a9f-4773fb5515d7
[Nodes Delete Qiy Node]: https://qiy.api.digital-me.nl/?version=latest#5c60f3f0-ea95-40f7-9487-3664d9a4b293
[Services]: https://qiy.api.digital-me.nl/?version=latest#ab572b83-bd18-4a8e-85be-b549a0ac6758
[Services Get service catalogue]: https://qiy.api.digital-me.nl/?version=latest#91f6b195-9c43-4c95-9618-57631714343b
[Services Set service catalogue]: https://qiy.api.digital-me.nl/?version=latest#d29ddd91-cdcf-48af-abe4-42cd6d54694b
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
[Definitions Access Provider]: ../Definitions.md#access-provider
[Definitions API Key]: #app-authentication
[Definitions Application Provider]: ../Definitions.md#application-provider
[Definitions Service Provider]: ../Definitions.md#service-provider
[Definitions Qiy Node]: ../Definitions.md#qiy-node
[Definitions Qiy Node Credential]: #qiy-node-credential
[Definitions Qiy Node Implementation]: ../Definitions.md#qiy-node-implementation
[Definitions Qiy Scheme]: ../Definitions.md#qiy-scheme
[Relations]: https://qiy.api.digital-me.nl/?version=latest#4f4c5a3e-388c-48ff-b847-6c11c3738254
[Subscriptions]: https://qiy.api.digital-me.nl/?version=latest#ec0ab04d-ab6e-4a9c-9b45-e6b75b583bff
[Messages]: https://qiy.api.digital-me.nl/?version=latest#b0169810-fd5c-4422-95a1-0beb2fc77a3e
[Messages Send message]: https://qiy.api.digital-me.nl/?version=latest#a58badea-0b4c-4c85-8254-96bab05892fa
[Messages List messages]: https://qiy.api.digital-me.nl/?version=latest#45ada0ae-c416-4348-81b1-44f7b2a9e44f
[Consents]: https://qiy.api.digital-me.nl/?version=latest#3f42e884-3ffa-4387-8896-05e7226d5a9f
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
[Getting help]: https://qiy.api.digital-me.nl/?version=latest#9acb0133-e012-4f49-a1e9-51283b8402c9
