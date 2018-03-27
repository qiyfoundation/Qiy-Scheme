# Definitions of the 'Qiy Scheme V1.0'

## Abstract

The Qiy Scheme defines a framework for individual Users, companies and governmental organizations to safely control and exchange personal information. This document defines the most important terms of the Qiy Scheme and is referred to from all other Scheme Documents.

# Definitions

### Accepter
A [Business Role](#business-role) for a [Qiy User](#qiy-user) who is creating a [Connection](#connection) using a [Connect Token](#connect-token) that is provided by a [Proposer](#proposer).

### Access Principle
The principle which authorizes the access of an [Individual](#individual) to his [Personal Data](#personal-data), one of the [Qiy Trust Principles](#qiy-trust-principles).

### Access Provider
An organization which provides [Qiy Users](#qiy-user) access to the [Qiy Trust Framework](#qiy-trust-framework), either an [Issuer](#issuer) or a [Service Provider](#service-provider).

### Accountability
Data provider and Relying Party are responsible for, and must be able to demonstrate compliance with the principles

### Anonymous
Not directly or indirectly traceable to a natural person.

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

### Assertion
A positive statement or declaration about a User.

### Attribute
A quality or characteristic of an Entity.

### Binding Individual Rights
One of the documents of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Binding Individual Rules
The general conditions on which basis the individual may agree to exchange personal data with other parties via the Qiy Scheme. In particular, this charter supervises all forms of data exchange between an individual and a third party offering its services within the Qiy Scheme (called Relying Parties and Data Providers).

### Binding Principles for Relying Parties and Data Providers
The rules for Entities (Relying Parties and Data Providers) to follow in order to be allowed to participate in the Qiy Scheme.

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

### Carrier Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Carriers](#carrier).

### Connect Proposal
A [Business Object](#business-object) for a proposal to connect via Qiy.

### Connect Token
A [Literal](#literal) used to create a [Connection](#connection).

### Connect Token Create Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](#connect-token) from the [Qiy Node](#qiy-node).

### Connect Token Register Request
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

### Connection Details Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain the details of a [Connection](#connection).

### Connection Uri
A [Uri](#uri) which is used to identify a [Connection](#connection).

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

### Core Identifier
Immutable and secret means, which uniquely identify a Qiy Node registration

### Credential
Immutable combination of Verified Identifier and Verified Attributes

### Data
Data in a raw form; unorganized facts that need to be processed. Data can be something simple and seemingly random and useless until it is organized.

### Data Description
A description of data that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Data Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Data Description](#data-description).

### Data Provider
A User who provides data (or Assertions) through the Qiy Network to other Users on request.

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

### Effective Date
5 January, 2015.

### Entitlement
A usage right for a resource owned by some other Entity.

### Federation
A formation of a unity by multiple Entities in which some components are shared, while each retains control of its own affairs.

### GDPR
General Data Protection Regulation, see http://eur-lex.europa.eu/legal-content/EN-NL/TXT/?uri=CELEX:32016R0679&from=EN. 

### Governance Model for the Qiy Scheme
Governance Model for the [Qiy Scheme](#qiy-scheme), see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/.

### HTTP Request
As defined in RFC 2616, see https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html

### Identifier
An attribute of an identity, which identifies it, with sufficient uniqueness and immutability, that its trustworthiness can be assessed in a known context.

### Identity
A User centric term. An Entity uses an Identity to represent an aspect of itself (such as parent or employee and client or server) through a collection of Attributes, in any interactive situation.

### Individual
A natural person provided with a Qiy Node by an Issuer allowing him or her to access and to control his or her Personal Data.

A [Business Role](#business-role) of a [Qiy User](#qiy-user) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Information 
Data processed, organised, structured, or presented in a certain context, so that it is usable. Information provides context to data.

### Issuer
An Entity entitled to create Qiy Nodes for Individuals.

A [Business Role](#business-role) for an [Access Provider](#access-provider) that provides services to natural persons, see [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Legal Entity
Any legal organisation, computing device, or tangible asset; also any self-managed collection or organisation of Entities.

### Licence Agreement Application Provider
A licence agreement for [Application Providers](#application-provider).

### Licence Agreement Issuer
A licence agreement for [Issuers](#issuer), the template of which is part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### Licence Agreement Service Provider
A licence agreement for [Service Providers](#service-provider), the template of which is part of the [Qiy Scheme Rulebook](#qiy-scheme-rulebook).

### License
All Qiy Scheme Servicing Parties (Regional Authority, Issuer, Service Provider) require a license to operate on the basis of the Qiy Scheme. Participants can apply for a License by paying a fee and by complying with the Qiy Scheme?s Rules & Regulations.

### License Fee
The combination of annual fees to be paid by a Service Provider to the Scheme Authority in exchange for a license.

### Literal
A fixex value, see https://en.wikipedia.org/wiki/Literal_(computer_programming).

### Local ID
Synonymous with Identifier

### Merchant
Data Provider or a Relying Party

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

### Offline Connect Token
A [Connect Token](#connect-token) created by a [Qiy Application](#qiy-application), for example when its [Qiy Node](#qiy-node) was temporarily not accessible.

### Online Connect Token
A [Connect Token](#connect-token) created by a [Qiy Node](#qiy-node).

### Operation
A 'sub-service' which can be used to consume a [Service](#service).

### Operation Execute Request
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

### Operation Register Request
A [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) by registrating an [Operation Specification](#operation-specification).

### Operation Specification
A specification of a [Http Request](#http-request) for the execution of an [Operation](#operation).

### Path
A connection between two [Transporters](#transporter) which is used to exchange [Transport Messages](#transport-message).

### Path Create Request
A request of a [Qiy Node](#qiy-node) to its [Transporter](#transporter) to create a [Path](#path).

### Personal Data
Data relating to an Individual. This can be the name, address, telephone number, age, health data, account balance, but also personal preferences, etcetera. Data are stored at Data Providers servers or at the site of the Individual (e.g. in a data vault) and can be shared with Relying Parties by Individuals.

As defined in the [GDPR](#gdpr).

### Proposer
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that initiates creating a [Connection](#connection) by providing a [Connect Token](#connect-token), sometimes using a [Connect Proposal](#connect-proposal).

### Provider
A [Business Role](#business-role) for a [Qiy User](#qiy-user) that is providing one or more [Services](#service) using Qiy, that is a [Data Provider](#data-provider) or a [Relying Party](#relying-party).

### Pseudonym
Synonymous with Identifier

### Qiy Application
An [Application Service](#application-service) or software that is authorized for use with Qiy.

### Qiy Application Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Applications](#qiy-application).

### Qiy Foundation
A foundation dedicated to putting people back in control of their personal data while creating value for organisations, see https://www.qiyfoundation.org/about-qiy/.

### Qiy Foundation Member
A member of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/membership/.

### Qiy Node
A single point of entry for a User to connect to his personal or organisational data and allowing to manage and share data via the Qiy Network.

A [Technology Service](#technology-service) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Qiy Node API
A [Technology Interface](#technology-interface) of the [Qiy Node](#qiy-node) that is part of the [Qiy Open Standard](#qiy-open-standard).

### Qiy Node Event
A [Technology Event](#technology-event) of a [Qiy Node](#qiy-node).

### Qiy Node Implementation
A software package which can be used to realize a [Qiy Node](#qiy-node).

### Qiy Node Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Qiy Node Message
A [Message](#message) that is exchanged using a [Connection](#connection).

### Qiy Node Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Qiy Nodes](#qiy-node).

### Qiy Node Request
A [Http Request](#http-request) for a [Qiy Node](#qiy-node).

### Qiy Open Standard
A set of open standards for Qiy, maintained by the [Work Stream Functionality & Technology](#work-stream-functionality-&-technology), see https://www.qiyfoundation.org/qiy-scheme/workstreams/.

### Qiy Scheme
The open standard and the set of technical, operational and business rules and agreements which fosters interoperability between the interconnected Entities, and which enables the exchange of Data between Data Providers, Individuals and Relying Parties, with the consent of the Individual. The Qiy Scheme forms the basis of the Qiy Network through which Users can safely control and exchange personal information to which an Individual can connect via a Personal Qiy Node.

See https://www.qiyfoundation.org/qiy-scheme/.

### Qiy Scheme Rulebook
A set of documents concerning governance, legal and technical aspects of the [Qiy Scheme](#qiy-scheme), see https://www.qiyfoundation.org/qiy-scheme/qiy-scheme-rulebook/

### Qiy Trust Framework
As defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Qiy Trust Principles
The basic principles, which underlie the Qiy Scheme and its overall business model. All Users must respect these principles.

As defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme), see https://www.qiyfoundation.org/qiy-trust-principles/.

### Qiy User
A [Business Actor](#business-actor); defined as 'User' in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Reference
A [Literal](#literal).

### Regional Scheme Authority
The Scheme Authority, which adheres to the overall Qiy Scheme and fulfils the following roles at the level of a geographic region: * License Issuers, Service Providers and Identity Providers under the rules and regulations of the Global Scheme Authority; * Certify regional auditors (technical and non-technical) to perform audits on behalf of the Global Scheme Authority and to assist in fraud prevention; * Regional stakeholder engagement, regional marketing, Public Relations and Public Affairs tasks and communication concerning the Qiy Scheme; * Facilitate an independent complaint and appeal process for licence and certificate holders; * Ensure compliance; * Collect Licence Fees.

### Relying Party
A User that relies on the Qiy Network to deliver services to an Individual.

A [Business Role](#business-role) as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Relying Party Agreement
An agreement that is required for [Relying Parties](#relying-party).

### Request
A [Business Object](#business-object): a message requesting something.

### Resource
A service, which its owner can provide to another identity.

### Role
A set of connected rights, obligations and behaviours as conceptualized in the Qiy Scheme.

### Scheme Authority
The non-profit Entity, which fulfils the following roles at a global level: * Supervision and monitoring * Definition of eligibility requirements for licenses and/or certifications * Definition and management of requirements, rules and regulations as specified in the Qiy Scheme * Lobbying and maintaining a constant dialogue with all stakeholders * Maintaining overall business continuity * Compliance

### Service
An 'information society service' as defined in the [GDPR](#gdpr).

### Service Catalogue
A [Business Object](#business-object) for information about all the [Services](#service) that a [Service Provider](#service-provider) can provide.

### Service Description
A description of a [Service](#service) that is both human- and machine-readable as addressed in https://en.wikipedia.org/wiki/Human-readable_medium.

### Service Descriptor
An [Uri](#uri) which can be used to identify and obtain a [Service Description](#service-description).

### Service Discovery
A [Business Process](#business-proces) to find [Providers](#provider) for a given [Service](#service).

### Service Endpoint
A [Technology Service](#technology-service) provided by a [Provider](#provider) to allow the consumption of his [Services](#service).

### Service Endpoint API
[Technology Interface](#technology-interface) of a [Service Endpoint](#service-endpoint).

### Service Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Service Library
A [Technology Service](#technology-service) that supports the [Service](#service) processes of the [Individuals](#individual) and the [Providers](#provider).

### Service Portfolio
A [Business Object](#business-object) for information about all the [Services](#service) that an [Individual](#individual) is or has been consuming.

### Service Provider
An Entity servicing Relying Parties and/or Data Providers. A Service Provider servicing individuals is called an Issuer.

A [Business Role](#business-role): an [Access Provider](#access-provider) which provides business-to-business services as defined in [Definitions of the Qiy Scheme](#definitions-of-the-qiy-scheme).

### Service Source
A [Provider](#provider) that can or is providing a specific [Service](#service).

### Service by Reference
A pattern for consuming [Services](#service) indirectly using references ([Operation Reference](#operation-reference)).

### Source Candidate Event
A [Qiy Node Event](#qiy-node-event) that is generated when a [Qiy Node](#qiy-node) has received a new [Source Candidate](#source-candidate) for a [Consent](#consent).

### Source Candidates Request
A [Qiy Node Request](#qiy-node-request) to obtain candidate [Providers](#provider) for a [Service](#service).

### Source Register Request
A [Qiy Node Request](#qiy-node-request) to register a [Provider](#provider) as source for a [Service](#service).

### Technology Event
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Technology Interface
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html

### Technology Service
As defined in Archimate 3.0, see https://pubs.opengroup.org/architecture/archimate3-doc/toc.html 

### Territory
The geographic region served by a Regional Authority.

### Transition Phase 
Temporarily Phase from July 1, 2015 to June 30, 2019 during which an ad-interim governance model for the Qiy Scheme is established. During this period the Qiy Foundation fulfills the roles of Global Scheme Authority and Regional Scheme Authority. 

### Transport Connect Token
A [Literal](#literal) used to create [Paths](#path).

### Transport Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Transport Message
A message that is exchanged over a [Path](#path) between two [Transporters](#transporter).

### Transport Message Description
A [Data Description](#data-description) that describes the contents, format and encryption (if any) of a [Transport Message](#transport-message).

### Transport Protocol
A protocol that is part of the [Qiy Open Standard](#qiy-open-standard) and which describes the interactions of [Transporters](#transporter).

### Transporter
A [Technology Service](#technology-service) that provides transport services.

### Transporter API
[Technology Interface](#technology-interface) of a [Transporter](#transporter).

### Transporter Implementation
A software package which can be used to realize a [Transporter](#transporter).

### Trust
An Entity's confident reliance on the outcome of an interaction.

### Trust Relation
A link between multiple Entities, which is characterized by a mutual reliance on the outcome of an interaction.

### Uuid
See https://en.wikipedia.org/wiki/Universally_unique_identifier

### Uri
See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

### Url
See https://en.wikipedia.org/wiki/Uniform_Resource_Identifier

### User
A user (Individual or Legal Entity) is connected to the Qiy Trust Framework in order to have access to, share and/or manage and/or use data. 

### User Layer
One of the [Architectural Layers](#architectural-layers) of the [Qiy Scheme](#qiy-scheme).

### Validated data
Data whose source can be determined reliably

### Verified Attribute
An Attribute that has been assigned to an Entity by a trusted third party.

### Verified Identifier
An Identifier that has been linked to an Entity by a trusted third party.

### Work Stream Functionality & Technology
One of the work streams of the [Qiy Foundation](#qiy-foundation), see https://www.qiyfoundation.org/qiy-scheme/workstreams/
