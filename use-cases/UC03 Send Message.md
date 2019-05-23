# UC03 Send Message

# Abstract

This document describes how [Qiy Users](../Definitions.md#qiy-user) can exchange [Qiy Node Messages](../Definitions.md#qiy-node-message).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow: Send Qiy Node Message](#basic-flow-send-qiy-node-message)
	1. [The Sender requests the Qiy Trust Network for the Connection Uri](#1-the-sender-requests-the-qiy-trust-network-for-the-connection-uri)
	1. [The Sender posts the Qiy Node Message](#2-the-sender-posts-the-qiy-node-message)
	1. [The Qiy Trust Network transports the Qiy Node Message](#3-the-qiy-trust-network-transports-the-qiy-node-message)
	1. [The Qiy Trust Network notifies the receipt of the message to the Receiver](#4-the-qiy-trust-network-notifies-the-receipt-of-the-message-to-the-receiver)
	1. [The Receiver fetches the Qiy Node Message from the Qiy Trust Network](#5-the-receiver-fetches-the-qiy-node-message-from-the-qiy-trust-network)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
1. [Sender sends a reply message](#21-sender-sends-a-reply-message)
1. [Diagram Source Code](#diagram-source-code)
	1. [Send Message](#send-message)

# Primary Actors

* [Sender](../Definitions.md#sender): a [Qiy User](../Definitions.md#qiy-user)
* [Receiver](../Definitions.md#receiver): a [Qiy User](../Definitions.md#qiy-user)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)

# Preconditions

1. The [Sender](../Definitions.md#sender) has access to the [Qiy Trust Network](../Definitions.md#qiy-trust-network).
1. The [Receiver](../Definitions.md#receiver) has access to the [Qiy Trust Network](../Definitions.md#qiy-trust-network).
1. The [Sender](../Definitions.md#sender) and [Receiver](../Definitions.md#receiver) have a [Connection](../Definitions.md#connection).
1. The [Sender](../Definitions.md#sender) knows the [Persistent Id](../Qiy%20Node%20Protocol.md#persistent-id) of the [Connection](../Qiy%20Node%20Protocol.md#connection) with the [Receiver](../Definitions.md#receiver).
1. The [Receiver](../Definitions.md#receiver) knows the [Persistent Id](../Qiy%20Node%20Protocol.md#persistent-id) of the [Connection](../Qiy%20Node%20Protocol.md#connection) with the [Sender](../Definitions.md#sender).
1. The [Message Descriptor](../Qiy%20Node%20Protocol.md#message-descriptor) has been registered with the [Service Library](../Qiy%20Node%20Protocol.md#service-library).

# Basic Flow: Send Qiy Node Message

![Send Message](../images/Send_Message_-_UC03.png)

## 1. The Sender requests the Qiy Trust Network for the Connection Uri

The [Sender](../Definitions.md#sender) requests the [Qiy Trust Network](../Definitions.md#qiy-trust-network) for the [Connection Uri](../Definitions.md#connection-uri) of the [Connection](../Qiy%20Node%20Protocol.md#connection) with the [Receiver](../Definitions.md#receiver) using the [Persistent Id](../Qiy%20Node%20Protocol.md#persistent-id) of the [Connection](../Qiy%20Node%20Protocol.md#connection) in a [Connections Request](../Qiy%20Node%20Protocol.md#connections-request).

## 2. The Sender posts the Qiy Node Message

The [Sender](../Definitions.md#sender) posts the [Qiy Node Message](../Qiy%20Node%20Protocol.md#qiy-node-message) using the [Connection Uri](../Definitions.md#connection-uri) of the [Connection](../Qiy%20Node%20Protocol.md#connection) in a [Message Post Request](../Qiy%20Node%20Protocol.md#message-post-request).
The [Sender](../Definitions.md#sender) does not specify the [Reference Serial Number](../Definitions.md#reference-serial-number) of the [Qiy Node Message](../Qiy%20Node%20Protocol.md#qiy-node-message).

## 3. The Qiy Trust Network transports the Qiy Node Message

The [Qiy Trust Network](../Definitions.md#qiy-trust-network) transports the [Qiy Node Message](../Qiy%20Node%20Protocol.md#qiy-node-message) to (the [Qiy Node](../Definitions.md#qiy-node) of) the [Receiver](../Definitions.md#receiver).

## 4. The Qiy Trust Network notifies the receipt of the message to the Receiver

The [Qiy Trust Network](../Definitions.md#qiy-trust-network) notifies the receipt of the message to the [Receiver](../Definitions.md#receiver) with a [Message Received Event](../Qiy%20Node%20Protocol.md#message-received-event) containing a [Connection Uri](../Definitions.md#connection-uri) of the [Connection](../Qiy%20Node%20Protocol.md#connection) over which is was received.

## 5. The Receiver fetches the Qiy Node Message from the Qiy Trust Network

The [Receiver](../Definitions.md#receiver) fetches the [Qiy Node Message](../Qiy%20Node%20Protocol.md#qiy-node-message) from the [Qiy Trust Network](../Definitions.md#qiy-trust-network) with a [Messages Request](../Qiy%20Node%20Protocol.md#messages-request) after retreiving the required [Mailbox Url](../Qiy%20Node%20Protocol.md#mailbox-url) of the [Connection](../Qiy%20Node%20Protocol.md#connection) using a [Connection Details Request](../Qiy%20Node%20Protocol.md#connection-details-request).


# Postconditions

1. The [Receiver](../Definitions.md#receiver) has received the message.

# Extensions

# 2.1 Sender sends a reply message

The [Sender](../Definitions.md#sender) can send a reply message by referencing the [Serial Number](../Qiy%20Node%20Protocol.md#serial-number) of the [Qiy Node Message](../Qiy%20Node%20Protocol.md#qiy-node-message) that he replies to in the [Reference Serial Number](../Qiy%20Node%20Protocol.md#reference-serial-number). 


# Diagram Source Code

## Send Message

![Send Message](../images/Send_Message_-_UC03.png)

```
title "Send Message"

participant "Sender"            as S
participant "Qiy Trust Network" as QTN
participant "Receiver"          as R

S   -> QTN : 1 Request Connection Uri
S   -> QTN : 2 Post message
QTN -> QTN : 3 Transport message
QTN -> R   : 4 Notify receipt
R   -> QTN : 5 Get message
```

