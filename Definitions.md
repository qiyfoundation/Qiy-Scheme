# Definitions of the Qiy Scheme


## Abstract

The [Qiy Scheme](#qiy-scheme) defines a framework for [Individuals](#individual) and [Entities](#entity) to safely control and exchange [Personal Data](#personal-data). This document defines the terms of the [Qiy Scheme](#qiy-scheme) and is referred to in all other [Qiy Scheme](#qiy-scheme)-documents.

## Definitions

### Accepter
A [Business Role](#business-role) for a [Qiy User](#qiy-user) who is creating a [Connection](#connection) using a [Connect Token](#connect-token) that is provided by a [Proposer](#proposer).

### Access
The principle which authorizes the access of an [Individual](#individual) to his or her [Personal Data](#personal-data), one of the [Qiy Trust Principles](#qiy-trust-principles).

### Access Provider
An organisation which provides [Qiy Users](#qiy-user) access to the [Qiy Trust Network](#qiy-trust-network).

### Accountability
[Service Providers](#service-provider) are responsible for, and must be able to demonstrate compliance with the [Qiy Trust Principles](#qiy-trust-principles).

### Anonymous
Not directly or indirectly traceable to a natural person.

### Application
An [Application Service](#application-service) or software for such a service. 

### Application Connect Token
A [Token](#token) that is used by [Qiy Applications](#qiy-application) to create [Connections](#connection).

### Application Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Application Service
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Architectural Layers
The [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme): the [User Layer](#user-layer), the [Application Layer](#application-layer), the [Qiy Node Layer](#qiy-node-layer), the [Service Layer](#service-layer), the [Transport Layer](#transport-layer) and the [Carrier Layer](#carrier-layer).

### Assertion
A positive statement or declaration about a [User](#user).

### Attribute
A quality that is a particular characteristic of an [Individual](#individual) or an [Entity](#entity).

### Binding Individual Terms
The general terms and conditions under which an [Individual](#individual) exchanges [Personal Data](#personal-data) with other [Users](#user) via the [Qiy Trust Network](#qiy-trust-network).

### Business Object
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Business Process
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap08.html#_Toc489946048

### Business Role
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

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

### Communication Network
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946090 

### Connect Proposal
A [Business Object](#business-object) for a proposal to connect via Qiy.

### Connect Token
A [Literal](#literal) used to create a [Connection](#connection).

### Connect Token Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](#connect-token) from the [Qiy Node](#qiy-node).

### Connect Token Register Request
A [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](#connect-token).

### Connection
A bi-directional digital communications link between two [Qiy Nodes](#qiy-node).

### Connection Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to create a [Connection](#connection) with a [Connect Token](#connect-token).

### Connection Created Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Connection](#connection) has been created.

### Connection Delete Request
A [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connection](#connection).

### Connection Uri
A [Uri](#uri) which is used to identify a [Connection](#connection).

### Consent
Any freely given, specific, informed and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her.

### Consent Data Descriptor
[Data Descriptor](#data-descriptor) in a [Service Description](#service-description) referring to the [Data Description](#data-description) describing the [Personal Data](#personal-data) that is used to provide the [Service](#service).

### Consent Denied Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the denial of a [Consent](#consent).

### Consent Granted Message
A [Qiy Node Message](#qiy-node-message) which can be used to communicate the granting of a [Consent](#consent).

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
An [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Provider
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Data](#data) (or [Assertions](#assertion)) through the [Qiy Trust Network](#qiy-trust-network) to other [Qiy Users](#qiy-user) on [Request](#request).

### Data Provider ID
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

Sometimes used in the sense of [Legal Entity](#legal-entity).

### Entitlement
A usage right for a [Resource](#resource) owned by some other [Entity](#entity).

### Escrow Agent
[Entity](#entity) that ensures the execution of the arrangements as laid down in the [Escrow Agreement](#escrow-agreement), the management, control and storage of the deposit and the assessment of the functionality and completeness of the deposited materials, and whether these are up-to-date, by means of a verification investigation.

### Escrow Agreement
A legal document which defines the arrangement by which an [Entity](#entity) deposits an asset with an [Escrow Agent](#escrow-agent), who, in turn, makes a delivery to another [Entity](#entity) if and when the specified conditions of the contract are met.

### Expiration Date
The Expiration Date of the [Transition Phase](#transition-phase): 30 juni 2019, or any earlier date as set unilaterally by the [Scheme Authority](#scheme-authority).

### Federation
A formation of a unity by multiple [Entities](#entity) in which some components are shared, while each retains control of its own affairs.

### General Data Protection Regulation
REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation), OJEU of 04.05.2016, No. L 119: 1-88. 

### Governance Model
The model on which basis the Qiy Scheme is independently administered, managed, controlled and audited. It is built on the concept of "trias politica": the division of powers into three branches, each with separate and independent powers and areas of responsibility so that the powers of one branch are not in conflict with the powers associated with the other branches. 

### HTTP Request
As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html.

### Identifier
Synonymous with [Local ID](#local-id) and [Pseudonym](#pseudonym).
An [Attribute](#attribute) of an [Identity](#identity), such as a name, an identification number, location data, an online identifier or one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity which identifies an [Individual](#individual) with sufficient uniqueness and immutability.

### Identity
A [User](#user) centric term. An [Entity](#entity) uses an [Identity](#identity) to represent an aspect of itself (such as parent or employee and client or server) through a collection of [Attributes](#attribute), in any interactive situation.

### Individual
A [Business Role](#business-role), a specialisation of [Qiy User](#qiy-user), for a natural person that uses the [Qiy Trust Network](#qiy-trust-network).

### Information 
[Data](#data) processed, organised, structured, or presented in a certain context, so that it is usable. Information provides context to [Data](#data).

### Legal Entity
An organisation that is capable of bearing legal rights and obligations, such as a business, a corporation, a government agency or a non-governmental organisation.

### Legitimate Purpose
A legal ground for the processing of [Personal Data](#personal-data).

### License
[Access Providers](#access-provider) require a [License](#license) to operate on the basis of the [Qiy Scheme](#qiy-scheme). Parties can apply for a [License](#license) which requires paying a fee and complying with the [Qiy Scheme](#qiy-scheme).

### License Agreement Access Provider
The agreement between the [Scheme Authority](#scheme-authority) (or in delegation by the [Scheme Authority](#scheme-authority), between a [Regional Authority](#regional-authority)) and an [Access Provider](#access-provider), of which the template forms part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### License Fee
The combination of annual fees to be paid by an [Access Provider](#access-provider) to the [Scheme Authority](#scheme-authority) in exchange for a [License](#license).

### Literal
See https://en.wikipedia.org/wiki/Literal_(computer_programming).

### Local ID
Synonymous with [Identifier](#identifier)

### Message Post Request
A [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### Message Received Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node Message](#qiy-node-message) has been received.

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
An activity undertaken to render a [Service](#service).

### Operation Execute Request
A [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by [Reference](#reference) using an [Operation Reference](#operation-reference).

### Operation Reference
A [Business Object](#business-object) used by the [Service by Reference](#service-by-reference)-pattern to execute an [Operation](#operation) by reference.

### Operation Reference Message
A [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference) over a [Connection](#connection).

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

### Persistent ID
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can take place over multiple sessions as long as the [Connection](#connection) is maintained.

### Personal Data
Any [Information](#information) relating to an [Individual](#individual) who can be identified, directly or indirectly, in particular by reference to an [Identifier](#identifier).

### Pseudo ID
An [Anonymous](#anoymous) [Attribute](#attribute) relating to an [Individual](#individual) which can either be persistent or transient.

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Proposer Id
The [Identity](#identity) of the [Proposer](#proposer) as registered by the [Access Provider](#access-provider).

### Pseudonym
Synonymous with [Identifier](#identifier) and [Local ID](#local-id).

### Public Key Infrastructure
See https://en.wikipedia.org/wiki/Public_key_infrastructure.

### Qiy Application
An [Application](#application) that complies with the [Qiy Scheme Policy for Applications](#qiy-scheme-policy-for-applications).

### Qiy Application Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Applications](#qiy-application).

### Qiy Foundation
A foundation dedicated to putting people back in control of their [Personal Data](#personal-data) while creating value for organizations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
An organization underwriting the vision and the mission of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A [Technology Service](#technology-service) that functions as a point of entry for a [Qiy User](#qiy-user) to the [Qiy Trust Network](#qiy-trust-network).

### Qiy Node API
A [Technology Interface](#technology-interface) of the [Qiy Node](#qiy-node) that is part of the [Qiy Open Standard](#qiy-open-standard).

### Qiy Node Credentials
The set of [Credentials](#credential) that can be used to access a [Qiy Node](#qiy-node).

### Qiy Node Documentation
The [Qiy Node Documentation](#qiy-node-documentation) consists of the [Qiy Node API](#qiy-node-api) and the [Qiy Node Protocol](#qiy-node-protocol).

### Qiy Node Event
A [Technology Event](#technology-event) of a [Qiy Node](#qiy-node).

### Qiy Node Implementation
An [Application](#application) which can be used to realize a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Qiy Node Message
A message that is exchanged using a [Connection](#connection).

### Qiy Node Request
A [HTTP Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Node Protocol
A technical protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Nodes](#qiy-node).

### Qiy Open Standard
A set of open technical protocols which form part of the [Qiy Scheme](#qiy-scheme).

### Qiy Scheme
The open standard consisting of technical, operational and business rules and agreements which fosters interoperability between the interconnected [Entities](#entity), and which enables the exchange of [Personal Data](#personal-data) between [Data Providers](#data-provider), [Individuals](#individual) and [Relying Parties](#relying-party), with the [Consent](#consent) of the [Individual](#individual). The [Qiy Scheme](#qiy-scheme) forms the basis of the [Qiy Trust Network](#qiy-trust-network) through which [Users](#user) can safely control and exchange [Personal Data](#personal-data) to which an [Individual](#individual) can connect via a personal [Qiy Node](#qiy-node).

### Qiy Scheme Policy for Applications
A set of [Qiy Scheme](#qiy-scheme) rules under which [Applications](#application) can access and use the [Qiy Trust Network](#qiy-trust-network).

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme).

### Qiy Trust Network
A [Technology Service](#technology-service) which is provided by [Access Providers](#access-provider) to [Qiy Users](#qiy-user) which enables people to access, manage and share [Personal Data](#personal-data) under the rules of the [Qiy Scheme](#qiy-scheme). 

### Qiy Trust Principles
The basic principles, which underlie the [Qiy Scheme](#qiy-scheme) and its overall business model. All [Qiy Users](#qiy-user) must respect these principles.

### Qiy User
A [Business Role](#business-role): an [Individual](#individual) or an [Entity](#entity) that is connected to the [Qiy Trust Network](#qiy-trust-network).

### QR Code
See https://en.wikipedia.org/wiki/QR_code.

### Reference
A [Literal](#literal).

### Regional Authority
A local [Entity](#entity) that adheres to the overall [Qiy Scheme](#qiy-scheme) and, in delegation by the [Scheme Authority](#scheme-authority) fulfils the following [Roles](#role) at the level of a geographic region: 
* License [Access Providers](#access-provider) under the rules and regulations of the Scheme Authority](#scheme-authority)
* Certify regional auditors (technical and non-technical) to perform audits on behalf of the [Scheme Authority](#scheme-authority) and to assist in fraud prevention
* Regional stakeholder engagement, regional marketing, public relations and public affairs tasks and communication concerning the [Qiy Scheme](#qiy-scheme)
* Facilitate an independent complaint and appeal process for licensees
* Ensure compliance
* Collect [License Fees](#license-fee)

### Relying Party
A [Business Role](#business-role), a specialisation of [Service Provider](#service-provider): a [Legal Entity](#legal-entity) that provides [Services](#service) to other [Qiy Users](#qiy-user) via the [Qiy Trust Network](#qiy-trust-network).

### Relying Party ID
An [Identifier](#identifier) which can be used to identify a [Relying Party](#relying-party) within the [Qiy Trust Network](#qiy-trust-network).

### Request
A [Business Object](#business-object): a call or message requesting something.

### Resource
A [Service](#service), which its owner can provide to another [Entity](#entity).

### Role
A set of connected rights, obligations and behaviours as conceptualized in the [Qiy Scheme](#qiy-scheme).

### Scheme Authority
The non-profit [Entity](#entity), which fulfils the following [Roles](#role) at a global level: 
* Supervision and monitoring 
* Definition of eligibility requirements for [Licenses](#license) 
* Definition and management of requirements, rules and regulations as specified in the [Qiy Scheme](#qiy-scheme) 
* Lobbying and maintaining a constant dialogue with all stakeholders 
* Maintaining overall business continuity 
* Compliance

### Scheme Authority
The global [Entity](#entity) that administers, manages, controls and further develops the [Qiy Scheme](#qiy=scheme).

### Service
An information society service; i.e., any service normally provided for remuneration, at a distance, by electronic means and at the individual request of a recipient of services.

### Service by Reference
A pattern for consuming [Services](#service) indirectly using [References](#reference) ([Operation Reference](#operation-reference)).

### Service Catalogue
A [Business Object](#business-object) for information about all the [Services](#service) that a [Service Provider](#service-provider) can provide.

### Service Description
A description of a [Service](#service) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Service Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Service Description](#service-description).

### Service Endpoint
A [Technology Service](#technology-service) provided by a [Service Provider](#service-provider) that makes it possible to yse the [Services](#service).

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

### Source Candidates Request
A [Qiy Node Request](#qiy-node-request) to obtain candidate [Service Providers](#service-provider) for a [Service](#service).

### Source Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Service Provider](#service-provider) as source for a [Service](#service).

### Service Source
A [Service Provider](#service-provider) that can or is providing a specific [Service](#service).

### Substitute Access Provider
An [Access Provider](#access-provider) that has been degignated by the Scheme Authority to replace te original [Access Provider](#access-provider) in case of default for any reason.

### Technology Event
As defined in Archimate 3.0, see http://pubs.opengroup.org/architecture/archimate3-doc/chap10.html#_Toc489946096

### Technology Interface
A software solution or a device with which different technologies can interact with each other, with an application or with a network.

### Technology Service
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 

### Territory
The geographic region served by a [Regional Authority](#regional-authority).

### Token
See https://en.wikipedia.org/wiki/Token#Computing.

### Transient ID
An [Identifier](#identifier) which can be used to identify a [Connection](#connection) and which has the same value for the [Qiy Users](#qiy-user) whose [Qiy Nodes](#qiy-nodes) are linked through this [Connection](#connection). Identification can only take place for the duration of a session.

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

### Validated Data
[Data](#data) emanating from a source that can be reliably identified and that has verified the validity of the data by itself.

### Verifiable Claim
A piece of information that is cryptographically trustworthy.

### Verified Attribute
An [Attribute](#attribute) that has been made available to an [Entity](#entity) by a trusted third party.

### Verified Identifier
An [Identifier](#identifier) that has been linked to an [Entity](#entity) by a trusted third party.


