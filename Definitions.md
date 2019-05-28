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
Not directly or indirectly traceable to a natural person.

### API
See [Application Programming Interface](#application-programming-interface).

### Application
A computer program that has been designed to perform tasks, for example to help persons and/or organisations to provide or consume [Services](#service).

### Application Connect Token
A [Token](#token) that is used by [Qiy Applications](#qiy-application) to create [Connections](#connection).

### Application Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Application Programming Interface
A description of how an [Application](Definitions.md#application) can be accessed by another [Application](Definitions.md#application).

### Architectural Layers
The [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme): the [User Layer](#user-layer), the [Application Layer](#application-layer), the [Qiy Node Layer](#qiy-node-layer), the [Service Layer](#service-layer), the [Transport Layer](#transport-layer) and the [Carrier Layer](#carrier-layer).

### Assertion
A positive statement or declaration about a [User](#user).

### Attribute
A quality that is a particular characteristic of an [Individual](#individual) or a [Legal Entity](#entity).

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
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Carrier Node
A [Node](#node) which hosts one or more [Carriers](#carrier).

### Carrier Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Carriers](#carrier).

### Catalogue Details Request
A [Qiy Node Request](#qiy-node-request) to get details of a [Service Catalogue](#service-catalogue).

### Catalogues Request
A [Qiy Node Request](#qiy-node-request) to list the [Service Catalogues](#service-catalogue) in the [Service Library](#service-library).

### Claim

A statement that one subject, such as a person or organization, makes about itself or another subject.

Definition taken from https://en.wikipedia.org/wiki/Claims-based_identity.

### Communication Network
A communication network represents a set of structures that connects computer systems or other electronic devices for transmission, routing, and reception of data or data-based communications such as voice and video as defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946090.

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
Any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her.

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

### Core Identifier
Immutable and secret means, which uniquely identify a [Qiy Node](#qiy-node) registration.

### Credential
Immutable combination of [Verified Identifier](#verified-identifier) and [Verified Attributes](#verified-attribute)

### Data
[Information](#information) that has been encoded in a computer-processable form.

### Data by Reference
A pattern for exchanging [Data](#data) indirectly using a [Data Reference](#data-reference), see also [Service by Reference](#service-by-reference).

### Data Description
A description of [Data](#data) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Data Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Object

[Data](#data) consisting of a collection of name/value pairs.

### Data Object Attribute

A name/value pair of a [Data Object](#data-object) where the name and value are known as the name and value of the attribute respectively.

### Data Provider
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Data](#data) (or [Assertions](#assertion)) through the [Qiy Trust Network](#qiy-trust-network) to other [Qiy Users](#qiy-user) on [Request](#request).

### Data Provider Id
An [Identifier](#identifier) which can be used to identify a [Data Provider](#data-provider) within the [Qiy Trust Network](#qiy-trust-network).

### Data Reference
An [Operation Reference](#operation-reference) which can be used to consume a [Data Service](#data-service) by reference, namely to obtain [Personal Data](#personal-data) of an [Individual](#individual).

### Data Reference Request
An [Operation Reference Request](#operation-reference-request) for a [Data Reference](#data-reference).

### Data Service
A [Service](#service), namely the provisioning of [Data](#data).

### Data Service Description
A [Service Description](#service-description) of a [Data Service](#data-service).

### Data Source
A [Service Source](#service-source): a [Data Service](#data-service) that will be used to provide the [Personal Data](#personal-data) for a [Consent](#consent).

### Data Subject
An identified or identifiable natural person to whom data relates to; an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an [Identifier](#identifier) such as a name, an identification number, location data, an online [Identifier](#identifier) or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person, as defined in the [General Data Protection Regulation](#general-data-protection-regulation).

Based on the definition given in the [General Data Protection Regulation](#general-data-protection-regulation).

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

### Effective Date
5 January, 2015.

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

### General Data Protection Regulation
REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation), OJEU of 04.05.2016, No. L 119: 1-88. 

### Governance Model
The model on which basis the Qiy Scheme is independently administered, managed, controlled and audited. It is built on the concept of "trias politica": the division of powers into three branches, each with separate and independent powers and areas of responsibility so that the powers of one branch are not in conflict with the powers associated with the other branches. 

### HTTP Request
A request message from a client to a server as defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html.

### Identifier
A letter, number, symbol, or any combination of those that identifies a unique [Entity](#entity).

Definition based on https://en.wikipedia.org/wiki/Identifier#In_computer_science.

### Identity
Any [Information](#information) and/or [Data](#data) that can be used to identify an [Entity](#entity).

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
Synonymous with [Identifier](#identifier)

### Message Description
A [Data Description](#data-description) of a [Qiy Node Message](#qiy-node-message).

### Message Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Qiy Node Message](#qiy-node-message).

### Message Descriptor
This term is used in the following senses:
* A [Uri](#uri) which identifies a [Message Description](#message-description).
* A [Uri](#uri) which can be used to obtain a [Message Description](#message-description) from the [Service Library](#service-library).
* A [Property](#property) of a [Qiy Node Message](#qiy-node-message).

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

### Operation
A 'sub-service' which can be used to consume a [Service](#service).

### Operation Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of an [Operation](#operation).

### Operation Execute Request
A [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by [Reference](#reference) using an [Operation Reference](#operation-reference).

### Operation Reference
A [Business Object](#business-object) used by the [Service by Reference](#service-by-reference)-pattern to execute an [Operation](#operation) by reference.

### Operation Reference Message
A [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference).

### Operation Reference Request
A [Request](#request) for an [Operation Reference](#operation-reference).

### Operation Reference Request Message
A [Qiy Node Message](#qiy-node-message) that can be used to convey a [Operation Reference Request](#operation-reference-request).

### Operation Register Request
A [Qiy Node Request](#qiy-node-request) to register an [Operation](#operation).

### Operation Specification
A specification of a [HTTP Request](#http-request) for the execution of an [Operation](#operation).

### Operation Specification Request Message
A [Qiy Node Message](#qiy-node-message) to request for an [Operation Specification](#operation-specification).

### Operation Type
The type of an [Operation](#operation).

### Operation Type Details Request
A [Qiy Node Request](#qiy-node-request) to get the details of an [Operation Type](#operation-type) in the [Service Library](#service-library).

### Operation Type Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Operation Type](#operation-type) in the [Service Library](#service-library).

### Operation Type Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Operation Type](#operation-type) in the [Service Library](#service-library).

### Operation Type Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of a [Operation Type](#operation-type) in the [Service Library](#service-library).

### Operation Types Request
A [Qiy Node Request](#qiy-node-request) to list the [Operation Types](#operation-type) that are registered in the [Service Library](#service-library).

### Operation Unregister Request
A [Qiy Node Request](#qiy-node-request) to register an [Operation](#operation).

### Operation Update Request
A [Qiy Node Request](#qiy-node-request) to update the details of an [Operation](#operation).

### Operations Request
A [Qiy Node Request](#qiy-node-request) to list [Operations](#operation).

### Path
A [Data](#data) link between two [Transporters](#transporter) which is used to exchange [Transport Messages](#transport-message).

### Path Create Request
A [Request](#request) of a [Qiy Node](#qiy-node) to its [Transporter](#transporter) to create a [Path](#path).

### Payload
A [Property](#property) of a [Qiy Node Message](#qiy-node-message) which contains the [Data](#data) that the [Sender](#sender) wants to transfer to the [Receiver](#receiver).

### Persistent Id
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can take place over multiple sessions as long as the [Connection](#connection) is maintained.

### Persistent Id Event
A [Qiy Node Event](#qiy-node-event) which is used to communicate the [Persistent Id](#persistent-id) of a new [Connection](#connection).

### Personal Data
Any [Information](#information) or [Data](#data) relating to a [Data Subject](#data-subject).
[Personal Data](#data) are stored at [Data Providers](#data-provider) servers or at the site of the [Individual](#individual) (e.g. in a [Data](#data) vault) and can be shared anonymously with [Relying Parties](#relying-party) by the related [Individuals](#individual).

Based on the definition given in the [General Data Protection Regulation](#general-data-protection-regulation).

### Portfolio Details Request
A [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Service Portfolio](#service-portfolio).

### Portfolio Register Message
A [Qiy Node Message](#qiy-node-message) to request to add a [Data Provider](#data-provider) to a [Service Portfolio](#service-portfolio).

### Property

A [Data Object Attribute](#data-object-attribute).

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Proposer Id
A [Proposer](#proposer) [Identifier](#identifier).

### Provider Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Provider Unregister Request
A [Qiy Node Request](#qiy-node-request) to unregister a [Service Provider](#service-provider) with the [Qiy Trust Network](#qiy-trust-network).

### Pseudo Id
An [Identifier](#identifier) that a [Service Provider](#service-provider) can use to provide services to a natural person, but that the [Service Provider](#service-provider) can not use to identify the natural person.
The Pseudo Id can either be persistent or transient.

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
An [Application](#application) that complies with the [Qiy Scheme Policy for Applications](#qiy-scheme-policy-for-applications).

### Qiy Application Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Applications](#qiy-application).

### Qiy Foundation
A foundation dedicated to putting people back in control of their [Personal Data](#personal-data) while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
An organization underwriting the vision and the mission of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A [Technology Service](#technology-service) that functions as a point of entry for a [Qiy User](#qiy-user) to the [Qiy Trust Network](#qiy-trust-network).

### Qiy Node API
The [Application Programming Interface](#application-programming-interface) of the [Qiy Node](#qiy-node) which is part of the [Qiy Open Standard](#qiy-open-standard).

### Qiy Node Credential
The [Credential](#credential) that can be used to access a [Qiy Node](#qiy-node).

### Qiy Node Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to create a [Qiy Node](#qiy-node).

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

### Qiy Node Interface
The [Technology Interface](#technology-interface) of a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Qiy Node Message
A message that is exchanged between a [Sender](#sender) and a [Receiver](#receiver) over a [Connection](#connection).

### Qiy Node Create Request
A [HTTP Request](#http-request) to create a [Qiy Node](#qiy-node).

### Qiy Node Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Nodes](#qiy-node), see [Qiy Node Protocol document](Qiy%20Node%20Protocol.md).

### Qiy Node Request
A [HTTP Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Open Standard
A set of open technical standards which form part of the [Qiy Scheme](#qiy-scheme).

### Qiy Scheme
The open standard consisting of technical, operational and business rules and agreements which fosters interoperability between the interconnected [Entities](#entity), and which enables the exchange of [Personal Data](#personal-data) between [Data Providers](#data-provider), [Individuals](#individual) and [Relying Parties](#relying-party), with the [Consent](#consent) of the [Individual](#individual). The [Qiy Scheme](#qiy-scheme) forms the basis of the [Qiy Trust Network](#qiy-trust-network) through which [Users](#user) can safely control and exchange [Personal Data](#personal-data) to which an [Individual](#individual) can connect via a personal [Qiy Node](#qiy-node).

### Qiy Scheme Policy for Applications
A set of [Qiy Scheme](#qiy-scheme) rules under which [Applications](#application) can access and use the [Qiy Trust Network](#qiy-trust-network).

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme).

### Qiy Trust Network
A [Communication Network](#communication-network) that connects [Qiy Nodes](#qiy-node) and that is provided by [Access Providers](#access-provider) to [Qiy Users](#qiy-user) under the rules of the [Qiy Scheme](#qiy-scheme). 

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
An [Identifier](#identifier).

### Reference Serial Number
A [Property](#property) of a [Qiy Node Message](#qiy-node-message) which is used in reply messages to indicate the related [Qiy Node Message](#qiy-node-message).

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
A [Service](#service), which its owner can provide to another [Legal Entity](#legal-entity).

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
An [[Property](#property) of a [Qiy Node Message](#qiy-node-message) which identify the [Qiy Node Messages](#qiy-node-message) exchanged between one [Sender](#sender) and one [Receiver](#receiver). [Serial Numbers](#serial-number) for [Qiy Node Messages](#qiy-node-message) that are exchanged in the same direction are unique and increase over time.

### Service
An information society service; i.e., any service normally provided for remuneration, at a distance, by electronic means and at the individual request of a recipient of services.

### Service by Reference
A pattern for consuming [Services](#service) indirectly using [References](#reference) ([Operation Reference](#operation-reference)).

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
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Service Library
A [Technology Service](#technology-service) that supports the [Service](#service) processes of the [Individuals](#individual) and the [Service Providers](#service-provider).

### Service Portfolio
A [Business Object](#business-object) for information about all the [Services](#service) that an [Individual](#individual) is or has been consuming.

### Service Provider
A [Business Role](#business-role): a [Qiy User](#qiy-user) which provides [Services](#service).

### Service Provider Id
A [Service Provider](#service-provider) [Identifier](#identifier).

### Service Provider Register Request
See [Provider Register Request].

### Service Provider Unregister Request
See [Provider Unregister Request].

### Service Source
A [Service](#service) of a [Service Provider](#service-provider) that provides input services required by another [Service](#service).

### Service Type
A type of [Service](#service).

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
An [Identifier](#identifier) used by [Applications](#application) that can only be used to access the [Entity](#entity) it identifies by the [Application](#application) that created it.

### Transient Id
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can only take place for the duration of a session.

### Transport Connect Token
A [Token](#token) used to create [Paths](#path).

### Transport Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Transport Message
A message that is exchanged over a [Path](#path) between two [Transporters](#transporter).

### Transport Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Transporters](#transporter).

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
A [Business Role](#business-role) for [Entities](#entity).

In general: a consumer of a [Service](#service).

In the context of the Qiy Scheme, see: [Qiy User](#qiy-user).

### User Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Uuid
See https://en.wikipedia.org/wiki/Universally_unique_identifier.

### Validated Data
[Data](#data) emanating from a source that can be reliably identified and that has verified the validity of the data by itself.

### Validated Attribute
An [Attribute](#attribute) emanating from a source that can be reliably identified and that has verified the validity of the [Attribute](#attribute) by itself.

### Verifiable Claim
A [Claim](#claim) that is cryptographically trustworthy.

### Verified Attribute
An [Attribute](#attribute) that has been made available to an [Entity](#entity) by a trusted third party.

### Verifiable Attribute
An [Attribute](#attribute) that has been made available to an [Entity](#entity), the source of which can be reliably identified and contacted to authoritatively authenticate the attribute.

### Verified Identifier
An [Identifier](#identifier) that has been linked to an [Entity](#entity) by a trusted third party.

