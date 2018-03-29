# Functional and Technical Overview 'Qiy Scheme V1.0'


# Abstract

The [Qiy Scheme](Definitions.md#qiy-scheme) is a set of agreements encompassing all necessary topics needed to realize the goals of the [Qiy Foundation](Definitions.md#qiy-foundation). The [Qiy Scheme](Definitions.md#qiy-scheme) consists of the [Qiy Standard](Definitions.md#qiy-standard) for technical aspects and the [Qiy Scheme Rulebook](Definitions.md#qiy-scheme-rulebook) for governance aspects.

This document is produced by the [Work Stream Functionality](Definitions.md#work-stream-functionality) & Technology and intended for developers and architects who wish to design systems and applications that conform to the [Qiy Standard](Definitions.md#qiy-standard) of [Qiy Schem](Definitions.md#qiy-schem)e V1.0, which is the version released to the public in January 2015. 

# Content


1. [Introduction](#1-introduction)
	1. [Overview](#11-overview)
	1. [Terminology](#12-terminology)
1. [High-Level Qiy Use Cases](#2-high-level-qiy-use-cases)
	1. [Qiy Participants](#21-qiy-participants)
		1. [Individuals](#individuals)
		1. [Organizations](#organizations)
	1. [Qiy Roles](#22-qiy-roles)
		1. [Users](#221-users)
		1. [Orchestrator](#orchestrator)
		1. [Data](#data)
		1. [Relying](#relying)
		1. [Router](#222-router)
		1. [Scheme Authority](#223-scheme-authority)
	1. [Individual as Data Provider Use Case](#23-individual-as-data-provider-use-case)
		1. [Overview](#231-overview)
		1. [Zooming in](#232-zooming-in)
1. [Qiy Architecture](#3-qiy-architecture)
	1. [Basic Qiy Concepts](#31-basic-qiy-concepts)
		1. [[Qiy Node](Definitions.md#qiy-node)](#311-[qiy-node])
		1. [Global Addresses](#312-global-addresses)
		1. [Persistent Connections](#313-persistent-connections)
		1. [Structured data](#314-structured-data)
		1. [Distributed network of Nodes and Routers](#315-distributed-network-of-nodes-and-routers)
	1. [Protocol Layering](#32-protocol-layering)
		1. [Layer responsibilities](#321-layer-responsibilities)
		1. [Layer constraints](#322-layer-constraints)
	1. [Privacy in Qiy](#33-privacy-in-qiy)
	1. [Security in Qiy](#34-security-in-qiy)
1. [Application Layer](#4-application-layer)
	1. [Application Messages](#41-application-messages)
	1. [Responsibilities](#42-responsibilities)
		1. [Interface for the User](#421-interface-for-the-user)
		1. [Out-of-band Application interface](#422-out-of-band-application-interface)
		1. [Authentication of the User](#423-authentication-of-the-user)
		1. [Data interpretation and processing](#424-data-interpretation-and-processing)
		1. [Policy Enforcement Point](#425-policy-enforcement-point)
	1. [Node Connection](#43-node-connection)
	1. [Application Requirements](#44-application-requirements)
1. [Node Layer](#5-node-layer)
	1. [Responsibilities](#51-responsibilities)
		1. [Application Management](#511-application-management)
			1. [Application Authentication ](#5111-application-authentication-)
			1. [Application Authorization](#5112-application-authorization)
		1. [Application Messaging](#512-application-messaging)
		1. [Consent Management](#513-consent-management)
		1. [Digital Identity](#514-digital-identity)
		1. [Connection Management](#515-connection-management)
		1. [Key Management](#516-key-management)
		1. [Preferences and Settings](#517-preferences-and-settings)
	1. [Inter-Node Communication](#52-inter-node-communication)
	1. [Router Connection](#53-router-connection)
	1. [Node Requirements](#54-node-requirements)
1. [Routing Layer](#6-routing-layer)
	1. [Route](#61-route)
	1. [Responsibilities](#62-responsibilities)
		1. [Registering a Node](#621-registering-a-node)
		1. [Authenticating a Node](#622-authenticating-a-node)
		1. [Creating a Route between Nodes](#623-creating-a-route-between-nodes)
		1. [Message Routing](#624-message-routing)


# 1 Introduction
## 1.1 Overview
The chapters are:
1. 'Introduction' introducing this document.
2. 'High-Level Qiy Use Cases' describing some of the high-level [Use Cases](Definitions.md#use-case) that Qiy addresses.
3. 'Qiy Architecture' providing a brief description of the key Qiy concepts, layers and components defined in the standard.
4. 'Application Layer' describing the [Application Layer](Definitions.md#application-layer) and containing references to related documentation.
5. 'Node Layer' describing the [Node Layer](Definitions.md#node-layer) and containing references to related documentation.
6. 'Routing Layer' describing the [Routing Layer](Definitions.md#routing-layer) and containing references to related documentation.

## 1.2 Terminology
See [Definitions of the Qiy Scheme](./Definitions.md).

# 2 High-Level Qiy Use Cases

[Individuals](Definitions.md#individual) and organizations, including government organizations can be participants in the [Qiy Scheme](Definitions.md#qiy-scheme) in different roles.

## 2.1 Qiy Participants

### Individuals
[Individuals](Definitions.md#individual) benefit from participating in the [Qiy Scheme](Definitions.md#qiy-scheme), by gaining oversight and control over their personal information. By participating in the [Qiy Scheme](Definitions.md#qiy-scheme) they can:
1. Know where their [Data](Definitions.md#data) is
2. Access their [Data](Definitions.md#data) at the source
3. Control who uses this [Data](Definitions.md#data) and for what purpose
4. Re-use the [Data](Definitions.md#data) to create insight and value for themselves, or to share with others
5. Re-use the [Data](Definitions.md#data) with a vouch for its correctness from the party providing the [Data](Definitions.md#data).

### Organizations 
While the benefits of the [Qiy Scheme](Definitions.md#qiy-scheme) are obvious for [Individuals](Definitions.md#individual), organizations may benefit from participating as well. This includes government organizations, which can participate in the Scheme in a similar way as any other organization.

Organizations benefit in the following ways:
1. The quality of the [Data](Definitions.md#data) is likely to be higher, as the [Individual](Definitions.md#individual) can keep it up to date himself, and only has to manage it in one location
2. Unnecessary [Data](Definitions.md#data) replication is prevented, as [Data](Definitions.md#data) can remain at the source
3. Organizations can make use of [Data](Definitions.md#data) that is enriched with the vouch of another organization, increasing the correctness and hence value of the [Data](Definitions.md#data) (if the vouching organization is trusted)
4. Lower costs to get quality and [Consent](Definitions.md#consent) based [Data](Definitions.md#data)
5. Dynamic [Data](Definitions.md#data): subscribe to actual (and validated) [Data](Definitions.md#data)
6. Get to know one's customer not by collecting, but by connecting.

## 2.2 Qiy Roles
In the [Qiy Scheme](Definitions.md#qiy-scheme) different roles can be distinguished. A single organization may participate in the [Qiy Scheme](Definitions.md#qiy-scheme) in more than one role. At a minimum, a transaction in the [Qiy Scheme](Definitions.md#qiy-scheme) involves two [User](Definitions.md#user) roles and their respective Routers.

![The roles in the Qiy Scheme](./images/the-roles-in-the-qiy-scheme.png)

    Diagram 2-1 The roles in the [Qiy Scheme](Definitions.md#qiy-scheme)

### 2.2.1 Users
[Individuals](Definitions.md#individual) and organizations can participate in the [Qiy Scheme](Definitions.md#qiy-scheme) in different roles. 

### Orchestrator
[Individuals](Definitions.md#individual) participate in the [Qiy Scheme](Definitions.md#qiy-scheme) in the role of Orchestrator. The Orchestrator is represented in the [Qiy Scheme](Definitions.md#qiy-scheme) by his [Node](Definitions.md#node). The Orchestrator is in control of his [Node](Definitions.md#node) enabling him to decide how other participants will interact with him. The Orchestrator controls the relations with other participants and uses his [Node](Definitions.md#node) to manage his [Consent](Definitions.md#consent) for who may use his [Data](Definitions.md#data) for what purpose.

### Data Providers
[Data Providers](Definitions.md#data-provider) make [Data](Definitions.md#data) accessible to other [Users](Definitions.md#user) in the [Qiy Scheme](Definitions.md#qiy-scheme). A [Data Provider](Definitions.md#data-provider) can make [Data](Definitions.md#data) available to an Orchestrator after he has established a [Connection](Definitions.md#connection) to the Orchestrator's [Node](Definitions.md#node), so that the Orchestrator may use the [Data](Definitions.md#data) for his personal use, or share it in an interaction with another [User](Definitions.md#user). If an Orchestrator has given [Consent](Definitions.md#consent), the [Data Provider](Definitions.md#data-provider) may also share [Data](Definitions.md#data) with a [Relying Party](Definitions.md#relying-party) on behalf of the Orchestrator. These assertions typically supply the receiving party some [Personal Data](Definitions.md#personal-data) of the [Individual](Definitions.md#individual) that is necessary to perform a transaction. If an assertion is sent by a [Data Provider](Definitions.md#data-provider), he can enrich the metadata belonging to the [Data](Definitions.md#data) with a vouch for correctness of the [Data](Definitions.md#data). The receiving party may value this vouch based on trust and reputation of the [Data Provider](Definitions.md#data-provider).
[Data Providers](Definitions.md#data-provider) will often be (government) organizations that have a relation with the Orchestrator. In some cases, an [Individual](Definitions.md#individual) can be a [Data Provider](Definitions.md#data-provider); in this case the [Individual](Definitions.md#individual) will be the original source and the assertion that is given is not vouched for by any other [User](Definitions.md#user).

### Relying Parties
A [Relying Party](Definitions.md#relying-party) is a [User](Definitions.md#user) that relies on the [Trust Framework](Definitions.md#trust-framework) to receive [Data](Definitions.md#data) from an Orchestrator, typically for some kind of [Business Process](Definitions.md#business-proces). To receive this [Data](Definitions.md#data), it is required that the [Relying Party](Definitions.md#relying-party) establishes a [Connection](Definitions.md#connection) with the [Node](Definitions.md#node) of an Orchestrator. In practice, [Relying Party](Definitions.md#relying-party) will often also participate as a [Data Provider](Definitions.md#data-provider), making the exchange with the Orchestrator possible in both ways.

### 2.2.2 Router
Router is the general term for [Service Providers](Definitions.md#service-provider) whose primary purpose is to [Connect](Definitions.md#connect) [Users](Definitions.md#user) (respectively their [Nodes](Definitions.md#node)) to the [Qiy Scheme](Definitions.md#qiy-scheme). Some [Service Providers](Definitions.md#service-provider) focus on offering [Connections](Definitions.md#connection) to [Users](Definitions.md#user), others add additional [Services](Definitions.md#service) to the primary [Service](Definitions.md#service) of issuing [Nodes](Definitions.md#node).

### 2.2.3 Scheme Authority
The [Qiy Scheme](Definitions.md#qiy-scheme) is managed through an independent and international organization, called the [Scheme Authority](Definitions.md#scheme-authority). At the national level, the implementation of the Scheme in that national market is delegated to a [Regional Authority](Definitions.md#regional-authority). At all times the independence of the [Scheme Authority](Definitions.md#scheme-authority) and its national 'branches' shall be warranted. Also, at all times the Scheme in its implementation shall be open and non-discriminatory. To ensure this, appropriate audits and sanctions will be in place at both the national and the international level.
The [Scheme Authority](Definitions.md#scheme-authority) and its national 'branches' set and enforce the rules and regulations and issue licenses to participants of the [Qiy Scheme](Definitions.md#qiy-scheme).

The [Qiy Foundation](Definitions.md#qiy-foundation) fulfils the role of [Scheme Authority](Definitions.md#scheme-authority).

## 2.3 Individual as Data Provider Use Case

### 2.3.1 Overview
In the following example, an [Individual](Definitions.md#individual) named Alice places an order from a web shop called Webshop.com.
To [Connect](Definitions.md#connect) with others on the [Qiy Infrastructure](Definitions.md#qiy-infrastructure), Alice uses an app on her smartphone that enables her to scan QR codes to [Connect](Definitions.md#connect). In her role as Orchestrator, Alice is in control of the process described in the [Use Case](Definitions.md#use-case).
Webshop.com is an organization connected to the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) by their Router. To serve Alice, Webshop.com relies on information to be supplied by her using the [Qiy Infrastructure](Definitions.md#qiy-infrastructure); Webshop.com is a [Relying Party](Definitions.md#relying-party) in this [Use Case](Definitions.md#use-case).

The processing sequence is as follows:
1. Alice visits the website of Webshop.com and puts an item in her shopping cart. 
2. Alice proceeds to the check out to purchase the item in her cart.
3. To further serve Alice, Webshop.com requests Alice to [Connect](Definitions.md#connect) so that Webshop.com may use Alice's [Data](Definitions.md#data). Webshop.com presents Alice with a [Connect Token](Definitions.md#connect-token) in the form of a QR code so that Alice can [Connect](Definitions.md#connect) with Webshop.com.
4. Using the app on her smartphone, Alice scans the QR code, establishing a [Connection](Definitions.md#connection) with the Webshop.com.
5. Alice can now share the necessary [Data](Definitions.md#data) (e.g. name, delivery address, preferences, etc.) with Webshop.com and complete her order.

![The individual as a data provider](./images/the-individual-as-a-data-provider.png)

    Diagram 2-2 The [Individual](Definitions.md#individual) as a [Data Provider](Definitions.md#data-provider)

### 2.3.2 Zooming in
The [Individual](Definitions.md#individual) and the [Node](Definitions.md#node)
Alice is represented in the [Qiy Scheme](Definitions.md#qiy-scheme) by her personal [Node](Definitions.md#node). As an Orchestrator she interacts with her [Node](Definitions.md#node) using one or more Applications. For the worked example, we assume that Alice uses an app on her smartphone that can interact with her [Node](Definitions.md#node). This app also enables Alice to [Connect](Definitions.md#connect) with other parties that participate in the [Qiy Scheme](Definitions.md#qiy-scheme), such as Webshop.com in this example.

Advertising the [Connect Token](Definitions.md#connect-token)
Alice can visit the website of Webshop.com and put items in her cart without having to identify herself to Webshop.com. To complete the order however, Webshop.com requires some information about Alice; e.g. her real name and her address. To acquire this information using Qiy, Webshop.com invites Alice to [Connect](Definitions.md#connect) them. To establish a [Connection](Definitions.md#connection) with her [Node](Definitions.md#node), Webshop.com generates a [Connect Token](Definitions.md#connect-token) and presents it out-of-band. In this example, the [Connect Token](Definitions.md#connect-token) is presented as a QR code that can be scanned using an appropriate app. The [Connect Token](Definitions.md#connect-token) contains the information necessary for the app to establish a [Connection](Definitions.md#connection) with Webshop.com. Alice scans this code using the app on her phone.

Establishing a [Connection](Definitions.md#connection)
Using the [Connect Token](Definitions.md#connect-token), the app establishes a secure, encrypted [Connection](Definitions.md#connection) between Alice's [Node](Definitions.md#node) and the [Node](Definitions.md#node) of Webshop.com via the Routers. Once this route has been established, Alice and Webshop.com may exchange [Data](Definitions.md#data) through the [Qiy Infrastructure](Definitions.md#qiy-infrastructure). All [Data](Definitions.md#data) transmitted over this [Connection](Definitions.md#connection) is shielded from other parties in between, i.e. the Routers only forward the [Data](Definitions.md#data) to the destination [Node](Definitions.md#node), but cannot read the contents of the [Messages](Definitions.md#message) they are passing along.

[Data](Definitions.md#data) exchange
The route between Alice's [Node](Definitions.md#node) and Webshop.com can be used to securely exchange information; Alice is, as the Orchestrator, in control over what [Data](Definitions.md#data) will or will not be shared with [Relying Parties](Definitions.md#relying-party) connected to her [Qiy Node](Definitions.md#qiy-node).
To complete Alice's order, Webshop.com requests the address where her order should be shipped to. Alice acts as a [Data Provider](Definitions.md#data-provider) and supplies this input herself. Webshop.com may then complete the order based on the [Data](Definitions.md#data) Alice has shared.
# 3 Qiy Architecture
This chapter describes the [Qiy Architecture](Definitions.md#qiy-architecture): the entities and their interrelations, which are involved in online communication and transactions. 

The capabilities of the architecture will be illustrated using a limited real-life [Qiy Scheme](Definitions.md#qiy-scheme) web scenario. The rest of the chapter addresses the rationale behind the architecture: why it has been designed the way it has been designed and how it relates to the [Qiy Principles](Definitions.md#qiy-principle) proclaimed by the [Qiy Foundation](Definitions.md#qiy-foundation).
## 3.1 Basic Qiy Concepts
### 3.1.1 [Qiy Node](Definitions.md#qiy-node)
The [Qiy Node](Definitions.md#qiy-node) is a delegate component for Applications. The [Node](Definitions.md#node) is responsible for [Connection](Definitions.md#connection) management of global addresses, [Connections](Definitions.md#connection), [Key Management](Definitions.md#key-management), and cryptographic transformations of [Messages](Definitions.md#message) and implements the [Connection](Definitions.md#connection) to the [Qiy Infrastructure](Definitions.md#qiy-infrastructure).
### 3.1.2 Global Addresses
Like e-mail addresses, you can send [Messages](Definitions.md#message) using the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) to a [Qiy Node](Definitions.md#qiy-node) by sending [Messages](Definitions.md#message) to the address. Unlike e-mail addresses however, [Users](Definitions.md#user) have many different [Qiy Node](Definitions.md#qiy-node) addresses, as each [Connection](Definitions.md#connection) should use their own unique address. Qiy uses globally unique addresses (based on the [Domain Name System](Definitions.md#domain-name-system)) in order to route [Connections](Definitions.md#connection) and deliver their [Messages](Definitions.md#message) over the [Qiy Infrastructure](Definitions.md#qiy-infrastructure). 
### 3.1.3 Persistent Connections
Upon fulfillment of the preconditions, a [Qiy Node](Definitions.md#qiy-node) has a long-lived [Connection](Definitions.md#connection) with another [Qiy Node](Definitions.md#qiy-node), which enables the [Users](Definitions.md#user) controlling the connected [Nodes](Definitions.md#node) to send and receive a potentially unlimited number of [Messages](Definitions.md#message) over the [Connection](Definitions.md#connection). Such a [Connection](Definitions.md#connection) can be used to engage in a-synchronous structured request-response interactions, in close to real time and real time [Data](Definitions.md#data) streaming.
### 3.1.4 Structured data
The basic protocol [Data](Definitions.md#data) unit in Qiy is not a [Connection](Definitions.md#connection) (which simply provides the transport for point-to-point communication) but a [Qiy Message](Definitions.md#qiy-message), which is essentially [Data](Definitions.md#data) or a fragment of [Data](Definitions.md#data) that is sent over a [Connection](Definitions.md#connection). 

After two [Qiy Nodes](Definitions.md#qiy-node) have completed the [Connection](Definitions.md#connection) negotiation, either party can send [Messages](Definitions.md#message). A [Message](Definitions.md#message) contains the following parts:
* [Connection](Definitions.md#connection) information
* [Consent](Definitions.md#consent) information
* [Application Data](Definitions.md#application-data).
[Connection](Definitions.md#connection) information
[Connection](Definitions.md#connection) information refers to the global address of a [Qiy Node](Definitions.md#qiy-node) and [Connection](Definitions.md#connection)-[Tokens](Definitions.md#token), intended to route [Messages](Definitions.md#message), and information used during the [Connection](Definitions.md#connection) negotiation like session keys.
[Consent](Definitions.md#consent) information
Per the [Qiy Principles](Definitions.md#qiy-principle), [Data](Definitions.md#data) may only be used with the [User](Definitions.md#user)'s permission only. [Consent](Definitions.md#consent) describes how an [Individual](Definitions.md#individual) allows his [Data](Definitions.md#data) to be used by a [Relying Party](Definitions.md#relying-party) in the [Qiy Scheme](Definitions.md#qiy-scheme). [Consent](Definitions.md#consent) specifies the permissions that are applied to a certain set of [Data](Definitions.md#data) for a specific [Relying Party](Definitions.md#relying-party). 

[Consent](Definitions.md#consent) specifies at least the following parameters:
* What [Data](Definitions.md#data) the [Consent](Definitions.md#consent) is applied to
* How many times the [Data](Definitions.md#data) may be accessed (e.g. single time only, or unlimited times)
* For what period of time the requesting party may access the [Data](Definitions.md#data) (e.g. an hour, or a year)
* The purpose for which the [Consent](Definitions.md#consent) was given (e.g. to deliver your order to your home address, or to give you financial advice).

The [Data Provider](Definitions.md#data-provider) initiates the [Consent Request](Definitions.md#consent-request) to the Orchestrator, where the [Consent Request](Definitions.md#consent-request) contains a clear human readable purpose declaration.
Application [Data](Definitions.md#data)
Application [Data](Definitions.md#data) can be considered as the [Message](Definitions.md#message) payload after the [Connection](Definitions.md#connection) is established. Applications are free to declare and implement namespaces to structure [Data](Definitions.md#data) elements and attributes of [Data](Definitions.md#data) contained in a [Message](Definitions.md#message) payload. 

The assessment of the quality of [Data](Definitions.md#data) received by a [Relying Party](Definitions.md#relying-party) and the trustworthiness of the [Data](Definitions.md#data) is at the discretion of the [Relying Party](Definitions.md#relying-party) and depends on the [Data Provider](Definitions.md#data-provider) reputation and relation to that [Relying Party](Definitions.md#relying-party). For this purpose the Application [Data](Definitions.md#data) contains metadata identifying the asserting [Data Provider](Definitions.md#data-provider) and the level of assurance of the [Connection](Definitions.md#connection) between [Data Provider](Definitions.md#data-provider) and Orchestrator.
### 3.1.5 Distributed network of Nodes and Routers
In practice, the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) consists of a network of Routers and [Nodes](Definitions.md#node) that inter-communicate. Important design considerations are:
* [Nodes](Definitions.md#node) only communicate with the Router where they are registered
* [Nodes](Definitions.md#node) only communicate with Routers that are licensed by the [Qiy Authority](Definitions.md#qiy-authority)
* Routers only communicate with [Qiy Nodes](Definitions.md#qiy-node) they trust; i.e. have registered
* Routers only communicate with routers that are licensed by the [Qiy Authority](Definitions.md#qiy-authority).
## 3.2 Protocol Layering
The [Qiy Standard](Definitions.md#qiy-standard) uses protocol layering to simplify the designs by dividing them into functional layers, and assigning protocols to perform each layer's task. The [Qiy Standard](Definitions.md#qiy-standard) divides the protocols into three virtual layers:

1. [Application Layer](Definitions.md#application-layer): consists of applications and/or [Services](Definitions.md#service), which deliver trustful [Services](Definitions.md#service) to end [Users](Definitions.md#user) and/or businesses
2. [Node Layer](Definitions.md#node-layer): consists of [Nodes](Definitions.md#node) representing [Users](Definitions.md#user), the layer is responsible for among other things [Consent Management](Definitions.md#consent-management), [Key Management](Definitions.md#key-management), [Session Management](Definitions.md#session-management) and [Connection Management](Definitions.md#connection-management)
3. [Routing Layer](Definitions.md#routing-layer): consist of Routers responsible for routing [Messages](Definitions.md#message) between [Nodes](Definitions.md#node).

Each layer provides [Services](Definitions.md#service) to the next-higher layer and shields the upper layer from the details of how the [Services](Definitions.md#service) below it are actually implemented. At the same time, each entity in a layer appears to be in direct communication with other entities.


![Example configuration of applications, nodes and routers](./images/example-configuration-of-applications-nodes-and-routers.png)

    Diagram 3-1 Example configuration of applications, [Nodes](Definitions.md#node) and routers

### 3.2.1 Layer responsibilities
The [Application Layer](Definitions.md#application-layer) responsibilities are:
1. Provide an Interface for the [User](Definitions.md#user)
2. Out of band Application interface
3. Authentication of the [User](Definitions.md#user)
4. [Data](Definitions.md#data) interpretation and processing
5. [Policy Enforcement Point](Definitions.md#policy-enforcement-point).

The [Node Layer](Definitions.md#node-layer) responsibilities are:
1. [Application Management](Definitions.md#application-management) - What Applications are linked to the [Node](Definitions.md#node) and what are their capabilities
2. [Application Messaging](Definitions.md#application-messaging) - Persist, deliver and delegate [Messages](Definitions.md#message) (from/to an Application or a [Node](Definitions.md#node))
3. [Consent Management](Definitions.md#consent-management) - Manage the 'Pass by reference register' (who may access what [Data](Definitions.md#data), and when does the permission expire)
4. [Connection Management](Definitions.md#connection-management) - Manage the [Connections](Definitions.md#connection) with other [Nodes](Definitions.md#node)
5. Key management
6. Preferences and settings.

The responsibilities of the [Routing Layer](Definitions.md#routing-layer) are:
1. Registering a [Node](Definitions.md#node)
2. Authenticating a [Node](Definitions.md#node)
3. Creating a Route between [Nodes](Definitions.md#node)
4. [Message](Definitions.md#message) routing.
### 3.2.2 Layer constraints
The configuration illustrates some of the major constraints of the [Qiy Architecture](Definitions.md#qiy-architecture):
1. [Users](Definitions.md#user) can use one or more Applications to communicate and interact
2. Each Application is connected to the [Node](Definitions.md#node) of the [User](Definitions.md#user)
3. Each [Node](Definitions.md#node) is connected to one Router
4. Each Router can be connected to one or more [Nodes](Definitions.md#node)
5. Each Router can be connected to one or more other Routers.
## 3.3 Privacy in Qiy
In designing and developing the [Qiy Scheme](Definitions.md#qiy-scheme), privacy by design is default. This refers to both a [User](Definitions.md#user)'s ability to control how their [Personal Data](Definitions.md#personal-data) is shared and used, and to mechanisms that inhibit their actions at multiple participants from being inappropriately correlated. 

Qiy has a number of mechanisms that support deployment in privacy:
* Qiy implements an indirect routing strategy. When a [Node](Definitions.md#node) sends a [Message](Definitions.md#message) to another [Node](Definitions.md#node), that [Message](Definitions.md#message) is send to the Router the sending [Node](Definitions.md#node) is registered at. The receiving Router forwards the [Message](Definitions.md#message) to the Router the destination [Node](Definitions.md#node) is registered at. Routing tables hold only information to forward to the next hop
* Qiy supports the establishment of pseudonyms established between an Orchestrator and other [Users](Definitions.md#user) ([RelyingParty](Definitions.md#relyingparty) and [Data Provider](Definitions.md#data-provider)). Such pseudonyms do not themselves enable inappropriate correlation between [Relying Parties](Definitions.md#relying-party) and [Data Providers](Definitions.md#data-provider) (as would be possible if the [Node](Definitions.md#node) asserted the same identifier for a [User](Definitions.md#user) to every other [User](Definitions.md#user), a so-called global address)
* Qiy supports one-time or transient identifiers ' such identifiers ensure that every time a certain Orchestrator establishes a connector with a given [Relying Party](Definitions.md#relying-party) or [Data Provider](Definitions.md#data-provider), that party will be unable to recognize them as the same Orchestrator that might have previously visited them (based solely on the identifier, correlation may be possible through non-Qiy [Data](Definitions.md#data)).

## 3.4 Security in Qiy
How can the [Relying Party](Definitions.md#relying-party) trust information being exchanged' In addition, what prevents a 'man-in-the-middle' attack that might grab information to be illicitly 'replayed' at a later date' These and many more security considerations are discussed in detail in the [Qiy Security and Privacy Considerations Specification](Definitions.md#qiy-security-and-privacy-considerations-specification). 

Qiy defines a number of security mechanisms to detect and protect against such attacks. The primary mechanism is for the Orchestrator and the [Data Provider](Definitions.md#data-provider) and [Relying Party](Definitions.md#relying-party) to have a pre-existing trust relationship which typically relies on a [Public Key Infrastructure](Definitions.md#public-key-infrastructure) (PKI). A general overview of what is recommended is provided below:
* All communication between a [Node](Definitions.md#node) and a Router and between Routers use the TLS protocol
* To prevent old communications to be reused in replay attacks, use of nonces is recommended. A nonce is an arbitrary number that may only be used once. To ensure that a nonce can only be used once, it should be time-variant (including a suitably fine-grained timestamp in its value), or generated with enough random bits to ensure a probabilistically insignificant chance of repeating a previously generated value. 
* Communication between [Nodes](Definitions.md#node) is encrypted using symmetric encryption. 
During the [Connection](Definitions.md#connection) negotiation all [Messages](Definitions.md#message) between a [Node](Definitions.md#node) and a Router and between Routers are digitally signed to ensure that the content of the [Message](Definitions.md#message) cannot be altered during this stage.

# 4 Application Layer
This chapter is describing the [Application Layer](Definitions.md#application-layer). While all other components of the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) are generic, Applications allow for specific behavior. The Application is what differentiates a web shop from a bank. 

![Application context diagram](./images/application-context-diagram.png)

    Diagram 4-1 Application context diagram

A [Node](Definitions.md#node) may use multiple Applications; each specialized in a specific behavior, together enabling their [User](Definitions.md#user) with a multitude of behaviors. Each Application instance is however always only connected to one [Node](Definitions.md#node). 
## 4.1 Application Messages
Once a [Connection](Definitions.md#connection) between [Nodes](Definitions.md#node) has been made, Applications can use it to exchange [Messages](Definitions.md#message). The actual content of these [Messages](Definitions.md#message) are meaningful for the Applications, but is out of scope for the [Qiy Standard](Definitions.md#qiy-standard). 

To exchange information an Application must communicate:
* Definition of the format of the [Message](Definitions.md#message), i.e. how the [Message](Definitions.md#message) can be understood by another Application protocol
* What the [Message](Definitions.md#message) is about is that are terms understandable for an [Individual](Definitions.md#individual) (used for [Consent](Definitions.md#consent) [Messages](Definitions.md#message))
* The meaningful content itself (also referred to as 'payload').

The Application may use an interface on the [Node](Definitions.md#node) that supports encryption to protect the [Message](Definitions.md#message) from prying eyes, but the [Message](Definitions.md#message) itself should be transmitted plaintext.
Each [Message](Definitions.md#message) that an Application constructs will be sent to a [Node](Definitions.md#node); each [Message](Definitions.md#message) that a [Node](Definitions.md#node) receives will be handled by an Application. Communication between Applications is indirect: multiple Applications may be able to respond to any [Message](Definitions.md#message), it is up to the [User](Definitions.md#user) to decide which one will actually handle the [Message](Definitions.md#message).
## 4.2 Responsibilities
The responsibilities of the [Application Layer](Definitions.md#application-layer) are stated in 3.2.1. Each of the following sections in this chapter will handle one. For convenience they are repeated here:

1. Interface for the [User](Definitions.md#user)
2. Out-of-band Application interface
3. Authentication of the [User](Definitions.md#user)
4. [Data](Definitions.md#data) interpretation and processing
5. [Policy Enforcement Point](Definitions.md#policy-enforcement-point).
### 4.2.1 Interface for the User
Only Applications are allowed to interface with the [Node](Definitions.md#node) and as such, the Application acts as an interface on the [Node](Definitions.md#node) for the [User](Definitions.md#user). If the [User](Definitions.md#user) is an automated system, this interface will be an API. If the [User](Definitions.md#user) is human, the interface will be a (G)UI. Separate Applications may provide parts of the interface, e.g. by only reacting on a subset of all [Data](Definitions.md#data) received by the [Node](Definitions.md#node).
### 4.2.2 Out-of-band Application interface
When the [User](Definitions.md#user) wants to set-up a [Connection](Definitions.md#connection) with another [User](Definitions.md#user), the initiating party uses an Application to present a [Connect Token](Definitions.md#connect-token). The Application does this by requesting the information required from the [Node](Definitions.md#node) and converting that to the presentable form. 
Some Application of the other [User](Definitions.md#user) must be able to receive the [Token](Definitions.md#token) and forward it to the other [User](Definitions.md#user)'s [Node](Definitions.md#node). 

The [Connect Token](Definitions.md#connect-token) should not be transmitted via the [Qiy Infrastructure](Definitions.md#qiy-infrastructure), i.e for security reasons there must be out-of-band communication of the [Connect Token](Definitions.md#connect-token).
In the [Use Case](Definitions.md#use-case) of the [Individual](Definitions.md#individual) as a [Data Provider](Definitions.md#data-provider), this is done by Webshop.com by displaying a QR code on their website (the Application) and Alice's Application scanning it, using the air as a transport medium. 
### 4.2.3 Authentication of the User
As the [Application Layer](Definitions.md#application-layer) is the main interface for the [User](Definitions.md#user), it needs to ensure that the [User](Definitions.md#user) accessing the Application is who he claims he is.
### 4.2.4 Data interpretation and processing
As a [Node](Definitions.md#node) is generic, it is left up to the Application to provide meaning to the received [Messages](Definitions.md#message). Depending on the protocol a specific Application may or may not be able to provide this meaning. Furthermore, once the meaning is given, the Application may be able to do further processing on the [Message](Definitions.md#message). 

For example: in the 'Individual as Data Provider' [Use Case](Definitions.md#use-case), this is done by Alice's Application on her phone. When Webshop.com sends a question to Alice's [Node](Definitions.md#node), the Application is able to see that Alice needs to answer it herself. The Application processes the [Message](Definitions.md#message) and presents it in a form, which Alice can understand and respond to.
### 4.2.5 Policy Enforcement Point
If an Application is a [Data Provider](Definitions.md#data-provider), it should check the validity of the [Data](Definitions.md#data) request on each invocation, i.e. whenever giving out [Data](Definitions.md#data) the Application should ensure that:
* The requesting party is allowed access to the [Data](Definitions.md#data);
* The time-frame for which access was allowed has not expired;
* The number of times access was allowed has not been exceeded;
* The access has not been revoked.
## 4.3 Node Connection
The Application may [Connect](Definitions.md#connect) to an existing [Node](Definitions.md#node) or register a new [Node](Definitions.md#node). In each case the Application must provide the proper means for the [Node](Definitions.md#node) to determine if the Application is authorized to do so. The Application must also provide the [Node](Definitions.md#node) with a listing of the capabilities the Application has. This list defines the [Data](Definitions.md#data) and [Services](Definitions.md#service) that the Application can provide. The list takes the form of a list of protocols
## 4.4 Application Requirements
[TBD](Definitions.md#tbd)

# 5 Node Layer
This chapter describes the [Node Layer](Definitions.md#node-layer), its responsibilities and how these are met.

![Node context diagram](./images/node-context-diagram.png)

    Diagram 5-1 [Node](Definitions.md#node) context diagram

## 5.1 Responsibilities
The [Node Layer](Definitions.md#node-layer) responsibilities are:
1. [Application Management](Definitions.md#application-management) - What Applications are linked to the [Node](Definitions.md#node) and what are their capabilities
2. [Application Messaging](Definitions.md#application-messaging) - Persist, deliver and delegate [Messages](Definitions.md#message) (from/to an Application or a [Node](Definitions.md#node))
3. [Consent Management](Definitions.md#consent-management) - Manage the 'Pass by reference register' (who may access what [Data](Definitions.md#data), and when does the permission expire)
4. [Connection Management](Definitions.md#connection-management) - Manage the [Connections](Definitions.md#connection) with other [Nodes](Definitions.md#node)
5. Key management
6. Preferences and settings.
### 5.1.1 Application Management
Each [Node](Definitions.md#node) maintains a registration of the connected Applications and acts as a registry for related information, such as the supported [Application Protocols](Definitions.md#application-protocol).
#### 5.1.1.1 Application Authentication 
An Application can only [Connect](Definitions.md#connect) with a [Node](Definitions.md#node) and exchange [Messages](Definitions.md#message) via the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) when it has been authenticated by that [Node](Definitions.md#node).
#### 5.1.1.2 Application Authorization
[TBD](Definitions.md#tbd)
### 5.1.2 Application Messaging
A [Node](Definitions.md#node) persists all the application [Messages](Definitions.md#message) it has received from and/or sent to other [Nodes](Definitions.md#node) and assures and maintains the delivery status. 
The [Node](Definitions.md#node) addresses outgoing application [Messages](Definitions.md#message) to the destination [Node](Definitions.md#node). [Application Messages](Definitions.md#application-message) are delivered to the Router. It is the sending [Node](Definitions.md#node)'s responsibility to ensure the confidentiality of the [Message](Definitions.md#message) by encrypting it in a way only the destination [Node](Definitions.md#node) can decrypt.
The delivery of incoming application [Messages](Definitions.md#message) is based on the [Application Protocol](Definitions.md#application-protocol). [Messages](Definitions.md#message) are delivered to a supporting Application. Which Application handles which [Message](Definitions.md#message) is determined either after [User](Definitions.md#user) interaction or by using preference. [Data](Definitions.md#data) requests and responses are delivered in the same way, but only when they have been consented for.
### 5.1.3 Consent Management
 All [Data](Definitions.md#data) exchanges are subject to [Consent](Definitions.md#consent) management:
1. [Incoming Data Requests](Definitions.md#incoming-data-request) (from other [Users](Definitions.md#user)) for [Data](Definitions.md#data) owned by the [Node](Definitions.md#node)'s [User](Definitions.md#user) are only accepted when the associated [Consent](Definitions.md#consent) is (or has previously been) accepted by the [User](Definitions.md#user).
2. [Incoming Data Requests](Definitions.md#incoming-data-request) for [Data](Definitions.md#data) of [Users](Definitions.md#user) other than the receiver or the sender are subject to the owner's [Consent](Definitions.md#consent). 

The [Node](Definitions.md#node) keeps track of all [Data Requests](Definitions.md#data-request), [Data Responses](Definitions.md#data-response), [Data Notifications](Definitions.md#data-notification) and [Consents](Definitions.md#consent).
### 5.1.4 Digital Identity
A [Node](Definitions.md#node) represents a [User](Definitions.md#user) in the digital realm and is as such his [Digital Identity](Definitions.md#digital-identity). A [Node](Definitions.md#node) can be addressed by any other [Node](Definitions.md#node) using global addresses when a [Connection](Definitions.md#connection) has been established between the two. This [Connection](Definitions.md#connection) can be regarded as the digital equivalent of a relationship between two [Users](Definitions.md#user), e.g. an [Individual](Definitions.md#individual) and a web shop.
### 5.1.5 Connection Management
The [Node](Definitions.md#node) acts as a registry for its [Connections](Definitions.md#connection), the status and related information and provides means for their management. 
### 5.1.6 Key Management
The [Node](Definitions.md#node) is responsible for the proper management of all the key pairs that are used to meet its responsibilities.
### 5.1.7 Preferences and Settings
 The [Node](Definitions.md#node) can act as a registry for preferences and settings of sorts and provides means for their management.
## 5.2 Inter-Node Communication
A [Node](Definitions.md#node) can only communicate another [Node](Definitions.md#node) over a bi-directional communication channel (route), which is created when two [Users](Definitions.md#user) establish a [Connection](Definitions.md#connection).
Please refer to Error! Reference source not found. Error! Reference source not found. for more information on establishing and using [Routes](Definitions.md#route).
## 5.3 Router Connection
Only [Nodes](Definitions.md#node) that fulfill the [Node Requirements](Definitions.md#node-requirement) can establish a [Connection](Definitions.md#connection) with a Router and only with Routers that fulfill the [Router Requirements](Definitions.md#router-requirement).
Please refer to chapter 6 [Routing Layer](Definitions.md#routing-layer) for more information. 
## 5.4 Node Requirements
[TBD](Definitions.md#tbd)


# 6 Routing Layer
This chapter is dedicated to the [Routing Layer](Definitions.md#routing-layer).


![Router context diagram](./images/router-context-diagram.png)

    Diagram 6-1 Router context diagram

## 6.1 Route
The Route is a key principle ensuring the privacy of the [Nodes](Definitions.md#node). The archetypical Route is shown in the next diagram: 

![Archetypical Route](./images/archetypical-route.png)

    Diagram 6-2 [Archetypical Route](Definitions.md#archetypical-route)
	
In this Route, [Node](Definitions.md#node) A has a unique address for this Route with Router A, which in turn publishes a unique address for this Route to both [Node](Definitions.md#node) A and Router B. Router B in turn has its own unique address for this route, which it publishes to both Router A and [Node](Definitions.md#node) B. No further information about the Route is given to each party. This ensures that [Node](Definitions.md#node) A cannot know the identity of Router B or [Node](Definitions.md#node) B.
Likewise [Node](Definitions.md#node) B cannot know the identity of Router A or [Node](Definitions.md#node) A. Router A cannot know [Node](Definitions.md#node) B and Router B cannot know [Node](Definitions.md#node) A. By splitting up the knowledge of the complete Route, the privacy of the [Nodes](Definitions.md#node) is ensured.
## 6.2 Responsibilities
The [Routing Layer](Definitions.md#routing-layer) responsibilities are:
1. Registering a [Node](Definitions.md#node)
2. Authenticating a [Node](Definitions.md#node)
3. Creating a Route between [Nodes](Definitions.md#node)
4. [Message](Definitions.md#message) routing.
### 6.2.1 Registering a Node
Any [Node](Definitions.md#node) can only participate in the [Qiy Infrastructure](Definitions.md#qiy-infrastructure) by using a Router. Each [Node](Definitions.md#node) should only [Connect](Definitions.md#connect) to one Router. In order to enable the [Node](Definitions.md#node) to [Connect](Definitions.md#connect), the Router has to be made aware of its presence. To do this, the [Node](Definitions.md#node) registers itself with the Router. In this process the [Node](Definitions.md#node) and the Router exchange whatever information is required for the Router to Authenticate the [Node](Definitions.md#node).
### 6.2.2 Authenticating a Node
It is the responsibility of the Router to ensure that any [Operation](Definitions.md#operation) made on a [Node](Definitions.md#node)'s behalf, can only be done by that [Node](Definitions.md#node) and no other.
### 6.2.3 Creating a Route between Nodes
When creating a [Node](Definitions.md#node), the design considerations from paragraph 3.1.5 should always be taken into account. The creation of a Route between [Node](Definitions.md#node) A and [Node](Definitions.md#node) B, initiated by [Node](Definitions.md#node) A is realized in the following steps:

1. [Node](Definitions.md#node) A requests a notification on a unique address (a) from Router A on a coming event
2. Router A provides [Node](Definitions.md#node) A with a unique address (b) to trigger the event
3. [Node](Definitions.md#node) A uses the unique address (b) in a [Connect Token](Definitions.md#connect-token) which it advertises
4. [Node](Definitions.md#node) B picks up the [Connect Token](Definitions.md#connect-token), creates a unique address (c)
5. [Node](Definitions.md#node) B provides Router B with unique address (c) and (b), the latter of which it got from the [Connect Token](Definitions.md#connect-token)
6. Router B creates a unique address (d), which it associates with [Node](Definitions.md#node) B's unique address (c)
7. Router B triggers the event by calling (b) on Router A, with (d) as a parameter
8. Router A creates a unique address (e) which it returns to Router B
9. Router B associates the partial Route (d)(c) with (e)
10. Router A calls (a) with parameter (e)
11. [Node](Definitions.md#node) A creates a unique address (f), which it returns to Router A
12. Router A associates the partial Route (e)(d) with (f)
13. [Node](Definitions.md#node) A associates (f) with (e).
14. The following Route has been created: (f)-(e)-(d)-(c)

Please note that Router A and Router B may be in fact the same entity. 

### 6.2.4 Message Routing

The [Routing Layer](Definitions.md#routing-layer) is responsible for routing [Application Messages](Definitions.md#application-message) between the [Nodes](Definitions.md#node). The [Application Messages](Definitions.md#application-message) are passed along the Route. Each of the [Nodes](Definitions.md#node) on the Route can use the Route to exchange [Messages](Definitions.md#message). All the information a Router needs to pass on the [Message](Definitions.md#message) is its unique address within the Route and the layer where the sender resides. Given the example in the previous paragraph: 

* If Router A receives a [Message](Definitions.md#message) at address (e) and the sender is the [Node](Definitions.md#node) layer, the [Message](Definitions.md#message) needs to be forwarded to (d)
* If Router A receives a [Message](Definitions.md#message) at address (e) and the sender is the Routing layer, the [Message](Definitions.md#message) needs to be forwarded to (f)

Only [Messages](Definitions.md#message) where a Route exists are processed.


