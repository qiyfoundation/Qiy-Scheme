# UC20 Qiy User Requests Connect Token

# Abstract

This document is the use case specification for use case [UC20 Qiy User Requests Connect Token](UC20%20Qiy%20User%20Requests%20Connect%20Token.md).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow](#basic-flow)
	1. [[Qiy User](../Definitions.md#qiy-user) requests [Qiy Trust Network](../Definitions.md#qiy-trust-network) for a [Connect Token](../Definitions.md#connect-token). ](#1-[qiy-user]-requests-[qiy-trust-network]-for-a-[connect-token]-)
	1. [[Qiy Trust Network](../Definitions.md#qiy-trust-network) creates [Connect Token](../Definitions.md#connect-token). ](#2-[qiy-trust-network]-creates-[connect-token]-)
	1. [[Qiy Trust Network](../Definitions.md#qiy-trust-network) returns [Connect Token](../Definitions.md#connect-token). ](#3-[qiy-trust-network]-returns-[connect-token]-)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
	1. [Expiration](#11-expiration)
	1. [Budget](#12-budget)
	1. [Change Connect Token Properties](#13-change-connect-token-properties)

# Primary Actors

* [Qiy User](../Definitions.md#qiy-user)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)

# Preconditions

1. [Qiy User](../Definitions.md#qiy-user) has access to [Qiy Trust Network](../Definitions.md#qiy-trust-network).

# Basic Flow

## 1. [Qiy User](../Definitions.md#qiy-user) requests [Qiy Trust Network](../Definitions.md#qiy-trust-network) for a [Connect Token](../Definitions.md#connect-token). 
## 2. [Qiy Trust Network](../Definitions.md#qiy-trust-network) creates [Connect Token](../Definitions.md#connect-token). 
## 3. [Qiy Trust Network](../Definitions.md#qiy-trust-network) returns [Connect Token](../Definitions.md#connect-token). 

# Postconditions

1. [Qiy User](../Definitions.md#qiy-user) has a new [Connect Token](../Definitions.md#connect-token).
1. The [Connect Token](../Definitions.md#connect-token) can be used to create an unlimited number of [Connections](../Definitions.md#connection).
1. The [Connect Token](../Definitions.md#connect-token) does not expire.

# Extensions

## 1.1 Expiration

The [Qiy User](../Definitions.md#qiy-user) can request for a Connect Token that will expire on a given date and time.

## 1.2 Budget

The [Qiy User](../Definitions.md#qiy-user) can request for a Connect Token that can only be used to create a specific number of [Connections](../Definitions.md#connection).

## 1.3 Change Connect Token Properties

The [Qiy User](../Definitions.md#qiy-user) can change the expiration and/or budget afterwards, see [UC24 Qiy User Changes Connect Token Properties](UC24%20Qiy%20User%20Changes%20Connect%20Token%20Properties.md).
