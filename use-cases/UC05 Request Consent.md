# UC05 Request Consent

# Abstract

This document describes how a [Relying Party](../Definitions.md#relying-party) can acquire [Consent](../Definitions.md#consent) to use [Personal Data](../Definitions.md#personal-data) of an [Individual](../Definitions.md#individual).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow](#basic-flow)
	1. [](#1-)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
	1. [](#11-)

# Primary Actors

* [Individual](../Definitions.md#individual)
* [Data Provider](../Definitions.md#data-provider)
* [Relying Party](../Definitions.md#relying-party)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)

# Preconditions

 Condition   | [Data Provider](../Definitions.md#data-provider) | [Relying Party](../Definitions.md#relying-party) | [Individual](../Definitions.md#individual)
------------ | --------------- | --------------- | ------------
1. The [Data Provider](../Definitions.md#data-provider) has [Personal Data](../Definitions.md#personal-data) of the [Individual](../Definitions.md#individual).                                | X |   | X
2. The [Individual](../Definitions.md#individual) has a [Connection](../Definitions.md#connection) with the [Data Provider](../Definitions.md#data-provider) and knows its [Persistent Id](../Definitions.md#persistent-id). | X |   | X
3. The [Data Provider](../Definitions.md#data-provider) has a [Connection](../Definitions.md#connection) with the [Individual](../Definitions.md#individual) and knows its [Persistent Id](../Definitions.md#persistent-id). | X |   | X
4. The [Data Provider](../Definitions.md#data-provider) knows the (local) [Identity](../Definitions.md#identity) of the [Individual](../Definitions.md#individual).                       | X |   | X
5. The [Individual](../Definitions.md#individual) has a [Connection](../Definitions.md#connection) with the [Relying Party](../Definitions.md#relying-party) and knows its [Persistent Id](../Definitions.md#persistent-id). |   | X | X
6. The [Relying Party](../Definitions.md#relying-party) has a [Connection](../Definitions.md#connection) with the [Individual](../Definitions.md#individual) and knows its [Persistent Id](../Definitions.md#persistent-id). |   | X | X
7. The [Relying Party](../Definitions.md#relying-party) knows the (local) [Identity](../Definitions.md#identity) of the [Individual](../Definitions.md#individual).                       |   | X | X
8. The [Relying Party](../Definitions.md#relying-party) has a [Data Reference](../Definitions.md#data-reference) to acquire the [Personal Data](../Definitions.md#personal-data).                  |   | X | 

# Basic Flow

## 1. 

# Postconditions

1.

# Extensions

## 1.1

