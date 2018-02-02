# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From Qiy Nodes to data exchange


# Contents
${toc}

# 1 Introduction
Qiy, or rather: the [Qiy Scheme], puts people back in control of their [Personal Data] while creating value for organizations that process it ([Relying Parties]).


## 1.1 Purpose

The document is aimed at people who know that Qiy puts people back in control of their [Personal Data], but who want or need to know the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.

## 1.2 Reader guidance

* Privacy officers are advised to read chapter [3 Architectural Description](#3 Architectural Description) and especially [section 3.2](#3.2 Privacy).
* Security officers are advised to read chapter [3 Architectural Description](#3 Architectural Description) and especially [section 3.3](#3.3 Privacy).
* Information analysts are advised to read chapters [3 Architectural Description](#3 Architectural Description), [4 The User layer](#4-the-user-layer) and [5 The Application layer](#5 The Application layer).
* Application developers are advised to read chapters [3 Architectural Description](#3 Architectural Description), [4 The User layer](#4-the-user-layer), [5 The Application layer](#5 The Application layer) and [6 The Qiy Node layer](#6 The Qiy Node layer).
* Systems engineers are advised to read chapters [3 Architectural Description](#3 Architectural Description), [8 The Transport Layer](#8 The Transport Layer) and [9 The Carrier Layer](#9 The Carrier Layer).

# 2 Overview

This chapter gives an overview of this document.
* [2.1 Data Reuse](#2.1 Data Reuse) describes how data can be reused with Qiy.
* [3 Architectural Description](#3 Architectural Description) describes the [Architectural Layers](#2.2 Architectural Layers) and addresses various concerns like privacy and security.
* [4 The User Layer](#4 The User Layer) describes the setup and processes of the data reuse at the user level.
* [5 The Application Layer](#5 The Application Layer) describes the processes at the application level.
* [6 The Qiy Node Layer](#6 The Qiy Node Layer) describes the same at the Qiy Node level.
* [7 The Service Layer](#7 The Service Layer) describes the [Service Layer] support.
* [8 The Transport Layer](#8 The Transpor Layer) describes the [Transport Layer] support.
* [9 The Carrier Layer](#9 The Carrier Layer) describes the [Carrier Layer] support.
* [10 Definitions](#10 Definitions) contains the definitions used in this document.
* [11 Diagram sources](#11 Diagram Sources) contains the source code used to generate the diagrams.

## 2.1 Data Reuse

This document describes a scenario in which a [Data Subject] ([Individual]) can reuse his [Personal Data] stored at one organization ([Data Provider]) and provide it to another organization ([Relying Party]) to consume one of its services.

The Data Reuse scenario is more complex and may require less user interaction, but in essence it goes as follows:
* The Individual subscribes to a service.
* The Relying Party asks the Individual for the data it needs to provide the service.
* The Individual retrieves the data from a Data Provider.
* The Individual routes the data to the Relying Party.

![Qiy Data Reuse](./images/Qiy Data Reuse.png)

### 2.1.1 Privacy concern

The Data Reuse process shows that the data is transferred to the Relying Party by choice of the Individual.
This breaks the chain of responsibility for the Data Provider; the responsibility for correct processing of the data does not extend to any processing that takes place after the handover to the Individual. 

# 3 Architectural Description

This chapter describes the major entities of Qiy and their relations with the help of the [Architectural Layers of the Qiy Scheme] and addresses how Qiy addresses concerns like security and privacy.

## 3.1 Architectural Layers
The realization of the scenario is described using the following layers:

![Layers](./images/layers.png)

## 3.2 Privacy

Qiy has been conceived with the aim to put people back in control of their [Personal Data], hence making privacy the primary concern of Qiy.
The aim has been elaborated in a set of principles called the [Qiy Trust Principles] and technical, legal and governance rules, all of which are maintained by the [Qiy Foundation] and the [Qiy Foundation Members].

The realization of the [Data Reuse] as described in this document demonstrates that a natural person ([Individual]) is in control:
* The [Individual] can securily exchange data and/or messages with another person or organization ([Qiy User]) via Qiy, using connections, see [4 The User Layer](#4 The User Layer).
* The [Individual] controls what [Qiy Users] he connects with and, in principle, when he wants to end it.
* When an [Individual] connects with a [Qiy User] that is providing a [Service] via Qiy ([Service Providing User]), the [Individual] is provided with the identity of the latter, but not the other way around.
* The [Individual] can access his [Personal Data] that is kept by another [Qiy User]([Data Provider] as a result of the [Access Principle], one of the [Qiy Trust Principles].
* The [Individual] controls what data he shares with what service provider ([Relying Party]) and under what terms using proveable [Consents].
* [Qiy Users] use applications that are authorized for use with Qiy ([Qiy Applications]).
* Access to Qiy, data exchange via Qiy, consent services and potentially [Qiy Nodes] are provided by [Access Providers].


All parties involved are bound by the rules of the [Qiy Scheme]:
* [Service Providing Users] are bound by the [Binding Individual Rights] and the [Binding Principles for Relying Parties and Data Providers].
* [Access Providers] are bound by the [Licence Agreement Issuer] or the [Licence Agreement Service Provider].
* [Application Providers] can only develop and produce [Qiy Application]-services and/or software with a [Licence Agreement Application Provider].

## 3.3 Security

As described above, privacy is at the heart of Qiy and security being a 'conditio sine qua no' for this, it is also addressed by the rules of the [Qiy Scheme].

## 3.4 Interoperability

An [Individual] can only control his [Personal Data], when all concerned systems are interoperable.
This is achieved as follows:
* Applications exchange data and/or messages via Qiy using open standards of the [Qiy Scheme] ([Qiy Open Standard]).
* Applications exchange described data using [Data Descriptions] which are available to all concerned parties.

## 3.5 Governance

The governance rules are laid down in the [Governance Model for the Qiy Scheme], one of the documents of the [Qiy Scheme Rulebook].

## 3.6 Compliancy

The compliancy rules for [Service Providing Users] can be found in the [Binding Principles for Relying Parties and Data Providers], one of the documents of the [Qiy Scheme Rulebook].


# 4 The User layer
This chapter describes the User layer and the interaction between the [Relying Party], [Individual], [Data Provider] and the lower layers for the [Data Reuse].

## 4.1 Qiy Users
The organizations and/or persons using Qiy are called [Qiy Users]. They can use Qiy in different [roles]; they can use Qiy as a [Relying Party], [Individual], [Data Provider] or a combination of these.
A business for example will generally use Qiy both as a [Relying Party] (for offering [Services] using reliable [Personal Data]) and as a [Data Provider] (as a source of [Personal Data]).
As for natural persons, most of these will use Qiy as an [Individual] to control their [Personal Data].

## 4.2 Service Providing User
A [Qiy User] that provides one or more [Services] to [Individuals] is said to be (or act in the [Business Role] of) '[Service Providing Users]'.
Any [Qiy User] acting in one or both of the roles [Relying Party] or [Data Provider] is implicitely acting in this role.

## 4.3 Qiy Node
A [Qiy User] must have a [Qiy Node]. 
[Service Providing Users] can acquire one from an [Access Provider].
[Individuals] obtain a [Qiy Node] the first time they use a [Qiy Application].
Alternatively, [Qiy Users] may instantiate a [Qiy Node] themselves using a [Qiy Node Implementation] and register it with an [Access Provider].

## 4.4 Connect via Qiy

Two [Qiy Users] can connect via Qiy by creating a connection between their [Qiy Nodes] ([Connection]).
The [Connection] can be initiated by either of the two [Qiy Users].
The [Qiy User] initiating the [Connection] is called the [Proposer], the other one [Accepter].
This goes as follows:
* The [Proposer] uses a [Qiy Application] to generate a token (see [4.7.1 Generate token]) and compose [Connect Proposal].
* The [Proposer] provides it out-of-band to the [Accepter], for example by lettre, see [4.7.2 'Media'](#4.7.2 Media).
* The [Accepter] may read the proposal and use a [Qiy Application] to extract the [Connect Token] and create a new [Connection] with the [Proposer].

As stated before, when a [Connection] is established, the identity of the [Qiy User] is provided to the other one if the Qiy User is a [Service Providing User]. 
This information may be used to reuse a formerly created [Connection] and delete the new [Connection].

![Users Connect](./images/users-connect.png)

### 4.4.1 Generate token
A [Proposer] can create a token using a [Qiy Application] and the following details:
* Name: The name or pseudonym to use in the [Connect Proposal].
* Expiration: Whether the token expires and if so, on what date and time.
* Budget: The number of times that the token can be used to create a [Connection].

In most cases, the expiration and budget are set by the application.
The Expiration and the Budget can be changed afterwards, for example to re-activate an expired token.

![Generate token](./images/generate-token.png)

 
### 4.4.2 Media
[Qiy Users] can use different media to connect as illustrated in this diagram:

![Media](./images/Connect.png)

 
#### 4.4.2.1 The web
[Qiy Users] can connect by transfering a token as a query parameter in a website address:
 
![Connect using a token in a website address](./images/connect-using-a-token-in-a-website-address.png)

 
#### 4.4.2.2 Print
[Qiy Users] can convert the token to a QR Code and use various 'Print'-media to connect:

![Present proposal containing a QR Code](./images/present-proposal-containing-a-qr-code.png)


The QR Code can be used as follows to create the [Connection]:
 
![Connect using a QR Code](./images/connect-using-a-qr-code.png)
 

## 4.5 Setup

This section addresses the setup for the [Data Reuse]

### 4.5.1 Relying Party

In order to be able to offer his services via Qiy, a [Relying Party] has met the following preconditions:
* The [Relying Party] has acquired access to Qiy with the help of an Access Provider.
* The [Access Provider] has verified and registered the identity of the [Relying Party] for use in Qiy.
* The [Service Library] contains the [Service Catalogue] of the [Relying Party] defining the provided services.
* The [Service Library] contains [Service Descriptions] for all the provided services, which also includes the terms of use, especially with regard to Personal Data.

### 4.5.1 Data Provider

In order to be able to provide the [Personal Data] via Qiy, a [Data Provider] has met the following preconditions:
* The [Data Provider] has acquired access to Qiy with the help of an Access Provider.
* The [Access Provider] has verified and registered the identity of the [Data Provider] for use in Qiy.
* A [Service Endpoint] is available to access the data.
* The [Service Library] contains the [Service Endpoint API] which describes how the data can be obtained.
* The [Service Library] contains [Data Descriptions] for the available data.
* The [Service Library] contains the [Service Catalogue] of the [Data Provider] defining the provided data services and the related endpoints.
* The [Service Library] contains [Service Descriptions] for the provided data services.

### 4.5.2 Individual

In order to be able to reuse [Personal Data] via Qiy, an [Individual] has met the following preconditions:
* The [Individual] has access to his [Personal Data] stored by one or more [Data Providers].
* The [Individual] has access to a personal [Qiy Node].
* The [Individual] is using a [Qiy Application] which is linked to his [Qiy Node].

## 4.6 Subscribe

Data Reuse starts with an Individual subscribing to a service, but only after considering and accepting the terms of use, including those regarding the use of Personal Data.
When an Individual subscribes to a service, the subscription is registered by the Qiy Application, so:
* The subscribed service is recorded using the [Service Portfolio] of the Individual.
* The record shows:
	* the start datetime of the subscription.
	* the provider of the service (the Relying Party).
	* what service is provided (using the [Service Library].
	* the related consent.

## 4.7 Consent

When a request for data is received, it is checked with the granted consents. If the request is not authorized by a granted consent, this may be resolved by granting one, after which the data request is processed. In other cases, the request will not be accepted and no data will be returned.

## 4.8 Routing

When all related conditions are met, a request for data from a Relying Party is processed as follows:
* The [Service Portfolio] is consulted to find the Data Provider or Data Providers and related [Service Endpoint API].
* Using the API, requests are created and used to obtain the data from the [Service Endpoints].
* The received data is forwarded to the Relying Party.

## 4.9 Source

When a [Relying Party] has requested for data, the [Service Portfolio] is used to look up the data source: the [Qiy User] or [Qiy Users] that will provide the data.
This can be the [Individual] himself, for self-declared data, but it can also be one or more [Data Providers].
The source of the data may be defined at the time of subscription, but if that it is not the case, the [Individual] will be asked to make a selection from a list of suitable [Data Providers] ([Servive Discovery]).
The list will be generated using the [Service Catalogues] from the [Service Library].
The [Service Portfolio] will be updated with the outcome.

## 4.10 Session

A Service Endpoint will only process a request when issued over an active Session. This Session may be started earlier, for example when the Individual selects a Data Provider as a source, but a new Session will be started if need be.
More often then not, this may require input from the Individual.
The session credentials are persisted in the [Service Catalogue] of the Individual.

# 5 The Application layer
This chapter describes the [Qiy Application Layer] and how it supports the processes of the Data Reuse scenario.

## 5.1 Qiy Application
A [Qiy Application] is an [Application Service] or software which is authorized for use with Qiy.
* A [Qiy Application] must comply with the requirements of the [Qiy Scheme].
* A [Qiy User] can only use Qiy with a [Qiy Application].
* A [Qiy User] can use one or more [Qiy Applications].
* [Qiy Applications] can use a [Qiy Node] at the same time.

### 5.1.1 Application Provider
[Qiy Applications] can be provided by [Application Providers]. An [Application Provider] can only do so with a valid [Qiy Licence Agreement Application Provider].

### 5.1.2 Qiy Application Protocol
The [Qiy Application Protocol] describes the interactions of the [Qiy Applications] with eachother and the underlying layers.
* The [Qiy Application Protocol] is an open standard and is part of the [Qiy Open Standard].

The [Qiy Application Protocol] describes among others how [Qiy Applications]:
* ... create a [Qiy Node] for a [Qiy User].
* ... can be linked to a [Qiy Node] of a [Qiy User].
* ... create [Connections].
* ... create a 'backup' of a [Qiy Node].
* ... exchange [Connection Tokens] out-of-band.
* ... exchange messages.
* ... exchange [Personal Data].

### 5.1.3 Creating Qiy Nodes for Individuals

A [Qiy Application] can create a [Qiy Node] for a [Qiy User], especially when he does not have one yet.
The [Qiy Application] can do so with the help of an [Access Provider], but first it has to generate the credentials for the [Qiy Node] ([Qiy Node Credentials]):
* A key pair, consisting of public key and a private key, 
* A [Node Id]

The [Qiy Application] must persists these in order to be able to keep using the [Qiy Node].

#### 5.1.3.1 Security consideration
Some security considerations related to the [Qiy Node Credentials] are:
* The [Node Id] must be a [Uuid] in order to assure that it is unique.
* The key pair must be unique.
* The private key must be persisted securily in order to guarantee the security of the [Qiy User]. 
* The [Node Id] should be persisted securily in order to guarantee the security of the [Qiy User]. 
* The [Qiy Applications] that can be used on consumer devices such as smart phones must provide a way to backup and recover the [Qiy Node Credentials] in order to overcome cases of loss of the device.
* A [Qiy User] must be able to control the devices that can access his [Qiy Node], for example in order to be able to block access of a (possibly) stolen device.


### 5.1.4 Link with an existing Qiy Node
A [Qiy Application] can be linked to an existing [Qiy Node] by providing it with its [Qiy Node Credentials].

## 5.2 Connect

### 5.2.1 Application Connect Token
[Qiy Applications] exchange [Application Connect Tokens] to create [Connections]. 
In addition to the [Connect Token] that is necessary to create the [Connection], it contains the name or pseudonym to be displayed in the [Connect Proposal]. 
For more information, please refer to [5.2.3 'Generate Application Connect Token'](#5.2.3 Generate Application Connect Token).

### 5.2.2 Proposer: Connect
For a [Qiy Application] of a [Proposer], a Connection is established as follows:
* The [Qiy Application] generates an [Application Conenct Token], see [5.2.3 'Generate Application Connect Token'](#5.2.3 Generate Application Connect Token).
* The [Qiy Application] composes a [Connect Proposal] for the [Proposer].
* The [Proposer] presents it out-of-band to the [Accepter].
* When the [Accepter] wants to connect, he uses the [Connect Proposal] to create a connection with his [Qiy Application], see [5.2.4 'Accepter: Connect'](#5.2.4 Accepter: Connect).
* The [Proposer] detects this by use of polling (using the [Connections Request]) or events (using the [Connection Created Event]).
 
![Proposer: Connect](./images/proposer--connect.png)

### 5.2.3 Generate Application Connect Token
The main part of an [Application Connect Token] is the [Connect Token]. The [Qiy Application] can create this both online and offline:
* Offline by creating a [Connect Token] and registering it later using a [Connect Token Registration Request].
* Online using a [Connect Token Creation Request].

![Generate Application Connect Token](./images/generate-application-connect-token.png)

### 5.2.4 Accepter: Connect
At the [Accepter]-side, a [Qiy Application] creates a [Connection] with a [Connect Proposal] or [Connect Token] as follows:
* In case of a [Connect Proposal], the [Qiy Application] extracts the [Connect Token] from the [Connect Proposal].
* The [Qiy Application] uses the [Connect Token] in [Connect Request] to the [Qiy Node] of the [Qiy User].
* The [Qiy Node] creates the [Connection] and returns the id of the [Connection] ([Connection Uri]).

![Accepter: Connect](./images/accepter--connect.png)

## 5.3 Consent

### 5.3.1 Relying Party: Request consent

A [Qiy Application] of a [Relying Party] can request an [Individual] for [Consent] as follows:
* The [Qiy Application] sends a [Consent Request Message] over the [Connection] with the [Individual].
* The [Qiy Application] receives a message with the outcome, either a [Consent Granted Message] or a [Consent Denied Message].

![Relying Party: Request consent](./images/relying-party--request-consent.png)

### 5.3.2 Individual: Consider consent request
A [Qiy Application] of an [Individual] processes a [Consent Request] as follows:
* The [Qiy Application] detects receiving a [Consent Request Message] by polling (using the [Messages Request]) or with events (using the [Message Received Event]).
* The [Qiy Application] extracts the [Consent Request] and presents it to the [Individual].
* Depending on the choice of the [Individual], the [Qiy Application] returns a [Consent Granted Message] or a [Consent Denied Message] using the [Connection] with the [Relying Party].

![Individual--consider-consent-request](./images/individual--consider-consent-request.png)

## 5.4 Service Discovery
A [Qiy Application] can present an [Individual] a list of suitable [Data Providers] (or in general [Service Providing Users]) that can produce some requested data (or services) as follows:
* The [Qiy Application] asks the [Qiy Node] of the [Individual] for a list of suitable [Data Providers] with a [Source Candidates Request].
* The [Qiy Node] consults the [Service Library] and returns the outcome to the [Qiy Application].
* The [Qiy Application] presents the result to the [Individual].
* The [Qiy Application] registers the selected sources with a [Source Registration Request].

## 5.5 Data by Reference
[Qiy Applications] exchange [data by reference] rather then by value.
This goes as follows:
* A [Qiy Application] requests a reference for the data ([Data Reference]).
* The [Qiy Application] receives a [Data Reference].
* The [Qiy Application] uses the [Data Reference] to acquire the data.

### 5.5.1 Service by Reference
In Qiy providing data is viewed as a service and requesting data as an operation of this service, so the 'data by reference'-pattern is implemented as using a [[Service by Reference]]-pattern:
* A [Qiy Application] requests an [Operation Reference] ([Operation Reference Request]).
* A [Operation Reference] is created by registrating the specification of the operation [Operation Specification] and returned ([Operation Registration]).
* The [Qiy Application] uses the [Data Reference] to acquire the data ([Operation Execution]).

### 5.5.1 Request data reference
The [Qiy Application] of a [Relying Party] can request an [Individual] for a data reference as follows:
* The [Qiy Application] sends a [Operation Reference Request Message] using the [Connection] of the [Individual].
* The [Qiy Application] receives the [Operation Reference] in an [Operation Reference Message].

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.4.2 Create reference
A [Qiy Application] can create an [Operation Reference] using a specification of the operation ([Operation Specification]).
This goes as follows:
* The [Qiy Application] uses the [Operation Specification] in an [Operation Registration Request] to the [Qiy Node] it is linked with.
* The [Qiy Node] creates the [Operation Reference] and returns it.

### 5.5.1 Request data
The [Qiy Application] of a [Relying Party] can obtain data using a [Data Reference] / [Operation Reference]. 
This goes as follows:
* The [Qiy Application] uses the [Operation Reference] in a [Operation Execution Request] to its [Qiy Node].
* The [Qiy Node] returns the requested data.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.2 Provide data
The [Data Provider] produces the data using his [Service Endpoint].
This does not involve any of the [Qiy Applications] of the [Data Provider] nor his [Qiy Node].

![Data Provider: Provide data](./images/data-provider--provide-data.png)

# 6 The Qiy Node layer
This chapter describes the [Qiy Node Layer] and how it supports the upper layers.

## 6.1 Access Provider
The services of this layer can be provided by an [Access Provider]:
* An [Access Provider] can provide [Qiy Nodes].
* An [Access Provider] can host [Qiy Nodes].

### 6.1.1 Portability
An [Access Provider] can offer [Qiy Node]-services to [Qiy Users], but must enable [Qiy Users] to easily transfer the services to a different [Access Provider].

## 6.2 Qiy Node
A [Qiy Node] is een [Technology Service] as defined in [Definitions of the Qiy Scheme].
A [Qiy Node]:
* ... must comply with the rules of the [Qiy Scheme].
* ... can be hosted on any host ([Node]).
* ... has its own [Transporter] which ensures secure transport of messages and/or data via Qiy.

### 6.2.1 Qiy Node Protocol
The [Qiy Node Protocol] describes the interaction between the [Qiy Nodes] and the underlying layers.
* The [Qiy Node Protocol] is one of the protocols in the [Qiy Open Standard].
The [Qiy Node Protocol] describes for example:
* How a [Qiy Node] is instantiated.
* How [Qiy Nodes] create [Connections] and use them to exchange data, messages or to provide/consume services.

### 6.2.2 Qiy Node API
The [Qiy Node API] is the [Technology Interface] of the [Qiy Node], one of the APIs of the [Qiy Open Standard].
* The [Qiy Node API] is intended for use by [Qiy Applications].

### 6.2.3 Qiy Node Implementation
A [Qiy Node Implementation] is a software package which can be used to realize a [Qiy Node].
The [Qiy Scheme] puts no limit on the number of [Qiy Node Implementation]s, as long as the implementation complies with the [Qiy Open Standard] and the rules of the [Qiy Scheme]. 

### 6.2.4 Qiy Node Instantiation
A [Qiy Node] can be created in two ways:
* It can be instantiated by an [Access Provider]. The [Access Provider] will instantiate it with its own [Transporter]. 
* It can be instantiated by a [Qiy User] on a [Node] of his own using a [Qiy Node Implementation]. 
When the second option is chosen, the [Qiy User] is responsible for obtaining a [Transporter] and linking it to the [Qiy Node].

### 6.2.5 Deleting a Qiy Node
In principle, a [Qiy Node] can be deleted by its owner whenever he wants to do so.
In this case, the [Qiy Node] will be deleted including persisted data, [Connections] and the linked [Transporter].
Related [Consents] will be withdrawn.

## 6.3 Connect
Two [Qiy Nodes] can connect by creating a [Path] between themselves.
* A [Qiy Node] can connect with zero or more other [Qiy Nodes].
* A [Qiy Node] can have zero or more [Paths] with any other [Qiy Node].
* A priori, a [Qiy Node] does not know the identity of the [Qiy Node] at the other side of a [Path].

### 6.3.1 Connection Uri
The [Connection Uri] is the [Uri] which identifies a [Connection] for one of the [Qiy Node] it connects.
* A [Connection] has two [Connection Uris]; one for each of the two [Qiy Nodes] it connects.
* The two [Connection Uris] of one [Connection] are not related to one another.
* A priori, a [Qiy Node] does not know the other [Connection Uri] of a [Connection].

EXAMPLE: [Connection Uris] of a [Connection] between [Qiy Node] 1 and [Qiy Node] 2:

[Qiy Node] | [Connection Uri]
---- | --------------
Qiy Node 1	| http://127.0.0.1:8087/user/connections/user/usernodeB/93590b55-9194-4cf4-944f-2cbceab7dbcd
Qiy Node 2	| http://127.0.0.1:8087/user/connections/user/usernodeA/f96bc541-e98b-449e-bfc5-48ec928e0dc9

#### 6.3.1.1 Security concern
The [Connection Uri] has only meaning in the context of the [Qiy Node] that knows it and is useless outside this scope.
For example, the [Uri] by itself can not be used to exchange a message with the [Qiy Node] nor any other existing [Qiy Node].

### 6.3.2 Connect Token
A [Connect Token] is a token which can be used by a [Qiy Application] to create a [Connection].
It consists of:
* a temporary secret
* a [Transport Connect Token].

A [Connect Token] has the following properties:
* An expiration setting: Whether the token expires and if so, on what date and time
* A budget: The number of times that the token can be used to create a Connection. 

The properties can not only be set when the token is registered or requested, but also later.
For example, it is possible to reactivate a [Connect Token] by increasing the budget or inactivate one by changing the expiration.

#### 6.3.2.1 Security concern
The [Connect Token] can only be used to create a [Connection] and only so via Qiy, with the help of a [Qiy Application] and a linked [Qiy Node].
By itself, it cannot be used for any other purpose, for example gain access to a [Qiy Node] nor any other parts of the Qiy infrastructuur.

#### 6.3.2.2 Creating a Connect Token
A [Connect Token] can be created both offline and online:
* A [Connect Token] can be obtained from the [Qiy Node] using a [Connect Token Creation Request] ([Online Connect Token]).
* A [Connect Token] can be created by a [Qiy Application] and registered later using a [Connect Token Registration Request] ([Offline Connect Token]).

The [Offline Connect Token] allows initiating a [Connection] (creating a [Connect Token]) even when Qiy is temporarily not available.
However, care must be taken that the created token is unique, especially so for the created [Transport Connect Token].

#### 6.3.2.3 Creating a Transport Connect Token
A [Qiy Node] will never create a [Transport Connect Token]:
* In case of an [Online Connect Token]: The [Qiy Node] will obtain a [Transport Connect Token] from its [Transporter].
* In case of an [Offline Connect Token]: The [Qiy Node] will compose a [Transport Connect Token] using the [Connect Token] provided by the [Qiy Application] and register it at its [Transporter].

### 6.3.3 Connecting
Two [Qiy Nodes] connect as follows:
* The [Qiy Node] of the [Proposer] either 1) obtains a [Transport Connect Token] from the [Transporter] or 2) from a linked [Qiy Application] in a [Connect Request].
* The [Qiy Node] either 1) provides the [Transport Connect Token] to the [Qiy Application] or 2) registers the [Transport Connect Token] at its [Transporter].
* The [Transport Connect Token] is made available (partly out-of-bands, for example in a [Connect Proposal]) to the [Qiy Node] of the [Accepter].
* The [Qiy Node] of the [Accepter] uses its [Transporter] to create a [Path] using the [Transport Connect Token] ([Path Creation Request]).
Each accepted [Path Creation Request] leads to a new [Path], irrespective of the number of existing [Paths] between the two [Qiy Nodes].

### 6.3.4 Deleting a Path
A [Path] can be deleted with a [Path Delete Request].
The [Path] will be deleted completely, including any persisted data and/or messages.

## 6.4 Consent
A [Consent] is a permission given by an [Individual] to a [Relying Party] defining what [Personal Data] a [Relying Party] is allowed to use for a provided [Service] and under what the terms.
A [Consent] has the following properties:
* a [Consent Uri]
* a [Consent Service Descriptor]
* a [Consent Data Descriptor]

### 6.4.1 Consent Uri
The [Consent Uri] is an [Uri] used to identify a [Consent].

### 6.4.2 Consent Service Descriptor
The [Consent Service Descriptor] is a [Service Descriptor] which indicates the [Service] that the [Consent] applies to.
A [Service Descriptor] can be used to obtain a description of a [Service] ([Service Description]) with the help of the [Service Library].

### 6.4.3 Consent Data Descriptor
The [Consent Data Descriptor] is a [Data Descriptor] which indicates the [Personal Data] that the [Consent] applies to.
A [Data Descriptor] can be used to obtain a description of [Data] ([Data Description]) with the help of the [Service Library].

#### 6.4.3.1 Privacy concern
A [Relying Party] can only ask [Consent] for [Personal Data] that can be provided by one of the available [Data Providers], eg for which a [Data Descriptor] exists in the [Service Library].
  
## 6.5 Qiy Node Request
A [[Qiy Node Request]] is a [Http Request] for a [Qiy Node]. 
[Qiy Node Requests] are only accepted when they are correctly authenticated with:
* the node id
* an actual timestamp
* a digital signature over the Node Id, the timestamp and the contents of the body of the request made with the private key

## 6.6 Qiy Node Requests
This section gives an overview of the [Qiy Node Requests].
Details of [Qiy Node Requests] can be found in the [Qiy Node API].

### 6.6.1 Connect Request
[[Connect Request]]
Met dit request kan een [Connection] worden gemaakt met behulp van een meegegeven [Connect Token].

### 6.6.2 Connect Token Creation Request
[[Connect Token Creation Request]]
Met dit request kan een [Connect Token] worden gecre&euml;erd door the [Qiy Node].

### 6.6.3 Connect Token Registration Request
[[Connect Token Registration Request]]
Met dit request kan een [Connect Token] worden geregistreerd.

### 6.6.4 Connect Token Update Request
[[Connect Token Update Request]]
Met dit request kunnen the eigenschappen van een [Connect Token] worden aangepast.

### 6.6.5 Connections Request
The [[Connections Request]] kan gebruikt worden om alle [Connections] inclusief status op te vragen.

### 6.6.6 Consent Granted Request
[[Consent Granted Request]]
[Request] voor the doorgeven van the geven van een [Consent].

### 6.6.7 Consent Denied Request
[[Consent Denied Request]]
[Request] voor the doorgeven van the niet geven van een [Consent].

### 6.6.9 Consent Request
The [[Consent Request]] is a [Qiy Node Request] which can be used to request for a [Consent].

### 6.6.8 Consent Withdrawn Request
[[Consent Withdrawn Request]]
[Request] voor the doorgeven van the intrekken van een [Consent].

### 6.6.9 Consents Request
[[Consents Request]]
[Request] waarmee alle [Consents] inclusief status opgevraagd kan worden.

### 6.6.10 Messages Request
[[Messages Request]]
[Request] which can be used to retrieve all [Qiy Node Messages] of a [Qiy Node].

### 6.6.11 Operation Execution Request
[[Operation Execution Request]]
[Request] which can be used to requests the execution of an operation using a [Operation Reference].

### 6.6.12 Operation Registration Request
[[Operation Registration Request]]
[Request] which can be used to create a [Operation Reference] by registrating the [Operation Specification].

### 6.6.13 Operation References Request
[[Operation References Request]]
[Request] which can be used to obtain a list of [Operation References].

### 6.6.14 Source Candidates Request
The [[Source Candidates Request]] is a  [Qiy Node Request] to obtain candidate [Service Providing Users] for a [Service].

### 6.6.15 Source Registration Request
The [[Source Registration Request]] is a  [Qiy Node Request] to register a [Service Providing Users] as source for a [Service].
 
## 6.7 Qiy Node Message
A [[Qiy Node Message]] is een bericht dat over een [Connection] wordt verstuurd.
[Qiy Node Messages] kunnen worden verstuurd en opgehaald met [Qiy Node Requests] en the status gevolgd middels [Qiy Node Events].
[Qiy Node Messages] kunnen door [Qiy Applications] worden gebruikt, maar worden ook 'intern' gebruikt voor the processen rondom the [Services], bijvoorbeeld voor the verkrijgen van een [Consent] en the afnemen van [Services]. The laatste [Qiy Node Messages] worden in the regel door the [Qiy Node] zelf verwerkt.

A [Qiy Node Message] heeft the volgende eigenschappen:
* [Qiy Node Message Serial Number]
* [Qiy Node Message Reference Serial Number]
* [Qiy Node Message Subject]
* [Qiy Node Message Descriptor]
* [Qiy Node Message Payload]

## 6.8 Qiy Node Messages
This section gives an overview of the [Qiy Node Messages].
Details of [Qiy Node Messages] can be found in the [Qiy Node Protocol].


### 6.8.1 Consent Denied Message
The [[Consent Denied Message]] is a [Qiy Node Message] which can be used to communicate the denial of a [Consent].

### 6.8.2 Consent Granted Message
The [[Consent Granted Message]] is a [Qiy Node Message] which can be used to communicate the granting of a [Consent].

### 6.8.3 Consent Request Message
The [[Consent Request Message]] is a [Qiy Node Message] which can be used to request for a [Consent].

A [Consent Request Message] has the following properties:
* [Consent Id]
* [Consent Service Descriptor]

Als een [Qiy Node] van een [Data Provider] een [Consent Request Message] heeft ontvangen onderzoekt the standaard of eventueel benodige gegevens niet betrokken kunnen worden van &eacute;&eacute;n van the [Qiy Nodes] waar the al een [Connection] mee heeft.
The [Qiy Node] heeft [Qiy Node Requests] waarmee nagevraagd kan worden of dit the geval en zo ja welke [Data Providers] dat dan zijn, maar daarnaast kent the [Qiy Node] ook enkele [Qiy Node Events].

### 6.8.4 Operation Reference Message
[[Operation Reference Message]]
This message can be used to convey [Operation References].
 
### 6.8.5 Operation Reference Request Message
[[Operation Reference Request Message]]
This message can be used to request for [Operation References].
 
## 6.9 Qiy Node Event
A [[Qiy Node]] genereert verschillende events die door gekoppelde [Qiy Applications] kunnen worden opgevangen en gebruikt. Zo genereert een [Qiy Node] een Event als er een bericht is ontvangen of als er een nieuwe [Connection] is gemaakt.

## 6.10 Qiy Node Events
This section gives an overview of the [Qiy Node Events].
Details of [Qiy Node Events] can be found in the [Qiy Node Protocol].

### 6.10.1 Connection Created Event
[[Connection Created Event]]
The [Qiy Node] van een Proposer ontvangt dit event (elke keer als) er een [Connection] gemaakt is.

### 6.10.2 Consent Withdrawn Event
The [[Consent Withdrawn Event]] wordt afgevuurd als een [Consent] is ingetrokken door een [Individual].

### 6.10.4 Message Received Event
[[Message Received Event]]
This event is fired when a [Qiy Node Message] has been received.

### 6.10.6 Reference Received Event
[[Reference Received Event]]
A [Qiy Node] van een [Relying Party] genereert dit event als the een [References Messages] heeft ontvangen.

### 6.7.9 Source Candidate Event
[[Source Candidate Event]]
A [Qiy Node] van een [Individual] vuurt dit event af als er een nieuwe [Source Candidate] is voor een [Consent].

# 7 The Service layer
The Service layer bevat the volgende ondersteunende diensten voor the onder regie van the gebruiker aanbieden en afnemen van [Services]:
* [Service Endpoints]
* [Service Library]
* [Consent Service]

## 7.1 Access Provider
Vanaf deze layer moet -met uitzondering van the [Service Endpoints]- gebruik gemaakt worden van the diensten van een [Access Provider].
### 7.1.1 Portability
Voor deze diensten geldt dat er makkelijk overgestapt kan worden op een andere aanbieder.
## 7.2 Service
A [Service] is een 'information society service' as defined in the [GDPR].
* A [Service] omvat &eacute;&eacute;n of meerdere Operations waarmee the dienst 'by Reference' af kan worden genomen.
* A [Service] wordt aangeboden door een dienstaanbieder.
* A dienstaanbieder kan &eacute;&eacute;n of meer [Services] aanbieden.
* Eenzelfde [Service] kan door verschillende dienstaanbieders worden aangeboden.
* A [Service] kan alleen worden afgenomen als the beschrijving hiervan is opgenomen in the [Service Description Library].

### 7.2.1 Operation
* A Operation is een deeldienst van een [Service] die 'by Reference' kan worden afgenomen, zoals bijvoorbeeld the leveren van een set [Personal Data] die met een [Data Reference] kan worden opgevraagd.

### 7.2.2 Service Providing User
A [Service Providing User] is een rol voor een [Qiy User] die [Services] via Qiy aanbiedt.
* A [Qiy User] heeft deze rol als hij een [Relying Party] is en/of als hij een [Data Provider] is.
* A [Service Providing User] kan alleen diensten aanbieden als zijn [Service Catalogue] is opgenomen in the [Service Catalogue Library].

### 7.2.3 Service Catalogue
A [Service Catalogue] beschrijft the aanbod van een [Service Providing User]: the [Services] van een [Service Providing User].
* The [Service Catalogue] van een [Service Providing User] bestaat uit een lijst van [Service Descriptors].

## 7.3 Service Description
A [Service Description] is een beschrijving van een [Service] die zowel door mensen als door machines gelezen kan worden.
### 7.3.1 Service Descriptor
A [Service Descriptor] is een [Uri] waarmee een [Service Description] wordt ge&iuml;dentificeerd en kan worden verkregen.
## 7.4 Service Endpoints
A [Service Endpoint] is een [Technology Service] voor the afnemen van [Services] van een [Service Providing User]. 
* A [Service Providing User] kan &eacute;&eacute;n of meer [Service Endpoints] inzetten voor the aanbieden van haar [Services].
* The [Service Providing User] is verantwoordelijk voor zijn [Service Endpoint](s).
* A [Service Endpoint] kan gebruikt worden voor the aanbieden van meerdere [Services].
* A [Service] kan geleverd worden met the hulp van meerder [Service Endpoints].
A [Service Endpoint] kan bijvoorbeeld gebruikt worden om database te ontsluiten met persoonsgegevens.

### 7.4.1 Security note
A [Service Endpoint] wordt alleen door the [Qiy Node] van the [Service Providing User] gebruikt met [Requests] die door the [Service Providing User] zelf zijn opgesteld.

## 7.5 Service Library
The [Service Library] wordt gebruikt voor the beheren van [Service Descriptions] en  [Service Catalogues] en bestaat uit:
* A [Service Description Library]
* A [Service Catalogue Library]
* [Service Provider Library]

### 7.5.1 Service Description Library
In the [Service Description Library] staan the [Registered Service Descriptions]: the geregistreerde [Service Descriptions] van the door [Service Providing Users] aangeboden [Services].

#### 7.5.1.1 Service Description Registration
[Service Description Registration] is the registreren van een [Service Description] bij een [Access Provider] voor opname in the [Service Description Library].

A [Service Description Registration Request] bevat:
* A [Service Descriptor]
* A [Service Description], maar alleen als die niet al beschikbaar is voor alle [Qiy Users], [Application Providers] en [Access Providers].

### 7.5.2 Service Catalogue Library
In the [Service Catalogue Library] staan the [Service Catalogue] van the aangeboden [Services].

#### 7.5.2.1 Service Catalogue Registration
[Service Catalogue Registration] is the registreren van een [Service Catalogue] bij een [Access Provider] voor opname in the [Service Catalogue Library].

A [Service Catalogue Registration Request] bevat:
* A lijst van [Registered Service Descriptions].

### 7.5.3 Service Provider Library
The [Service Provider Library] wordt gebruikt voor the beheren van the [Service Providing Users].
Met behulp van the [Service Provider Library] kunnen [Service Providing Users] binnen Qiy worden ge&iuml;dentificeerd.

#### 7.5.3.1 Service Provider Registration
[Service Provider Registration] is the registreren van een [Service Providing User] bij een [Access Provider] voor opname in the [Service Provider Library].
### 7.5.4 Data Description Library
The [Data Description Library] wordt gebruikt voor the beheren van [Data Descriptions].
Hiervoor worden gangbare gegevensbeschrijvingsmethodes gebruikt zoals [Linked Data], XML Schema, JSON Schema of RDF Schema, en externe bronnen, zoals Schema.org  of [Linked Open Vocabularies] .

#### 7.5.4.1 Data Description Registration
[Data Description Registration] is the registreren van een [Data Descrition] bij een [Access Provider] voor opname in the [Data Description Library].

## 7.6 Consent Service
A [Consent Service] wordt gebruikt voor the beheren van [Consents] en hun status. Deze [Consents] zijn zowel beschikbaar voor the [Individual] die the gegeven heeft als the [Service Providing User].
* A [Consent] kan alleen gebruikt worden als deze zowel voor the [Individual] als the [Relying Party] via the [Consent Service] beschikbaar is.
* In principe kan alleen een [Individual] een door hem gegunde [Consent] intrekken.
* A [Relying Party] kan alleen gebruik maken van [Consents] als die niet is ingetrokken.

# 8 The Transport layer
The Transport layer verzorgt the maken van Paths tussen [Transporters] en the veilig transporteren van [Transport Messages] daarover.
## 8.1 Access Provider
Voor deze layer moet gebruik gemaakt worden van the diensten van een [Access Provider]:
* The Transport diensten kunnen alleen worden afgenomen van een [Access Provider].

### 8.1.1 Portability
Voor deze diensten geldt dat er makkelijk overgestapt kan worden op een andere aanbieder.
## 8.2 Transporter
A [Transporter] is een [Technology Service] die transportdiensten levert aan een [Qiy Node].
* A [Transporter] moet altijd voldoen aan the eisen van the [Qiy Scheme].
* A [Transporter] wordt geleverd door een [Access Provider].
* A [Transporter] wordt gehost op een [Carrier Node].
* Elke Qiy Node heeft een eigen [Transporter].

A [Transporter] biedt the volgende diensten:
* The leggen van Paths met andere [Transporters].
* The veilig transporteren van [Transport Messages] over Paths..

## 8.3 Transport Protocol
The [Transport Protocol] beschrijft the interacties tussen [Transporters] en the onderliggende lagen voor the realiseren van the Transport diensten.
The protocol is een open standaard en maakt deel uit van the [Qiy Scheme].
## 8.4 Transport Connect Token
A [Transport Connect Token] is een token dat door [Transporters] gebruikt wordt om een Path te maken.
## 8.5 Transporter Instantiation
A [Transporter] kan alleen door een [Access Provider] worden ge&iuml;nstantieerd. Dat kan the [Access Provider] doen voor [Qiy Nodes] die ze zelf heeft ge&iuml;nstantieerd of anders op verzoek voor andere [Qiy Nodes].
## 8.6 Deleting a Transporter
In principe kan een [Transporter] op elk gewenst moment alleen op verzoek van the [Qiy User] worden verwijderd. The [Transporter] wordt dan inclusief gepersisteerde gegevens en/of berichten en onderliggende Paths verwijderd.
## 8.7 Transporter API
The [Transporter API] beschrijft the koppelvlak van een [Transporter], dus bijvoorbeeld the [Transporter Requests] voor the maken van Paths en the uitwisselen van berichten daarover.
The [Transporter API] is een open standaard en maakt deel uit van the [Qiy Scheme].
## 8.8 Transporter Implementation
The [Qiy Scheme] schrijft geen implementatie voor voor the [Transporter], dus the is toegestaan om zelf [Transporter Implementation] te maken of anders een implementatie te kiezen uit the beschikbare aanbod. Wel mag een [Transporter Implementation] alleen gebruikt worden als die voldoet aan the daarvoor geldende eisen in the [Qiy Scheme].
### 8.8.1 QS Issuer
The QS Issuer is een software pakket van Digital Me dat een implementatie bevat van the [Transporter] en waarmee [Transporters] kunnen worden uitgegeven.
## 8.9 Path
A Path is een logische verbinding tussen twee [Transporters] die gebruikt kan worden voor the uitwisselen van [Transport Messages].
Physiek gezien kan een Path over &eacute;&eacute;n of meerdere [Carriers] lopen.
### 8.9.1 Path Creation
A Path wordt door een [Transporter] of verzoek van een [Qiy Node] gemaakt met behulp van een [Transport Connect Token].
### 8.9.2 Deleting a Path
In principe kan een Path op elk gewenst alleen op verzoek van &eacute;&eacute;n van the betrokken [Qiy Nodes] worden verwijderen. The Path wordt dan verwijderd inclusief gepersisteerde gegevens en/of berichten.
## 8.10 Transport Message
A [Transport Message] is een bericht dat uitgewisseld wordt tussen twee [Transporters] over een Path. 
* Van een [Transport Message] kunnen alleen the versturende [Transporter] en the ontvangende [Transporter] achterhaald worden.
* A [Transport Message] is versleuteld en kan alleen door the ontvangende [Transporter] worden ontsleuteld.

A [Transport Message] bevat:
* A [Transport Message Descriptor]
* A [Transport Message Payload]

### 8.10.1 Transport Message Descriptor
The [Transport Message Descriptor] kan gebruikt worden om the [Transport Message Description] te achterhalen: een beschrijving van the [Transport Message] en haar Payload.
A [Transport Message] moet altijd een [Transport Message Descriptor] hebben. 
### 8.10.2 Transport Message Payload
The [Transport Message Payload] bevat the contents van the bericht. The contents, the formaat en the eventuele versleuteling van the [Transport Message Payload] staat beschreven in the [Transport Message Description].

# 9 The Carrier layer
The Carrier layer is the onderste layer en the basis van Qiy.
## 9.1 Access Provider
Voor deze layer moet -met uitzondering van the levering van [Qiy Nodes]- gebruik gemaakt worden van the diensten van een [Access Provider]:
* The Carrier diensten kunnen alleen worden afgenomen van een [Access Provider].

### 9.1.1 Portability
Voor deze diensten geldt dat er makkelijk overgestapt kan worden op een andere aanbieder.
## 9.2 Carrier
The [Carrier] is the belangrijkste dienst van deze layer en kan gebruikt worden om:
* The verkrijgen van een [Transporter].
* The veilig transporteren van berichten tussen [Carrier Services].
* The verkrijgen van een [Qiy Node].

Verder geldt:
* A [Carrier Service] moet voldoen aan the eisen van the [Qiy Scheme].
* A [Carrier Service] moet the [Carrier API] ondersteunen.
* A [Carrier Service] wordt gehost op een [Carrier Node].
* Van een [Carrier Service] kunnen meerdere [Carrier Service Implementations] bestaan.

## 9.3 Carrier API
The [Carrier API] beschrijft the diensten van the [Carrier Service].
* The [Carrier API] is een open standaard en maakt deel uit van the [Qiy Scheme].
* The [Carrier API] maakt Transportering van berichten tussen verschillende [Carrier Nodes] mogelijk.
* Elke Access Provider is verplicht om the [Carrier API] te ondersteunen..

## 9.4 Carrier Protocol
The [Carrier Protocol] beschrijft the interacties tussen Carriers voor the realiseren van the Carrier diensten.
The protocol is een open standaard en maakt deel uit van the [Qiy Scheme].
## 9.5 Carrier Service Implementation
The [Qiy Scheme] schrijft geen implementatie voor voor the [Carrier Service], dus the is toegestaan om zelf een [Carrier Service Implementation] te maken of er anders een te kiezen uit the beschikbare aanbod. Wel mag een implementatie alleen gebruikt worden als die voldoet aan the daarvoor geldende eisen in the [Qiy Scheme].
### 9.5.1 QS Issuer
The QS Issuer is een software pakket van Digital Me dat een implementatie bevat van the [Transporter] en waarmee [Transporters] kunnen worden uitgegeven.
### 9.5.2 QS User Node
The QS User Node is een software pakket van Digital Me waarmee [Qiy Nodes] kunnen worden uitgegeven.
## 9.6 Carrier Node
A Node voor the hosten van [Carrier Services].
* The [Carrier Node] valt onder the verantwoordelijkheid van the [Access Provider].
* A [Acces Provider] kan &eacute;&eacute;n of meerdere [Carrier Nodes] gebruiken.

## 9.7 Requesting a Qiy Node
Met the volgende gegevens kan een [Qiy Node] worden aangevraagd:
* the node id
* the publieke sleutel
* the transportwachtwoord

# 10 Definitions
In dit document worden the volgende definitions gebruikt:

Term	| Definitie
------- | ---------
<a id="access-provider">Access Provider</a>| A organisatie die [Qiy Users] toegangsdiensten levert voor the [Qiy Trust Framework], d.w.z een [Issuer] of een [Service Provider].
<a id="access-principle">Access Principle</a>| The principle which authorizes the access of an [Individual] to his [Personal Data], one of the [Qiy Trust Principles].
<a id="accepter">Accepter</a>|One of the two [Business Roles] which are used for creating a [Connection], the other one being [Proposer]: an [Accepter] can create a [Connection] by accepting a [Connect Proposal](@Connect Proposal) from a [Proposer].
<a id="application-connect-token">Application Connect Token</a>|A [Connect Token] dat door [Qiy Applications] wordt gebruikt om [Connections] te maken.
<a id="application-interface">Application Interface</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="application-layer">Application Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="application-provider">Application Provider</a>|A [Bussiness Role] for suppliers of [Qiy Applications].
<a id="application-service">Application Service</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="architectural-layers-of-the-qiy-scheme">Architectural Layers of the Qiy Scheme</a.>|The architectural layers of the [Qiy Scheme]: the [User Layer], the [Application Layer], the [Qiy Node Layer], the [Service Layer], the [Transport Layer] and the [Carrier Layer].
<a id="binding-individual-rights">Binding Individual Rights</a>|One of the documents of the [Qiy Scheme Rulebook].
<a id="binding-principles-for-relying-parties-and-data-providers">Binding Principles for Relying Parties and Data Providers</a>|One of the documents of the [Qiy Scheme Rulebook].
<a id="business-actor">Business Actor</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-object">Business Object</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-process">Business Process</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-role">Business Role</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="carrier-api">Carrier API</a>|[Technology Interface] of the [Carrier Service].
<a id="carrier-layer">Carrier Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="carrier-node">Carrier Node</a>|A Node van een [Access Provider] voor the hosten van [Carrier Services].
<a id="carrier-service">Carrier Service</a>|A [Technology Service] die Carrier diensten levert.
<a id="carrier-service-implementation">Carrier Service Implementation</a>|A implementatie van een [Carrier Service], bestaande uit een software pakket.
<a id="connect-proposal">Connect Proposal</a>|A [Business Object] for a proposal to connect via Qiy.
<a id="connect-token">Connect Token</a>|A Literal used to create a [Connection].
<a id="connection">Connection</a>|A connection between two [Qiy Nodes].
<a id="connection-uri">Connection Uri</a>|[Uri] voor the id van een [Connection].
<a id="consent">Consent</a>|As defined in the [GDPR].
<a id="consent-data-descriptor">Consent Data Descriptor</a>|[Data Descriptor] in een [Service Description] voor the beschrijving van the voor the [Service] benodigde [Personal Data].
<a id="consent-service">Consent Service</a>|A [Technology Service] voor the persisteren van [Consents] en the status daarvan voor the betrokken [Qiy Users].
<a id="consent-service-description">Consent Service Description</a>|[Service Description] van een [Service] waarvoor [Consent] wordt of is gevraagd.
<a id="consent-service-descriptor">Consent Service Descriptor</a>|[Service Descriptor] van een [Consent Service Description].
<a id="consent-uri">Consent Uri</a>|A [Uri] waarmee een [Consent] kan worden ge&iuml;dentificeerd.
<a id="consented-service">Consented Service</a>|A [Service] van een [Service Providing User] waarvoor een [Consent] is gegeven aan een [Relying Party]. Meestal betreft dit een [Data Service], namelijk the leveren van van bepaalde [Personal Data] die the [Relying Party] nodig heeft voor the leveren van haar [Service]. 
<a id="data-by-reference">Data by Reference</a>|Proces waarbij data niet als waarde maar met behulp van een Reference wordt doorgegeven, see also [Request by Reference].
<a id="data-description">Data Description</a>|A beschrijving van een gegevensset die zowel gelezen kan worden door mensen als machines.
<a id="data-description-library">Data Description Library</a>|A [Technology Service] voor the beheren van [Data Descriptions].
<a id="data-descriptor">Data Descriptor</a>|A [Uri] waarmee een [Data Description] kan worden ge&iuml;dentificeerd en verkregen.
<a id="data-provider">Data Provider</a>|A [Business Role] as defined in [Definitions of the Qiy Scheme].
<a id="data-provider-agreement">Data Provider Agreement</a>|A overeenkomst die een [Qiy User] met een [Access Provider] moet hebben om als [Data Provider] te kunnen acteren.
<a id="data-reference">Data Reference</a>|A [Operation Reference] waarmee een [Relying Party] [Personal Data] by Reference kan opvragen bij een [Data Provider].
<a id="data-subject">Data Subject</a>|As defined in the [GDPR].
<a id="definitions-of-the-qiy-scheme">Definitions of the Qiy Scheme</a>|One of the documents of the [Qiy Scheme Rulebook].
<a id="gdpr">GDPR</a>|General Data Protection Regulation, see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 
<a id="governance-model-for-the-qiy-scheme">Governance Model for the Qiy Scheme</a>|Governance Model for the [Qiy Scheme], see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/.
<a id="http-request">HTTP Request</a>|As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
<a id="individual">Individual</a>|A [Business Role] of a [Qiy User] as defined in [Definitions of the Qiy Scheme].
<a id="issuer">Issuer</a>|A [Business Role]: an [Access Provider] servicing natural persons, see also [Definitions of the Qiy Scheme].
<a id="licence-agreement-application-provider">Licence Agreement Application Provider</a>| A licence agreement for [Application Providers], the template of which is part of the [Qiy Scheme Rulebook].
<a id="licence-agreement-issuer">Licence Agreement Issuer</a>|A licence agreement for [Issuers], the template of which is part of the [Qiy Scheme Rulebook].
<a id="licence-agreement-service-provider">Licence Agreement Service Provider</a>|A licence agreement for [Service Providers], the template of which is part of the [Qiy Scheme Rulebook].
<a id="literal">Literal</a>|A vaste waarde zoals beschreven op Wikipedia, see  https://en.wikipedia.org/wiki/Literal_(computer_programming).
<a id="node">Node</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
[[Operation]] | A sub-service which can be used to consume a [Service].
[[Operation Reference Request]] | A [Request] for an [Operation Reference].
<a id="personal-data">Personal Data</a>|As defined in the [GDPR].
<a id="proposer">Proposer</a>|A [Business Role] for a [Qiy User] that initiates creating a [Connection].
<a id="qiy-application">Qiy Application</a>|An [Application Service] or software that is authorized for use with Qiy.
<a id="qiy-application-protocol">Qiy Application Protocol</a>|A protocol for the interactions between [Qiy Applications] and the underlying layers.
<a id="qiy-foundation">Qiy Foundation</a>|A foundation dedicated to putting people back in control of their personal data while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.
<a id="qiy-foundation-member">Qiy Foundation Member</a>|A member of the [Qiy Foundation], see https://www.qiyfoundation.org/membership/.
<a id="qiy-node">Qiy Node</a>|A [Technology Service] as defined in [Definitions of the Qiy Scheme].
<a id="qiy-node-api">Qiy Node API</a>|[Technology Interface] of the [Qiy Node], an Open Standard which is part of the [Qiy Scheme].
<a id="qiy-node-event">Qiy Node Event</a>|A [Technology Event] dat door een [Qiy Node] wordt gegeneerd.
<a id="qiy-node-implementation">Qiy Node Implementation</a>|A implementatie van een [Qiy Node], bestaande uit een software pakket.
<a id="qiy-node-layer">Qiy Node Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="qiy-node-message">Qiy Node Message</a>|A bericht dat over een [Connection] wordt verstuurd van &eacute;&eacute;n [Qiy Node] naar een andere [Qiy Node].
<a id="qiy-node-protocol">Qiy Node Protocol</a>|Protocol dat the interacties tussen [Qiy Nodes] onderling en the onderliggende lagen beschrijft.
<a id="qiy-node-request">Qiy Node Request</a>|A [HTTP Request] to a [Qiy Node].
<a id="qiy-open-standard">Qiy Open Standard</a>|A set of open standards for Qiy, maintained by the [Work Stream Functionality & Technology](#Work Stream Functionality & Technology), see https://www.qiyfoundation.org/qiy-scheme/workstreams/.
<a id="qiy-scheme">Qiy Scheme</a>|The blueprint of Qiy, showing how the Qiy Principles are realized, see https://www.qiyfoundation.org/qiy-scheme/.
<a id="qiy-scheme-rulebook">Qiy Scheme Rulebook</a>|A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme], see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/
<a id="qiy-trust-framework">Qiy Trust Framework</a>|As defined in [Definitions of the Qiy Scheme].
<a id="qiy-trust-principles">Qiy Trust Principles</a>|As defined in [Definitions of the Qiy Scheme] and available on: https://www.qiyfoundation.org/qiy-trust-principles/.
<a id="qiy-user">Qiy User</a>|A [Business Actor]; 'User' as defined in [Definitions of the Qiy Scheme].
<a id="reference">Reference</a>|A [Literal].
<a id="operation-registration-request">Operation Registration Request</a>|A [Qiy Node Request] which can be used to generate a [Operation Reference].
[[Operation Specification]] | A specification of a [Http Request] for the execution of an [Operation].
<a id="reference-received-event">Reference Received Event</a>|A [Qiy Node Event] dat een [Qiy Node] afvuurt als the een nieuwe [Operation Reference] heeft ontvangen.
<a id="registered-service-description">Registered Service Description</a>|A [Service Description] die is opgenomen in the [Service Description Library].
<a id="relying-party">Relying Party</a>|A [Business Role] as defined in [Definitions of the Qiy Scheme].
<a id="relying-party-agreement">Relying Party Agreement</a>|A overeenkomst die een [Qiy User] met een [Access Provider] moet hebben om als [Relying Party] te kunnen acteren.
<a id="request">Request</a>|A [Business Object]: a message requesting something.
<a id="request-by-reference">Request by Reference</a>|A [Business Process] which allows to issue a [Request] indirectly by using a [Operation Reference].
<a id="operation-reference">Operation Reference</a>|A [Business Object] used by the [Service by Reference]-pattern.
<a id="request-specification">Request Specification</a>|A [Business Object]: The specification of a [Request].
<a id="route">Path</a>|A logische verbinding tussen twee [Transporters].
<a id="route-message">Transport Message</a>|A bericht dat uitgewisseld wordt tussen twee [Transporters] over een Path. 
<a id="route-message-description">Transport Message Description</a>|A [Service Description] die the [Transport Message] en the contents, the opmaak en versleuteling van the [Transport Message Payload] beschrijft.
<a id="route-message-descriptor">Transport Message Descriptor</a>|A [Uri] waarmee the [Transport Message Description] kan worden verkregen.
<a id="service">Service</a>|'information society service' as defined in the [GDPR].
<a id="service-catalogue">Service Catalogue</a>|The [Services] aanbod van een [Service Providing User].
<a id="service-catalogue-library">Service Catalogue Library</a>|A [Technology Service] voor the beheren van [Service Catalogues] van [Service Providing Users].
<a id="service-discovery">Service Discovery</a>|Proces voor the vinden van [Service Sources]: [Service Providing Users] die een bepaalde [Service] kan bieden.
<a id="service-discovered-event">Service Discovered Event</a>|A [Qiy Node Event] dat wordt afgevuurd door een [Qiy Node] van een [Individual] als er een (nieuwe) [Service Providing User] is die een [Service] kan leveren voor een [Consent].
<a id="service-description">Service Description</a>|A beschrijving van een [Service].
<a id="service-description-library">Service Description Library</a>|A [Technology Service] voor the beheren van [Service Descriptions].
<a id="service-descriptor">Service Descriptor</a>|A uri waarmee een [Service Description] kan worden verkregen met hulp van the [Service Library].
<a id="service-endpoint">Service Endpoint</a>|A [Technology Service] van een [Service Providing User] waarmee &eacute;&eacute;n of meer van haar [Services] kan worden afgenomen.
<a id="service-layer">Service Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="service-library">Service Library</a>|A [Technology Service] voor the beheren van the [Services].  Deze omvat: een [Service Description Library], een [Service Catalogue Library], een [Service Provider Library] en een [Data Description Library]
<a id="service-provider">Service Provider</a>|A [Business Role]: an [Access Provider] servicing organizations as defined in [Definitions of the Qiy Scheme].
<a id="service-provider-library">Service Provider Library</a>|A [Technology Service] voor the beheren van the [Service Providing Users].
<a id="service-providing-user">Service Providing User</a>|A [Business Role] for a [Qiy User] that is providing one or more [Services] using Qiy, that is a [Data Provider] or a [Relying Party].
<a id="operation-execution-request">Operation Execution Request</a>|A [Qiy Node Request] to request the execution of a service operation using a [Service Reference].
<a id="service-source">Service Source</a>|A [Service Providing User] die een bepaalde dienst kan leveren of dat doet.
<a id="source-registration-request">Source Registration Request</a>|A [Qiy Node Request] waarmee the [Service Sources] voor [Consented Services] kunnen worden vastgelegd.
<a id="technology-event">Technology Event</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="technology-interface">Technology Interface</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="technology-service">Technology Service</a>|As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 
<a id="transport-connect-token">Transport Connect Token</a>|A Literal dat gebruikt wordt voor the leggen van Paths tussen [Transporters].
<a id="transport-layer">Transport Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="transport-protocol">Transport Protocol</a>|Protocol dat the interactie beschrijft tussen the [Transporters] onderling en onderliggende lagen.
<a id="transporter">Transporter</a>|A [Technology Service] die transportdiensten levert aan een [Qiy Node].
<a id="transporter-api">Transporter API</a>|[Technology Interface] of the [Transporter].
<a id="transporter-implementation">Transporter Implementation</a>|A implementatie van een [Transporter], bestaande uit een software pakket.
<a id="user-layer">User Layer</a>|One of the [Architectural Layers of the Qiy Scheme].
<a id="uri">Uri</a>|See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
<a id="url">Url</a>|See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
<a id="work-stream-functionality-&-technology">Work Stream Functionality & Technology</a>|One of the work streams of the [Qiy Foundation], see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

# 11 Diagram sources


## 11.1 User Layer
### 11.1.1 Qiy Data Reuse
```
title Qiy Data Reuse

Individual->Relying Party: Subscribe
loop Route data
Relying Party->Individual: Request data
opt No consent
    Individual->Relying Party: Grant consent 
end
opt No source selected
    Individual->Individual: Select source
end
Individual->Data Provider: Request data
opt No session
    Data Provider->Individual: Start session
end
Data Provider-->Individual: Data
Individual -->Relying Party: Data
end
```
### 11.1.2 Connect
#### 11.1.2.1 Users Connect
```
title Users Connect

Proposer->Proposer: Generate token
Proposer->Proposer: Compose proposal
Proposer->Accepter: Propose
Accepter->Accepter: Consider proposal

alt Accept proposal
Accepter->Accepter: Extract token
Accepter->Proposer: Connect
else Ignore proposal
end
```

#### 11.1.2.2 Generate token
```
title Generate token

Proposer->Proposer: Set name, expiration & budget
Proposer->+Qiy Application: Request token
Qiy Application->Qiy Application: Generate token
Qiy Application-->Proposer: token
```

#### 11.1.2.3 Media
```
title Connect

Proposer->Accepter: ... using ...
alt ... the web
else ... print
else ... apps
else ... NFC
else ... sound
else ... images
else ...
end
```
#### 11.1.2.4 Connect using a token in a website address
```
title Connect using a token in a website address

Proposer->Proposer: Generate token
Proposer->Proposer: Set query parameter in website address
Proposer->Accepter: Visit website
Accepter->Accepter: Consider to connect
alt Accept
Accepter->Accepter: Extract token
Accepter->Proposer: Connect
else Ignore
end
```
#### 11.1.2.5 Connect using a QR Code
```
title Connect using a QR Code

Proposer->Proposer: Generate token
Proposer->Proposer: Convert to QR Code
Proposer->Proposer: Compose proposal
Proposer->Accepter: Present proposal
Accepter->Accepter: Consider proposal

alt Accept proposal
Accepter->Accepter: Scan QR Code
Accepter->Accepter: Extract token
Accepter->Accepter: Verify token
Accepter->Proposer: Connect
else Ignore proposal
end
```
#### 11.1.2.6 Present proposal containing a QR Code
```
title Present proposal containing a QR Code

Proposer->Accepter: ... using ...

alt ... a poster
else ... e-mail
else ... a letter
else ... a newspaper
else ... a website
else ...
end
```

### 11.1.3 Authenticate
#### 11.1.3.1 Data Provider: Authenticate
```
title Data Provider: Authenticate

Data Provider->Individual: Identify & authenticate
alt pass
Data Provider->Data Provider: Persist connection id 
else fail
end
```
### 11.1.4 Consent
```
title Consent

Relying Party->Individual: Request consent
Individual->Individual: Consider
alt 
Individual->Relying Party: Grant
else
Individual->Relying Party: Deny
end
```

### 11.1.5 Service discovery
```
title Service discovery
Individual->Qiy: Request service catalogue
Individual->+Individual: Select source
opt For other then self-declared data
    Individual->Data Provider: Connect
end
```

### 11.1.6 Request data
```
title Request data

Individual->Data Provider: Request reference
Data Provider->Qiy: Register request
Qiy-->Data Provider: Reference
Data Provider-->Individual: Reference
Individual-->Relying Party: Reference
Relying Party-->Qiy: Reference
Qiy->Data Provider: Execute registered request
Qiy-->Relying Party: Data
```
## 11.2 Application Layer
### 11.2.1 Connect
#### 11.2.1.1 Proposer: Connect
```
title Proposer: Connect

note over Qiy Application,Qiy Node: Generate token
Qiy Application->Qiy Application: Create connect proposal
alt event
Qiy Node-->Qiy Application: Connection Created Event
else polling
Qiy Application->Qiy Node: Get connections
end
```
#### 11.2.1.2 Generate Application Connect Token
```
title Generate Application Connect Token

alt online
Qiy Application->Qiy Node: Get Connect Token
Qiy Node->Qiy Node: Create Connect Token
Qiy Node-->Qiy Application: Connect Token
else offline
Qiy Application->Qiy Application: Create Connect Token
note right of Qiy Application
    When online again:
end note
Qiy Application->Qiy Node: Register Connect Token
Qiy Node->Qiy Node: Register Connect Token
end
Qiy Application->Qiy Application: Create Application Connect Token
```

#### 11.2.1.3 Accepter: Connect
```
title Accepter: Connect

Qiy Application->Qiy Application: Extract Connect Token from connect proposal
Qiy Application->Qiy Node: Connect
Qiy Node-->Qiy Application: Connection Uri, [Proposer Id]```

### 11.2.2 Consent
#### 11.2.2.1 Relying Party: Request consent
```
title Relying Party: Request consent

Qiy Application->Qiy Node: Request consent
alt Grant
    Qiy Node->Qiy Application: Consent Granted Event
else Deny
    Qiy Node->Qiy Application: Consent Denied Event
end
```
#### 11.2.2.2 Individual: Consider consent request
```
title Individual: Consider consent request

alt Use events
Qiy Node-->Qiy Application: Consent Request Message
else Use polling
Qiy Application->Qiy Node: Request consents
end
Qiy Application->Qiy Application: Present Consent Request
alt Grant
    Qiy Application->Qiy Node: Consent Granted Request
    Qiy Node->Qiy Node: Initiate service discovery
else Deny
    Qiy Application->Qiy Node: Consent Denied Request
end
```

### 11.2.3 Service Discovery 
#### 11.2.3.1 Individual: Select source
```
title Individual: Select source

Qiy Application->Qiy Node: Request source candidates
Qiy Node->Qiy Node: Search for source candidates
Qiy Node->Qiy Application: Return candidate(s)

opt For not connected candidate(s)
    Qiy Application->Qiy Application: Propose candidate
    opt Connect with Data Provider
    end
end

Qiy Application->Qiy Application: Propose candidate(s)
opt Select candidate(s)
Qiy Application->Qiy Node: Set source
Qiy Node->Qiy Node: Generate and distribute reference(s)
```

#### 11.2.3.2 Qiy Node: Generate and distribute references
```
title Qiy Node: Generate and distribute references

Individual Qiy Node->Data Provider Qiy Node: Request reference(s)
Data Provider Qiy Node->Data Provider Qiy Node: Generate reference(s)
Data Provider Qiy Node-->Individual Qiy Node: Return reference(s)
Individual Qiy Node-->Relying Party Qiy Node: Provide reference(s)
```

#### 11.2.3.3 Generate operation reference
```
title Generate operation reference

Qiy Application->Qiy Application: Specify operation
Qiy Application->Qiy Node: Register operation specification
Qiy Node->Qiy Node: Generate operation reference
Qiy Node->Qiy Application: Operation reference
```

#### 11.2.3.4 Relying Party: Persist reference
```
title Relying Party: Persist reference

alt Events
Qiy Node-->Qiy Application: Reference Received Event
else Polling
Qiy Application->Qiy Node: Request references
end
Qiy Application->Qiy Application: Persist reference
```

### 11.2.4 Request data
#### 11.2.4.1 Relying Party: Request data
```
title Relying Party: Request data

Qiy Application->Qiy Application: Look-up reference
Qiy Application->+Qiy Node: Request data
Qiy Node->Qiy Node: Look-up and use request
Qiy Node-->Qiy Application: data
```

#### 11.2.4.2 Data Provider: Provide data
```
title Data Provider: Provide data

note over Qiy Application,Qiy Node: 
The data is fetched and returned by 
the Service Endpoint 
of the Data Provider.
```




