# Qiy Node Protocol

# Abstract

This document describes the [Qiy Node Protocol](#qiy-node-protocol): the lifecycle, requests, events and messages of the [Qiy Node](Definitions.md#qiy-node) and their realization.
The document refers for details to the [Qiy Node API](#qiy-node-api), which is available in [Open API Specification](https://swagger.io/specification/)-format and can be viewed with an [online editor](https://editor2.swagger.io/#!/).

# Contents


1. [Introduction](#1-introduction)
	1. [Purpose](#11-purpose)
	1. [Readers' Guidance](#12-readers-guidance)
	1. [Overview](#13-overview)
1. [Requests](#2-requests)
	1. [General](#21-general)
		1. [Health Check](#211-health-check)
		1. [Dynamic Path Endpoint Addresses](#212-dynamic-path-endpoint-addresses)
		1. [Authentication](#213-authentication)
			1. [Java](#2131-java)
			1. [Python](#2132-python)
	1. [Catalogue Requests](#22-catalogue-requests)
		1. [Catalogue Register Request](#221-catalogue-register-request)
		1. [Catalogue Unregister Request](#222-catalogue-unregister-request)
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
	1. [Message Requests](#27-message-requests)
		1. [Message Delete Request](#271-message-delete-request)
		1. [Message Details Request](#272-message-details-request)
		1. [Message Post Request](#273-message-post-request)
		1. [Messages Request](#274-messages-request)
	1. [Operation Requests](#28-operation-requests)
		1. [Operation Execute Request](#281-operation-execute-request)
		1. [Operation Register Request](#282-operation-register-request)
	1. [Qiy Node Requests](#29-qiy-node-requests)
		1. [Qiy Node Delete Request](#291-qiy-node-delete-request)
		1. [Qiy Node Create Request](#292-qiy-node-create-request)
	1. [Service Registration Requests](#210-service-registration-requests)
		1. [Service Register Request](#2101-service-register-request)
		1. [Service Unregister Request](#2102-service-unregister-request)
	1. [Service Provider Registration Requests](#211-service-provider-registration-requests)
		1. [Service Provider Register Request](#2111-service-provider-register-request)
		1. [Service Provider Unregister Request](#2112-service-provider-unregister-request)
	1. [Source Requests](#212-source-requests)
		1. [Source Candidates Request](#2125-source-candidates-request)
		1. [Source Register Request](#2126-source-register-request)
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
		1. [Consent Request Message](#411-consent-request-message)
	1. [Operation Messages](#42-operation-messages)
		1. [Operation Reference Message](#421-operation-reference-message)
		1. [Operation Reference Request Message](#422-operation-reference-request-message)
	1. [Service Credentials Messages](#43-service-credentials-messages)
		1. [Service Credentials Request Message](#431-service-credentials-request-message)
	1. [Portfolio Messages](#44-portfolio-messages)
		1. [Portfolio Register Message](#441-portfolio-register-message)
1. [Index](#5-index)
	1. [Authorization Header Parameter](#authorization-header-parameter)
	1. [Connect Token](#connect-token)
	1. [Connect Token Create Request](#connect-token-create-request)
	1. [Connect Token Register Request](#connect-token-register-request)
	1. [Connection Create Request](#connection-create-request)
	1. [Connection Details Request](#connection-details-request)
	1. [Connections Request](#connections-request)
	1. [Data Provider](#data-provider)
	1. [Data Reference](#data-reference)
	1. [Data Reference Request](#data-reference-request)
	1. [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses)
	1. [Events](#events)
	1. [Events Request](#events-request)
	1. [Message Post Request](#message-post-request)
	1. [Messages Request](#messages-request)
	1. [Operate Request](#operate-request)
	1. [Operation Execute Request](#operation-execute-request)
	1. [Operation Reference Message](#operation-reference-message)
	1. [Operation Reference Request](#operation-reference-request)
	1. [Operation Reference Request Message](#operation-reference-request-message)
	1. [Operation Register Request](#operation-register-request)
	1. [Operation Specification](#operation-specification)
	1. [Persistent Id](#persistent-id)
	1. [Persistent Id Event](#persistent-id-event)
	1. [Qiy Node](#qiy-node)
	1. [Qiy Node Create Request](#qiy-node-create-request)
	1. [Qiy Node Delete Request](#qiy-node-delete-request)
	1. [Qiy Node Message](#qiy-node-message)
	1. [Qiy App](#qiy-app)
	1. [Qiy Node](#qiy-node)
	1. [Relying Party](#relying-party)
	1. [Service Catalogue](#service-catalogue)
	1. [Service Endpoint](#service-endpoint)
	1. [Source Candidate Proposal](#source-candidate-proposal)
	1. [Transport Layer](#transport-layer)
	1. [Transport Protocol](#transport-protocol)


# 1 Introduction

## 1.1 Purpose

This document aims to be the entry point for information analysts and software engineers that need to kow how they can use the [Qiy Node](#qiy-node).

## 1.2 Readers' Guidance

* Information analysts are advised to read all of the document.
* Software engineers are advised to read all of the document and the [Qiy Node API](Definitions.md#qiy-node-api).

## 1.3 Overview

* Chapter [2 Requests](#2-requests) describes the [Qiy Node Requests](Definitions.md#qiy-node-request).
* Chapter [3 Events](#3-events) describes the [Qiy Node Events](Definitions.md#qiy-node-event).
* Chapter [4 Messages](#4-messages) describes the [Qiy Node Messages](Definitions.md#qiy-node-message).
* Chapter [5 Index](#5-index) contains an index for the used terms.


# 2 Requests

This chapter describes the [Qiy Node Requests](Definitions.md#qiy-node-request).

## 2.1 General

### 2.1.1 Health Check

The health of a Qiy Node can be checked with the following request:

GET /admin/healthcheck


### 2.1.2 Dynamic Path Endpoint Addresses

The Qiy Node uses [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses) for all but the /api path endpoint, which is strongly advised to be used at the start of every new day to obtain valid addresses and remain operational.


### 2.1.3 Authentication

Most requests must be authenticated using the [Authorization Header Parameter](#authorization-header-parameter) containing a signature over the Qiy Node Id, the current Unix time in ms using a Private Key which is unique for the Qiy Node.

#### 2.1.3.1 Java

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

#### 2.1.3.2 Python

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

### 2.2.1 Catalogue Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to register a [Service](Definitions.md#service) with an [Access Provider](Definitions.md#access-provider) and include it in a [Service Catalogue](Definitions.md#service-catalogue).

### 2.2.2 Catalogue Unregister Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to unregister a [Service](Definitions.md#service) with an [Access Provider](Definitions.md#access-provider) and remove it from a [Service Catalogue](Definitions.md#service-catalogue).

## 2.3 Connect Token Requests

### 2.3.1 Connect Token Create Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a [Connect Token](Definitions.md#connect-token) from the [Qiy Node](Definitions.md#qiy-node).

### 2.3.2 Connect Token Delete Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Connect Token](Definitions.md#connect-token).

### 2.3.3 Connect Token Details Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Connect Token](Definitions.md#connect-token).

### 2.3.4 Connect Token Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.5 Connect Token Update Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.6 Connect Tokens Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to access [Connect Tokens](Definitions.md#connect-token).


## 2.4 Connection Requests

### 2.4.1 Connection Create Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to create a [Connection](Definitions.md#connection) with a [Connect Token](Definitions.md#connect-token).

### 2.4.2 Connection Delete Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Connection](Definitions.md#connection).

### 2.4.3 Connection Details Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Connection](Definitions.md#connection).

### 2.4.4 Connections Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a list of all the [Connections](Definitions.md#connection) of a [Qiy Node](Definitions.md#qiy-node).

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
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to delete a [Consent](Definitions.md#consent).

### 2.5.2 Consent Denied Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the denial of a [Consent](Definitions.md#consent).

### 2.5.3 Consent Details Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to acquire the details of a [Consent](Definitions.md#consent).

### 2.5.4 Consent Granted Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the granting of a [Consent](Definitions.md#consent).

### 2.5.5 Consent Withdrawn Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the withdrawal of a [Consent](Definitions.md#consent).

### 2.5.6 Consents Request
A [Qiy Node Request](Definitions.md#qiy-node-request) which can be used by [Qiy Users](Definitions.md#qiy-user) to access their [Consents](Definitions.md#consent).

## 2.6 Event Requests

### 2.6.1 Events Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to handle [Qiy Node Events](Definitions.md#qiy-node-event).

## 2.7 Message Requests

### 2.7.1 Message Delete Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.7.2 Message Details Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.7.3 Message Post Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to post a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.7.4 Messages Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a list of all the messages of a [Qiy Node](Definitions.md#qiy-node).

## 2.8 Operation Requests

### 2.8.1 Operation Execute Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to command the execution of an [Operation](Definitions.md#operation) by [Reference](Definitions.md#reference) using an [Operation Reference](Definitions.md#operation-reference).

### 2.8.2 Operation Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain an [Operation Reference](Definitions.md#operation-reference) by registrating an [Operation Specification](Definitions.md#operation-specification).

## 2.9 Qiy Node Requests

### 2.9.1 Qiy Node Delete Request
A [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Qiy Node](Definitions.md#qiy-node).

### 2.9.2 Qiy Node Create Request
A [HTTP Request](Definitions.md#http-request) to create a [Qiy Node](Definitions.md#qiy-node).

## 2.10 Service Registration Requests

### 2.10.1 Service Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) to register a [Service](Definitions.md#service).

### 2.10.2 Service Unregister Request
A [Qiy Node Request](Definitions.md#qiy-node-request) to unregister a [Service](Definitions.md#service).

## 2.11 Service Provider Registration Requests

### 2.11.1 Service Provider Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to register a [Service Provider](Definitions.md#service-provider) with the [Qiy Trust Network](Definitions.md#qiy-trust-network).

### 2.11.2 Service Provider Unregister Request
A [Qiy Node Request](Definitions.md#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to unregister a [Service Provider](Definitions.md#service-provider) with the [Qiy Trust Network](Definitions.md#qiy-trust-network).

## 2.12 Source Requests

### 2.12.5 Source Candidates Request
A [Qiy Node Request](Definitions.md#qiy-node-request) to obtain candidate [Service Providers](Definitions.md#service-provider) for a [Service](Definitions.md#service).

### 2.12.6 Source Register Request
A [Qiy Node Request](Definitions.md#qiy-node-request) to register a [Service Provider](Definitions.md#service-provider) as source for a [Service](Definitions.md#service).



# 3 Events

A Qiy Application can use the [Events Request](#events-request) to start listening to the [Events](#events) generated by its Qiy Node.
The Events comply to the [Server-Sent Events Standard](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

## 3.1 Connection Events

### 3.1.1 Connection Created Event
A [Qiy Node Event](Definitions.md#qiy-node-event) that is generated when a [Connection](Definitions.md#connection) has been created.

## 3.2 Consent Events

### 3.2.1 Consent Denied Event
A [Qiy Node Event](Definitions.md#qiy-node-event) which can be used to communicate the denial of a [Consent](Definitions.md#consent).

### 3.2.2 Consent Granted Event
A [Qiy Node Event](Definitions.md#qiy-node-event) which can be used to communicate the granting or regranting of a [Consent](Definitions.md#consent).

## 3.3 Message Events

### 3.3.1 Message Received Event
A [Qiy Node Event](Definitions.md#qiy-node-event) that notifies a [Receiver](Definitions.md#receiver) that he has received a new [Qiy Node Message](Definitions.md#qiy-node-message).

## 3.4 Persistent Id Events

### 3.4.1 Persistent Id Event
A [Qiy Node Event](Definitions.md#qiy-node-event) which is used to communicate the [Persistent Id](Definitions.md#persistent-id) of a new [Connection](Definitions.md#connection).


# 4 Messages

This chapter describes the [Qiy Node Messages](#qiy-node-messages).

## 4.1 Consent Messages

### 4.1.1 Consent Request Message

A [Qiy Node Message](Definitions.md#qiy-node-message) which can be used to [Request](Definitions.md#request) for a [Consent](Definitions.md#consent).

## 4.2 Operation Messages

### 4.2.1 Operation Reference Message
A [Qiy Node Message](Definitions.md#qiy-node-message) that can be used to convey [Operation References](Definitions.md#operation-reference).

### 4.2.2 Operation Reference Request Message
A [Qiy Node Message](Definitions.md#qiy-node-message) that can be used to [Request](Definitions.md#request) for [Operation References](Definitions.md#operation-reference).

## 4.3 Service Credentials Messages

### 4.3.1 Service Credentials Request Message
A [Qiy Node Message](Definitions.md#qiy-node-message) for requesting [Service Credentials](Definitions.md#service-credentials).

## 4.4 Portfolio Messages

### 4.4.1 Portfolio Register Message
A [Qiy Node Message](Definitions.md#qiy-node-message) which can be used to add a [Service Provider](Definitions.md#service-provider) to a [Service Portfolio](Definitions.md#service-portfolio).



# 5 Index

## Authorization Header Parameter

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.3 Authentication](#213-authentication)

## Connect Token

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connect Token](Definitions.md#connect-token)
[Qiy Node API](Qiy%20Node%20API.json) | [Connect Token Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConnectTokenModel)

## Connect Token Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connect Token Create Request](Definitions.md#connect-token-create-request)
[Qiy Node API](Qiy%20Node%20API.json) | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ctCreateEndpointPost)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectTokenUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.1 Connect Token Create Request](#231-connect-token-create-request)

## Connect Token Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connect Token Register Request](Definitions.md#connect-token-register-request)
[Qiy Node API](Qiy%20Node%20API.json) | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ctCreateEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.4 Connect Token Register Request](#234-connect-token-register-request)

## Connection Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connection Create Request](Definitions.md#connection-create-request)
[Qiy Node API](Qiy%20Node%20API.json) | [POST /scanEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#scanEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.1 Connection Create Request](#241-connection-create-request)

## Connection Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connection Details Request](Definitions.md#connection-details-request)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /connectionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.3 Connection Details Request](#243-connection-details-request)

## Connections Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Connections Request](Definitions.md#connections-request)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /connectionsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.4 Connections Request](#244-connections-request)

## Data Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Data Provider](Definitions.md#data-provider)

## Data Reference

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Data Reference](Definitions.md#data-reference)

## Data Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Data Reference Request]

## Dynamic Path Endpoint Addresses

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json) | [Path Endpoint Addresses](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PathEndpointAddresses)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.2 Dynamic Path Endpoint Addresses](#212-dynamic-path-endpoint-addresses)

## Events

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json) | [Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#EventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3 Events](#3-events)

## Events Request

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json) | [GET /eventsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#eventsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.6 Events Request](#26-events-request)

## Message Post Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Message Post Request](Definitions.md#message-post-request)
[Qiy Node API](Qiy%20Node%20API.json) | [POST /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#mboxUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Message Post Request](Definitions.md#message-post-request)

## Messages Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Messages Request](Definitions.md#messages-request)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#mboxUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Messages Request](Definitions.md#messages-request)

## Operate Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operate Request]
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operate Request]

## Operation Execute Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Execute Request](Definitions.md#operation-execute-request)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /refsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#refsEndpointGet)
[Qiy Node API](Qiy%20Node%20API.json) | [GET /refEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#refEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Execute Request](Definitions.md#operation-execute-request)


## Operation Reference Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Reference Message](Definitions.md#operation-reference-message)
[Qiy Node API](Qiy%20Node%20API.json) | tbd
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference Message](Definitions.md#operation-reference-message)

## Operation Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Reference Request]
[Qiy Node API](Qiy%20Node%20API.json) | [Operation Reference Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationReferenceRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference Request]

## Operation Reference Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Reference Request Message](Definitions.md#operation-reference-request-message)
[Qiy Node API](Qiy%20Node%20API.json) | [Operation Reference Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationReferenceRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference Request Message](Definitions.md#operation-reference-request-message)

## Operation Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Register Request](Definitions.md#operation-register-request)
[Qiy Node API](Qiy%20Node%20API.json) | [POST /refsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#refsEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Register Request](Definitions.md#operation-register-request)

## Operation Specification

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Operation Specification](Definitions.md#operation-specification)
[Qiy Node API](Qiy%20Node%20API.json) | [Operation Specification Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationSpecificationModel)

## Persistent Id

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Persistent Id](Definitions.md#persistent-id)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [6.3.2 Accepter Events](#632-accepter-events)

## Persistent Id Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Persistent Id Event](Definitions.md#persistent-id-event)
[Qiy Node API](Qiy%20Node%20API.json) | [Persistent Id Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PersistentIdEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Persistent Id Event](Definitions.md#persistent-id-event)

## Qiy Node

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Qiy Node](Definitions.md#qiy-node)

## Qiy Node Create Request

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json) | [POST /createEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#createEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node Create Request](Definitions.md#qiy-node-create-request)

## Qiy Node Delete Request

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json) | [DELETE /owners/id/{id}](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ownersIdIdDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node Delete Request](Definitions.md#qiy-node-delete-request)

## Qiy Node Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Qiy Node Message](Definitions.md#qiy-node-message)
[Qiy Node API](Qiy%20Node%20API.json) | [Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#MessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Qiy Node Message](Definitions.md#qiy-node-message)

## Qiy App

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Qiy Application](Definitions.md#qiy-application)

## Qiy Node

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Qiy Node](Definitions.md#qiy-node)

## Relying Party

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Relying Party](Definitions.md#relying-party)

## Service Catalogue

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Service Catalogue](Definitions.md#service-catalogue)

## Service Endpoint

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Service Endpoint](Definitions.md#service-endpoint)

## Source Candidate Proposal

tbd

## Transport Layer

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Transport Layer](Definitions.md#transport-layer)

## Transport Protocol

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Transport Protocol](Definitions.md#transport-protocol)



