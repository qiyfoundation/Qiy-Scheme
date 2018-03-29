# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From [Qiy Nodes] to [Data] exchange


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
		1. ['Help, I am lost!'](#4111-help,-i-am-lost)
		1. ['Let us know'](#4112-let-us-know)
		1. [Login](#4113-login)
		1. [Share Medical Data](#4114-share-medical-data)
		1. ['Have you seen this man?'](#4115-have-you-seen-this-man)
		1. [At the airport](#4116-at-the-airport)
		1. ['The lines are open: scan now!'](#4117-the-lines-are-open-scan-now)
		1. [Clothing Label](#4118-clothing-label)
		1. [Formal Elections](#4119-formal-elections)
		1. [Luggage Label](#41110-luggage-label)
		1. [Track & Trace](#41111-track-&-trace)
		1. [Video Doorbell / Electronic Access](#41112-video-doorbell--electronic-access)
		1. [Trustable Reviews](#41113-trustable-reviews)
		1. [Tickets](#41114-tickets)
		1. [News Source](#41115-news-source)
		1. [Product Data](#41116-product-data)
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
		1. [Connect Token Create Request](#661-connect-token-create-request)
		1. [Connect Token Register Request](#662-connect-token-register-request)
		1. [Connect Token Update Request](#663-connect-token-update-request)
		1. [Connection Create Request](#664-connection-create-request)
		1. [Connection Delete Request](#665-connection-delete-request)
		1. [Connection Details Request](#666-connection-details-request)
		1. [Connections Request](#667-connections-request)
		1. [Consent Denied Request](#668-consent-denied-request)
		1. [Consent Granted Request](#669-consent-granted-request)
		1. [Consent Request](#6610-consent-request)
		1. [Consent Withdrawn Request](#6611-consent-withdrawn-request)
		1. [Consents Request](#6612-consents-request)
		1. [Message Post Request](#6613-message-post-request)
		1. [Messages Request](#6614-messages-request)
		1. [Operation Execute Request](#6615-operation-execute-request)
		1. [Operation Register Request](#6616-operation-register-request)
		1. [Operation References Request](#6617-operation-references-request)
		1. [Source Candidates Request](#6618-source-candidates-request)
		1. [Source Register Request](#6619-source-register-request)
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
1. [Diagram sources](#10-diagram-sources)
	1. [User Layer](#101-user-layer)
		1. [[Qiy Data Reuse]](#1011-[qiy-data-reuse])
		1. [Connect](#1012-connect)
			1. [[Users Connect]](#10121-[users-connect])
			1. [Generate token](#10122-generate-token)
			1. [Media](#10123-media)
			1. [Connect using a token in a website address](#10124-connect-using-a-token-in-a-website-address)
			1. [Connect using a QR Code](#10125-connect-using-a-qr-code)
			1. [Present proposal containing a QR Code](#10126-present-proposal-containing-a-qr-code)
	1. [Application Layer](#102-application-layer)
		1. [[Connect]](#1021-[connect])
			1. [Proposer: Connect](#10211-proposer-connect)
			1. [Generate Application Connect Token](#10212-generate-application-connect-token)
			1. [Accepter: Connect](#10213-accepter-connect)
		1. [Consent](#1022-consent)
			1. [[Relying Party]: Request [Consent]](#10221-[relying-party]-request-[consent])
			1. [Individual: Consider consent request](#10222-individual-consider-consent-request)
		1. [Request data](#1023-request-data)
			1. [[Relying Party]: Request [Data]](#10231-[relying-party]-request-[data])
			1. [Data Provider: Provide data](#10232-data-provider-provide-data)

# 1 Introduction
Qiy, or rather: the [Qiy Scheme], puts people back in control of their [Personal Data] while creating value for organizations that process it ([Relying Parties]).


## 1.1 Purpose

The document is aimed at people who know that Qiy puts people back in control of their [Personal Data], but who want or need to know the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.

## 1.2 Reader guidance

* Privacy officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Security officers are advised to read chapter [3 Architectural Description](#3-architectural-description).
* Information analysts are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer) and [5 The Application Layer](#5-the-application-layer).
* Application developers are advised to read chapters [3 Architectural Description](#3-architectural-description), [4 The User Layer](#4-the-user-layer), [5 The Application Layer](#5-the-application-layer) and [6 The Qiy Node Layer](#6-the-qiy-node-layer).
* Systems engineers are advised to read chapters [3 Architectural Description](#3-architectural-description), [8 The Transport Layer](#8-the-transport-layer) and [9 The Carrier Layer](#9-the-carrier-layer).

# 2 Overview

This chapter gives an overview of this document.
* [2.1 Data Reuse](#21-data-reuse) describes how [Data] can be reused with Qiy.
* [3 Architectural Description](#3-architectural-description) describes the [Architectural Layers] and addresses various concerns like privacy and security.
* [4 The User Layer](#4-the-user-layer) describes the setup and processes of the [Data Reuse] scenario at the [User] level.
* [5 The Application Layer](#5-the-application-layer) describes the processes at the application level.
* [6 The Qiy Node Layer](#6-the-qiy-node-layer) describes the same at the [Qiy Node] level.
* [7 The Service Layer](#7-the-service-layer) describes the [Service Layer] support.
* [8 The Transport Layer](#8-the-transport-layer) describes the [Transport Layer] support.
* [9 The Carrier Layer](#9-the-carrier-layer) describes the [Carrier Layer] support.
* [10 Diagram sources](#10-diagram-sources) contains the source code that has been used to generate the diagrams in this document.

## 2.1 Data Reuse

This document describes how Qiy realizes a [Data Reuse] scenario in which a [Data Subject] ([Individual]) reuses his [Personal Data] stored at one organization ([Data Provider]) and provide it to another organization ([Relying Party]) to consume one of its [Services].
Qiy can also be used for other applications, examples of wich can be found in [4.11 Application examples](#411-application-examples)

In essence, the [Data Reuse] goes as follows:
* The [Individual] subscribes to a [Service].
* The [Relying Party] asks the [Individual] for the [Data] it needs to provide the [Service].
* The [Individual] retrieves the [Data] from a [Data Provider].
* The [Individual] provides the [Data] to the [Relying Party].

![Qiy Data Reuse](./images/qiy-data-reuse.png)

### 2.1.1 Privacy concern

The [Data Reuse] scenario shows that the [Data] is transferred to the [Relying Party] by choice of the [Individual].
This breaks the chain of responsibility for the [Data Provider]; the responsibility for correct processing of the [Data] does not extend to any processing that takes place after the handover to the [Individual]. 

# 3 Architectural Description

This chapter describes the major entities of Qiy and their relations with the help of the [Architectural Layers] of the [Qiy Scheme] and addresses how Qiy addresses concerns like security and privacy.

## 3.1 Architectural Layers
The realization of the scenario is described using the following layers:

![Layers](./images/layers.png)

## 3.2 Privacy

Qiy has been conceived with the aim to put people back in control of their [Personal Data], hence making privacy the primary concern of Qiy.
The aim has been elaborated in a set of principles called the [Qiy Trust Principles] and technical, legal and governance rules, all of which are maintained by the [Qiy Foundation] and the [Qiy Foundation Members].

The realization of the [Data Reuse] as described in this document demonstrates that a natural person ([Individual]) is in control:
* The [Individual] can securily exchange [Data] and/or [Messages] with another person or organization ([Qiy User]) via Qiy, using [Connections], see [4 The User Layer](#4-the-user-layer).
* The [Individual] controls what [Qiy Users] he [Connects] with and, in principle, when he wants to end it.
* When an [Individual] [Connects] with a [Qiy User] that is providing a [Service] via Qiy ([Provider]), the [Individual] is provided with the identity of the latter, but not the other way around.
* The [Individual] can access his [Personal Data] that is kept by another [Qiy User] ([Data Provider]) as a result of the [Access Principle], one of the [Qiy Trust Principles].
* The [Individual] controls what [Data] he shares with what [Provider] ([Relying Party]) and under what terms using proveable [Consents].
* The [Data Provider] knows what [Data] is obtained by (or in name of) an [Individual], but he does not know whether the [Data] is shared and if so, with what [Relying Parties].
* [Relying Parties] however know the [Data Provider] of shared [Data] and can use this information to assess the trustworthiness of the [Data] and/or to verify the validity of the [Data].
* [Qiy Users] use applications that are authorized for use with Qiy ([Qiy Applications]).
* Access to Qiy, [Data] exchange via Qiy, [Consent Services] and potentially [Qiy Nodes] are provided by [Access Providers].


All parties involved are bound by the rules of the [Qiy Scheme]:
* [Providers] are bound by the [Binding Individual Rights] and the [Binding Principles for Relying Parties and Data Providers].
* [Access Providers] are bound by the [Licence Agreement Issuer] or the [Licence Agreement Service Provider].
* [Application Providers] can only develop and produce [Qiy Application]-[Services] and/or software with a [Licence Agreement Application Provider].

## 3.3 Security

As described above, privacy is at the heart of Qiy and security being a 'conditio sine qua no' for this, it is also addressed by the rules of the [Qiy Scheme].

## 3.4 Interoperability

An [Individual] can only control his [Personal Data], when all concerned systems are interoperable.
This is achieved as follows:
* Applications exchange [Data] and/or [Messages] via Qiy using open standards of the [Qiy Scheme] ([Qiy Open Standard]).
* Applications exchange self-describing [Data] and/or [Messages] using [Data Descriptions] which are available to all concerned parties (via the [Service Library]).

## 3.5 Governance

The governance rules are laid down in the [Governance Model for the Qiy Scheme], one of the documents of the [Qiy Scheme Rulebook].

## 3.6 Compliancy

The compliancy rules for [Providers] can be found in the [Binding Principles for Relying Parties and Data Providers], one of the documents of the [Qiy Scheme Rulebook].


# 4 The User Layer
This chapter describes the [User Layer] and the interaction between the [Relying Party], [Individual], [Data Provider] and the lower layers for the [Data Reuse].

## 4.1 Qiy Users
The organizations and/or persons using Qiy are called [Qiy Users]. They can use Qiy in different [roles]; they can use Qiy as a [Relying Party], [Individual], [Data Provider] or a combination of these.
A business for example will generally use Qiy both as a [Relying Party] (for offering [Services] using reliable [Personal Data]) and as a [Data Provider] (as a source of [Personal Data]).
As for natural persons, most of these will use Qiy as an [Individual] to control their [Personal Data].

## 4.2 Provider
A [Qiy User] that provides one or more [Services] to [Individuals] is said to be (or act in the [Business Role] of) '[Providers]'.
Any [Qiy User] acting in one or both of the roles [Relying Party] or [Data Provider] is implicitely acting in this role.

## 4.3 Qiy Node
A [Qiy User] must have a [Qiy Node]. 
[Providers] can acquire one from an [Access Provider].
[Individuals] obtain a [Qiy Node] the first time they use a [Qiy Application].
Alternatively, [Qiy Users] may instantiate a [Qiy Node] themselves using a [Qiy Node Implementation] and register it with an [Access Provider].

## 4.4 Connect via Qiy

Two [Qiy Users] can [Connect] via Qiy by creating a [Connection] between their [Qiy Nodes] ([Connection]).
The [Connection] can be initiated by either of the two [Qiy Users].
The [Qiy User] initiating the [Connection] is called the [Proposer], the other one [Accepter].
This goes as follows:
* The [Proposer] uses a [Qiy Application] to generate a [Token] (see [4.4.1 Generate token](#441-generate-token)) and to compose a [Connect Proposal].
* The [Proposer] provides it out-of-band to the [Accepter], for example by lettre, see [4.4.2 Media](#442-media).
* The [Accepter] may read the proposal and use a [Qiy Application] to extract the [Connect Token] and create a new [Connection] with the [Proposer].

As stated before, when a [Connection] is established, the identity of the [Qiy User] is provided to the other one if the [Qiy User] is a [Provider]. 
This information may be used to reuse a formerly created [Connection] and delete the new [Connection].

![Users Connect](./images/users-connect.png)

### 4.4.1 Generate token
A [Proposer] can create a [Token] using a [Qiy Application] and the following details:
* Name: The name or pseudonym to use in the [Connect Proposal].
* Expiration: Whether the [Token] expires and if so, on what date and time.
* Budget: The number of times that the [Token] can be used to create a [Connection].

In most cases, the expiration and budget are set by the application.
The Expiration and the Budget can be changed afterwards, for example to re-activate an expired [Token].

![Generate token](./images/generate-token.png)

(Diagram source code: [10.1.2.2 Generate token](#10122-generate-token))

 
### 4.4.2 Media
[Qiy Users] can use different media to [Connect] as illustrated in this diagram:

![Media](./images/Connect.png)

(Diagram source code: [10.1.2.3 Media](#10123-media))

 
#### 4.4.2.1 The web
[Qiy Users] can [Connect] by transfering a [Token] as a query parameter in a website address:
 
![Connect using a token in a website address](./images/connect-using-a-token-in-a-website-address.png)

(Diagram source code: [10.1.2.4 Connect using a token in a website address](#10124-connect-using-a-token-in-a-website-address))

 
#### 4.4.2.2 Print
[Qiy Users] can convert the [Token] to a QR Code and use various 'Print'-media to [Connect]:

![Present proposal containing a QR Code](./images/present-proposal-containing-a-qr-code.png)

(Diagram source code: [10.1.2.6 Present proposal containing a QR Code](#10126-present-proposal-containing-a-qr-code))


The QR Code can be used as follows to create the [Connection]:
 
![Connect using a QR Code](./images/connect-using-a-qr-code.png)

(Diagram source code: [10.1.2.5 Connect using a QR Code](#10125-connect-using-a-qr-code))
 

### 4.4.3 Examples


#### 4.4.3.1 Connect Proposal

The picture below shows a [Connect Proposal] that is generated by an [Individual] using a mobile app containing a QR Code.
The [Individual] can use this proposal to invite other [Individuals] to [Connect].

![An example of a Connect Proposal](./images/example--connect-proposal--qr-code-on-phone.PNG)

#### 4.4.3.2 Email
The picture below shows an example of a [Connect Proposal] in an email:

![An example of a Connect Proposal in an email](./images/example--connect-proposal--email.PNG)

#### 4.4.3.3 Webpage with QR Code
The picture below shows an example of a [Connect Proposal] in a webpage which displays a QR code when viewed on a laptop, pc or tablet:

![An example of a Connect Proposal in a webpage with QR code](./images/example--connect-proposal--webpage-laptop-pc-tablet.PNG)

#### 4.4.3.4 Webpage with button
The picture below shows an example of a [Connect Proposal] in a webpage which displays a button when viewed on smartphone:

![An example of a Connect Proposal in a webpage with button](./images/example--connect-proposal--webpage-phone.PNG)

#### 4.4.3.5 Accepting a Connect Proposal by scanning a QR code

The picture below shows an example of scanning the QR code in a [Connect Proposal] using a [Qiy Application]:

![An example of scanning a QR code](./images/example--connect-proposal--scan-qr-code.PNG)

#### 4.4.3.6 Accepting a Connect Proposal with a button click

When an [Accepter] has viewed a webpage with a [Connect Proposal] on his phone and clicked the button to accept it, he will be asked to confirm that he will be redirected to a [Qiy Application]:

![An example of confirming the redirect to a Qiy Application](./images/example--connect-proposal--after-the-button-click.PNG)

#### 4.4.3.7 Confirmation

The picture below shows an example of an [Qiy Application] verifying the acceptance of a [Connect Proposal].
The [Qiy Application] will create the [Connection] when the [Accepter] has confirmed that he wants to [Connect] with the [Proposer].

![An example of confirming the acceptance a Connect Proposal](./images/example--connect-proposal--verify.PNG)


## 4.5 Setup

This section addresses the setup for the [Data Reuse]

### 4.5.1 Relying Party

In order to be able to offer his [Services] via Qiy, a [Relying Party] has met the following preconditions:
* The [Relying Party] has acquired access to Qiy with the help of an [Access Provider].
* The [Access Provider] has verified and registered the identity of the [Relying Party] for use in Qiy.
* The [Service Library] contains the [Service Catalogue] of the [Relying Party] defining the provided [Services].
* The [Service Library] contains [Service Descriptions] for all the provided [Services], which also includes the terms of use, especially with regard to [Personal Data].

### 4.5.2 Data Provider

In order to be able to provide the [Personal Data] via Qiy, a [Data Provider] has met the following preconditions:
* The [Data Provider] has acquired access to Qiy with the help of an [Access Provider].
* The [Access Provider] has verified and registered the identity of the [Data Provider] for use in Qiy.
* A [Service Endpoint] is available to access the [Data].
* The [Service Library] contains the [Service Endpoint API] which describes how the [Data] can be obtained.
* The [Service Library] contains [Data Descriptions] for the available [Data].
* The [Service Library] contains the [Service Catalogue] of the [Data Provider] defining the provided [Data] [Services] and the related endpoints.
* The [Service Library] contains [Service Descriptions] for the provided [Data] [Services].

### 4.5.3 Individual

In order to be able to reuse [Personal Data] via Qiy, an [Individual] has met the following preconditions:
* The [Individual] has access to his [Personal Data] stored by one or more [Data Providers].
* The [Individual] has access to a personal [Qiy Node].
* The [Individual] is using a [Qiy Application] which is linked to his [Qiy Node].

## 4.6 Subscribe

[Data Reuse] starts with an [Individual] subscribing to a [Service], but only after considering and accepting the terms of use, including those regarding the use of [Personal Data].
When an [Individual] subscribes to a [Service], the subscription is registered by the [Qiy Application], so:
* The subscribed [Service] is recorded using the [Service Portfolio] of the [Individual].
* The record shows:
	* the start datetime of the subscription.
	* the [Provider] of the [Service] (the [Relying Party]).
	* what [Service] is provided (using the [Service Library]).
	* the related [Consent].

## 4.7 Consent

When a request for [Data] is received, it is checked with the granted [Consents]. If the request is not authorized by an active granted [Consent], this may be resolved by granting one, after which the [Data] request is processed.
In other cases, the request will not be accepted and no [Data] will be returned.

## 4.8 Routing

When all related conditions are met, a request for [Data] from a [Relying Party] is processed as follows:
* The [Service Portfolio] of the [Individual] is consulted to find the [Data Provider] or [Data Providers] and related [Service Endpoint API].
* Using the API, requests are created and used to obtain the [Data] from the [Service Endpoints].
* The received [Data] is forwarded to the [Relying Party].

## 4.9 Source

When a [Relying Party] has requested for [Data], the [Service Portfolio] is used to look up the [Data] source: the [Provider] or [Providers] that will provide the [Data] ([Service Source]).
This can be the [Individual] himself, for self-declared [Data], but it can also be one or more [Data Providers].
The source of the [Data] may have been defined before at the time of subscription, but if that it is not the case, the [Individual] will be asked to make a selection from a list of suitable [Data Providers] ([Service Discovery]).
The list will be generated using the [Service Catalogues] from the [Service Library].
The [Service Portfolio] will be updated with the outcome.

## 4.10 Session

A [Service Endpoint] will only process a request when issued over an active Session. This session may be started earlier, for example when the [Individual] selects a [Data Provider] as a source, but a new Session will be started if need be.
More often then not, this may require input from the [Individual].
The session credentials are persisted in the [Service Portfolio] of the [Individual].

## 4.11 Application Examples

This section gives some examples of other applications of Qiy.

### 4.11.1 'Help, I am lost!'

The [Connect Proposal] can be used on a badge to contact the parents of a wandering child:
![Scan the code to contact my parents](./images/example-application--help-iam-lost.PNG)

### 4.11.2 'Let us know'

The [Connect Proposal] can be used to react anonymously to a news item in a newspaper:

![Scan the code to let us know](./images/example-application--let-us-know.PNG)

### 4.11.3 Login

The [Connect Proposal] can be used by websites as a [User] friendly login alternative:

![Login](./images/example-application--login.PNG)

### 4.11.4 Share Medical Data

The [Connect Proposal] can be used to anonymously share medical [Data] for a visit at a medical facility:

![Share medical data](./images/example-application--share-medical-data.PNG)

### 4.11.5 'Have you seen this man?'

The [Connect Proposal] can be used to anonymously contribute to reduce crime:

![Have you seen this man?](./images/example-application--have-you-seen-this-man.PNG)

### 4.11.6 At the airport

Qiy can be used to route verifiable identifying [Data], for example to digitally use your passport to authenticate yourself at an airport:

![Digital passport](./images/example-application--digital-passport.PNG)

### 4.11.7 'The lines are open: scan now!'

The [Connect Proposal] can be used to vote for your favourite singer at a song contest:

![The lines are open: scan now!](./images/example-application--the-lines-are-open-scan-now.PNG)

### 4.11.8 Clothing Label

A [Connect Token] in its representation as a QR Code can be used in a clothing label to disclose product details:

![Clothing label](./images/example-application--clothing-label.jpg)

### 4.11.9 Formal Elections

A [Connect Token] in its representation as a QR Code can be used in formal elections to vote for a candidate:

![Formal Elections](./images/example-application--serious-voting.jpg)

### 4.11.10 Luggage Label

A [Connect Token] in its representation as a QR Code can be used as a luggage label:

![Luggage Label](./images/example-application--luggage-label.jpg)

### 4.11.11 Track & Trace

Barcodes in existing Track & Trace systems can be used as [Connect Tokens] for example to track and trace the delivery of a parcel:

![Track & Trace](./images/example-application--track-and-trace.jpg)

### 4.11.12 Video Doorbell / Electronic Access

Scanning a QR Code placed next to an entrance may be used to ring a doorbell and start a video call with the reception or house owner or result in the opening of a door when the visitor was invited for a meeting at the premises:

![Video Doorbell](./images/example-application--video-doorbell.jpg)

### 4.11.13 Trustable Reviews

Qiy allows solutions in which consumers can trust posted reviews on products or [Services]:

![Trustable Reviews](./images/example-application--trustable-reviews.jpg)

### 4.11.14 Tickets

Qiy allows ticketing-solutions were consumers can easily join an event and where ticket distribution is more under control of the organizer:

![Ticket](./images/example-application--ticket.jpg)

### 4.11.15 News Source

Qiy allows solutions were consumers can verify the source of news articles:

![Ticket](./images/example-application--trustable-news-source.jpg)

### 4.11.16 Product Data

Qiy allows consumers to share product [Data] and/or experiences with manufacturers:

![Product Data](./images/example-application--product-data.jpg)

# 5 The Application Layer
This chapter describes the [Application Layer] and how it supports the processes of the [Data Reuse] scenario.

## 5.1 Qiy Application
A [Qiy Application] is an [Application Service] or software which is authorized for use with Qiy.
* A [Qiy Application] must comply with the requirements of the [Qiy Scheme].
* A [Qiy User] can only use Qiy with a [Qiy Application].
* A [Qiy User] can use one or more [Qiy Applications].
* Two or more [Qiy Applications] can concurrently use one and the same [Qiy Node].

### 5.1.1 Application Provider
[Qiy Applications] can be provided by [Application Providers]. An [Application Provider] can only do so with a valid [License Agreement Application Provider].

### 5.1.2 Qiy Application Protocol
The [Qiy Application Protocol] describes the interactions of the [Qiy Applications] with eachother and the underlying layers.
* The [Qiy Application Protocol] is an open standard and is part of the [Qiy Open Standard].

The [Qiy Application Protocol] describes among others how [Qiy Applications]:
* ... create a [Qiy Node] for a [Qiy User].
* ... can be linked to a [Qiy Node] of a [Qiy User].
* ... create [Connections].
* ... create a 'backup' of a [Qiy Node].
* ... exchange [Connect Tokens] out-of-band.
* ... exchange [Messages].
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
For more information, please refer to [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).

### 5.2.2 Proposer: Connect
For a [Qiy Application] of a [Proposer], a [Connection] is established as follows:
* The [Qiy Application] generates an [Application Connect Token], see [5.2.3 'Generate Application Connect Token'](#523-generate-application-connect-token).
* The [Qiy Application] composes a [Connect Proposal] for the [Proposer].
* The [Proposer] presents it out-of-band to the [Accepter].
* When the [Accepter] wants to [Connect], he uses the [Connect Proposal] to create a [Connection] with his [Qiy Application], see [5.2.4 'Accepter: Connect'](#524-accepter-connect).
* The [Proposer] detects this by use of polling (using the [Connections Request]) or events (using the [Connection Created Event]).
 
![Proposer: Connect](./images/proposer--connect.png)

(Diagram source code: [10.2.1.1 Proposer: Connect](#10211-proposer-connect))

### 5.2.3 Generate Application Connect Token
The main part of an [Application Connect Token] is the [Connect Token]. The [Qiy Application] can create this both online and offline:
* Offline by creating a [Connect Token] and registering it later using a [Connect Token Register Request].
* Online using a [Connect Token Create Request].

![Generate Application Connect Token](./images/generate-application-connect-token.png)

(Diagram source code: [10.2.1.2 Generate Application Connect Token](#10212-generate-application-connect-token))

### 5.2.4 Accepter: Connect
At the [Accepter]-side, a [Qiy Application] creates a [Connection] with a [Connect Proposal] or [Connect Token] as follows:
* In case of a [Connect Proposal], the [Qiy Application] extracts the [Connect Token] from the [Connect Proposal].
* The [Qiy Application] uses the [Connect Token] in [Connection Create Request] to the [Qiy Node] of the [Qiy User].
* The [Qiy Node] creates the [Connection] and returns the id of the [Connection] ([Connection Uri]).

![Accepter: Connect](./images/accepter--connect.png)

(Diagram source code: [10.2.1.3 Accepter: Connect](#10213-accepter-connect))

## 5.3 Consent

### 5.3.1 Relying Party: Request consent

A [Qiy Application] of a [Relying Party] can request an [Individual] for [Consent] as follows:
* The [Qiy Application] sends a [Consent Request Message] over the [Connection] with the [Individual].
* The [Qiy Application] receives a [Message] with the outcome, either a [Consent Granted Message] or a [Consent Denied Message].

![Relying Party: Request consent](./images/relying-party--request-consent.png)

### 5.3.2 Individual: Consider consent request
A [Qiy Application] of an [Individual] processes a [Consent Request] as follows:
* The [Qiy Application] detects receiving a [Consent Request Message] by polling (using the [Messages Request]) or with events (using the [Message Received Event]).
* The [Qiy Application] extracts the [Consent Request] and presents it to the [Individual].
* Depending on the choice of the [Individual], the [Qiy Application] returns a [Consent Granted Message] or a [Consent Denied Message] using the [Connection] with the [Relying Party].

![Individual: Consider consent request](./images/individual--consider-consent-request.png)

(Diagram source code: [10.2.2.2 Individual: Consider consent request](#10222-individual-consider-consent-request))

## 5.4 Service Discovery
A [Qiy Application] can present an [Individual] a list of suitable [Data Providers] (or in general [Providers]) that can produce some requested [Data] (or [Services]) as follows:
* The [Qiy Application] asks the [Qiy Node] of the [Individual] for a list of suitable [Data Providers] with a [Source Candidates Request].
* The [Qiy Node] consults the [Service Library] and returns the outcome to the [Qiy Application].
* The [Qiy Application] presents the result to the [Individual].
* The [Qiy Application] registers the selected sources with a [Source Register Request].

## 5.5 Data by Reference
[Qiy Applications] exchange [data by reference] rather then by value.
This goes as follows:
* A [Qiy Application] requests a reference for the [Data] ([Data Reference]).
* The [Qiy Application] receives a [Data Reference].
* The [Qiy Application] uses the [Data Reference] to acquire the [Data].

### 5.5.1 Service by Reference
In Qiy providing [Data] is viewed as a [Service] and requesting [Data] as an [Operation] of this [Service], so the 'data by reference'-pattern is implemented as using a [Service by Reference]-pattern:
* A [Qiy Application] requests an [Operation Reference] using an [Operation Reference Request Message].
* An [Operation Reference] is created by registrating the [Operation Specification] using an [Operation Register Request] and returned using an [Operation Reference Message].
* The [Qiy Application] can call for the execution of an [Operation] by submitting the [Operation Reference] in an [Operation Execute Request].

### 5.5.2 Request data reference
The [Qiy Application] of a [Relying Party] can request an [Individual] for a [Data Reference] as follows:
* The [Qiy Application] sends a [Operation Reference Request Message] using the [Connection] of the [Individual].
* The [Qiy Application] receives the [Operation Reference] in an [Operation Reference Message].

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.3 Create reference
A [Qiy Application] can create an [Operation Reference] using a specification of the [Operation] ([Operation Specification]).
This goes as follows:
* The [Qiy Application] uses the [Operation Specification] in an [Operation Register Request] to the [Qiy Node] it is linked with.
* The [Qiy Node] creates the [Operation Reference] and returns it.

### 5.5.4 Request data
The [Qiy Application] of a [Relying Party] can obtain [Data] using a [Data Reference] / [Operation Reference]. 
This goes as follows:
* The [Qiy Application] uses the [Operation Reference] in a [Operation Execute Request] to its [Qiy Node].
* The [Qiy Node] returns the requested [Data].

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.5 Provide data
The [Data Provider] produces the [Data] using his [Service Endpoint].
This does not involve any of the [Qiy Applications] of the [Data Provider] nor his [Qiy Node].

![Data Provider: Provide data](./images/data-provider--provide-data.png)

(Diagram source code: [10.2.3.2 Data Provider: Provide data](#10232-data-provider-provide-data))

# 6 The Qiy Node Layer
This chapter describes the [Qiy Node Layer] and how it supports the upper layers.

## 6.1 Access Provider
The [Services] of this layer can be provided by an [Access Provider]:
* An [Access Provider] can provide [Qiy Nodes].
* An [Access Provider] can host [Qiy Nodes].

### 6.1.1 Portability
An [Access Provider] can offer [Qiy Node]-[Services] to [Qiy Users], but must enable [Qiy Users] to easily transfer the [Services] to a different [Access Provider].

## 6.2 Qiy Node
A [Qiy Node] is a [Technology Service] as defined in [Definitions of the Qiy Scheme].
A [Qiy Node]:
* ... must comply with the rules of the [Qiy Scheme].
* ... can be hosted on any host ([Node]).
* ... has its own [Transporter] which ensures secure transport of [Messages] and/or [Data] via Qiy.

### 6.2.1 Qiy Node Protocol
The [Qiy Node Protocol] describes the interaction between the [Qiy Nodes] and the underlying layers.
* The [Qiy Node Protocol] is one of the protocols in the [Qiy Open Standard].
The [Qiy Node Protocol] describes for example:
* How a [Qiy Node] is instantiated.
* How [Qiy Nodes] create [Connections] and use them to exchange [Data], [Messages] or to provide/consume [Services].

### 6.2.2 Qiy Node API
The [Qiy Node API] is the [Technology Interface] of the [Qiy Node], one of the APIs of the [Qiy Open Standard].
* The [Qiy Node API] is intended for use by [Qiy Applications].

### 6.2.3 Qiy Node Implementation
A [Qiy Node Implementation] is a software package which can be used to realize a [Qiy Node].
The [Qiy Scheme] puts no limit on the number of [Qiy Node Implementations], as long as the implementation complies with the [Qiy Open Standard] and the rules of the [Qiy Scheme]. 

### 6.2.4 Qiy Node Instantiation
A [Qiy Node] can be created in two ways:
* It can be instantiated by an [Access Provider]. The [Access Provider] will instantiate it with its own [Transporter]. 
* It can be instantiated by a [Qiy User] on a [Node] of his own using a [Qiy Node Implementation]. 
When the second option is chosen, the [Qiy User] is responsible for obtaining a [Transporter] and linking it to the [Qiy Node].

### 6.2.5 Deleting a Qiy Node
In principle, a [Qiy Node] can be deleted by its owner whenever he wants to do so.
In this case, the [Qiy Node] will be deleted including persisted [Data], [Connections] and the linked [Transporter].
Related [Consents] will be withdrawn.

## 6.3 Connect
Two [Qiy Nodes] can [Connect] by creating a [Path] between themselves.
* A [Qiy Node] can [Connect] with zero or more other [Qiy Nodes].
* A [Qiy Node] can have zero or more [Paths] with any other [Qiy Node].
* A priori, a [Qiy Node] does not know the identity of the [Qiy Node] at the other side of a [Path].

### 6.3.1 Connection Uri
The [Connection Uri] is the [Uri] which identifies a [Connection] for one of the [Qiy Node] it [Connects].
* A [Connection] has two [Connection Uris]; one for each of the two [Qiy Nodes] it [Connects].
* The two [Connection Uris] of one [Connection] are not related to one another.
* A priori, a [Qiy Node] does not know the other [Connection Uri] of a [Connection].

EXAMPLE: [Connection Uris] of a [Connection] between [Qiy Node] 1 and [Qiy Node] 2:

[Qiy Node] | [Connection Uri]
---- | --------------
[Qiy Node] 1	| http://127.0.0.1:8087/[User]/[Connections]/[User]/usernodeB/93590b55-9194-4cf4-944f-2cbceab7dbcd
[Qiy Node] 2	| http://127.0.0.1:8087/[User]/[Connections]/[User]/usernodeA/f96bc541-e98b-449e-bfc5-48ec928e0dc9

#### 6.3.1.1 Security concern
The [Connection Uri] has only meaning in the context of the [Qiy Node] that knows it and is useless outside this scope.
For example, the [Uri] by itself can not be used to exchange a [Message] with the [Qiy Node] nor any other existing [Qiy Node].

### 6.3.2 Connect Token
A [Connect Token] is a [Token] which can be used by a [Qiy Application] to create a [Connection].
It consists of:
* a temporary secret
* a [Transport Connect Token].

A [Connect Token] has the following properties:
* An expiration setting: Whether the [Token] expires and if so, on what date and time
* A budget: The number of times that the [Token] can be used to create a [Connection]. 

The properties can not only be set when the [Token] is registered or requested, but also later.
For example, it is possible to reactivate a [Connect Token] by increasing the budget or inactivate one by changing the expiration.

#### 6.3.2.1 Security concern
The [Connect Token] can only be used to create a [Connection] and only so via Qiy, with the help of a [Qiy Application] and a linked [Qiy Node].
By itself, it cannot be used for any other purpose, for example gain access to a [Qiy Node] nor any other parts of the Qiy infrastructuur.

#### 6.3.2.2 Creating a Connect Token
A [Connect Token] can be created both offline and online:
* A [Connect Token] can be obtained from the [Qiy Node] using a [Connect Token Create Request] ([Online Connect Token]).
* A [Connect Token] can be created by a [Qiy Application] and registered later using a [Connect Token Register Request] ([Offline Connect Token]).

The [Offline Connect Token] allows initiating a [Connection] (creating a [Connect Token]) even when Qiy is temporarily not available.
However, care must be taken that the created [Token] is unique, especially so for the created [Transport Connect Token].

#### 6.3.2.3 Creating a Transport Connect Token
A [Qiy Node] will never create a [Transport Connect Token]:
* In case of an [Online Connect Token]: The [Qiy Node] will obtain a [Transport Connect Token] from its [Transporter].
* In case of an [Offline Connect Token]: The [Qiy Node] will compose a [Transport Connect Token] using the [Connect Token] provided by the [Qiy Application] and register it at its [Transporter].

### 6.3.3 Connecting
Two [Qiy Nodes] [Connect] as follows:
* The [Qiy Node] of the [Proposer] either 1) obtains a [Transport Connect Token] from the [Transporter] or 2) from a linked [Qiy Application] in a [Connection Create Request].
* The [Qiy Node] either 1) provides the [Transport Connect Token] to the [Qiy Application] or 2) registers the [Transport Connect Token] at its [Transporter].
* The [Transport Connect Token] is made available (partly out-of-bands, for example in a [Connect Proposal]) to the [Qiy Node] of the [Accepter].
* The [Qiy Node] of the [Accepter] uses its [Transporter] to create a [Path] using the [Transport Connect Token].
Each accepted [Path Create Request] leads to a new [Path], irrespective of the number of existing [Paths] between the two [Qiy Nodes].

### 6.3.4 Deleting a Connection
A [Connection] can be deleted with a [Connection Delete Request].
The [Connection] will be deleted completely, including any persisted [Data] and/or [Messages] and underlying [Paths].
Any related [Consents] will be withdrawn.

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
A [Qiy Node Request] is a [Http Request] for a [Qiy Node]. 
[Qiy Node Requests] are only accepted when they are correctly authenticated with:
* the [Node Id].
* an actual timestamp
* a digital signature over the [Node Id], the timestamp and the contents of the body of the request made with the private key

## 6.6 Qiy Node Requests
This section gives an overview of the [Qiy Node Requests].
Details of [Qiy Node Requests] can be found in the [Qiy Node API].

### 6.6.1 Connect Token Create Request
The [Connect Token Create Request] is a [Qiy Node Request] that can be used to obtain a [Connect Token] from the [Qiy Node].

### 6.6.2 Connect Token Register Request
The [Connect Token Register Request] is a [Qiy Node Request] that can be used to register a [Connect Token].

### 6.6.3 Connect Token Update Request
The [Connect Token Update Request] is a [Qiy Node Request] that can be used to update a [Connect Token].

### 6.6.4 Connection Create Request
The [Connection Create Request] is a [Qiy Node Request] that can be used to create a [Connection] with a [Connect Token].

### 6.6.5 Connection Delete Request
The [Connection Delete Request] is a [Qiy Node Request] that can be used to delete a [Connection].

### 6.6.6 Connection Details Request
The [Connection Details Request] is a [Qiy Node Request] that can be used to acquire the details of a [Connection].

### 6.6.7 Connections Request
The [Connections Request] is a [Qiy Node Request] that can be used to obtain a list of all the [Connections] of a [Qiy Node].

### 6.6.8 Consent Denied Request
The [Consent Denied Request] is a [Qiy Node Request] that can be used to record the denial of a [Consent].

### 6.6.9 Consent Granted Request
The [Consent Granted Request] is a [Qiy Node Request] that can be used to record the granting of a [Consent].

### 6.6.10 Consent Request
The [Consent Request] is a [Qiy Node Request] which can be used to request for a [Consent].

### 6.6.11 Consent Withdrawn Request
The [Consent Withdrawn Request] is a [Qiy Node Request] that can be used to record the withdrawal of a [Consent].

### 6.6.12 Consents Request
The [Consents Request] is a [Qiy Node Request] that can be used to obtain a list of all the [Consents] of a [Qiy Node].

### 6.6.13 Message Post Request
The [Message Post Request] is a [Qiy Node Request] that can be used to post a [Qiy Node Message].

### 6.6.14 Messages Request
The [Messages Request] is a [Qiy Node Request] that can be used to obtain a list of all the [Messages] of a [Qiy Node].

### 6.6.15 Operation Execute Request
The [Operation Execute Request] is a [Qiy Node Request] that can be used to command the execution of an [Operation] by reference using an [Operation Reference].

### 6.6.16 Operation Register Request
The [Operation Register Request] is a [Qiy Node Request] that can be used to obtain an [Operation Reference] by registrating an [Operation Specification].

### 6.6.17 Operation References Request
The [Operation References Request] is a [Qiy Node Request] that can be used to obtain a list of all the [Operation References] of a [Qiy Node].

### 6.6.18 Source Candidates Request
The [Source Candidates Request] is a [Qiy Node Request] to obtain candidate [Providers] for a [Service].

### 6.6.19 Source Register Request
The [Source Register Request] is a [Qiy Node Request] to register a [Provider] as source for a [Service].
 
## 6.7 Qiy Node Message
A [Qiy Node Message] is a [Message] that is exchanged using a [Connection].
[Qiy Node Messages] can be sent with the [Message Post Request], obtained using a [Messages Request] and monitored with [Qiy Node Events] like [Message Received Event].

## 6.8 Qiy Node Messages
This section gives an overview of the [Qiy Node Messages].
Details of [Qiy Node Messages] can be found in the [Qiy Node Protocol].

### 6.8.1 Consent Denied Message
The [Consent Denied Message] is a [Qiy Node Message] which can be used to communicate the denial of a [Consent].

### 6.8.2 Consent Granted Message
The [Consent Granted Message] is a [Qiy Node Message] which can be used to communicate the granting of a [Consent].

### 6.8.3 Consent Request Message
The [Consent Request Message] is a [Qiy Node Message] which can be used to request for a [Consent].

### 6.8.4 Operation Reference Message
The [Operation Reference Message] is a [Qiy Node Message] that can be used to convey [Operation References] over a [Connection].
 
### 6.8.5 Operation Reference Request Message
The [Operation Reference Request Message] is a [Qiy Node Message] that can be used to request for [Operation References].
 
## 6.9 Qiy Node Event
A [Qiy Node Event] is a [Technology Event] of a [Qiy Node].

## 6.10 Qiy Node Events
This section gives an overview of the [Qiy Node Events].
Details of [Qiy Node Events] can be found in the [Qiy Node Protocol].

### 6.10.1 Connection Created Event
The [Connection Created Event] is a [Qiy Node Event] that is generated when a [Connection] has been created.

### 6.10.2 Consent Withdrawn Event
The [Consent Withdrawn Event] is a [Qiy Node Event] that is generated when a [Consent] has been withdrawn.

### 6.10.3 Message Received Event
The [Message Received Event] is a [Qiy Node Event] that is generated when a [Qiy Node Message] has been received.

### 6.10.4 Operation Reference Received Event
The [Operation Reference Received Event] is a [Qiy Node Event] that is generated when a [Qiy Node] has received a new [Operation Reference].

### 6.10.5 Source Candidate Event
The [Source Candidate Event] is a [Qiy Node Event] that is generated when a [Qiy Node] has received a new [Source Candidate] for a [Consent].

# 7 The Service Layer
The [Service Layer] provides the following [Technology Services] to support the provisioning and consumption of [Services] via Qiy:
* [Service Endpoints]
* [Service Library]
* [Consent Service]

## 7.1 Access Provider
The [Service Library] and [Consent Service] are both provided by an [Access Provider].

### 7.1.1 Portability
The [Qiy Scheme] prescribes that one can easily change to a different [Access Provider] for these [Services].

## 7.2 Service
In general, a [Service] is an 'information society service' as defined in the [GDPR], with the following enhancements:
* A [Service] can be consumed with the use of one or more [Operations].
* A [Service] is provided by a [Provider].
* A [Provider] can offer one or more [Services].
* One [Service] can be offered by one or more [Providers].
* The [Services] that a [Provider] offers are described in a [Service Catalogue].
* The [Services] that an [Individual] consumes are described in his [Service Portfolio].

As for Qiy, the following definitions apply:
* Both [Relying Parties] and [Data Providers] are [Providers].

## 7.3 Service Endpoints
A [Service Endpoint] is a [Technology Service] provided by a [Provider] to allow the consumption of his [Services]:
* A [Provider] can employ one or more [Service Endpoints].
* A [Service Endpoint] can be used for one or more [Services].
* A [Service] can be consumed with the use of one or more [Service Endpoints].

For example, a [Service Endpoint] may be used by a [Data Provider] to disclose the [Personal Data] from one of his databases.

## 7.4 Service Library
The [Service Library] is used for:
* [Data Descriptions]
* [Providers]
* [Service Catalogues]
* [Service Descriptions]

## 7.5 Consent Service
A [Consent Service] is used for maintaining [Consents] and their status.
A [Consent] can be accessed by both of the involved [Qiy Users]: the [Individual] and the [Provider].

* In principle, only an [Individual] can withdraw a [Consent] he has granted before.
* A [Provider] can only obtain [Personal Data] under a [Consent] which has not been withdrawn.

# 8 The Transport Layer
The [Transport Layer] supports the secure transmission of [Messages] ([Transport Messages]) over [Paths] between [Transporters].

## 8.1 Access Provider
The [Services] of this layer are only provided by an [Access Provider].

### 8.1.1 Portability
The [Qiy Scheme] prescribes that one can easily switch [Access Provider] for these [Services].

## 8.2 Transporter
A [Transporter] is a [Technology Service] which allows the secure transmission of [Messages] and/or [Data].
* A [Transporter] must comply with the rules of the [Qiy Scheme].
* A [Transporter] is hosted on a [Carrier Node].
* Each [Qiy Node] has its own [Transporter].

A [Transporter] can be used for:
* Creating [Paths] with other [Transporters].
* Securely transmitting [Transport Messages] over these [Paths].

## 8.3 Transport Protocol
The [Transport Protocol] describes the interaction between [Transporters] and the underlying layer.
The protocol is one of the protocols of the [Qiy Open Standard].

## 8.4 Transporter API
The [Transporter API] is the [Technology Interface] of the [Transporter], one of the APIs of the [Qiy Open Standard].
* The [Transporter API] is intended for use by [Qiy Nodes].

## 8.5 Transporter Implementation
A [Transporter Implementation] is a software package which can be used to realize a [Transporter].
The [Qiy Scheme] puts no limit on the number of [Transporter Implementations], as long as the implementation complies with the [Qiy Open Standard] and the rules of the [Qiy Scheme]. 

## 8.6 Transporter Instantiation
A [Transporter] can only be instantiated by an [Access Provider].

## 8.7 Deleting a Transporter
A [Transporter] can be deleted by its [Qiy Node].
In this case, the [Transporter] will be deleted including any persisted [Data] and [Routes].

## 8.8 Path
A [Path] is a logical [Connection] between two [Transporters] that can be used to exchange [Transport Messages].
Physically seen, the [Path] may be dynamic and stretch over several [Carriers].

### 8.8.1 Path Creation
A [Path] can be created by a [Transporter] with a [Transport Connect Token].

### 8.8.2 Deleting a Path
A [Path] can be deleted by either of the ending [Transporters]. 
The [Path] will be deleted including any persisted [Data] and/or [Messages].

# 9 The Carrier Layer
The [Carrier Layer] supports the creation of [Paths] and the secure transport of [Messages] over them.

## 9.1 Access Provider
The [Services] of this layer are only provided by an [Access Provider].

### 9.1.1 Portability
The [Qiy Scheme] prescribes that one can easily switch [Access Provider] for these [Services].

## 9.2 Carrier
The [Carrier] is [Technology Service] which can be used for:
* To obtain a [Transporter].
* To create [Paths].
* To safely [Transport Messages] between [Carriers].
* To obtain a [Qiy Node].

The [Carrier] comes with the following rules:
* A [Carrier] must comply with the rules of the [Qiy Scheme].
* A [Carrier] must support the [Carrier API].

## 9.3 Carrier Protocol
The [Carrier Protocol] describes the interaction between [Carriers].
The protocol is part of the [Qiy Open Standard].

## 9.4 Carrier API
The [Carrier API] is the [Technology Interface] of the [Carrier] and is part of the [Qiy Open Standard].

## 9.5 Carrier Implementation
A [Carrier Implementation] is a software package which can be used to realize a [Carrier]
The [Qiy Scheme] puts no limit on the number of [Carrier Implementations], as long as the implementation complies with the [Qiy Open Standard] and the rules of the [Qiy Scheme]. 

## 9.6 Carrier Node
A [Carrier Node] is a [Node] which hosts one or more [Carriers].
* The [Carrier Node] is provided by an [Access Provider].
* The [Access Provider] can provide one or more [Carrier Nodes].


# 10 Diagram sources

The diagrams in this document are generated using the online sequence diagram generator of https://www.websequencediagrams.com.
This chapter contains the source code of these diagrams.

## 10.1 User Layer
### 10.1.1 [Qiy Data Reuse]
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
### 10.1.2 Connect
#### 10.1.2.1 [Users Connect]
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

#### 10.1.2.2 Generate token
```
title Generate token

Proposer->Proposer: Set name, expiration & budget
Proposer->+Qiy Application: Request token
Qiy Application->Qiy Application: Generate token
Qiy Application-->Proposer: token
```

#### 10.1.2.3 Media
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
#### 10.1.2.4 Connect using a token in a website address
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
#### 10.1.2.5 Connect using a QR Code
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
#### 10.1.2.6 Present proposal containing a QR Code
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

## 10.2 Application Layer
### 10.2.1 [Connect]
#### 10.2.1.1 Proposer: Connect
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
#### 10.2.1.2 Generate Application Connect Token
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

#### 10.2.1.3 Accepter: Connect
```
title Accepter: Connect

Qiy Application->Qiy Application: Extract Connect Token from connect proposal
Qiy Application->Qiy Node: Connect
Qiy Node-->Qiy Application: Connection Uri, [Proposer Id]
```

### 10.2.2 Consent
#### 10.2.2.1 [Relying Party]: Request [Consent]
```
title Relying Party: Request consent

Qiy Application->Qiy Node: Request consent
alt Grant
    Qiy Node->Qiy Application: Consent Granted Event
else Deny
    Qiy Node->Qiy Application: Consent Denied Event
end
```
#### 10.2.2.2 Individual: Consider consent request
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

### 10.2.3 Request data
#### 10.2.3.1 [Relying Party]: Request [Data]
```
title Relying Party: Request data

Qiy Application->Qiy Application: Look-up reference
Qiy Application->+Qiy Node: Request data
Qiy Node->Qiy Node: Look-up and use request
Qiy Node-->Qiy Application: data
```

#### 10.2.3.2 Data Provider: Provide data
```
title Data Provider: Provide data

note over Qiy Application,Qiy Node: 
The data is fetched and returned by 
the Service Endpoint 
of the Data Provider.
```




