# UC08 Manage Messages

# Abstract

This document describes how a [Qiy User] can manage his [Qiy Node Messages].

# Contents

${toc}

# Primary Actors

* [Qiy User]
* [Qiy Trust Network]

# Preconditions

1. The [Qiy User] has exchanged a [Qiy Node Message].


# Basic Flow: Delete Message

![Delete Message](../images/Delete_Message-_UC08.png)


## 1. The Qiy User requests the Qiy Trust Network to delete a Message

The [Qiy User] requests the [Qiy Trust Network] to delete a [Qiy Node Message] by using its [Message Uri] in a [Message Delete Request].

## 2. The Qiy Trust Network deletes the Message

The [Qiy Trust Network] deletes the [Qiy Node Message].


# Postconditions

1. The [Qiy Node Message] does not exist anymore.


# Extensions

## E1 List Messages

A [Qiy User] can list his [Qiy Node Messages] using a [Messages Request].

## E2 Get Message Details

A [Qiy User] can get the details of a [Qiy Node Message] using a [Message Details Request].



# Diagram Source Code

## Delete Message

![Delete Message](../images/Delete_Message-_UC08.png)

```
title "Delete Message"

participant "Qiy User"        as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Deletion
QTF  ->  QTF  : 2 Delete Message
```


