# Definitions of the Qiy Scheme


## Abstract

The [Qiy Scheme](#qiy-scheme) defines a framework for individual persons, companies and governmental organizations to safely control and exchange personal information. This document defines the terms of the [Qiy Scheme](#qiy-scheme) and is referred to from all other [Qiy Scheme](#qiy-scheme)-documents.

# Definitions

### Accepter
A [Business Role](#business-role) for a [Qiy User](#qiy-user) who is creating a [Connection](#connection) using a [Connect Token](#connect-token) that is provided by a [Proposer](#proposer).

### Access Principle
The principle which authorizes the access of an [Individual](#individual) to his [Personal Data](#personal-data), one of the [Qiy Trust Principles](#qiy-trust-principles).

### Access Provider
An organization which provides [Qiy Users](#qiy-user) access to the [Qiy Trust Network](#qiy-trust-network).

### Accountability
[Data Provider](#data-provider) and [Relying Party](#relying-party) are responsible for, and must be able to demonstrate compliance with the principles.

### Anonymous
Not directly or indirectly traceable to a natural person.

### Application
An [Application Service](#application-service) or software for such a service. 

### Application Connect Token
A [Token](#token) that is used by [Qiy Applications](#qiy-application) to create [Connections](#connection).

### Application Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Application Service
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap09.html#_Toc489946075

### Architectural Layers
The [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme): the [User Layer](#user-layer), the [Application Layer](#application-layer), the [Qiy Node Layer](#qiy-node-layer), the [Service Layer](#service-layer), the [Transport Layer](#transport-layer) and the [Carrier Layer](#carrier-layer).

### Assertion
A positive statement or declaration about a [User](#user).

### Attribute
A quality or characteristic of an [Entity](#entity).

### Binding Individual Rights
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Binding Individual Rules
The general conditions on which basis the [Individual](#individual) may agree to exchange [Personal Data](#personal-data) with other parties via the [Qiy Scheme](#qiy-scheme). In particular, this charter supervises all forms of [Data](#data) exchange between an [Individual](#individual) and a third party offering its [Services](#service) within the [Qiy Scheme](#qiy-scheme) (called [Relying Parties](#relying-party) and [Data Providers](#data-provider)).

### Binding Principles
See [Binding Principles for Relying Parties and Data Providers](#binding-principles-for-relying-parties-and-data-providers).

### Binding Principles for Relying Parties and Data Providers
The rules for [Entities](#entity) ([Relying Parties](#relying-party) and [Data Providers](#data-provider)) to follow in order to be allowed to participate in the [Qiy Scheme](#qiy-scheme).

One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook), see [Binding Principles for Relying Parties and Data Providers](Binding%20Principles%20for%20Relying%20Parties%20and%20Data%20Providers%20within%20Qiy%20Trust%20Framework.md).

### Business Object
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946055

### Business Process
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946048

### Business Role
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946043

### Carrier
A [Technology Service](#technology-service) that provides the [Services](#service) of the [Carrier Layer](#carrier-layer). 

### Carrier API
[Technology Interface](#technology-interface) of the [Carrier](#carrier).

### Carrier Implementation
A software package which can be used to realize a [Carrier](#carrier).

### Carrier Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Carrier Node
A [Node](#node) which hosts one or more [Carriers](#carrier).

### Carrier Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Carriers](#carrier).

### Connect Proposal
A [Business Object](#business-object) for a proposal to connect via Qiy.

### Connect Token
A [Literal](#literal) used to create a [Connection](#connection).

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
A [Connection](#connection) between two [Qiy Nodes](#qiy-node).

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
As defined in the [GDPR](#gdpr).

### Consent Audit Log
An audit log of a [Consent](#consent) which is accessible via its [Consent Repository](#consent-repository).

### Consent Credentials
Credentials which provide access to a [Consent Repository](#consent-repository), consisting of a [Consent Uri](#consent-uri) and a [Consent Access Token].

### Consent Data Descriptor
[Data Descriptor](#data-descriptor) in a [Service Description](#service-description) referring to the [Data Description](#data-description) describing the [Personal Data](#personal-data) that is used to provide the [Service](#service).

### Consent Data Provider Credentials
[Consent Credentials](#consent-credentials) for a [Data Provider](#data-provider).

### Consent Delete Request
A [Qiy Node Request](#qiy-node-request) which can be used to delete a [Consent](#consent).

### Consent Denied Request
A [Qiy Node Request](#qiy-node-request) which can be used to communicate the denial of a [Consent](#consent).

### Consent Denied Event
A [Qiy Node Event](#qiy-node-event) which can be used to communicate the denial of a [Consent](#consent).

### Consent Details Request
A [Qiy Node Request](#qiy-node-request) which can be used to acquire the details of a [Consent](#consent).

### Consent Granted Request
A [Qiy Node Request](#qiy-node-request) which can be used to communicate the granting of a [Consent](#consent).

### Consent Granted Event
A [Qiy Node Event](#qiy-node-event) which can be used to communicate the granting or regranting of a [Consent](#consent).

### Consent Individual Credentials
[Consent Credentials](#consent-credentials) for an [Individual](#individual).

### Consent Relying Party Credentials
[Consent Credentials](#consent-credentials) for a [Relying Party](#relying-party).

### Consent Repository
A repository for a [Consent](#consent) which can only be accessed with the proper [Consent Credentials](#consent-credentials).

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

### Core Identifier
Immutable and secret means, which uniquely identify a [Qiy Node](#qiy-node) registration.

### Credential
Immutable combination of [Verified Identifier](#verified-identifier) and [Verified Attributes](#verified-attribute)

### Data
[Data](#data) in a raw form; unorganized facts that need to be processed. [Data](#data) can be something simple and seemingly random and useless until it is organized.

### Data by Reference
A pattern for exchanging [Data](#data) indirectly using a [Data Reference](#data-reference), see also [Service by Reference](#service-by-reference).

### Data Description
A description of [Data](#data) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Data Descriptor
A [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Provider
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Data](#data) (or [Assertions](#assertion)) through the [Qiy Trust Network](#qiy-trust-network) to other [Qiy Users](#qiy-user) on [Request](#request).

### Data Provider Id
An [Identifier](#identifier) which can be used to identify a [Data Provider](#data-provider) within the [Qiy Trust Network](#qiy-trust-network).

### Data Reference
An [Operation Reference](#operation-reference) which can be used to obtain [Personal Data](#personal-data) of an [Individual](#individual).

### Data Service
A [Service](#service), namely the provisioning of [Data](#data).

### Data Service Description
A [Service Description](#service-description) of a [Data Service](#data-service).

### Data Subject
As defined in the [GDPR](#gdpr).

### Definitions of the Qiy Scheme
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook), this document.

### Effective Date
5 January, 2015.

### Entity
See https://en.wikipedia.org/wiki/Entity.

### Entitlement
A usage right for a [Resource](#resource) owned by some other [Entity](#entity).

### Expiration Date
The Expiration Date of the [Transition Phase](#transition-phase): 30 juni 2019, or any earlier date as set unilaterally by the [Scheme Authority](#scheme-authority).

### Federation
A formation of a unity by multiple [Entities](#entity) in which some components are shared, while each retains control of its own affairs.

### Functional Specification
One of the [Qiy Scheme](#qiy-scheme) documents, see [Functional Specification](Functional Specification.md).

### GDPR
See [General Data Protection Regulation](#general-data-protection-regulation).

### General Data Protection Regulation
[General Data Protection Regulation](#general-data-protection-regulation), see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 

### Global Scheme Authority
tbd

### Governance Model
See [Governance Model for the Qiy Scheme](#governance-model-for-the-qiy-scheme).

### Governance Model for the Qiy Scheme
tbd

### HTTP Request
As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html.

### Identifier
An [Attribute](#attribute) of an [Identity](#identity), which identifies it, with sufficient uniqueness and immutability, that its trustworthiness can be assessed in a known context.

### Identity
A [User](#user) centric term. An [Entity](#entity) uses an [Identity](#identity) to represent an aspect of itself (such as parent or employee and client or server) through a collection of [Attributes](#attribute), in any interactive situation.

### Individual
A [Business Role](#business-role), a specialisation of [Qiy User](#qiy-user), for a natural person that uses the [Qiy Trust Network](#qiy-trust-network).

### Information 
[Data](#data) processed, organised, structured, or presented in a certain context, so that it is usable. Information provides context to [Data](#data).

### Json
Json is an open-standard format, see https://en.wikipedia.org/wiki/JSON

### Json Object
One of the basic data types of [Json](#json).

### Legal Entity
See https://en.wikipedia.org/wiki/Entity#In_law.

### License
[Regional Authorities](#regional-authority) and [Access Providers](#access-provider) require a [License](#license) to operate on the basis of the [Qiy Scheme](#qiy-scheme). Parties can apply for a [License](#license) which requires paying a fee and complying with the [Qiy Scheme](#qiy-scheme)'s Rules & Regulations.

### License Agreement Access Provider
A licence agreement for [Access Providers](#access-provider), the template of which is part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### License Fee
The combination of annual fees to be paid by an [Access Provider](#access-provider) to the [Scheme Authority](#scheme-authority) in exchange for a [License](#license).

### Literal
See https://en.wikipedia.org/wiki/Literal_(computer_programming).

### Local ID
Synonymous with [Identifier](#identifier)

### Message Description
A [Data Description](#data-description) of a [Qiy Node Message](#qiy-node-message).

### Message Descriptor
This term is used in the following senses:
* A [Uri](#uri) which identifies a [Message Description](#message-description).
* A [Uri](#uri) which can be used to obtain a [Message Description](#message-description) from the [Service Library](#service-library).
* An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message).

### Message Post Request
A [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### Message Received Event
A [Qiy Node Event](#qiy-node-event) that notifies a [Receiver](#receiver) that he has received a new [Qiy Node Message](#qiy-node-message).

### Messages Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the messages of a [Qiy Node](#qiy-node).

### Node
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946084

### Node Id
A [Qiy Node](#qiy-node) id.

### Offline Connect Token
A [Connect Token](#connect-token) created by a [Qiy Application](#qiy-application), for example when its [Qiy Node](#qiy-node) was temporarily not accessible.

### Online Connect Token
A [Connect Token](#connect-token) created by a [Qiy Node](#qiy-node).

### Operation
A 'sub-service' which can be used to consume a [Service](#service).

### Operation Execute Request
A [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by [Reference](#reference) using an [Operation Reference](#operation-reference).

### Operation Reference
A [Business Object](#business-object) used by the [Service by Reference](#service-by-reference)-pattern to execute an [Operation](#operation) by reference.

### Operation Reference Message
A [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference).

### Operation Reference Request Message
A [Qiy Node Message](#qiy-node-message) that can be used to [Request](#request) for [Operation References](#operation-reference).

### Operation Register Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) by registrating an [Operation Specification](#operation-specification).

### Operation Specification
A specification of a [HTTP Request](#http-request) for the execution of an [Operation](#operation).

### Path
A [Data](#data) link between two [Transporters](#transporter) which is used to exchange [Transport Messages](#transport-message).

### Path Create Request
A [Request](#request) of a [Qiy Node](#qiy-node) to its [Transporter](#transporter) to create a [Path](#path).

### Payload
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which contains the [Data](#data) that the [Sender](#sender) wants to transfer to the [Receiver](#receiver).

### Persistent Id
An [Identifier](#identifier) which can be used in addition to a [Connection Uri](#connection-uri) to identify a [Connection](#connection) and which has the same value for both related [Qiy Users](#qiy-user).

### Persistent Id Event
A [Qiy Node Event](#qiy-node-event) which is used to communicate the [Persistent Id](#persistent-id) of a new [Connection](#connection).

### Personal Data
[Data](#data) relating to an [Individual](#individual). This can be the name, address, telephone number, age, health [Data](#data), account balance, but also personal preferences, etcetera. [Data](#data) are stored at [Data Providers](#data-provider) servers or at the site of the [Individual](#individual) (e.g. in a [Data](#data) vault) and can be shared with [Relying Parties](#relying-party) by [Individuals](#individual).

As defined in the [GDPR](#gdpr).

### Portfolio Register Message
A [Qiy Node Message](#qiy-node-message) which can be used to add a [Service Provider](#service-provider) to a [Service Portfolio](#service-portfolio).

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Proposer Id
The [Identity](#identity) of the [Proposer](#proposer) as registered by the [Access Provider](#access-provider).

### Pseudonym
Synonymous with [Identifier](#identifier)

### Public Key Infrastructure
See https://en.wikipedia.org/wiki/Public_key_infrastructure.

### Qiy App
A [Qiy Application](#qiy-application) that can be installed on a smart phone or similar device.

### Qiy Application
An [Application](#application) that complies with the [Qiy Scheme Policy for Applications](#qiy-scheme-policy-for-applications).

### Qiy Application Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Applications](#qiy-application).

### Qiy Foundation
A foundation dedicated to putting people back in control of their [Personal Data](#personal-data) while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
A member of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A [Technology Service](#technology-service): a point of entry for a [Qiy User](#qiy-user) to connect to his personal or organisational [Data](#data) and allowing to manage and reuse [Data](#data) via the [Qiy Trust Network](#qiy-trust-network).

### Qiy Node API
A [Technology Interface](#technology-interface) of the [Qiy Node](#qiy-node) that is part of the [Qiy Open Standard](#qiy-open-standard).

### Qiy Node Credentials
The set of [Credentials](#credential) that can be used to access a [Qiy Node](#qiy-node).

### Qiy Node Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Qiy Node](#qiy-node).

### Qiy Node Documentation
The [Qiy Node Documentation](#qiy-node-documentation) consists of the [Qiy Node API](#qiy-node-api) and the [Qiy Node Protocol](#qiy-node-protocol).

### Qiy Node Event
A [Technology Event](#technology-event) of a [Qiy Node](#qiy-node).

### Qiy Node Id
An [Identifier](#identifier) which can be used to identify a [Qiy Node](#qiy-node) within the [Qiy Trust Network](#qiy-trust-network).

### Qiy Node Implementation
An [Application](#application) which can be used to realize a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Qiy Node Message
A message that is exchanged between a [Sender](#sender) and a [Receiver](#receiver) over a [Connection](#connection).

### Qiy Node Request
A [HTTP Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Node Create Request
A [HTTP Request](#http-request) to create a [Qiy Node](#qiy-node).

### Qiy Node Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Nodes](#qiy-node).

### Qiy Open Standard
A set of open standards for Qiy, maintained by the [Work Stream Functionality & Technology](#work-stream-functionality--technology), see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

### Qiy Scheme
The open standard and the set of technical, operational and business rules and agreements which fosters interoperability between the interconnected [Entities](#entity), and which enables the exchange of [Data](#data) between [Data Providers](#data-provider), [Individuals](#individual) and [Relying Parties](#relying-party), with the [Consent](#consent) of the [Individual](#individual). The [Qiy Scheme](#qiy-scheme) forms the basis of the [Qiy Trust Network](#qiy-trust-network) through which [Users](#user) can safely control and exchange personal information to which an [Individual](#individual) can connect via a personal [Qiy Node](#qiy-node).

### Qiy Scheme Policy for Applications
A set of [Qiy Scheme](#qiy-scheme) rules under which [Applications](#application) can access and use the [Qiy Trust Network](#qiy-trust-network).

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme).

### Qiy Trust Network
A [Technology Service](#technology-service) which is provided by [Access Providers](#access-provider) to [Qiy Users](#qiy-user) which enables people to access, manage and share [Personal Data](#personal-data) under the rules of the [Qiy Scheme](#qiy-scheme). 

### Qiy Trust Principles
The basic principles, which underlie the [Qiy Scheme](#qiy-scheme) and its overall business model. All [Qiy Users](#qiy-user) must respect these principles.

### Qiy User
A [Business Role](#business-role): an [Entity](#entity) that is using the [Qiy Trust Network](#qiy-trust-network).

### Qiy Webapp
A [Qiy Application](#qiy-application) that is accessible via a web browser.

### QR Code
See https://en.wikipedia.org/wiki/QR_code.

### Receiver
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that receives a [Qiy Node Message](#qiy-node-message) from a [Sender](#sender).

### Reference
A [Literal](#literal).

### Reference Serial Number
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which is used in reply messages to indicate the related [Qiy Node Message](#qiy-node-message).

### Regional Authority
tbd

### Regional Scheme Authority
The [Scheme Authority](#scheme-authority), which adheres to the overall [Qiy Scheme](#qiy-scheme) and fulfils the following [Roles](#role) at the level of a geographic region: 
* License [Access Providers](#access-provider) under the rules and regulations of the [Global Scheme Authority](#global-scheme-authority)
* Certify regional auditors (technical and non-technical) to perform audits on behalf of the [Global Scheme Authority](#global-scheme-authority) and to assist in fraud prevention
* Regional stakeholder engagement, regional marketing, public relations and public affairs tasks and communication concerning the [Qiy Scheme](#qiy-scheme)
* Facilitate an independent complaint and appeal process for licence and certificate holders
* Ensure compliance
* Collect [License Fees](#license-fee)

### Relying Party
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Services](#service) to other [Qiy Users](#qiy-user) via the [Qiy Trust Network](#qiy-trust-network).

### Relying Party Id
An [Identifier](#identifier) which can be used to identify a [Relying Party](#relying-party) within the [Qiy Trust Network](#qiy-trust-network).

### Request
A [Business Object](#business-object): a call or message requesting something.

### Resource
A [Service](#service), which its owner can provide to another [Identity](#identity).

### Role
A set of connected rights, obligations and behaviours as conceptualized in the [Qiy Scheme](#qiy-scheme).

### Route
tbd

### RSA Private Key
An RSA private key, see https://en.wikipedia.org/wiki/RSA_(cryptosystem).

### Scheme Authority
The non-profit [Entity](#entity), which fulfils the following [Roles](#role) at a global level: 
* Supervision and monitoring 
* Definition of eligibility requirements for [Licenses](#license) and/or certifications 
* Definition and management of requirements, rules and regulations as specified in the [Qiy Scheme](#qiy-scheme) 
* Lobbying and maintaining a constant dialogue with all stakeholders 
* Maintaining overall business continuity 
* Compliance

### Sender
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that sends a [Qiy Node Message](#qiy-node-message) to a [Receiver](#receiver).

### Serial Number
An [Attribute](#attribute) of a [Qiy Node Message](#qiy-node-message) which identify the [Qiy Node Messages](#qiy-node-message) exchanged between one [Sender](#sender) and one [Receiver](#receiver). [Serial Numbers](#serial-number) for [Qiy Node Messages](#qiy-node-message) that are exchanged in the same direction are unique and increase over time.

### Service
An 'information society service' as defined in the [GDPR](#gdpr).

### Service by Reference
A pattern for consuming [Services](#service) indirectly using [References](#reference) ([Operation Reference](#operation-reference)).

### Service Catalogue
A [Business Object](#business-object) for information about all the [Services](#service) that a [Service Provider](#service-provider) can provide.

### Service Credentials
[Credentials](#credential) for accessing a [Service Endpoint](#service-endpoint).

### Service Credentials Request Message
A [Qiy Node Message](#qiy-node-message) for requesting [Service Credentials](#service-credentials).

### Service Description
A description of a [Service](#service) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Service Descriptor
A [Uri](#uri) which can be used to identify and obtain a [Service Description](#service-description).

### Service Discovery
A [Business Process](#business-process) to find [Service Providers](#service-provider) for a given [Service](#service).

### Service Endpoint
A [Technology Service](#technology-service) provided by a [Service Provider](#service-provider) to allow the consumption of his [Services](#service).

### Service Endpoint API
[Technology Interface](#technology-interface) of a [Service Endpoint](#service-endpoint).

### Service Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Service Library
A [Technology Service](#technology-service) that supports the [Service](#service) processes of the [Individuals](#individual) and the [Service Providers](#service-provider).

### Service Portfolio
A [Business Object](#business-object) for information about all the [Services](#service) that an [Individual](#individual) is or has been consuming.

### Service Provider
A [Business Role](#business-role): a [Qiy User](#qiy-user) which provides [Services](#service).

### Service Provider Id
The [Identity](#identity) of the [Service Provider](#service-provider) as registered by the [Access Provider](#access-provider).

### Service Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service](#service).

### Service Source
A [Service Provider](#service-provider) that can or is providing a specific [Service](#service).

### Service Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service](#service).

### Source Candidates Request
A [Qiy Node Request](#qiy-node-request) to obtain candidate [Service Providers](#service-provider) for a [Service](#service).

### Source Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Provider](#service-provider) as source for a [Service](#service).

### Technology Event
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946096

### Technology Interface
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946088

### Technology Service
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946097 

### Territory
The geographic region served by a [Regional Authority](#regional-authority).

### Token
See https://en.wikipedia.org/wiki/Token#Computing.

### Transition Phase
Temporarily phase from July 1, 2015 to the [Expiration Date](#expiration-date) during which an ad-interim [Governance Model](#governance-model) for the [Qiy Scheme](#qiy-scheme) is established. During this period the [Qiy Foundation](#qiy-foundation) fulfills the [Roles](#role) of [Global Scheme Authority](#global-scheme-authority) and [Regional Scheme Authority](#regional-scheme-authority). 

### Transport Connect Token
A [Literal](#literal) used to create [Paths](#path).

### Transport Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Transport Message
A message that is exchanged over a [Path](#path) between two [Transporters](#transporter).

### Transport Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Transporters](#transporter).

### Transporter
A [Technology Service](#technology-service) that provides transport [Services](#service).

### Transporter API
[Technology Interface](#technology-interface) of a [Transporter](#transporter).

### Transporter Implementation
A software package which can be used to realize a [Transporter](#transporter).

### Trust
An [Entity](#entity)'s confident reliance on the outcome of an interaction.

### Trust Relation
A relation between multiple [Entities](#entity), which is characterized by a mutual reliance on the outcome of an interaction.

### Uri
See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

### Use Case
See https://en.wikipedia.org/wiki/Use_case.

### User
A [Business Role](#business-role) for [Entities](#entity).

In general: a consumer of a [Service](#service).

In the context of the Qiy Scheme, see: [Qiy User](#qiy-user).

### User Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Uuid
See https://en.wikipedia.org/wiki/Universally_unique_identifier.

### Validated data
[Data](#data) whose source can be determined reliably.

### Verified Attribute
An [Attribute](#attribute) that has been assigned to an [Entity](#entity) by a trusted third party.

### Verified Identifier
An [Identifier](#identifier) that has been linked to an [Entity](#entity) by a trusted third party.

### Work Stream Functionality & Technology
One of the work streams of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/qiy-scheme/workstreams/

