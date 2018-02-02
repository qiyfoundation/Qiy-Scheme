# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From Qiy Nodes to data exchange


# Contents

1. [Introduction](#1-introduction)
	1. [Purpose](#1.1-purpose)
	1. [Reader guidance](#1.2-reader-guidance)
1. [Overview](#2-overview)
	1. [Data Reuse](#2.1-data-reuse)
		1. [Privacy concern](#2.1.1-privacy-concern)
1. [Architectural Description](#3-architectural-description)
	1. [Architectural Layers](#3.1-architectural-layers)
	1. [Privacy](#3.2-privacy)
	1. [Security](#3.3-security)
	1. [Interoperability](#3.4-interoperability)
	1. [Governance](#3.5-governance)
	1. [Compliancy](#3.6-compliancy)
1. [The User Layer](#4-the-user-layer)
	1. [Qiy Users](#4.1-qiy-users)
	1. [Provider](#4.2-provider)
	1. [Qiy Node](#4.3-qiy-node)
	1. [Connect via Qiy](#4.4-connect-via-qiy)
		1. [Generate token](#4.4.1-generate-token)
		1. [Media](#4.4.2-media)
			1. [The web](#4.4.2.1-the-web)
			1. [Print](#4.4.2.2-print)
	1. [Setup](#4.5-setup)
		1. [Relying Party](#4.5.1-relying-party)
		1. [Data Provider](#4.5.1-data-provider)
		1. [Individual](#4.5.2-individual)
	1. [Subscribe](#4.6-subscribe)
	1. [Consent](#4.7-consent)
	1. [Routing](#4.8-routing)
	1. [Source](#4.9-source)
	1. [Session](#4.10-session)
1. [The Application Layer](#5-the-application-layer)
	1. [Qiy Application](#5.1-qiy-application)
		1. [Application Provider](#5.1.1-application-provider)
		1. [Qiy Application Protocol](#5.1.2-qiy-application-protocol)
		1. [Creating Qiy Nodes for Individuals](#5.1.3-creating-qiy-nodes-for-individuals)
			1. [Security consideration](#5.1.3.1-security-consideration)
		1. [Link with an existing Qiy Node](#5.1.4-link-with-an-existing-qiy-node)
	1. [Connect](#5.2-connect)
		1. [Application Connect Token](#5.2.1-application-connect-token)
		1. [Proposer: Connect](#5.2.2-proposer:-connect)
		1. [Generate Application Connect Token](#5.2.3-generate-application-connect-token)
		1. [Accepter: Connect](#5.2.4-accepter:-connect)
	1. [Consent](#5.3-consent)
		1. [Relying Party: Request consent](#5.3.1-relying-party:-request-consent)
		1. [Individual: Consider consent request](#5.3.2-individual:-consider-consent-request)
	1. [Service Discovery](#5.4-service-discovery)
	1. [Data by Reference](#5.5-data-by-reference)
		1. [Service by Reference](#5.5.1-service-by-reference)
		1. [Request data reference](#5.5.1-request-data-reference)
		1. [Create reference](#5.4.2-create-reference)
		1. [Request data](#5.5.1-request-data)
		1. [Provide data](#5.5.2-provide-data)
1. [The Qiy Node Layer](#6-the-qiy-node-layer)
	1. [Access Provider](#6.1-access-provider)
		1. [Portability](#6.1.1-portability)
	1. [Qiy Node](#6.2-qiy-node)
		1. [Qiy Node Protocol](#6.2.1-qiy-node-protocol)
		1. [Qiy Node API](#6.2.2-qiy-node-api)
		1. [Qiy Node Implementation](#6.2.3-qiy-node-implementation)
		1. [Qiy Node Instantiation](#6.2.4-qiy-node-instantiation)
		1. [Deleting a Qiy Node](#6.2.5-deleting-a-qiy-node)
	1. [Connect](#6.3-connect)
		1. [Connection Uri](#6.3.1-connection-uri)
			1. [Security concern](#6.3.1.1-security-concern)
		1. [Connect Token](#6.3.2-connect-token)
			1. [Security concern](#6.3.2.1-security-concern)
			1. [Creating a Connect Token](#6.3.2.2-creating-a-connect-token)
			1. [Creating a Transport Connect Token](#6.3.2.3-creating-a-transport-connect-token)
		1. [Connecting](#6.3.3-connecting)
		1. [Deleting a Connection](#6.3.4-deleting-a-connection)
	1. [Consent](#6.4-consent)
		1. [Consent Uri](#6.4.1-consent-uri)
		1. [Consent Service Descriptor](#6.4.2-consent-service-descriptor)
		1. [Consent Data Descriptor](#6.4.3-consent-data-descriptor)
			1. [Privacy concern](#6.4.3.1-privacy-concern)
	1. [Qiy Node Request](#6.5-qiy-node-request)
	1. [Qiy Node Requests](#6.6-qiy-node-requests)
		1. [Connect Token Creation Request](#6.6.1-connect-token-creation-request)
		1. [Connect Token Registration Request](#6.6.2-connect-token-registration-request)
		1. [Connect Token Update Request](#6.6.3-connect-token-update-request)
		1. [Connection Create Request](#6.6.4-connection-create-request)
		1. [Connection Delete Request](#6.6.5-connection-delete-request)
		1. [Connections Request](#6.6.6-connections-request)
		1. [Consent Denied Request](#6.6.7-consent-denied-request)
		1. [Consent Granted Request](#6.6.8-consent-granted-request)
		1. [Consent Request](#6.6.9-consent-request)
		1. [Consent Withdrawn Request](#6.6.10-consent-withdrawn-request)
		1. [Consents Request](#6.6.11-consents-request)
		1. [Message Post Request](#6.6.12-message-post-request)
		1. [Messages Request](#6.6.13-messages-request)
		1. [Operation Execution Request](#6.6.14-operation-execution-request)
		1. [Operation Registration Request](#6.6.15-operation-registration-request)
		1. [Operation References Request](#6.6.16-operation-references-request)
		1. [Source Candidates Request](#6.6.17-source-candidates-request)
		1. [Source Registration Request](#6.6.18-source-registration-request)
	1. [Qiy Node Message](#6.7-qiy-node-message)
	1. [Qiy Node Messages](#6.8-qiy-node-messages)
		1. [Consent Denied Message](#6.8.1-consent-denied-message)
		1. [Consent Granted Message](#6.8.2-consent-granted-message)
		1. [Consent Request Message](#6.8.3-consent-request-message)
		1. [Operation Reference Message](#6.8.4-operation-reference-message)
		1. [Operation Reference Request Message](#6.8.5-operation-reference-request-message)
	1. [Qiy Node Event](#6.9-qiy-node-event)
	1. [Qiy Node Events](#6.10-qiy-node-events)
		1. [Connection Created Event](#6.10.1-connection-created-event)
		1. [Consent Withdrawn Event](#6.10.2-consent-withdrawn-event)
		1. [Message Received Event](#6.10.3-message-received-event)
		1. [Operation Reference Received Event](#6.10.4-operation-reference-received-event)
		1. [Source Candidate Event](#6.10.5-source-candidate-event)
1. [The Service Layer](#7-the-service-layer)
	1. [Access Provider](#7.1-access-provider)
		1. [Portability](#7.1.1-portability)
	1. [Service](#7.2-service)
	1. [Service Endpoints](#7.3-service-endpoints)
	1. [Service Library](#7.4-service-library)
	1. [Consent Service](#7.5-consent-service)
1. [The Transport Layer](#8-the-transport-layer)
	1. [Access Provider](#8.1-access-provider)
		1. [Portability](#8.1.1-portability)
	1. [Transporter](#8.2-transporter)
	1. [Transport Protocol](#8.2.1-transport-protocol)
	1. [Transporter API](#8.2.2-transporter-api)
	1. [Transporter Implementation](#8.2.3-transporter-implementation)
	1. [Transporter Instantiation](#8.2.4-transporter-instantiation)
	1. [Deleting a Transporter](#8.2.5-deleting-a-transporter)
	1. [Path](#8.3-path)
		1. [Path Creation](#8.3.1-path-creation)
		1. [Deleting a Path](#8.3.2-deleting-a-path)
1. [The Carrier Layer](#9-the-carrier-layer)
	1. [Access Provider](#9.1-access-provider)
		1. [Portability](#9.1.1-portability)
	1. [Carrier](#9.2-carrier)
	1. [Carrier Protocol](#9.2.1-carrier-protocol)
	1. [Carrier API](#9.2.2-carrier-api)
	1. [Carrier Implementation](#9.2.3-carrier-implementation)
	1. [Carrier Node](#9.3-carrier-node)
1. [Definitions](#10-definitions)

# 1 Introduction
Qiy, or rather: the <a href="Qiy Scheme">Qiy Scheme</a>, puts people back in control of their <a href="Personal Data">Personal Data</a> while creating value for organizations that process it (<a href="Relying Party">Relying Parties</a>).


## 1.1 Purpose

The document is aimed at people who know that Qiy puts people back in control of their <a href="Personal Data">Personal Data</a>, but who want or need to know the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.

## 1.2 Reader guidance

* Privacy officers are advised to read chapter [3 Architectural Description](#3 Architectural Description) and especially [section 3.2](#3.2 Privacy).
* Security officers are advised to read chapter [3 Architectural Description](#3 Architectural Description) and especially [section 3.3](#3.3 Privacy).
* Information analysts are advised to read chapters [3 Architectural Description](#3 Architectural Description), [4 The User Layer] and [5 The Application Layer].
* Application developers are advised to read chapters [3 Architectural Description](#3 Architectural Description), [4 The User Layer], [5 The Application Layer] and [6 The Qiy Node Layer].
* Systems engineers are advised to read chapters [3 Architectural Description], [8 The Transport Layer] and [9 The Carrier Layer].

# 2 Overview

This chapter gives an overview of this document.
* [2.1 Data Reuse](#2.1 Data Reuse) describes how data can be reused with Qiy.
* [3 Architectural Description](#3 Architectural Description) describes the [Architectural Layers](#2.2 Architectural Layers) and addresses various concerns like privacy and security.
* [4 The User Layer](#4 The User Layer) describes the setup and processes of the data reuse at the user level.
* [5 The Application Layer](#5 The Application Layer) describes the processes at the application level.
* [6 The Qiy Node Layer](#6 The Qiy Node Layer) describes the same at the Qiy Node level.
* [7 The Service Layer](#7 The Service Layer) describes the <a href="Service Layer">Service Layer</a> support.
* [8 The Transport Layer](#8 The Transpor Layer) describes the <a href="Transport Layer">Transport Layer</a> support.
* [9 The Carrier Layer](#9 The Carrier Layer) describes the <a href="Carrier Layer">Carrier Layer</a> support.
* [10 Definitions](#10 Definitions) contains the definitions used in this document.
* [11 Diagram sources](#11 Diagram Sources) contains the source code used to generate the diagrams.

## 2.1 Data Reuse

This document describes how Qiy realizes a <a id="data-reuse">Data Reuse</a> scenario in which a <a href="Data Subject">Data Subject</a> (<a href="Individual">Individual</a>) reuses his <a href="Personal Data">Personal Data</a> stored at one organization (<a href="Data Provider">Data Provider</a>) and provide it to another organization (<a href="Relying Party">Relying Party</a>) to consume one of its services.

In essence, the <a href="Data Reuse">Data Reuse</a> goes as follows:
* The <a href="Individual">Individual</a> subscribes to a service.
* The <a href="Relying Party">Relying Party</a> asks the <a href="Individual">Individual</a> for the data it needs to provide the service.
* The <a href="Individual">Individual</a> retrieves the data from a <a href="Data Provider">Data Provider</a>.
* The <a href="Individual">Individual</a> provides the data to the <a href="Relying Party">Relying Party</a>.

![Qiy Data Reuse](./images/Qiy Data Reuse.png)

### 2.1.1 Privacy concern

The <a href="Data Reuse">Data Reuse</a> scenario shows that the data is transferred to the <a href="Relying Party">Relying Party</a> by choice of the <a href="Individual">Individual</a>.
This breaks the chain of responsibility for the <a href="Data Provider">Data Provider</a>; the responsibility for correct processing of the data does not extend to any processing that takes place after the handover to the <a href="Individual">Individual</a>. 

# 3 Architectural Description

This chapter describes the major entities of Qiy and their relations with the help of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a> and addresses how Qiy addresses concerns like security and privacy.

## 3.1 Architectural Layers
The realization of the scenario is described using the following layers:

![Layers](./images/layers.png)

## 3.2 Privacy

Qiy has been conceived with the aim to put people back in control of their <a href="Personal Data">Personal Data</a>, hence making privacy the primary concern of Qiy.
The aim has been elaborated in a set of principles called the <a href="Qiy Trust Principle">Qiy Trust Principles</a> and technical, legal and governance rules, all of which are maintained by the <a href="Qiy Foundation">Qiy Foundation</a> and the <a href="Qiy Foundation Member">Qiy Foundation Members</a>.

The realization of the <a href="Data Reuse">Data Reuse</a> as described in this document demonstrates that a natural person (<a href="Individual">Individual</a>) is in control:
* The <a href="Individual">Individual</a> can securily exchange data and/or messages with another person or organization (<a href="Qiy User">Qiy User</a>) via Qiy, using connections, see [4 The User Layer](#4 The User Layer).
* The <a href="Individual">Individual</a> controls what <a href="Qiy User">Qiy Users</a> he connects with and, in principle, when he wants to end it.
* When an <a href="Individual">Individual</a> connects with a <a href="Qiy User">Qiy User</a> that is providing a <a href="Service">Service</a> via Qiy (<a href="Provider">Provider</a>), the <a href="Individual">Individual</a> is provided with the identity of the latter, but not the other way around.
* The <a href="Individual">Individual</a> can access his <a href="Personal Data">Personal Data</a> that is kept by another [Qiy User](<a href="Data Provider">Data Provider</a> as a result of the <a href="Access Principle">Access Principle</a>, one of the <a href="Qiy Trust Principle">Qiy Trust Principles</a>.
* The <a href="Individual">Individual</a> controls what data he shares with what service provider (<a href="Relying Party">Relying Party</a>) and under what terms using proveable <a href="Consent">Consents</a>.
* <a href="Qiy User">Qiy Users</a> use applications that are authorized for use with Qiy (<a href="Qiy Application">Qiy Applications</a>).
* Access to Qiy, data exchange via Qiy, consent services and potentially <a href="Qiy Node">Qiy Nodes</a> are provided by <a href="Access Provider">Access Providers</a>.


All parties involved are bound by the rules of the <a href="Qiy Scheme">Qiy Scheme</a>:
* <a href="Provider">Providers</a> are bound by the <a href="Binding Individual Right">Binding Individual Rights</a> and the <a href="Binding Principles for Relying Parties and Data Provider">Binding Principles for Relying Parties and Data Providers</a>.
* <a href="Access Provider">Access Providers</a> are bound by the <a href="Licence Agreement Issuer">Licence Agreement Issuer</a> or the <a href="Licence Agreement Service Provider">Licence Agreement Service Provider</a>.
* <a href="Application Provider">Application Providers</a> can only develop and produce <a href="Qiy Application">Qiy Application</a>-services and/or software with a <a href="Licence Agreement Application Provider">Licence Agreement Application Provider</a>.

## 3.3 Security

As described above, privacy is at the heart of Qiy and security being a 'conditio sine qua no' for this, it is also addressed by the rules of the <a href="Qiy Scheme">Qiy Scheme</a>.

## 3.4 Interoperability

An <a href="Individual">Individual</a> can only control his <a href="Personal Data">Personal Data</a>, when all concerned systems are interoperable.
This is achieved as follows:
* Applications exchange data and/or messages via Qiy using open standards of the <a href="Qiy Scheme">Qiy Scheme</a> (<a href="Qiy Open Standard">Qiy Open Standard</a>).
* Applications exchange described data using <a href="Data Description">Data Descriptions</a> which are available to all concerned parties.

## 3.5 Governance

The governance rules are laid down in the <a href="Governance Model for the Qiy Scheme">Governance Model for the Qiy Scheme</a>, one of the documents of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.

## 3.6 Compliancy

The compliancy rules for <a href="Provider">Providers</a> can be found in the <a href="Binding Principles for Relying Parties and Data Provider">Binding Principles for Relying Parties and Data Providers</a>, one of the documents of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.


# 4 The User Layer
This chapter describes the <a href="User Layer">User Layer</a> and the interaction between the <a href="Relying Party">Relying Party</a>, <a href="Individual">Individual</a>, <a href="Data Provider">Data Provider</a> and the lower layers for the <a href="Data Reuse">Data Reuse</a>.

## 4.1 Qiy Users
The organizations and/or persons using Qiy are called <a href="Qiy User">Qiy Users</a>. They can use Qiy in different <a href="role">roles</a>; they can use Qiy as a <a href="Relying Party">Relying Party</a>, <a href="Individual">Individual</a>, <a href="Data Provider">Data Provider</a> or a combination of these.
A business for example will generally use Qiy both as a <a href="Relying Party">Relying Party</a> (for offering <a href="Service">Services</a> using reliable <a href="Personal Data">Personal Data</a>) and as a <a href="Data Provider">Data Provider</a> (as a source of <a href="Personal Data">Personal Data</a>).
As for natural persons, most of these will use Qiy as an <a href="Individual">Individual</a> to control their <a href="Personal Data">Personal Data</a>.

## 4.2 Provider
A <a href="Qiy User">Qiy User</a> that provides one or more <a href="Service">Services</a> to <a href="Individual">Individuals</a> is said to be (or act in the <a href="Business Role">Business Role</a> of) '<a href="Provider">Providers</a>'.
Any <a href="Qiy User">Qiy User</a> acting in one or both of the roles <a href="Relying Party">Relying Party</a> or <a href="Data Provider">Data Provider</a> is implicitely acting in this role.

## 4.3 Qiy Node
A <a href="Qiy User">Qiy User</a> must have a <a href="Qiy Node">Qiy Node</a>. 
<a href="Provider">Providers</a> can acquire one from an <a href="Access Provider">Access Provider</a>.
<a href="Individual">Individuals</a> obtain a <a href="Qiy Node">Qiy Node</a> the first time they use a <a href="Qiy Application">Qiy Application</a>.
Alternatively, <a href="Qiy User">Qiy Users</a> may instantiate a <a href="Qiy Node">Qiy Node</a> themselves using a <a href="Qiy Node Implementation">Qiy Node Implementation</a> and register it with an <a href="Access Provider">Access Provider</a>.

## 4.4 Connect via Qiy

Two <a href="Qiy User">Qiy Users</a> can connect via Qiy by creating a connection between their <a href="Qiy Node">Qiy Nodes</a> (<a href="Connection">Connection</a>).
The <a href="Connection">Connection</a> can be initiated by either of the two <a href="Qiy User">Qiy Users</a>.
The <a href="Qiy User">Qiy User</a> initiating the <a href="Connection">Connection</a> is called the <a href="Proposer">Proposer</a>, the other one <a href="Accepter">Accepter</a>.
This goes as follows:
* The <a href="Proposer">Proposer</a> uses a <a href="Qiy Application">Qiy Application</a> to generate a token (see [4.7.1 Generate token]) and compose <a href="Connect Proposal">Connect Proposal</a>.
* The <a href="Proposer">Proposer</a> provides it out-of-band to the <a href="Accepter">Accepter</a>, for example by lettre, see [4.7.2 'Media'](#4.7.2 Media).
* The <a href="Accepter">Accepter</a> may read the proposal and use a <a href="Qiy Application">Qiy Application</a> to extract the <a href="Connect Token">Connect Token</a> and create a new <a href="Connection">Connection</a> with the <a href="Proposer">Proposer</a>.

As stated before, when a <a href="Connection">Connection</a> is established, the identity of the <a href="Qiy User">Qiy User</a> is provided to the other one if the Qiy User is a <a href="Provider">Provider</a>. 
This information may be used to reuse a formerly created <a href="Connection">Connection</a> and delete the new <a href="Connection">Connection</a>.

![Users Connect](./images/users-connect.png)

### 4.4.1 Generate token
A <a href="Proposer">Proposer</a> can create a token using a <a href="Qiy Application">Qiy Application</a> and the following details:
* Name: The name or pseudonym to use in the <a href="Connect Proposal">Connect Proposal</a>.
* Expiration: Whether the token expires and if so, on what date and time.
* Budget: The number of times that the token can be used to create a <a href="Connection">Connection</a>.

In most cases, the expiration and budget are set by the application.
The Expiration and the Budget can be changed afterwards, for example to re-activate an expired token.

![Generate token](./images/generate-token.png)

 
### 4.4.2 Media
<a href="Qiy User">Qiy Users</a> can use different media to connect as illustrated in this diagram:

![Media](./images/Connect.png)

 
#### 4.4.2.1 The web
<a href="Qiy User">Qiy Users</a> can connect by transfering a token as a query parameter in a website address:
 
![Connect using a token in a website address](./images/connect-using-a-token-in-a-website-address.png)

 
#### 4.4.2.2 Print
<a href="Qiy User">Qiy Users</a> can convert the token to a QR Code and use various 'Print'-media to connect:

![Present proposal containing a QR Code](./images/present-proposal-containing-a-qr-code.png)


The QR Code can be used as follows to create the <a href="Connection">Connection</a>:
 
![Connect using a QR Code](./images/connect-using-a-qr-code.png)
 

## 4.5 Setup

This section addresses the setup for the <a href="Data Reuse">Data Reuse</a>

### 4.5.1 Relying Party

In order to be able to offer his services via Qiy, a <a href="Relying Party">Relying Party</a> has met the following preconditions:
* The <a href="Relying Party">Relying Party</a> has acquired access to Qiy with the help of an Access Provider.
* The <a href="Access Provider">Access Provider</a> has verified and registered the identity of the <a href="Relying Party">Relying Party</a> for use in Qiy.
* The <a href="Service Library">Service Library</a> contains the <a href="Service Catalogue">Service Catalogue</a> of the <a href="Relying Party">Relying Party</a> defining the provided services.
* The <a href="Service Library">Service Library</a> contains <a href="Service Description">Service Descriptions</a> for all the provided services, which also includes the terms of use, especially with regard to Personal Data.

### 4.5.1 Data Provider

In order to be able to provide the <a href="Personal Data">Personal Data</a> via Qiy, a <a href="Data Provider">Data Provider</a> has met the following preconditions:
* The <a href="Data Provider">Data Provider</a> has acquired access to Qiy with the help of an Access Provider.
* The <a href="Access Provider">Access Provider</a> has verified and registered the identity of the <a href="Data Provider">Data Provider</a> for use in Qiy.
* A <a href="Service Endpoint">Service Endpoint</a> is available to access the data.
* The <a href="Service Library">Service Library</a> contains the <a href="Service Endpoint API">Service Endpoint API</a> which describes how the data can be obtained.
* The <a href="Service Library">Service Library</a> contains <a href="Data Description">Data Descriptions</a> for the available data.
* The <a href="Service Library">Service Library</a> contains the <a href="Service Catalogue">Service Catalogue</a> of the <a href="Data Provider">Data Provider</a> defining the provided data services and the related endpoints.
* The <a href="Service Library">Service Library</a> contains <a href="Service Description">Service Descriptions</a> for the provided data services.

### 4.5.2 Individual

In order to be able to reuse <a href="Personal Data">Personal Data</a> via Qiy, an <a href="Individual">Individual</a> has met the following preconditions:
* The <a href="Individual">Individual</a> has access to his <a href="Personal Data">Personal Data</a> stored by one or more <a href="Data Provider">Data Providers</a>.
* The <a href="Individual">Individual</a> has access to a personal <a href="Qiy Node">Qiy Node</a>.
* The <a href="Individual">Individual</a> is using a <a href="Qiy Application">Qiy Application</a> which is linked to his <a href="Qiy Node">Qiy Node</a>.

## 4.6 Subscribe

Data Reuse starts with an Individual subscribing to a service, but only after considering and accepting the terms of use, including those regarding the use of Personal Data.
When an <a href="Individual">Individual</a> subscribes to a service, the subscription is registered by the <a href="Qiy Application">Qiy Application</a>, so:
* The subscribed service is recorded using the <a href="Service Portfolio">Service Portfolio</a> of the <a href="Individual">Individual</a>.
* The record shows:
	* the start datetime of the subscription.
	* the <a href="Provider">Provider</a> of the service (the <a href="Relying Party">Relying Party</a>).
	* what service is provided (using the <a href="Service Library">Service Library</a>.
	* the related <a href="Consent">Consent</a>.

## 4.7 Consent

When a request for data is received, it is checked with the granted consents. If the request is not authorized by an active granted consent, this may be resolved by granting one, after which the data request is processed.
In other cases, the request will not be accepted and no data will be returned.

## 4.8 Routing

When all related conditions are met, a request for data from a <a href="Relying Party">Relying Party</a> is processed as follows:
* The <a href="Service Portfolio">Service Portfolio</a> of the <a href="Individual">Individual</a> is consulted to find the <a href="Data Provider">Data Provider</a> or <a href="Data Provider">Data Providers</a> and related <a href="Service Endpoint API">Service Endpoint API</a>.
* Using the API, requests are created and used to obtain the data from the <a href="Service Endpoint">Service Endpoints</a>.
* The received data is forwarded to the <a href="Relying Party">Relying Party</a>.

## 4.9 Source

When a <a href="Relying Party">Relying Party</a> has requested for data, the <a href="Service Portfolio">Service Portfolio</a> is used to look up the data source: the <a href="Provider">Provider</a> or <a href="Provider">Providers</a> that will provide the data (<a href="Service Source">Service Source</a>).
This can be the <a href="Individual">Individual</a> himself, for self-declared data, but it can also be one or more <a href="Data Provider">Data Providers</a>.
The source of the data may have been defined before at the time of subscription, but if that it is not the case, the <a href="Individual">Individual</a> will be asked to make a selection from a list of suitable <a href="Data Provider">Data Providers</a> (<a href="Servive Discovery">Servive Discovery</a>).
The list will be generated using the <a href="Service Catalogue">Service Catalogues</a> from the <a href="Service Library">Service Library</a>.
The <a href="Service Portfolio">Service Portfolio</a> will be updated with the outcome.

## 4.10 Session

A Service Endpoint will only process a request when issued over an active Session. This Session may be started earlier, for example when the Individual selects a Data Provider as a source, but a new Session will be started if need be.
More often then not, this may require input from the Individual.
The session credentials are persisted in the <a href="Service Catalogue">Service Catalogue</a> of the Individual.

# 5 The Application Layer
This chapter describes the <a href="Application Layer">Application Layer</a> and how it supports the processes of the <a href="Data Reuse">Data Reuse</a> scenario.

## 5.1 Qiy Application
A <a href="Qiy Application">Qiy Application</a> is an <a href="Application Service">Application Service</a> or software which is authorized for use with Qiy.
* A <a href="Qiy Application">Qiy Application</a> must comply with the requirements of the <a href="Qiy Scheme">Qiy Scheme</a>.
* A <a href="Qiy User">Qiy User</a> can only use Qiy with a <a href="Qiy Application">Qiy Application</a>.
* A <a href="Qiy User">Qiy User</a> can use one or more <a href="Qiy Application">Qiy Applications</a>.
* <a href="Qiy Application">Qiy Applications</a> can use a <a href="Qiy Node">Qiy Node</a> at the same time.

### 5.1.1 Application Provider
<a href="Qiy Application">Qiy Applications</a> can be provided by <a href="Application Provider">Application Providers</a>. An <a href="Application Provider">Application Provider</a> can only do so with a valid <a href="Qiy Licence Agreement Application Provider">Qiy Licence Agreement Application Provider</a>.

### 5.1.2 Qiy Application Protocol
The <a href="Qiy Application Protocol">Qiy Application Protocol</a> describes the interactions of the <a href="Qiy Application">Qiy Applications</a> with eachother and the underlying layers.
* The <a href="Qiy Application Protocol">Qiy Application Protocol</a> is an open standard and is part of the <a href="Qiy Open Standard">Qiy Open Standard</a>.

The <a href="Qiy Application Protocol">Qiy Application Protocol</a> describes among others how <a href="Qiy Application">Qiy Applications</a>:
* ... create a <a href="Qiy Node">Qiy Node</a> for a <a href="Qiy User">Qiy User</a>.
* ... can be linked to a <a href="Qiy Node">Qiy Node</a> of a <a href="Qiy User">Qiy User</a>.
* ... create <a href="Connection">Connections</a>.
* ... create a 'backup' of a <a href="Qiy Node">Qiy Node</a>.
* ... exchange <a href="Connection Token">Connection Tokens</a> out-of-band.
* ... exchange messages.
* ... exchange <a href="Personal Data">Personal Data</a>.

### 5.1.3 Creating Qiy Nodes for Individuals

A <a href="Qiy Application">Qiy Application</a> can create a <a href="Qiy Node">Qiy Node</a> for a <a href="Qiy User">Qiy User</a>, especially when he does not have one yet.
The <a href="Qiy Application">Qiy Application</a> can do so with the help of an <a href="Access Provider">Access Provider</a>, but first it has to generate the credentials for the <a href="Qiy Node">Qiy Node</a> (<a href="Qiy Node Credential">Qiy Node Credentials</a>):
* A key pair, consisting of public key and a private key, 
* A <a href="Node Id">Node Id</a>

The <a href="Qiy Application">Qiy Application</a> must persists these in order to be able to keep using the <a href="Qiy Node">Qiy Node</a>.

#### 5.1.3.1 Security consideration
Some security considerations related to the <a href="Qiy Node Credential">Qiy Node Credentials</a> are:
* The <a href="Node Id">Node Id</a> must be a <a href="Uuid">Uuid</a> in order to assure that it is unique.
* The key pair must be unique.
* The private key must be persisted securily in order to guarantee the security of the <a href="Qiy User">Qiy User</a>. 
* The <a href="Node Id">Node Id</a> should be persisted securily in order to guarantee the security of the <a href="Qiy User">Qiy User</a>. 
* The <a href="Qiy Application">Qiy Applications</a> that can be used on consumer devices such as smart phones must provide a way to backup and recover the <a href="Qiy Node Credential">Qiy Node Credentials</a> in order to overcome cases of loss of the device.
* A <a href="Qiy User">Qiy User</a> must be able to control the devices that can access his <a href="Qiy Node">Qiy Node</a>, for example in order to be able to block access of a (possibly) stolen device.


### 5.1.4 Link with an existing Qiy Node
A <a href="Qiy Application">Qiy Application</a> can be linked to an existing <a href="Qiy Node">Qiy Node</a> by providing it with its <a href="Qiy Node Credential">Qiy Node Credentials</a>.

## 5.2 Connect

### 5.2.1 Application Connect Token
<a href="Qiy Application">Qiy Applications</a> exchange <a href="Application Connect Token">Application Connect Tokens</a> to create <a href="Connection">Connections</a>. 
In addition to the <a href="Connect Token">Connect Token</a> that is necessary to create the <a href="Connection">Connection</a>, it contains the name or pseudonym to be displayed in the <a href="Connect Proposal">Connect Proposal</a>. 
For more information, please refer to [5.2.3 'Generate Application Connect Token'](#5.2.3 Generate Application Connect Token).

### 5.2.2 Proposer: Connect
For a <a href="Qiy Application">Qiy Application</a> of a <a href="Proposer">Proposer</a>, a Connection is established as follows:
* The <a href="Qiy Application">Qiy Application</a> generates an <a href="Application Conenct Token">Application Conenct Token</a>, see [5.2.3 'Generate Application Connect Token'](#5.2.3 Generate Application Connect Token).
* The <a href="Qiy Application">Qiy Application</a> composes a <a href="Connect Proposal">Connect Proposal</a> for the <a href="Proposer">Proposer</a>.
* The <a href="Proposer">Proposer</a> presents it out-of-band to the <a href="Accepter">Accepter</a>.
* When the <a href="Accepter">Accepter</a> wants to connect, he uses the <a href="Connect Proposal">Connect Proposal</a> to create a connection with his <a href="Qiy Application">Qiy Application</a>, see [5.2.4 'Accepter: Connect'](#5.2.4 Accepter: Connect).
* The <a href="Proposer">Proposer</a> detects this by use of polling (using the <a href="Connections Request">Connections Request</a>) or events (using the <a href="Connection Created Event">Connection Created Event</a>).
 
![Proposer: Connect](./images/proposer--connect.png)

### 5.2.3 Generate Application Connect Token
The main part of an <a href="Application Connect Token">Application Connect Token</a> is the <a href="Connect Token">Connect Token</a>. The <a href="Qiy Application">Qiy Application</a> can create this both online and offline:
* Offline by creating a <a href="Connect Token">Connect Token</a> and registering it later using a <a href="Connect Token Registration Request">Connect Token Registration Request</a>.
* Online using a <a href="Connect Token Creation Request">Connect Token Creation Request</a>.

![Generate Application Connect Token](./images/generate-application-connect-token.png)

### 5.2.4 Accepter: Connect
At the <a href="Accepter">Accepter</a>-side, a <a href="Qiy Application">Qiy Application</a> creates a <a href="Connection">Connection</a> with a <a href="Connect Proposal">Connect Proposal</a> or <a href="Connect Token">Connect Token</a> as follows:
* In case of a <a href="Connect Proposal">Connect Proposal</a>, the <a href="Qiy Application">Qiy Application</a> extracts the <a href="Connect Token">Connect Token</a> from the <a href="Connect Proposal">Connect Proposal</a>.
* The <a href="Qiy Application">Qiy Application</a> uses the <a href="Connect Token">Connect Token</a> in <a href="Connection Create Request">Connection Create Request</a> to the <a href="Qiy Node">Qiy Node</a> of the <a href="Qiy User">Qiy User</a>.
* The <a href="Qiy Node">Qiy Node</a> creates the <a href="Connection">Connection</a> and returns the id of the <a href="Connection">Connection</a> (<a href="Connection Uri">Connection Uri</a>).

![Accepter: Connect](./images/accepter--connect.png)

## 5.3 Consent

### 5.3.1 Relying Party: Request consent

A <a href="Qiy Application">Qiy Application</a> of a <a href="Relying Party">Relying Party</a> can request an <a href="Individual">Individual</a> for <a href="Consent">Consent</a> as follows:
* The <a href="Qiy Application">Qiy Application</a> sends a <a href="Consent Request Message">Consent Request Message</a> over the <a href="Connection">Connection</a> with the <a href="Individual">Individual</a>.
* The <a href="Qiy Application">Qiy Application</a> receives a message with the outcome, either a <a href="Consent Granted Message">Consent Granted Message</a> or a <a href="Consent Denied Message">Consent Denied Message</a>.

![Relying Party: Request consent](./images/relying-party--request-consent.png)

### 5.3.2 Individual: Consider consent request
A <a href="Qiy Application">Qiy Application</a> of an <a href="Individual">Individual</a> processes a <a href="Consent Request">Consent Request</a> as follows:
* The <a href="Qiy Application">Qiy Application</a> detects receiving a <a href="Consent Request Message">Consent Request Message</a> by polling (using the <a href="Messages Request">Messages Request</a>) or with events (using the <a href="Message Received Event">Message Received Event</a>).
* The <a href="Qiy Application">Qiy Application</a> extracts the <a href="Consent Request">Consent Request</a> and presents it to the <a href="Individual">Individual</a>.
* Depending on the choice of the <a href="Individual">Individual</a>, the <a href="Qiy Application">Qiy Application</a> returns a <a href="Consent Granted Message">Consent Granted Message</a> or a <a href="Consent Denied Message">Consent Denied Message</a> using the <a href="Connection">Connection</a> with the <a href="Relying Party">Relying Party</a>.

![Individual--consider-consent-request](./images/individual--consider-consent-request.png)

## 5.4 Service Discovery
A <a href="Qiy Application">Qiy Application</a> can present an <a href="Individual">Individual</a> a list of suitable <a href="Data Provider">Data Providers</a> (or in general <a href="Provider">Providers</a>) that can produce some requested data (or services) as follows:
* The <a href="Qiy Application">Qiy Application</a> asks the <a href="Qiy Node">Qiy Node</a> of the <a href="Individual">Individual</a> for a list of suitable <a href="Data Provider">Data Providers</a> with a <a href="Source Candidates Request">Source Candidates Request</a>.
* The <a href="Qiy Node">Qiy Node</a> consults the <a href="Service Library">Service Library</a> and returns the outcome to the <a href="Qiy Application">Qiy Application</a>.
* The <a href="Qiy Application">Qiy Application</a> presents the result to the <a href="Individual">Individual</a>.
* The <a href="Qiy Application">Qiy Application</a> registers the selected sources with a <a href="Source Registration Request">Source Registration Request</a>.

## 5.5 Data by Reference
<a href="Qiy Application">Qiy Applications</a> exchange <a href="data by reference">data by reference</a> rather then by value.
This goes as follows:
* A <a href="Qiy Application">Qiy Application</a> requests a reference for the data (<a href="Data Reference">Data Reference</a>).
* The <a href="Qiy Application">Qiy Application</a> receives a <a href="Data Reference">Data Reference</a>.
* The <a href="Qiy Application">Qiy Application</a> uses the <a href="Data Reference">Data Reference</a> to acquire the data.

### 5.5.1 Service by Reference
In Qiy providing data is viewed as a service and requesting data as an operation of this service, so the 'data by reference'-pattern is implemented as using a <a id="service-by-reference">Service by Reference</a>-pattern:
* A <a href="Qiy Application">Qiy Application</a> requests an <a href="Operation Reference">Operation Reference</a> (<a href="Operation Reference Request">Operation Reference Request</a>).
* A <a href="Operation Reference">Operation Reference</a> is created by registrating the specification of the operation <a href="Operation Specification">Operation Specification</a> and returned (<a href="Operation Registration">Operation Registration</a>).
* The <a href="Qiy Application">Qiy Application</a> uses the <a href="Data Reference">Data Reference</a> to acquire the data (<a href="Operation Execution">Operation Execution</a>).

### 5.5.1 Request data reference
The <a href="Qiy Application">Qiy Application</a> of a <a href="Relying Party">Relying Party</a> can request an <a href="Individual">Individual</a> for a data reference as follows:
* The <a href="Qiy Application">Qiy Application</a> sends a <a href="Operation Reference Request Message">Operation Reference Request Message</a> using the <a href="Connection">Connection</a> of the <a href="Individual">Individual</a>.
* The <a href="Qiy Application">Qiy Application</a> receives the <a href="Operation Reference">Operation Reference</a> in an <a href="Operation Reference Message">Operation Reference Message</a>.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.4.2 Create reference
A <a href="Qiy Application">Qiy Application</a> can create an <a href="Operation Reference">Operation Reference</a> using a specification of the operation (<a href="Operation Specification">Operation Specification</a>).
This goes as follows:
* The <a href="Qiy Application">Qiy Application</a> uses the <a href="Operation Specification">Operation Specification</a> in an <a href="Operation Registration Request">Operation Registration Request</a> to the <a href="Qiy Node">Qiy Node</a> it is linked with.
* The <a href="Qiy Node">Qiy Node</a> creates the <a href="Operation Reference">Operation Reference</a> and returns it.

### 5.5.1 Request data
The <a href="Qiy Application">Qiy Application</a> of a <a href="Relying Party">Relying Party</a> can obtain data using a <a href="Data Reference">Data Reference</a> / <a href="Operation Reference">Operation Reference</a>. 
This goes as follows:
* The <a href="Qiy Application">Qiy Application</a> uses the <a href="Operation Reference">Operation Reference</a> in a <a href="Operation Execution Request">Operation Execution Request</a> to its <a href="Qiy Node">Qiy Node</a>.
* The <a href="Qiy Node">Qiy Node</a> returns the requested data.

![Relying Party: Request data](./images/relying-party--request-data.png)

### 5.5.2 Provide data
The <a href="Data Provider">Data Provider</a> produces the data using his <a href="Service Endpoint">Service Endpoint</a>.
This does not involve any of the <a href="Qiy Application">Qiy Applications</a> of the <a href="Data Provider">Data Provider</a> nor his <a href="Qiy Node">Qiy Node</a>.

![Data Provider: Provide data](./images/data-provider--provide-data.png)

# 6 The Qiy Node Layer
This chapter describes the <a href="Qiy Node Layer">Qiy Node Layer</a> and how it supports the upper layers.

## 6.1 Access Provider
The services of this layer can be provided by an <a href="Access Provider">Access Provider</a>:
* An <a href="Access Provider">Access Provider</a> can provide <a href="Qiy Node">Qiy Nodes</a>.
* An <a href="Access Provider">Access Provider</a> can host <a href="Qiy Node">Qiy Nodes</a>.

### 6.1.1 Portability
An <a href="Access Provider">Access Provider</a> can offer <a href="Qiy Node">Qiy Node</a>-services to <a href="Qiy User">Qiy Users</a>, but must enable <a href="Qiy User">Qiy Users</a> to easily transfer the services to a different <a href="Access Provider">Access Provider</a>.

## 6.2 Qiy Node
A <a href="Qiy Node">Qiy Node</a> is een <a href="Technology Service">Technology Service</a> as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
A <a href="Qiy Node">Qiy Node</a>:
* ... must comply with the rules of the <a href="Qiy Scheme">Qiy Scheme</a>.
* ... can be hosted on any host (<a href="Node">Node</a>).
* ... has its own <a href="Transporter">Transporter</a> which ensures secure transport of messages and/or data via Qiy.

### 6.2.1 Qiy Node Protocol
The <a href="Qiy Node Protocol">Qiy Node Protocol</a> describes the interaction between the <a href="Qiy Node">Qiy Nodes</a> and the underlying layers.
* The <a href="Qiy Node Protocol">Qiy Node Protocol</a> is one of the protocols in the <a href="Qiy Open Standard">Qiy Open Standard</a>.
The <a href="Qiy Node Protocol">Qiy Node Protocol</a> describes for example:
* How a <a href="Qiy Node">Qiy Node</a> is instantiated.
* How <a href="Qiy Node">Qiy Nodes</a> create <a href="Connection">Connections</a> and use them to exchange data, messages or to provide/consume services.

### 6.2.2 Qiy Node API
The <a href="Qiy Node API">Qiy Node API</a> is the <a href="Technology Interface">Technology Interface</a> of the <a href="Qiy Node">Qiy Node</a>, one of the APIs of the <a href="Qiy Open Standard">Qiy Open Standard</a>.
* The <a href="Qiy Node API">Qiy Node API</a> is intended for use by <a href="Qiy Application">Qiy Applications</a>.

### 6.2.3 Qiy Node Implementation
A <a href="Qiy Node Implementation">Qiy Node Implementation</a> is a software package which can be used to realize a <a href="Qiy Node">Qiy Node</a>.
The <a href="Qiy Scheme">Qiy Scheme</a> puts no limit on the number of <a href="Qiy Node Implementation">Qiy Node Implementation</a>s, as long as the implementation complies with the <a href="Qiy Open Standard">Qiy Open Standard</a> and the rules of the <a href="Qiy Scheme">Qiy Scheme</a>. 

### 6.2.4 Qiy Node Instantiation
A <a href="Qiy Node">Qiy Node</a> can be created in two ways:
* It can be instantiated by an <a href="Access Provider">Access Provider</a>. The <a href="Access Provider">Access Provider</a> will instantiate it with its own <a href="Transporter">Transporter</a>. 
* It can be instantiated by a <a href="Qiy User">Qiy User</a> on a <a href="Node">Node</a> of his own using a <a href="Qiy Node Implementation">Qiy Node Implementation</a>. 
When the second option is chosen, the <a href="Qiy User">Qiy User</a> is responsible for obtaining a <a href="Transporter">Transporter</a> and linking it to the <a href="Qiy Node">Qiy Node</a>.

### 6.2.5 Deleting a Qiy Node
In principle, a <a href="Qiy Node">Qiy Node</a> can be deleted by its owner whenever he wants to do so.
In this case, the <a href="Qiy Node">Qiy Node</a> will be deleted including persisted data, <a href="Connection">Connections</a> and the linked <a href="Transporter">Transporter</a>.
Related <a href="Consent">Consents</a> will be withdrawn.

## 6.3 Connect
Two <a href="Qiy Node">Qiy Nodes</a> can connect by creating a <a href="Path">Path</a> between themselves.
* A <a href="Qiy Node">Qiy Node</a> can connect with zero or more other <a href="Qiy Node">Qiy Nodes</a>.
* A <a href="Qiy Node">Qiy Node</a> can have zero or more <a href="Path">Paths</a> with any other <a href="Qiy Node">Qiy Node</a>.
* A priori, a <a href="Qiy Node">Qiy Node</a> does not know the identity of the <a href="Qiy Node">Qiy Node</a> at the other side of a <a href="Path">Path</a>.

### 6.3.1 Connection Uri
The <a href="Connection Uri">Connection Uri</a> is the <a href="Uri">Uri</a> which identifies a <a href="Connection">Connection</a> for one of the <a href="Qiy Node">Qiy Node</a> it connects.
* A <a href="Connection">Connection</a> has two <a href="Connection Uri">Connection Uris</a>; one for each of the two <a href="Qiy Node">Qiy Nodes</a> it connects.
* The two <a href="Connection Uri">Connection Uris</a> of one <a href="Connection">Connection</a> are not related to one another.
* A priori, a <a href="Qiy Node">Qiy Node</a> does not know the other <a href="Connection Uri">Connection Uri</a> of a <a href="Connection">Connection</a>.

EXAMPLE: <a href="Connection Uri">Connection Uris</a> of a <a href="Connection">Connection</a> between <a href="Qiy Node">Qiy Node</a> 1 and <a href="Qiy Node">Qiy Node</a> 2:

<a href="Qiy Node">Qiy Node</a> | <a href="Connection Uri">Connection Uri</a>
---- | --------------
Qiy Node 1	| http://127.0.0.1:8087/user/connections/user/usernodeB/93590b55-9194-4cf4-944f-2cbceab7dbcd
Qiy Node 2	| http://127.0.0.1:8087/user/connections/user/usernodeA/f96bc541-e98b-449e-bfc5-48ec928e0dc9

#### 6.3.1.1 Security concern
The <a href="Connection Uri">Connection Uri</a> has only meaning in the context of the <a href="Qiy Node">Qiy Node</a> that knows it and is useless outside this scope.
For example, the <a href="Uri">Uri</a> by itself can not be used to exchange a message with the <a href="Qiy Node">Qiy Node</a> nor any other existing <a href="Qiy Node">Qiy Node</a>.

### 6.3.2 Connect Token
A <a href="Connect Token">Connect Token</a> is a token which can be used by a <a href="Qiy Application">Qiy Application</a> to create a <a href="Connection">Connection</a>.
It consists of:
* a temporary secret
* a <a href="Transport Connect Token">Transport Connect Token</a>.

A <a href="Connect Token">Connect Token</a> has the following properties:
* An expiration setting: Whether the token expires and if so, on what date and time
* A budget: The number of times that the token can be used to create a Connection. 

The properties can not only be set when the token is registered or requested, but also later.
For example, it is possible to reactivate a <a href="Connect Token">Connect Token</a> by increasing the budget or inactivate one by changing the expiration.

#### 6.3.2.1 Security concern
The <a href="Connect Token">Connect Token</a> can only be used to create a <a href="Connection">Connection</a> and only so via Qiy, with the help of a <a href="Qiy Application">Qiy Application</a> and a linked <a href="Qiy Node">Qiy Node</a>.
By itself, it cannot be used for any other purpose, for example gain access to a <a href="Qiy Node">Qiy Node</a> nor any other parts of the Qiy infrastructuur.

#### 6.3.2.2 Creating a Connect Token
A <a href="Connect Token">Connect Token</a> can be created both offline and online:
* A <a href="Connect Token">Connect Token</a> can be obtained from the <a href="Qiy Node">Qiy Node</a> using a <a href="Connect Token Creation Request">Connect Token Creation Request</a> (<a href="Online Connect Token">Online Connect Token</a>).
* A <a href="Connect Token">Connect Token</a> can be created by a <a href="Qiy Application">Qiy Application</a> and registered later using a <a href="Connect Token Registration Request">Connect Token Registration Request</a> (<a href="Offline Connect Token">Offline Connect Token</a>).

The <a href="Offline Connect Token">Offline Connect Token</a> allows initiating a <a href="Connection">Connection</a> (creating a <a href="Connect Token">Connect Token</a>) even when Qiy is temporarily not available.
However, care must be taken that the created token is unique, especially so for the created <a href="Transport Connect Token">Transport Connect Token</a>.

#### 6.3.2.3 Creating a Transport Connect Token
A <a href="Qiy Node">Qiy Node</a> will never create a <a href="Transport Connect Token">Transport Connect Token</a>:
* In case of an <a href="Online Connect Token">Online Connect Token</a>: The <a href="Qiy Node">Qiy Node</a> will obtain a <a href="Transport Connect Token">Transport Connect Token</a> from its <a href="Transporter">Transporter</a>.
* In case of an <a href="Offline Connect Token">Offline Connect Token</a>: The <a href="Qiy Node">Qiy Node</a> will compose a <a href="Transport Connect Token">Transport Connect Token</a> using the <a href="Connect Token">Connect Token</a> provided by the <a href="Qiy Application">Qiy Application</a> and register it at its <a href="Transporter">Transporter</a>.

### 6.3.3 Connecting
Two <a href="Qiy Node">Qiy Nodes</a> connect as follows:
* The <a href="Qiy Node">Qiy Node</a> of the <a href="Proposer">Proposer</a> either 1) obtains a <a href="Transport Connect Token">Transport Connect Token</a> from the <a href="Transporter">Transporter</a> or 2) from a linked <a href="Qiy Application">Qiy Application</a> in a <a href="Connection Create Request">Connection Create Request</a>.
* The <a href="Qiy Node">Qiy Node</a> either 1) provides the <a href="Transport Connect Token">Transport Connect Token</a> to the <a href="Qiy Application">Qiy Application</a> or 2) registers the <a href="Transport Connect Token">Transport Connect Token</a> at its <a href="Transporter">Transporter</a>.
* The <a href="Transport Connect Token">Transport Connect Token</a> is made available (partly out-of-bands, for example in a <a href="Connect Proposal">Connect Proposal</a>) to the <a href="Qiy Node">Qiy Node</a> of the <a href="Accepter">Accepter</a>.
* The <a href="Qiy Node">Qiy Node</a> of the <a href="Accepter">Accepter</a> uses its <a href="Transporter">Transporter</a> to create a <a href="Path">Path</a> using the <a href="Transport Connect Token">Transport Connect Token</a>.
Each accepted <a href="Path Creation Request">Path Creation Request</a> leads to a new <a href="Path">Path</a>, irrespective of the number of existing <a href="Path">Paths</a> between the two <a href="Qiy Node">Qiy Nodes</a>.

### 6.3.4 Deleting a Connection
A <a href="Connection">Connection</a> can be deleted with a <a href="Connection Delete Request">Connection Delete Request</a>.
The <a href="Connection">Connection</a> will be deleted completely, including any persisted data and/or messages and underlying <a href="Path">Paths</a>.
Any related <a href="Consent">Consents</a> will be withdrawn.

## 6.4 Consent
A <a href="Consent">Consent</a> is a permission given by an <a href="Individual">Individual</a> to a <a href="Relying Party">Relying Party</a> defining what <a href="Personal Data">Personal Data</a> a <a href="Relying Party">Relying Party</a> is allowed to use for a provided <a href="Service">Service</a> and under what the terms.
A <a href="Consent">Consent</a> has the following properties:
* a <a href="Consent Uri">Consent Uri</a>
* a <a href="Consent Service Descriptor">Consent Service Descriptor</a>
* a <a href="Consent Data Descriptor">Consent Data Descriptor</a>

### 6.4.1 Consent Uri
The <a href="Consent Uri">Consent Uri</a> is an <a href="Uri">Uri</a> used to identify a <a href="Consent">Consent</a>.

### 6.4.2 Consent Service Descriptor
The <a href="Consent Service Descriptor">Consent Service Descriptor</a> is a <a href="Service Descriptor">Service Descriptor</a> which indicates the <a href="Service">Service</a> that the <a href="Consent">Consent</a> applies to.
A <a href="Service Descriptor">Service Descriptor</a> can be used to obtain a description of a <a href="Service">Service</a> (<a href="Service Description">Service Description</a>) with the help of the <a href="Service Library">Service Library</a>.

### 6.4.3 Consent Data Descriptor
The <a href="Consent Data Descriptor">Consent Data Descriptor</a> is a <a href="Data Descriptor">Data Descriptor</a> which indicates the <a href="Personal Data">Personal Data</a> that the <a href="Consent">Consent</a> applies to.
A <a href="Data Descriptor">Data Descriptor</a> can be used to obtain a description of <a href="Data">Data</a> (<a href="Data Description">Data Description</a>) with the help of the <a href="Service Library">Service Library</a>.

#### 6.4.3.1 Privacy concern
A <a href="Relying Party">Relying Party</a> can only ask <a href="Consent">Consent</a> for <a href="Personal Data">Personal Data</a> that can be provided by one of the available <a href="Data Provider">Data Providers</a>, eg for which a <a href="Data Descriptor">Data Descriptor</a> exists in the <a href="Service Library">Service Library</a>.
  
## 6.5 Qiy Node Request
A <a id="qiy-node-request">Qiy Node Request</a> is a <a href="Http Request">Http Request</a> for a <a href="Qiy Node">Qiy Node</a>. 
<a href="Qiy Node Request">Qiy Node Requests</a> are only accepted when they are correctly authenticated with:
* the <a id="node-id">Node Id</a>.
* an actual timestamp
* a digital signature over the <a href="Node Id">Node Id</a>, the timestamp and the contents of the body of the request made with the private key

## 6.6 Qiy Node Requests
This section gives an overview of the <a href="Qiy Node Request">Qiy Node Requests</a>.
Details of <a href="Qiy Node Request">Qiy Node Requests</a> can be found in the <a href="Qiy Node API">Qiy Node API</a>.

### 6.6.1 Connect Token Creation Request
<a id="connect-token-creation-request">Connect Token Creation Request</a>
Met dit request kan een <a href="Connect Token">Connect Token</a> worden gecre&euml;erd door the <a href="Qiy Node">Qiy Node</a>.

### 6.6.2 Connect Token Registration Request
<a id="connect-token-registration-request">Connect Token Registration Request</a>
Met dit request kan een <a href="Connect Token">Connect Token</a> worden geregistreerd.

### 6.6.3 Connect Token Update Request
The <a id="connect-token-update-request">Connect Token Update Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to update a <a href="Connect Token">Connect Token</a>.

### 6.6.4 Connection Create Request
The <a id="connection-create-request">Connection Create Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to create a <a href="Connection">Connection</a> with a <a href="Connect Token">Connect Token</a>.

### 6.6.5 Connection Delete Request
The <a id="connection-delete-request">Connection Delete Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to delete a <a href="Connection">Connection</a>.

### 6.6.6 Connections Request
The <a id="connections-request">Connections Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to obtain a list of all the <a href="Connection">Connections</a> of a <a href="Qiy Node">Qiy Node</a>.

### 6.6.7 Consent Denied Request
The <a id="consent-denied-request">Consent Denied Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to record the denial of a <a href="Consent">Consent</a>.

### 6.6.8 Consent Granted Request
The <a id="consent-granted-request">Consent Granted Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to record the granting of a <a href="Consent">Consent</a>.

### 6.6.9 Consent Request
The <a id="consent-request">Consent Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> which can be used to request for a <a href="Consent">Consent</a>.

### 6.6.10 Consent Withdrawn Request
The <a id="consent-withdrawn-request">Consent Withdrawn Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to record the withdrawal of a <a href="Consent">Consent</a>.

### 6.6.11 Consents Request
The <a id="consents-request">Consents Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to obtain a list of all the <a href="Consent">Consents</a> of a <a href="Qiy Node">Qiy Node</a>.

### 6.6.12 Message Post Request
The <a id="message-post-request">Message Post Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to post a <a href="Qiy Node Message">Qiy Node Message</a>.

### 6.6.13 Messages Request
The <a id="messages-request">Messages Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to obtain a list of all the <a href="Message">Messages</a> of a <a href="Qiy Node">Qiy Node</a>.

### 6.6.14 Operation Execution Request
The <a id="operation-execution-request">Operation Execution Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to command the execution of an <a href="Operation">Operation</a> by reference using an <a href="Operation Reference">Operation Reference</a>.

### 6.6.15 Operation Registration Request
The <a id="operation-registration-request">Operation Registration Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to obtain an <a href="Operation Reference">Operation Reference</a> by registrating an <a href="Operation Specification">Operation Specification</a>.

### 6.6.16 Operation References Request
The <a id="operation-references-request">Operation References Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> that can be used to obtain a list of all the <a href="Operation Reference">Operation References</a> of a <a href="Qiy Node">Qiy Node</a>.

### 6.6.17 Source Candidates Request
The <a id="source-candidates-request">Source Candidates Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> to obtain candidate <a href="Provider">Providers</a> for a <a href="Service">Service</a>.

### 6.6.18 Source Registration Request
The <a id="source-registration-request">Source Registration Request</a> is a <a href="Qiy Node Request">Qiy Node Request</a> to register a <a href="Provider">Provider</a> as source for a <a href="Service">Service</a>.
 
## 6.7 Qiy Node Message
A <a id="qiy-node-message">Qiy Node Message</a> is a <a href="Message">Message</a> that is exchanged using a <a href="Connection">Connection</a>.
<a href="Qiy Node Message">Qiy Node Messages</a> can be sent with the <a href="Message Post Request">Message Post Request</a>, obtained using a <a href="Messages Request">Messages Request</a> and monitored with <a href="Qiy Node Event">Qiy Node Events</a> like <a href="Message Received Event">Message Received Event</a>.

## 6.8 Qiy Node Messages
This section gives an overview of the <a href="Qiy Node Message">Qiy Node Messages</a>.
Details of <a href="Qiy Node Message">Qiy Node Messages</a> can be found in the <a href="Qiy Node Protocol">Qiy Node Protocol</a>.

### 6.8.1 Consent Denied Message
The <a id="consent-denied-message">Consent Denied Message</a> is a <a href="Qiy Node Message">Qiy Node Message</a> which can be used to communicate the denial of a <a href="Consent">Consent</a>.

### 6.8.2 Consent Granted Message
The <a id="consent-granted-message">Consent Granted Message</a> is a <a href="Qiy Node Message">Qiy Node Message</a> which can be used to communicate the granting of a <a href="Consent">Consent</a>.

### 6.8.3 Consent Request Message
The <a id="consent-request-message">Consent Request Message</a> is a <a href="Qiy Node Message">Qiy Node Message</a> which can be used to request for a <a href="Consent">Consent</a>.

### 6.8.4 Operation Reference Message
<a id="operation-reference-message">Operation Reference Message</a>
This message can be used to convey <a href="Operation Reference">Operation References</a>.
 
### 6.8.5 Operation Reference Request Message
<a id="operation-reference-request-message">Operation Reference Request Message</a>
This message can be used to request for <a href="Operation Reference">Operation References</a>.
 
## 6.9 Qiy Node Event
A <a id="qiy-node-event">Qiy Node Event</a> is a <a id="technology-event">Technology Event</a> of a <a href="Qiy Node">Qiy Node</a>.

## 6.10 Qiy Node Events
This section gives an overview of the <a href="Qiy Node Event">Qiy Node Events</a>.
Details of <a href="Qiy Node Event">Qiy Node Events</a> can be found in the <a href="Qiy Node Protocol">Qiy Node Protocol</a>.

### 6.10.1 Connection Created Event
The <a id="connection-created-event">Connection Created Event</a> is a <a href="Qiy Node Event">Qiy Node Event</a> that is generated when a <a href="Connection">Connection</a> has been created.

### 6.10.2 Consent Withdrawn Event
The <a id="consent-withdrawn-event">Consent Withdrawn Event</a> is a <a href="Qiy Node Event">Qiy Node Event</a> that is generated when a <a href="Consent">Consent</a> has been withdrawn.

### 6.10.3 Message Received Event
The <a id="message-received-event">Message Received Event</a> is a <a href="Qiy Node Event">Qiy Node Event</a> that is generated when a <a href="Qiy Node Message">Qiy Node Message</a> has been received.

### 6.10.4 Operation Reference Received Event
The <a id="operation-reference-received-event">Operation Reference Received Event</a> is a <a href="Qiy Node Event">Qiy Node Event</a> that is generated when a <a href="Qiy Node">Qiy Node</a> has received a new <a href="Operation Reference">Operation Reference</a>.

### 6.10.5 Source Candidate Event
The <a id="source-candidate-event">Source Candidate Event</a> is a <a href="Qiy Node Event">Qiy Node Event</a> that is generated when a <a href="Qiy Node">Qiy Node</a> has received a new <a href="Source Candidate">Source Candidate</a> for a <a href="Consent">Consent</a>.

# 7 The Service Layer
The <a href="Service Layer">Service Layer</a> provides the following <a href="Technology Service">Technology Services</a> to support the provisioning and consumption of <a href="Service">Services</a> via Qiy:
* <a href="Service Endpoint">Service Endpoints</a>
* <a href="Service Library">Service Library</a>
* <a href="Consent Service">Consent Service</a>

## 7.1 Access Provider
The <a href="Service Library">Service Library</a> and <a href="Consent Service">Consent Service</a> are both provided by an <a href="Access Provider">Access Provider</a>.

### 7.1.1 Portability
The <a href="Qiy Scheme">Qiy Scheme</a> prescribes that one can easily change to a different <a href="Access Provider">Access Provider</a> for these services.

## 7.2 Service
In general, a <a href="Service">Service</a> is an 'information society service' as defined in the <a href="GDPR">GDPR</a>, with the following enhancements:
* A <a href="Service">Service</a> can be consumed with the use of one or more <a href="Operation">Operations</a>.
* A <a href="Service">Service</a> is provided by a <a href="Provider">Provider</a>.
* A <a href="Provider">Provider</a> can offer one or more <a href="Service">Services</a>.
* One <a href="Service">Service</a> can be offered by one or more <a href="Provider">Providers</a>.
* The <a href="Service">Services</a> that a <a href="Provider">Provider</a> offers are described in a <a href="Service Catalogue">Service Catalogue</a>.
* The <a href="Service">Services</a> that an <a href="Individual">Individual</a> consumes are described in his <a href="Service Portfolio">Service Portfolio</a>.

As for Qiy, the following definitions apply:
* Both <a href="Relying Party">Relying Parties</a> and <a href="Data Provider">Data Providers</a> are <a href="Provider">Providers</a>.

## 7.3 Service Endpoints
A <a href="Service Endpoint">Service Endpoint</a> is a <a href="Technology Service">Technology Service</a> provided by a <a href="Provider">Provider</a> to allow the consumption of his <a href="Service">Services</a>:
* A <a href="Provider">Provider</a> can employ one or more <a href="Service Endpoint">Service Endpoints</a>.
* A <a href="Service Endpoint">Service Endpoint</a> can be used for one or more <a href="Service">Services</a>.
* A <a href="Service">Service</a> can be consumed with the use of one or more <a href="Service Endpoint">Service Endpoints</a>.

For example, a <a href="Service Endpoint">Service Endpoint</a> may be used by a <a href="Data Provider">Data Provider</a> to disclose the <a href="Personal Data">Personal Data</a> from one of his databases.

## 7.4 Service Library
The <a href="Service Library">Service Library</a> is used for:
* <a href="Data Description">Data Descriptions</a>
* <a href="Provider">Providers</a>
* <a href="Service Catalogue">Service Catalogues</a>
* <a href="Service Description">Service Descriptions</a>

## 7.5 Consent Service
A <a href="Consent Service">Consent Service</a> is used for maintaining <a href="Consent">Consents</a> and their status.
A <a href="Consent">Consent</a> can be accessed by both of the involved <a href="Qiy User">Qiy Users</a>: the <a href="Individual">Individual</a> and the <a href="Provider">Provider</a>.

* In principle, only an <a href="Individual">Individual</a> can withdraw a <a href="Consent">Consent</a> he has granted before.
* A <a href="Provider">Provider</a> can only obtain <a href="Personal Data">Personal Data</a> under a <a href="Consent">Consent</a> which has not been withdrawn.

# 8 The Transport Layer
The <a href="Transport Layer">Transport Layer</a> supports the secure transmission of messages (<a href="Transport Message">Transport Messages</a>) over <a href="Path">Paths</a> between <a href="Transporter">Transporters</a>.

## 8.1 Access Provider
The services of this layer are only provided by an <a href="Access Provider">Access Provider</a>.

### 8.1.1 Portability
The <a href="Qiy Scheme">Qiy Scheme</a> prescribes that one can easily switch <a href="Access Provider">Access Provider</a> for these services.

## 8.2 Transporter
A <a href="Transporter">Transporter</a> is a <a href="Technology Service">Technology Service</a> which allows the secure transmission of messages and/or data.
* A <a href="Transporter">Transporter</a> must comply with the rules of the <a href="Qiy Scheme">Qiy Scheme</a>.
* A <a href="Transporter">Transporter</a> is hosted on a <a href="Carrier Node">Carrier Node</a>.
* Each <a href="Qiy Node">Qiy Node</a> has its own <a href="Transporter">Transporter</a>.

A <a href="Transporter">Transporter</a> can be used for:
* Creating <a href="Path">Paths</a> with other <a href="Transporter">Transporters</a>.
* Securely transmitting <a href="Transport Message">Transport Messages</a> over these <a href="Path">Paths</a>.

## 8.2.1 Transport Protocol
The <a href="Transport Protocol">Transport Protocol</a> describes the interaction between <a href="Transporter">Transporters</a> and the underlying layer.
The protocol is one of the protocols of the <a href="Qiy Open Standard">Qiy Open Standard</a>.

## 8.2.2 Transporter API
The <a href="Transporter API">Transporter API</a> is the <a href="Technology Interface">Technology Interface</a> of the <a href="Transporter">Transporter</a>, one of the APIs of the <a href="Qiy Open Standard">Qiy Open Standard</a>.
* The <a href="Transporter API">Transporter API</a> is intended for use by <a href="Qiy Node">Qiy Nodes</a>.

## 8.2.3 Transporter Implementation
A <a href="Transporter Implementation">Transporter Implementation</a> is a software package which can be used to realize a <a href="Transporter">Transporter</a>.
The <a href="Qiy Scheme">Qiy Scheme</a> puts no limit on the number of <a href="Transporter Implementation">Transporter Implementation</a>s, as long as the implementation complies with the <a href="Qiy Open Standard">Qiy Open Standard</a> and the rules of the <a href="Qiy Scheme">Qiy Scheme</a>. 

## 8.2.4 Transporter Instantiation
A <a href="Transporter">Transporter</a> can only be instantiated by an <a href="Access Provider">Access Provider</a>.

## 8.2.5 Deleting a Transporter
A <a href="Transporter">Transporter</a> can be deleted by its <a href="Qiy Node">Qiy Node</a>.
In this case, the <a href="Transporter">Transporter</a> will be deleted including any persisted data and <a href="Route">Routes</a>.

## 8.3 Path
A <a href="Path">Path</a> is a logical connection between two <a href="Transporter">Transporters</a> that can be used to exchange <a href="Transport Message">Transport Messages</a>.
Physically seen, the <a href="Path">Path</a> may be dynamic and stretch over several <a href="Carrier">Carriers</a>.

### 8.3.1 Path Creation
A <a href="Path">Path</a> can be created by a <a href="Transporter">Transporter</a> with a <a href="Transport Connect Token">Transport Connect Token</a>.

### 8.3.2 Deleting a Path
A <a href="Path">Path</a> can be deleted by either of the ending <a href="Transporter">Transporters</a>. 
The <a href="Path">Path</a> will be deleted including any persisted data and/or messages.

# 9 The Carrier Layer
The <a href="Carrier Layer">Carrier Layer</a> supports the creation of <a href="Path">Paths</a> and the secure transport of messages over them.

## 9.1 Access Provider
The services of this layer are only provided by an <a href="Access Provider">Access Provider</a>.

### 9.1.1 Portability
The <a href="Qiy Scheme">Qiy Scheme</a> prescribes that one can easily switch <a href="Access Provider">Access Provider</a> for these services.

## 9.2 Carrier
The <a href="Carrier">Carrier</a> is <a href="Technology Service">Technology Service</a> which can be used for:
* To obtain a <a href="Transporter">Transporter</a>.
* To create <a href="Path">Paths</a>.
* To safely transport messages between <a href="Carrier">Carriers</a>.
* To obtain a <a href="Qiy Node">Qiy Node</a>.

The <a href="Carrier">Carrier</a> comes with the following rules:
* A <a href="Carrier">Carrier</a> must comply with the rules of the <a href="Qiy Scheme">Qiy Scheme</a>.
* A <a href="Carrier">Carrier</a> must support the <a href="Carrier API">Carrier API</a>.

## 9.2.1 Carrier Protocol
The <a href="Carrier Protocol">Carrier Protocol</a> describes the interaction between <a href="Carrier">Carriers</a>.
The protocol is part of the <a href="Qiy Open Standard">Qiy Open Standard</a>.

## 9.2.2 Carrier API
The <a href="Carrier API">Carrier API</a> is the <a href="Technology Interface">Technology Interface</a> of the <a href="Carrier">Carrier</a> and is part of the <a href="Qiy Open Standard">Qiy Open Standard</a>.

## 9.2.3 Carrier Implementation
A <a href="Carrier Implementation">Carrier Implementation</a> is a software package which can be used to realize a <a href="Carrier">Carrier</a>.
The <a href="Qiy Scheme">Qiy Scheme</a> puts no limit on the number of <a href="Carrier Implementation">Carrier Implementations</a>, as long as the implementation complies with the <a href="Qiy Open Standard">Qiy Open Standard</a> and the rules of the <a href="Qiy Scheme">Qiy Scheme</a>. 

## 9.3 Carrier Node
A <a href="Carrier Node">Carrier Node</a> is a <a href="Node">Node</a> which hosts one or more <a href="Carrier">Carriers</a>.
* The <a href="Carrier Node">Carrier Node</a> is provided by an <a href="Access Provider">Access Provider</a>.
* The <a href="Access Provider">Access Provider</a> can provide one or more <a href="Carrier Node">Carrier Nodes</a>.

# 10 Definitions
This document uses the following definitions:

Term	| Definition
------- | ----------
<a id="access-provider">Access Provider</a>	| An organization which provides <a href="Qiy User">Qiy Users</a> access to the <a href="Qiy Trust Framework">Qiy Trust Framework</a>, either an <a href="Issuer">Issuer</a> or a <a href="Service Provider">Service Provider</a>.
<a id="access-principle">Access Principle</a>	| The principle which authorizes the access of an <a href="Individual">Individual</a> to his <a href="Personal Data">Personal Data</a>, one of the <a href="Qiy Trust Principle">Qiy Trust Principles</a>.
<a id="accepter">Accepter</a>	| A <a href="Business Role">Business Role</a> for a <a href="Qiy User">Qiy User</a> who is creating a <a href="Connection">Connection</a> using a <a href="Connect Token">Connect Token</a> that is provided by a <a href="Proposer">Proposer</a>.
<a id="application-connect-token">Application Connect Token</a>	| A <a href="Token">Token</a> that is used by <a href="Qiy Application">Qiy Applications</a> to create <a href="Connection">Connections</a>.
<a id="application-interface">Application Interface</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="application-layer">Application Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="application-provider">Application Provider</a>	| A <a href="Bussiness Role">Bussiness Role</a> for suppliers of <a href="Qiy Application">Qiy Applications</a>.
<a id="application-service">Application Service</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="architectural-layers-of-the-qiy-scheme">Architectural Layers of the Qiy Scheme</a>	| The architectural layers of the <a href="Qiy Scheme">Qiy Scheme</a>: the <a href="User Layer">User Layer</a>, the <a href="Application Layer">Application Layer</a>, the <a href="Qiy Node Layer">Qiy Node Layer</a>, the <a href="Service Layer">Service Layer</a>, the <a href="Transport Layer">Transport Layer</a> and the <a href="Carrier Layer">Carrier Layer</a>.
<a id="binding-individual-rights">Binding Individual Rights</a>	| One of the documents of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.
<a id="binding-principles-for-relying-parties-and-data-providers">Binding Principles for Relying Parties and Data Providers</a>	| One of the documents of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.
<a id="business-actor">Business Actor</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-object">Business Object</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-process">Business Process</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="business-role">Business Role</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="carrier">Carrier</a>	| A <a href="Technology Service">Technology Service</a> that provides the services of the <a href="Carrier Layer">Carrier Layer</a>. 
<a id="carrier-api">Carrier API</a>	| <a href="Technology Interface">Technology Interface</a> of the <a href="Carrier">Carrier</a>.
<a id="carrier-implementation">Carrier Implementation</a>	| A software package which can be used to realize a <a href="Carrier">Carrier</a>.
<a id="carrier-layer">Carrier Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="carrier-node">Carrier Node</a>	| A <a href="Node">Node</a> which hosts one or more <a href="Carrier">Carriers</a>.
<a id="connect-proposal">Connect Proposal</a>	| A <a href="Business Object">Business Object</a> for a proposal to connect via Qiy.
<a id="connect-token">Connect Token</a>	| A Literal used to create a <a href="Connection">Connection</a>.
<a id="connection">Connection</a>	| A connection between two <a href="Qiy Node">Qiy Nodes</a>.
<a id="connection-uri">Connection Uri</a>	| <a href="Uri">Uri</a> voor the id van een <a href="Connection">Connection</a>.
<a id="consent">Consent</a>	| As defined in the <a href="GDPR">GDPR</a>.
<a id="consent-data-descriptor">Consent Data Descriptor</a>	| <a href="Data Descriptor">Data Descriptor</a> in een <a href="Service Description">Service Description</a> voor the beschrijving van the voor the <a href="Service">Service</a> benodigde <a href="Personal Data">Personal Data</a>.
<a id="consent-service">Consent Service</a>	| A <a href="Technology Service">Technology Service</a> used to maintain <a href="Consent">Consents</a> and their status.
<a id="consent-service-description">Consent Service Description</a>	| A <a href="Service Description">Service Description</a> of the <a href="Service">Service</a> for which a <a href="Consent">Consent</a> applies.
<a id="consent-service-descriptor">Consent Service Descriptor</a>	| A <a href="Service Descriptor">Service Descriptor</a> of a <a href="Consent Service Description">Consent Service Description</a>.
<a id="consent-uri">Consent Uri</a>	| A <a href="Uri">Uri</a> which is used to identify a <a href="Consent">Consent</a>.
<a id="data-by-reference">Data by Reference</a>	| A pattern for exchanging data indirectly using a <a href="Data Reference">Data Reference</a>, see also <a href="Service by Reference">Service by Reference</a>.
<a id="data-description">Data Description</a>	| A description of data.
<a id="data-descriptor">Data Descriptor</a>	| An <a href="Uri">Uri</a> which can be used to identify and obtain a <a href="Data Description">Data Description</a>.
<a id="data-provider">Data Provider</a>	| A <a href="Business Role">Business Role</a> as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="data-provider-agreement">Data Provider Agreement</a>	| An agreement required for <a href="Data Provider">Data Providers</a>.
<a id="data-reference">Data Reference</a>	| An <a href="Operation Reference">Operation Reference</a> which can be used to obtain <a href="Personal Data">Personal Data</a> of an <a href="Individual">Individual</a>.
<a id="data-subject">Data Subject</a>	| As defined in the <a href="GDPR">GDPR</a>.
<a id="definitions-of-the-qiy-scheme">Definitions of the Qiy Scheme</a>	| One of the documents of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.
<a id="gdpr">GDPR</a>	| General Data Protection Regulation, see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 
<a id="governance-model-for-the-qiy-scheme">Governance Model for the Qiy Scheme</a>	| Governance Model for the <a href="Qiy Scheme">Qiy Scheme</a>, see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/.
<a id="http-request">HTTP Request</a>	| As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
<a id="individual">Individual</a>	| A <a href="Business Role">Business Role</a> of a <a href="Qiy User">Qiy User</a> as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="issuer">Issuer</a>	| A <a href="Business Role">Business Role</a> for an <a href="Access Provider">Access Provider</a> that provides services to natural persons, see <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="licence-agreement-application-provider">Licence Agreement Application Provider</a>	| A licence agreement for <a href="Application Provider">Application Providers</a>.
<a id="licence-agreement-issuer">Licence Agreement Issuer</a>	| A licence agreement for <a href="Issuer">Issuers</a>, the template of which is part of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.
<a id="licence-agreement-service-provider">Licence Agreement Service Provider</a>	| A licence agreement for <a href="Service Provider">Service Providers</a>, the template of which is part of the <a href="Qiy Scheme Rulebook">Qiy Scheme Rulebook</a>.
<a id="literal">Literal</a>	| A fixex value, see https://en.wikipedia.org/wiki/Literal_(computer_programming).
<a id="node">Node</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="operation">Operation</a> | A 'sub-service' which can be used to consume a <a href="Service">Service</a>.
<a id="operation-reference">Operation Reference</a>	| A <a href="Business Object">Business Object</a> used by the <a href="Service by Reference">Service by Reference</a>-pattern.
<a id="operation-specification">Operation Specification</a> | A specification of a <a href="Http Request">Http Request</a> for the execution of an <a href="Operation">Operation</a>.
<a id="personal-data">Personal Data</a>	| As defined in the <a href="GDPR">GDPR</a>.
<a id="path">Path</a>	| A connection between two <a href="Transporter">Transporters</a> which is used to exchange <a href="Transport Message">Transport Messages</a>.
<a id="proposer">Proposer</a>	| A <a href="Business Role">Business Role</a> for a <a href="Qiy User">Qiy User</a> that initiates creating a <a href="Connection">Connection</a> by providing a <a href="Connect Token">Connect Token</a>, sometimes using a <a href="Connect Proposal">Connect Proposal</a>.
<a id="provider">Provider</a>	| A <a href="Business Role">Business Role</a> for a <a href="Qiy User">Qiy User</a> that is providing one or more <a href="Service">Services</a> using Qiy, that is a <a href="Data Provider">Data Provider</a> or a <a href="Relying Party">Relying Party</a>.
<a id="qiy-application">Qiy Application</a>	| An <a href="Application Service">Application Service</a> or software that is authorized for use with Qiy.
<a id="qiy-application-protocol">Qiy Application Protocol</a>	| A protocol for the interactions between <a href="Qiy Application">Qiy Applications</a> and the underlying layers.
<a id="qiy-foundation">Qiy Foundation</a>	| A foundation dedicated to putting people back in control of their personal data while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.
<a id="qiy-foundation-member">Qiy Foundation Member</a>	| A member of the <a href="Qiy Foundation">Qiy Foundation</a>, see https://www.qiyfoundation.org/membership/.
<a id="qiy-node">Qiy Node</a>	| A <a href="Technology Service">Technology Service</a> as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="qiy-node-api">Qiy Node API</a>	| A <a href="Technology Interface">Technology Interface</a> of the <a href="Qiy Node">Qiy Node</a> that is part of the <a href="Qiy Open Standard">Qiy Open Standard</a>.
<a id="qiy-node-implementation">Qiy Node Implementation</a>	| A software package which can be used to realize a <a href="Qiy Node">Qiy Node</a>.
<a id="qiy-node-layer">Qiy Node Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="qiy-node-protocol">Qiy Node Protocol</a>	| A protocol describing the interaction between <a href="Qiy Node">Qiy Nodes</a> and the underlying layers.
<a id="qiy-open-standard">Qiy Open Standard</a>	| A set of open standards for Qiy, maintained by the <a href="Work Stream Functionality & Technology">Work Stream Functionality & Technology</a>, see https://www.qiyfoundation.org/qiy-scheme/workstreams/.
<a id="qiy-scheme">Qiy Scheme</a>	| See https://www.qiyfoundation.org/qiy-scheme/.
<a id="qiy-scheme-rulebook">Qiy Scheme Rulebook</a>	| A set of documents concerning governance, legal and technical aspects of the <a href="Qiy Scheme">Qiy Scheme</a>, see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/
<a id="qiy-trust-framework">Qiy Trust Framework</a>	| As defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="qiy-trust-principles">Qiy Trust Principles</a>	| As defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>, see https://www.qiyfoundation.org/qiy-trust-principles/.
<a id="qiy-user">Qiy User</a>	| A <a href="Business Actor">Business Actor</a>; defined as 'User' in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="reference">Reference</a>	| A <a href="Literal">Literal</a>.
<a id="relying-party">Relying Party</a>	| A <a href="Business Role">Business Role</a> as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="relying-party-agreement">Relying Party Agreement</a>	| An agreement that is required for <a href="Relying Party">Relying Parties</a>.
<a id="request">Request</a>	| A <a href="Business Object">Business Object</a>: a message requesting something.
<a id="transport-message">Transport Message</a>	| A message that is exchanged over a <a href="Path">Path</a> between two <a href="Transporter">Transporters</a>.
<a id="transport-message-description">Transport Message Description</a>	| A <a href="Data Description">Data Description</a> that describes the contents, format and encryption (if any) of a <a href="Transport Message">Transport Message</a>.
<a id="service">Service</a>	| An 'information society service' as defined in the <a href="GDPR">GDPR</a>.
<a id="service-by-reference">Service by Reference</a>	| A pattern for consuming <a href="Service">Services</a> indirectly using references (<a href="Operation Reference">Operation Reference</a>).
<a id="service-discovery">Service Discovery</a>	| A <a href="Business Proces">Business Process</a> to find <a href="Provider">Providers</a> for a given <a href="Service">Service</a>.
<a id="service-endpoint">Service Endpoint</a>	| A <a href="Technology Service">Technology Service</a> provided by a <a href="Provider">Provider</a> to allow the consumption of his <a href="Service">Services</a>.
<a id="service-layer">Service Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="service-library">Service Library</a>	| A <a href="Technology Service">Technology Service</a> that supports the <a href="Service">Service</a> processes of the <a href="Individual">Individuals</a> and the <a href="Provider">Providers</a>.
<a id="service-provider">Service Provider</a>	| A <a href="Business Role">Business Role</a>: an <a href="Access Provider">Access Provider</a> which provides business-to-business services as defined in <a href="Definitions of the Qiy Scheme">Definitions of the Qiy Scheme</a>.
<a id="service-source">Service Source</a>	| A <a href="Provider">Provider</a> that can or is providing a specific <a href="Service">Service</a>.
<a id="technology-event">Technology Event</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="technology-interface">Technology Interface</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html
<a id="technology-service">Technology Service</a>	| As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 
<a id="transport-connect-token">Transport Connect Token</a>	| A Literal used to create <a href="Path">Paths</a>.
<a id="transport-layer">Transport Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="transport-protocol">Transport Protocol</a>	| A protocol that is part of the <a href="Qiy Open Standard">Qiy Open Standard</a> and which describes the interaction between <a href="Transporter">Transporters</a> and the lower layers.
<a id="transporter">Transporter</a>	| A <a href="Technology Service">Technology Service</a> that provides transport services.
<a id="transporter-api">Transporter API</a>	| <a href="Technology Interface">Technology Interface</a> of a <a href="Transporter">Transporter</a>.
<a id="transporter-implementation">Transporter Implementation</a>	| A software package which can be used to realize a <a href="Transporter">Transporter</a>.
<a id="user-layer">User Layer</a>	| One of the <a href="Architectural Layers of the Qiy Scheme">Architectural Layers of the Qiy Scheme</a>.
<a id="uri">Uri</a>	| See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
<a id="url">Url</a>	| See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier
<a id="work-stream-functionality-&-technology">Work Stream Functionality & Technology</a>	| One of the work streams of the <a href="Qiy Foundation">Qiy Foundation</a>, see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

