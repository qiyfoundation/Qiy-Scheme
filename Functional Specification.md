# FUNCTIONAL SPECIFICATION 'QIY SCHEME V1.1'
From [Qiy Nodes](Definitions.md#qiy-node) to [Data](Definitions.md#data) exchange


# Contents

1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Reader guidance](#12-reader-guidance)
1. [Overview](#2-overview)
	1. [Data Reuse](#21-data-reuse)

# 1 Introduction

tbd

## 1.1 Purpose

tbd

## 1.2 Reader guidance

tbd

# 2 Overview

This chapter gives an overview of this document.
* tbd

## 2.1 Data Reuse

This chapter describes a typical data reuse scenario as an introduction to the full functional description provided by the [Use Cases](Definitions.md#use-case) listed in [UC00 Use Cases Overview](./use-cases/UC00%20Use%20Cases%20Overview.md).
Qiy can also be used for many other applications, examples of wich can be found in [Example Applications](example-applications/Example%20Applications.md).

In this scenario a [Data Subject](Definitions.md#data-subject) ([Individual](Definitions.md#individual)) reuses his [Personal Data](Definitions.md#personal-data) stored at one organization ([Data Provider](Definitions.md#data-provider)) and provides it to another organization ([Relying Party](Definitions.md#relying-party)) to consume one of its [Services](Definitions.md#service). This goes as follows:
* The [Individual](Definitions.md#individual) connects with a [Relying Party](Definitions.md#relying-party) and subscribes to one its [Services](Definitions.md#service) with the necessary and/or optional [Consents](Definitions.md#consent), see [UC17 Qiy User Connects](./use-cases/UC17%20Qiy%20User%20Connects.md) and [UC59 Individual Subscribes to Service](./use-cases/UC59%20Individual%20Subscribes%20to%20Service.md).
* The [Relying Party](Definitions.md#relying-party) asks the [Qiy Trust Framework](Definitions.md#qiy-trust-framework) for [Personal Data](Definitions.md#personal-data) of the [Individual](Definitions.md#individual), see [UC34 Qiy User Requests Data](./use-cases/UC34%20Qiy%20User%20Requests%20Data.md).
* The [Qiy Trust Framework](Definitions.md#qiy-trust-framework) returns a [Data Reference](Definitions.md#data-reference).
* The [Relying Party](Definitions.md#relying-party) asks the [Qiy Trust Framework](Definitions.md#qiy-trust-framework) to resolve the [Data Reference](Definitions.md#data-reference), see [UC36 Qiy User Resolves Data Reference](./use-cases/UC36%20Qiy%20User%20Resolves%20Data%20Reference.md).
* The [Qiy Trust Framework](Definitions.md#qiy-trust-framework) acquires the [Data](Definitions.md#data) from the [Data Provider](Definitions.md#data-provider) and returns it to the [Relying Party](Definitions.md#relying-party).



