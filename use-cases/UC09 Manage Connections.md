# UC09 Manage Connections

# Abstract

This document describes how a [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user) can manage his [Connections](../Qiy%20Node%20Protocol.md#connection).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow: Delete Connection](#basic-flow-delete-connection)
	1. [The Qiy User requests the Qiy Trust Network to delete a Connection](#1-the-qiy-user-requests-the-qiy-trust-network-to-delete-a-connection)
	1. [The Qiy Trust Network deletes the Connection](#2-the-qiy-trust-network-deletes-the-connection)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
	1. [E1 List Connections](#e1-list-connections)
	1. [E2 Get Connection Details](#e2-get-connection-details)
1. [Diagram Source Code](#diagram-source-code)
	1. [Delete Connection](#delete-connection)

# Primary Actors

* [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)

# Preconditions

1. The [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user) has a [Connection](../Qiy%20Node%20Protocol.md#connection).


# Basic Flow: Delete Connection

![Delete Connection](../images/Delete_Connection_-_UC09.png)


## 1. The Qiy User requests the Qiy Trust Network to delete a Connection

The [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user) requests the [Qiy Trust Network](../Definitions.md#qiy-trust-network) to delete a [Connection](../Qiy%20Node%20Protocol.md#connection) using a [Connection Delete Request](../Qiy%20Node%20Protocol.md#connection-delete-request).

## 2. The Qiy Trust Network deletes the Connection

The [Qiy Trust Network](../Definitions.md#qiy-trust-network) deletes the [Connection](../Qiy%20Node%20Protocol.md#connection).


# Postconditions

1. The [Connection](../Qiy%20Node%20Protocol.md#connection) does not exist anymore.


# Extensions

## E1 List Connections

A [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user) can list his [Connections](../Qiy%20Node%20Protocol.md#connection) using a [Connections Request](../Qiy%20Node%20Protocol.md#connections-request).

## E2 Get Connection Details

A [Qiy User](../Qiy%20Node%20Protocol.md#qiy-user) can get the details of a [Connection](../Qiy%20Node%20Protocol.md#connection) using a [Connection Details Request](../Qiy%20Node%20Protocol.md#connection-details-request).



# Diagram Source Code

## Delete Connection

![Delete Connection](../images/Delete_Connection_-_UC09.png)

```
title "Delete Connection"

participant "Qiy User"        as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Deletion
QTF  ->  QTF  : 2 Delete Connection
```


