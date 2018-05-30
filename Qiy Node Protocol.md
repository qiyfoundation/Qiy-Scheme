# Qiy Node Protocol

# Abstract

This document describes the [Qiy Node Protocol](#qiy-node-protocol): the lifecycle, [requests](#request), [events](#event), [models](#model) and [messages](#message) of the [Qiy Node](Definitions.md#qiy-node) and their realization.
The document refers for details to the [Qiy Node API](#qiy-node-api), which is available in [Open API Specification](https://swagger.io/specification/)-format.

The api can be viewed with the online editor at [https://editor2.swagger.io/#!/](https://editor2.swagger.io/#!/). Either import the .json file or use 'File'->'Import url...' with:

https://raw.githubusercontent.com/qiyfoundation/Qiy-Scheme/topic/qiy-node-interface/qiy-node-api.json

# Contents


1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Readers' Guidance](#12-readers-guidance)
	1. [Overview](#13-overview)
1. [Requests](#2-requests)
	1. [General](#21-general)
		1. [Health Check](#211-health-check)
		1. [Versions](#212-versions)
		1. [Dynamic Path Endpoint Addresses](#213-dynamic-path-endpoint-addresses)
		1. [Authentication](#214-authentication)
			1. [Java](#2141-java)
			1. [Python](#2142-python)
	1. [Catalogue Requests](#22-catalogue-requests)
		1. [Catalogue Details Request](#221-catalogue-details-request)
		1. [Catalogues Request](#222-catalogues-request)
		1. [Published Service Details Request](#223-published-service-details-request)
		1. [Published Service Register Request](#224-published-service-register-request)
		1. [Published Service Unregister Request](#225-published-service-unregister-request)
		1. [Published Services Request](#226-published-services-request)
	1. [Connect Token Requests](#23-connect-token-requests)
		1. [Connect Token Create Request](#231-connect-token-create-request)
		1. [Connect Token Delete Request](#232-connect-token-delete-request)
		1. [Connect Token Details Request](#233-connect-token-details-request)
		1. [Connect Token Register Request](#234-connect-token-register-request)
		1. [Connect Token Update Request](#235-connect-token-update-request)
		1. [Connect Tokens Request](#236-connect-tokens-request)
	1. [Connection Requests](#24-connection-requests)
		1. [Connection Create Request](#241-connection-create-request)
		1. [Connection Delete Request](#242-connection-delete-request)
		1. [Connection Details Request](#243-connection-details-request)
		1. [Connections Request](#244-connections-request)
			1. [Example Connections Request](#2441-example-connections-request)
	1. [Consent Requests](#25-consent-requests)
		1. [Consent Delete Request](#251-consent-delete-request)
		1. [Consent Denied Request](#252-consent-denied-request)
		1. [Consent Details Request](#253-consent-details-request)
		1. [Consent Granted Request](#254-consent-granted-request)
		1. [Consent Withdrawn Request](#255-consent-withdrawn-request)
		1. [Consents Request](#256-consents-request)
	1. [Event Requests](#26-event-requests)
		1. [Events Request](#261-events-request)
	1. [Library Requests](#27-library-requests)
		1. [Data Type Details Request](#271-data-type-details-request)
		1. [Data Type Register Request](#272-data-type-register-request)
		1. [Data Type Unregister Request](#273-data-type-unregister-request)
		1. [Data Type Update Request](#274-data-type-update-request)
		1. [Data Types Request](#275-data-types-request)
		1. [Library Details Request](#276-library-details-request)
		1. [Message Type Details Request](#277-message-type-details-request)
		1. [Message Type Register Request](#278-message-type-register-request)
		1. [Message Type Unregister Request](#279-message-type-unregister-request)
		1. [Message Type Update Request](#2710-message-type-update-request)
		1. [Message Types Request](#2711-message-types-request)
		1. [Operation Type Details Request](#2712-operation-type-details-request)
		1. [Operation Type Register Request](#2713-operation-type-register-request)
		1. [Operation Type Unregister Request](#2714-operation-type-unregister-request)
		1. [Operation Type Update Request](#2715-operation-type-update-request)
		1. [Operation Types Request](#2716-operation-types-request)
		1. [Published Provider Details Request](#2717-published-provider-details-request)
		1. [Published Provider Register Request](#2718-published-provider-register-request)
		1. [Published Provider Unregister Request](#2719-published-provider-unregister-request)
		1. [Published Provider Update Request](#2720-published-provider-update-request)
		1. [Published Providers Request](#2721-published-providers-request)
		1. [Service Type Details Request](#2722-service-type-details-request)
		1. [Service Type Register Request](#2723-service-type-register-request)
		1. [Service Type Unregister Request](#2724-service-type-unregister-request)
		1. [Service Type Update Request](#2725-service-type-update-request)
		1. [Service Types Request](#2726-service-types-request)
	1. [Message Requests](#28-message-requests)
		1. [Message Delete Request](#281-message-delete-request)
		1. [Message Details Request](#282-message-details-request)
		1. [Message Post Request](#283-message-post-request)
		1. [Messages Request](#284-messages-request)
	1. [Operation Requests](#29-operation-requests)
		1. [Operation Execute Request](#291-operation-execute-request)
		1. [Operation Reference Request](#292-operation-reference-request)
		1. [Operation Register Request](#293-operation-register-request)
	1. [Portfolio Requests](#210-portfolio-requests)
		1. [Account Details Request](#2101-account-details-request)
		1. [Account Register Request](#2102-account-register-request)
		1. [Account Unregister Request](#2103-account-unregister-request)
		1. [Account Update Request](#2104-account-update-request)
		1. [Accounts Request](#2105-accounts-request)
		1. [Portfolio Details Request](#2106-portfolio-details-request)
		1. [Subscription Details Request](#2107-subscription-details-request)
		1. [Subscription Register Request](#2108-subscription-register-request)
		1. [Subscription Unregister Request](#2109-subscription-unregister-request)
		1. [Subscriptions Request](#21010-subscriptions-request)
	1. [Qiy Node Requests](#211-qiy-node-requests)
		1. [Qiy Node Create Request](#2111-qiy-node-create-request)
		1. [Qiy Node Delete Request](#2112-qiy-node-delete-request)
	1. [Source Requests](#212-source-requests)
		1. [Candidates Request](#2121-candidates-request)
		1. [Operation Details Request](#2122-operation-details-request)
		1. [Operation Register Request](#2123-operation-register-request)
		1. [Operation Unregister Request](#2124-operation-unregister-request)
		1. [Operation Update Request](#2125-operation-update-request)
		1. [Operations Request](#2125-operations-request)
		1. [Source Details Request](#2127-source-details-request)
		1. [Source Register Request](#2128-source-register-request)
		1. [Source Unregister Request](#2129-source-unregister-request)
		1. [Source Update Request](#21210-source-update-request)
		1. [Service Credential Details Request](#21211-service-credential-details-request)
		1. [Service Credential Register Request](#21212-service-credential-register-request)
		1. [Service Credential Unregister Request](#21213-service-credential-unregister-request)
		1. [Service Credential Update Request](#21214-service-credential-update-request)
		1. [Service Credentials Request](#21215-service-credentials-request)
1. [Events](#3-events)
	1. [Connection Events](#31-connection-events)
		1. [Connection Created Event](#311-connection-created-event)
	1. [Consent Events](#32-consent-events)
		1. [Consent Denied Event](#321-consent-denied-event)
		1. [Consent Granted Event](#322-consent-granted-event)
	1. [Message Events](#33-message-events)
		1. [Message Received Event](#331-message-received-event)
	1. [Persistent Id Events](#34-persistent-id-events)
		1. [Persistent Id Event](#341-persistent-id-event)
1. [Messages](#4-messages)
	1. [Consent Messages](#41-consent-messages)
		1. [Consent Notification Message](#411-consent-notification-message)
		1. [Consent Request Message](#412-consent-request-message)
	1. [Operation Messages](#42-operation-messages)
		1. [Operation Reference Message](#421-operation-reference-message)
		1. [Operation Reference Request Message](#422-operation-reference-request-message)
		1. [Operation Specification Request Message](#423-operation-specification-request-message)
	1. [Portfolio Messages](#43-portfolio-messages)
		1. [Portfolio Register Message](#431-portfolio-register-message)
	1. [Service Credential Messages](#44-service-credential-messages)
		1. [Service Credential Request Message](#441-service-credential-request-message)
	1. [Source Messages](#45-source-messages)
		1. [Candidates Message](#451-candidates-message)
1. [Models](#5-models)
	1. [Account Model](#51-account-model)
		1. [Account Attributes](#511-account-attributes)
		1. [Account Relations](#512-account-relations)
		1. [Account Business Rules](#513-account-business-rules)
	1. [Candidate Model](#52-candidate-model)
		1. [Candidate Attributes](#521-candidate-attributes)
		1. [Candidate Relations](#522-candidate-relations)
		1. [Candidate Business Rules](#523-candidate-business-rules)
	1. [Catalogue Model](#53-catalogue-model)
		1. [Catalogue Attributes](#531-catalogue-attributes)
		1. [Catalogue Relations](#532-catalogue-relations)
		1. [Catalogue Business Rules](#533-catalogue-business-rules)
	1. [Connect Token Model](#54-connect-token-model)
		1. [Connect Token Attributes](#541-connect-token-attributes)
		1. [Connect Token Relations](#542-connect-token-relations)
		1. [Connect Token Business Rules](#543-connect-token-business-rules)
	1. [Connection Model](#55-connection-model)
		1. [Connection Attributes](#551-connection-attributes)
			1. [Mailbox Url](#5511-mailbox-url)
		1. [Connection Relations](#552-connection-relations)
		1. [Connection Business Rules](#553-connection-business-rules)
	1. [Consent Model](#56-consent-model)
		1. [Consent Attributes](#561-consent-attributes)
		1. [Consent Relations](#562-consent-relations)
		1. [Consent Business Rules](#563-consent-business-rules)
	1. [Event Model](#57-event-model)
		1. [Event Attributes](#571-event-attributes)
		1. [Event Relations](#572-event-relations)
		1. [Event Business Rules](#573-event-business-rules)
	1. [Library Model](#58-library-model)
		1. [Library Attributes](#581-library-attributes)
		1. [Library Relations](#582-library-relations)
		1. [Library Business Rules](#583-library-business-rules)
	1. [Message Model](#59-message-model)
		1. [Message Attributes](#591-message-attributes)
		1. [Reference Serial Number](#5911-reference-serial-number)
		1. [Serial Number](#5912-serial-number)
		1. [Message Relations](#592-message-relations)
		1. [Message Business Rules](#593-message-business-rules)
	1. [Message Type Model](#510-message-type-model)
		1. [Message Type Attributes](#5101-message-type-attributes)
		1. [Message Type Relations](#5102-message-type-relations)
		1. [Message Type Business Rules](#5103-message-type-business-rules)
	1. [Operation Model](#511-operation-model)
		1. [Operation Attributes](#5111-operation-attributes)
		1. [Operation Relations](#5112-operation-relations)
		1. [Operation Business Rules](#5113-operation-business-rules)
	1. [Operation Specification Model](#512-operation-specification-model)
		1. [Operation Specification Attributes](#5121-operation-specification-attributes)
		1. [Operation Specification Relations](#5122-operation-specification-relations)
		1. [Operation Specification Business Rules](#5123-operation-specification-business-rules)
	1. [Persistent Id Model](#513-persistent-id-model)
		1. [Persistent Id Relations](#5131-persistent-id-relations)
		1. [Persistent Id Business Rules](#5132-persistent-id-business-rules)
	1. [Portfolio Model](#514-portfolio-model)
		1. [Portfolio Attributes](#5141-portfolio-attributes)
		1. [Portfolio Relations](#5142-portfolio-relations)
		1. [Portfolio Business Rules](#5143-portfolio-business-rules)
	1. [Published Provider Model](#515-published-provider-model)
		1. [Published Provider Attributes](#5151-published-provider-attributes)
		1. [Published Provider Relations](#5152-published-provider-relations)
		1. [Published Provider Business Rules](#5153-published-provider-business-rules)
	1. [Published Service Model](#516-published-service-model)
		1. [Published Service Attributes](#5161-published-service-attributes)
		1. [Published Service Relations](#5162-published-service-relations)
		1. [Published Service Business Rules](#5163-published-service-business-rules)
	1. [Qiy Node Model](#517-qiy-node-model)
		1. [Qiy Node  Attributes](#5171-qiy-node--attributes)
		1. [Qiy Node Relations](#5172-qiy-node-relations)
		1. [Qiy Node Business Rules](#5173-qiy-node-business-rules)
	1. [Qiy Node Credential Model](#518-qiy-node-credential-model)
		1. [Qiy Node Credential Attributes](#5181-qiy-node-credential-attributes)
		1. [Qiy Node Credential Relations](#5182-qiy-node-credential-relations)
		1. [Qiy Node Credential Business Rules](#5183-qiy-node-credential-business-rules)
	1. [Service Description Model](#519-service-description-model)
		1. [Service Description Attributes](#5191-service-description-attributes)
		1. [Service Description Relations](#5192-service-description-relations)
		1. [Service Description Business Rules](#5193-service-description-business-rules)
	1. [Service Type Model](#520-service-type-model)
		1. [Service Type Attributes](#5201-service-type-attributes)
		1. [Service Type Relations](#5202-service-type-relations)
		1. [Service Type Business Rules](#5203-service-type-business-rules)
	1. [Source Model](#521-source-model)
		1. [Source Attributes](#5211-source-attributes)
		1. [Source Relations](#5212-source-relations)
		1. [Source Business Rules](#5213-source-business-rules)
	1. [Subscription Model](#522-subscription-model)
		1. [Subscription Attributes](#5221-subscription-attributes)
		1. [Subscription Relations](#5222-subscription-relations)
		1. [Subscription Business Rules](#5223-subscription-business-rules)
1. [Index](#6-index)
	1. [Access Provider](#access-provider)
	1. [Account](#account)
	1. [Account Details Request](#account-details-request)
	1. [Account Register Request](#account-register-request)
	1. [Account Unregister Request](#account-unregister-request)
	1. [Account Update Request](#account-update-request)
	1. [Accounts Request](#accounts-request)
	1. [Authorization Header Parameter](#authorization-header-parameter)
	1. [Candidate](#candidate)
	1. [Candidates Message](#candidates-message)
	1. [Candidates Request](#candidates-request)
	1. [Catalogue](#catalogue)
	1. [Catalogue Details Request](#catalogue-details-request)
	1. [Catalogues Request](#catalogues-request)
	1. [Connect Token](#connect-token)
	1. [Connect Token Create Request](#connect-token-create-request)
	1. [Connect Token Delete Request](#connect-token-delete-request)
	1. [Connect Token Details Request](#connect-token-details-request)
	1. [Connect Token Register Request](#connect-token-register-request)
	1. [Connect Token Update Request](#connect-token-update-request)
	1. [Connect Tokens Request](#connect-tokens-request)
	1. [Connection](#connection)
	1. [Connection Create Request](#connection-create-request)
	1. [Connection Created Event](#connection-created-event)
	1. [Connection Delete Request](#connection-delete-request)
	1. [Connection Details Request](#connection-details-request)
	1. [Connections Request](#connections-request)
	1. [Consent](#consent)
	1. [Consent Delete Request](#consent-delete-request)
	1. [Consent Denied Event](#consent-denied-event)
	1. [Consent Denied Request](#consent-denied-request)
	1. [Consent Details Request](#consent-details-request)
	1. [Consent Granted Event](#consent-granted-event)
	1. [Consent Granted Request](#consent-granted-request)
	1. [Consent Notification Message](#consent-notification-message)
	1. [Consent Request Message](#consent-request-message)
	1. [Consent Withdrawn Request](#consent-withdrawn-request)
	1. [Consents Request](#consents-request)
	1. [Data Provider](#data-provider)
	1. [Data Reference](#data-reference)
	1. [Data Reference Request](#data-reference-request)
	1. [Data Service](#data-service)
	1. [Data Source](#data-source)
	1. [Data Type](#data-type)
	1. [Data Type Details Request](#data-type-details-request)
	1. [Data Type Register Request](#data-type-register-request)
	1. [Data Type Unregister Request](#data-type-unregister-request)
	1. [Data Type Update Request](#data-type-update-request)
	1. [Data Types Request](#data-types-request)
	1. [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses)
	1. [Entity Type](#entity-type)
	1. [Event](#event)
	1. [Events Request](#events-request)
	1. [Library](#library)
	1. [Library Details Request](#library-details-request)
	1. [Message](#message)
	1. [Mailbox Url](#mailbox-url)
	1. [Message Delete Request](#message-delete-request)
	1. [Message Details Request](#message-details-request)
	1. [Message Post Request](#message-post-request)
	1. [Message Received Event](#message-received-event)
	1. [Messages Request](#messages-request)
	1. [Message Descriptor](#message-descriptor)
	1. [Message Type](#message-type)
	1. [Message Type Details Request](#message-type-details-request)
	1. [Message Type Register Request](#message-type-register-request)
	1. [Message Type Unregister Request](#message-type-unregister-request)
	1. [Message Type Update Request](#message-type-update-request)
	1. [Message Types Request](#message-types-request)
	1. [Model](#model)
	1. [Operation](#operation)
	1. [Operation Details Request](#operation-details-request)
	1. [Operation Execute Request](#operation-execute-request)
	1. [Operation Reference](#operation-reference)
	1. [Operation Reference Message](#operation-reference-message)
	1. [Operation Reference Request](#operation-reference-request)
	1. [Operation Reference Request Message](#operation-reference-request-message)
	1. [Operation Register Request](#operation-register-request)
	1. [Operation Specification](#operation-specification)
	1. [Operation Specification Request Message](#operation-specification-request-message)
	1. [Operation Type](#operation-type)
	1. [Operation Type Details Request](#operation-type-details-request)
	1. [Operation Type Register Request](#operation-type-register-request)
	1. [Operation Type Unregister Request](#operation-type-unregister-request)
	1. [Operation Type Update Request](#operation-type-update-request)
	1. [Operation Types Request](#operation-types-request)
	1. [Operation Unregister Request](#operation-unregister-request)
	1. [Operation Update Request](#operation-update-request)
	1. [Operations Request](#operations-request)
	1. [Persistent Id](#persistent-id)
	1. [Persistent Id Event](#persistent-id-event)
	1. [Portfolio](#portfolio)
	1. [Portfolio Details Request](#portfolio-details-request)
	1. [Portfolio Register Message](#portfolio-register-message)
	1. [Provider](#provider)
	1. [Published Provider](#published-provider)
	1. [Published Provider Details Request](#published-provider-details-request)
	1. [Published Provider Register Request](#published-provider-register-request)
	1. [Published Provider Unregister Request](#published-provider-unregister-request)
	1. [Published Provider Update Request](#published-provider-update-request)
	1. [Published Providers Request](#published-providers-request)
	1. [Published Service](#published-service)
	1. [Published Service Details Request](#published-service-details-request)
	1. [Published Service Register Request](#published-service-register-request)
	1. [Published Service Unregister Request](#published-service-unregister-request)
	1. [Published Services Request](#published-services-request)
	1. [Qiy App](#qiy-app)
	1. [Qiy Node](#qiy-node)
	1. [Qiy Node API](#qiy-node-api)
	1. [Qiy Node Create Request](#qiy-node-create-request)
	1. [Qiy Node Credential](#qiy-node-credential)
	1. [Qiy Node Delete Request](#qiy-node-delete-request)
	1. [Qiy Node Event](#qiy-node-event)
	1. [Qiy Node Message](#qiy-node-message)
	1. [Qiy Node Request](#qiy-node-request)
	1. [Relying Party](#relying-party)
	1. [Request](#request)
	1. [Reference Serial Number](#reference-serial-number)
	1. [Serial Number](#serial-number)
	1. [Service](#service)
	1. [Service Catalogue](#service-catalogue)
	1. [Service Credential](#service-credential)
	1. [Service Credential Details Request](#service-credential-details-request)
	1. [Service Credential Request Message](#service-credential-request-message)
	1. [Service Credential Register Request](#service-credential-register-request)
	1. [Service Credential Unregister Request](#service-credential-unregister-request)
	1. [Service Credential Update Request](#service-credential-update-request)
	1. [Service Credentials Request](#service-credentials-request)
	1. [Service Description](#service-description)
	1. [Service Endpoint](#service-endpoint)
	1. [Service Portfolio](#service-portfolio)
	1. [Service Provider](#service-provider)
	1. [Service Source](#service-source)
	1. [Service Source Candidate](#service-source-candidate)
	1. [Service Type](#service-type)
	1. [Service Type Details Request](#service-type-details-request)
	1. [Service Type Register Request](#service-type-register-request)
	1. [Service Type Unregister Request](#service-type-unregister-request)
	1. [Service Type Update Request](#service-type-update-request)
	1. [Service Types Request](#service-types-request)
	1. [Source](#source)
	1. [Source Details Request](#source-details-request)
	1. [Source Register Request](#source-register-request)
	1. [Source Unregister Request](#source-unregister-request)
	1. [Source Update Request](#source-update-request)
	1. [Subscription](#subscription)
	1. [Subscription Details Request](#subscription-details-request)
	1. [Subscription Register Request](#subscription-register-request)
	1. [Subscription Unregister Request](#subscription-unregister-request)
	1. [Subscriptions Request](#subscriptions-request)
	1. [Transport Layer](#transport-layer)
	1. [Transport Protocol](#transport-protocol)


# 1 Introduction

## 1.1 Purpose

This document aims to be the entry point for information analysts and software engineers that need to kow how they can use the [Qiy Node](#qiy-node).

## 1.2 Readers' Guidance

* Information analysts are advised to read all of the document.
* Software engineers are advised to read all of the document and the [Qiy Node API](Definitions.md#qiy-node-api).

## 1.3 Overview

* Chapter [2 Requests](#2-requests) describes the [Qiy Node Requests](#qiy-node-request).
* Chapter [3 Events](#3-events) describes the [Qiy Node Events](#qiy-node-event).
* Chapter [4 Messages](#4-messages) describes the [Qiy Node Messages](#qiy-node-message).
* Chapter [5 Models](#5-models) describes the entities of the [Qiy Node Interface](Definitions.md#qiy-node-interface).
* Chapter [6 Index](#6-index) contains an index for the used terms.


# 2 Requests

This chapter describes the [Qiy Node Requests](#qiy-node-request).

## 2.1 General

### 2.1.1 Health Check

The health of a Qiy Node can be checked with the following request:

GET /admin/healthcheck


### 2.1.2 Versions

The supported [Qiy Node API](Definitions.md#qiy-node-api) version can be obtained with the call:

[GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#apiGet)

The returned version tag complies with Semantic Versioning 2.0.0, see [https://semver.org](https://semver.org).
[Qiy Node Implementations](Definitions.md#qiy-node-implementation) are to support the two latest major versions, with the additional rule that a new major version will never be released within 6 months of its predecessor.

### 2.1.3 Dynamic Path Endpoint Addresses

The Qiy Node uses [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses) for all but the /api path endpoint, which is strongly advised to be used at the start of every new day to obtain valid addresses and remain operational.
To obtain the endpoint addresses, use:

[GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#apiGet)

### 2.1.4 Authentication

Most requests must be authenticated using the [Authorization Header Parameter](#authorization-header-parameter) containing a signature over the Qiy Node Id, the current Unix time in ms using a Private Key which is unique for the Qiy Node.

#### 2.1.4.1 Java

In Java, the value of the Authorization header parameter can be calculated as follows:
```
public String signatureHeaderForData(String uuid, byte[] data) {
  String nonce = "" + System.currentTimeMillis();
  byte[] nonceBytes = nonce.getBytes(StandardCharsets.UTF_8);
  byte[] id = uuid.getBytes();
  PrivateKey pk = getKeyPair(uuid).getPrivate();

  Signature sig = Signature.getInstance("SHA256withRSA", "SunRsaSign");
  sig.initSign(pk);
  sig.update(id, 0, id.length);
  sig.update(nonceBytes, 0, nonceBytes.length);
  if (data != null) {
	sig.update(data, 0, data.length);
  }
  byte[] signature = sig.sign();

  String result = Base64.getEncoder().encodeToString(signature);
  return String.format("QTF %s %s:%s", uuid, nonce, result);
}
````

#### 2.1.4.2 Python

In Python, the value of the Authorization header parameter can be calculated as follows:

```
from OpenSSL.crypto import sign
from base64 import b64encode
import OpenSSL

def authHeader(uuid, nonce, Input):
        tosign="{0}{1}{2}".format(uuid,nonce,Input)
        print("tosign: '{0}'".format(tosign))
        with open(<File with private key in pem format>,"r") as f:
                buffer=f.read()
        key=OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM,buffer)
        signature=b64encode(sign(
                key
                ,tosign
                ,"sha256")
                ).decode()
        return "QTF {0} {1}:{2}".format(uuid, nonce, signature)
```

Information of the connections can be acquired using the [Connections Request](#connections-request).

## 2.2 Catalogue Requests

### 2.2.1 Catalogue Details Request
The [Catalogue Details Request](#catalogue-details-request) is a [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Service Catalogue](Definitions.md#service-catalogue).

### 2.2.2 Catalogues Request
The [Catalogues Request](#catalogues-request) is a [Qiy Node Request](#qiy-node-request) which can be used to consult the [Service Catalogues](Definitions.md#service-catalogue) of [Service Providers](Definitions.md#service-provider).

### 2.2.3 Published Service Details Request
The [Published Service Details Request](#published-service-details-request) is a [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Service](Definitions.md#service) that has been published in a [Service Catalogue](Definitions.md#service-catalogue).

### 2.2.4 Published Service Register Request
The [Published Service Register Request](#published-service-register-request) is a [Qiy Node Request](#qiy-node-request) which can be used to register a [Service](Definitions.md#service) of a [Service Provider](#service-provider) with an [Access Provider](Definitions.md#access-provider) and include it in [Service Catalogue](Definitions.md#service-catalogue) of the [Service Provider](#service-provider).

### 2.2.5 Published Service Unregister Request
The [Published Service Unregister Request](#published-service-unregister-request) is a [Qiy Node Request](#qiy-node-request) which can be used to unregister a [Service](Definitions.md#service) of a [Service Provider](#service-provider) with an [Access Provider](Definitions.md#access-provider) and remove it from the [Service Catalogue](Definitions.md#service-catalogue) of the [Service Provider](#service-provider).

### 2.2.6 Published Services Request
The [Published Services Request](#published-services-request) is a [Qiy Node Request](#qiy-node-request) which can be used to list the [Services](Definitions.md#service) in a [Catalogue](#catalogue).

## 2.3 Connect Token Requests

### 2.3.1 Connect Token Create Request
The [Connect Token Create Request](#connect-token-create-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a [Connect Token](Definitions.md#connect-token) from the [Qiy Node](Definitions.md#qiy-node).

### 2.3.2 Connect Token Delete Request
The [Connect Token Delete Request](#connect-token-delete-request) is a [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connect Token](Definitions.md#connect-token).

### 2.3.3 Connect Token Details Request
The [Connect Token Details Request](#connect-token-details-request) is a [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Connect Token](Definitions.md#connect-token).

### 2.3.4 Connect Token Register Request
The [Connect Token Register Request](#connect-token-register-request) is a [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.5 Connect Token Update Request
The [Connect Token Update Request](#connect-token-update-request) is a [Qiy Node Request](#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.6 Connect Tokens Request
The [Connect Tokens Request](#connect-tokens-request) is a [Qiy Node Request](#qiy-node-request) that can be used to access [Connect Tokens](Definitions.md#connect-token).


## 2.4 Connection Requests

### 2.4.1 Connection Create Request
The [Connection Create Request](#connection-create-request) is a [Qiy Node Request](#qiy-node-request) that can be used to create a [Connection](#connection) using a [Connect Token](Definitions.md#connect-token).

### 2.4.2 Connection Delete Request
The [Connection Delete Request](#connection-delete-request) is a [Qiy Node Request](#qiy-node-request) that can be used to delete a [Connection](#connection).

### 2.4.3 Connection Details Request
The [Connection Details Request](#connection-details-request) is a [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Connection](#connection).

### 2.4.4 Connections Request
The [Connections Request](#connections-request) is a  [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the [Connections](#connection) of a [Qiy Node](Definitions.md#qiy-node).

#### 2.4.4.1 Example Connections Request

```
Request:
GET http://127.0.0.1:8087/user/connections/user/pt_usernode_dr_dp_lo HTTP/1.1


User-Agent: python-requests/2.18.4
Accept: */*
Connection: keep-alive
Accept-Encoding: gzip, deflate
Authorization: QTF pt_usernode_dr_dp_lo 1521728878364:nNNvY8BxY0LucrOFOCBgg7s0GMaO9z+883CQEyMTvTvxUYlsN4OvA18tchuplVT9nmN4btD4NXAntqBkrGzey/fdyYrz6DmYSkB1d63/guXwLXhcwW0oI3JRIrCFcVwkCzAQ0uy3ppg979acz1Q8EMcQo9P5p06rRFlp1KEZ0HMPjHTW8ox60JAVHh+mc7h38g4RtQ2kLl5MiQfc66qa3EXF5Qf35CV4QL7phmozZzb/FafscpHdriY8oGGzYJa8M2YQdtc9Ql467c3A9U5Ab9rxxGEAdkh1Tts0Le05mk2ryAV7ao2+FOgwJEmahrcLwzqrCKnkm5wiwwWXaXOZYw==


None


Response:
200
Date: Thu, 22 Mar 2018 14:27:58 GMT
tracker: USR-102315
Content-Type: application/json
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 215


{"result":[{"state":"connected","activeFrom":1521728877000,"activeUntil":null,"links":{"self":"http://127.0.0.1:8087/user/connections/user/pt_usernode_dr_dp_lo/22452909-c659-418e-bf63-53175643e886","references":"http://127.0.0.1:8087/user/references/pt_usernode_dr_dp_lo/22452909-c659-418e-bf63-53175643e886","mbox":"http://127.0.0.1:8087/user/mbox/user/pt_usernode_dr_dp_lo/22452909-c659-418e-bf63-53175643e886"}}],"links":null}
```


## 2.5 Consent Requests

### 2.5.1 Consent Delete Request
The [Consent Delete Request](#consent-delete-request) is a [Qiy Node Request](#qiy-node-request) which can be used to delete a [Consent](#consent).

### 2.5.2 Consent Denied Request
The [Consent Denied Request](#consent-denied-request) is a [Qiy Node Request](#qiy-node-request) which can be used to communicate the denial of a [Consent](#consent).

### 2.5.3 Consent Details Request
The [Consent Details Request](#consent-details-request) is a [Qiy Node Request](#qiy-node-request) which can be used to acquire the details of a [Consent](#consent).

### 2.5.4 Consent Granted Request
The [Consent Granted Request](#consent-granted-request) is a [Qiy Node Request](#qiy-node-request) which can be used to communicate the granting of a [Consent](#consent).

### 2.5.5 Consent Withdrawn Request
The [Consent Withdrawn Request](#consent-withdrawn-request) is a [Qiy Node Request](#qiy-node-request) which can be used to communicate the withdrawal of a [Consent](#consent).

### 2.5.6 Consents Request
The [Consents Request](#consents-request) is a [Qiy Node Request](#qiy-node-request) which can be used to access [Consents](#consent).

## 2.6 Event Requests

### 2.6.1 Events Request
The [Events Request](#events-request) is a [Qiy Node Request](#qiy-node-request) that can be used to handle [Qiy Node Events](#qiy-node-event).

## 2.7 Library Requests

### 2.7.1 Data Type Details Request
The [Data Type Details Request](#data-type-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of a [Data Type](Definitions.md#data-type) in the [Service Library](Definitions.md#service-library).

### 2.7.2 Data Type Register Request
The [Data Type Register Request](#data-type-register-request) is a [Qiy Node Request](#qiy-node-request) to register a [Data Type](Definitions.md#data-type) in the [Service Library](Definitions.md#service-library).

### 2.7.3 Data Type Unregister Request
The [Data Type Unregister Request](#data-type-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister a [Data Type](Definitions.md#data-type) in the [Service Library](Definitions.md#service-library).

### 2.7.4 Data Type Update Request
The [Data Type Update Request](#data-type-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of a [Data Type](Definitions.md#data-type) in the [Service Library](Definitions.md#service-library).

### 2.7.5 Data Types Request
The [Data Types Request](#data-types-request) is a [Qiy Node Request](#qiy-node-request) to list the [Data Types](Definitions.md#data-type) that are registered in the [Service Library](Definitions.md#service-library).

### 2.7.6 Library Details Request
The [Library Details Request](#library-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of the [Service Library](Definitions.md#service-library).

### 2.7.7 Message Type Details Request
The [Message Type Details Request](#message-type-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of a [Message Type](#message-type) in the [Service Library](Definitions.md#service-library).

### 2.7.8 Message Type Register Request
The [Message Type Register Request](#message-type-register-request) is a [Qiy Node Request](#qiy-node-request) to register a [Message Type](#message-type) in the [Service Library](Definitions.md#service-library).

### 2.7.9 Message Type Unregister Request
The [Message Type Unregister Request](#message-type-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister a [Message Type](#message-type) in the [Service Library](Definitions.md#service-library).

### 2.7.10 Message Type Update Request
The [Message Type Update Request](#message-type-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of a [Message Type](#message-type) in the [Service Library](Definitions.md#service-library).

### 2.7.11 Message Types Request
The [Message Types Request](#message-types-request) is a [Qiy Node Request](#qiy-node-request) to list [Message Types](#message-type) that are registered in the [Service Library](Definitions.md#service-library).

### 2.7.12 Operation Type Details Request
The [Operation Type Details Request](#operation-type-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of a [Operation Type](#operation-type) in the [Service Library](Definitions.md#service-library).

### 2.7.13 Operation Type Register Request
The [Operation Type Register Request](#operation-type-register-request) is a [Qiy Node Request](#qiy-node-request) to register a [Operation Type](#operation-type) in the [Service Library](Definitions.md#service-library).

### 2.7.14 Operation Type Unregister Request
The [Operation Type Unregister Request](#operation-type-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister a [Operation Type](#operation-type) in the [Service Library](Definitions.md#service-library).

### 2.7.15 Operation Type Update Request
The [Operation Type Update Request](#operation-type-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of a [Operation Type](#operation-type) in the [Service Library](Definitions.md#service-library).

### 2.7.16 Operation Types Request
The [Operation Types Request](#operation-types-request) is a [Qiy Node Request](#qiy-node-request) to list the [Operation Types](#operation-type) that are registered in the [Service Library](Definitions.md#service-library).

### 2.7.17 Published Provider Details Request
The [Published Provider Details Request](#published-provider-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of a [Service Provider](#service-provider).

### 2.7.18 Published Provider Register Request
The [Published Provider Register Request](#published-provider-register-request) is a [Qiy Node Request](#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to register a [Service Provider](#service-provider) with the [Qiy Trust Network](Definitions.md#qiy-trust-network).

### 2.7.19 Published Provider Unregister Request
The [Published Provider Unregister Request](#published-provider-unregister-request) is a [Qiy Node Request](#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to unregister a [Service Provider](#service-provider) from the [Qiy Trust Network](Definitions.md#qiy-trust-network).

### 2.7.20 Published Provider Update Request
The [Published Provider Update Request](#published-provider-update-request) is a [Qiy Node Request](#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to update details of a [Service Provider](#service-provider).

### 2.7.21 Published Providers Request
The [Published Providers Request](#published-providers-request) is a [Qiy Node Request](#qiy-node-request) to list [Service Providers](Definitions.md#service-provider).

### 2.7.22 Service Type Details Request
The [Service Type Details Request](#service-type-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of a [Service Type](#service-type) in the [Service Library](Definitions.md#service-library).

### 2.7.23 Service Type Register Request
The [Service Type Register Request](#service-type-register-request) is a [Qiy Node Request](#qiy-node-request) to register a [Service Type](#service-type) in the [Service Library](Definitions.md#service-library).

### 2.7.24 Service Type Unregister Request
The [Service Type Unregister Request](#service-type-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister a [Service Type](#service-type) in the [Service Library](Definitions.md#service-library).

### 2.7.25 Service Type Update Request
The [Service Type Update Request](#service-type-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of a [Service Type](#service-type) in the [Service Library](Definitions.md#service-library).

### 2.7.26 Service Types Request
The [Service Types Request](#service-types-request) is a [Qiy Node Request](#qiy-node-request) to list the [Service Types](Definitions.md#service-type) that are registered in the [Service Library](Definitions.md#service-library).

## 2.8 Message Requests

### 2.8.1 Message Delete Request
The [Message Delete Request](#message-delete-request) is a [Qiy Node Request](#qiy-node-request) that can be used to delete a [Qiy Node Message](#qiy-node-message).

### 2.8.2 Message Details Request
The [Message Details Request](#message-details-request) is a [Qiy Node Request](#qiy-node-request) that can be used to get the details of a [Qiy Node Message](#qiy-node-message).

### 2.8.3 Message Post Request
The [Message Post Request](#message-post-request) is a [Qiy Node Request](#qiy-node-request) that can be used to post a [Qiy Node Message](#qiy-node-message).

### 2.8.4 Messages Request
The [Messages Request](#messages-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain a list of all the messages of a [Qiy Node](Definitions.md#qiy-node).

## 2.9 Operation Requests

### 2.9.1 Operation Execute Request
The [Operation Execute Request](#operation-execute-request) is a [Qiy Node Request](#qiy-node-request) that can be used to command the execution of an [Operation](#operation) by [Reference](Definitions.md#reference) using an [Operation Reference](#operation-reference).

### 2.9.2 Operation Reference Request
The [Operation Reference Request](#operation-reference-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) for a [Data Source](#data-source) of a [Consent](#consent).

### 2.9.3 Operation Register Request
The [Operation Register Request](#operation-register-request) is a [Qiy Node Request](#qiy-node-request) that can be used to obtain an [Operation Reference](#operation-reference) by registering an [Operation Specification](#operation-specification).

## 2.10 Portfolio Requests

### 2.10.1 Account Details Request
The [Account Details Request](#account-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of an [Account](Definitions.md#account).

### 2.10.2 Account Register Request
The [Account Register Request](#account-register-request) is a [Qiy Node Request](#qiy-node-request) to register an [Account](Definitions.md#account).

### 2.10.3 Account Unregister Request
The [Account Unregister Request](#account-unregister-request) is a [Qiy Node Request](#qiy-node-request) to register an [Account](Definitions.md#account).

### 2.10.4 Account Update Request
The [Account Update Request](#account-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of an [Account](Definitions.md#account).

### 2.10.5 Accounts Request
The [Accounts Request](#accounts-request) is a [Qiy Node Request](#qiy-node-request) to list [Accounts](Definitions.md#account).

### 2.10.6 Portfolio Details Request
The [Portfolio Details Request](#portfolio-details-request) is a [Qiy Node Request](#qiy-node-request) that can be used by a [Qiy User](Definitions.md#qiy-user) to get the details of his [Service Portfolio](#service-portfolio).

### 2.10.7 Subscription Details Request
The [Subscription Details Request](#subscription-details-request) is a [Qiy Node Request](#qiy-node-request) which can be used to get the details of a [Subscription](#subscription) in a [Service Portfolio](#service-portfolio).

### 2.10.8 Subscription Register Request
The [Subscription Register Request](#subscription-register-request) is a [Qiy Node Request](#qiy-node-request) which can be used to register a subscription to a [Service](Definitions.md#service).

### 2.10.9 Subscription Unregister Request
The [Subscription Unregister Request](#subscription-unregister-request) is a [Qiy Node Request](#qiy-node-request) which can be used to unregister a subscription to a [Service](Definitions.md#service).

### 2.10.10 Subscriptions Request
The [Subscriptions Request](#subscriptions-request) is a [Qiy Node Request](#qiy-node-request) which can be used to list the [Subscription](#subscription) in a [Service Portfolio](#service-portfolio).

## 2.11 Qiy Node Requests

### 2.11.1 Qiy Node Create Request
The [Qiy Node Create Request](#qiy-node-create-request) is a [Qiy Node Request](#qiy-node-request) to create a [Qiy Node](Definitions.md#qiy-node).

### 2.11.2 Qiy Node Delete Request
The [Qiy Node Delete Request](#qiy-node-delete-request) is a [Qiy Node Request](#qiy-node-request) to delete a [Qiy Node](Definitions.md#qiy-node).

## 2.12 Source Requests

### 2.12.1 Candidates Request
The [Candidates Request](#candidates-request) is a [Qiy Node Request](#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to obtain [Candidates](#candidate) for a [Consent](#consent).

### 2.12.2 Operation Details Request
The [Operation Details Request](#operation-details-request) is a [Qiy Node Request](#qiy-node-request) to get the details of an [Operation](#operation).

### 2.12.3 Operation Register Request
The [Operation Register Request](#operation-register-request) is a [Qiy Node Request](#qiy-node-request) to register an [Operation](#operation).

### 2.12.4 Operation Unregister Request
The [Operation Unregister Request](#operation-unregister-request) is a [Qiy Node Request](#qiy-node-request) to register an [Operation](#operation).

### 2.12.5 Operation Update Request
The [Operation Update Request](#operation-update-request) is a [Qiy Node Request](#qiy-node-request) to update the details of an [Operation](#operation).

### 2.12.5 Operations Request
The [Operations Request](#operations-request) is a [Qiy Node Request](#qiy-node-request) to list [Operations](Definitions.md#operation).

### 2.12.7 Source Details Request
The [Source Details Request](#source-details-request) is a [Qiy Node Request](#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to obtain details of a [Data Source](#data-source) of a [Consent](#consent).

### 2.12.8 Source Register Request
The [Source Register Request](#source-register-request) is a [Qiy Node Request](#qiy-node-request) to register [Data Sources](#data-source) for a [Consent](#consent).

### 2.12.9 Source Unregister Request
The [Source Unregister Request](#source-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister [Data Sources](#data-source) for a [Consent](#consent).

### 2.12.10 Source Update Request
The [Source Update Request](#source-update-request) is a [Qiy Node Request](#qiy-node-request) to update [Data Sources](#data-source) for a [Consent](#consent).

### 2.12.11 Service Credential Details Request
The [Service Credential Details Request](#service-credential-details-request) is a [Qiy Node Request](#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to obtain details of a [Service Credential](Definitions.md#service-credential) for a [Data Source](#data-source) of a [Consent](#consent).

### 2.12.12 Service Credential Register Request
The [Service Credential Register Request](#service-credential-register-request) is a [Qiy Node Request](#qiy-node-request) to register a [Service Credential](Definitions.md#service-credential) for a [Data Source](#data-source) of a [Consent](#consent).

### 2.12.13 Service Credential Unregister Request
The [Service Credential Unregister Request](#service-credential-unregister-request) is a [Qiy Node Request](#qiy-node-request) to unregister a [Service Credential](Definitions.md#service-credential) of a [Data Source](#data-source) of a [Consent](#consent).

### 2.12.14 Service Credential Update Request
The [Service Credential Update Request](#service-credential-update-request) is a [Qiy Node Request](#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to update a [Service Credential](Definitions.md#service-credential) of a [Data Source](#data-source) of a [Consent](#consent).

### 2.12.15 Service Credentials Request
The [Service Credentials Request](#service-credentials-request) is a [Qiy Node Request](#qiy-node-request) to list [Service Credentials](Definitions.md#service-credential).


# 3 Events

A [Qiy Application](Definitions.md#qiy-application) can use the [Events Request](#events-request) to start listening to the [Events](#event) generated by its [Qiy Node](Definitions.md#qiy-node).
The Events comply to the Server-Sent Events Standard, see [https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

## 3.1 Connection Events

### 3.1.1 Connection Created Event
The [Connection Created Event](#connection-created-event) is a [Qiy Node Event](#qiy-node-event) that is generated when a [Connection](#connection) has been created.

## 3.2 Consent Events

### 3.2.1 Consent Denied Event
The [Consent Denied Event](#consent-denied-event) is a [Qiy Node Event](#qiy-node-event) which can be used to communicate the denial of a [Consent](#consent).

### 3.2.2 Consent Granted Event
The [Consent Granted Event](#consent-granted-event) is a [Qiy Node Event](#qiy-node-event) which can be used to communicate the granting or regranting of a [Consent](#consent).

## 3.3 Message Events

### 3.3.1 Message Received Event
The [Message Received Event](#message-received-event) is a [Qiy Node Event](#qiy-node-event) that notifies a [Receiver](Definitions.md#receiver) that he has received a new [Qiy Node Message](#qiy-node-message).

## 3.4 Persistent Id Events

### 3.4.1 Persistent Id Event
The [Persistent Id Event](#persistent-id-event) is a [Qiy Node Event](#qiy-node-event) which is used to communicate the [Persistent Id](Definitions.md#persistent-id) of a new [Connection](#connection).


# 4 Messages

This chapter describes the [Qiy Node Messages](#message).

## 4.1 Consent Messages

### 4.1.1 Consent Notification Message

The [Consent Notification Message](#consent-notification-message) is a [Qiy Node Message](#qiy-node-message) which can be used to notify the registration of a [Consent](#consent).

### 4.1.2 Consent Request Message

The [Consent Request Message](#consent-request-message) is a [Qiy Node Message](#qiy-node-message) which can be used to [Request](Definitions.md#request) for a [Consent](#consent).

## 4.2 Operation Messages

### 4.2.1 Operation Reference Message
The [Operation Reference Message](#operation-reference-message) is a [Qiy Node Message](#qiy-node-message) that can be used to convey [Operation References](#operation-reference).

### 4.2.2 Operation Reference Request Message
The [Operation Reference Request Message](#operation-reference-request-message) is a [Qiy Node Message](#qiy-node-message) that can be used to [Request](Definitions.md#request) for [Operation References](#operation-reference).

### 4.2.3 Operation Specification Request Message
The [Operation Specification Request Message](#operation-specification-request-message) is a [Qiy Node Message](#qiy-node-message) to request for an [Operation Specification](#operation-specification).

## 4.3 Portfolio Messages

### 4.3.1 Portfolio Register Message
The [Portfolio Register Message](#portfolio-register-message) is a [Qiy Node Message](#qiy-node-message) to request to add a [Data Provider](Definitions.md#data-provider) to a [Service Portfolio](#service-portfolio).

## 4.4 Service Credential Messages

### 4.4.1 Service Credential Request Message
The [Service Credential Request Message](#service-credential-request-message) is a [Qiy Node Message](#qiy-node-message) for requesting a [Service Credential](Definitions.md#service-credential).

## 4.5 Source Messages

### 4.5.1 Candidates Message
The [Candidates Message](#candidates-message) is a [Qiy Node Message](#qiy-node-message) to propose candidate [Data Sources](#data-source) for a [Consent](#consent).


# 5 Models

This chapters describes the [Entity Types](#entity-type) of the [Qiy Node Interface](Definitions.md#qiy-node-interface).

## 5.1 Account Model

This section describes the [Account](#account) [Entity Type](#entity-type).
A [Qiy User](Definitions.md#qiy-user) can have linked [Accounts](#account) with any [Service Provider](#service-provider), but is initially used for linked accounts with [Data Providers](Definitions.md#data-provider).

### 5.1.1 Account Attributes

See [Account](#account) [model](#model).

### 5.1.2 Account Relations

See [Account](#account) [model](#model).
An [Account](#account):
* has one [Qiy User](Definitions.md#qiy-user).
* has one [Service Provider](#service-provider) ([Published Provider](#published-provider)).
* has zero or more [Persistent Ids](#persistent-id).
* is used for zero or more [Candidates](#candidate).
* is used for zero or more [Sources](#source).
* is used for zero or more [Subcriptions](#subscription).

### 5.1.3 Account Business Rules

See [Account](#account) [model](#model).

## 5.2 Candidate Model

This section describes the [Candidate](#candidate) [Entity Type](#entity-type).

A [Candidate](#candidate) is a possible [Source](#source) to provide [Personal Data](Definitions.md#personal-data) for a [Consent](#consent).

### 5.2.1 Candidate Attributes

See [Candidate](#candidate) [model](#model).

### 5.2.2 Candidate Relations

See [Candidate](#candidate) [model](#model).
A [Candidate](#candidate):
* is related to one [Consent](#consent).
* is related to one [Data Service](#data-service) ([Published Service](#published-service)).
* is related to zero or one [Account](#account).

### 5.2.3 Candidate Business Rules

See [Candidate](#candidate) [model](#model).

## 5.3 Catalogue Model

This section describes the [Catalogue](#catalogue) [Entity Type](#entity-type).
A [Catalogue](#catalogue) contains the [Service Descriptions](#service-description) ([Published Services](#published-service)) of the [Services](#service) that a [Published Provider](#published-provider) can provide via Qiy.

### 5.3.1 Catalogue Attributes

See [Catalogue](#catalogue) [model](#model).

### 5.3.2 Catalogue Relations

See also [Catalogue](#catalogue) [model](#model).
A [Catalogue](#catalogue):
* is part of: [Library](#library)
* has zero or more [Published Services](#published-service)
* has one [Published Provider](#published-provider)

### 5.3.3 Catalogue Business Rules

See [Catalogue](#catalogue) [model](#model).
In addition:
* Each registered [Service Provider](#service-provider) ([Published Provider](#published-provider)) has one [Catalogue](#catalogue).
* The [Service Provider](#service-provider) has write-access to the [Catalogue](#catalogue).
* The [Access Provider](Definitions.md#access-provider) of the [Service Provider](#service-provider) has write-access to the [Catalogue](#catalogue).
* All [Qiy Users](Definitions.md#qiy-user) have read-access to any [Catalogue](#catalogue).

## 5.4 Connect Token Model

This section describes the [Connect Token](#connect-token) [Entity Type](#entity-type).

### 5.4.1 Connect Token Attributes

See [Connect Token](#connect-token) [model](#model).

### 5.4.2 Connect Token Relations

See [Connect Token](#connect-token) [model](#model).

### 5.4.3 Connect Token Business Rules

See [Connect Token](#connect-token) [model](#model).

## 5.5 Connection Model

This section describes the [Connection](#connection) [Entity Type](#entity-type).

### 5.5.1 Connection Attributes

See [Connection](#connection) [model](#model).

#### 5.5.1.1 Mailbox Url

See [Connection](#connection) [model](#model).

### 5.5.2 Connection Relations

See [Connection](#connection) [model](#model).

### 5.5.3 Connection Business Rules

See [Connection](#connection) [model](#model).

## 5.6 Consent Model

This section describes the [Consent](#consent) [Entity Type](#entity-type).
A [Qiy User](Definitions.md#qiy-user) can consent a [Service Provider](#service-provider) the use of his [Personal Data](Definitions.md#personal-data) from different [Data Sources](#data-source) for a [Subscription](#subscription).

### 5.6.1 Consent Attributes

See [Consent](#consent) [model](#model).

### 5.6.2 Consent Relations

See [Consent](#consent) [model](#model).
A [Consent](#consent):
* is part of one: [Portfolio](#portfolio).
* has one: [Subscription](#subscription).
* has zero or more of: [Data Source](#data-source) ([Source](#source)).

### 5.6.3 Consent Business Rules

See [Consent](#consent) [model](#model).
In addition:
* A [Qiy User](Definitions.md#qiy-user) has read-access and write-access to a [Consent](#consent).
* A [Service Provider](#service-provider) has read-access to a [Consent](#consent).

## 5.7 Event Model

This section describes the [Event](#event) [Entity Type](#entity-type).

### 5.7.1 Event Attributes

See [Event](#event) [model](#model).

### 5.7.2 Event Relations

See [Event](#event) [model](#model).

### 5.7.3 Event Business Rules

See [Event](#event) [model](#model).

## 5.8 Library Model

This section describes the [Library](#library) [Entity Type](#entity-type).
The [Library](#library) discloses data about all registered [Service Providers](#service-provider) ([Published Provider](#published-provider)), [Catalogues](#catalogues), [Data Types](#data-type), [Message Types](#message-type) and [Service Types](#service-type).

### 5.8.1 Library Attributes

See [Library](#library) [model](#model).

### 5.8.2 Library Relations

See [Library](#library) [model](#model).
A [Library](#library):
* has zero or more [Catalogues](#catalogue).
* has zero or more [Data Types](#data-type).
* has zero or more [Message Types](#message-type).
* has zero or more [Service Types](#service-type).
* has zero or more [Published Providers](#published-provider).

### 5.8.3 Library Business Rules

See [Library](#library) [model](#model).
In addition:
* There is one and only one [Library](#library).
* All [Qiy Users](Definitions.md#qiy-user) have read-access to the [Library](#library).
* Only [Access Providers](Definitions.md#access-provider) have write-access to the [Library](#library).


## 5.9 Message Model

This section describes the [Message](#message) [Entity Type](#entity-type).
The [Message](#message) is used to exchange messages between [Qiy Users](Definitions.md#qiy-user).

### 5.9.1 Message Attributes

### 5.9.1.1 Reference Serial Number

See [Message](#message) [model](#model).

NB: This attribute is nullable which has been modelled here using the format property, see also [OpenAPI 2.0 does not support nullable fields](https://github.com/swagger-api/swagger-node/issues/399) and [OpenAPI 3.0 'nullable'-attribute](https://swagger.io/docs/specification/data-models/data-types/#nullable).

### 5.9.1.2 Serial Number

See [Message](#message) [model](#model).

### 5.9.2 Message Relations

See [Message](#message) [model](#model).
A [Message](#message):
* is described by a [Message Type](#message-type).
* has one sender (a [Qiy User](Definitions.md#qiy-user)).
* has one receiver (a [Qiy User](Definitions.md#qiy-user)).
* uses one [Connection](#connection).

### 5.9.3 Message Business Rules

See [Message](#message) [model](#model).
In addition:
* A [Message](#message) can only be exchanged over an active [Connection](#connection).
* A [Message](#message) is persisted as part of the [Connection](#connection).
* A [Message](#message) expires with the [Connection](#connection).
* A [Message](#message) is to follow the rules of its [Message Type](#message-type).

## 5.10 Message Type Model

This section describes the [Message Type](#message-type) [Entity Type](#entity-type).
The [Message Type](#message-type) is used to describe [Qiy Node Messages](#qiy-node-message) using [Message Descriptors](#message-descriptor).

### 5.10.1 Message Type Attributes

See [Message Type](#message-type) [model](#model).

### 5.10.2 Message Type Relations

See [Message Type](#message-type) [model](#model).
A [Message Type](#message-type):
* is part of the [Library](#library).
* is used by a [Message](#message).

### 5.10.3 Message Type Business Rules

See [Message Type](#message-type) [model](#model).

## 5.11 Operation Model

This section describes the [Operation](#operation) [Entity Type](#entity-type).

An [Operation](#operation) is a command which can be used to acquire [Personal Data](Definitions.md#personal-data) for a [Consent](#consent) from the [Service Endpoint](#service-endpoint) of a [Data Provider](Definitions.md#data-provider).

### 5.11.1 Operation Attributes

See [Operation](#operation) [model](#model).

### 5.11.2 Operation Relations

See [Operation](#operation) [model](#model).
An [Operation](#operation):
* has one [Source](#source).
* has zero or one [Operation Reference](#operation-reference).
* has zero or one [Operation Specification](#operation-specification).

### 5.11.3 Operation Business Rules

See [Operation](#operation) [model](#model).

## 5.12 Operation Specification Model

This section describes the [Operation Specification](#operation-specification) [Entity Type](#entity-type).
The [Operation Specification](#operation-specification) specifies an [Operation](#operation) that can be used to acquire [Personal Data](Definitions.md#personal-data) from the [Service Endpoint](#service-endpoint) of a [Data Provider](Definitions.md#data-provider).

### 5.12.1 Operation Specification Attributes

See [Operation Specification](#operation-specification) [model](#model).

### 5.12.2 Operation Specification Relations

See [Operation Specification](#operation-specification) [model](#model).
An [Operation Specification](#operation-specification):
* is part of an [Operation](#operation).

### 5.12.3 Operation Specification Business Rules

See [Operation Specification](#operation-specification) [model](#model).
In addition:
* A [Data Subject](Definitions.md#data-subject) ([Qiy User](Definitions.md#qiy-user)) has read-access and write-access to an [Operation Specification](#operation-specification).
* A [Data Provider](Definitions.md#data-provider) has read-access and write-access to an [Operation Specification](#operation-specification).

## 5.13 Persistent Id Model

This section describes the [Persistent Id](#persistent-id) [Entity Type](#entity-type).

### 5.13.1 Persistent Id Relations

See [Persistent Id](#persistent-id) [model](#model).

### 5.13.2 Persistent Id Business Rules

See [Persistent Id](#persistent-id) [model](#model).

## 5.14 Portfolio Model

This section describes the [Service Portfolio](#service-portfolio) [Entity Type](#entity-type).
The [Service Portfolio](#service-portfolio) of a [Qiy User](Definitions.md#qiy-user) is used to maintain information related to his [Subscriptions](#subscription), [Consents](#consent) and [Personal Data](Definitions.md#personal-data).

### 5.14.1 Portfolio Attributes

See [Portfolio](#portfolio) [model](#model).

### 5.14.2 Portfolio Relations

See [Portfolio](#portfolio) [model](#model).
A [Portfolio](#portfolio):
* has one owner, a [Qiy User](Definitions.md#qiy-user).
* has zero or more linked data [Accounts](#account).
* has zero or more [Consents](#consent).
* has zero or more [Subscriptions](#subscription).

### 5.14.3 Portfolio Business Rules

See [Portfolio](#portfolio) [model](#model).
In addition:
* Each [Qiy User](Definitions.md#qiy-user) has one [Portfolio](#portfolio).
* Only the [Qiy User](Definitions.md#qiy-user) has read-access and write-access to a [Portfolio](#portfolio).

## 5.15 Published Provider Model

This section describes the [Published Provider](#published-provider) [Entity Type](#entity-type).
A [Published Provider](#published-provider) is a [Service Provider](#service-provider) that can provide [Services](#service) via Qiy.

### 5.15.1 Published Provider Attributes

See [Published Provider](#published-provider) [model](#model).

### 5.15.2 Published Provider Relations

See [Published Provider](#published-provider) [model](#model).
A [Published Provider](#published-provider):
* relates to one [Library](#library).
* relates to one [Access Provider](#access-provider).
* relates to one [Service Provider](#service-provider).
* relates to one [Catalogue](#catalogue).
* consumes data of zero or more [Data Types](#data-type).
* produces data of zero or more [Data Types](#data-type).

### 5.15.3 Published Provider Business Rules

See [Published Provider](#published-provider) [model](#model).

## 5.16 Published Service Model

This section describes the [Published Service](#published-service) [Entity Type](#entity-type).
A [Published Service](#published-service) is used to describe a [Service](#service) that a [Published Provider](#published-provider) can provide via Qiy.

### 5.16.1 Published Service Attributes

See [Published Service](#published-service) [model](#model).

### 5.16.2 Published Service Relations

See [Published Service](#published-service) [model](#model).
A [Published Service](#published-service):
* is part of one [Catalogue](#catalogue).
* has one [Published Provider](#published-provider).
* has one [Service Descriptor](#service-descriptor).
* has one [Service Type](#service-type).
* has one or more [Operation Types](#operation-type).

### 5.16.3 Published Service Business Rules

See [Published Service](#published-service) [model](#model).

## 5.17 Qiy Node Model

This section describes the [Qiy Node](#qiy-node) [Entity Type](#entity-type).

### 5.17.1 Qiy Node  Attributes

See [Qiy Node](#qiy-node) [model](#model).

### 5.17.2 Qiy Node Relations

See [Qiy Node](#qiy-node) [model](#model).

### 5.17.3 Qiy Node Business Rules

See [Qiy Node](#qiy-node) [model](#model).

## 5.18 Qiy Node Credential Model

This section describes the [Qiy Node Credential](#qiy-node-credential) [Entity Type](#entity-type).

### 5.18.1 Qiy Node Credential Attributes

See [Qiy Node Credential](#qiy-node-credential) [model](#model).

### 5.18.2 Qiy Node Credential Relations

See [Qiy Node Credential](#qiy-node-credential) [model](#model).

### 5.18.3 Qiy Node Credential Business Rules

See [Qiy Node Credential](#qiy-node-credential) [model](#model).

## 5.19 Service Description Model

This section describes the [Service Description](#service-description) [Entity Type](#entity-type).

### 5.19.1 Service Description Attributes

See [Service Description](#service-description) [model](#model).

### 5.19.2 Service Description Relations

See [Service Description](#service-description) [model](#model).

### 5.19.3 Service Description Business Rules

See [Service Description](#service-description) [model](#model).

## 5.20 Service Type Model

This section describes the [Service Type](#service-type) [Entity Type](#entity-type).
A [Service Type](#service-type) is used to describe the type of a [Service](#service).

### 5.20.1 Service Type Attributes

See [Service Type](#service-type) [model](#model).

### 5.20.2 Service Type Relations

See [Service Type](#service-type) [model](#model).
A [Service Type](#service-type):
* is part of the [Library](#library).
* is used by zero or more [Service Descriptions](#service-description).

### 5.20.3 Service Type Business Rules

See [Service Type](#service-type) [model](#model).

## 5.21 Source Model

This section describes the [Source](#source) [Entity Type](#entity-type).

A [Source](#source) is an origin for the [Personal Data](Definitions.md#personal-data) in a [Consent](#consent).

### 5.21.1 Source Attributes

See [Source](#source) [model](#model).

### 5.21.2 Source Relations

See [Source](#source) [model](#model).
A [Source](#source):
* has zero or one [Account](#account).
* has one [Consent](#consent).
* has zero or one [Data Service](#data-service) ([Published Service](#published-service)).
* has zero or more [Operations](#operation).
* has zero or more [Service Credentials](#service-credential).

### 5.21.3 Source Business Rules

See [Source](#source) [model](#model).

## 5.22 Subscription Model

This section describes the [Subscription](#subscription) [Entity Type](#entity-type).
A [Qiy User](Definitions.md#qiy-user) can have [Subscriptions](Definitions.md#subscription) to any [Service](Definitions.md#service) of any [Service Provider](#service-provider).

### 5.22.1 Subscription Attributes

See [Subscription](#subscription) [model](#model).

### 5.22.2 Subscription Relations

See [Subscription](#subscription) [model](#model).
A [Subscription](#subscription):
* has one subscriber, a [Qiy User](Definitions.md#qiy-user).
* has one [Service](Definitions.md#service) ([Published Service](#published-service)).
* has zero or one [Account](#account).
* has zero or one [Consent](#consent).
* has one [Persistent Id](#persistent-id).

### 5.22.3 Subscription Business Rules

See [Subscription](#subscription) [model](#model).
In addition:
* The [Qiy User](Definitions.md#qiy-user) has read-access and write-access to a [Subscription](#subscription).
* The [Service Provider](#service-provider) has read-access to a [Subscription](#subscription).


# 6 Index

## Access Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Access Provider](Definitions.md#access-provider)

## Account

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Account](Definitions.md#account)
[Qiy Node API](Qiy%20Node%20API.json)         | [Account](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#Account) requests
[Qiy Node API](Qiy%20Node%20API.json)         | [Account Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#AccountModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.1 Account Model](#51-account-model)

## Account Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Account Details Request](Definitions.md#account-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /accountUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#accountUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.1 Account Details Request](#2101-account-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Account Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Account Register Request](Definitions.md#account-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /accountsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#accountsUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.2 Account Register Request](#2102-account-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Account Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Account Unregister Request](Definitions.md#account-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /accountUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#accountUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.3 Account Unregister Request](#2103-account-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Account Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Account Update Request](Definitions.md#account-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /accountUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#accountUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.4 Account Update Request](#2104-account-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Accounts Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Accounts Request](Definitions.md#accounts-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /accountsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#accountsUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.5 Accounts Request](#2105-accounts-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Authorization Header Parameter

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.4 Authentication](#214-authentication)

## Candidate

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Candidate Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#CandidateModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12 Candidate Requests](#212-candidate-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.5.1 Candidates Message](#451-candidates-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.2 Candidate Model](#52-candidate-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Source Candidate](#service-source-candidate)

## Candidates Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Candidates Message]
[Qiy Node API](Qiy%20Node%20API.json)         | [Candidates Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#CandidatesMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.5.1 Candidates Message](#451-candidates-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)

## Candidates Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Candidates Request]
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /candidatesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#candidatesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.1 Candidates Request](#2121-candidates-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)

## Catalogue

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Catalogue](Definitions.md#service-catalogue)
[Qiy Node API](Qiy%20Node%20API.json)         | [Catalogue Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#CatalogueModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.3 Catalogue Model](#53-catalogue-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Catalogue Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogue Details Request](Definitions.md#catalogue-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /catalogueUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#catalogueUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.1 Catalogue Details Request](#221-catalogue-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)

## Catalogues Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogues Request](Definitions.md#catalogues-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /cataloguesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#cataloguesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.2 Catalogues Request](#222-catalogues-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)

## Connect Token

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token](Definitions.md#connect-token)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connect Token Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConnectTokenModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.4 Connect Token Model](#54-connect-token-model)

## Connect Token Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Create Request](Definitions.md#connect-token-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ctCreateEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.1 Connect Token Create Request](#231-connect-token-create-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connect Token Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Delete Request](Definitions.md#connect-token-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectTokenUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.2 Connect Token Delete Request](#232-connect-token-delete-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connect Token Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Details Request](Definitions.md#connect-token-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectTokenUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.3 Connect Token Details Request](#233-connect-token-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connect Token Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Register Request](Definitions.md#connect-token-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ctCreateEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.4 Connect Token Register Request](#234-connect-token-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connect Token Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Update Request](Definitions.md#connect-token-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectTokenUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.5 Connect Token Update Request](#235-connect-token-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connect Tokens Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Tokens Request](Definitions.md#connect-tokens-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /ctListEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ctListEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.6 Connect Tokens Request](#236-connect-tokens-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)

## Connection

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection](Definitions.md#connection)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connect](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#Connect)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connection Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConnectionModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4 Connection Requests](#24-connection-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.1 Connection Events](#31-connection-events)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.5 Connection Model](#55-connection-model)

## Connection Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Create Request](Definitions.md#connection-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /connectionsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectionsEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.1 Connection Create Request](#241-connection-create-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Connection Created Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Created Event](Definitions.md#connection-created-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connection Created Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConnectionCreatedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.1.1 Connection Created Event](#311-connection-created-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Connection Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Delete Request](Definitions.md#connection-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /connectionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectionUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.2 Connection Delete Request](#242-connection-delete-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Connection Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Details Request](Definitions.md#connection-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectionUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.3 Connection Details Request](#243-connection-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Connections Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connections Request](Definitions.md#connections-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectionsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#connectionsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.4 Connections Request](#244-connections-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Consent

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent](Definitions.md#consent)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConsentModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5 Consent Requests](#25-consent-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.2 Consent Events](#32-consent-events)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.1 Consent Messages](#41-consent-messages)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.6 Consent Model](#56-consent-model)

## Consent Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Delete Request](Definitions.md#consent-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.1 Consent Delete Request](#251-consent-delete-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Denied Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Denied Event](Definitions.md#consent-denied-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Denied Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConsentDeniedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.2.1 Consent Denied Event](#321-consent-denied-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Denied Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Denied Request](Definitions.md#consent-denied-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.2 Consent Denied Request](#252-consent-denied-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Details Request](Definitions.md#consent-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.3 Consent Details Request](#253-consent-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Granted Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Consent Granted Event](Definitions.md#consent-granted-event)
[Qiy Node API](Qiy%20Node%20API.json) | [Consent Granted Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConsentGrantedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.2.2 Consent Granted Event](#322-consent-granted-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Granted Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Granted Request](Definitions.md#consent-granted-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.4 Consent Granted Request](#254-consent-granted-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Notification Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Notification Message](Definitions.md#consent-notification-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Notification Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConsentNotificationMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.1.1 Consent Notification Message](#411-consent-notification-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Consent Request Message](Definitions.md#consent-request-message)
[Qiy Node API](Qiy%20Node%20API.json) | [Consent Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ConsentRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.1.2 Consent Request Message](#412-consent-request-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consent Withdrawn Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Withdrawn Request](Definitions.md#consent-withdrawn-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.5 Consent Withdrawn Request](#255-consent-withdrawn-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Consents Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consents Request](Definitions.md#consents-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentsUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.6 Consents Request](#256-consents-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)

## Data Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Provider](Definitions.md#data-provider)

## Data Reference

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Reference](Definitions.md#data-reference)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)

## Data Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Reference Request](Definitions.md#data-reference-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference Request](#operation-reference-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Reference](#data-reference)

## Data Service

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Service](Definitions.md#data-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Data Source

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Source](Definitions.md#data-source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Data Type

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Data Type Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#DataTypeModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.8 Library Model](#58-library-model)

## Data Type Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Type Details Request](Definitions.md#data-type-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /dataTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#dataTypeUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.1 Data Type Details Request](#271-data-type-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)

## Data Type Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Type Register Request](Definitions.md#data-type-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /dataTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#dataTypesUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.2 Data Type Register Request](#272-data-type-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)

## Data Type Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Type Unregister Request](Definitions.md#data-type-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /dataTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#dataTypeUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.3 Data Type Unregister Request](#273-data-type-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)

## Data Type Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Type Update Request](Definitions.md#data-type-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /dataTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#dataTypeUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.4 Data Type Update Request](#274-data-type-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)

## Data Types Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Types Request](Definitions.md#data-types-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /dataTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#dataTypesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.5 Data Types Request](#275-data-types-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)

## Dynamic Path Endpoint Addresses

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Path Endpoint Addresses](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PathEndpointAddresses)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#apiGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.3 Dynamic Path Endpoint Addresses](#213-dynamic-path-endpoint-addresses)

## Entity Type

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Entity](Definitions.md#entity)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5 Models](#5-models)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connect Token](#connect-token)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Reference](#data-reference)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Data Type](#data-type)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Event](#event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Library](#library)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Descriptor](#message-descriptor)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Specification](#operation-specification)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Persistent Id](#persistent-id)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Portfolio](#portfolio)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Provider](#provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy App](#qiy-app)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node API](#qiy-node-api)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node Credential](#qiy-node-credential)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Request](#request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Description](#service-description)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Endpoint](#service-endpoint)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Event](Definitions.md#qiy-node-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#EventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3 Events](#3-events)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.7 Event Model](#57-event-model)

## Events Request

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /eventsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#eventsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.6.1 Events Request](#261-events-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Event](#event)

## Library

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Library](Definitions.md#service-library)
[Qiy Node API](Qiy%20Node%20API.json)         | [Library Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#LibraryModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.8 Library Model](#58-library-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Library Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Details Request](Definitions.md#library-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /libraryEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#libraryEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.6 Library Details Request](#276-library-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Library](#library)

## Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Message](Definitions.md#qiy-node-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#Message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#MessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8 Message Requests](#28-message-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.3 Message Events](#33-message-events)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4 Messages](#4-messages)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.9 Message Model](#59-message-model)

## Mailbox Url

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.5.1.1 Mailbox Url](#5511-mailbox-url)

## Message Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Delete Request](Definitions.md#message-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /messageUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.1 Message Delete Request](#281-message-delete-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Message Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Details Request](Definitions.md#message-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /messageUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.2 Message Details Request](#282-message-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Message Post Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Post Request](Definitions.md#message-post-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#mboxUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.3 Message Post Request](#283-message-post-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Message Received Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Received Event](Definitions.md#message-received-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Received Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#MessageReceivedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.3.1 Message Received Event](#331-message-received-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Messages Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Messages Request](Definitions.md#messages-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#mboxUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.4 Messages Request](#284-messages-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Message Descriptor

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Descriptor](Definitions.md#message-descriptor)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.10 Message Type Model](#510-message-type-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Message Type

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Type](Definitions.md#message-type)
[Qiy Node API](Qiy%20Node%20API.json)         | [Library](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#Library)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Type Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#MessageTypeModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.10 Message Type Model](#510-message-type-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Message Type Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Type Details Request](Definitions.md#message-type-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /messageTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageTypeUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.7 Message Type Details Request](#277-message-type-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Message Type Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Type Register Request](Definitions.md#message-type-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /messageTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageTypesUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.8 Message Type Register Request](#278-message-type-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Message Type Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Type Unregister Request](Definitions.md#message-type-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /messageTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageTypeUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.9 Message Type Unregister Request](#279-message-type-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Message Type Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Type Update Request](Definitions.md#message-type-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /messageTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageTypeUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.10 Message Type Update Request](#2710-message-type-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Message Types Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Types Request](Definitions.md#message-types-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /messageTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#messageTypesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.11 Message Types Request](#2711-message-types-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Type](#message-type)

## Model

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [__Models](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#__Models)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5 Models](#5-models)

## Operation

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation](Definitions.md#operation)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.11 Operation Model](#511-operation-model)

## Operation Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Details Request](Definitions.md#operation-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /operationUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.2 Operation Details Request](#2122-operation-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Execute Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Execute Request](Definitions.md#operation-execute-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /refEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#refEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.9.1 Operation Execute Request](#291-operation-execute-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Reference

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                   | [Operation Reference](Definitions.md#operation-reference)
[Qiy Node API](Qiy%20Node%20API.json)           | [Operation Reference Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationReferenceModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md)   | [5.11 Operation Model](#511-operation-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md)   | [Data Reference](#data-reference)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Reference Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Message](Definitions.md#operation-reference-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Reference Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationReferenceMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.1 Operation Reference Message](#421-operation-reference-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)

## Operation Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Request](Definitions.md#operation-reference-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.9.2 Operation Reference Request](#292-operation-reference-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)

## Operation Reference Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Request Message](Definitions.md#operation-reference-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Reference Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationReferenceRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.2 Operation Reference Request Message](#422-operation-reference-request-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)

## Operation Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Register Request](Definitions.md#operation-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /operationssUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationssUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.3 Operation Register Request](#2123-operation-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)

## Operation Specification

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Specification](Definitions.md#operation-specification)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Specification Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationSpecificationModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.12 Operation Specification Model](#512-operation-specification-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Specification Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Specification Request Message](Definitions.md#operation-specification-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Specification Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationSpecificationRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.3 Operation Specification Request Message](#423-operation-specification-request-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Specification](#operation-specification)

## Operation Type

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Type Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#OperationTypeModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.8 Library Model](#58-library-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Type Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Type Details Request](Definitions.md#operation-type-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /operationTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationTypeUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.12 Operation Type Details Request](#2712-operation-type-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)

## Operation Type Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Type Register Request](Definitions.md#operation-type-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /operationTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationTypesUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.13 Operation Type Register Request](#2713-operation-type-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)

## Operation Type Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Type Unregister Request](Definitions.md#operation-type-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /operationTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationTypeUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.14 Operation Type Unregister Request](#2714-operation-type-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)

## Operation Type Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Type Update Request](Definitions.md#operation-type-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /serviceTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypeUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.15 Operation Type Update Request](#2715-operation-type-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)

## Operation Types Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Types Request](Definitions.md#operation-types-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /serviceTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.16 Operation Types Request](#2716-operation-types-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Type](#operation-type)

## Operation Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Unregister Request](Definitions.md#operation-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /operationUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.4 Operation Unregister Request](#2124-operation-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operation Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Update Request](Definitions.md#operation-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /operationUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.5 Operation Update Request](#2125-operation-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Operations Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operations Request](Definitions.md#operations-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /operationsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#operationsUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.6 Operations Request](#2126-operations-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)

## Persistent Id

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Persistent Id](Definitions.md#persistent-id)
[Qiy Node API](Qiy%20Node%20API.json)         | [Persistent Id Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PersistentIdModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.4.1 Persistent Id Event](#341-persistent-id-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.13 Persistent Id Model](#513-persistent-id-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Connection](#connection)

## Persistent Id Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Persistent Id Event](Definitions.md#persistent-id-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Persistent Id Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PersistentIdEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.4.1 Persistent Id Event](#341-persistent-id-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Persistent Id](#persistent-id)

## Portfolio

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                   | [Service Portfolio](Definitions.md#service-portfolio)
[Qiy Node API](Qiy%20Node%20API.json)           | [Portfolio Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PortfolioModel)
[Qiy Node Protocol](Qiy%20Node%20Protocoyyl.md) | [5.14 Portfolio Model](#514-portfolio-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Portfolio Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Details Request](Definitions.md#portfolio-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /portfolioEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#portfolioEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.6 Portfolio Details Request](#2106-portfolio-details-request)

## Portfolio Register Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Register Message](Definitions.md#portfolio-register-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Portfolio Register Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PortfolioRegisterMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.3.1 Portfolio Register Message](#431-portfolio-register-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Portfolio](#portfolio)

## Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service Provider](Definitions.md#service-provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Library](#library)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Account](#account)

## Published Provider

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Published Provider Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PublishedProviderModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.15 Published Provider Model](#515-published-provider-model)

## Published Provider Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Provider Details Request](Definitions.md#published-provider-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /publishedProviderUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedProviderUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.17 Published Provider Details Request](#2717-published-provider-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)

## Published Provider Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Provider Register Request](Definitions.md#published-provider-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /publishedProvidersUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedProvidersUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.18 Published Provider Register Request](#2718-published-provider-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)

## Published Provider Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Provider Unregister Request](Definitions.md#published-provider-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /publishedProviderUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedProviderUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.19 Published Provider Unregister Request](#2719-published-provider-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)

## Published Provider Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Provider Update Request](Definitions.md#published-provider-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /publishedProviderUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedProviderUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.20 Published Provider Update Request](#2720-published-provider-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)

## Published Providers Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Providers Request](Definitions.md#published-providers-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /publishedProvidersUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedProvidersUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.21 Published Providers Request](#2721-published-providers-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Provider](#published-provider)

## Published Service

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Published Service Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#PublishedServiceModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.16 Published Service Model](#516-published-service-model)

## Published Service Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Service Details Request](Definitions.md#published-service-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /publishedServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedServiceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.3 Published Service Details Request](#223-published-service-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)

## Published Service Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Service Register Request](Definitions.md#published-service-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /publishedServicesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedServicesUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.4 Published Service Register Request](#224-published-service-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Published Service Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Service Unregister Request](Definitions.md#published-service-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /publishedServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedServiceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.5 Published Service Unregister Request](#225-published-service-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Published Services Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Published Services Request](Definitions.md#published-services-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /publishedServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedServiceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.6 Published Services Request](#226-published-services-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Qiy App

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Qiy Application](Definitions.md#qiy-application)

## Qiy Node

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node](Definitions.md#qiy-node)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.17 Qiy Node Model](#517-qiy-node-model)

## Qiy Node API

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node](Definitions.md#qiy-node)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Abstract](#abstract)

## Qiy Node Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Create Request](Definitions.md#qiy-node-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /createEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#createEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.11.1 Qiy Node Create Request](#2111-qiy-node-create-request)

## Qiy Node Credential

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Credential](Definitions.md#qiy-node-credential)
[Qiy Node API](Qiy%20Node%20API.json)         | [Qiy Node Credential Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#QiyNodeCredentialModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.18 Qiy Node Credential Model](#518-qiy-node-credential-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)

## Qiy Node Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Delete Request](Definitions.md#qiy-node-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /deleteEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#deleteEndpointDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.11.2 Qiy Node Delete Request](#2112-qiy-node-delete-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)

## Qiy Node Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Event](Definitions.md#qiy-node-event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Event](#event)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)

## Qiy Node Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Message](Definitions.md#qiy-node-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)

## Qiy Node Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Request](Definitions.md#qiy-node-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [__Methods](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#__Methods)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Request](#request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2 Requests](#2-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node](#qiy-node)

## Relying Party

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Relying Party](Definitions.md#relying-party)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Provider](#service-provider)

## Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Request](Definitions.md#qiy-node-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [__Methods](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#__Methods)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2 Requests](#2-requests)

## Reference Serial Number

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.9.1.1 Reference Serial Number](#5911-reference-serial-number)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Serial Number

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.9.1.2 Serial Number](#5912-serial-number)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message](#message)

## Service

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service](Definitions.md#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Consent](#consent)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation](#operation)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Published Service](#published-service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Description](#service-description)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Endpoint](#service-endpoint)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Library](#library)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Provider](#provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference](#operation-reference)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Service Catalogue

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Catalogue](Definitions.md#service-catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Service Credential

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Endpoint](#service-endpoint)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Service Credential Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credential Details Request](Definitions.md#service-credential-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /serviceCredentialUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceCredentialUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.11 Service Credential Details Request](#21211-service-credential-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Credential Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credential Request Message](Definitions.md#service-credential-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Service Credential Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ServiceCredentialRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.4.1 Service Credential Request Message](#441-service-credential-request-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Credential Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credential Register Request](Definitions.md#service-credential-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /serviceCredentialUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceCredentialUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.12 Service Credential Register Request](#21212-service-credential-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Credential Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credential Unregister Request](Definitions.md#service-credential-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /serviceCredentialUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceCredentialUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.13 Service Credential Unregister Request](#21213-service-credential-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Credential Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credential Update Request](Definitions.md#service-credential-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /serviceCredentialUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceCredentialUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.14 Service Credential Update Request](#21214-service-credential-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Credentials Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credentials Request](Definitions.md#service-credentials-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /serviceCredentialsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceCredentialsUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.15 Service Credentials Request](#21215-service-credentials-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Credential](#service-credential)

## Service Description

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Description](Definitions.md#service-description)
[Qiy Node API](Qiy%20Node%20API.json)         | [Service Description Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ServiceDescriptionModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.19 Service Description Model](#519-service-description-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Service Endpoint

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service Endpoint](Definitions.md#service-endpoint)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Service Portfolio

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Portfolio](Definitions.md#service-portfolio)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Portfolio](#portfolio)

## Service Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Provider](Definitions.md#service-provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Provider](#provider)

## Service Source

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Source](Definitions.md#service-source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Service Source Candidate

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)

## Service Type

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Service Type Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#ServiceTypeModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.20 Service Type Model](#520-service-type-model)

## Service Type Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Type Details Request](Definitions.md#service-type-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /serviceTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypeUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.22 Service Type Details Request](#2722-service-type-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)

## Service Type Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Type Register Request](Definitions.md#service-type-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /serviceTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypesUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.23 Service Type Register Request](#2723-service-type-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)

## Service Type Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Type Unregister Request](Definitions.md#service-type-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /serviceTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypeUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.24 Service Type Unregister Request](#2724-service-type-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)

## Service Type Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Type Update Request](Definitions.md#service-type-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /serviceTypeUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypeUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.25 Service Type Update Request](#2725-service-type-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)

## Service Types Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Types Request](Definitions.md#service-types-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /serviceTypesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#serviceTypesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.26 Service Types Request](#2726-service-types-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Type](#service-type)

## Source

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Source](#data-source)
[Qiy Node API](Qiy%20Node%20API.json)         | [Source](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#Source)
[Qiy Node API](Qiy%20Node%20API.json)         | [Source Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#SourceModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.21 Source Model](#521-source-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12 Source Requests](#212-source-requests)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service Source](#service-source)

## Source Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Details Request](Definitions.md#source-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#sourceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.7 Source Details Request](#2127-source-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Candidate](#candidate)

## Source Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Register Request](Definitions.md#source-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#consentUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.8 Source Register Request](#2128-source-register-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Source Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Unregister Request](Definitions.md#source-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#sourceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.9 Source Unregister Request](#2129-source-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Source Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Update Request](Definitions.md#source-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#sourceUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.10 Source Update Request](#21210-source-update-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Subscription

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Subscription](#subscription)
[Qiy Node API](Qiy%20Node%20API.json)         | [Subscription Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#SubscriptionModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.22 Subscription Model](#522-subscription-model)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Service](#service)

## Subscription Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Subscription Details Request](Definitions.md#subscription-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /subscriptionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#subscriptionUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.7 Subscription Details Request](#2107-subscription-details-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Subscription Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Subscription Register Request](Definitions.md#subscription-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /subscriptionsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#subscriptionsUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.8 Subscription Register Message](#2108-subscription-register-message)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Subscription Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Subscription Unregister Request](Definitions.md#subscription-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /publishedServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#publishedServiceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.9 Subscription Unregister Request](#2109-subscription-unregister-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Subscriptions Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Subscriptions Request](Definitions.md#subscriptions-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /subscriptionsUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/qiy-node-api.html#subscriptionsUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.10 Subscriptions Request](#21010-subscriptions-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Subscription](#subscription)

## Transport Layer

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Transport Layer](Definitions.md#transport-layer)

## Transport Protocol

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Transport Protocol](Definitions.md#transport-protocol)



