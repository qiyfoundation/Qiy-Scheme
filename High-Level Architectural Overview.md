# High-Level Architectural Overview


# Abstract

This document is produced by the [Work Stream Functionality & Technology] and describes the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.


# Content


1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Readers' Guidance](#12-readers-guidance)
	1. [Overview](#13-overview)
	1. [Terminology](#14-terminology)
1. [High-Level Qiy Use Cases](#2-high-level-qiy-use-cases)
1. [Qiy Architecture](#3-qiy-architecture)
	1. [Basic Qiy Concepts](#31-basic-qiy-concepts)
		1. [Qiy Node](#311-qiy-node)
		1. [Global Addresses](#312-global-addresses)
		1. [Persistent Connections](#313-persistent-connections)
		1. [Structured data](#314-structured-data)
		1. [Distributed network of Nodes and [Routers]](#315-distributed-network-of-nodes-and-[routers])
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
1. [Qiy Node Layer](#5-qiy-node-layer)
	1. [Responsibilities](#51-responsibilities)
		1. [Application Management](#511-application-management)
			1. [Application Authentication ](#5111-application-authentication-)
			1. [Application Authorization](#5112-application-authorization)
		1. [Messaging](#512-messaging)
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
		1. [Registering a Qiy Node](#621-registering-a-qiy-node)
		1. [Authenticating a Qiy Node](#622-authenticating-a-qiy-node)
		1. [Creating a Route between Nodes](#623-creating-a-route-between-nodes)
		1. [Message Routing](#624-message-routing)


# 1 Introduction

This chapter describes the purpose, contents, structure and use of this document.


## 1.1 Purpose

Qiy, or rather: the [Qiy Scheme], puts people back in control of their [Personal Data] while creating value for organizations that process it ([Relying Parties]).
The document describes the functional, technical, privacy, security, legal and/or compliancy aspects of Qiy.


## 1.2 Readers' Guidance

* Privacy officers are advised to read chapters [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases) and [3 Qiy Architecture](#3-qiy-architecture).
* Security officers are advised to read chapters [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases) and [3 Qiy Architecture](#3-qiy-architecture).
* Information analysts are advised to read chapters [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases), [3 Qiy Architecture](#3-qiy-architecture), [4 Application Layer](#4-application-layer) and [5 Qiy Node Layer](#5-qiy-node-layer).
* Application developers are advised to read chapters [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases), [3 Qiy Architecture](#3-qiy-architecture), [4 Application Layer](#4-application-layer) and [5 Qiy Node Layer](#5-qiy-node-layer).
* Systems engineers are advised to read chapters [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases), [3 Qiy Architecture](#3-qiy-architecture) and [6 Routing Layer](#6-routing-layer).


## 1.3 Overview

This document has the following chapters:
* [1 Introduction](#1-introduction) - this chapter - describes the purpose, contents, structure and use of this document.
* [2 High-Level Qiy Use Cases](#2-high-level-qiy-use-cases) describes some of the high-level [Use Cases] that Qiy addresses.
* [3 Qiy Architecture](#3-qiy-architecture) provides a brief description of the key Qiy concepts, layers and components.
* [4 Application Layer](#4-application-layer) describes the [Application Layer].
* [5 Qiy Node Layer](#5-qiy-node-layer) describes the [Qiy Node Layer].
* [6 Routing Layer](#6-routing-layer) describes the [Routing Layer].


## 1.4 Terminology

Please refer to [Definitions](./Definitions.md) for a description of the meaning of the used terms.


# 2 High-Level Qiy Use Cases

This chapter describes the main use cases that put individual persons ([Individuals]) in control of their [Personal Data] that are kept by organizations ([Data Providers]) and create value for organizations that process it ([Relying Parties]).

Qiy achieves this with the help of the [Qiy Trust Network] and [Consents]. The [Qiy Trust Network] is a [Technology Service] which allows individuals and organizations to connect and interact under the rules of the [Qiy Scheme]. The organizations that provide this service ([Access Providers]) can only do so under the same rules.
[Relying Party] can only get Personal Data with the [Consent] of the [Data Subject].

Hence the main use cases:

* [Data Provider] joins Qiy (see [example flow](Functional%20Specification.md#31-setup)).
* [Individual] starts using Qiy  (see [example flow](Functional%20Specification.md#41-setup)).
* [Relying Party] joins Qiy  (see [example flow](Functional%20Specification.md#51-setup)).
* [Individual] connects with [Data Provider]  (see [example flow](Functional%20Specification.md#42-data-reuse)).
* [Individual] connects with [Relying Party]  (see [example flow](Functional%20Specification.md#42-data-reuse)).
* [Individual] consents to the use of his data by a [Relying Party] (see [example flow](Functional%20Specification.md#42-data-reuse)).
* [Relying Party] gets [Personal Data] (see [example flow](Functional%20Specification.md#52-data-reuse)).

Please refer to the [Functional Specification](Functional%20Specification.md) for more information.


# 3 Qiy Architecture
This chapter describes the [Qiy Architecture]: the entities and their interrelations, which are involved in online communication and transactions. 

The capabilities of the architecture will be illustrated using a limited real-life [Qiy Scheme] web scenario. The rest of the chapter addresses the rationale behind the architecture: why it has been designed the way it has been designed and how it relates to the [Qiy Trust Principles] proclaimed by the [Qiy Foundation].
## 3.1 Basic Qiy Concepts
### 3.1.1 Qiy Node
The [Qiy Node] is a delegate component for Applications. The [Qiy Node] is responsible for [Connection] management of global addresses, [Connections], [Key Management], and cryptographic transformations of messages and implements the [Connection] to the [Qiy Infrastructure].
### 3.1.2 Global Addresses
Like e-mail addresses, you can send messages using the [Qiy Infrastructure] to a [Qiy Node] by sending messages to the address. Unlike e-mail addresses however, [Users] have many different [Qiy Node] addresses, as each [Connection] should use their own unique address. Qiy uses globally unique addresses (based on the [Domain Name System]) in order to route [Connections] and deliver their messages over the [Qiy Infrastructure]. 
### 3.1.3 Persistent Connections
Upon fulfillment of the preconditions, a [Qiy Node] has a long-lived [Connection] with another [Qiy Node], which enables the [Users] controlling the connected [Qiy Nodes] to send and receive a potentially unlimited number of messages over the [Connection]. Such a [Connection] can be used to engage in a-synchronous structured [Request]-response interactions, in close to real time and real time [Data] streaming.
### 3.1.4 Structured data
The basic protocol [Data] unit in Qiy is not a [Connection] (which simply provides the transport for point-to-point communication) but a Qiy Message, which is essentially [Data] or a fragment of [Data] that is sent over a [Connection]. 

After two [Qiy Nodes] have completed the [Connection] negotiation, either party can send messages. A message contains the following parts:
* [Connection] information
* [Consent] information
* Application [Data].

[Connection] information

[Connection] information refers to the global address of a [Qiy Node] and [Connection]-[Tokens], intended to route messages, and information used during the [Connection] negotiation like session keys.

[Consent] information

Per the [Qiy Trust Principles], [Data] may only be used with the [User]'s permission only. [Consent] describes how an [Individual] allows his [Data] to be used by a [Relying Party] in the [Qiy Scheme]. [Consent] specifies the permissions that are applied to a certain set of [Data] for a specific [Relying Party]. 

[Consent] specifies at least the following parameters:
* What [Data] the [Consent] is applied to
* How many times the [Data] may be accessed (e.g. single time only, or unlimited times)
* For what period of time the requesting party may access the [Data] (e.g. an hour, or a year)
* The purpose for which the [Consent] was given (e.g. to deliver your order to your home address, or to give you financial advice).

The [Data Provider] initiates the [Consent Request] to the [Orchestrator], where the [Consent Request] contains a clear human readable purpose declaration.

Application [Data]

Application [Data] can be considered as the message payload after the [Connection] is established. Applications are free to declare and implement namespaces to structure [Data] elements and [Attributes] of [Data] contained in a message payload. 

The assessment of the quality of [Data] received by a [Relying Party] and the trustworthiness of the [Data] is at the discretion of the [Relying Party] and depends on the [Data Provider] reputation and relation to that [Relying Party]. For this purpose the Application [Data] contains metadata identifying the asserting [Data Provider] and the level of assurance of the [Connection] between [Data Provider] and [Orchestrator].

### 3.1.5 Distributed network of Nodes and [Routers]
In practice, the [Qiy Infrastructure] consists of a network of [Routers] and [Qiy Nodes] that inter-communicate. Important design considerations are:
* [Qiy Nodes] only communicate with the [Router] where they are registered
* [Qiy Nodes] only communicate with [Routers] that are licensed by the [Qiy Authority]
* [Routers] only communicate with [Qiy Nodes] they [Trust]; i.e. have registered
* [Routers] only communicate with routers that are licensed by the [Qiy Authority].

## 3.2 Protocol Layering
The [Qiy Standard] uses protocol layering to simplify the designs by dividing them into functional layers, and assigning protocols to perform each layer's task. The [Qiy Standard] divides the protocols into three virtual layers:

1. [Application Layer]: consists of applications and/or [Services], which deliver trustful [Services] to end [Users] and/or businesses
2. [Qiy Node Layer]: consists of [Qiy Nodes] representing [Users], the layer is responsible for among other things [Consent Management], [Key Management], [Session Management] and [Connection Management]
3. [Routing Layer]: consist of [Routers] responsible for routing messages between [Qiy Nodes].

Each layer provides [Services] to the next-higher layer and shields the upper layer from the details of how the [Services] below it are actually implemented. At the same time, each entity in a layer appears to be in direct communication with other entities.


![Example configuration of applications, nodes and routers](./images/example-configuration-of-applications-nodes-and-routers.png)

    Diagram 3-1 Example configuration of applications, [Qiy Nodes] and routers

### 3.2.1 Layer responsibilities
The [Application Layer] responsibilities are:
1. Provide an Interface for the [User]
2. Out of band Application interface
3. Authentication of the [User]
4. [Data] interpretation and processing
5. [Policy Enforcement Point].

The [Qiy Node Layer] responsibilities are:
1. [Application Management] - What Applications are linked to the [Qiy Node] and what are their capabilities
2. Messaging - Persist, deliver and delegate messages (from/to an Application or a [Qiy Node])
3. [Consent Management] - Manage the 'Pass by reference register' (who may access what [Data], and when does the permission expire)
4. [Connection Management] - Manage the [Connections] with other [Qiy Nodes]
5. Key management
6. Preferences and settings.

The responsibilities of the [Routing Layer] are:
1. Registering a [Qiy Node]
2. Authenticating a [Qiy Node]
3. Creating a Route between [Qiy Nodes]
4. Message routing.
### 3.2.2 Layer constraints
The configuration illustrates some of the major constraints of the [Qiy Architecture]:
1. [Users] can use one or more Applications to communicate and interact
2. Each Application is connected to the [Qiy Node] of the [User]
3. Each [Qiy Node] is connected to one [Router]
4. Each [Router] can be connected to one or more [Qiy Nodes]
5. Each [Router] can be connected to one or more other [Routers].
## 3.3 Privacy in Qiy
In designing and developing the [Qiy Scheme], privacy by design is default. This refers to both a [User]'s ability to control how their [Personal Data] is shared and used, and to mechanisms that inhibit their actions at multiple participants from being inappropriately correlated. 

Qiy has a number of mechanisms that support deployment in privacy:
* Qiy implements an indirect routing strategy. When a [Qiy Node] sends a message to another [Qiy Node], that message is send to the [Router] the sending [Qiy Node] is registered at. The receiving [Router] forwards the message to the [Router] the destination [Qiy Node] is registered at. Routing tables hold only information to forward to the next hop
* Qiy supports the establishment of [Pseudonyms] established between an [Orchestrator] and other [Users] ([Relying Party] and [Data Provider]). Such [Pseudonyms] do not themselves enable inappropriate correlation between [Relying Parties] and [Data Providers] (as would be possible if the [Qiy Node] asserted the same [Identifier] for a [User] to every other [User], a so-called global address)
* Qiy supports one-time or transient [Identifiers] ' such [Identifiers] ensure that every time a certain [Orchestrator] establishes a connector with a given [Relying Party] or [Data Provider], that party will be unable to recognize them as the same [Orchestrator] that might have previously visited them (based solely on the [Identifier], correlation may be possible through non-Qiy [Data]).

## 3.4 Security in Qiy
How can the [Relying Party] [Trust] information being exchanged' In addition, what prevents a 'man-in-the-middle' attack that might grab information to be illicitly 'replayed' at a later date' These and many more security considerations are discussed in detail in the [Qiy Security and Privacy Considerations Specification]. 

Qiy defines a number of security mechanisms to detect and protect against such attacks. The primary mechanism is for the [Orchestrator] and the [Data Provider] and [Relying Party] to have a pre-existing [Trust] relationship which typically relies on a [Public Key Infrastructure] (PKI). A general overview of what is recommended is provided below:
* All communication between a [Qiy Node] and a [Router] and between [Routers] use the TLS protocol
* To prevent old communications to be reused in replay attacks, use of nonces is recommended. A nonce is an arbitrary number that may only be used once. To ensure that a nonce can only be used once, it should be time-variant (including a suitably fine-grained timestamp in its value), or generated with enough random bits to ensure a probabilistically insignificant chance of repeating a previously generated value. 
* Communication between [Qiy Nodes] is encrypted using symmetric encryption. 
During the [Connection] negotiation all messages between a [Qiy Node] and a [Router] and between [Routers] are digitally signed to ensure that the content of the message cannot be altered during this stage.

# 4 Application Layer
This chapter is describing the [Application Layer]. While all other components of the [Qiy Infrastructure] are generic, Applications allow for specific behavior. The Application is what differentiates a web shop from a bank. 

![Application context diagram](./images/application-context-diagram.png)

    Diagram 4-1 Application context diagram

A [Qiy Node] may use multiple Applications; each specialized in a specific behavior, together enabling their [User] with a multitude of behaviors. Each Application instance is however always only connected to one [Qiy Node]. 
## 4.1 Application Messages
Once a [Connection] between [Qiy Nodes] has been made, Applications can use it to exchange messages. The actual content of these messages are meaningful for the Applications, but is out of scope for the [Qiy Standard]. 

To exchange information an Application must communicate:
* Definition of the format of the message, i.e. how the message can be understood by another Application protocol
* What the message is about is that are terms understandable for an [Individual] (used for consent messages)
* The meaningful content itself (also referred to as 'payload').

The Application may use an interface on the [Qiy Node] that supports encryption to protect the message from prying eyes, but the message itself should be transmitted plaintext.
Each message that an Application constructs will be sent to a [Qiy Node]; each message that a [Qiy Node] receives will be handled by an Application. Communication between Applications is indirect: multiple Applications may be able to respond to any message, it is up to the [User] to decide which one will actually handle the message.
## 4.2 Responsibilities
The responsibilities of the [Application Layer] are stated in 3.2.1. Each of the following sections in this chapter will handle one. For convenience they are repeated here:

1. Interface for the [User]
2. Out-of-band Application interface
3. Authentication of the [User]
4. [Data] interpretation and processing
5. [Policy Enforcement Point].
### 4.2.1 Interface for the User
Only Applications are allowed to interface with the [Qiy Node] and as such, the Application acts as an interface on the [Qiy Node] for the [User]. If the [User] is an automated system, this interface will be an API. If the [User] is human, the interface will be a (G)UI. Separate Applications may provide parts of the interface, e.g. by only reacting on a subset of all [Data] received by the [Qiy Node].
### 4.2.2 Out-of-band Application interface
When the [User] wants to set-up a [Connection] with another [User], the initiating party uses an Application to present a [Connect Token]. The Application does this by requesting the information required from the [Qiy Node] and converting that to the presentable form. 
Some Application of the other [User] must be able to receive the [Token] and forward it to the other [User]'s [Qiy Node]. 

The [Connect Token] should not be transmitted via the [Qiy Infrastructure], i.e for security reasons there must be out-of-band communication of the [Connect Token].
In the [Use Case] of the [Individual] as a [Data Provider], this is done by Webshop.com by displaying a QR code on their website (the Application) and Alice's Application scanning it, using the air as a transport medium. 
### 4.2.3 Authentication of the User
As the [Application Layer] is the main interface for the [User], it needs to ensure that the [User] accessing the Application is who he claims he is.
### 4.2.4 Data interpretation and processing
As a [Qiy Node] is generic, it is left up to the Application to provide meaning to the received messages. Depending on the protocol a specific Application may or may not be able to provide this meaning. Furthermore, once the meaning is given, the Application may be able to do further processing on the message. 

For example: in the 'Individual as Data Provider' [Use Case], this is done by Alice's Application on her phone. When Webshop.com sends a question to Alice's [Qiy Node], the Application is able to see that Alice needs to answer it herself. The Application processes the message and presents it in a form, which Alice can understand and respond to.
### 4.2.5 Policy Enforcement Point
If an Application is a [Data Provider], it should check the validity of the [Data] [Request] on each invocation, i.e. whenever giving out [Data] the Application should ensure that:
* The requesting party is allowed access to the [Data];
* The time-frame for which access was allowed has not expired;
* The number of times access was allowed has not been exceeded;
* The access has not been revoked.
## 4.3 Node Connection
The Application may connect to an existing [Qiy Node] or register a new [Qiy Node]. In each case the Application must provide the proper means for the [Qiy Node] to determine if the Application is authorized to do so. The Application must also provide the [Qiy Node] with a listing of the capabilities the Application has. This list defines the [Data] and [Services] that the Application can provide. The list takes the form of a list of protocols
## 4.4 Application Requirements
TBD

# 5 Qiy Node Layer
This chapter describes the [Qiy Node Layer], its responsibilities and how these are met.

![Node context diagram](./images/node-context-diagram.png)

    Diagram 5-1 [Qiy Node] context diagram

## 5.1 Responsibilities
The [Qiy Node Layer] responsibilities are:
1. [Application Management] - What Applications are linked to the [Qiy Node] and what are their capabilities
2. Messaging - Persist, deliver and delegate messages (from/to an Application or a [Qiy Node])
3. [Consent Management] - Manage the 'Pass by reference register' (who may access what [Data], and when does the permission expire)
4. [Connection Management] - Manage the [Connections] with other [Qiy Nodes]
5. Key management
6. Preferences and settings.

### 5.1.1 Application Management
Each [Qiy Node] maintains a registration of the connected Applications and acts as a registry for related information, such as the supported [Application Protocols].
#### 5.1.1.1 Application Authentication 
An Application can only connect with a [Qiy Node] and exchange messages via the [Qiy Infrastructure] when it has been authenticated by that [Qiy Node].
#### 5.1.1.2 Application Authorization
TBD

### 5.1.2 Messaging
A [Qiy Node] persists all the [Application Messages] it has received from and/or sent to other [Qiy Nodes] and assures and maintains the delivery status. 
The [Qiy Node] addresses outgoing [Application Messages] to the destination [Qiy Node]. [Application Messages] are delivered to the [Router]. It is the sending [Qiy Node]'s responsibility to ensure the confidentiality of the message by encrypting it in a way only the destination [Qiy Node] can decrypt.
The delivery of incoming [Application Messages] is based on the [Application Protocol]. Messages are delivered to a supporting Application. Which Application handles which message is determined either after [User] interaction or by using preference. [Data] [Requests] and responses are delivered in the same way, but only when they have been consented for.

### 5.1.3 Consent Management
All data exchanges are subject to [Consent Management]:
1. Incoming data requests (from other [Users]) for [Data] owned by the [Qiy Node]'s [User] are only accepted when the associated [Consent] is (or has previously been) accepted by the [User].
2. Incoming data requests for [Data] of [Users] other than the receiver or the sender are subject to the owner's [Consent]. 

The [Qiy Node] keeps track of all data requests, data responses, data notifications and [Consents].

### 5.1.4 Digital Identity
A [Qiy Node] represents a [User] in the digital realm and is as such his digital [Identity]. A [Qiy Node] can be addressed by any other [Qiy Node] using global addresses when a [Connection] has been established between the two. This [Connection] can be regarded as the digital equivalent of a relationship between two [Users], e.g. an [Individual] and a web shop.

### 5.1.5 Connection Management
The [Qiy Node] acts as a registry for its [Connections], the status and related information and provides means for their management. 

### 5.1.6 Key Management
The [Qiy Node] is responsible for the proper management of all the key pairs that are used to meet its responsibilities.
### 5.1.7 Preferences and Settings
 The [Qiy Node] can act as a registry for preferences and settings of sorts and provides means for their management.
## 5.2 Inter-Node Communication
A [Qiy Node] can only communicate another [Qiy Node] over a bi-directional communication channel (route), which is created when two [Users] establish a [Connection].
Please refer to Error! [Reference] source not found. Error! [Reference] source not found. for more information on establishing and using [Routes].
## 5.3 Router Connection
Only [Qiy Nodes] that fulfill the [Qiy Node Requirements] can establish a [Connection] with a [Router] and only with [Routers] that fulfill the [Router Requirements].
Please refer to chapter 6 [Routing Layer] for more information. 

## 5.4 Node Requirements
TBD


# 6 Routing Layer
This chapter is dedicated to the [Routing Layer].


![Router context diagram](./images/router-context-diagram.png)

    Diagram 6-1 [Router] context diagram

## 6.1 Route
The Route is a key principle ensuring the privacy of the [Qiy Nodes]. The archetypical Route is shown in the next diagram: 

![Archetypical Route](./images/archetypical-route.png)

    Diagram 6-2 Archetypical Route
	
In this Route, Qiy Node A has a unique address for this Route with Router A, which in turn publishes a unique address for this Route to both Qiy Node A and Router B. Router B in turn has its own unique address for this route, which it publishes to both Router A and Qiy Node B. No further information about the Route is given to each party. This ensures that Qiy Node A cannot know the [Identity] of Router B or Qiy Node B.
Likewise Qiy Node B cannot know the [Identity] of Router A or Qiy Node A. Router A cannot know Qiy Node B and Router B cannot know Qiy Node A. By splitting up the knowledge of the complete Route, the privacy of the [Qiy Nodes] is ensured.
## 6.2 Responsibilities
The [Routing Layer] responsibilities are:
1. Registering a [Qiy Node]
2. Authenticating a [Qiy Node]
3. Creating a Route between [Qiy Nodes]
4. Message routing.

### 6.2.1 Registering a Qiy Node
Any [Qiy Node] can only participate in the [Qiy Infrastructure] by using a [Router]. Each [Qiy Node] should only connect to one [Router]. In order to enable the [Qiy Node] to connect, the [Router] has to be made aware of its presence. To do this, the [Qiy Node] registers itself with the [Router]. In this process the [Qiy Node] and the [Router] exchange whatever information is required for the [Router] to Authenticate the [Qiy Node].

### 6.2.2 Authenticating a Qiy Node
It is the responsibility of the [Router] to ensure that any operation made on a [Qiy Node]'s behalf, can only be done by that [Qiy Node] and no other.

### 6.2.3 Creating a Route between Nodes
When creating a [Qiy Node], the design considerations from paragraph 3.1.5 should always be taken into account. The creation of a Route between Qiy Node A and Qiy Node B, initiated by Qiy Node A is realized in the following steps:

1. Qiy Node A [Requests] a notification on a unique address (a) from Router A on a coming event
2. Router A provides Qiy Node A with a unique address (b) to trigger the event
3. Qiy Node A uses the unique address (b) in a [Connect Token] which it advertises
4. Qiy Node B picks up the [Connect Token], creates a unique address (c)
5. Qiy Node B provides Router B with unique address (c) and (b), the latter of which it got from the [Connect Token]
6. Router B creates a unique address (d), which it associates with Qiy Node B's unique address (c)
7. Router B triggers the event by calling (b) on Router A, with (d) as a parameter
8. Router A creates a unique address (e) which it returns to Router B
9. Router B associates the partial Route (d)(c) with (e)
10. Router A calls (a) with parameter (e)
11. Qiy Node A creates a unique address (f), which it returns to Router A
12. Router A associates the partial Route (e)(d) with (f)
13. Qiy Node A associates (f) with (e).
14. The following Route has been created: (f)-(e)-(d)-(c)

Please note that Router A and Router B may be in fact the same entity. 

### 6.2.4 Message Routing

The [Routing Layer] is responsible for routing [Application Messages] between the [Qiy Nodes]. The [Application Messages] are passed along the Route. Each of the [Qiy Nodes] on the Route can use the Route to exchange messages. All the information a [Router] needs to pass on the message is its unique address within the Route and the layer where the sender resides. Given the example in the previous paragraph: 

* If Router A receives a message at address (e) and the sender is the [Qiy Node Layer], the message needs to be forwarded to (d)
* If Router A receives a message at address (e) and the sender is the [Routing Layer], the message needs to be forwarded to (f)

Only messages where a Route exists are processed.


