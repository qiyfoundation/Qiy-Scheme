# UC12 Manage Access to Qiy Trust Network

# Abstract

This document describe how [Qiy Users] and [Access Providers] manage the access to the [Qiy Trust Network].

# Contents

${toc}

# Primary Actors

* [Qiy User]
* [Qiy Trust Network]

# Preconditions

1. The [Qiy User] has access to the [Qiy Trust Network] via one [Qiy Node].


# Basic Flow: Qiy User deletes Qiy Node

![Delete Qiy Node](../images/Delete_Qiy_Node_-_UC12.png)

## 1. The Qiy User requests the Qiy Trust Network to delete a Qiy Node

The [Qiy User] requests the [Qiy Trust Network] to delete a [Qiy Node] using a [Qiy Node Delete Request].

## 2. The Qiy Trust Network deletes the Qiy Node

The [Qiy Trust Network] deletes the [Qiy Node].


# Postconditions

1. The [Qiy User] does not have access to the [Qiy Trust Network].


# Extensions

## E1 Application Management

tbd

## E2 Qiy Node Management

tbd

## E3 Service Provider Management

tbd


# Diagram Source Code

## Delete Qiy Node

![Delete Qiy Node](../images/Delete_Qiy_Node_-_UC12.png)

```
title "Delete Qiy Node"

participant "Qiy User"          as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Deletion
QTF  ->  QTF  : 2 Delete Qiy Node
```

