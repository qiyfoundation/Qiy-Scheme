# UC10 Manage Connect Tokens

# Abstract

This document describes how a [Qiy User] can manage his [Connect Tokens].

# Contents

${toc}

# Primary Actors

* [Qiy User]
* [Qiy Trust Network]


# Preconditions

1.  The [Qiy User] has a [Connect Token].


# Basic Flow: Delete Connect Token

![Delete Connect Token](../images/Delete_Connect_Token_-_UC10.png)


## 1. The Qiy User requests the Qiy Trust Network to delete a Connect Token

The [Qiy User] requests the [Qiy Trust Network] to delete a [Connect Token] by using its [Connect Token Uri] in a [Connect Token Delete Request].

## 2. The Qiy Trust Network deletes the Connect Token

The [Qiy Trust Network] deletes the [Connect Token].


# Postconditions

1. The [Connect Token] does not exist anymore.


# Extensions


## E1 List Connect Tokens

A [Qiy User] can list his [Connect Tokens] using a [Connect Tokens Request].


## E2 Get Connect Token Details

A [Qiy User] can get the details of a [Connect Token] using a [Connect Token Details Request].


## E3 Update Connect Token

A [Qiy User] can change [Attributes] of a [Connect Token] using a [Connect Token Update Request].


# Diagram Source Code

## Delete Connect Token

![Delete Connect Token](../images/Delete_Connect_Token_-_UC10.png)

```
title "Delete Connect Token"

participant "Qiy User"        as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Deletion
QTF  ->  QTF  : 2 Delete Connect Token
```

