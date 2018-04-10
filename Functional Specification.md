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
*   The [Data Provider](Definitions.md#data-provider) configures his Applications with the [Qiy Node Credentials](Definitions.md#qiy-node-credential) and gains physical access the [Qiy Trust Network](Definitions.md#qiy-trust-network).
*   The [Data Provider](Definitions.md#data-provider) publishes its [Service Catalogue](Definitions.md#service-catalogue) in the [Service Library](Definitions.md#service-library).


# 4 Individual Acquires Access to Qiy Trust Network

This chapter describes how Individuals generally acquire access to the Qiy Trust Network as an introduction to the full description provided in [UC01 Acquire Access to Qiy Trust Network](./use-cases/UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

tbd

# 5 Relying Party Acquires Access to Qiy Trust Network

This chapter describes how Relying Parties generally acquire access to the Qiy Trust Network as an introduction to the full description provided in [UC01 Acquire Access to Qiy Trust Network](./use-cases/UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

tbd


# 6 Individual Connects with Data Provider

This chapter describes how Individuals generally connect with a [Data Provider](Definitions.md#data-provider) as an introduction to the full description provided in [UC02 Connect with Qiy User](./use-cases/UC02%20Connect%20with%20Qiy%20User.md).

tbd


# 7 Individual Connects with Relying Party

This chapter describes how Individuals generally connect with a [Data Provider](Definitions.md#data-provider) as an introduction to the full description provided in [UC02 Connect with Qiy User](./use-cases/UC02%20Connect%20with%20Qiy%20User.md).

tbd


# 8 Relying Party Requests Personal Data

This chapter describes how Relying Parties generally acquire [Personal Data](Definitions.md#personal-data) as an introduction to the full description provided in [UC03 Request Personal Data](./use-cases/UC03%20Request%20Personal%20Data.md).

tbd



