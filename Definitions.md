# Definitions of the Qiy Scheme


## Abstract

The [Qiy Scheme](#qiy-scheme) defines a framework for [Individuals](#individual) and [Entities](#entity) to safely control and exchange [Personal Data](#personal-data). This document defines the terms of the [Qiy Scheme](#qiy-scheme) and is referred to in all other [Qiy Scheme](#qiy-scheme)-documents.

## Definitions

### Accepter
A [Business Role](#business-role) for a [Qiy User](#qiy-user) who is creating a [Connection](#connection) using a [Connect Token](#connect-token) that is provided by a [Proposer](#proposer).

### Access Provider
An organisation which provides [Qiy Users](#qiy-user) access to the [Qiy Trust Network](#qiy-trust-network).

### Account
A [Business Object](#business-object) for a relation between a consumer ([Qiy User](#qiy-user)) and a [Service Provider](#service-provider).

### Account Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of an [Account](#account).

### Account Register Request
A [Qiy Node Request](#qiy-node-request) to register an [Account](#account).

### Account Unregister Request
A [Qiy Node Request](#qiy-node-request) to register an [Account](#account).

### Account Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of an [Account](#account).

### Accountability
[Service Providers](#service-provider) shall ensure compliance with the [Qiy Trust Principles](#qiy-trust-principles) and must be able to demonstrate that they do so.

### Accounts Request
A [Qiy Node Request](#qiy-node-request) to list [Accounts](#account).

### Anonymous
Not directly or indirectly traceable to an [Individual](#individual).

### API
See [Application Programming Interface](#application-programming-interface).

### API Document
A document (or set of documents) that defines or describes an [API].

### Application
A computer program that has been designed to perform tasks, for example to help persons and/or organisations to provide or consume [Services](#service).

### Application Connect Token
A [Token](#token) that is used by [Qiy Applications](#qiy-application) to create [Connections](#connection).

### Application Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Application Programming Interface
A description of how an [Application](Definitions.md#application) can be accessed by another [Application](Definitions.md#application).

### Application Provider
A legal entity that provides [Qiy Applications](#qiy-application).

### Architectural Layers
The [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme): the [User Layer](#user-layer), the [Application Layer](#application-layer), the [Qiy Node Layer](#qiy-node-layer), the [Service Layer](#service-layer), the [Transport Layer](#transport-layer) and the [Carrier Layer](#carrier-layer).

### Assertion
A positive statement or declaration about a [User](#user).


### Binding Individual Terms
The general terms and conditions under which an [Individual](#individual) exchanges [Personal Data](#personal-data) with other [Users](#user) via the [Qiy Trust Network](#qiy-trust-network), see [Binding Individual Terms](Binding%20Individual%20Terms.md).

### Business Object
A business object represents a concept used within a particular business domain as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946055

### Business Process
A business process represents a sequence of business behaviors that achieves a specific outcome such as a defined set of products or business services as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946048

### Business Role
A business role is the responsibility for performing specific behavior, to which an actor can be assigned, or the part an actor plays in a particular action or event as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946043

### Carrier
A [Technology Service](#technology-service) that provides the [Services](#service) of the [Carrier Layer](#carrier-layer). 

### Carrier API
The [Application Programming Interface](#application-programming-interface) of a [Carrier](#carrier).

### Carrier Implementation
A software package which can be used to realize a [Carrier](#carrier).

### Carrier Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Carrier Node
A [Node](#node) which hosts one or more [Carriers](#carrier).

### Carrier Protocol
A protocol that is part of the [Qiy Standard](#qiy-standard) and which describes the interactions of [Carriers](#carrier).

### Catalogue Details Request
A [Qiy Node Request](#qiy-node-request) to get details of a [Service Catalogue](#service-catalogue).

### Catalogues Request
A [Qiy Node Request](#qiy-node-request) to list the [Service Catalogues](#service-catalogue) in the [Service Library](#service-library).

### Claim
A statement that one subject, such as a person or organization, makes about itself or another subject.

Definition taken from https://en.wikipedia.org/wiki/Claims-based_identity.

### Client
A [Qiy Node Client] that accesses a [Resource] of a [Server], see [Resource Access Management].

### Connect Proposal
A [Business Object](#business-object) for a proposal to connect via Qiy.

### Connect Token
A [Token](#token) used to create a [Connection](#connection).

### Connect Token Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](#connect-token) from the [Qiy Node](#qiy-node).

### Connect Token Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connect Token](#connect-token).

### Connect Token Details Request
A [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Connect Token](#connect-token).

### Connect Token Register Request
A [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](#connect-token).

### Connect Token Update Request
A [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](#connect-token).

### Connect Token Uri
A [Uri](#uri) which is used to identify a [Connect Token](#connect-token).

### Connect Tokens Request
A [Qiy Node Request](#qiy-node-request) that can be used to access [Connect Tokens](#connect-token).

### Connection
A bi-directional digital communications link between two [Qiy Nodes](#qiy-node).

### Connection Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to create a [Connection](#connection) with a [Connect Token](#connect-token).

### Connection Created Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Connection](#connection) has been created.

### Connection Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connection](#connection).

### Connection Details Request
A [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Connection](#connection).

### Connection Uri
A [Uri](#uri) which is used to identify a [Connection](#connection).

### Connections Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Connections](#connection) of a [Qiy Node](#qiy-node).

### Consent
Any freely given, specific, informed and unambiguous indication of the [Individual](#individual)'s wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of [Personal Data](#personal-data).

### Consent Audit Log
An audit log of a [Consent](#consent) which is accessible via its [Consent Repository](#consent-repository).

### Consent Credential
Credential which provide access to a [Consent Repository](#consent-repository).

### Consent Data Descriptor
[Data Descriptor](#data-descriptor) in a [Service Description](#service-description) referring to the [Data Description](#data-description) describing the [Personal Data](#personal-data) that is used to provide the [Service](#service).

### Consent Data Provider Credential
[Consent Credential](#consent-credential) for a [Data Provider](#data-provider).

### Consent Delete Request
A [Qiy Node Request](#qiy-node-request) which can be used to delete a [Consent](#consent).

### Consent Denied Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the denial of a [Consent](#consent).

### Consent Denied Request
A [Qiy Node Request](#qiy-node-request) which can be used to communicate the denial of a [Consent](#consent).

### Consent Denied Event
A [Qiy Node Event](#qiy-node-event) which can be used to communicate the denial of a [Consent](#consent).

### Consent Details Request
A [Qiy Node Request](#qiy-node-request) which can be used to acquire the details of a [Consent](#consent).

### Consent Granted Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the granting of a [Consent](#consent).

### Consent Granted Request
A [Qiy Node Request](#qiy-node-request) which can be used to communicate the granting of a [Consent](#consent).

### Consent Granted Event
A [Qiy Node Event](#qiy-node-event) which can be used to communicate the granting or regranting of a [Consent](#consent).

### Consent Individual Credential
[Consent Credential](#consent-credential) for an [Individual](#individual).

### Consent Notification Message
A [Qiy Node Message](#qiy-node-message) which can be used to notify the registration of a [Consent](#consent).

### Consent Relying Party Credential
[Consent Credential](#consent-credential) for a [Relying Party](#relying-party).

### Consent Repository
A repository for a [Consent](#consent) which can only be accessed with the proper [Consent Credential](#consent-credential).

### Consent Request
A [Qiy Node Request](#qiy-node-request) which can be used to [Request](#request) for a [Consent](#consent).

### Consent Request Message
A [Qiy Node Message](#qiy-node-message) which can be used to [Request](#request) for a [Consent](#consent).

### Consent Service
A [Technology Service](#technology-service) used to maintain [Consents](#consent) and their status.

### Consent Service Description
A [Service Description](#service-description) of the [Service](#service) for which a [Consent](#consent) applies.

### Consent Service Descriptor
A [Service Descriptor](#service-descriptor) of a [Consent Service Description](#consent-service-description).

### Consent Uri
A [Uri](#uri) which is used to identify a [Consent](#consent).

### Consent Withdrawn Request
A [Qiy Node Request](#qiy-node-request) which can be used to communicate the withdrawal of a [Consent](#consent).

### Consents Request
A [Qiy Node Request](#qiy-node-request) which can be used by [Qiy Users](#qiy-user) to access their [Consents](#consent).

### Controller
A [Qiy Node Client] that controls the access to a [Resource], see [Resource Access Management].

### Credential
One or more named [Strings](#string) or [Data](#data) that can be used to gain access to a resource.

### Data
[Information](#information) that has been encoded in a computer-processable form; a collection of binary digits.

### Data Description
A description of [Data](#data) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Data Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Object
[Data](#data) consisting of a collection of name/value pairs.

### Attribute
A name/value pair of a [Data Object](#data-object) where the name and value are known as the name and value of the attribute respectively.

### Data Provider
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Data](#data) (or [Assertions](#assertion)) through the [Qiy Trust Network](#qiy-trust-network) to other [Qiy Users](#qiy-user) on [Request](#request).

### Data Provider Id
An [Identifier](#identifier) which can be used to identify a [Data Provider](#data-provider) within the [Qiy Trust Network](#qiy-trust-network).

### Data Reference
Synonym of [Feed] in the context of a [Client] that is accessing data, see [Access Resource Management].

### Data Service
A [Service](#service), namely the provisioning of [Data](#data).

### Data Service Description
A [Service Description](#service-description) of a [Data Service](#data-service).

### Data Source
A [Service Source](#service-source): a [Data Service](#data-service) that will be used to provide the [Personal Data](#personal-data) for a [Consent](#consent).

### Data Type
A type of [Data](#data).

### Data Type Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of a [Data Type](#data-type) in the [Service Library](#service-library).

### Data Type Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Data Type](#data-type) in the [Service Library](#service-library).

### Data Type Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Data Type](#data-type) in the [Service Library](#service-library).

### Data Type Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of a [Data Type](#data-type) in the [Service Library](#service-library).

### Data Types Request
A [Qiy Node Request](#qiy-node-request) to list the [Data Types](#data-type) that are registered in the [Service Library](#service-library).

### Definitions of the Qiy Scheme
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook), this document.

### Described Resource
A [Resource] with a describing [API Document].

### Electronic Communications Network
A transmission systems, whether or not based on a permanent infrastructure or centralised administration capacity,  and, where applicable, switching or routing equipment and other resources, including network elements which are not active, which permit the conveyance of signals by wire, radio, optical or other electromagnetic means, including satellite networks, fixed (circuit- and packet-switched, including internet) and mobile networks, electricity cable systems, to the extent that they are used for the purpose of transmitting signals, networks used for radio and television broadcasting, and cable television networks, irrespective of the type of information conveyed.
(source: Article 2: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32018L1972&from=EN).

### Electronic Communications Service
a service normally provided for remuneration via [Electronic Communications Networks](#electronic-communications-network), which encompasses, with the exception of services providing, or exercising editorial control over, content transmitted using electronic communications networks and services, the following types of services:
* 'internet access service' as defined in point (2) of the second paragraph of Article 2 of Regulation (EU) 2015/2120;
* interpersonal communications service; and
* services consisting wholly or mainly in the conveyance of signals such as transmission services used for the provision of machine-to-machine services and for broadcasting.
(source: Article 2 DIRECTIVE (EU) 2018/1972 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 11 December 2018)

### Entitlement
A usage right for a [Resource](#resource) owned by some other [Legal Entity](#legal-entity).

### Entity
A concept (thing, thought, organism, ...) with distinct and independent existence.

### Escrow Agent
A [Legal Entity](#legal-entity) that ensures the execution of the arrangements as laid down in the [Escrow Agreement](#escrow-agreement), the management, control and storage of the deposit and the assessment of the functionality and completeness of the deposited materials, and whether these are up-to-date, by means of a verification investigation.

### Escrow Agreement
A legal document which defines the arrangement by which a [Legal Entity](#legal-entity) deposits an asset with an [Escrow Agent](#escrow-agent), who, in turn, makes a delivery to another [Legal Entity](#legal-entity) if and when the specified conditions of the contract are met.

### Events Request
A [Qiy Node Request](#qiy-node-request) to handle [Qiy Node Events](#qiy-node-event).

### Federation
A formation of a unity by multiple [Entities](#entity) in which some components are shared, while each retains control of its own affairs.

### Feed
A [Feed] can be used by a [Client] to access a resource of a [Server], see [Resource Access Management].

### General Data Protection Regulation
REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation), OJEU of 04.05.2016, No. L 119: 1-88. 

### Governance Model
The model on which basis the Qiy Scheme is independently administered, managed, controlled and audited. It is built on the concept of "trias politica": the division of powers into three branches, each with separate and independent powers and areas of responsibility so that the powers of one branch are not in conflict with the powers associated with the other branches. 

### HTTP Request
A request message from a client to a server as defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html.

### Identifier
A [String](#string) that identifies a unique [Entity](#entity).

Definition based on https://en.wikipedia.org/wiki/Identifier#In_computer_science.

### Identity
Any [Information](#information) that can be used to identify an [Entity](#entity).

### Individual
A [Business Role](#business-role), a specialisation of [Qiy User](#qiy-user), for a natural person that uses the [Qiy Trust Network](#qiy-trust-network).

### Information 
A human-processable physical representation of facts, perceptions or other concepts.

### Json
Json is data-interchange format, see https://en.wikipedia.org/wiki/JSON

### Legal Entity
An [Entity](#entity) that is capable of bearing legal rights and obligations, such as a business, a corporation, a government agency or a non-governmental organisation.

### Legitimate Purpose
A legal ground for the processing of [Personal Data](#personal-data).

### Library Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of a [Service Library](#service-library).

### License
[Access Providers](#access-provider) require a [License](#license) to operate on the basis of the [Qiy Scheme](#qiy-scheme). Parties can apply for a [License](#license) which requires paying a fee and complying with the [Qiy Scheme](#qiy-scheme).

### License Agreement Access Provider
The agreement between the [Scheme Authority](#scheme-authority) (or in delegation by the [Scheme Authority](#scheme-authority), between a [Regional Authority](#regional-authority)) and an [Access Provider](#access-provider), of which the template forms part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### License Fee
The combination of annual fees to be paid by an [Access Provider](#access-provider) to the [Scheme Authority](#scheme-authority) in exchange for a [License](#license).

### Local Id
An [Identifier](#identifier) that can only be used for identification within a limited scope, for example by a [Service Provider](#service-provider) to identify its costumers.

### Message Description
A [Data Description](#data-description) of a [Qiy Node Message](#qiy-node-message).

### Message Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Qiy Node Message](#qiy-node-message).

### Message Descriptor
This term is used in the following senses:
* A [Uri](#uri) which identifies a [Message Description](#message-description).
* A [Uri](#uri) which can be used to obtain a [Message Description](#message-description) from the [Service Library](#service-library).
* An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message).

### Message Details Request
A [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Qiy Node Message](#qiy-node-message).

### Message Post Request
A [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### Message Received Event
A [Qiy Node Event](#qiy-node-event) that notifies a [Receiver](#receiver) that he has received a new [Qiy Node Message](#qiy-node-message).

### Messages Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the messages of a [Qiy Node](#qiy-node).

### Message Type
A type of [Qiy Node Message](#qiy-node-message).

### Message Type Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of a [Message Type](#message-type) in the [Service Library](#service-library).

### Message Type Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Message Type](#message-type) in the [Service Library](#service-library).

### Message Type Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Message Type](#message-type) in the [Service Library](#service-library).

### Message Type Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of a [Message Type](#message-type) in the [Service Library](#service-library).

### Message Types Request
A [Qiy Node Request](#qiy-node-request) to list [Message Types](#message-type) that are registered in the [Service Library](#service-library).

### Node
A node represents a computational or physical resource that hosts, manipulates, or interacts with other computational or physical resources as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946084.

### Node Id
A [Qiy Node](#qiy-node) id.

### Offline Connect Token
A [Connect Token](#connect-token) created by a [Qiy Application](#qiy-application), for example when its [Qiy Node](#qiy-node) was temporarily not accessible.

### Online Connect Token
A [Connect Token](#connect-token) created by a [Qiy Node](#qiy-node).

### Path
A [Data](#data) link between two [Transporters](#transporter) which is used to exchange [Transport Messages](#transport-message).

### Path Create Request
A [Request](#request) of a [Qiy Node](#qiy-node) to its [Transporter](#transporter) to create a [Path](#path).

### Payload
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which contains the [Data](#data) that the [Sender](#sender) wants to transfer to the [Receiver](#receiver).

### Persistent Id
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can take place over multiple sessions as long as the [Connection](#connection) is maintained.

### Persistent Id Event
A [Qiy Node Event](#qiy-node-event) which is used to communicate the [Persistent Id](#persistent-id) of a new [Connection](#connection).

### Personal Data
Any [Information](#information) relating to an identified or identifiable [Individual](#individual).
Identifiable [Individual](#individual) means any who can be identified, directly or indirectly, in particular by reference to an [Identifier](#identifier), such as an identification number, location data, an online [Identifier](#identifier) or one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of an [Individual](#individual).

### Portfolio Details Request
A [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Service Portfolio](#service-portfolio).

### Portfolio Register Message
A [Qiy Node Message](#qiy-node-message) to request to add a [Data Provider](#data-provider) to a [Service Portfolio](#service-portfolio).

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Proposer Id
A [Proposer](#proposer) [Identifier](#identifier).

### Provider Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Provider Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Pseudo Id
An [Identifier](#identifier) that a [Service Provider](#service-provider) can use to provide services to an [Individual](#individual), but that the [Service Provider](#service-provider) can not use to identify the [Individual](#individual).
The Pseudo Id can either be persistent or transient.

### Pseudonymisation
The processing of [Personal Data](#personal-data) in such a manner that the [Personal Data](#personal-data) can no longer be attributed to a specific [Individual](#individual) without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the [Personal Data](#personal-data) are not attributed to an identified or identifiable [Individual](#individual).

### Public Key Infrastructure
A public key infrastructure (PKI) is a set of roles, policies, and procedures needed to create, manage, distribute, use, store & revoke digital certificates and manage public-key encryption, see https://en.wikipedia.org/wiki/Public_key_infrastructure.

### Published Provider Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of a [Service Provider](#service-provider).

### Published Provider Register Request
A [Qiy Node Request](#qiy-node-request) for [Access Providers](#access-provider) to register a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Published Provider Unregister Request
A [Qiy Node Request](#qiy-node-request) for [Access Providers](#access-provider) to unregister a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Published Provider Update Request
A [Qiy Node Request](#qiy-node-request) for [Access Providers](#access-provider) to update details of a [Service Provider](#service-provider).

### Published Providers Request
A [Qiy Node Request](#qiy-node-request) to list [Service Providers](#service-provider).

### Published Service Details Request
A [Qiy Node Request](#qiy-node-request) to get details of a [Service](#service) that has been published in a [Service Catalogue](#service-catalogue).

### Published Service Register Request
A [Qiy Node Request](#qiy-node-request) which can be used to register a [Service](#service) of a [Service Provider](#service-provider) with an [Access Provider](#access-provider) and include it in [Service Catalogue](#service-catalogue) of the [Service Provider](#service-provider).

### Published Service Unregister Request
A [Qiy Node Request](#qiy-node-request) which can be used to unregister a [Service](#service) of a [Service Provider](#service-provider) with an [Access Provider](#access-provider) and remove it from the [Service Catalogue](#service-catalogue) of the [Service Provider](#service-provider).

### Published Services Request
A [Qiy Node Request](#qiy-node-request) which can be used to list the [Services](#service) in a [Service Catalogue](#service-catalogue).

### Qiy App
A [Qiy Application](#qiy-application) that can be installed on a smart phone or similar device.

### Qiy Application
An [Application](#application) that uses the [Qiy Trust Network](#qiy-trust-network) and that complies with the [Qiy Scheme](#qiy-scheme).

### Qiy Application Protocol
A protocol that is part of the [Qiy Standard](#qiy-standard) and which describes the interactions of [Qiy Applications](#qiy-application).

### Qiy Foundation
A foundation dedicated to putting people back in control of their [Personal Data](#personal-data) while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
An organization underwriting the vision and the mission of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A [Technology Service](#technology-service) that functions as a point of entry for a [Qiy User](#qiy-user) to the [Qiy Trust Network](#qiy-trust-network).

### Qiy Node API
The [Application Programming Interface](#application-programming-interface) of the [Qiy Node](#qiy-node) which is part of the [Qiy Standard](#qiy-standard), see [Qiy Node API document].

### Qiy Node Client
An [Application](#application) that uses a [Qiy Node](#qiy-node).

### Qiy Node Credential
The [Credential](#credential) that can be used to access a [Qiy Node](#qiy-node), see [Qiy Node API][Qiy Node API Qiy Node Credential].

### Qiy Node Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to create a [Qiy Node](#qiy-node), see [Qiy Node API][Qiy Node API Request creation of Qiy Node].

### Qiy Node Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Qiy Node](#qiy-node), see [Qiy Node API][Qiy Node API Delete Qiy Node].

### Qiy Node Documentation
The [Qiy Node Documentation](#qiy-node-documentation) consists of the [Qiy Node API](#qiy-node-api) and the [Qiy Node Protocol](#qiy-node-protocol).

### Qiy Node Event
A [Technology Event](#technology-event) of a [Qiy Node](#qiy-node), see [Qiy Node API Events].

### Qiy Node Id
An [Identifier](#identifier) which can be used to identify a [Qiy Node](#qiy-node) within the [Qiy Trust Network](#qiy-trust-network), see [Qiy Node Credential].

### Qiy Node Implementation
An [Application](#application) which can be used to realize a [Qiy Node](#qiy-node).

### Qiy Node Interface
The [Technology Interface](#technology-interface) of a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Qiy Node Message
A message that is exchanged between [Qiy Nodes], see [Qiy Node API][Qiy Node API Messages].

### Qiy Node Create Request
A [HTTP Request](#http-request) to create a [Qiy Node](#qiy-node).

### Qiy Node Protocol
A protocol that is part of the [Qiy Standard](#qiy-standard) and which describes the interactions of [Qiy Nodes](#qiy-node), see [Qiy Node Protocol document](Qiy%20Node%20Protocol.md).

### Qiy Node Request
A [HTTP Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Scheme
The open standard consisting of technical, operational and business rules and agreements which fosters interoperability between the interconnected [Entities](#entity), and which enables the exchange of [Personal Data](#personal-data) between [Data Providers](#data-provider), [Individuals](#individual) and [Relying Parties](#relying-party), with the [Consent](#consent) of the [Individual](#individual). The [Qiy Scheme](#qiy-scheme) forms the basis of the [Qiy Trust Network](#qiy-trust-network) through which [Users](#user) can safely control and exchange [Personal Data](#personal-data) to which an [Individual](#individual) can connect via a personal [Qiy Node](#qiy-node).

### Qiy Scheme Policy for Applications
A set of [Qiy Scheme](#qiy-scheme) rules under which [Applications](#application) can access and use the [Qiy Trust Network](#qiy-trust-network).

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme).

### Qiy Standard
A set of open standards concerning the technical aspects of the [Qiy Scheme](#qiy-scheme), a subset of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Qiy Trust Network
An [Electronic Communications Network](#electronic-communications-network) that connects [Qiy Nodes](#qiy-node) and that is provided by [Access Providers](#access-provider) to [Qiy Users](#qiy-user) under the rules of the [Qiy Scheme](#qiy-scheme). 

### Qiy Trust Principles
The basic principles, which underlie the [Qiy Scheme](#qiy-scheme) and its overall business model. All [Qiy Users](#qiy-user) must respect these principles.

### Qiy User
A [Business Role](#business-role): a [Legal Entity](#legal-entity) that is using the [Qiy Trust Network](#qiy-trust-network).

### Qiy Webapp
A [Qiy Application](#qiy-application) that is accessible via a web browser.

### QR Code
See https://en.wikipedia.org/wiki/QR_code.

### Receiver
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that receives a [Qiy Node Message](#qiy-node-message) from a [Sender](#sender).

### Reference
See [Data Reference].

### Reference Serial Number
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which is used in reply messages to indicate the related [Qiy Node Message](#qiy-node-message).

### Regional Authority
A local [Legal Entity](#legal-entity) that adheres to the overall [Qiy Scheme](#qiy-scheme) and, in delegation by the [Scheme Authority](#scheme-authority) fulfils the following [Roles](#role) at the level of a geographic region: 
* License [Access Providers](#access-provider) under the rules and regulations of the Scheme Authority](#scheme-authority)
* Certify regional auditors (technical and non-technical) to perform audits on behalf of the [Scheme Authority](#scheme-authority) and to assist in fraud prevention
* Regional stakeholder engagement, regional marketing, public relations and public affairs tasks and communication concerning the [Qiy Scheme](#qiy-scheme)
* Facilitate an independent complaint and appeal process for licensees
* Ensure compliance
* Collect [License Fees](#license-fee)

### Relying Party
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Services](#service) to other [Qiy Users](#qiy-user) via the [Qiy Trust Network](#qiy-trust-network).

### Relying Party Id
A [Relying Party](#relying-party) [Identifier](#identifier).

### Request
A [Business Object](#business-object): a call or message requesting something.

### Resource
A [Web Service](#web-service) provided by a [Server], see [Resource Access Management].

### Resource Access Management
The [Qiy Node API] enables a [Client] to access protected [Described Resources] of a [Server] via a [Controller] using [Feeds]. 
This can be used for example by a [Relying Party] to access [Personal Data] of an [Individual] from a [Data Provider] under control by the [Individual] using what is then called a [Data Reference] or [Reference].

### Role
A set of connected rights, obligations and behaviours as conceptualized in the [Qiy Scheme](#qiy-scheme).

### RSA Private Key
An RSA private key, see https://en.wikipedia.org/wiki/RSA_(cryptosystem).

### Scheme Authority
The non-profit [Legal Entity](#legal-entity), which fulfils the following [Roles](#role) at a global level: 
* Supervision and monitoring 
* Definition of eligibility requirements for [Licenses](#license) 
* Definition and management of requirements, rules and regulations as specified in the [Qiy Scheme](#qiy-scheme) 
* Lobbying and maintaining a constant dialogue with all stakeholders 
* Maintaining overall business continuity 
* Compliance

### Scheme Authority
The global [Legal Entity](#legal-entity) that administers, manages, controls and further develops the [Qiy Scheme](#qiy=scheme).

### Sender
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that sends a [Qiy Node Message](#qiy-node-message) to a [Receiver](#receiver).

### Serial Number
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which identify the [Qiy Node Messages](#qiy-node-message) exchanged between one [Sender](#sender) and one [Receiver](#receiver). [Serial Numbers](#serial-number) for [Qiy Node Messages](#qiy-node-message) that are exchanged in the same direction are unique and increase over time.

### Service
An information society service; i.e., any service normally provided for remuneration, at a distance, by electronic means and at the individual request of a recipient of services.

### Service Catalogue
A [Business Object](#business-object) for information about all the [Services](#service) that a [Service Provider](#service-provider) can provide.

### Service Credential
[Credential](#credential) for accessing a [Service Endpoint](#service-endpoint).

### Service Credential Details Request
A [Qiy Node Request](#qiy-node-request) for [Qiy Users](#qiy-user) to obtain details of [Service Credential](#service-credential) for a [Data Source](#data-source) of a [Consent](#consent).

### Service Credential Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Credential](#service-credential) for a [Data Source](#data-source) of a [Consent](#consent).

### Service Credentials Request Message
A [Qiy Node Message](#qiy-node-message) for requesting [Service Credentials](#service-credential).

### Service Credentials Response Message
A [Qiy Node Message](#qiy-node-message) for providing [Service Credentials](#service-credential).

### Service Credential Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service Credential](#service-credential) of a [Data Source](#data-source) of a [Consent](#consent).

### Service Credential Update Request
A [Qiy Node Request](#qiy-node-request) for [Qiy Users](#qiy-user) to update a [Service Credential](#service-credential) of a [Data Source](#data-source) of a [Consent](#consent).

### Service Credentials Request
A [Qiy Node Request](#qiy-node-request) to list [Service Credentials](#service-credential).

### Service Description
A description of a [Service](#service) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Service Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Service Description](#service-description).

### Service Discovery
A [Business Process](#business-process) to find [Service Providers](#service-provider) for a given [Service](#service).

### Service Endpoint
A [Technology Interface](#technology-interface) provided by a [Service Provider](#service-provider) to allow the consumption of one or more of his [Services](#service).

### Service Endpoint API
The [Application Programming Interface](#application-programming-interface) of a [Service Endpoint](#service-endpoint).

### Service Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Service Library
A [Technology Service](#technology-service) that supports the [Service](#service) processes of the [Individuals](#individual) and the [Service Providers](#service-provider).

### Service Portfolio
A [Business Object](#business-object) for information about all the [Services](#service) that an [Individual](#individual) is or has been consuming.

### Service Provider
A [Business Role](#business-role): a [Qiy User](#qiy-user) which provides [Services](#service): a [Relying Party](#relying-party) or a [Data Provider](#data-provider).

### Service Provider Id
A [Service Provider](#service-provider) [Identifier](#identifier).

### Service Provider Register Request
See [Provider Register Request].

### Service Provider Unregister Request
See [Provider Unregister Request].

### Service Source
A [Service](#service) of a [Service Provider](#service-provider) that provides input services required by another [Service](#service).

### Service Type
The type of a [Service](#service) denoted with a [Service Type Url](#service-type-url) such as https://github.com/qiyfoundation/Payment-Due-List/tree/master/schema/v1.

### Service Type Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of a [Service Type](#service-type) in the [Service Library](#service-library).

### Service Type Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Type](#service-type) in the [Service Library](#service-library).

### Service Type Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service Type](#service-type) in the [Service Library](#service-library).

### Service Type Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of a [Service Type](#service-type) in the [Service Library](#service-library).

### Service Types Request
A [Qiy Node Request](#qiy-node-request) to list [Service Types](#service-type) that are registered in the [Service Library](#service-library).

### Server
A [Qiy Node Client] that owns a [Resource], see [Resource Access Management].

### Source Candidates Request
A [Qiy Node Request](#qiy-node-request) to obtain candidate [Service Providers](#service-provider) for a [Service](#service).

### Source Candidates Message
A [Qiy Node Message](#qiy-node-message) to propose candidate [Data Sources](#data-source) for a [Consent](#consent).

### Source Details Request
A [Qiy Node Request](#qiy-node-request) for [Qiy Users](#qiy-user) to obtain details of a [Data Source](#data-source) of a [Consent](#consent).

### Source Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service](#service) as a [Service Source](#service-source).

### Source Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service](#service) as a [Service Source](#service-source).

### Source Update Request
A [Qiy Node Request](#qiy-node-request) to update a [Service Source](#service-source).

### Subscription
A [Business Object](#business-object) for a relation between a consumer ([Qiy User](#qiy-user)) and a [Service Provider](#service-provider) with regard to a [Service](#service).

### Subscription Details Request
A [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Subscription](#subscription).

### Subscription Register Request
A [Qiy Node Request](#qiy-node-request) which can be used to register a [Subscription](#subscription) to a [Service](#service).

### Subscription Unregister Request
A [Qiy Node Request](#qiy-node-request) which can be used to unregister a [Subscription](#subscription) to a [Service](#service).

### Subscriptions Request
A [Qiy Node Request](#qiy-node-request) which can be used to list the [Subscriptions](#subscription) in a [Service Portfolio](#service-portfolio).

### Substitute Access Provider
An [Access Provider](#access-provider) that has been degignated by the Scheme Authority to replace te original [Access Provider](#access-provider) in case of default for any reason.

### Technology Event
A technology event is a technology behavior element that denotes a state change as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946096.

### Technology Interface
A technology interface represents a point of access where technology services offered by a node can be accessed as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946088.

### Technology Service
A technology service represents an explicitly defined exposed technology behavior as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946097.

### Territory
The geographic region served by a [Regional Authority](#regional-authority).

### Token
A [String](#string) or [Data](#data) that has meaning in a specific context.

### Transient Id
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can only take place for the duration of a session.

### Transport Connect Token
A [Token](#token) used to create [Paths](#path).

### Transport Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Transport Message
A message that is exchanged over a [Path](#path) between two [Transporters](#transporter).

### Transport Protocol
A protocol that is part of the [Qiy Standard](#qiy-standard) and which describes the interactions of [Transporters](#transporter).

### Transporter
A [Technology Service](#technology-service) that provides transport [Services](#service).

### Transporter API
The [Application Programming Interface](#application-programming-interface) of a [Transporter](#transporter).

### Transporter Implementation
A software package which can be used to realize a [Transporter](#transporter).

### Trust
An [Entity](#entity)'s confident reliance on the outcome of an interaction.

### Trust Relation
A relation between multiple [Entities](#entity), which is characterized by a mutual reliance on the outcome of an interaction.

### Uri
A Uniform Resource Identifier (URI) is a compact sequence of characters that identifies an abstract or physical resource and that complies with the syntax defined in https://tools.ietf.org/html/rfc3986.

### Use Case
A list of actions or event steps typically defining the interactions between a role and a system to achieve a goal.

Definition based on https://en.wikipedia.org/wiki/Use_case.

For the [Use Cases](#use-case) of the [Qiy Scheme](#qiy-scheme), see [UC00 Use Cases Overview](./use-cases/UC00%20Use%20Cases%20Overview.md).

### User
A [Business Role](#business-role) for [Individuals](#individual) and [Legal Entities](#legal-entities) that use an [Application](#application).

In the context of the Qiy Scheme, see: [Qiy User](#qiy-user).

### User Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme), see [High-Level Architectural Overview Document].

### Uuid
See https://en.wikipedia.org/wiki/Universally_unique_identifier.

### Verified Data
Self-describing [Data](#data) emanating from a source that can be reliably identified and contacted, of which the authenticity can be reliably determined without contacting the source.

### Verifiable Data
[Data](#data) emanating from a source that can be reliably identified and contacted to verify the authenticty of the [Data](#data).

### Web Service
A [Technology Service].

[API]: #api
[API Document]: #api-document
[Controller]: #controller
[Described Resource]: #described-resource
[DigitalMe]: https://digital-me.nl/
[Data Provider]: #data-provider
[Data Reference]: #data-reference
[Feed]: #feed
[Feeds]: #feeds
[High-Level Architectural Overview Document]: ../High-Level%20Architectural%20Overview.md
[Individual]: #individual
[Personal Data]: #personal-data
[Qiy Node Create Request]: #qiy-node-create-request
[Qiy Node Client]: #qiy-node-client
[Qiy Node API document]: Qiy-Node/Qiy%20Node%20API.md
[Qiy Node]: #qiy-node
[Qiy Nodes]: #qiy-node
[Reference]: #reference
[Relying Party]: #relying-party
[Resource]: #resource
[Resource Access Management]: #resource-access-management
[Server]: #server
[Technology Service]: #technology-service
[Token]: #token
[Web Service]: #web-service


[High-Level Architectural Overview Creating Qiy Nodes for Individuals]: ../High-Level%20Architectural%20Overview.mdQiy-Node/Qiy%20Node%20API.md#512-creating-qiy-nodes-for-individuals
[High-Level Architectural Overview Transport Layer]: ../High-Level%20Architectural%20Overview.md#8-the-transport-layer

[Qiy Node API Access feed]: Qiy-Node/Qiy%20Node%20API.md#access-feed
[Qiy Node API Access feed request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/Access_feed
[Qiy Node API Access Feed Callback]: Qiy-Node/Qiy%20Node%20API.md#access-feed-callback
[Qiy Node API Access Feed Callbacks]: Qiy-Node/Qiy%20Node%20API.md#access-feed-callback
[Qiy Node API Access feeds]: Qiy-Node/Qiy%20Node%20API.md#access-feeds
[Qiy Node API Access feeds request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/Access_feeds
[Qiy Node API Add feed source]: Qiy-Node/Qiy%20Node%20API.md#add-feed-source
[Qiy Node API Add feed source request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/Add_feed_source
[Qiy Node API Action Endpoint]: Qiy-Node/Qiy%20Node%20API.md#action-endpoint
[Qiy Node API Action Message Endpoint]: Qiy-Node/Qiy%20Node%20API.md#action-message-endpoint
[Qiy Node API Action Message List Endpoint]: Qiy-Node/Qiy%20Node%20API.md#action-message-list-endpoint
[Qiy Node API Annex A Dynamic Endpoint Addresses]: Qiy-Node/Qiy%20Node%20API.md#annex-a-dynamic-endpoint-addresses
[Qiy Node API Annex B Events]: Qiy-Node/Qiy%20Node%20API.md#annex-b-events
[Qiy Node API Annex C Callbacks]: Qiy-Node/Qiy%20Node%20API.md#annex-c-callbacks
[Qiy Node API Client]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/client
[Qiy Node API Connect Token Create Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connect-token-create-endpoint
[Qiy Node API Connect Token Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connect-token-endpoint
[Qiy Node API Connect Token List Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connect-token-list-endpoint
[Qiy Node API Connection Create Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connection-create-endpoint
[Qiy Node API Connection Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connection-endpoint
[Qiy Node API Connection Feeds Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connection-feeds-endpoint
[Qiy Node API Connection List Endpoint]: Qiy-Node/Qiy%20Node%20API.md#connection-list-endpoint
[Qiy Node API Controller]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/controller
[Qiy Node API controller]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/controller
[Qiy Node API Data Reference Received-v2 Event]: Qiy-Node/Qiy%20Node%20API.md#data-reference-received-v2-event
[Qiy Node API Data Reference Received-v2 Callback]: Qiy-Node/Qiy%20Node%20API.md#data-reference-received-v2-callback
[Qiy Node API Data Reference Received-v2 Callback Endpoint]: Qiy-Node/Qiy%20Node%20API.md#data-reference-received-v2-callback-endpoint
[Qiy Node API Delete Qiy Node]: Qiy-Node/Qiy%20Node%20API.md#delete-qiy-node
[Qiy Node API Delete Qiy Node request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/node/Delete_Qiy_Node
[Qiy Node API Document]: Qiy-Node/Qiy%20Node%20API.md
[Qiy Node API Dynamic Endpoint Addresses]: Qiy-Node/Qiy%20Node%20API.md#dynamic-endpoint-addresses
[Qiy Node API Events]: Qiy-Node/Qiy%20Node%20API.md#events
[Qiy Node API Event Callback Endpoint]: Qiy-Node/Qiy%20Node%20API.md#event-callback-endpoints
[Qiy Node API Event Callback Endpoints]: Qiy-Node/Qiy%20Node%20API.md#event-callback-endpoints
[Qiy Node API Event Callbacks Endpoint]: Qiy-Node/Qiy%20Node%20API.md#event-callbacks-endpoint
[Qiy Node API Feed]: Qiy-Node/Qiy%20Node%20API.md#feed
[Qiy Node API Feed Request Callback]: Qiy-Node/Qiy%20Node%20API.md#feed-request-callback
[Qiy Node API Feed Request Callbacks]: Qiy-Node/Qiy%20Node%20API.md#feed-request-callback
[Qiy Node API Feeds Endpoint]: Qiy-Node/Qiy%20Node%20API.md#feeds-endpoint
[Qiy Node API Get /api]: https://fdriesenaar.github.io/openapi.html
[Qiy Node API Get action message]: Qiy-Node/Qiy%20Node%20API.md#get-action-message
[Qiy Node API Get action message request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/action_message/Get_action_message
[Qiy Node API Get connect token]: Qiy-Node/Qiy%20Node%20API.md#get-connect-token
[Qiy Node API Get connect token request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Get_connect_token
[Qiy Node API Get connection]: Qiy-Node/Qiy%20Node%20API.md#get-connection
[Qiy Node API Get connection request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Get_connection
[Qiy Node API Get endpoint addresses]: Qiy-Node/Qiy%20Node%20API.md#get-endpoint-addresses
[Qiy Node API Get endpoint addresses request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/api/api
[Qiy Node API Get event callback endpoints]: Qiy-Node/Qiy%20Node%20API.md#get-event-callback-endpoints
[Qiy Node API Get event callback endpoints request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/configuration/get_event_callback_endpoints
[Qiy Node API Get node settings]: Qiy-Node/Qiy%20Node%20API.md#get-node-settings
[Qiy Node API Get node settings request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/node/Get_node_settings
[Qiy Node API Get service catalogue]: Qiy-Node/Qiy%20Node%20API.md#get-service-catalogue
[Qiy Node API Get service catalogue request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/server/Get_service_catalogue
[Qiy Node API Get user action message]: Qiy-Node/Qiy%20Node%20API.md#get-user-action-message
[Qiy Node API Getting help]: https://qiy.api.digital-me.nl/?version=latestQiy-Node/Qiy%20Node%20API.md#9acb0133-e012-4f49-a1e9-51283b8402c9
[Qiy Node API List action messages]: Qiy-Node/Qiy%20Node%20API.md#list-action-messages
[Qiy Node API List action messages request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/action_message/List_action_messages
[Qiy Node API List connect tokens]: Qiy-Node/Qiy%20Node%20API.md#list-connect-tokens
[Qiy Node API List connect tokens request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/List_connect_tokens
[Qiy Node API List connections]: Qiy-Node/Qiy%20Node%20API.md#list-connections
[Qiy Node API List connections request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/List_connections
[Qiy Node API List feeds]: Qiy-Node/Qiy%20Node%20API.md#list-feeds
[Qiy Node API List feeds request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/List_feeds
[Qiy Node API List messages]: Qiy-Node/Qiy%20Node%20API.md#list-messages
[Qiy Node API List messages request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/message/List_messages
[Qiy Node API Message]: Qiy-Node/Qiy%20Node%20API.md#message
[Qiy Node API Messages]: Qiy-Node/Qiy%20Node%20API.md#messages
[Qiy Node API Messages Endpoint]: Qiy-Node/Qiy%20Node%20API.md#messages-endpoint
[Qiy Node API Node Create Endpoint]: Qiy-Node/Qiy%20Node%20API.md#node-create-endpoint
[Qiy Node API Node Settings Endpoint]: Qiy-Node/Qiy%20Node%20API.md#node-settings-endpoint
[Qiy Node API POST /FeedsEndpoint/{feedId}]: https://fdriesenaar.github.io/openapi.html
[Qiy Node API POST /ConnectionCreateEndpoint]: https://fdriesenaar.github.io/openapi.html
[Qiy Node API Qiy Node Credential]: Qiy-Node/Qiy%20Node%20API.md#qiy-node-credential
[Qiy Node API Qiy Test Tool dm]: https://qiy-test-tool-dpyt.cloud.digital-me.nl/
[Qiy Node API Qiy Test Tool pa]: https://qiytesttool.pythonanywhere.com/
[Qiy Node API Register connect token]: Qiy-Node/Qiy%20Node%20API.md#register-connect-token
[Qiy Node API Register connect token request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Request_or_register_connect_token
[Qiy Node API Request connect token]: Qiy-Node/Qiy%20Node%20API.md#request-connect-token
[Qiy Node API Request connect token request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Request_or_register_connect_token
[Qiy Node API Request connection]: Qiy-Node/Qiy%20Node%20API.md#request-connection
[Qiy Node API Request connection request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Request_connection
[Qiy Node API Request creation of Qiy Node]: Qiy-Node/Qiy%20Node%20API.md#request-creation-of-qiy-node
[Qiy Node API Request creation of Qiy Node request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/node/Request_creation_of_qiy-node
[Qiy Node API Request for feed]: Qiy-Node/Qiy%20Node%20API.md#request-for-feed
[Qiy Node API Request for feed request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/Request_for_feed
[Qiy Node API Request connection request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/connection/Request_connection
[Qiy Node API Self Endpoint]: Qiy-Node/Qiy%20Node%20API.md#self-endpoint
[Qiy Node API Send message]: Qiy-Node/Qiy%20Node%20API.md#send-message
[Qiy Node API Send message request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/message/Send_message
[Qiy Node API Server]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/server
[Qiy Node API Service Access Endpoint]: Qiy-Node/Qiy%20Node%20API.md#service-access-endpoint
[Qiy Node API Service Catalogue Endpoint]: Qiy-Node/Qiy%20Node%20API.md#service-catalogue-endpoint
[Qiy Node API Service Endpoint]: Qiy-Node/Qiy%20Node%20API.md#service-endpoint
[Qiy Node API Services]: https://qiy.api.digital-me.nl/?version=latestQiy-Node/Qiy%20Node%20API.md#ab572b83-bd18-4a8e-85be-b549a0ac6758
[Qiy Node API Set feed source]: Qiy-Node/Qiy%20Node%20API.md#set-feed-source
[Qiy Node API Set feed source request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/feed/Set_feed_source
[Qiy Node API Set service catalogue]: Qiy-Node/Qiy%20Node%20API.md#set-service-catalogue
[Qiy Node API Set service catalogue request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/service/Set_service_catalogue
[Qiy Node API Set event callback endpoints]: Qiy-Node/Qiy%20Node%20API.md#set-event-callback-endpoints
[Qiy Node API Set event callback endpoints request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/configuration/set_event_callback_endpoints
[Qiy Node API Set node settings]: Qiy-Node/Qiy%20Node%20API.md#set-node-settings
[Qiy Node API Set node settings request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/node/Set_node_settings
[Qiy Node API Start listening to events]: Qiy-Node/Qiy%20Node%20API.md#start-listening-to-events
[Qiy Node API Start listening to events request]: https://fdriesenaar.github.io/openapi-doc.htmlQiy-Node/Qiy%20Node%20API.md#/controller/Start_listening_to_events
[Qiy Node API State Handled Event]: Qiy-Node/Qiy%20Node%20API.md#state-handled-event
[Qiy Node API State Handled Callback]: Qiy-Node/Qiy%20Node%20API.md#state-handled-callback
[Qiy Node API State Handled Callback Endpoint]: Qiy-Node/Qiy%20Node%20API.md#state-handled-callback-endpoint
[Qiy Node API Subscriptions]: https://qiy.api.digital-me.nl/?version=latestQiy-Node/Qiy%20Node%20API.md#ec0ab04d-ab6e-4a9c-9b45-e6b75b583bff
[Qiy Node API User Action Message Event]: Qiy-Node/Qiy%20Node%20API.md#user-action-message-event
[Qiy Node API User Action Message Events]: Qiy-Node/Qiy%20Node%20API.md#user-action-message-event

