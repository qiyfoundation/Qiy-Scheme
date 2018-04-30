# UC01 Acquire Access to Qiy Trust Network

# Abstract

This document is the use case specification for use case [UC01 Acquire Access to Qiy Trust Network](UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow](#basic-flow)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
1. [Web application](#11-web-application)
1. [Service Provider](#2-service-provider)
1. [Qiy Application](#3-qiy-application)
1. [Qiy Node](#4-qiy-node)
1. [Access Provider](#5-access-provider)
1. [Other extensions](#other-extensions)
1. [Diagram Source Code](#diagram-source-code)
	1. [Individual Acquires Access](#individual-acquires-access)

# Primary Actors

* [Individual](../Definitions.md#individual)
* [Qiy Application](../Definitions.md#qiy-application)

# Preconditions

1. The [Individual](../Definitions.md#individual) wants exclusive access to a new [Qiy Node](../Definitions.md#qiy-node).

# Basic Flow

[Individual](../Definitions.md#individual) acquires access to the [Qiy Trust Network](../Definitions.md#qiy-trust-network)
* with a new [Qiy Node](../Definitions.md#qiy-node) and
* with a new [Qiy Application](../Definitions.md#qiy-application) for smart phones.

1. The [Individual](../Definitions.md#individual) installs a new [Qiy Application](../Definitions.md#qiy-application).
2. The [Individual](../Definitions.md#individual) secures access to the [Qiy Application](../Definitions.md#qiy-application).
3. The [Qiy Application](../Definitions.md#qiy-application) creates [Qiy Node Credentials](../Definitions.md#qiy-node-credentials).
4. The [Qiy Application](../Definitions.md#qiy-application) persists the [Qiy Node Credentials](../Definitions.md#qiy-node-credentials).
5. The [Qiy Application](../Definitions.md#qiy-application) requests the [Qiy Trust Network](../Definitions.md#qiy-trust-network) to create a [Qiy Node](../Definitions.md#qiy-node).

![Individual Acquires Access](../images/Individual_Acquires_Access_-_UC01.png)

# Postconditions

1. The [Individual](../Definitions.md#individual) has exclusive access to a new [Qiy Application](../Definitions.md#qiy-application).
1. The [Individual](../Definitions.md#individual) has exclusive access to a new [Qiy Node](../Definitions.md#qiy-node).
1. The [Qiy Application](../Definitions.md#qiy-application) has exclusive access to the [Qiy Node](../Definitions.md#qiy-node).


# Extensions

# 1.1 Web application

The flow for Web applications is the same as the basic flow but for the first step:

1. The [Individual](../Definitions.md#individual) registers an account for the [Qiy Application](../Definitions.md#qiy-application).
2. The [Individual](../Definitions.md#individual) secures access to the [Qiy Application](../Definitions.md#qiy-application).
3. The [Qiy Application](../Definitions.md#qiy-application) creates [Qiy Node Credentials](../Definitions.md#qiy-node-credentials).
4. The [Qiy Application](../Definitions.md#qiy-application) persists the [Qiy Node Credentials](../Definitions.md#qiy-node-credentials).
5. The [Qiy Application](../Definitions.md#qiy-application) requests the [Qiy Trust Network](../Definitions.md#qiy-trust-network) to create a [Qiy Node](../Definitions.md#qiy-node).

# 2 Service Provider

tbd

# 3 Qiy Application

tbd

# 4 Qiy Node

tbd

# 5 Access Provider

tbd

# Other extensions

Please refer to [UC08 Manage Access to Qiy Trust Network](UC08%20Manage%20Access%20to%20Qiy%20Trust%20Network.md).

# Diagram Source Code

## Individual Acquires Access

```
title "Individual Acquires Access"

participant "Individual"        as User
participant "Qiy Application"   as App
participant "Qiy Trust Network" as QTN

User -> App  : 1 Install
User -> App  : 2 Secure Access
App  -> App  : 3 Create Qiy Node Credentials
App  -> App  : 4 Persist Qiy Node Credentials
App  -> QTN   : 5 Create Qiy Node
```
