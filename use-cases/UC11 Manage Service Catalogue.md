# UC11 Manage Service Catalogue


# Abstract

This document describes how [Service Providers](../Qiy%20Node%20Protocol.md#service-provider) and [Access Providers](../Qiy%20Node%20Protocol.md#access-provider) manage [Service Catalogues](../Qiy%20Node%20Protocol.md#service-catalogue).


# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow: Service Provider registers a Service](#basic-flow-service-provider-registers-a-service)
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
	1. [E1. The Service Provider unregisters a Service](#e1-the-service-provider-unregisters-a-service)
1. [Diagram Source Code](#diagram-source-code)
	1. [Register Service](#register-service)
	1. [Unregister Service](#unregister-service)


# Primary Actors

* [Service Provider](../Qiy%20Node%20Protocol.md#service-provider)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)


# Preconditions

1. [Service Provider](../Qiy%20Node%20Protocol.md#service-provider) has access to the [Qiy Trust Network](../Definitions.md#qiy-trust-network).


# Basic Flow: Service Provider registers a Service

The [Service Provider](../Qiy%20Node%20Protocol.md#service-provider) can register a [Service](../Qiy%20Node%20Protocol.md#service) using a [Published Service Register Request](../Qiy%20Node%20Protocol.md#published-service-register-request).

![Register Service](../images/Register_Service_-_UC11.png)


# Postconditions

1. The [Service](../Qiy%20Node%20Protocol.md#service) is included in the [Service Catalogue](../Qiy%20Node%20Protocol.md#service-catalogue) of the [Service Provider](../Qiy%20Node%20Protocol.md#service-provider).


# Extensions

## E1. The Service Provider unregisters a Service

The [Service Provider](../Qiy%20Node%20Protocol.md#service-provider) can unregister a [Service](../Qiy%20Node%20Protocol.md#service) using a [Published Service Unregister Request](../Qiy%20Node%20Protocol.md#published-service-unregister-request).

![Unregister Service](../images/Unregister_Service_-_UC11.png)


# Diagram Source Code

## Register Service

![Register Service](../images/Register_Service_-_UC11.png)

```
title "Register Service"

participant "Qiy User"          as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Registration
QTF  ->  QTF  : 2 Register Service
```

## Unregister Service

![Unregister Service](../images/Unregister_Service_-_UC11.png)

```
title "Unregister Service"

participant "Qiy User"          as User
participant "Qiy Trust Network" as QTF

User ->  QTF  : 1 Request Unregistration
QTF  ->  QTF  : 2 Unregister Service
```

