# UC11 Manage Service Catalogue


# Abstract

This document describes how [Service Providers] and [Access Providers] manage [Service Catalogues].


# Contents

${toc}


# Primary Actors

* [Service Provider]
* [Qiy Trust Network]


# Preconditions

1. [Service Provider] has access to the [Qiy Trust Network].


# Basic Flow: Service Provider registers a Service

The [Service Provider] can register a [Service] using a [Catalogue Register Request].

![Register Service](../images/Register_Service_-_UC11.png)


# Postconditions

1. The [Service] is included in the [Service Catalogue] of the [Service Provider].


# Extensions

## E1. The Service Provider unregisters a Service

The [Service Provider] can uregister a [Service] using a [Catalogue Unregister Request].

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

