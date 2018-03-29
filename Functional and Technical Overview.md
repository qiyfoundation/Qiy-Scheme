# Functional and Technical Overview 'Qiy Scheme V1.0'


# Abstract

The [Qiy Scheme] is a set of agreements encompassing all necessary topics needed to realize the goals of the [Qiy Foundation]. The [Qiy Scheme] consists of the [Qiy Standard] for technical aspects and the [Qiy Scheme Rulebook] for governance aspects.

This document is produced by the [Work Stream Functionality] & Technology and intended for developers and architects who wish to design systems and applications that conform to the [Qiy Standard] of [Qiy Schem]e V1.0, which is the version released to the public in January 2015. 

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
		1. [[Qiy Node]](#311-[qiy-node])
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
2. 'High-Level Qiy Use Cases' describing some of the high-level [Use Cases] that Qiy addresses.
3. 'Qiy Architecture' providing a brief description of the key Qiy concepts, layers and components defined in the standard.
4. 'Application Layer' describing the [Application Layer] and containing references to related documentation.
5. 'Node Layer' describing the [Node Layer] and containing references to related documentation.
6. 'Routing Layer' describing the [Routing Layer] and containing references to related documentation.

## 1.2 Terminology
See [Definitions of the Qiy Scheme](./Definitions.md).

# 2 High-Level Qiy Use Cases

[Individuals] and organizations, including government organizations can be participants in the [Qiy Scheme] in different roles.

## 2.1 Qiy Participants

### Individuals
[Individuals] benefit from participating in the [Qiy Scheme], by gaining oversight and control over their personal information. By participating in the [Qiy Scheme] they can:
1. Know where their [Data] is
2. Access their [Data] at the source
3. Control who uses this [Data] and for what purpose
4. Re-use the [Data] to create insight and value for themselves, or to share with others
5. Re-use the [Data] with a vouch for its correctness from the party providing the [Data].

### Organizations 
While the benefits of the [Qiy Scheme] are obvious for [Individuals], organizations may benefit from participating as well. This includes government organizations, which can participate in the Scheme in a similar way as any other organization.

Organizations benefit in the following ways:
1. The quality of the [Data] is likely to be higher, as the [Individual] can keep it up to date himself, and only has to manage it in one location
2. Unnecessary [Data] replication is prevented, as [Data] can remain at the source
3. Organizations can make use of [Data] that is enriched with the vouch of another organization, increasing the correctness and hence value of the [Data] (if the vouching organization is trusted)
4. Lower costs to get quality and [Consent] based [Data]
5. Dynamic [Data]: subscribe to actual (and validated) [Data]
6. Get to know one's customer not by collecting, but by connecting.

## 2.2 Qiy Roles
In the [Qiy Scheme] different roles can be distinguished. A single organization may participate in the [Qiy Scheme] in more than one role. At a minimum, a transaction in the [Qiy Scheme] involves two [User] roles and their respective Routers.

![The roles in the Qiy Scheme](./images/the-roles-in-the-qiy-scheme.png)

    Diagram 2-1 The roles in the [Qiy Scheme]

### 2.2.1 Users
[Individuals] and organizations can participate in the [Qiy Scheme] in different roles. 

### Orchestrator
[Individuals] participate in the [Qiy Scheme] in the role of Orchestrator. The Orchestrator is represented in the [Qiy Scheme] by his [Node]. The Orchestrator is in control of his [Node] enabling him to decide how other participants will interact with him. The Orchestrator controls the relations with other participants and uses his [Node] to manage his [Consent] for who may use his [Data] for what purpose.

### Data Providers
[Data Providers] make [Data] accessible to other [Users] in the [Qiy Scheme]. A [Data Provider] can make [Data] available to an Orchestrator after he has established a [Connection] to the Orchestrator's [Node], so that the Orchestrator may use the [Data] for his personal use, or share it in an interaction with another [User]. If an Orchestrator has given [Consent], the [Data Provider] may also share [Data] with a [Relying Party] on behalf of the Orchestrator. These assertions typically supply the receiving party some [Personal Data] of the [Individual] that is necessary to perform a transaction. If an assertion is sent by a [Data Provider], he can enrich the metadata belonging to the [Data] with a vouch for correctness of the [Data]. The receiving party may value this vouch based on trust and reputation of the [Data Provider].
[Data Providers] will often be (government) organizations that have a relation with the Orchestrator. In some cases, an [Individual] can be a [Data Provider]; in this case the [Individual] will be the original source and the assertion that is given is not vouched for by any other [User].

### Relying Parties
A [Relying Party] is a [User] that relies on the [Trust Framework] to receive [Data] from an Orchestrator, typically for some kind of [Business Process]. To receive this [Data], it is required that the [Relying Party] establishes a [Connection] with the [Node] of an Orchestrator. In practice, [Relying Party] will often also participate as a [Data Provider], making the exchange with the Orchestrator possible in both ways.

### 2.2.2 Router
Router is the general term for [Service Providers] whose primary purpose is to [Connect] [Users] (respectively their [Nodes]) to the [Qiy Scheme]. Some [Service Providers] focus on offering [Connections] to [Users], others add additional [Services] to the primary [Service] of issuing [Nodes].

### 2.2.3 Scheme Authority
The [Qiy Scheme] is managed through an independent and international organization, called the [Scheme Authority]. At the national level, the implementation of the Scheme in that national market is delegated to a [Regional Authority]. At all times the independence of the [Scheme Authority] and its national 'branches' shall be warranted. Also, at all times the Scheme in its implementation shall be open and non-discriminatory. To ensure this, appropriate audits and sanctions will be in place at both the national and the international level.
The [Scheme Authority] and its national 'branches' set and enforce the rules and regulations and issue licenses to participants of the [Qiy Scheme].

The [Qiy Foundation] fulfils the role of [Scheme Authority].

## 2.3 Individual as Data Provider Use Case

### 2.3.1 Overview
In the following example, an [Individual] named Alice places an order from a web shop called Webshop.com.
To [Connect] with others on the [Qiy Infrastructure], Alice uses an app on her smartphone that enables her to scan QR codes to [Connect]. In her role as Orchestrator, Alice is in control of the process described in the [Use Case].
Webshop.com is an organization connected to the [Qiy Infrastructure] by their Router. To serve Alice, Webshop.com relies on information to be supplied by her using the [Qiy Infrastructure]; Webshop.com is a [Relying Party] in this [Use Case].

The processing sequence is as follows:
1. Alice visits the website of Webshop.com and puts an item in her shopping cart. 
2. Alice proceeds to the check out to purchase the item in her cart.
3. To further serve Alice, Webshop.com requests Alice to [Connect] so that Webshop.com may use Alice's [Data]. Webshop.com presents Alice with a [Connect Token] in the form of a QR code so that Alice can [Connect] with Webshop.com.
4. Using the app on her smartphone, Alice scans the QR code, establishing a [Connection] with the Webshop.com.
5. Alice can now share the necessary [Data] (e.g. name, delivery address, preferences, etc.) with Webshop.com and complete her order.

![The individual as a data provider](./images/the-individual-as-a-data-provider.png)

    Diagram 2-2 The [Individual] as a [Data Provider]

### 2.3.2 Zooming in
The [Individual] and the [Node]
Alice is represented in the [Qiy Scheme] by her personal [Node]. As an Orchestrator she interacts with her [Node] using one or more Applications. For the worked example, we assume that Alice uses an app on her smartphone that can interact with her [Node]. This app also enables Alice to [Connect] with other parties that participate in the [Qiy Scheme], such as Webshop.com in this example.

Advertising the [Connect Token]
Alice can visit the website of Webshop.com and put items in her cart without having to identify herself to Webshop.com. To complete the order however, Webshop.com requires some information about Alice; e.g. her real name and her address. To acquire this information using Qiy, Webshop.com invites Alice to [Connect] them. To establish a [Connection] with her [Node], Webshop.com generates a [Connect Token] and presents it out-of-band. In this example, the [Connect Token] is presented as a QR code that can be scanned using an appropriate app. The [Connect Token] contains the information necessary for the app to establish a [Connection] with Webshop.com. Alice scans this code using the app on her phone.

Establishing a [Connection]
Using the [Connect Token], the app establishes a secure, encrypted [Connection] between Alice's [Node] and the [Node] of Webshop.com via the Routers. Once this route has been established, Alice and Webshop.com may exchange [Data] through the [Qiy Infrastructure]. All [Data] transmitted over this [Connection] is shielded from other parties in between, i.e. the Routers only forward the [Data] to the destination [Node], but cannot read the contents of the [Messages] they are passing along.

[Data] exchange
The route between Alice's [Node] and Webshop.com can be used to securely exchange information; Alice is, as the Orchestrator, in control over what [Data] will or will not be shared with [Relying Parties] connected to her [Qiy Node].
To complete Alice's order, Webshop.com requests the address where her order should be shipped to. Alice acts as a [Data Provider] and supplies this input herself. Webshop.com may then complete the order based on the [Data] Alice has shared.
# 3 Qiy Architecture
This chapter describes the [Qiy Architecture]: the entities and their interrelations, which are involved in online communication and transactions. 

The capabilities of the architecture will be illustrated using a limited real-life [Qiy Scheme] web scenario. The rest of the chapter addresses the rationale behind the architecture: why it has been designed the way it has been designed and how it relates to the [Qiy Principles] proclaimed by the [Qiy Foundation].
## 3.1 Basic Qiy Concepts
### 3.1.1 [Qiy Node]
The [Qiy Node] is a delegate component for Applications. The [Node] is responsible for [Connection] management of global addresses, [Connections], [Key Management], and cryptographic transformations of [Messages] and implements the [Connection] to the [Qiy Infrastructure].
### 3.1.2 Global Addresses
Like e-mail addresses, you can send [Messages] using the [Qiy Infrastructure] to a [Qiy Node] by sending [Messages] to the address. Unlike e-mail addresses however, [Users] have many different [Qiy Node] addresses, as each [Connection] should use their own unique address. Qiy uses globally unique addresses (based on the [Domain Name System]) in order to route [Connections] and deliver their [Messages] over the [Qiy Infrastructure]. 
### 3.1.3 Persistent Connections
Upon fulfillment of the preconditions, a [Qiy Node] has a long-lived [Connection] with another [Qiy Node], which enables the [Users] controlling the connected [Nodes] to send and receive a potentially unlimited number of [Messages] over the [Connection]. Such a [Connection] can be used to engage in a-synchronous structured request-response interactions, in close to real time and real time [Data] streaming.
### 3.1.4 Structured data
The basic protocol [Data] unit in Qiy is not a [Connection] (which simply provides the transport for point-to-point communication) but a [Qiy Message], which is essentially [Data] or a fragment of [Data] that is sent over a [Connection]. 

After two [Qiy Nodes] have completed the [Connection] negotiation, either party can send [Messages]. A [Message] contains the following parts:
* [Connection] information
* [Consent] information
* [Application Data].
[Connection] information
[Connection] information refers to the global address of a [Qiy Node] and [Connection]-[Tokens], intended to route [Messages], and information used during the [Connection] negotiation like session keys.
[Consent] information
Per the [Qiy Principles], [Data] may only be used with the [User]'s permission only. [Consent] describes how an [Individual] allows his [Data] to be used by a [Relying Party] in the [Qiy Scheme]. [Consent] specifies the permissions that are applied to a certain set of [Data] for a specific [Relying Party]. 

[Consent] specifies at least the following parameters:
* What [Data] the [Consent] is applied to
* How many times the [Data] may be accessed (e.g. single time only, or unlimited times)
* For what period of time the requesting party may access the [Data] (e.g. an hour, or a year)
* The purpose for which the [Consent] was given (e.g. to deliver your order to your home address, or to give you financial advice).

The [Data Provider] initiates the [Consent Request] to the Orchestrator, where the [Consent Request] contains a clear human readable purpose declaration.
Application [Data]
Application [Data] can be considered as the [Message] payload after the [Connection] is established. Applications are free to declare and implement namespaces to structure [Data] elements and attributes of [Data] contained in a [Message] payload. 

The assessment of the quality of [Data] received by a [Relying Party] and the trustworthiness of the [Data] is at the discretion of the [Relying Party] and depends on the [Data Provider] reputation and relation to that [Relying Party]. For this purpose the Application [Data] contains metadata identifying the asserting [Data Provider] and the level of assurance of the [Connection] between [Data Provider] and Orchestrator.
### 3.1.5 Distributed network of Nodes and Routers
In practice, the [Qiy Infrastructure] consists of a network of Routers and [Nodes] that inter-communicate. Important design considerations are:
* [Nodes] only communicate with the Router where they are registered
* [Nodes] only communicate with Routers that are licensed by the [Qiy Authority]
* Routers only communicate with [Qiy Nodes] they trust; i.e. have registered
* Routers only communicate with routers that are licensed by the [Qiy Authority].
## 3.2 Protocol Layering
The [Qiy Standard] uses protocol layering to simplify the designs by dividing them into functional layers, and assigning protocols to perform each layer's task. The [Qiy Standard] divides the protocols into three virtual layers:

1. [Application Layer]: consists of applications and/or [Services], which deliver trustful [Services] to end [Users] and/or businesses
2. [Node Layer]: consists of [Nodes] representing [Users], the layer is responsible for among other things [Consent Management], [Key Management], [Session Management] and [Connection Management]
3. [Routing Layer]: consist of Routers responsible for routing [Messages] between [Nodes].

Each layer provides [Services] to the next-higher layer and shields the upper layer from the details of how the [Services] below it are actually implemented. At the same time, each entity in a layer appears to be in direct communication with other entities.


![Example configuration of applications, nodes and routers](./images/example-configuration-of-applications-nodes-and-routers.png)

    Diagram 3-1 Example configuration of applications, [Nodes] and routers

### 3.2.1 Layer responsibilities
The [Application Layer] responsibilities are:
1. Provide an Interface for the [User]
2. Out of band Application interface
3. Authentication of the [User]
4. [Data] interpretation and processing
5. [Policy Enforcement Point].

The [Node Layer] responsibilities are:
1. [Application Management] - What Applications are linked to the [Node] and what are their capabilities
2. [Application Messaging] - Persist, deliver and delegate [Messages] (from/to an Application or a [Node])
3. [Consent Management] - Manage the 'Pass by reference register' (who may access what [Data], and when does the permission expire)
4. [Connection Management] - Manage the [Connections] with other [Nodes]
5. Key management
6. Preferences and settings.

The responsibilities of the [Routing Layer] are:
1. Registering a [Node]
2. Authenticating a [Node]
3. Creating a Route between [Nodes]
4. [Message] routing.
### 3.2.2 Layer constraints
The configuration illustrates some of the major constraints of the [Qiy Architecture]:
1. [Users] can use one or more Applications to communicate and interact
2. Each Application is connected to the [Node] of the [User]
3. Each [Node] is connected to one Router
4. Each Router can be connected to one or more [Nodes]
5. Each Router can be connected to one or more other Routers.
## 3.3 Privacy in Qiy
In designing and developing the [Qiy Scheme], privacy by design is default. This refers to both a [User]'s ability to control how their [Personal Data] is shared and used, and to mechanisms that inhibit their actions at multiple participants from being inappropriately correlated. 

Qiy has a number of mechanisms that support deployment in privacy:
* Qiy implements an indirect routing strategy. When a [Node] sends a [Message] to another [Node], that [Message] is send to the Router the sending [Node] is registered at. The receiving Router forwards the [Message] to the Router the destination [Node] is registered at. Routing tables hold only information to forward to the next hop
* Qiy supports the establishment of pseudonyms established between an Orchestrator and other [Users] ([RelyingParty] and [Data Provider]). Such pseudonyms do not themselves enable inappropriate correlation between [Relying Parties] and [Data Providers] (as would be possible if the [Node] asserted the same identifier for a [User] to every other [User], a so-called global address)
* Qiy supports one-time or transient identifiers ' such identifiers ensure that every time a certain Orchestrator establishes a connector with a given [Relying Party] or [Data Provider], that party will be unable to recognize them as the same Orchestrator that might have previously visited them (based solely on the identifier, correlation may be possible through non-Qiy [Data]).

## 3.4 Security in Qiy
How can the [Relying Party] trust information being exchanged' In addition, what prevents a 'man-in-the-middle' attack that might grab information to be illicitly 'replayed' at a later date' These and many more security considerations are discussed in detail in the [Qiy Security and Privacy Considerations Specification]. 

Qiy defines a number of security mechanisms to detect and protect against such attacks. The primary mechanism is for the Orchestrator and the [Data Provider] and [Relying Party] to have a pre-existing trust relationship which typically relies on a [Public Key Infrastructure] (PKI). A general overview of what is recommended is provided below:
* All communication between a [Node] and a Router and between Routers use the TLS protocol
* To prevent old communications to be reused in replay attacks, use of nonces is recommended. A nonce is an arbitrary number that may only be used once. To ensure that a nonce can only be used once, it should be time-variant (including a suitably fine-grained timestamp in its value), or generated with enough random bits to ensure a probabilistically insignificant chance of repeating a previously generated value. 
* Communication between [Nodes] is encrypted using symmetric encryption. 
During the [Connection] negotiation all [Messages] between a [Node] and a Router and between Routers are digitally signed to ensure that the content of the [Message] cannot be altered during this stage.

# 4 Application Layer
This chapter is describing the [Application Layer]. While all other components of the [Qiy Infrastructure] are generic, Applications allow for specific behavior. The Application is what differentiates a web shop from a bank. 

![Application context diagram](./images/application-context-diagram.png)

    Diagram 4-1 Application context diagram

A [Node] may use multiple Applications; each specialized in a specific behavior, together enabling their [User] with a multitude of behaviors. Each Application instance is however always only connected to one [Node]. 
## 4.1 Application Messages
Once a [Connection] between [Nodes] has been made, Applications can use it to exchange [Messages]. The actual content of these [Messages] are meaningful for the Applications, but is out of scope for the [Qiy Standard]. 

To exchange information an Application must communicate:
* Definition of the format of the [Message], i.e. how the [Message] can be understood by another Application protocol
* What the [Message] is about is that are terms understandable for an [Individual] (used for [Consent] [Messages])
* The meaningful content itself (also referred to as 'payload').

The Application may use an interface on the [Node] that supports encryption to protect the [Message] from prying eyes, but the [Message] itself should be transmitted plaintext.
Each [Message] that an Application constructs will be sent to a [Node]; each [Message] that a [Node] receives will be handled by an Application. Communication between Applications is indirect: multiple Applications may be able to respond to any [Message], it is up to the [User] to decide which one will actually handle the [Message].
## 4.2 Responsibilities
The responsibilities of the [Application Layer] are stated in 3.2.1. Each of the following sections in this chapter will handle one. For convenience they are repeated here:

1. Interface for the [User]
2. Out-of-band Application interface
3. Authentication of the [User]
4. [Data] interpretation and processing
5. [Policy Enforcement Point].
### 4.2.1 Interface for the User
Only Applications are allowed to interface with the [Node] and as such, the Application acts as an interface on the [Node] for the [User]. If the [User] is an automated system, this interface will be an API. If the [User] is human, the interface will be a (G)UI. Separate Applications may provide parts of the interface, e.g. by only reacting on a subset of all [Data] received by the [Node].
### 4.2.2 Out-of-band Application interface
When the [User] wants to set-up a [Connection] with another [User], the initiating party uses an Application to present a [Connect Token]. The Application does this by requesting the information required from the [Node] and converting that to the presentable form. 
Some Application of the other [User] must be able to receive the [Token] and forward it to the other [User]'s [Node]. 

The [Connect Token] should not be transmitted via the [Qiy Infrastructure], i.e for security reasons there must be out-of-band communication of the [Connect Token].
In the [Use Case] of the [Individual] as a [Data Provider], this is done by Webshop.com by displaying a QR code on their website (the Application) and Alice's Application scanning it, using the air as a transport medium. 
### 4.2.3 Authentication of the User
As the [Application Layer] is the main interface for the [User], it needs to ensure that the [User] accessing the Application is who he claims he is.
### 4.2.4 Data interpretation and processing
As a [Node] is generic, it is left up to the Application to provide meaning to the received [Messages]. Depending on the protocol a specific Application may or may not be able to provide this meaning. Furthermore, once the meaning is given, the Application may be able to do further processing on the [Message]. 

For example: in the 'Individual as Data Provider' [Use Case], this is done by Alice's Application on her phone. When Webshop.com sends a question to Alice's [Node], the Application is able to see that Alice needs to answer it herself. The Application processes the [Message] and presents it in a form, which Alice can understand and respond to.
### 4.2.5 Policy Enforcement Point
If an Application is a [Data Provider], it should check the validity of the [Data] request on each invocation, i.e. whenever giving out [Data] the Application should ensure that:
* The requesting party is allowed access to the [Data];
* The time-frame for which access was allowed has not expired;
* The number of times access was allowed has not been exceeded;
* The access has not been revoked.
## 4.3 Node Connection
The Application may [Connect] to an existing [Node] or register a new [Node]. In each case the Application must provide the proper means for the [Node] to determine if the Application is authorized to do so. The Application must also provide the [Node] with a listing of the capabilities the Application has. This list defines the [Data] and [Services] that the Application can provide. The list takes the form of a list of protocols
## 4.4 Application Requirements
[TBD]

# 5 Node Layer
This chapter describes the [Node Layer], its responsibilities and how these are met.

![Node context diagram](./images/node-context-diagram.png)

    Diagram 5-1 [Node] context diagram

## 5.1 Responsibilities
The [Node Layer] responsibilities are:
1. [Application Management] - What Applications are linked to the [Node] and what are their capabilities
2. [Application Messaging] - Persist, deliver and delegate [Messages] (from/to an Application or a [Node])
3. [Consent Management] - Manage the 'Pass by reference register' (who may access what [Data], and when does the permission expire)
4. [Connection Management] - Manage the [Connections] with other [Nodes]
5. Key management
6. Preferences and settings.
### 5.1.1 Application Management
Each [Node] maintains a registration of the connected Applications and acts as a registry for related information, such as the supported [Application Protocols].
#### 5.1.1.1 Application Authentication 
An Application can only [Connect] with a [Node] and exchange [Messages] via the [Qiy Infrastructure] when it has been authenticated by that [Node].
#### 5.1.1.2 Application Authorization
[TBD]
### 5.1.2 Application Messaging
A [Node] persists all the application [Messages] it has received from and/or sent to other [Nodes] and assures and maintains the delivery status. 
The [Node] addresses outgoing application [Messages] to the destination [Node]. [Application Messages] are delivered to the Router. It is the sending [Node]'s responsibility to ensure the confidentiality of the [Message] by encrypting it in a way only the destination [Node] can decrypt.
The delivery of incoming application [Messages] is based on the [Application Protocol]. [Messages] are delivered to a supporting Application. Which Application handles which [Message] is determined either after [User] interaction or by using preference. [Data] requests and responses are delivered in the same way, but only when they have been consented for.
### 5.1.3 Consent Management
 All [Data] exchanges are subject to [Consent] management:
1. [Incoming Data Requests] (from other [Users]) for [Data] owned by the [Node]'s [User] are only accepted when the associated [Consent] is (or has previously been) accepted by the [User].
2. [Incoming Data Requests] for [Data] of [Users] other than the receiver or the sender are subject to the owner's [Consent]. 

The [Node] keeps track of all [Data Requests], [Data Responses], [Data Notifications] and [Consents].
### 5.1.4 Digital Identity
A [Node] represents a [User] in the digital realm and is as such his [Digital Identity]. A [Node] can be addressed by any other [Node] using global addresses when a [Connection] has been established between the two. This [Connection] can be regarded as the digital equivalent of a relationship between two [Users], e.g. an [Individual] and a web shop.
### 5.1.5 Connection Management
The [Node] acts as a registry for its [Connections], the status and related information and provides means for their management. 
### 5.1.6 Key Management
The [Node] is responsible for the proper management of all the key pairs that are used to meet its responsibilities.
### 5.1.7 Preferences and Settings
 The [Node] can act as a registry for preferences and settings of sorts and provides means for their management.
## 5.2 Inter-Node Communication
A [Node] can only communicate another [Node] over a bi-directional communication channel (route), which is created when two [Users] establish a [Connection].
Please refer to Error! Reference source not found. Error! Reference source not found. for more information on establishing and using [Routes].
## 5.3 Router Connection
Only [Nodes] that fulfill the [Node Requirements] can establish a [Connection] with a Router and only with Routers that fulfill the [Router Requirements].
Please refer to chapter 6 [Routing Layer] for more information. 
## 5.4 Node Requirements
[TBD]


# 6 Routing Layer
This chapter is dedicated to the [Routing Layer].


![Router context diagram](./images/router-context-diagram.png)

    Diagram 6-1 Router context diagram

## 6.1 Route
The Route is a key principle ensuring the privacy of the [Nodes]. The archetypical Route is shown in the next diagram: 

![Archetypical Route](./images/archetypical-route.png)

    Diagram 6-2 [Archetypical Route]
	
In this Route, [Node] A has a unique address for this Route with Router A, which in turn publishes a unique address for this Route to both [Node] A and Router B. Router B in turn has its own unique address for this route, which it publishes to both Router A and [Node] B. No further information about the Route is given to each party. This ensures that [Node] A cannot know the identity of Router B or [Node] B.
Likewise [Node] B cannot know the identity of Router A or [Node] A. Router A cannot know [Node] B and Router B cannot know [Node] A. By splitting up the knowledge of the complete Route, the privacy of the [Nodes] is ensured.
## 6.2 Responsibilities
The [Routing Layer] responsibilities are:
1. Registering a [Node]
2. Authenticating a [Node]
3. Creating a Route between [Nodes]
4. [Message] routing.
### 6.2.1 Registering a Node
Any [Node] can only participate in the [Qiy Infrastructure] by using a Router. Each [Node] should only [Connect] to one Router. In order to enable the [Node] to [Connect], the Router has to be made aware of its presence. To do this, the [Node] registers itself with the Router. In this process the [Node] and the Router exchange whatever information is required for the Router to Authenticate the [Node].
### 6.2.2 Authenticating a Node
It is the responsibility of the Router to ensure that any [Operation] made on a [Node]'s behalf, can only be done by that [Node] and no other.
### 6.2.3 Creating a Route between Nodes
When creating a [Node], the design considerations from paragraph 3.1.5 should always be taken into account. The creation of a Route between [Node] A and [Node] B, initiated by [Node] A is realized in the following steps:

1. [Node] A requests a notification on a unique address (a) from Router A on a coming event
2. Router A provides [Node] A with a unique address (b) to trigger the event
3. [Node] A uses the unique address (b) in a [Connect Token] which it advertises
4. [Node] B picks up the [Connect Token], creates a unique address (c)
5. [Node] B provides Router B with unique address (c) and (b), the latter of which it got from the [Connect Token]
6. Router B creates a unique address (d), which it associates with [Node] B's unique address (c)
7. Router B triggers the event by calling (b) on Router A, with (d) as a parameter
8. Router A creates a unique address (e) which it returns to Router B
9. Router B associates the partial Route (d)(c) with (e)
10. Router A calls (a) with parameter (e)
11. [Node] A creates a unique address (f), which it returns to Router A
12. Router A associates the partial Route (e)(d) with (f)
13. [Node] A associates (f) with (e).
14. The following Route has been created: (f)-(e)-(d)-(c)

Please note that Router A and Router B may be in fact the same entity. 

### 6.2.4 Message Routing

The [Routing Layer] is responsible for routing [Application Messages] between the [Nodes]. The [Application Messages] are passed along the Route. Each of the [Nodes] on the Route can use the Route to exchange [Messages]. All the information a Router needs to pass on the [Message] is its unique address within the Route and the layer where the sender resides. Given the example in the previous paragraph: 

* If Router A receives a [Message] at address (e) and the sender is the [Node] layer, the [Message] needs to be forwarded to (d)
* If Router A receives a [Message] at address (e) and the sender is the Routing layer, the [Message] needs to be forwarded to (f)

Only [Messages] where a Route exists are processed.


