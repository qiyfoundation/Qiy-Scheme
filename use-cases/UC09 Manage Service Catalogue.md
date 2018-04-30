# UC09 Manage Service Catalogue

# Abstract

This document is the use case specification for use case [UC09 Manage Service Catalogue](UC09%20Manage%20Service%20Catalogue.md).

# Contents


1. [Primary Actors](#primary-actors)
1. [Preconditions](#preconditions)
1. [Basic Flow](#basic-flow)
	1. [The [Service Provider](../Definitions.md#service-provider) registers a [Service](../Definitions.md#service)](#1-the-[service-provider](definitionsmd#service-provider)-registers-a-[service](definitionsmd#service))
1. [Postconditions](#postconditions)
1. [Extensions](#extensions)
	1. [The [Service Provider](../Definitions.md#service-provider) unregisters a [Service](../Definitions.md#service)](#2-the-[service-provider](definitionsmd#service-provider)-unregisters-a-[service](definitionsmd#service))

# Primary Actors

* [Service Provider](../Definitions.md#service-provider) - a [Data Provider](../Definitions.md#data-provider) or a [Relying Party](../Definitions.md#relying-party)
* [Qiy Trust Network](../Definitions.md#qiy-trust-network)

# Preconditions

1. [Service Provider](../Definitions.md#service-provider) has access to the [Qiy Trust Network](../Definitions.md#qiy-trust-network), see [UC01 Acquire Access to Qiy Trust Network](UC01%20Acquire%20Access%20to%20Qiy%20Trust%20Network.md).

# Basic Flow

## 1. The [Service Provider](../Definitions.md#service-provider) registers a [Service](../Definitions.md#service)

* The [Service Provider](../Definitions.md#service-provider) issues a [Service Register Request](../Definitions.md#service-register-request) containing a [Service Descriptor](../Definitions.md#service-descriptor) of the [Service](../Definitions.md#service).
* The [Qiy Trust Network](../Definitions.md#qiy-trust-network) adds the [Service Descriptor](../Definitions.md#service-descriptor) to the [Service Catalogue](../Definitions.md#service-catalogue) of the [Service Provider](../Definitions.md#service-provider).


# Postconditions

1. The [Service](../Definitions.md#service) is included in the [Service Catalogue](../Definitions.md#service-catalogue) of the [Service Provider](../Definitions.md#service-provider).

# Extensions

## 2. The [Service Provider](../Definitions.md#service-provider) unregisters a [Service](../Definitions.md#service)

* The [Service Provider](../Definitions.md#service-provider) issues a [Service Unregister Request](../Definitions.md#service-unregister-request) containing a [Service Descriptor](../Definitions.md#service-descriptor) of the [Service](../Definitions.md#service).
* The [Qiy Trust Network](../Definitions.md#qiy-trust-network) removes the [Service Descriptor](../Definitions.md#service-descriptor) from the [Service Catalogue](../Definitions.md#service-catalogue) of the [Service Provider](../Definitions.md#service-provider).


