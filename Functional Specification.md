# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From [Qiy Nodes](Definitions.md#qiy-node) to [Data exchange](Definitions.md#data-exchange)


# Contents

1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Readers' Guidance](#12-readers-guidance)
1. [Overview](#2-overview)
1. [Data Provider Acquires Access to Qiy Trust Network](#3-data-provider-acquires-access-to-qiy-trust-network)
1. [Individual Acquires Access to Qiy Trust Network](#4-individual-acquires-access-to-qiy-trust-network)
1. [Relying Party Acquires Access to Qiy Trust Network](#5-relying-party-acquires-access-to-qiy-trust-network)
1. [Individual Connects with Data Provider](#6-individual-connects-with-data-provider)
1. [Individual Connects with Relying Party](#7-individual-connects-with-relying-party)
1. [Relying Party Requests Personal Data](#8-relying-party-requests-personal-data)

# 1 Introduction

This document describes the basic Qiy Scheme scenarios as an introduction to the full functional description provided in the [Use Cases](Definitions.md#use-case) listed in [UC00 Use Cases Overview](./use-cases/UC00%20Use%20Cases%20Overview.md).
These scenarios form the prelude for many other applications, examples of wich can be found in [Example Applications](example-applications/Example%20Applications.md).


## 1.1 Purpose

This document is the entry point for information analysts and software engineers that need to know how they can use the [Qiy Trust Network](Definitions.md#qiy-trust-network).

## 1.2 Readers' Guidance

* Information analysts are advised to read the scenarios of interest and the related [Use Case Specifications](use-cases/UC00%20Use%20Cases%20Overview.md).
* Software engineers are advised to read the scenarios of interest, the related [Use Case Specifications](use-cases/UC00%20Use%20Cases%20Overview.md) and the related [Qiy Node Documentation](Definitions.md#qiy-node-documentation).

# 2 Overview

This document describes the following scenarios:
* [Data Provider](Definitions.md#data-provider) scenarios:
  * [3 Data Provider Acquires Access to Qiy Trust Network](#3-data-provider-acquires-access-to-qiy-trust-network)
  * [7 Individual Connects with Data Provider](#7-individual-connects-with-data-provider)
* Scenarios for [Individuals](Definitions.md#individual):
  * [4 Individual Acquires Access to Qiy Trust Network](#4-individual-acquires-access-to-qiy-trust-network)
  * [6 Individual Connects with Data Provider](#6-individual-connects-with-data-provider)
  * [7 Individual Connects with Relying Party](#7-individual-connects-with-relying-party)
  * [8 Relying Party Requests Personal Data](#8-relying-party-requests-personal-data)
* [Relying Party](Definitions.md#relying-party) scenarios:
  * [5 Relying Party Acquires Access to Qiy Trust Network](#5-relying-party-acquires-access-to-qiy-trust-network)
  * [8 Relying Party Requests Personal Data](#8-relying-party-requests-personal-data)


# 3 Data Provider Acquires Access to Qiy Trust Network

This chapter describes a scenario of a [Data Provider](Definitions.md#data-provider) acquiring access to the Qiy Trust Network as an introduction to the full description provided in [UC01 Acquire Access to Qiy Trust Network](./use-cases/UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

The [Functional and Technical Overview](Functional%20and%20Technical%20Overview.md) describes the conditions under which a [Data Provider](Definitions.md#data-provider) can put a [Data Subject](Definitions.md#data-subject) ([Individual](Definitions.md#individual)) in control of his [Personal Data](Definitions.md#personal-data) via Qiy. In this scenario, the [Data Provider](Definitions.md#data-provider) (to be) has already made the necessary arrangements to meet these conditions.
The remaining steps for a [Data Provider](Definitions.md#data-provider) in order to enable [Data Subjects](Definitions.md#data-subject) to get in control of their [Personal Data](Definitions.md#personal-data) via the [Qiy Trust Network](Definitions.md#qiy-trust-network) are:
*   The [Data Provider](Definitions.md#data-provider) selects an [Access Provider](Definitions.md#access-provider).
*   The [Data Provider](Definitions.md#data-provider) concludes an access agreement with the [Access Provider](Definitions.md#access-provider).
*   The [Access Provider](Definitions.md#access-provider) authenticates and registers the [Identity](Definitions.md#identity) of the [Data Provider](Definitions.md#data-provider) in the [Service Library](Definitions.md#service-library).
*   The [Access Provider](Definitions.md#access-provider) creates a [Qiy Node](Definitions.md#qiy-node) for the [Data Provider](Definitions.md#data-provider) and provides the [Data Provider](Definitions.md#data-provider) with the [Qiy Node Credentials](Definitions.md#qiy-node-credential).
*   The [Data Provider](Definitions.md#data-provider) configures its computing system with the [Qiy Node Credentials](Definitions.md#qiy-node-credential) and gains physical access to the [Qiy Trust Network](Definitions.md#qiy-trust-network).
*   The [Data Provider](Definitions.md#data-provider) publishes its [Service Catalogue](Definitions.md#service-catalogue) in the [Service Library](Definitions.md#service-library).


# 4 Individual Acquires Access to Qiy Trust Network

This chapter describes a scenario in which an [Individual](Definitions.md#individual) acquires access to the Qiy Trust Network as an introduction to the full description provided in [UC01 Acquire Access to Qiy Trust Network](./use-cases/UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

The [Qiy Scheme](Definitions.md#qiy-scheme) allows [Individuals](Definitions.md#individual) to use the [Qiy Trust Network](Definitions.md#qiy-trust-network) in many different ways, but the [Individual](Definitions.md#individual) in this scenario has never used the [Qiy Trust Network](Definitions.md#qiy-trust-network) before and acquires access as follows:
* The [Individual](Definitions.md#individual) selects a [Qiy Application](Definitions.md#qiy-application).
* The [Individual](Definitions.md#individual) installs the application on his smart phone and secures access to it by setting a passcode.
* The [Qiy Application](Definitions.md#qiy-application) creates a [Qiy Node](Definitions.md#qiy-node) for the [Individual](Definitions.md#individual) and persists the [Qiy Node Credentials](Definitions.md#qiy-node-credential).

After these steps, the [Individual](Definitions.md#individual) has gained access to the [Qiy Trust Network](Definitions.md#qiy-trust-network) and he can use it by means of the [Qiy Application](Definitions.md#qiy-application).


# 5 Relying Party Acquires Access to Qiy Trust Network

This chapter describes a scenario in which a [Relying Party](Definitions.md#relying-party) acquires access to the [Qiy Trust Network](Definitions.md#qiy-trust-network) as an introduction to the full description provided in [UC01 Acquire Access to Qiy Trust Network](./use-cases/UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

The [Functional and Technical Overview](Functional%20and%20Technical%20Overview.md) describes the conditions under which a [Relying Party](Definitions.md#relying-party) can provide its [Services](Definitions.md#service) via Qiy while using verifiable [Personal Data](Definitions.md#personal-data) under control of their [Data Subject](Definitions.md#data-subject) ([Individual](Definitions.md#individual)).
In this scenario, the [Relying Party](Definitions.md#relying-party) (to be) has already made the necessary arrangements to meet these conditions.
The remaining steps for a [Relying Party](Definitions.md#relying-party) in order to enable [Individuals](Definitions.md#individual) to use its [Services](Definitions.md#service) via the [Qiy Trust Network](Definitions.md#qiy-trust-network) are:
*   The [Relying Party](Definitions.md#relying-party) selects an [Access Provider](Definitions.md#access-provider).
*   The [Relying Party](Definitions.md#relying-party) concludes an access agreement with the [Access Provider](Definitions.md#access-provider).
*   The [Access Provider](Definitions.md#access-provider) authenticates and registers the [Identity](Definitions.md#identity) of the [Relying Party](Definitions.md#relying-party) in the [Service Library](Definitions.md#service-library).
*   The [Access Provider](Definitions.md#access-provider) creates a [Qiy Node](Definitions.md#qiy-node) for the [Relying Party](Definitions.md#relying-party) and provides the [Relying Party](Definitions.md#relying-party) with the [Qiy Node Credentials](Definitions.md#qiy-node-credential).
*   The [Relying Party](Definitions.md#relying-party) configures its computing system with the [Qiy Node Credentials](Definitions.md#qiy-node-credential) and gains physical access to the [Qiy Trust Network](Definitions.md#qiy-trust-network).
*   The [Relying Party](Definitions.md#relying-party) publishes its [Service Catalogue](Definitions.md#service-catalogue) in the [Service Library](Definitions.md#service-library).


# 6 Individual Connects with Data Provider

This chapter describes a scenario in which an [Individual](Definitions.md#individual) connects with a [Data Provider](Definitions.md#data-provider) and get access to his [Personal Data](Definitions.md#personal-data) as an introduction to the full description provided in [UC02 Connect with Qiy User](./use-cases/UC02%20Connect%20with%20Qiy%20User.md).

The [Qiy Scheme](Definitions.md#qiy-scheme) allows [Individuals](Definitions.md#individual) to connect with a [Data Provider](Definitions.md#data-provider) and get access to his [Personal Data](Definitions.md#personal-data) in many different ways, but the [Individual](Definitions.md#individual) in this scenario does so as follows:
* The [Individual](Definitions.md#individual) starts the previously installed [Qiy Application](Definitions.md#qiy-application) and enters the passcode.
* The [Qiy Application](Definitions.md#qiy-application) presents an option to connect with a specific [Data Provider](Definitions.md#data-provider). 
* The [Individual](Definitions.md#individual) selects the option to connect with the [Data Provider](Definitions.md#data-provider).
* The [Qiy Application](Definitions.md#qiy-application) retrieves a [Connect Token](Definitions.md#connect-token) from the [Qiy Trust Network](Definitions.md#qiy-trust-network).
* The [Qiy Application](Definitions.md#qiy-application) redirects the [Individual](Definitions.md#individual) to a webpage of the [Data Provider](Definitions.md#data-provider) while passing the [Connect Token](Definitions.md#connect-token) in the webpage address.
* The [Individual](Definitions.md#individual) has an account with the [Data Provider](Definitions.md#data-provider) and uses his credentials to sign on.
* The [Data Provider](Definitions.md#data-provider) verifies the credentials and looks up the local account id.
* The [Data Provider](Definitions.md#data-provider) asks the [Qiy Trust Network](Definitions.md#qiy-trust-network) to create a [Connection](Definitions.md#connection) using the [Connect Token](Definitions.md#connect-token) which was included in the webpage address.
* The [Qiy Trust Framework](Definitions.md#qiy-trust-framework) creates the [Connection](Definitions.md#connection) with the [Indivdidual](Definitions.md#indivdidual) and returns the [Connection Uri](Definitions.md#connection-uri).
* The [Data Provider](Definitions.md#data-provider) persists the relation between the local account id and the [Connection Uri](Definitions.md#connection-uri). 
* The [Data Provider](Definitions.md#data-provider) informs the [Individual](Definitions.md#individual) that he can control his [Personal Data](Definitions.md#personal-data) via Qiy and redirects him back to his [Qiy Application](Definitions.md#qiy-application).


# 7 Individual Connects with Relying Party

This chapter describes a scenario in which an [Individual](Definitions.md#individual) connects with a [Relying Party](Definitions.md#relying-party) as an introduction to the full description provided in [UC02 Connect with Qiy User](./use-cases/UC02%20Connect%20with%20Qiy%20User.md).

tbd


# 8 Relying Party Requests Personal Data

This chapter describes how Relying Parties generally acquire [Personal Data](Definitions.md#personal-data) as an introduction to the full description provided in [UC03 Request Personal Data](./use-cases/UC03%20Request%20Personal%20Data.md).

tbd



