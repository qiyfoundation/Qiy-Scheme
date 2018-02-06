# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From Qiy Nodes to data exchange


# Contents

1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Reader guidance](#12-reader-guidance)
1. [Overview](#2-overview)
	1. [Data Reuse](#21-data-reuse)
		1. [Privacy concern](#211-privacy-concern)
1. [Architectural Description](#3-architectural-description)
	1. [Architectural Layers](#31-architectural-layers)
	1. [Privacy](#32-privacy)
	1. [Security](#33-security)
	1. [Interoperability](#34-interoperability)
	1. [Governance](#35-governance)
	1. [Compliancy](#36-compliancy)
1. [The User Layer](#4-the-user-layer)
	1. [Qiy Users](#41-qiy-users)
	1. [Provider](#42-provider)
	1. [Qiy Node](#43-qiy-node)
	1. [Connect via Qiy](#44-connect-via-qiy)
		1. [Generate token](#441-generate-token)
		1. [Media](#442-media)
			1. [The web](#4421-the-web)
			1. [Print](#4422-print)
		1. [Examples](#443-examples)
			1. [Connect Proposal](#4431-connect-proposal)
			1. [Email](#4432-email)
			1. [Webpage](#4433-webpage)
	1. [Setup](#45-setup)
		1. [Relying Party](#451-relying-party)
		1. [Data Provider](#451-data-provider)
		1. [Individual](#452-individual)
	1. [Subscribe](#46-subscribe)
	1. [Consent](#47-consent)
	1. [Routing](#48-routing)
	1. [Source](#49-source)
	1. [Session](#410-session)
1. [The Application Layer](#5-the-application-layer)
	1. [Qiy Application](#51-qiy-application)
		1. [Application Provider](#511-application-provider)
		1. [Qiy Application Protocol](#512-qiy-application-protocol)
		1. [Creating Qiy Nodes for Individuals](#513-creating-qiy-nodes-for-individuals)
			1. [Security consideration](#5131-security-consideration)
		1. [Link with an existing Qiy Node](#514-link-with-an-existing-qiy-node)
	1. [Connect](#52-connect)
		1. [Application Connect Token](#521-application-connect-token)
		1. [Proposer: Connect](#522-proposer-connect)
		1. [Generate Application Connect Token](#523-generate-application-connect-token)
		1. [Accepter: Connect](#524-accepter-connect)
	1. [Consent](#53-consent)
		1. [Relying Party: Request consent](#531-relying-party-request-consent)
		1. [Individual: Consider consent request](#532-individual-consider-consent-request)
	1. [Service Discovery](#54-service-discovery)
	1. [Data by Reference](#55-data-by-reference)
		1. [Service by Reference](#551-service-by-reference)
		1. [Request data reference](#551-request-data-reference)
		1. [Create reference](#542-create-reference)
		1. [Request data](#551-request-data)
		1. [Provide data](#552-provide-data)
1. [The Qiy Node Layer](#6-the-qiy-node-layer)
	1. [Access Provider](#61-access-provider)
		1. [Portability](#611-portability)
	1. [Qiy Node](#62-qiy-node)
		1. [Qiy Node Protocol](#621-qiy-node-protocol)
		1. [Qiy Node API](#622-qiy-node-api)
		1. [Qiy Node Implementation](#623-qiy-node-implementation)
		1. [Qiy Node Instantiation](#624-qiy-node-instantiation)
		1. [Deleting a Qiy Node](#625-deleting-a-qiy-node)
	1. [Connect](#63-connect)
		1. [Connection Uri](#631-connection-uri)
			1. [Security concern](#6311-security-concern)
		1. [Connect Token](#632-connect-token)
			1. [Security concern](#6321-security-concern)
			1. [Creating a Connect Token](#6322-creating-a-connect-token)
			1. [Creating a Transport Connect Token](#6323-creating-a-transport-connect-token)
		1. [Connecting](#633-connecting)
		1. [Deleting a Connection](#634-deleting-a-connection)
	1. [Consent](#64-consent)
		1. [Consent Uri](#641-consent-uri)
		1. [Consent Service Descriptor](#642-consent-service-descriptor)
		1. [Consent Data Descriptor](#643-consent-data-descriptor)
			1. [Privacy concern](#6431-privacy-concern)
	1. [Qiy Node Request](#65-qiy-node-request)
	1. [Qiy Node Requests](#66-qiy-node-requests)
		1. [Connect Token Creation Request](#661-connect-token-creation-request)
		1. [Connect Token Registration Request](#662-connect-token-registration-request)
		1. [Connect Token Update Request](#663-connect-token-update-request)
		1. [Connection Create Request](#664-connection-create-request)
		1. [Connection Delete Request](#665-connection-delete-request)
		1. [Connections Request](#666-connections-request)
		1. [Consent Denied Request](#667-consent-denied-request)
		1. [Consent Granted Request](#668-consent-granted-request)
		1. [Consent Request](#669-consent-request)
		1. [Consent Withdrawn Request](#6610-consent-withdrawn-request)
		1. [Consents Request](#6611-consents-request)
		1. [Message Post Request](#6612-message-post-request)
		1. [Messages Request](#6613-messages-request)
		1. [Operation Execution Request](#6614-operation-execution-request)
		1. [Operation Registration Request](#6615-operation-registration-request)
		1. [Operation References Request](#6616-operation-references-request)
		1. [Source Candidates Request](#6617-source-candidates-request)
		1. [Source Registration Request](#6618-source-registration-request)
	1. [Qiy Node Message](#67-qiy-node-message)
	1. [Qiy Node Messages](#68-qiy-node-messages)
		1. [Consent Denied Message](#681-consent-denied-message)
		1. [Consent Granted Message](#682-consent-granted-message)
		1. [Consent Request Message](#683-consent-request-message)
		1. [Operation Reference Message](#684-operation-reference-message)
		1. [Operation Reference Request Message](#685-operation-reference-request-message)
	1. [Qiy Node Event](#69-qiy-node-event)
	1. [Qiy Node Events](#610-qiy-node-events)
		1. [Connection Created Event](#6101-connection-created-event)
		1. [Consent Withdrawn Event](#6102-consent-withdrawn-event)
		1. [Message Received Event](#6103-message-received-event)
		1. [Operation Reference Received Event](#6104-operation-reference-received-event)
		1. [Source Candidate Event](#6105-source-candidate-event)
1. [The Service Layer](#7-the-service-layer)
	1. [Access Provider](#71-access-provider)
		1. [Portability](#711-portability)
	1. [Service](#72-service)
	1. [Service Endpoints](#73-service-endpoints)
	1. [Service Library](#74-service-library)
	1. [Consent Service](#75-consent-service)
1. [The Transport Layer](#8-the-transport-layer)
	1. [Access Provider](#81-access-provider)
		1. [Portability](#811-portability)
	1. [Transporter](#82-transporter)
	1. [Transport Protocol](#821-transport-protocol)
	1. [Transporter API](#822-transporter-api)
	1. [Transporter Implementation](#823-transporter-implementation)
	1. [Transporter Instantiation](#824-transporter-instantiation)
	1. [Deleting a Transporter](#825-deleting-a-transporter)
	1. [Path](#83-path)
		1. [Path Creation](#831-path-creation)
		1. [Deleting a Path](#832-deleting-a-path)
1. [The Carrier Layer](#9-the-carrier-layer)
	1. [Access Provider](#91-access-provider)
		1. [Portability](#911-portability)
	1. [Carrier](#92-carrier)
	1. [Carrier Protocol](#921-carrier-protocol)
	1. [Carrier API](#922-carrier-api)
	1. [Carrier Implementation](#923-carrier-implementation)
	1. [Carrier Node](#93-carrier-node)
1. [Definitions](#10-definitions)

# 1 Introduction
Qiy, or rather: the _Qiy Scheme_, puts people back in control of their _Personal Data_ while creating value for organizations that process it (_Relying Parties_).


## 1.1 Purpose

The document is aimed at people who know that Qiy puts people back in control of their _Personal Data_, but who want or need to know the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.

## 1.2 Reader guidance

* Privacy officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Security officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Information analysts are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer) and [5 The Application Layer](#5-the-application-layer).
* Application developers are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer), [5 The Application Layer](#5-the-application-layer) and [6 The Qiy Node Layer](#6-the-qiy-node-layer).
* Systems engineers are advised to read chapters [3 Architectural Description](#3-architectural-description), [8 The Transport Layer](#8-the-transport-layer) and [9 The Carrier Layer](#9-the-carrier-layer).

# 2 Overview

This chapter gives an overview of this document.
* [2.1 Data Reuse](#21-data-reuse) describes how data can be reused with Qiy.
* [3 Architectural Description](#3-architectural-description) describes the _Architectural Layers_ and addresses various concerns like privacy and security.
* [4 The User Layer](#4-the-user-layer) describes the setup and processes of the data reuse at the user level.
* [5 The Application Layer](#5-the-application-layer) describes the processes at the application level.
* [6 The Qiy Node Layer](#6-the-qiy-node-layer) describes the same at the Qiy Node level.
* [7 The Service Layer](#7-the-service-layer) describes the _Service Layer_ support.
* [8 The Transport Layer](#8-the-transport-layer) describes the _Transport Layer_ support.
* [9 The Carrier Layer](#9-the-carrier-layer) describes the _Carrier Layer_ support.
* [10 Definitions](#10-definitions) contains the definitions used in this document.

## 2.1 Data Reuse

This document describes how Qiy realizes a Data Reuse scenario in which a _Data Subject_ (_Individual_) reuses his _Personal Data_ stored at one organization (_Data Provider_) and provide it to another organization (_Relying Party_) to consume one of its services.

In essence, the _Data Reuse_ goes as follows:
* The _Individual_ subscribes to a service.
* The _Relying Party_ asks the _Individual_ for the data it needs to provide the service.
* The _Individual_ retrieves the data from a _Data Provider_.
* The _Individual_ provides the data to the _Relying Party_.

![Qiy Data Reuse](./images/qiy-data-reuse.png)

### 2.1.1 Privacy concern

The _Data Reuse_ scenario shows that the data is transferred to the _Relying Party_ by choice of the _Individual_.
This breaks the chain of responsibility for the _Data Provider_; the responsibility for correct processing of the data does not extend to any processing that takes place after the handover to the _Individual_. 

# 3 Architectural Description

This chapter describes the major entities of Qiy and their relations with the help of the _Architectural Layers of the Qiy Scheme_ and addresses how Qiy addresses concerns like security and privacy.

## 3.1 Architectural Layers
The realization of the scenario is described using the following layers:

![Layers](./images/layers.png)

## 3.2 Privacy

Qiy has been conceived with the aim to put people back in control of their _Personal Data_, hence making privacy the primary concern of Qiy.
The aim has been elaborated in a set of principles called the _Qiy Trust Principles_ and technical, legal and governance rules, all of which are maintained by the _Qiy Foundation_ and the _Qiy Foundation Members_.

The realization of the _Data Reuse_ as described in this document demonstrates that a natural person (_Individual_) is in control:
* The _Individual_ can securily exchange data and/or messages with another person or organization (_Qiy User_) via Qiy, using connections, see [4 The User Layer](#4-the-user-layer).
* The _Individual_ controls what _Qiy Users_ he connects with and, in principle, when he wants to end it.
* When an _Individual_ connects with a _Qiy User_ that is providing a _Service_ via Qiy (_Provider_), the _Individual_ is provided with the identity of the latter, but not the other way around.
* The _Individual_ can access his _Personal Data_ that is kept by another _Qiy User_ (_Data Provider_) as a result of the _Access Principle_, one of the _Qiy Trust Principles_.
* The _Individual_ controls what data he shares with what _Provider_ (_Relying Party_) and under what terms using proveable _Consents_.
* _Qiy Users_ use applications that are authorized for use with Qiy (_Qiy Applications_).
* Access to Qiy, data exchange via Qiy, consent services and potentially _Qiy Nodes_ are provided by _Access Providers_.


All parties involved are bound by the rules of the _Qiy Scheme_:
* _Providers_ are bound by the _Binding Individual Rights_ and the _Binding Principles for Relying Parties and Data Providers_.
* _Access Providers_ are bound by the _Licence Agreement Issuer_ or the _Licence Agreement Service Provider_.
* _Application Providers_ can only develop and produce _Qiy Application_-services and/or software with a _Licence Agreement Application Provider_.

## 3.3 Security

As described above, privacy is at the heart of Qiy and security being a 'conditio sine qua no' for this, it is also addressed by the rules of the _Qiy Scheme_.

## 3.4 Interoperability

An _Individual_ can only control his _Personal Data_, when all concerned systems are interoperable.
This is achieved as follows:
* Applications exchange data and/or messages via Qiy using open standards of the _Qiy Scheme_ (_Qiy Open Standard_).
* Applications exchange described data using _Data Descriptions_ which are available to all concerned parties (via the _Service Library_).

## 3.5 Governance

The governance rules are laid down in the _Governance Model for the Qiy Scheme_, one of the documents of the _Qiy Scheme Rulebook_.

## 3.6 Compliancy

The compliancy rules for _Providers_ can be found in the _Binding Principles for Relying Parties and Data Providers_, one of the documents of the _Qiy Scheme Rulebook_.


# 4 The User Layer
This chapter describes the _User Layer_ and the interaction between the _Relying Party_, _Individual_, _Data Provider_ and the lower layers for the _Data Reuse_.

## 4.1 Qiy Users
The organizations and/or persons using Qiy are called _Qiy Users_. They can use Qiy in different _roles_; they can use Qiy as a _Relying Party_, _Individual_, _Data Provider_ or a combination of these.
A business for example will generally use Qiy both as a _Relying Party_ (for offering _Services_ using reliable _Personal Data_) and as a _Data Provider_ (as a source of _Personal Data_).
As for natural persons, most of these will use Qiy as an _Individual_ to control their _Personal Data_.

## 4.2 Provider
A _Qiy User_ that provides one or more _Services_ to _Individuals_ is said to be (or act in the _Business Role_ of) '_Providers_'.
Any _Qiy User_ acting in one or both of the roles _Relying Party_ or _Data Provider_ is implicitely acting in this role.

## 4.3 Qiy Node
A _Qiy User_ must have a _Qiy Node_. 
_Providers_ can acquire one from an _Access Provider_.
_Individuals_ obtain a _Qiy Node_ the first time they use a _Qiy Application_.
Alternatively, _Qiy Users_ may instantiate a _Qiy Node_ themselves using a _Qiy Node Implementation_ and register it with an _Access Provider_.

## 4.4 Connect via Qiy

Two _Qiy Users_ can connect via Qiy by creating a connection between their _Qiy Nodes_ (_Connection_).
The _Connection_ can be initiated by either of the two _Qiy Users_.
The _Qiy User_ initiating the _Connection_ is called the _Proposer_, the other one _Accepter_.
This goes as follows:
* The _Proposer_ uses a _Qiy Application_ to generate a token (see [4.4.1 Generate token](#441-generate-token)) and to compose a _Connect Proposal_.
* The _Proposer_ provides it out-of-band to the _Accepter_, for example by lettre, see [4.4.2 Media](#442-media).
* The _Accepter_ may read the proposal and use a _Qiy Application_ to extract the _Connect Token_ and create a new _Connection_ with the _Proposer_.

As stated before, when a _Connection_ is established, the identity of the _Qiy User_ is provided to the other one if the Qiy User is a _Provider_. 
This information may be used to reuse a formerly created _Connection_ and delete the new _Connection_.

![Users Connect](./images/users-connect.png)

### 4.4.1 Generate token
A _Proposer_ can create a token using a _Qiy Application_ and the following details:
* Name: The name or pseudonym to use in the _Connect Proposal_.
* Expiration: Whether the token expires and if so, on what date and time.
* Budget: The number of times that the token can be used to create a _Connection_.

In most cases, the expiration and budget are set by the application.
The Expiration and the Budget can be changed afterwards, for example to re-activate an expired token.

![Generate token](./images/generate-token.png)

 
### 4.4.2 Media
_Qiy Users_ can use different media to connect as illustrated in this diagram:

![Media](./images/Connect.png)

 
#### 4.4.2.1 The web
_Qiy Users_ can connect by transfering a token as a query parameter in a website address:
 
![Connect using a token in a website address](./images/connect-using-a-token-in-a-website-address.png)

 
#### 4.4.2.2 Print
_Qiy Users_ can convert the token to a QR Code and use various 'Print'-media to connect:

![Present proposal containing a QR Code](./images/present-proposal-containing-a-qr-code.png)


The QR Code can be used as follows to create the _Connection_:
 
![Connect using a QR Code](./images/connect-using-a-qr-code.png)
 

### 4.4.3 Examples


#### 4.4.3.1 Connect Proposal

The picture below shows a _Connect Proposal_ that is generated by an _Individual_ using a mobile app containing a QR Code.
The _Individual_ can use this proposal to invite other _Individuals_ to connect.

![An example of a Connect Proposal](./images/example--connect-proposal--qr-code-on-phone.PNG)

#### 4.4.3.2 Email
The picture below shows an example of a _Connect Proposal_ in an email:

![An example of a Connect Proposal in an email](./images/example--connect-proposal--email.PNG)

#### 4.4.3.3 Webpage
The picture below shows an example of a _Connect Proposal_ in a webpage which displays a QR code when viewed on a laptop, pc or tablet:

![An example of a Connect Proposal in a webpage with QR code](./images/example--connect-proposal--webpage-laptop-pc-tablet.PNG)

## 4.5 Setup

This section addresses the setup for the _Data Reuse_

### 4.5.1 Relying Party

In order to be able to offer his services via Qiy, a _Relying Party_ has met the following preconditions:
* The _Relying Party_ has acquired access to Qiy with the help of an Access Provider.
* The _Access Provider_ has verified and registered the identity of the _Relying Party_ for use in Qiy.
* The _Service Library_ contains the _Service Catalogue_ of the _Relying Party_ defining the provided services.
* The _Service Library_ contains _Service Descriptions_ for all the provided services, which also includes the terms of use, especially with regard to Personal Data.

### 4.5.1 Data Provider

In order to be able to provide the _Personal Data_ via Qiy, a _Data Provider_ has met the following preconditions:
* The _Data Provider_ has acquired access to Qiy with the help of an Access Provider.
* The _Access Provider_ has verified and registered the identity of the _Data Provider_ for use in Qiy.
* A _Service Endpoint_ is available to access the data.
* The _Service Library_ contains the _Service Endpoint API_ which describes how the data can be obtained.
* The _Service Library_ contains _Data Descriptions_ for the available data.
* The _Service Library_ contains the _Service Catalogue_ of the _Data Provider_ defining the provided data services and the related endpoints.
* The _Service Library_ contains _Service Descriptions_ for the provided data services.

### 4.5.2 Individual

In order to be able to reuse _Personal Data_ via Qiy, an _Individual_ has met the following preconditions:
* The _Individual_ has access to his _Personal Data_ stored by one or more _Data Providers_.
* The _Individual_ has access to a personal _Qiy Node_.
* The _Individual_ is using a _Qiy Application_ which is linked to his _Qiy Node_.

## 4.6 Subscribe

Data Reuse starts with an Individual subscribing to a service, but only after considering and accepting the terms of use, including those regarding the use of Personal Data.
When an _Individual_ subscribes to a service, the subscription is registered by the _Qiy Application_, so:
* The subscribed service is recorded using the _Service Portfolio_ of the _Individual_.
* The record shows:
	* the start datetime of the subscription.
	* the _Provider_ of the service (the _Relying Party_).
	* what service is provided (using the _Service Library_.
	* the related _Consent_.

## 4.7 Consent

When a request for data is received, it is checked with the granted consents. If the request is not authorized by an active granted consent, this may be resolved by granting one, after which the data request is processed.
In other cases, the request will not be accepted and no data will be returned.

## 4.8 Routing

When all related conditions are met, a request for data from a _Relying Party_ is processed as follows:
* The _Service Portfolio_ of the _Individual_ is consulted to find the _Data Provider_ or _Data Providers_ and related _Service Endpoint API_.
* Using the API, requests are created and used to obtain the data from the _Service Endpoints_.
* The received data is forwarded to the _Relying Party_.

## 4.9 Source

When a _Relying Party_ has requested for data, the _Service Portfolio_ is used to look up the data source: the _Provider_ or _Providers_ that will provide the data (_Service Source_).
This can be the _Individual_ himself, for self-declared data, but it can also be one or more _Data Providers_.
The source of the data may have been defined before at the time of subscription, but if that it is not the case, the _Individual_ will be asked to make a selection from a list of suitable _Data Providers_ (_Servive Discovery_).
The list will be generated using the _Service Catalogues_ from the _Service Library_.
The _Service Portfolio_ will be updated with the outcome.

## 4.10 Session

A Service Endpoint will only process a request when issued over an active Session. This Session may be started earlier, for example when the Individual selects a Data Provider as a source, but a new Session will be started if need be.
More often then not, this may require input from the Individual.
The session credentials are persisted in the _Service Catalogue_ of the Individual.

# 5 The Application Layer
This chapter describes the _Application Layer_ and how it supports the processes of the _Data Reuse_ scenario.

## 5.1 Qiy Application
A _Qiy Application_ is an _Application Service_ or software which is authorized for use with Qiy.
* A _Qiy Application_ must comply with the requirements of the _Qiy Scheme_.
* A _Qiy User_ can only use Qiy with a _Qiy Application_.
* A _Qiy User_ can use one or more _Qiy Applications_.
* _Qiy Applications_ can use a _Qiy Node_ at the same time.

### 5.1.1 Application Provider
_Qiy Applications_ can be provided by _Application Providers_. An _Application Provider_ can only do so with a valid _Qiy Licence Agreement Application Provider_.

### 5.1.2 Qiy Application Protocol
The _Qiy Application Protocol_ describes the interactions of the _Qiy Applications_ with eachother and the underlying layers.
* The _Qiy Application Protocol_ is an open standard and is part of the _Qiy Open Standard_.

The _Qiy Application Protocol_ describes among others how _Qiy Applications_:
* ... create a _Qiy Node_ for a _Qiy User_.
* ... can be linked to a _Qiy Node_ of a _Qiy User_.
* ... create _Connections_.
* ... create a 'backup' of a _Qiy Node_.
* ... exchange _Connection Tokens_ out-of-band.
* ... exchange messages.
* ... exchange _Personal Data_.

### 5.1.3 Creating Qiy Nodes for Individuals

A _Qiy Application_ can create a _Qiy Node_ for a _Qiy User_, especially when he does not have one yet.
The _Qiy Application_ can do so with the help of an _Access Provider_, but first it has to generate the credentials for the _Qiy Node_ (_Qiy Node Credentials_):
* A key pair, consisting of public key and a private key, 
* A _Node Id_

The _Qiy Application_ must persists these in order to be able to keep using the _Qiy Node_.

#### 5.1.3.1 Security consideration
Some security considerations related to the _Qiy Node Credentials_ are:
* The _Node Id_ must be a _Uuid_ in order to assure that it is unique.
* The key pair must be unique.
* The private key must be persisted securily in order to guarantee the security of the _Qiy User_. 
* The _Node Id_ should be persisted securily in order to guarantee the security of the _Qiy User_. 
* The _Qiy Applications_ that can be used on consumer devices such as smart phones must provide a way to backup and recover the _Qiy Node Credentials_ in order to overcome cases of loss of the device.
* A _Qiy User_ must be able to control the devices that can access his _Qiy Node_, for example in order to be able to block access of a (possibly) stolen device.


### 5.1.4 Link with an existing Qiy Node
A _Qiy Application_ can be linked to an existing _Qiy Node_ by providing it with its _Qiy Node Credentials_.

## 5.2 Connect

### 5.2.1 Application Connect Token
_Qiy Applications_ exchange _Application Connect Tokens_ to create _Connections_. 
In addition to the _Connect Token_ that is necessary to create the _Connection_, it contains the name or pseudonym to be displayed in the _Connect Proposal_. 
For more information, please refer to [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).

### 5.2.2 Proposer: Connect
For a _Qiy Application_ of a _Proposer_, a Connection is established as follows:
* The _Qiy Application_ generates an _Application Conenct Token_, see [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).
* The _Qiy Application_ composes a _Connect Proposal_ for the _Proposer_.
* The _Proposer_ presents it out-of-band to the _Accepter_.
* When the _Accepter_ wants to connect, he uses the _Connect Proposal_ to create a connection with his _Qiy Application_, see [5.2.4 'Accepter: Connect'](#524-accepter-connect).
* The _Proposer_ detects this by use of polling (using the _Connections Request_) or events (using the _Connection Created Event_).
 
![Proposer: Connect](./images/proposer--connect.png)

### 5.2.3 Generate Application Connect Token
The main part of an _Application Connect Token_ is the _Connect Token_. The _Qiy Application_ can create this both online and offline:
* Offline by creating a _Connect Token_ and registering it later using a _Connect Token Registration Request_.
* Online using a _Connect Token Creation Request_.

![Generate Application Connect Token](./images/generate-application-connect-token.png)

### 5.2.4 Accepter: Connect
At the _Accepter_-side, a _Qiy Application_ creates a _Connection_ with a _Connect Proposal_ or _Connect Token_ as follows:
* In case of a _Connect Proposal_, the _Qiy Application_ extracts the _Connect Token_ from the _Connect Proposal_.
* The _Qiy Application_ uses the _Connect Token_ in _Connection Create Request_ to the _Qiy Node_ of the _Qiy User_.
* The _Qiy Node_ creates the _Connection_ and returns the id of the _Connection_ (_Connection Uri_).

![Accepter: Connect](./images/accepter--connect.png)

## 5.3 Consent

### 5.3.1 Relying Party: Request consent

A _Qiy Application_ of a _Relying Party_ can request an _Individual_ for _Consent_ as follows:
* The _Qiy Application_ sends a _Consent Request Message_ over the _Connection_ with the _Individual_.
* The _Qiy Application_ receives a message with the outcome, either a _Consent Granted Message_ or a _Consent Denied Message_.

![Relying Party: Request consent](./images/relying-party--request-consent.png)

### 5.3.2 Individual: Consider consent request
A _Qiy Application_ of an _Individual_ processes a _Consent Request_ as follows:
* The _Qiy Application_ detects receiving a _Consent Request Message_ by polling (using the _Messages Request_) or with events (using the _Message Received Event_).
* The _Qiy Application_ extracts the _Consent Request_ and presents it to the _Individual_.
* Depending on the choice of the _Individual_, the _Qiy Application_ returns a _Consent Granted Message_ or a _Consent Denied Message_ using the _Connection_ with the _Relying Party_.

![Individual--consider-consent-request](./images/individual--consider-consent-request.png)

## 5.4 Service Discovery
A _Qiy Application_ can present an _Individual_ a list of suitable _Data Providers_ (or in general _Providers_) that can produce some requested data (or services) as follows:
* The _Qiy Application_ asks the _Qiy Node_ of the _Individual_ for a list of suitable _Data Providers_ with a _Source Candidates Request_.
* The _Qiy Node_ consults the _Service Library_ and returns the outcome to the _Qiy Application_.
* The _Qiy Application_ presents the result to the _Individual_.
* The _Qiy Application_ registers the selected sources with a _Source Registration Request_.

## 5.5 Data by Reference
_Qiy Applications_ exchange _data by reference_ rather then by value.
This goes as follows:
* A _Qiy Application_ requests a reference for the data (_Data Reference_).
* The _Qiy Application_ receives a _Data Reference_.
* The _Qiy Application_ uses the _Data Reference_ to acquire the data.

### 5.5.1 Service by Reference
In Qiy providing data is viewed as a service and requesting data as an operation of this service, so the 'data by reference'-pattern is implemented as using a Service by Reference-pattern:
* A _Qiy Application_ requests an _Operation Reference_ (_Operation Reference Request_).
* A _Operation Reference_ is created by registrating the specification of the operation _Operation Specification_ and returned (_Operation Registration_).
* The _Qiy Application_ uses the _Data Reference_ to acquire the data (_Operation Execution_).

### 5.5.1 Request data reference
The _Qiy Application_ of a _Relying Party_ can request an _Individual_ for a data reference as follows:
* The _Qiy Application_ sends a _Operation Reference Request Message_ using the _Connection_ of the _Individual_.
* The _Qiy Application_ receives the _Operation Reference_ in an _Operation Reference Message_.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.4.2 Create reference
A _Qiy Application_ can create an _Operation Reference_ using a specification of the operation (_Operation Specification_).
This goes as follows:
* The _Qiy Application_ uses the _Operation Specification_ in an _Operation Registration Request_ to the _Qiy Node_ it is linked with.
* The _Qiy Node_ creates the _Operation Reference_ and returns it.

### 5.5.1 Request data
The _Qiy Application_ of a _Relying Party_ can obtain data using a _Data Reference_ / _Operation Reference_. 
This goes as follows:
* The _Qiy Application_ uses the _Operation Reference_ in a _Operation Execution Request_ to its _Qiy Node_.
* The _Qiy Node_ returns the requested data.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.2 Provide data
The _Data Provider_ produces the data using his _Service Endpoint_.
This does not involve any of the _Qiy Applications_ of the _Data Provider_ nor his _Qiy Node_.

![Data Provider: Provide data](./images/data-provider--provide-data.png)

# 6 The Qiy Node Layer
This chapter describes the _Qiy Node Layer_ and how it supports the upper layers.

## 6.1 Access Provider
The services of this layer can be provided by an _Access Provider_:
* An _Access Provider_ can provide _Qiy Nodes_.
* An _Access Provider_ can host _Qiy Nodes_.

### 6.1.1 Portability
An _Access Provider_ can offer _Qiy Node_-services to _Qiy Users_, but must enable _Qiy Users_ to easily transfer the services to a different _Access Provider_.

## 6.2 Qiy Node
A _Qiy Node_ is een _Technology Service_ as defined in _Definitions of the Qiy Scheme_.
A _Qiy Node_:
* ... must comply with the rules of the _Qiy Scheme_.
* ... can be hosted on any host (_Node_).
* ... has its own _Transporter_ which ensures secure transport of messages and/or data via Qiy.

### 6.2.1 Qiy Node Protocol
The _Qiy Node Protocol_ describes the interaction between the _Qiy Nodes_ and the underlying layers.
* The _Qiy Node Protocol_ is one of the protocols in the _Qiy Open Standard_.
The _Qiy Node Protocol_ describes for example:
* How a _Qiy Node_ is instantiated.
* How _Qiy Nodes_ create _Connections_ and use them to exchange data, messages or to provide/consume services.

### 6.2.2 Qiy Node API
The _Qiy Node API_ is the _Technology Interface_ of the _Qiy Node_, one of the APIs of the _Qiy Open Standard_.
* The _Qiy Node API_ is intended for use by _Qiy Applications_.

### 6.2.3 Qiy Node Implementation
A _Qiy Node Implementation_ is a software package which can be used to realize a _Qiy Node_.
The _Qiy Scheme_ puts no limit on the number of _Qiy Node Implementation_s, as long as the implementation complies with the _Qiy Open Standard_ and the rules of the _Qiy Scheme_. 

### 6.2.4 Qiy Node Instantiation
A _Qiy Node_ can be created in two ways:
* It can be instantiated by an _Access Provider_. The _Access Provider_ will instantiate it with its own _Transporter_. 
* It can be instantiated by a _Qiy User_ on a _Node_ of his own using a _Qiy Node Implementation_. 
When the second option is chosen, the _Qiy User_ is responsible for obtaining a _Transporter_ and linking it to the _Qiy Node_.

### 6.2.5 Deleting a Qiy Node
In principle, a _Qiy Node_ can be deleted by its owner whenever he wants to do so.
In this case, the _Qiy Node_ will be deleted including persisted data, _Connections_ and the linked _Transporter_.
Related _Consents_ will be withdrawn.

## 6.3 Connect
Two _Qiy Nodes_ can connect by creating a _Path_ between themselves.
* A _Qiy Node_ can connect with zero or more other _Qiy Nodes_.
* A _Qiy Node_ can have zero or more _Paths_ with any other _Qiy Node_.
* A priori, a _Qiy Node_ does not know the identity of the _Qiy Node_ at the other side of a _Path_.

### 6.3.1 Connection Uri
The _Connection Uri_ is the _Uri_ which identifies a _Connection_ for one of the _Qiy Node_ it connects.
* A _Connection_ has two _Connection Uris_; one for each of the two _Qiy Nodes_ it connects.
* The two _Connection Uris_ of one _Connection_ are not related to one another.
* A priori, a _Qiy Node_ does not know the other _Connection Uri_ of a _Connection_.

EXAMPLE: _Connection Uris_ of a _Connection_ between _Qiy Node_ 1 and _Qiy Node_ 2:

_Qiy Node_ | _Connection Uri_
---- | --------------
Qiy Node 1	| http://127.0.0.1:8087/user/connections/user/usernodeB/93590b55-9194-4cf4-944f-2cbceab7dbcd
Qiy Node 2	| http://127.0.0.1:8087/user/connections/user/usernodeA/f96bc541-e98b-449e-bfc5-48ec928e0dc9

#### 6.3.1.1 Security concern
The _Connection Uri_ has only meaning in the context of the _Qiy Node_ that knows it and is useless outside this scope.
For example, the _Uri_ by itself can not be used to exchange a message with the _Qiy Node_ nor any other existing _Qiy Node_.

### 6.3.2 Connect Token
A _Connect Token_ is a token which can be used by a _Qiy Application_ to create a _Connection_.
It consists of:
* a temporary secret
* a _Transport Connect Token_.

A _Connect Token_ has the following properties:
* An expiration setting: Whether the token expires and if so, on what date and time
* A budget: The number of times that the token can be used to create a Connection. 

The properties can not only be set when the token is registered or requested, but also later.
For example, it is possible to reactivate a _Connect Token_ by increasing the budget or inactivate one by changing the expiration.

#### 6.3.2.1 Security concern
The _Connect Token_ can only be used to create a _Connection_ and only so via Qiy, with the help of a _Qiy Application_ and a linked _Qiy Node_.
By itself, it cannot be used for any other purpose, for example gain access to a _Qiy Node_ nor any other parts of the Qiy infrastructuur.

#### 6.3.2.2 Creating a Connect Token
A _Connect Token_ can be created both offline and online:
* A _Connect Token_ can be obtained from the _Qiy Node_ using a _Connect Token Creation Request_ (_Online Connect Token_).
* A _Connect Token_ can be created by a _Qiy Application_ and registered later using a _Connect Token Registration Request_ (_Offline Connect Token_).

The _Offline Connect Token_ allows initiating a _Connection_ (creating a _Connect Token_) even when Qiy is temporarily not available.
However, care must be taken that the created token is unique, especially so for the created _Transport Connect Token_.

#### 6.3.2.3 Creating a Transport Connect Token
A _Qiy Node_ will never create a _Transport Connect Token_:
* In case of an _Online Connect Token_: The _Qiy Node_ will obtain a _Transport Connect Token_ from its _Transporter_.
* In case of an _Offline Connect Token_: The _Qiy Node_ will compose a _Transport Connect Token_ using the _Connect Token_ provided by the _Qiy Application_ and register it at its _Transporter_.

### 6.3.3 Connecting
Two _Qiy Nodes_ connect as follows:
* The _Qiy Node_ of the _Proposer_ either 1) obtains a _Transport Connect Token_ from the _Transporter_ or 2) from a linked _Qiy Application_ in a _Connection Create Request_.
* The _Qiy Node_ either 1) provides the _Transport Connect Token_ to the _Qiy Application_ or 2) registers the _Transport Connect Token_ at its _Transporter_.
* The _Transport Connect Token_ is made available (partly out-of-bands, for example in a _Connect Proposal_) to the _Qiy Node_ of the _Accepter_.
* The _Qiy Node_ of the _Accepter_ uses its _Transporter_ to create a _Path_ using the _Transport Connect Token_.
Each accepted _Path Creation Request_ leads to a new _Path_, irrespective of the number of existing _Paths_ between the two _Qiy Nodes_.

### 6.3.4 Deleting a Connection
A _Connection_ can be deleted with a _Connection Delete Request_.
The _Connection_ will be deleted completely, including any persisted data and/or messages and underlying _Paths_.
Any related _Consents_ will be withdrawn.

## 6.4 Consent
A _Consent_ is a permission given by an _Individual_ to a _Relying Party_ defining what _Personal Data_ a _Relying Party_ is allowed to use for a provided _Service_ and under what the terms.
A _Consent_ has the following properties:
* a _Consent Uri_
* a _Consent Service Descriptor_
* a _Consent Data Descriptor_

### 6.4.1 Consent Uri
The _Consent Uri_ is an _Uri_ used to identify a _Consent_.

### 6.4.2 Consent Service Descriptor
The _Consent Service Descriptor_ is a _Service Descriptor_ which indicates the _Service_ that the _Consent_ applies to.
A _Service Descriptor_ can be used to obtain a description of a _Service_ (_Service Description_) with the help of the _Service Library_.

### 6.4.3 Consent Data Descriptor
The _Consent Data Descriptor_ is a _Data Descriptor_ which indicates the _Personal Data_ that the _Consent_ applies to.
A _Data Descriptor_ can be used to obtain a description of _Data_ (_Data Description_) with the help of the _Service Library_.

#### 6.4.3.1 Privacy concern
A _Relying Party_ can only ask _Consent_ for _Personal Data_ that can be provided by one of the available _Data Providers_, eg for which a _Data Descriptor_ exists in the _Service Library_.
  
## 6.5 Qiy Node Request
A Qiy Node Request is a _Http Request_ for a _Qiy Node_. 
_Qiy Node Requests_ are only accepted when they are correctly authenticated with:
* the Node Id.
* an actual timestamp
* a digital signature over the _Node Id_, the timestamp and the contents of the body of the request made with the private key

## 6.6 Qiy Node Requests
This section gives an overview of the _Qiy Node Requests_.
Details of _Qiy Node Requests_ can be found in the _Qiy Node API_.

### 6.6.1 Connect Token Creation Request
Connect Token Creation Request
Met dit request kan een _Connect Token_ worden gecre&euml;erd door the _Qiy Node_.

### 6.6.2 Connect Token Registration Request
Connect Token Registration Request
Met dit request kan een _Connect Token_ worden geregistreerd.

### 6.6.3 Connect Token Update Request
The Connect Token Update Request is a _Qiy Node Request_ that can be used to update a _Connect Token_.

### 6.6.4 Connection Create Request
The Connection Create Request is a _Qiy Node Request_ that can be used to create a _Connection_ with a _Connect Token_.

### 6.6.5 Connection Delete Request
The Connection Delete Request is a _Qiy Node Request_ that can be used to delete a _Connection_.

### 6.6.6 Connections Request
The Connections Request is a _Qiy Node Request_ that can be used to obtain a list of all the _Connections_ of a _Qiy Node_.

### 6.6.7 Consent Denied Request
The Consent Denied Request is a _Qiy Node Request_ that can be used to record the denial of a _Consent_.

### 6.6.8 Consent Granted Request
The Consent Granted Request is a _Qiy Node Request_ that can be used to record the granting of a _Consent_.

### 6.6.9 Consent Request
The Consent Request is a _Qiy Node Request_ which can be used to request for a _Consent_.

### 6.6.10 Consent Withdrawn Request
The Consent Withdrawn Request is a _Qiy Node Request_ that can be used to record the withdrawal of a _Consent_.

### 6.6.11 Consents Request
The Consents Request is a _Qiy Node Request_ that can be used to obtain a list of all the _Consents_ of a _Qiy Node_.

### 6.6.12 Message Post Request
The Message Post Request is a _Qiy Node Request_ that can be used to post a _Qiy Node Message_.

### 6.6.13 Messages Request
The Messages Request is a _Qiy Node Request_ that can be used to obtain a list of all the _Messages_ of a _Qiy Node_.

### 6.6.14 Operation Execution Request
The Operation Execution Request is a _Qiy Node Request_ that can be used to command the execution of an _Operation_ by reference using an _Operation Reference_.

### 6.6.15 Operation Registration Request
The Operation Registration Request is a _Qiy Node Request_ that can be used to obtain an _Operation Reference_ by registrating an _Operation Specification_.

### 6.6.16 Operation References Request
The Operation References Request is a _Qiy Node Request_ that can be used to obtain a list of all the _Operation References_ of a _Qiy Node_.

### 6.6.17 Source Candidates Request
The Source Candidates Request is a _Qiy Node Request_ to obtain candidate _Providers_ for a _Service_.

### 6.6.18 Source Registration Request
The Source Registration Request is a _Qiy Node Request_ to register a _Provider_ as source for a _Service_.
 
## 6.7 Qiy Node Message
A Qiy Node Message is a _Message_ that is exchanged using a _Connection_.
_Qiy Node Messages_ can be sent with the _Message Post Request_, obtained using a _Messages Request_ and monitored with _Qiy Node Events_ like _Message Received Event_.

## 6.8 Qiy Node Messages
This section gives an overview of the _Qiy Node Messages_.
Details of _Qiy Node Messages_ can be found in the _Qiy Node Protocol_.

### 6.8.1 Consent Denied Message
The Consent Denied Message is a _Qiy Node Message_ which can be used to communicate the denial of a _Consent_.

### 6.8.2 Consent Granted Message
The Consent Granted Message is a _Qiy Node Message_ which can be used to communicate the granting of a _Consent_.

### 6.8.3 Consent Request Message
The Consent Request Message is a _Qiy Node Message_ which can be used to request for a _Consent_.

### 6.8.4 Operation Reference Message
Operation Reference Message
This message can be used to convey _Operation References_.
 
### 6.8.5 Operation Reference Request Message
Operation Reference Request Message
This message can be used to request for _Operation References_.
 
## 6.9 Qiy Node Event
A Qiy Node Event is a Technology Event of a _Qiy Node_.

## 6.10 Qiy Node Events
This section gives an overview of the _Qiy Node Events_.
Details of _Qiy Node Events_ can be found in the _Qiy Node Protocol_.

### 6.10.1 Connection Created Event
The Connection Created Event is a _Qiy Node Event_ that is generated when a _Connection_ has been created.

### 6.10.2 Consent Withdrawn Event
The Consent Withdrawn Event is a _Qiy Node Event_ that is generated when a _Consent_ has been withdrawn.

### 6.10.3 Message Received Event
The Message Received Event is a _Qiy Node Event_ that is generated when a _Qiy Node Message_ has been received.

### 6.10.4 Operation Reference Received Event
The Operation Reference Received Event is a _Qiy Node Event_ that is generated when a _Qiy Node_ has received a new _Operation Reference_.

### 6.10.5 Source Candidate Event
The Source Candidate Event is a _Qiy Node Event_ that is generated when a _Qiy Node_ has received a new _Source Candidate_ for a _Consent_.

# 7 The Service Layer
The _Service Layer_ provides the following _Technology Services_ to support the provisioning and consumption of _Services_ via Qiy:
* _Service Endpoints_
* _Service Library_
* _Consent Service_

## 7.1 Access Provider
The _Service Library_ and _Consent Service_ are both provided by an _Access Provider_.

### 7.1.1 Portability
The _Qiy Scheme_ prescribes that one can easily change to a different _Access Provider_ for these services.

## 7.2 Service
In general, a _Service_ is an 'information society service' as defined in the _GDPR_, with the following enhancements:
* A _Service_ can be consumed with the use of one or more _Operations_.
* A _Service_ is provided by a _Provider_.
* A _Provider_ can offer one or more _Services_.
* One _Service_ can be offered by one or more _Providers_.
* The _Services_ that a _Provider_ offers are described in a _Service Catalogue_.
* The _Services_ that an _Individual_ consumes are described in his _Service Portfolio_.

As for Qiy, the following definitions apply:
* Both _Relying Parties_ and _Data Providers_ are _Providers_.

## 7.3 Service Endpoints
A _Service Endpoint_ is a _Technology Service_ provided by a _Provider_ to allow the consumption of his _Services_:
* A _Provider_ can employ one or more _Service Endpoints_.
* A _Service Endpoint_ can be used for one or more _Services_.
* A _Service_ can be consumed with the use of one or more _Service Endpoints_.

For example, a _Service Endpoint_ may be used by a _Data Provider_ to disclose the _Personal Data_ from one of his databases.

## 7.4 Service Library
The _Service Library_ is used for:
* _Data Descriptions_
* _Providers_
* _Service Catalogues_
* _Service Descriptions_

## 7.5 Consent Service
A _Consent Service_ is used for maintaining _Consents_ and their status.
A _Consent_ can be accessed by both of the involved _Qiy Users_: the _Individual_ and the _Provider_.

* In principle, only an _Individual_ can withdraw a _Consent_ he has granted before.
* A _Provider_ can only obtain _Personal Data_ under a _Consent_ which has not been withdrawn.

# 8 The Transport Layer
The _Transport Layer_ supports the secure transmission of messages (_Transport Messages_) over _Paths_ between _Transporters_.

## 8.1 Access Provider
The services of this layer are only provided by an _Access Provider_.

### 8.1.1 Portability
The _Qiy Scheme_ prescribes that one can easily switch _Access Provider_ for these services.

## 8.2 Transporter
A _Transporter_ is a _Technology Service_ which allows the secure transmission of messages and/or data.
* A _Transporter_ must comply with the rules of the _Qiy Scheme_.
* A _Transporter_ is hosted on a _Carrier Node_.
* Each _Qiy Node_ has its own _Transporter_.

A _Transporter_ can be used for:
* Creating _Paths_ with other _Transporters_.
* Securely transmitting _Transport Messages_ over these _Paths_.

## 8.2.1 Transport Protocol
The _Transport Protocol_ describes the interaction between _Transporters_ and the underlying layer.
The protocol is one of the protocols of the _Qiy Open Standard_.

## 8.2.2 Transporter API
The _Transporter API_ is the _Technology Interface_ of the _Transporter_, one of the APIs of the _Qiy Open Standard_.
* The _Transporter API_ is intended for use by _Qiy Nodes_.

## 8.2.3 Transporter Implementation
A _Transporter Implementation_ is a software package which can be used to realize a _Transporter_.
The _Qiy Scheme_ puts no limit on the number of _Transporter Implementation_s, as long as the implementation complies with the _Qiy Open Standard_ and the rules of the _Qiy Scheme_. 

## 8.2.4 Transporter Instantiation
A _Transporter_ can only be instantiated by an _Access Provider_.

## 8.2.5 Deleting a Transporter
A _Transporter_ can be deleted by its _Qiy Node_.
In this case, the _Transporter_ will be deleted including any persisted data and _Routes_.

## 8.3 Path
A _Path_ is a logical connection between two _Transporters_ that can be used to exchange _Transport Messages_.
Physically seen, the _Path_ may be dynamic and stretch over several _Carriers_.

### 8.3.1 Path Creation
A _Path_ can be created by a _Transporter_ with a _Transport Connect Token_.

### 8.3.2 Deleting a Path
A _Path_ can be deleted by either of the ending _Transporters_. 
The _Path_ will be deleted including any persisted data and/or messages.

# 9 The Carrier Layer
The _Carrier Layer_ supports the creation of _Paths_ and the secure transport of messages over them.

## 9.1 Access Provider
The services of this layer are only provided by an _Access Provider_.

### 9.1.1 Portability
The _Qiy Scheme_ prescribes that one can easily switch _Access Provider_ for these services.

## 9.2 Carrier
The _Carrier_ is _Technology Service_ which can be used for:
* To obtain a _Transporter_.
* To create _Paths_.
* To safely transport messages between _Carriers_.
* To obtain a _Qiy Node_.

The _Carrier_ comes with the following rules:
* A _Carrier_ must comply with the rules of the _Qiy Scheme_.
* A _Carrier_ must support the _Carrier API_.

## 9.2.1 Carrier Protocol
The _Carrier Protocol_ describes the interaction between _Carriers_.
The protocol is part of the _Qiy Open Standard_.

## 9.2.2 Carrier API
The _Carrier API_ is the _Technology Interface_ of the _Carrier_ and is part of the _Qiy Open Standard_.

## 9.2.3 Carrier Implementation
A _Carrier Implementation_ is a software package which can be used to realize a _Carrier_.
The _Qiy Scheme_ puts no limit on the number of _Carrier Implementations_, as long as the implementation complies with the _Qiy Open Standard_ and the rules of the _Qiy Scheme_. 

## 9.3 Carrier Node
A _Carrier Node_ is a _Node_ which hosts one or more _Carriers_.
* The _Carrier Node_ is provided by an _Access Provider_.
* The _Access Provider_ can provide one or more _Carrier Nodes_.

# 10 Definitions
This document uses the following definitions:

Term	| Definition
------- | ----------
Access Provider	| An organization which provides _Qiy Users_ access to the _Qiy Trust Framework_, either an _Issuer_ or a _Service Provider_.
Access Principle	| The principle which authorizes the access of an _Individual_ to his _Personal Data_, one of the _Qiy Trust Principles_.
Accepter	| A _Business Role_ for a _Qiy User_ who is creating a _Connection_ using a _Connect Token_ that is provided by a _Proposer_.
Application Connect Token	| A _Token_ that is used by _Qiy Applications_ to create _Connections_.
Application Interface	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Application Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Application Provider	| A _Bussiness Role_ for suppliers of _Qiy Applications_.
Application Service	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Architectural Layers of the Qiy Scheme	| The architectural layers of the _Qiy Scheme_: the _User Layer_, the _Application Layer_, the _Qiy Node Layer_, the _Service Layer_, the _Transport Layer_ and the _Carrier Layer_.
Binding Individual Rights	| One of the documents of the _Qiy Scheme Rulebook_.
Binding Principles for Relying Parties and Data Providers	| One of the documents of the _Qiy Scheme Rulebook_.
Business Actor	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Business Object	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Business Process	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Business Role	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Carrier	| A _Technology Service_ that provides the services of the _Carrier Layer_. 
Carrier API	| _Technology Interface_ of the _Carrier_.
Carrier Implementation	| A software package which can be used to realize a _Carrier_.
Carrier Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Carrier Node	| A _Node_ which hosts one or more _Carriers_.
Connect Proposal	| A _Business Object_ for a proposal to connect via Qiy.
Connect Token	| A Literal used to create a _Connection_.
Connection	| A connection between two _Qiy Nodes_.
Connection Uri	| _Uri_ voor the id van een _Connection_.
Consent	| As defined in the _GDPR_.
Consent Data Descriptor	| _Data Descriptor_ in een _Service Description_ voor the beschrijving van the voor the _Service_ benodigde _Personal Data_.
Consent Service	| A _Technology Service_ used to maintain _Consents_ and their status.
Consent Service Description	| A _Service Description_ of the _Service_ for which a _Consent_ applies.
Consent Service Descriptor	| A _Service Descriptor_ of a _Consent Service Description_.
Consent Uri	| A _Uri_ which is used to identify a _Consent_.
Data by Reference	| A pattern for exchanging data indirectly using a _Data Reference_, see also _Service by Reference_.
Data Description	| A description of data.
Data Descriptor	| An _Uri_ which can be used to identify and obtain a _Data Description_.
Data Provider	| A _Business Role_ as defined in _Definitions of the Qiy Scheme_.
Data Provider Agreement	| An agreement required for _Data Providers_.
Data Reference	| An _Operation Reference_ which can be used to obtain _Personal Data_ of an _Individual_.
Data Subject	| As defined in the _GDPR_.
Definitions of the Qiy Scheme	| One of the documents of the _Qiy Scheme Rulebook_.
GDPR	| General Data Protection Regulation, see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 
Governance Model for the Qiy Scheme	| Governance Model for the _Qiy Scheme_, see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/.
HTTP Request	| As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
Individual	| A _Business Role_ of a _Qiy User_ as defined in _Definitions of the Qiy Scheme_.
Issuer	| A _Business Role_ for an _Access Provider_ that provides services to natural persons, see _Definitions of the Qiy Scheme_.
Licence Agreement Application Provider	| A licence agreement for _Application Providers_.
Licence Agreement Issuer	| A licence agreement for _Issuers_, the template of which is part of the _Qiy Scheme Rulebook_.
Licence Agreement Service Provider	| A licence agreement for _Service Providers_, the template of which is part of the _Qiy Scheme Rulebook_.
Literal	| A fixex value, see https://en.wikipedia.org/wiki/Literal_(computer_programming).
Node	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Operation | A 'sub-service' which can be used to consume a _Service_.
Operation Reference	| A _Business Object_ used by the _Service by Reference_-pattern.
Operation Specification | A specification of a _Http Request_ for the execution of an _Operation_.
Personal Data	| As defined in the _GDPR_.
Path	| A connection between two _Transporters_ which is used to exchange _Transport Messages_.
Proposer	| A _Business Role_ for a _Qiy User_ that initiates creating a _Connection_ by providing a _Connect Token_, sometimes using a _Connect Proposal_.
Provider	| A _Business Role_ for a _Qiy User_ that is providing one or more _Services_ using Qiy, that is a _Data Provider_ or a _Relying Party_.
Qiy Application	| An _Application Service_ or software that is authorized for use with Qiy.
Qiy Application Protocol	| A protocol for the interactions between _Qiy Applications_ and the underlying layers.
Qiy Foundation	| A foundation dedicated to putting people back in control of their personal data while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.
Qiy Foundation Member	| A member of the _Qiy Foundation_, see https://www.qiyfoundation.org/membership/.
Qiy Node	| A _Technology Service_ as defined in _Definitions of the Qiy Scheme_.
Qiy Node API	| A _Technology Interface_ of the _Qiy Node_ that is part of the _Qiy Open Standard_.
Qiy Node Implementation	| A software package which can be used to realize a _Qiy Node_.
Qiy Node Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Qiy Node Protocol	| A protocol describing the interaction between _Qiy Nodes_ and the underlying layers.
Qiy Open Standard	| A set of open standards for Qiy, maintained by the _Work Stream Functionality & Technology_, see https://www.qiyfoundation.org/qiy-scheme/workstreams/.
Qiy Scheme	| See https://www.qiyfoundation.org/qiy-scheme/.
Qiy Scheme Rulebook	| A set of documents concerning governance, legal and technical aspects of the _Qiy Scheme_, see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/
Qiy Trust Framework	| As defined in _Definitions of the Qiy Scheme_.
Qiy Trust Principles	| As defined in _Definitions of the Qiy Scheme_, see https://www.qiyfoundation.org/qiy-trust-principles/.
Qiy User	| A _Business Actor_; defined as 'User' in _Definitions of the Qiy Scheme_.
Reference	| A _Literal_.
Relying Party	| A _Business Role_ as defined in _Definitions of the Qiy Scheme_.
Relying Party Agreement	| An agreement that is required for _Relying Parties_.
Request	| A _Business Object_: a message requesting something.
Transport Message	| A message that is exchanged over a _Path_ between two _Transporters_.
Transport Message Description	| A _Data Description_ that describes the contents, format and encryption (if any) of a _Transport Message_.
Service	| An 'information society service' as defined in the _GDPR_.
Service by Reference	| A pattern for consuming _Services_ indirectly using references (_Operation Reference_).
Service Discovery	| A _Business Process_ to find _Providers_ for a given _Service_.
Service Endpoint	| A _Technology Service_ provided by a _Provider_ to allow the consumption of his _Services_.
Service Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Service Library	| A _Technology Service_ that supports the _Service_ processes of the _Individuals_ and the _Providers_.
Service Provider	| A _Business Role_: an _Access Provider_ which provides business-to-business services as defined in _Definitions of the Qiy Scheme_.
Service Source	| A _Provider_ that can or is providing a specific _Service_.
Technology Event	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Technology Interface	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
Technology Service	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 
Transport Connect Token	| A Literal used to create _Paths_.
Transport Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Transport Protocol	| A protocol that is part of the _Qiy Open Standard_ and which describes the interaction between _Transporters_ and the lower layers.
Transporter	| A _Technology Service_ that provides transport services.
Transporter API	| _Technology Interface_ of a _Transporter_.
Transporter Implementation	| A software package which can be used to realize a _Transporter_.
User Layer	| One of the _Architectural Layers of the Qiy Scheme_.
Uri	| See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
Url	| See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
Work Stream Functionality & Technology	| One of the work streams of the _Qiy Foundation_, see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

