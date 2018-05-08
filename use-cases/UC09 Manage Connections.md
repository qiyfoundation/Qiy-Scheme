# UC09 Manage Connections

# Abstract

This document describes how a [Qiy User] can manage his [Connections].

# Contents

${toc}

# Primary Actors

* [Qiy User]
* [Qiy Trust Network]

# Preconditions

1. The [Qiy User] has a [Connection].


# Basic Flow: Delete Connection

![Delete Connection](../images/Delete_Connection_-_UC09.png)


## 1. The Qiy User requests the Qiy Trust Network to delete a Connection

The [Qiy User] requests the [Qiy Trust Network] to delete a [Connection] by using its [Connection Uri] in a [Connection Delete Request].

## 2. The Qiy Trust Network deletes the Connection

The [Qiy Trust Network] deletes the [Connection].


# Postconditions

1. The [Connection] does not exist anymore.


# Extensions

## E1 List Connections

A [Qiy User] can list his [Connections] using a [Connections Request].

## E2 Get Connection Details

A [Qiy User] can get the details of a [Connection] using a [Connection Details Request].



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


