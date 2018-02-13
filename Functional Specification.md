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
			1. [Webpage with QR Code](#4433-webpage-with-qr-code)
			1. [Webpage with button](#4434-webpage-with-button)
			1. [Accepting a Connect Proposal by scanning a QR code](#4435-accepting-a-connect-proposal-by-scanning-a-qr-code)
			1. [Accepting a Connect Proposal with a button click](#4436-accepting-a-connect-proposal-with-a-button-click)
			1. [Confirmation](#4437-confirmation)
	1. [Setup](#45-setup)
		1. [Relying Party](#451-relying-party)
		1. [Data Provider](#452-data-provider)
		1. [Individual](#453-individual)
	1. [Subscribe](#46-subscribe)
	1. [Consent](#47-consent)
	1. [Routing](#48-routing)
	1. [Source](#49-source)
	1. [Session](#410-session)
	1. [Application Examples](#411-application-examples)
		1. ['Help, I am lost!'](#4111-help,-i-am-lost!)
		1. ['Let us know'](#4112-let-us-know)
		1. [Login](#4113-login)
		1. [Share Medical Data](#4114-share-medical-data)
		1. ['Have you seen this man?'](#4115-have-you-seen-this-man)
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
		1. [Request data reference](#552-request-data-reference)
		1. [Create reference](#553-create-reference)
		1. [Request data](#554-request-data)
		1. [Provide data](#555-provide-data)
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
	1. [Transport Protocol](#83-transport-protocol)
	1. [Transporter API](#84-transporter-api)
	1. [Transporter Implementation](#85-transporter-implementation)
	1. [Transporter Instantiation](#86-transporter-instantiation)
	1. [Deleting a Transporter](#87-deleting-a-transporter)
	1. [Path](#88-path)
		1. [Path Creation](#881-path-creation)
		1. [Deleting a Path](#882-deleting-a-path)
1. [The Carrier Layer](#9-the-carrier-layer)
	1. [Access Provider](#91-access-provider)
		1. [Portability](#911-portability)
	1. [Carrier](#92-carrier)
	1. [Carrier Protocol](#93-carrier-protocol)
	1. [Carrier API](#94-carrier-api)
	1. [Carrier Implementation](#95-carrier-implementation)
	1. [Carrier Node](#96-carrier-node)
1. [Definitions](#10-definitions)

# 1 Introduction
Qiy, or rather: the [Qiy Scheme](#qiy-scheme), puts people back in control of their [Personal Data](#personal-data) while creating value for organizations that process it ([Relying Parties](#relying-partie)).


## 1.1 Purpose

The document is aimed at people who know that Qiy puts people back in control of their [Personal Data](#personal-data), but who want or need to know the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.

## 1.2 Reader guidance

* Privacy officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Security officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Information analysts are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer) and [5 The Application Layer](#5-the-application-layer).
* Application developers are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer), [5 The Application Layer](#5-the-application-layer) and [6 The Qiy Node Layer](#6-the-qiy-node-layer).
* Systems engineers are advised to read chapters [3 Architectural Description](#3-architectural-description), [8 The Transport Layer](#8-the-transport-layer) and [9 The Carrier Layer](#9-the-carrier-layer).

# 2 Overview

This chapter gives an overview of this document.
* [2.1 Data Reuse](#21-data-reuse) describes how data can be reused with Qiy.
* [3 Architectural Description](#3-architectural-description) describes the [Architectural Layers](#architectural-layers) and addresses various concerns like privacy and security.
* [4 The User Layer](#4-the-user-layer) describes the setup and processes of the Data Reuse scenario at the user level.
* [5 The Application Layer](#5-the-application-layer) describes the processes at the application level.
* [6 The Qiy Node Layer](#6-the-qiy-node-layer) describes the same at the Qiy Node level.
* [7 The Service Layer](#7-the-service-layer) describes the [Service Layer](#service-layer) support.
* [8 The Transport Layer](#8-the-transport-layer) describes the [Transport Layer](#transport-layer) support.
* [9 The Carrier Layer](#9-the-carrier-layer) describes the [Carrier Layer](#carrier-layer) support.
* [10 Definitions](#10-definitions) contains the definitions used in this document.

## 2.1 Data Reuse

This document describes how Qiy realizes a Data Reuse scenario in which a [Data Subject](#data-subject) ([Individual](#individual)) reuses his [Personal Data](#personal-data) stored at one organization ([Data Provider](#data-provider)) and provide it to another organization ([Relying Party](#relying-party)) to consume one of its services.
Qiy can also be used for other applications, examples of wich can be found in [4.11 Application examples](#411-application-examples)

In essence, the Data Reuse goes as follows:
* The [Individual](#individual) subscribes to a service.
* The [Relying Party](#relying-party) asks the [Individual](#individual) for the data it needs to provide the service.
* The [Individual](#individual) retrieves the data from a [Data Provider](#data-provider).
* The [Individual](#individual) provides the data to the [Relying Party](#relying-party).

![Qiy Data Reuse](./images/qiy-data-reuse.png)

### 2.1.1 Privacy concern

The Data Reuse scenario shows that the data is transferred to the [Relying Party](#relying-party) by choice of the [Individual](#individual).
This breaks the chain of responsibility for the [Data Provider](#data-provider); the responsibility for correct processing of the data does not extend to any processing that takes place after the handover to the [Individual](#individual). 

# 3 Architectural Description

This chapter describes the major entities of Qiy and their relations with the help of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme) and addresses how Qiy addresses concerns like security and privacy.

## 3.1 Architectural Layers
The realization of the scenario is described using the following layers:

![Layers](./images/layers.png)

## 3.2 Privacy

Qiy has been conceived with the aim to put people back in control of their [Personal Data](#personal-data), hence making privacy the primary concern of Qiy.
The aim has been elaborated in a set of principles called the [Qiy Trust Principles](#qiy-trust-principles) and technical, legal and governance rules, all of which are maintained by the [Qiy Foundation](#qiy-foundation) and the [Qiy Foundation Members](#qiy-foundation-member).

The realization of the Data Reuse as described in this document demonstrates that a natural person ([Individual](#individual)) is in control:
* The [Individual](#individual) can securily exchange data and/or messages with another person or organization ([Qiy User](#qiy-user)) via Qiy, using connections, see [4 The User Layer](#4-the-user-layer).
* The [Individual](#individual) controls what [Qiy Users](#qiy-user) he connects with and, in principle, when he wants to end it.
* When an [Individual](#individual) connects with a [Qiy User](#qiy-user) that is providing a [Service](#service) via Qiy ([Provider](#provider)), the [Individual](#individual) is provided with the identity of the latter, but not the other way around.
* The [Individual](#individual) can access his [Personal Data](#personal-data) that is kept by another [Qiy User](#qiy-user) ([Data Provider](#data-provider)) as a result of the [Access Principle](#access-principle), one of the [Qiy Trust Principles](#qiy-trust-principles).
* The [Individual](#individual) controls what data he shares with what [Provider](#provider) ([Relying Party](#relying-party)) and under what terms using proveable [Consents](#consent).
* [Qiy Users](#qiy-user) use applications that are authorized for use with Qiy ([Qiy Applications](#qiy-application)).
* Access to Qiy, data exchange via Qiy, consent services and potentially [Qiy Nodes](#qiy-node) are provided by [Access Providers](#access-provider).


All parties involved are bound by the rules of the [Qiy Scheme](#qiy-scheme):
* [Providers](#provider) are bound by the [Binding Individual Rights](#binding-individual-right) and the [Binding Principles for Relying Parties and Data Providers](#binding-principles-for-relying-parties-and-data-provider).
* [Access Providers](#access-provider) are bound by the [Licence Agreement Issuer](#licence-agreement-issuer) or the [Licence Agreement Service Provider](#licence-agreement-service-provider).
* [Application Providers](#application-provider) can only develop and produce [Qiy Application](#qiy-application)-services and/or software with a [Licence Agreement Application Provider](#licence-agreement-application-provider).

## 3.3 Security

As described above, privacy is at the heart of Qiy and security being a 'conditio sine qua no' for this, it is also addressed by the rules of the [Qiy Scheme](#qiy-scheme).

## 3.4 Interoperability

An [Individual](#individual) can only control his [Personal Data](#personal-data), when all concerned systems are interoperable.
This is achieved as follows:
* Applications exchange data and/or messages via Qiy using open standards of the [Qiy Scheme](#qiy-scheme) ([Qiy Open Standard](#qiy-open-standard)).
* Applications exchange self-describing data and/or messages using [Data Descriptions](#data-description) which are available to all concerned parties (via the [Service Library](#service-library)).

## 3.5 Governance

The governance rules are laid down in the [Governance Model for the Qiy Scheme](#governance-model-for-the-qiy-scheme), one of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

## 3.6 Compliancy

The compliancy rules for [Providers](#provider) can be found in the [Binding Principles for Relying Parties and Data Providers](#binding-principles-for-relying-parties-and-data-provider), one of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).


# 4 The User Layer
This chapter describes the [User Layer](#user-layer) and the interaction between the [Relying Party](#relying-party), [Individual](#individual), [Data Provider](#data-provider) and the lower layers for the Data Reuse.

## 4.1 Qiy Users
The organizations and/or persons using Qiy are called [Qiy Users](#qiy-user). They can use Qiy in different [roles](#role); they can use Qiy as a [Relying Party](#relying-party), [Individual](#individual), [Data Provider](#data-provider) or a combination of these.
A business for example will generally use Qiy both as a [Relying Party](#relying-party) (for offering [Services](#service) using reliable [Personal Data](#personal-data)) and as a [Data Provider](#data-provider) (as a source of [Personal Data](#personal-data)).
As for natural persons, most of these will use Qiy as an [Individual](#individual) to control their [Personal Data](#personal-data).

## 4.2 Provider
A [Qiy User](#qiy-user) that provides one or more [Services](#service) to [Individuals](#individual) is said to be (or act in the [Business Role](#business-role) of) '[Providers](#provider)'.
Any [Qiy User](#qiy-user) acting in one or both of the roles [Relying Party](#relying-party) or [Data Provider](#data-provider) is implicitely acting in this role.

## 4.3 Qiy Node
A [Qiy User](#qiy-user) must have a [Qiy Node](#qiy-node). 
[Providers](#provider) can acquire one from an [Access Provider](#access-provider).
[Individuals](#individual) obtain a [Qiy Node](#qiy-node) the first time they use a [Qiy Application](#qiy-application).
Alternatively, [Qiy Users](#qiy-user) may instantiate a [Qiy Node](#qiy-node) themselves using a [Qiy Node Implementation](#qiy-node-implementation) and register it with an [Access Provider](#access-provider).

## 4.4 Connect via Qiy

Two [Qiy Users](#qiy-user) can connect via Qiy by creating a connection between their [Qiy Nodes](#qiy-node) ([Connection](#connection)).
The [Connection](#connection) can be initiated by either of the two [Qiy Users](#qiy-user).
The [Qiy User](#qiy-user) initiating the [Connection](#connection) is called the [Proposer](#proposer), the other one [Accepter](#accepter).
This goes as follows:
* The [Proposer](#proposer) uses a [Qiy Application](#qiy-application) to generate a token (see [4.4.1 Generate token](#441-generate-token)) and to compose a [Connect Proposal](#connect-proposal).
* The [Proposer](#proposer) provides it out-of-band to the [Accepter](#accepter), for example by lettre, see [4.4.2 Media](#442-media).
* The [Accepter](#accepter) may read the proposal and use a [Qiy Application](#qiy-application) to extract the [Connect Token](#connect-token) and create a new [Connection](#connection) with the [Proposer](#proposer).

As stated before, when a [Connection](#connection) is established, the identity of the [Qiy User](#qiy-user) is provided to the other one if the Qiy User is a [Provider](#provider). 
This information may be used to reuse a formerly created [Connection](#connection) and delete the new [Connection](#connection).

![Users Connect](./images/users-connect.png)

### 4.4.1 Generate token
A [Proposer](#proposer) can create a token using a [Qiy Application](#qiy-application) and the following details:
* Name: The name or pseudonym to use in the [Connect Proposal](#connect-proposal).
* Expiration: Whether the token expires and if so, on what date and time.
* Budget: The number of times that the token can be used to create a [Connection](#connection).

In most cases, the expiration and budget are set by the application.
The Expiration and the Budget can be changed afterwards, for example to re-activate an expired token.

![Generate token](./images/generate-token.png)

 
### 4.4.2 Media
[Qiy Users](#qiy-user) can use different media to connect as illustrated in this diagram:

![Media](./images/Connect.png)

 
#### 4.4.2.1 The web
[Qiy Users](#qiy-user) can connect by transfering a token as a query parameter in a website address:
 
![Connect using a token in a website address](./images/connect-using-a-token-in-a-website-address.png)

 
#### 4.4.2.2 Print
[Qiy Users](#qiy-user) can convert the token to a QR Code and use various 'Print'-media to connect:

![Present proposal containing a QR Code](./images/present-proposal-containing-a-qr-code.png)


The QR Code can be used as follows to create the [Connection](#connection):
 
![Connect using a QR Code](./images/connect-using-a-qr-code.png)
 

### 4.4.3 Examples


#### 4.4.3.1 Connect Proposal

The picture below shows a [Connect Proposal](#connect-proposal) that is generated by an [Individual](#individual) using a mobile app containing a QR Code.
The [Individual](#individual) can use this proposal to invite other [Individuals](#individual) to connect.

![An example of a Connect Proposal](./images/example--connect-proposal--qr-code-on-phone.PNG)

#### 4.4.3.2 Email
The picture below shows an example of a [Connect Proposal](#connect-proposal) in an email:

![An example of a Connect Proposal in an email](./images/example--connect-proposal--email.PNG)

#### 4.4.3.3 Webpage with QR Code
The picture below shows an example of a [Connect Proposal](#connect-proposal) in a webpage which displays a QR code when viewed on a laptop, pc or tablet:

![An example of a Connect Proposal in a webpage with QR code](./images/example--connect-proposal--webpage-laptop-pc-tablet.PNG)

#### 4.4.3.4 Webpage with button
The picture below shows an example of a [Connect Proposal](#connect-proposal) in a webpage which displays a button when viewed on smartphone:

![An example of a Connect Proposal in a webpage with button](./images/example--connect-proposal--webpage-phone.PNG)

#### 4.4.3.5 Accepting a Connect Proposal by scanning a QR code

The picture below shows an example of scanning the QR code in a [Connect Proposal](#connect-proposal) using a [Qiy Application](#qiy-application):

![An example of scanning a QR code](./images/example--connect-proposal--scan-qr-code.PNG)

#### 4.4.3.6 Accepting a Connect Proposal with a button click

When an [Accepter](#accepter) has viewed a webpage with a [Connect Proposal](#connect-proposal) on his phone and clicked the button to accept it, he will be asked to confirm that he will be redirected to a [Qiy Application](#qiy-application):

![An example of confirming the redirect to a Qiy Application](./images/example--connect-proposal--after-the-button-click.PNG)

#### 4.4.3.7 Confirmation

The picture below shows an example of an [Qiy Application](#qiy-application) verifying the acceptance of a [Connect Proposal](#connect-proposal).
The [Qiy Application](#qiy-application) will create the [Connection](#connection) when the [Accepter](#accepter) has confirmed that he wants to [Connect](#connect) with the [Proposer](#proposer).

![An example of confirming the acceptance a Connect Proposal](./images/example--connect-proposal--verify.PNG)


## 4.5 Setup

This section addresses the setup for the Data Reuse

### 4.5.1 Relying Party

In order to be able to offer his services via Qiy, a [Relying Party](#relying-party) has met the following preconditions:
* The [Relying Party](#relying-party) has acquired access to Qiy with the help of an Access Provider.
* The [Access Provider](#access-provider) has verified and registered the identity of the [Relying Party](#relying-party) for use in Qiy.
* The [Service Library](#service-library) contains the [Service Catalogue](#service-catalogue) of the [Relying Party](#relying-party) defining the provided services.
* The [Service Library](#service-library) contains [Service Descriptions](#service-description) for all the provided services, which also includes the terms of use, especially with regard to Personal Data.

### 4.5.2 Data Provider

In order to be able to provide the [Personal Data](#personal-data) via Qiy, a [Data Provider](#data-provider) has met the following preconditions:
* The [Data Provider](#data-provider) has acquired access to Qiy with the help of an Access Provider.
* The [Access Provider](#access-provider) has verified and registered the identity of the [Data Provider](#data-provider) for use in Qiy.
* A [Service Endpoint](#service-endpoint) is available to access the data.
* The [Service Library](#service-library) contains the [Service Endpoint API](#service-endpoint-api) which describes how the data can be obtained.
* The [Service Library](#service-library) contains [Data Descriptions](#data-description) for the available data.
* The [Service Library](#service-library) contains the [Service Catalogue](#service-catalogue) of the [Data Provider](#data-provider) defining the provided data services and the related endpoints.
* The [Service Library](#service-library) contains [Service Descriptions](#service-description) for the provided data services.

### 4.5.3 Individual

In order to be able to reuse [Personal Data](#personal-data) via Qiy, an [Individual](#individual) has met the following preconditions:
* The [Individual](#individual) has access to his [Personal Data](#personal-data) stored by one or more [Data Providers](#data-provider).
* The [Individual](#individual) has access to a personal [Qiy Node](#qiy-node).
* The [Individual](#individual) is using a [Qiy Application](#qiy-application) which is linked to his [Qiy Node](#qiy-node).

## 4.6 Subscribe

Data Reuse starts with an Individual subscribing to a service, but only after considering and accepting the terms of use, including those regarding the use of Personal Data.
When an [Individual](#individual) subscribes to a service, the subscription is registered by the [Qiy Application](#qiy-application), so:
* The subscribed service is recorded using the [Service Portfolio](#service-portfolio) of the [Individual](#individual).
* The record shows:
	* the start datetime of the subscription.
	* the [Provider](#provider) of the service (the [Relying Party](#relying-party)).
	* what service is provided (using the [Service Library](#service-library)).
	* the related [Consent](#consent).

## 4.7 Consent

When a request for data is received, it is checked with the granted consents. If the request is not authorized by an active granted consent, this may be resolved by granting one, after which the data request is processed.
In other cases, the request will not be accepted and no data will be returned.

## 4.8 Routing

When all related conditions are met, a request for data from a [Relying Party](#relying-party) is processed as follows:
* The [Service Portfolio](#service-portfolio) of the [Individual](#individual) is consulted to find the [Data Provider](#data-provider) or [Data Providers](#data-provider) and related [Service Endpoint API](#service-endpoint-api).
* Using the API, requests are created and used to obtain the data from the [Service Endpoints](#service-endpoint).
* The received data is forwarded to the [Relying Party](#relying-party).

## 4.9 Source

When a [Relying Party](#relying-party) has requested for data, the [Service Portfolio](#service-portfolio) is used to look up the data source: the [Provider](#provider) or [Providers](#provider) that will provide the data ([Service Source](#service-source)).
This can be the [Individual](#individual) himself, for self-declared data, but it can also be one or more [Data Providers](#data-provider).
The source of the data may have been defined before at the time of subscription, but if that it is not the case, the [Individual](#individual) will be asked to make a selection from a list of suitable [Data Providers](#data-provider) ([Servive Discovery](#servive-discovery)).
The list will be generated using the [Service Catalogues](#service-catalogue) from the [Service Library](#service-library).
The [Service Portfolio](#service-portfolio) will be updated with the outcome.

## 4.10 Session

A Service Endpoint will only process a request when issued over an active Session. This Session may be started earlier, for example when the Individual selects a Data Provider as a source, but a new Session will be started if need be.
More often then not, this may require input from the Individual.
The session credentials are persisted in the [Service Catalogue](#service-catalogue) of the Individual.

## 4.11 Application Examples

This section gives some examples of other applications of Qiy.

### 4.11.1 'Help, I am lost!'

The [Connect Proposal](#connect-proposal) can be used on a badge to contact the parents of a wandering child:
![Scan the code to contact my parents](./images/example-application--help-iam-lost.PNG)

### 4.11.2 'Let us know'

The [Connect Proposal](#connect-proposal) can be used to react anonymously to a news item in a newspaper:

![Scan the code to let us know](./images/example-application--let-us-know.PNG)

### 4.11.3 Login

The [Connect Proposal](#connect-proposal) can be used by websites as a user friendly login alternative:

![Login](./images/example-application--login.PNG)

### 4.11.4 Share Medical Data

The [Connect Proposal](#connect-proposal) can be used to anonymously share medical data for a visit at a medical facility:

![Share medical data](./images/example-application--share-medical-data.PNG)

### 4.11.5 'Have you seen this man?'

The [Connect Proposal](#connect-proposal) can be used to anonymously contribute to reduce crime:

![Have you seen this man?](./images/example-application--have-you-seen-this-man.PNG)

# 5 The Application Layer
This chapter describes the [Application Layer](#application-layer) and how it supports the processes of the Data Reuse scenario.

## 5.1 Qiy Application
A [Qiy Application](#qiy-application) is an [Application Service](#application-service) or software which is authorized for use with Qiy.
* A [Qiy Application](#qiy-application) must comply with the requirements of the [Qiy Scheme](#qiy-scheme).
* A [Qiy User](#qiy-user) can only use Qiy with a [Qiy Application](#qiy-application).
* A [Qiy User](#qiy-user) can use one or more [Qiy Applications](#qiy-application).
* [Qiy Applications](#qiy-application) can use a [Qiy Node](#qiy-node) at the same time.

### 5.1.1 Application Provider
[Qiy Applications](#qiy-application) can be provided by [Application Providers](#application-provider). An [Application Provider](#application-provider) can only do so with a valid [Qiy Licence Agreement Application Provider](#qiy-licence-agreement-application-provider).

### 5.1.2 Qiy Application Protocol
The [Qiy Application Protocol](#qiy-application-protocol) describes the interactions of the [Qiy Applications](#qiy-application) with eachother and the underlying layers.
* The [Qiy Application Protocol](#qiy-application-protocol) is an open standard and is part of the [Qiy Open Standard](#qiy-open-standard).

The [Qiy Application Protocol](#qiy-application-protocol) describes among others how [Qiy Applications](#qiy-application):
* ... create a [Qiy Node](#qiy-node) for a [Qiy User](#qiy-user).
* ... can be linked to a [Qiy Node](#qiy-node) of a [Qiy User](#qiy-user).
* ... create [Connections](#connection).
* ... create a 'backup' of a [Qiy Node](#qiy-node).
* ... exchange [Connection Tokens](#connection-token) out-of-band.
* ... exchange messages.
* ... exchange [Personal Data](#personal-data).

### 5.1.3 Creating Qiy Nodes for Individuals

A [Qiy Application](#qiy-application) can create a [Qiy Node](#qiy-node) for a [Qiy User](#qiy-user), especially when he does not have one yet.
The [Qiy Application](#qiy-application) can do so with the help of an [Access Provider](#access-provider), but first it has to generate the credentials for the [Qiy Node](#qiy-node) ([Qiy Node Credentials](#qiy-node-credential)):
* A key pair, consisting of public key and a private key, 
* A [Node Id](#node-id)

The [Qiy Application](#qiy-application) must persists these in order to be able to keep using the [Qiy Node](#qiy-node).

#### 5.1.3.1 Security consideration
Some security considerations related to the [Qiy Node Credentials](#qiy-node-credential) are:
* The [Node Id](#node-id) must be a [Uuid](#uuid) in order to assure that it is unique.
* The key pair must be unique.
* The private key must be persisted securily in order to guarantee the security of the [Qiy User](#qiy-user). 
* The [Node Id](#node-id) should be persisted securily in order to guarantee the security of the [Qiy User](#qiy-user). 
* The [Qiy Applications](#qiy-application) that can be used on consumer devices such as smart phones must provide a way to backup and recover the [Qiy Node Credentials](#qiy-node-credential) in order to overcome cases of loss of the device.
* A [Qiy User](#qiy-user) must be able to control the devices that can access his [Qiy Node](#qiy-node), for example in order to be able to block access of a (possibly) stolen device.


### 5.1.4 Link with an existing Qiy Node
A [Qiy Application](#qiy-application) can be linked to an existing [Qiy Node](#qiy-node) by providing it with its [Qiy Node Credentials](#qiy-node-credential).

## 5.2 Connect

### 5.2.1 Application Connect Token
[Qiy Applications](#qiy-application) exchange [Application Connect Tokens](#application-connect-token) to create [Connections](#connection). 
In addition to the [Connect Token](#connect-token) that is necessary to create the [Connection](#connection), it contains the name or pseudonym to be displayed in the [Connect Proposal](#connect-proposal). 
For more information, please refer to [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).

### 5.2.2 Proposer: Connect
For a [Qiy Application](#qiy-application) of a [Proposer](#proposer), a Connection is established as follows:
* The [Qiy Application](#qiy-application) generates an [Application Conenct Token](#application-conenct-token), see [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).
* The [Qiy Application](#qiy-application) composes a [Connect Proposal](#connect-proposal) for the [Proposer](#proposer).
* The [Proposer](#proposer) presents it out-of-band to the [Accepter](#accepter).
* When the [Accepter](#accepter) wants to connect, he uses the [Connect Proposal](#connect-proposal) to create a connection with his [Qiy Application](#qiy-application), see [5.2.4 'Accepter: Connect'](#524-accepter-connect).
* The [Proposer](#proposer) detects this by use of polling (using the [Connections Request](#connections-request)) or events (using the [Connection Created Event](#connection-created-event)).
 
![Proposer: Connect](./images/proposer--connect.png)

### 5.2.3 Generate Application Connect Token
The main part of an [Application Connect Token](#application-connect-token) is the [Connect Token](#connect-token). The [Qiy Application](#qiy-application) can create this both online and offline:
* Offline by creating a [Connect Token](#connect-token) and registering it later using a [Connect Token Registration Request](#connect-token-registration-request).
* Online using a [Connect Token Creation Request](#connect-token-creation-request).

![Generate Application Connect Token](./images/generate-application-connect-token.png)

### 5.2.4 Accepter: Connect
At the [Accepter](#accepter)-side, a [Qiy Application](#qiy-application) creates a [Connection](#connection) with a [Connect Proposal](#connect-proposal) or [Connect Token](#connect-token) as follows:
* In case of a [Connect Proposal](#connect-proposal), the [Qiy Application](#qiy-application) extracts the [Connect Token](#connect-token) from the [Connect Proposal](#connect-proposal).
* The [Qiy Application](#qiy-application) uses the [Connect Token](#connect-token) in [Connection Create Request](#connection-create-request) to the [Qiy Node](#qiy-node) of the [Qiy User](#qiy-user).
* The [Qiy Node](#qiy-node) creates the [Connection](#connection) and returns the id of the [Connection](#connection) ([Connection Uri](#connection-uri)).

![Accepter: Connect](./images/accepter--connect.png)

## 5.3 Consent

### 5.3.1 Relying Party: Request consent

A [Qiy Application](#qiy-application) of a [Relying Party](#relying-party) can request an [Individual](#individual) for [Consent](#consent) as follows:
* The [Qiy Application](#qiy-application) sends a [Consent Request Message](#consent-request-message) over the [Connection](#connection) with the [Individual](#individual).
* The [Qiy Application](#qiy-application) receives a message with the outcome, either a [Consent Granted Message](#consent-granted-message) or a [Consent Denied Message](#consent-denied-message).

![Relying Party: Request consent](./images/relying-party--request-consent.png)

### 5.3.2 Individual: Consider consent request
A [Qiy Application](#qiy-application) of an [Individual](#individual) processes a [Consent Request](#consent-request) as follows:
* The [Qiy Application](#qiy-application) detects receiving a [Consent Request Message](#consent-request-message) by polling (using the [Messages Request](#messages-request)) or with events (using the [Message Received Event](#message-received-event)).
* The [Qiy Application](#qiy-application) extracts the [Consent Request](#consent-request) and presents it to the [Individual](#individual).
* Depending on the choice of the [Individual](#individual), the [Qiy Application](#qiy-application) returns a [Consent Granted Message](#consent-granted-message) or a [Consent Denied Message](#consent-denied-message) using the [Connection](#connection) with the [Relying Party](#relying-party).

![Individual--consider-consent-request](./images/individual--consider-consent-request.png)

## 5.4 Service Discovery
A [Qiy Application](#qiy-application) can present an [Individual](#individual) a list of suitable [Data Providers](#data-provider) (or in general [Providers](#provider)) that can produce some requested data (or services) as follows:
* The [Qiy Application](#qiy-application) asks the [Qiy Node](#qiy-node) of the [Individual](#individual) for a list of suitable [Data Providers](#data-provider) with a [Source Candidates Request](#source-candidates-request).
* The [Qiy Node](#qiy-node) consults the [Service Library](#service-library) and returns the outcome to the [Qiy Application](#qiy-application).
* The [Qiy Application](#qiy-application) presents the result to the [Individual](#individual).
* The [Qiy Application](#qiy-application) registers the selected sources with a [Source Registration Request](#source-registration-request).

## 5.5 Data by Reference
[Qiy Applications](#qiy-application) exchange [data by reference](#data-by-reference) rather then by value.
This goes as follows:
* A [Qiy Application](#qiy-application) requests a reference for the data ([Data Reference](#data-reference)).
* The [Qiy Application](#qiy-application) receives a [Data Reference](#data-reference).
* The [Qiy Application](#qiy-application) uses the [Data Reference](#data-reference) to acquire the data.

### 5.5.1 Service by Reference
In Qiy providing data is viewed as a service and requesting data as an operation of this service, so the 'data by reference'-pattern is implemented as using a [Service by Reference](#service-by-reference)-pattern:
* A [Qiy Application](#qiy-application) requests an [Operation Reference](#operation-reference) ([Operation Reference Request](#operation-reference-request)).
* A [Operation Reference](#operation-reference) is created by registrating the specification of the operation [Operation Specification](#operation-specification) and returned ([Operation Registration](#operation-registration)).
* The [Qiy Application](#qiy-application) uses the [Data Reference](#data-reference) to acquire the data ([Operation Execution](#operation-execution)).

### 5.5.2 Request data reference
The [Qiy Application](#qiy-application) of a [Relying Party](#relying-party) can request an [Individual](#individual) for a data reference as follows:
* The [Qiy Application](#qiy-application) sends a [Operation Reference Request Message](#operation-reference-request-message) using the [Connection](#connection) of the [Individual](#individual).
* The [Qiy Application](#qiy-application) receives the [Operation Reference](#operation-reference) in an [Operation Reference Message](#operation-reference-message).

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.3 Create reference
A [Qiy Application](#qiy-application) can create an [Operation Reference](#operation-reference) using a specification of the operation ([Operation Specification](#operation-specification)).
This goes as follows:
* The [Qiy Application](#qiy-application) uses the [Operation Specification](#operation-specification) in an [Operation Registration Request](#operation-registration-request) to the [Qiy Node](#qiy-node) it is linked with.
* The [Qiy Node](#qiy-node) creates the [Operation Reference](#operation-reference) and returns it.

### 5.5.4 Request data
The [Qiy Application](#qiy-application) of a [Relying Party](#relying-party) can obtain data using a [Data Reference](#data-reference) / [Operation Reference](#operation-reference). 
This goes as follows:
* The [Qiy Application](#qiy-application) uses the [Operation Reference](#operation-reference) in a [Operation Execution Request](#operation-execution-request) to its [Qiy Node](#qiy-node).
* The [Qiy Node](#qiy-node) returns the requested data.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.5 Provide data
The [Data Provider](#data-provider) produces the data using his [Service Endpoint](#service-endpoint).
This does not involve any of the [Qiy Applications](#qiy-application) of the [Data Provider](#data-provider) nor his [Qiy Node](#qiy-node).

![Data Provider: Provide data](./images/data-provider--provide-data.png)

# 6 The Qiy Node Layer
This chapter describes the [Qiy Node Layer](#qiy-node-layer) and how it supports the upper layers.

## 6.1 Access Provider
The services of this layer can be provided by an [Access Provider](#access-provider):
* An [Access Provider](#access-provider) can provide [Qiy Nodes](#qiy-node).
* An [Access Provider](#access-provider) can host [Qiy Nodes](#qiy-node).

### 6.1.1 Portability
An [Access Provider](#access-provider) can offer [Qiy Node](#qiy-node)-services to [Qiy Users](#qiy-user), but must enable [Qiy Users](#qiy-user) to easily transfer the services to a different [Access Provider](#access-provider).

## 6.2 Qiy Node
A [Qiy Node](#qiy-node) is a [Technology Service](#technology-service) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).
A [Qiy Node](#qiy-node):
* ... must comply with the rules of the [Qiy Scheme](#qiy-scheme).
* ... can be hosted on any host ([Node](#node)).
* ... has its own [Transporter](#transporter) which ensures secure transport of messages and/or data via Qiy.

### 6.2.1 Qiy Node Protocol
The [Qiy Node Protocol](#qiy-node-protocol) describes the interaction between the [Qiy Nodes](#qiy-node) and the underlying layers.
* The [Qiy Node Protocol](#qiy-node-protocol) is one of the protocols in the [Qiy Open Standard](#qiy-open-standard).
The [Qiy Node Protocol](#qiy-node-protocol) describes for example:
* How a [Qiy Node](#qiy-node) is instantiated.
* How [Qiy Nodes](#qiy-node) create [Connections](#connection) and use them to exchange data, messages or to provide/consume services.

### 6.2.2 Qiy Node API
The [Qiy Node API](#qiy-node-api) is the [Technology Interface](#technology-interface) of the [Qiy Node](#qiy-node), one of the APIs of the [Qiy Open Standard](#qiy-open-standard).
* The [Qiy Node API](#qiy-node-api) is intended for use by [Qiy Applications](#qiy-application).

### 6.2.3 Qiy Node Implementation
A [Qiy Node Implementation](#qiy-node-implementation) is a software package which can be used to realize a [Qiy Node](#qiy-node).
The [Qiy Scheme](#qiy-scheme) puts no limit on the number of [Qiy Node Implementations](#qiy-node-implementation), as long as the implementation complies with the [Qiy Open Standard](#qiy-open-standard) and the rules of the [Qiy Scheme](#qiy-scheme). 

### 6.2.4 Qiy Node Instantiation
A [Qiy Node](#qiy-node) can be created in two ways:
* It can be instantiated by an [Access Provider](#access-provider). The [Access Provider](#access-provider) will instantiate it with its own [Transporter](#transporter). 
* It can be instantiated by a [Qiy User](#qiy-user) on a [Node](#node) of his own using a [Qiy Node Implementation](#qiy-node-implementation). 
When the second option is chosen, the [Qiy User](#qiy-user) is responsible for obtaining a [Transporter](#transporter) and linking it to the [Qiy Node](#qiy-node).

### 6.2.5 Deleting a Qiy Node
In principle, a [Qiy Node](#qiy-node) can be deleted by its owner whenever he wants to do so.
In this case, the [Qiy Node](#qiy-node) will be deleted including persisted data, [Connections](#connection) and the linked [Transporter](#transporter).
Related [Consents](#consent) will be withdrawn.

## 6.3 Connect
Two [Qiy Nodes](#qiy-node) can connect by creating a [Path](#path) between themselves.
* A [Qiy Node](#qiy-node) can connect with zero or more other [Qiy Nodes](#qiy-node).
* A [Qiy Node](#qiy-node) can have zero or more [Paths](#path) with any other [Qiy Node](#qiy-node).
* A priori, a [Qiy Node](#qiy-node) does not know the identity of the [Qiy Node](#qiy-node) at the other side of a [Path](#path).

### 6.3.1 Connection Uri
The [Connection Uri](#connection-uri) is the [Uri](#uri) which identifies a [Connection](#connection) for one of the [Qiy Node](#qiy-node) it connects.
* A [Connection](#connection) has two [Connection Uris](#connection-uri); one for each of the two [Qiy Nodes](#qiy-node) it connects.
* The two [Connection Uris](#connection-uri) of one [Connection](#connection) are not related to one another.
* A priori, a [Qiy Node](#qiy-node) does not know the other [Connection Uri](#connection-uri) of a [Connection](#connection).

EXAMPLE: [Connection Uris](#connection-uri) of a [Connection](#connection) between [Qiy Node](#qiy-node) 1 and [Qiy Node](#qiy-node) 2:

[Qiy Node](#qiy-node) | [Connection Uri](#connection-uri)
Qiy Node 1	| http://127.0.0.1:8087/user/connections/user/usernodeB/93590b55-9194-4cf4-944f-2cbceab7dbcd
Qiy Node 2	| http://127.0.0.1:8087/user/connections/user/usernodeA/f96bc541-e98b-449e-bfc5-48ec928e0dc9

#### 6.3.1.1 Security concern
The [Connection Uri](#connection-uri) has only meaning in the context of the [Qiy Node](#qiy-node) that knows it and is useless outside this scope.
For example, the [Uri](#uri) by itself can not be used to exchange a message with the [Qiy Node](#qiy-node) nor any other existing [Qiy Node](#qiy-node).

### 6.3.2 Connect Token
A [Connect Token](#connect-token) is a token which can be used by a [Qiy Application](#qiy-application) to create a [Connection](#connection).
It consists of:
* a temporary secret
* a [Transport Connect Token](#transport-connect-token).

A [Connect Token](#connect-token) has the following properties:
* An expiration setting: Whether the token expires and if so, on what date and time
* A budget: The number of times that the token can be used to create a Connection. 

The properties can not only be set when the token is registered or requested, but also later.
For example, it is possible to reactivate a [Connect Token](#connect-token) by increasing the budget or inactivate one by changing the expiration.

#### 6.3.2.1 Security concern
The [Connect Token](#connect-token) can only be used to create a [Connection](#connection) and only so via Qiy, with the help of a [Qiy Application](#qiy-application) and a linked [Qiy Node](#qiy-node).
By itself, it cannot be used for any other purpose, for example gain access to a [Qiy Node](#qiy-node) nor any other parts of the Qiy infrastructuur.

#### 6.3.2.2 Creating a Connect Token
A [Connect Token](#connect-token) can be created both offline and online:
* A [Connect Token](#connect-token) can be obtained from the [Qiy Node](#qiy-node) using a [Connect Token Creation Request](#connect-token-creation-request) ([Online Connect Token](#online-connect-token)).
* A [Connect Token](#connect-token) can be created by a [Qiy Application](#qiy-application) and registered later using a [Connect Token Registration Request](#connect-token-registration-request) ([Offline Connect Token](#offline-connect-token)).

The [Offline Connect Token](#offline-connect-token) allows initiating a [Connection](#connection) (creating a [Connect Token](#connect-token)) even when Qiy is temporarily not available.
However, care must be taken that the created token is unique, especially so for the created [Transport Connect Token](#transport-connect-token).

#### 6.3.2.3 Creating a Transport Connect Token
A [Qiy Node](#qiy-node) will never create a [Transport Connect Token](#transport-connect-token):
* In case of an [Online Connect Token](#online-connect-token): The [Qiy Node](#qiy-node) will obtain a [Transport Connect Token](#transport-connect-token) from its [Transporter](#transporter).
* In case of an [Offline Connect Token](#offline-connect-token): The [Qiy Node](#qiy-node) will compose a [Transport Connect Token](#transport-connect-token) using the [Connect Token](#connect-token) provided by the [Qiy Application](#qiy-application) and register it at its [Transporter](#transporter).

### 6.3.3 Connecting
Two [Qiy Nodes](#qiy-node) connect as follows:
* The [Qiy Node](#qiy-node) of the [Proposer](#proposer) either 1) obtains a [Transport Connect Token](#transport-connect-token) from the [Transporter](#transporter) or 2) from a linked [Qiy Application](#qiy-application) in a [Connection Create Request](#connection-create-request).
* The [Qiy Node](#qiy-node) either 1) provides the [Transport Connect Token](#transport-connect-token) to the [Qiy Application](#qiy-application) or 2) registers the [Transport Connect Token](#transport-connect-token) at its [Transporter](#transporter).
* The [Transport Connect Token](#transport-connect-token) is made available (partly out-of-bands, for example in a [Connect Proposal](#connect-proposal)) to the [Qiy Node](#qiy-node) of the [Accepter](#accepter).
* The [Qiy Node](#qiy-node) of the [Accepter](#accepter) uses its [Transporter](#transporter) to create a [Path](#path) using the [Transport Connect Token](#transport-connect-token).
Each accepted [Path Creation Request](#path-creation-request) leads to a new [Path](#path), irrespective of the number of existing [Paths](#path) between the two [Qiy Nodes](#qiy-node).

### 6.3.4 Deleting a Connection
A [Connection](#connection) can be deleted with a [Connection Delete Request](#connection-delete-request).
The [Connection](#connection) will be deleted completely, including any persisted data and/or messages and underlying [Paths](#path).
Any related [Consents](#consent) will be withdrawn.

## 6.4 Consent
A [Consent](#consent) is a permission given by an [Individual](#individual) to a [Relying Party](#relying-party) defining what [Personal Data](#personal-data) a [Relying Party](#relying-party) is allowed to use for a provided [Service](#service) and under what the terms.
A [Consent](#consent) has the following properties:
* a [Consent Uri](#consent-uri)
* a [Consent Service Descriptor](#consent-service-descriptor)
* a [Consent Data Descriptor](#consent-data-descriptor)

### 6.4.1 Consent Uri
The [Consent Uri](#consent-uri) is an [Uri](#uri) used to identify a [Consent](#consent).

### 6.4.2 Consent Service Descriptor
The [Consent Service Descriptor](#consent-service-descriptor) is a [Service Descriptor](#service-descriptor) which indicates the [Service](#service) that the [Consent](#consent) applies to.
A [Service Descriptor](#service-descriptor) can be used to obtain a description of a [Service](#service) ([Service Description](#service-description)) with the help of the [Service Library](#service-library).

### 6.4.3 Consent Data Descriptor
The [Consent Data Descriptor](#consent-data-descriptor) is a [Data Descriptor](#data-descriptor) which indicates the [Personal Data](#personal-data) that the [Consent](#consent) applies to.
A [Data Descriptor](#data-descriptor) can be used to obtain a description of [Data](#data) ([Data Description](#data-description)) with the help of the [Service Library](#service-library).

#### 6.4.3.1 Privacy concern
A [Relying Party](#relying-party) can only ask [Consent](#consent) for [Personal Data](#personal-data) that can be provided by one of the available [Data Providers](#data-provider), eg for which a [Data Descriptor](#data-descriptor) exists in the [Service Library](#service-library).
  
## 6.5 Qiy Node Request
A [Qiy Node Request](#qiy-node-request) is a [Http Request](#http-request) for a [Qiy Node](#qiy-node). 
[Qiy Node Requests](#qiy-node-request) are only accepted when they are correctly authenticated with:
* the [Node Id](#node-id).
* an actual timestamp
* a digital signature over the [Node Id](#node-id), the timestamp and the contents of the body of the request made with the private key

## 6.6 Qiy Node Requests
This section gives an overview of the [Qiy Node Requests](#qiy-node-request).
Details of [Qiy Node Requests](#qiy-node-request) can be found in the [Qiy Node API](#qiy-node-api).

### 6.6.1 Connect Token Creation Request
The [Connect Token Creation Request](#connect-token-creation-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](#connect-token) from the [Qiy Node](#qiy-node).

### 6.6.2 Connect Token Registration Request
The [Connect Token Registration Request](#connect-token-registration-request) is a [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](#connect-token).

### 6.6.3 Connect Token Update Request
The [Connect Token Update Request](#connect-token-update-request) is a [Qiy Node Request](#qiy-node-request) that can be used to update a [Connect Token](#connect-token).

### 6.6.4 Connection Create Request
The [Connection Create Request](#connection-create-request) is a [Qiy Node Request](#qiy-node-request) that can be used to create a [Connection](#connection) with a [Connect Token](#connect-token).

### 6.6.5 Connection Delete Request
The [Connection Delete Request](#connection-delete-request) is a [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connection](#connection).

### 6.6.6 Connections Request
The [Connections Request](#connections-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Connections](#connection) of a [Qiy Node](#qiy-node).

### 6.6.7 Consent Denied Request
The [Consent Denied Request](#consent-denied-request) is a [Qiy Node Request](#qiy-node-request) that can be used to record the denial of a [Consent](#consent).

### 6.6.8 Consent Granted Request
The [Consent Granted Request](#consent-granted-request) is a [Qiy Node Request](#qiy-node-request) that can be used to record the granting of a [Consent](#consent).

### 6.6.9 Consent Request
The [Consent Request](#consent-request) is a [Qiy Node Request](#qiy-node-request) which can be used to request for a [Consent](#consent).

### 6.6.10 Consent Withdrawn Request
The [Consent Withdrawn Request](#consent-withdrawn-request) is a [Qiy Node Request](#qiy-node-request) that can be used to record the withdrawal of a [Consent](#consent).

### 6.6.11 Consents Request
The [Consents Request](#consents-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Consents](#consent) of a [Qiy Node](#qiy-node).

### 6.6.12 Message Post Request
The [Message Post Request](#message-post-request) is a [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### 6.6.13 Messages Request
The [Messages Request](#messages-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Messages](#message) of a [Qiy Node](#qiy-node).

### 6.6.14 Operation Execution Request
The [Operation Execution Request](#operation-execution-request) is a [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by reference using an [Operation Reference](#operation-reference).

### 6.6.15 Operation Registration Request
The [Operation Registration Request](#operation-registration-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) by registrating an [Operation Specification](#operation-specification).

### 6.6.16 Operation References Request
The [Operation References Request](#operation-references-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Operation References](#operation-reference) of a [Qiy Node](#qiy-node).

### 6.6.17 Source Candidates Request
The [Source Candidates Request](#source-candidates-request) is a [Qiy Node Request](#qiy-node-request) to obtain candidate [Providers](#provider) for a [Service](#service).

### 6.6.18 Source Registration Request
The [Source Registration Request](#source-registration-request) is a [Qiy Node Request](#qiy-node-request) to register a [Provider](#provider) as source for a [Service](#service).
 
## 6.7 Qiy Node Message
A [Qiy Node Message](#qiy-node-message) is a [Message](#message) that is exchanged using a [Connection](#connection).
[Qiy Node Messages](#qiy-node-message) can be sent with the [Message Post Request](#message-post-request), obtained using a [Messages Request](#messages-request) and monitored with [Qiy Node Events](#qiy-node-event) like [Message Received Event](#message-received-event).

## 6.8 Qiy Node Messages
This section gives an overview of the [Qiy Node Messages](#qiy-node-message).
Details of [Qiy Node Messages](#qiy-node-message) can be found in the [Qiy Node Protocol](#qiy-node-protocol).

### 6.8.1 Consent Denied Message
The [Consent Denied Message](#consent-denied-message) is a [Qiy Node Message](#qiy-node-message) which can be used to communicate the denial of a [Consent](#consent).

### 6.8.2 Consent Granted Message
The [Consent Granted Message](#consent-granted-message) is a [Qiy Node Message](#qiy-node-message) which can be used to communicate the granting of a [Consent](#consent).

### 6.8.3 Consent Request Message
The [Consent Request Message](#consent-request-message) is a [Qiy Node Message](#qiy-node-message) which can be used to request for a [Consent](#consent).

### 6.8.4 Operation Reference Message
The [Operation Reference Message](#operation-reference-message) is a [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference) over a [Connection](#connection).
 
### 6.8.5 Operation Reference Request Message
The [Operation Reference Request Message](#operation-reference-request-message) is a [Qiy Node Message](#qiy-node-message) that can be used to request for [Operation References](#operation-reference).
 
## 6.9 Qiy Node Event
A [Qiy Node Event](#qiy-node-event) is a [Technology Event](#technology-event) of a [Qiy Node](#qiy-node).

## 6.10 Qiy Node Events
This section gives an overview of the [Qiy Node Events](#qiy-node-event).
Details of [Qiy Node Events](#qiy-node-event) can be found in the [Qiy Node Protocol](#qiy-node-protocol).

### 6.10.1 Connection Created Event
The [Connection Created Event](#connection-created-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Connection](#connection) has been created.

### 6.10.2 Consent Withdrawn Event
The [Consent Withdrawn Event](#consent-withdrawn-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Consent](#consent) has been withdrawn.

### 6.10.3 Message Received Event
The [Message Received Event](#message-received-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node Message](#qiy-node-message) has been received.

### 6.10.4 Operation Reference Received Event
The [Operation Reference Received Event](#operation-reference-received-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node](#qiy-node) has received a new [Operation Reference](#operation-reference).

### 6.10.5 Source Candidate Event
The [Source Candidate Event](#source-candidate-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node](#qiy-node) has received a new [Source Candidate](#source-candidate) for a [Consent](#consent).

# 7 The Service Layer
The [Service Layer](#service-layer) provides the following [Technology Services](#technology-service) to support the provisioning and consumption of [Services](#service) via Qiy:
* [Service Endpoints](#service-endpoint)
* [Service Library](#service-library)
* [Consent Service](#consent-service)

## 7.1 Access Provider
The [Service Library](#service-library) and [Consent Service](#consent-service) are both provided by an [Access Provider](#access-provider).

### 7.1.1 Portability
The [Qiy Scheme](#qiy-scheme) prescribes that one can easily change to a different [Access Provider](#access-provider) for these services.

## 7.2 Service
In general, a [Service](#service) is an 'information society service' as defined in the [GDPR](#gdpr), with the following enhancements:
* A [Service](#service) can be consumed with the use of one or more [Operations](#operation).
* A [Service](#service) is provided by a [Provider](#provider).
* A [Provider](#provider) can offer one or more [Services](#service).
* One [Service](#service) can be offered by one or more [Providers](#provider).
* The [Services](#service) that a [Provider](#provider) offers are described in a [Service Catalogue](#service-catalogue).
* The [Services](#service) that an [Individual](#individual) consumes are described in his [Service Portfolio](#service-portfolio).

As for Qiy, the following definitions apply:
* Both [Relying Parties](#relying-partie) and [Data Providers](#data-provider) are [Providers](#provider).

## 7.3 Service Endpoints
A [Service Endpoint](#service-endpoint) is a [Technology Service](#technology-service) provided by a [Provider](#provider) to allow the consumption of his [Services](#service):
* A [Provider](#provider) can employ one or more [Service Endpoints](#service-endpoint).
* A [Service Endpoint](#service-endpoint) can be used for one or more [Services](#service).
* A [Service](#service) can be consumed with the use of one or more [Service Endpoints](#service-endpoint).

For example, a [Service Endpoint](#service-endpoint) may be used by a [Data Provider](#data-provider) to disclose the [Personal Data](#personal-data) from one of his databases.

## 7.4 Service Library
The [Service Library](#service-library) is used for:
* [Data Descriptions](#data-description)
* [Providers](#provider)
* [Service Catalogues](#service-catalogue)
* [Service Descriptions](#service-description)

## 7.5 Consent Service
A [Consent Service](#consent-service) is used for maintaining [Consents](#consent) and their status.
A [Consent](#consent) can be accessed by both of the involved [Qiy Users](#qiy-user): the [Individual](#individual) and the [Provider](#provider).

* In principle, only an [Individual](#individual) can withdraw a [Consent](#consent) he has granted before.
* A [Provider](#provider) can only obtain [Personal Data](#personal-data) under a [Consent](#consent) which has not been withdrawn.

# 8 The Transport Layer
The [Transport Layer](#transport-layer) supports the secure transmission of messages ([Transport Messages](#transport-message)) over [Paths](#path) between [Transporters](#transporter).

## 8.1 Access Provider
The services of this layer are only provided by an [Access Provider](#access-provider).

### 8.1.1 Portability
The [Qiy Scheme](#qiy-scheme) prescribes that one can easily switch [Access Provider](#access-provider) for these services.

## 8.2 Transporter
A [Transporter](#transporter) is a [Technology Service](#technology-service) which allows the secure transmission of messages and/or data.
* A [Transporter](#transporter) must comply with the rules of the [Qiy Scheme](#qiy-scheme).
* A [Transporter](#transporter) is hosted on a [Carrier Node](#carrier-node).
* Each [Qiy Node](#qiy-node) has its own [Transporter](#transporter).

A [Transporter](#transporter) can be used for:
* Creating [Paths](#path) with other [Transporters](#transporter).
* Securely transmitting [Transport Messages](#transport-message) over these [Paths](#path).

## 8.3 Transport Protocol
The [Transport Protocol](#transport-protocol) describes the interaction between [Transporters](#transporter) and the underlying layer.
The protocol is one of the protocols of the [Qiy Open Standard](#qiy-open-standard).

## 8.4 Transporter API
The [Transporter API](#transporter-api) is the [Technology Interface](#technology-interface) of the [Transporter](#transporter), one of the APIs of the [Qiy Open Standard](#qiy-open-standard).
* The [Transporter API](#transporter-api) is intended for use by [Qiy Nodes](#qiy-node).

## 8.5 Transporter Implementation
A [Transporter Implementation](#transporter-implementation) is a software package which can be used to realize a [Transporter](#transporter).
The [Qiy Scheme](#qiy-scheme) puts no limit on the number of [Transporter Implementations](#transporter-implementation), as long as the implementation complies with the [Qiy Open Standard](#qiy-open-standard) and the rules of the [Qiy Scheme](#qiy-scheme). 

## 8.6 Transporter Instantiation
A [Transporter](#transporter) can only be instantiated by an [Access Provider](#access-provider).

## 8.7 Deleting a Transporter
A [Transporter](#transporter) can be deleted by its [Qiy Node](#qiy-node).
In this case, the [Transporter](#transporter) will be deleted including any persisted data and [Routes](#route).

## 8.8 Path
A [Path](#path) is a logical connection between two [Transporters](#transporter) that can be used to exchange [Transport Messages](#transport-message).
Physically seen, the [Path](#path) may be dynamic and stretch over several [Carriers](#carrier).

### 8.8.1 Path Creation
A [Path](#path) can be created by a [Transporter](#transporter) with a [Transport Connect Token](#transport-connect-token).

### 8.8.2 Deleting a Path
A [Path](#path) can be deleted by either of the ending [Transporters](#transporter). 
The [Path](#path) will be deleted including any persisted data and/or messages.

# 9 The Carrier Layer
The [Carrier Layer](#carrier-layer) supports the creation of [Paths](#path) and the secure transport of messages over them.

## 9.1 Access Provider
The services of this layer are only provided by an [Access Provider](#access-provider).

### 9.1.1 Portability
The [Qiy Scheme](#qiy-scheme) prescribes that one can easily switch [Access Provider](#access-provider) for these services.

## 9.2 Carrier
The [Carrier](#carrier) is [Technology Service](#technology-service) which can be used for:
* To obtain a [Transporter](#transporter).
* To create [Paths](#path).
* To safely transport messages between [Carriers](#carrier).
* To obtain a [Qiy Node](#qiy-node).

The [Carrier](#carrier) comes with the following rules:
* A [Carrier](#carrier) must comply with the rules of the [Qiy Scheme](#qiy-scheme).
* A [Carrier](#carrier) must support the [Carrier API](#carrier-api).

## 9.3 Carrier Protocol
The [Carrier Protocol](#carrier-protocol) describes the interaction between [Carriers](#carrier).
The protocol is part of the [Qiy Open Standard](#qiy-open-standard).

## 9.4 Carrier API
The [Carrier API](#carrier-api) is the [Technology Interface](#technology-interface) of the [Carrier](#carrier) and is part of the [Qiy Open Standard](#qiy-open-standard).

## 9.5 Carrier Implementation
A [Carrier Implementation](#carrier-implementation) is a software package which can be used to realize a [Carrier](#carrier)
The [Qiy Scheme](#qiy-scheme) puts no limit on the number of [Carrier Implementations](#carrier-implementation), as long as the implementation complies with the [Qiy Open Standard](#qiy-open-standard) and the rules of the [Qiy Scheme](#qiy-scheme). 

## 9.6 Carrier Node
A [Carrier Node](#carrier-node) is a [Node](#node) which hosts one or more [Carriers](#carrier).
* The [Carrier Node](#carrier-node) is provided by an [Access Provider](#access-provider).
* The [Access Provider](#access-provider) can provide one or more [Carrier Nodes](#carrier-node).

# 10 Definitions
This document uses the following definitions:

### Accepter
A [Business Role](#business-role) for a [Qiy User](#qiy-user) who is creating a [Connection](#connection) using a [Connect Token](#connect-token) that is provided by a [Proposer](#proposer).

### Access Principle
The principle which authorizes the access of an [Individual](#individual) to his [Personal Data](#personal-data), one of the [Qiy Trust Principles](#qiy-trust-principles).

### Access Provider
An organization which provides [Qiy Users](#qiy-user) access to the [Qiy Trust Framework](#qiy-trust-framework), either an [Issuer](#issuer) or a [Service Provider](#service-provider).

### Application Connect Token
A [Token](#token) that is used by [Qiy Applications](#qiy-application) to create [Connections](#connection).

### Application Interface
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Application Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Application Provider
A [Bussiness Role](#bussiness-role) for suppliers of [Qiy Applications](#qiy-application).

### Application Service
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Architectural Layers
The architectural layers of the [Qiy Scheme](#qiy-scheme): the [User Layer](#user-layer), the [Application Layer](#application-layer), the [Qiy Node Layer](#qiy-node-layer), the [Service Layer](#service-layer), the [Transport Layer](#transport-layer) and the [Carrier Layer](#carrier-layer).

### Binding Individual Rights
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Binding Principles for Relying Parties and Data Providers
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Business Actor
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Business Object
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Business Process
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Business Role
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Carrier
A [Technology Service](#technology-service) that provides the services of the [Carrier Layer](#carrier-layer). 

### Carrier API
[Technology Interface](#technology-interface) of the [Carrier](#carrier).

### Carrier Implementation
A software package which can be used to realize a [Carrier](#carrier).

### Carrier Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Carrier Node
A [Node](#node) which hosts one or more [Carriers](#carrier).

### Connect Proposal
A [Business Object](#business-object) for a proposal to connect via Qiy.

### Connect Token
A [Literal](#literal) used to create a [Connection](#connection).

### Connect Token Creation Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](#connect-token) from the [Qiy Node](#qiy-node).

### Connect Token Registration Request
A [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](#connect-token).

### Connect Token Update Request
A [Qiy Node Request](#qiy-node-request) that can be used to update a [Connect Token](#connect-token).

### Connection
A connection between two [Qiy Nodes](#qiy-node).

### Connection Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to create a [Connection](#connection) with a [Connect Token](#connect-token).

### Connection Created Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Connection](#connection) has been created.

### Connection Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connection](#connection).

### Connection Uri
[Uri](#uri) voor the id van een [Connection](#connection).

### Connections Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Connections](#connection) of a [Qiy Node](#qiy-node).

### Consent
As defined in the [GDPR](#gdpr).

### Consent Data Descriptor
[Data Descriptor](#data-descriptor) in a [Service Description](#service-description) referring to the [Data Description](#data-description) describing the [Personal Data](#personal-data) that is used to provide the [Service](#service).

### Consent Denied Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the denial of a [Consent](#consent).

### Consent Denied Request
A [Qiy Node Request](#qiy-node-request) that can be used to record the denial of a [Consent](#consent).

### Consent Granted Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the granting of a [Consent](#consent).

### Consent Granted Request
A [Qiy Node Request](#qiy-node-request) that can be used to record the granting of a [Consent](#consent).

### Consent Request
A [Qiy Node Request](#qiy-node-request) which can be used to request for a [Consent](#consent).

### Consent Request Message
A [Qiy Node Message](#qiy-node-message) which can be used to request for a [Consent](#consent).

### Consent Service
A [Technology Service](#technology-service) used to maintain [Consents](#consent) and their status.

### Consent Service Description
A [Service Description](#service-description) of the [Service](#service) for which a [Consent](#consent) applies.

### Consent Service Descriptor
A [Service Descriptor](#service-descriptor) of a [Consent Service Description](#consent-service-description).

### Consent Uri
A [Uri](#uri) which is used to identify a [Consent](#consent).

### Consent Withdrawn Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Consent](#consent) has been withdrawn.

### Consent Withdrawn Request
A [Qiy Node Request](#qiy-node-request) that can be used to record the withdrawal of a [Consent](#consent).

### Consents Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Consents](#consent) of a [Qiy Node](#qiy-node).

### Data Description
A description of data that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Data Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Provider
A [Business Role](#business-role) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Data Provider Agreement
An agreement required for [Data Providers](#data-provider).

### Data Reference
An [Operation Reference](#operation-reference) which can be used to obtain [Personal Data](#personal-data) of an [Individual](#individual).

### Data Subject
As defined in the [GDPR](#gdpr).

### Data by Reference
A pattern for exchanging data indirectly using a [Data Reference](#data-reference), see also [Service by Reference](#service-by-reference).

### Definitions of the Qiy Scheme
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### GDPR
General Data Protection Regulation, see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 

### Governance Model for the Qiy Scheme
Governance Model for the [Qiy Scheme](#qiy-scheme), see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/.

### HTTP Request
As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html

### Individual
A [Business Role](#business-role) of a [Qiy User](#qiy-user) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Issuer
A [Business Role](#business-role) for an [Access Provider](#access-provider) that provides services to natural persons, see [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Licence Agreement Application Provider
A licence agreement for [Application Providers](#application-provider).

### Licence Agreement Issuer
A licence agreement for [Issuers](#issuer), the template of which is part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Licence Agreement Service Provider
A licence agreement for [Service Providers](#service-provider), the template of which is part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Literal
A fixex value, see https://en.wikipedia.org/wiki/Literal_(computer_programming).

### Message Post Request
A [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### Message Received Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node Message](#qiy-node-message) has been received.

### Messages Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Messages](#message) of a [Qiy Node](#qiy-node).

### Node
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Node Id
A [Qiy Node](#qiy-node) id.

### Operation
A 'sub-service' which can be used to consume a [Service](#service).

### Operation Execution Request
A [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by reference using an [Operation Reference](#operation-reference).

### Operation Reference
A [Business Object](#business-object) used by the [Service by Reference](#service-by-reference)-pattern.

### Operation Reference Message
A [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference) over a [Connection](#connection).

### Operation Reference Received Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node](#qiy-node) has received a new [Operation Reference](#operation-reference).

### Operation Reference Request Message
A [Qiy Node Message](#qiy-node-message) that can be used to request for [Operation References](#operation-reference).

### Operation References Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Operation References](#operation-reference) of a [Qiy Node](#qiy-node).

### Operation Registration Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) by registrating an [Operation Specification](#operation-specification).

### Operation Specification
A specification of a [Http Request](#http-request) for the execution of an [Operation](#operation).

### Path
A connection between two [Transporters](#transporter) which is used to exchange [Transport Messages](#transport-message).

### Personal Data
As defined in the [GDPR](#gdpr).

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Provider
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that is providing one or more [Services](#service) using Qiy, that is a [Data Provider](#data-provider) or a [Relying Party](#relying-party).

### Qiy Application
An [Application Service](#application-service) or software that is authorized for use with Qiy.

### Qiy Application Protocol
A protocol for the interactions between [Qiy Applications](#qiy-application) and the underlying layers.

### Qiy Foundation
A foundation dedicated to putting people back in control of their personal data while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
A member of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A [Technology Service](#technology-service) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Qiy Node API
A [Technology Interface](#technology-interface) of the [Qiy Node](#qiy-node) that is part of the [Qiy Open Standard](#qiy-open-standard).

### Qiy Node Event
A [[Technology Event](#technology-event)] of a [Qiy Node](#qiy-node).

### Qiy Node Implementation
A software package which can be used to realize a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Qiy Node Message
A [Message](#message) that is exchanged using a [Connection](#connection).

### Qiy Node Protocol
A protocol describing the interaction between [Qiy Nodes](#qiy-node) and the underlying layers.

### Qiy Node Request
A [Http Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Open Standard
A set of open standards for Qiy, maintained by the [Work Stream Functionality & Technology](#work-stream-functionality-&-technology), see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

### Qiy Scheme
See https://www.qiyfoundation.org/qiy-scheme/.

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme), see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/

### Qiy Trust Framework
As defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Qiy Trust Principles
As defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme), see https://www.qiyfoundation.org/qiy-trust-principles/.

### Qiy User
A [Business Actor](#business-actor); defined as 'User' in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Reference
A [Literal](#literal).

### Relying Party
A [Business Role](#business-role) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Relying Party Agreement
An agreement that is required for [Relying Parties](#relying-partie).

### Request
A [Business Object](#business-object): a message requesting something.

### Service
An 'information society service' as defined in the [GDPR](#gdpr).

### Service Description
A description of a [Service](#service) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Service Discovery
A [Business Process](#business-proces) to find [Providers](#provider) for a given [Service](#service).

### Service Endpoint
A [Technology Service](#technology-service) provided by a [Provider](#provider) to allow the consumption of his [Services](#service).

### Service Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Service Library
A [Technology Service](#technology-service) that supports the [Service](#service) processes of the [Individuals](#individual) and the [Providers](#provider).

### Service Provider
A [Business Role](#business-role): an [Access Provider](#access-provider) which provides business-to-business services as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Service Source
A [Provider](#provider) that can or is providing a specific [Service](#service).

### Service by Reference
A pattern for consuming [Services](#service) indirectly using references ([Operation Reference](#operation-reference)).

### Source Candidate Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node](#qiy-node) has received a new [Source Candidate](#source-candidate) for a [Consent](#consent).

### Source Candidates Request
A [Qiy Node Request](#qiy-node-request) to obtain candidate [Providers](#provider) for a [Service](#service).

### Source Registration Request
A [Qiy Node Request](#qiy-node-request) to register a [Provider](#provider) as source for a [Service](#service).

### Technology Event
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Technology Interface
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Technology Service
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 

### Transport Connect Token
A [Literal](#literal) used to create [Paths](#path).

### Transport Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Transport Message
A message that is exchanged over a [Path](#path) between two [Transporters](#transporter).

### Transport Message Description
A [Data Description](#data-description) that describes the contents, format and encryption (if any) of a [Transport Message](#transport-message).

### Transport Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interaction between [Transporters](#transporter) and the lower layers.

### Transporter
A [Technology Service](#technology-service) that provides transport services.

### Transporter API
[Technology Interface](#technology-interface) of a [Transporter](#transporter).

### Transporter Implementation
A software package which can be used to realize a [Transporter](#transporter).

### Uri
See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

### Url
See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

### User Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Work Stream Functionality & Technology
One of the work streams of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/qiy-scheme/workstreams/


