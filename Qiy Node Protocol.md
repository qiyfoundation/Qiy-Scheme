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
		1. [Versions](#212-versions)
		1. [Dynamic Path Endpoint Addresses](#213-dynamic-path-endpoint-addresses)
		1. [Authentication](#214-authentication)
			1. [Java](#2141-java)
			1. [Python](#2142-python)
	1. [Catalogue Requests](#22-catalogue-requests)
		1. [Catalogue Details Request](#221-catalogue-details-request)
		1. [Catalogue Service Details Request](#222-catalogue-service-details-request)
		1. [Catalogue Service Register Request](#223-catalogue-service-register-request)
		1. [Catalogue Service Unregister Request](#224-catalogue-service-unregister-request)
		1. [Catalogues Request](#225-catalogues-request)
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
		1. [Library Details Request](#271-library-details-request)
		1. [Library Service Details Request](#272-library-service-details-request)
		1. [Library Service Register Request](#273-library-service-register-request)
		1. [Library Service Unregister Request](#274-library-service-unregister-request)
		1. [Library Service Update Request](#275-library-service-update-request)
		1. [Library Services Request](#276-library-services-request)
		1. [Provider Details Request](#277-provider-details-request)
		1. [Provider Register Request](#278-provider-register-request)
		1. [Provider Unregister Request](#279-provider-unregister-request)
		1. [Provider Update Request](#2710-provider-update-request)
		1. [Providers Request](#2711-providers-request)
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
		1. [Portfolio Details Request](#2101-portfolio-details-request)
		1. [Portfolio Service Details Request](#2102-portfolio-service-details-request)
		1. [Portfolio Services Request](#2103-portfolio-services-request)
	1. [Qiy Node Requests](#211-qiy-node-requests)
		1. [Qiy Node Create Request](#2111-qiy-node-create-request)
		1. [Qiy Node Delete Request](#2112-qiy-node-delete-request)
	1. [Source Requests](#212-source-requests)
		1. [Source Candidates Request](#2121-source-candidates-request)
		1. [Source Details Request](#2122-source-details-request)
		1. [Source Register Request](#2123-source-register-request)
		1. [Source Unregister Request](#2124-source-unregister-request)
		1. [Source Update Request](#2125-source-update-request)
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
	1. [Service Credentials Messages](#44-service-credentials-messages)
		1. [Service Credentials Request Message](#441-service-credentials-request-message)
	1. [Source Messages](#45-source-messages)
		1. [Source Candidates Message](#451-source-candidates-message)
1. [Models](#5-models)
	1. [Catalogue](#51-catalogue)
		1. [Catalogue Attributes](#511-catalogue-attributes)
		1. [Catalogue Relations](#512-catalogue-relations)
		1. [Catalogue Business Rules](#513-catalogue-business-rules)
	1. [Connect Token](#52-connect-token)
		1. [Connect Token Attributes](#521-connect-token-attributes)
		1. [Connect Token Relations](#522-connect-token-relations)
		1. [Connect Token Business Rules](#523-connect-token-business-rules)
	1. [Connection](#53-connection)
		1. [Connection Attributes](#531-connection-attributes)
		1. [Connection Relations](#532-connection-relations)
		1. [Connection Business Rules](#533-connection-business-rules)
	1. [Consent](#54-consent)
		1. [Consent Attributes](#541-consent-attributes)
		1. [Consent Relations](#542-consent-relations)
		1. [Consent Business Rules](#543-consent-business-rules)
	1. [Event](#55-event)
		1. [Event Attributes](#551-event-attributes)
		1. [Event Relations](#552-event-relations)
		1. [Event Business Rules](#553-event-business-rules)
	1. [Library](#56-library)
		1. [Library Attributes](#561-library-attributes)
		1. [Library Relations](#562-library-relations)
		1. [Library Business Rules](#563-library-business-rules)
	1. [Message](#57-message)
		1. [Message Attributes](#571-message-attributes)
		1. [Message Relations](#572-message-relations)
		1. [Message Business Rules](#573-message-business-rules)
	1. [Operation Specification](#58-operation-specification)
		1. [Operation Specification Attributes](#581-operation-specification-attributes)
		1. [Operation Specification Relations](#582-operation-specification-relations)
		1. [Operation Specification Business Rules](#583-operation-specification-business-rules)
	1. [Portfolio](#59-portfolio)
		1. [Portfolio Attributes](#591-portfolio-attributes)
		1. [Portfolio Relations](#592-portfolio-relations)
		1. [Portfolio Business Rules](#593-portfolio-business-rules)
	1. [Qiy Node Credentials](#510-qiy-node-credentials)
		1. [Qiy Node Credentials Attributes](#5101-qiy-node-credentials-attributes)
		1. [Qiy Node Credentials Relations](#5102-qiy-node-credentials-relations)
		1. [Qiy Node Credentials Business Rules](#5103-qiy-node-credentials-business-rules)
	1. [Service Description](#511-service-description)
		1. [Service Description Attributes](#5111-service-description-attributes)
		1. [Service Description Relations](#5112-service-description-relations)
		1. [Service Description Business Rules](#5113-service-description-business-rules)
1. [Index](#6-index)
	1. [Authorization Header Parameter](#authorization-header-parameter)
	1. [Catalogue](#catalogue)
	1. [Catalogue Details Request](#catalogue-details-request)
	1. [Catalogue Service Details Request](#catalogue-service-details-request)
	1. [Catalogue Service Register Request](#catalogue-service-register-request)
	1. [Catalogue Service Unregister Request](#catalogue-service-unregister-request)
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
	1. [Data Source](#data-source)
	1. [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses)
	1. [Event](#event)
	1. [Events Request](#events-request)
	1. [Library](#library)
	1. [Library Details Request](#library-details-request)
	1. [Library Service Details Request](#library-service-details-request)
	1. [Library Service Register Request](#library-service-register-request)
	1. [Library Service Unregister Request](#library-service-unregister-request)
	1. [Library Service Update Request](#library-service-update-request)
	1. [Library Services Request](#library-services-request)
	1. [Message](#message)
	1. [Message Delete Request](#message-delete-request)
	1. [Message Details Request](#message-details-request)
	1. [Message Post Request](#message-post-request)
	1. [Message Received Event](#message-received-event)
	1. [Messages Request](#messages-request)
	1. [Operation Execute Request](#operation-execute-request)
	1. [Operation Reference Message](#operation-reference-message)
	1. [Operation Reference Request](#operation-reference-request)
	1. [Operation Reference Request Message](#operation-reference-request-message)
	1. [Operation Register Request](#operation-register-request)
	1. [Operation Specification](#operation-specification)
	1. [Operation Specification Request Message](#operation-specification-request-message)
	1. [Persistent Id](#persistent-id)
	1. [Persistent Id Event](#persistent-id-event)
	1. [Portfolio](#portfolio)
	1. [Portfolio Details Request](#portfolio-details-request)
	1. [Portfolio Service Details Request](#portfolio-service-details-request)
	1. [Portfolio Register Message](#portfolio-register-message)
	1. [Portfolio Services Request](#portfolio-services-request)
	1. [Provider](#provider)
	1. [Provider Details Request](#provider-details-request)
	1. [Provider Register Request](#provider-register-request)
	1. [Provider Unregister Request](#provider-unregister-request)
	1. [Provider Update Request](#provider-update-request)
	1. [Providers Request](#providers-request)
	1. [Qiy Node](#qiy-node)
	1. [Qiy Node Create Request](#qiy-node-create-request)
	1. [Qiy Node Credentials](#qiy-node-credentials)
	1. [Qiy Node Delete Request](#qiy-node-delete-request)
	1. [Qiy Node Message](#qiy-node-message)
	1. [Qiy App](#qiy-app)
	1. [Qiy Node](#qiy-node)
	1. [Relying Party](#relying-party)
	1. [Service](#service)
	1. [Service Catalogue](#service-catalogue)
	1. [Service Credentials Request Message](#service-credentials-request-message)
	1. [Service Description](#service-description)
	1. [Service Endpoint](#service-endpoint)
	1. [Service Portfolio](#service-portfolio)
	1. [Service Provider](#service-provider)
	1. [Source](#source)
	1. [Source Candidates Message](#source-candidates-message)
	1. [Source Candidates Request](#source-candidates-request)
	1. [Source Details Request](#source-details-request)
	1. [Source Register Request](#source-register-request)
	1. [Source Unregister Request](#source-unregister-request)
	1. [Source Update Request](#source-update-request)
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
* Chapter [5 Models](#5-models) describes the entities of the [Qiy Node Interface](Definitions.md#qiy-node-interface).
* Chapter [6 Index](#6-index) contains an index for the used terms.


# 2 Requests

This chapter describes the [Qiy Node Requests](Definitions.md#qiy-node-request).

## 2.1 General

### 2.1.1 Health Check

The health of a Qiy Node can be checked with the following request:

GET /admin/healthcheck


### 2.1.2 Versions

The supported [Qiy Node API](Definitions.md#qiy-node-api) version can be obtained with the call:

[GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#apiGet)

The returned version tag complies with Semantic Versioning 2.0.0, see [https://semver.org](https://semver.org).
[Qiy Node Implementations](Definitions.md#qiy-node-implementation) are to support the two latest major versions, with the additional rule that a new major version will never be released within 6 months of its predecessor.

### 2.1.3 Dynamic Path Endpoint Addresses

The Qiy Node uses [Dynamic Path Endpoint Addresses](#dynamic-path-endpoint-addresses) for all but the /api path endpoint, which is strongly advised to be used at the start of every new day to obtain valid addresses and remain operational.
To obtain the endpoint addresses, use:

[GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#apiGet)

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
The [Catalogue Details Request](#catalogue-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to get the details of a [Service Catalogue](Definitions.md#service-catalogue).

### 2.2.2 Catalogue Service Details Request
The [Catalogue Service Details Request](#catalogue-service-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to get the details of a [Service](Definitions.md#service) that has been published in a [Service Catalogue](Definitions.md#service-catalogue).

### 2.2.3 Catalogue Service Register Request
The [Catalogue Service Register Request](#catalogue-service-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to register a [Service](Definitions.md#service) of a [Service Provider](Definitions.md#service-provider) with an [Access Provider](Definitions.md#access-provider) and include it in [Service Catalogue](Definitions.md#service-catalogue) of the [Service Provider](Definitions.md#service-provider).

### 2.2.4 Catalogue Service Unregister Request
The [Catalogue Service Unregister Request](#catalogue-service-unregister-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to unregister a [Service](Definitions.md#service) of a [Service Provider](Definitions.md#service-provider) with an [Access Provider](Definitions.md#access-provider) and remove it from the [Service Catalogue](Definitions.md#service-catalogue) of the [Service Provider](Definitions.md#service-provider).

### 2.2.5 Catalogues Request
The [Catalogues Request](#catalogues-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to consult the [Service Catalogues](Definitions.md#service-catalogue) of [Service Providers](Definitions.md#service-provider).

## 2.3 Connect Token Requests

### 2.3.1 Connect Token Create Request
The [Connect Token Create Request](#connect-token-create-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a [Connect Token](Definitions.md#connect-token) from the [Qiy Node](Definitions.md#qiy-node).

### 2.3.2 Connect Token Delete Request
The [Connect Token Delete Request](#connect-token-delete-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Connect Token](Definitions.md#connect-token).

### 2.3.3 Connect Token Details Request
The [Connect Token Details Request](#connect-token-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Connect Token](Definitions.md#connect-token).

### 2.3.4 Connect Token Register Request
The [Connect Token Register Request](#connect-token-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.5 Connect Token Update Request
The [Connect Token Update Request](#connect-token-update-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to register a [Connect Token](Definitions.md#connect-token).

### 2.3.6 Connect Tokens Request
The [Connect Tokens Request](#connect-tokens-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to access [Connect Tokens](Definitions.md#connect-token).


## 2.4 Connection Requests

### 2.4.1 Connection Create Request
The [Connection Create Request](#connection-create-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to create a [Connection](Definitions.md#connection) using a [Connect Token](Definitions.md#connect-token).

### 2.4.2 Connection Delete Request
The [Connection Delete Request](#connection-delete-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Connection](Definitions.md#connection).

### 2.4.3 Connection Details Request
The [Connection Details Request](#connection-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Connection](Definitions.md#connection).

### 2.4.4 Connections Request
The [Connections Request](#connections-request) is a  [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a list of all the [Connections](Definitions.md#connection) of a [Qiy Node](Definitions.md#qiy-node).

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
The [Consent Delete Request](#consent-delete-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to delete a [Consent](Definitions.md#consent).

### 2.5.2 Consent Denied Request
The [Consent Denied Request](#consent-denied-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the denial of a [Consent](Definitions.md#consent).

### 2.5.3 Consent Details Request
The [Consent Details Request](#consent-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to acquire the details of a [Consent](Definitions.md#consent).

### 2.5.4 Consent Granted Request
The [Consent Granted Request](#consent-granted-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the granting of a [Consent](Definitions.md#consent).

### 2.5.5 Consent Withdrawn Request
The [Consent Withdrawn Request](#consent-withdrawn-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to communicate the withdrawal of a [Consent](Definitions.md#consent).

### 2.5.6 Consents Request
The [Consents Request](#consents-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to access [Consents](Definitions.md#consent).

## 2.6 Event Requests

### 2.6.1 Events Request
The [Events Request](#events-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to handle [Qiy Node Events](Definitions.md#qiy-node-event).

## 2.7 Library Requests

### 2.7.1 Library Details Request
The [Library Details Request](#library-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to get the details of the [Service Library](Definitions.md#service-library).

### 2.7.2 Library Service Details Request
The [Library Service Details Request](#library-service-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to get the details of a [Service](Definitions.md#service) in the [Service Library](Definitions.md#service-library).

### 2.7.3 Library Service Register Request
The [Library Service Register Request](#library-service-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to register a [Service](Definitions.md#service) in the [Service Library](Definitions.md#service-library).

### 2.7.4 Library Service Unregister Request
The [Library Service Unregister Request](#library-service-unregister-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to register a [Service](Definitions.md#service) in the [Service Library](Definitions.md#service-library).

### 2.7.5 Library Service Update Request
The [Library Service Update Request](#library-service-update-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to update the details of a [Service](Definitions.md#service) in the [Service Library](Definitions.md#service-library).

### 2.7.6 Library Services Request
The [Library Services Request](#library-services-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to list the [Services](Definitions.md#service) that are registered in the [Service Library](Definitions.md#service-library).

### 2.7.7 Provider Details Request
The [Provider Details Request](#provider-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to get the details of a [Service Provider](Definitions.md#service-provider).

### 2.7.8 Provider Register Request
The [Provider Register Request](#provider-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to register a [Service Provider](Definitions.md#service-provider) with the [Qiy Trust Network](Definitions.md#qiy-trust-network).

### 2.7.9 Provider Unregister Request
The [Provider Unregister Request](#provider-unregister-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to unregister a [Service Provider](Definitions.md#service-provider) from the [Qiy Trust Network](Definitions.md#qiy-trust-network).

### 2.7.10 Provider Update Request
The [Provider Update Request](#provider-update-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) for [Access Providers](Definitions.md#access-provider) to update details of a [Service Provider](Definitions.md#service-provider).

### 2.7.11 Providers Request
The [Providers Request](#providers-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to list [Service Providers](Definitions.md#service-provider).

## 2.8 Message Requests

### 2.8.1 Message Delete Request
The [Message Delete Request](#message-delete-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to delete a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.8.2 Message Details Request
The [Message Details Request](#message-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to get the details of a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.8.3 Message Post Request
The [Message Post Request](#message-post-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to post a [Qiy Node Message](Definitions.md#qiy-node-message).

### 2.8.4 Messages Request
The [Messages Request](#messages-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain a list of all the messages of a [Qiy Node](Definitions.md#qiy-node).

## 2.9 Operation Requests

### 2.9.1 Operation Execute Request
The [Operation Execute Request](#operation-execute-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to command the execution of an [Operation](Definitions.md#operation) by [Reference](Definitions.md#reference) using an [Operation Reference](Definitions.md#operation-reference).

### 2.9.2 Operation Reference Request
The [Operation Reference Request](#operation-reference-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain an [Operation Reference](Definitions.md#operation-reference) for a [Data Source](Definitions.md#data-source) of a [Consent](Definitions.md#consent).

### 2.9.3 Operation Register Request
The [Operation Register Request](#operation-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used to obtain an [Operation Reference](Definitions.md#operation-reference) by registering an [Operation Specification](Definitions.md#operation-specification).

## 2.10 Portfolio Requests

### 2.10.1 Portfolio Details Request
The [Portfolio Details Request](#portfolio-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) that can be used by a [Qiy User](Definitions.md#qiy-user) to get the details of his [Service Portfolio](Definitions.md#service-portfolio).

### 2.10.2 Portfolio Service Details Request
The [Portfolio Service Details Request](#portfolio-service-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to get the details of a [Service](Definitions.md#service) in a [Service Portfolio](Definitions.md#service-portfolio).

### 2.10.3 Portfolio Services Request
The [Portfolio Services Request](#portfolio-services-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) which can be used to list the [Service](Definitions.md#service) in a [Service Portfolio](Definitions.md#service-portfolio).

## 2.11 Qiy Node Requests

### 2.11.1 Qiy Node Create Request
The [Qiy Node Create Request](#qiy-node-create-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to create a [Qiy Node](Definitions.md#qiy-node).

### 2.11.2 Qiy Node Delete Request
The [Qiy Node Delete Request](#qiy-node-delete-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to delete a [Qiy Node](Definitions.md#qiy-node).

## 2.12 Source Requests

### 2.12.1 Source Candidates Request
The [Source Candidates Request](#source-candidates-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to obtain candidate [Data Sources](Definitions.md#data-source) for a [Consent](Definitions.md#consent).

### 2.12.2 Source Details Request
The [Source Details Request](#source-details-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) for [Qiy Users](Definitions.md#qiy-user) to obtain details of a [Data Source](Definitions.md#data-source) of a [Consent](Definitions.md#consent).

### 2.12.3 Source Register Request
The [Source Register Request](#source-register-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to register [Data Sources](Definitions.md#data-source) for a [Consent](Definitions.md#consent).

### 2.12.4 Source Unregister Request
The [Source Unregister Request](#source-unregister-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to unregister [Data Sources](Definitions.md#data-source) for a [Consent](Definitions.md#consent).

### 2.12.5 Source Update Request
The [Source Update Request](#source-update-request) is a [Qiy Node Request](Definitions.md#qiy-node-request) to update [Data Sources](Definitions.md#data-source) for a [Consent](Definitions.md#consent).


# 3 Events

A [Qiy Application](Definitions.md#qiy-application) can use the [Events Request](#events-request) to start listening to the [Events](#event) generated by its [Qiy Node](Definitions.md#qiy-node).
The Events comply to the Server-Sent Events Standard, see [https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

## 3.1 Connection Events

### 3.1.1 Connection Created Event
The [Connection Created Event](#connection-created-event) is a [Qiy Node Event](Definitions.md#qiy-node-event) that is generated when a [Connection](Definitions.md#connection) has been created.

## 3.2 Consent Events

### 3.2.1 Consent Denied Event
The [Consent Denied Event](#consent-denied-event) is a [Qiy Node Event](Definitions.md#qiy-node-event) which can be used to communicate the denial of a [Consent](Definitions.md#consent).

### 3.2.2 Consent Granted Event
The [Consent Granted Event](#consent-granted-event) is a [Qiy Node Event](Definitions.md#qiy-node-event) which can be used to communicate the granting or regranting of a [Consent](Definitions.md#consent).

## 3.3 Message Events

### 3.3.1 Message Received Event
The [Message Received Event](#message-received-event) is a [Qiy Node Event](Definitions.md#qiy-node-event) that notifies a [Receiver](Definitions.md#receiver) that he has received a new [Qiy Node Message](Definitions.md#qiy-node-message).

## 3.4 Persistent Id Events

### 3.4.1 Persistent Id Event
The [Persistent Id Event](#persistent-id-event) is a [Qiy Node Event](Definitions.md#qiy-node-event) which is used to communicate the [Persistent Id](Definitions.md#persistent-id) of a new [Connection](Definitions.md#connection).


# 4 Messages

This chapter describes the [Qiy Node Messages](#message).

## 4.1 Consent Messages

### 4.1.1 Consent Notification Message

The [Consent Notification Message](#consent-notification-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) which can be used to notify the registration of a [Consent](Definitions.md#consent).

### 4.1.2 Consent Request Message

The [Consent Request Message](#consent-request-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) which can be used to [Request](Definitions.md#request) for a [Consent](Definitions.md#consent).

## 4.2 Operation Messages

### 4.2.1 Operation Reference Message
The [Operation Reference Message](#operation-reference-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) that can be used to convey [Operation References](Definitions.md#operation-reference).

### 4.2.2 Operation Reference Request Message
The [Operation Reference Request Message](#operation-reference-request-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) that can be used to [Request](Definitions.md#request) for [Operation References](Definitions.md#operation-reference).

### 4.2.3 Operation Specification Request Message
The [Operation Specification Request Message](#operation-specification-request-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) to request for an [Operation Specification](Definitions.md#operation-specification).

## 4.3 Portfolio Messages

### 4.3.1 Portfolio Register Message
The [Portfolio Register Message](#portfolio-register-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) to add a [Service Provider](Definitions.md#service-provider) to a [Service Portfolio](Definitions.md#service-portfolio).

## 4.4 Service Credentials Messages

### 4.4.1 Service Credentials Request Message
The [Service Credentials Request Message](#service-credentials-request-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) for requesting [Service Credentials](Definitions.md#service-credentials).

## 4.5 Source Messages

### 4.5.1 Source Candidates Message
The [Source Candidates Message](#source-candidates-message) is a [Qiy Node Message](Definitions.md#qiy-node-message) to propose candidate [Data Sources](Definitions.md#data-source) for a [Consent](Definitions.md#consent).


# 5 Models

This chapters describes the entities of the [Qiy Node Interface](Definitions.md#qiy-node-interface).

## 5.1 Catalogue

### 5.1.1 Catalogue Attributes

See [Catalogue](#catalogue) model.

### 5.1.2 Catalogue Relations

See [Catalogue](#catalogue) model.

### 5.1.3 Catalogue Business Rules

tbd

## 5.2 Connect Token

### 5.2.1 Connect Token Attributes

See [Connect Token](#connect-token) model.

### 5.2.2 Connect Token Relations

See [Connect Token](#connect-token) model.

### 5.2.3 Connect Token Business Rules

tbd

## 5.3 Connection

### 5.3.1 Connection Attributes

See [Connection](#connection) model.

### 5.3.2 Connection Relations

See [Connection](#connection) model.

### 5.3.3 Connection Business Rules

tbd

## 5.4 Consent

### 5.4.1 Consent Attributes

See [Consent](#consent) model.

### 5.4.2 Consent Relations

See [Consent](#consent) model.

### 5.4.3 Consent Business Rules

tbd

## 5.5 Event

### 5.5.1 Event Attributes

See [Event](#event) model.

### 5.5.2 Event Relations

See [Event](#event) model.

### 5.5.3 Event Business Rules

tbd

## 5.6 Library

### 5.6.1 Library Attributes

See [Library](#library) model.

### 5.6.2 Library Relations

See [Library](#library) model.

### 5.6.3 Library Business Rules

tbd

## 5.7 Message

### 5.7.1 Message Attributes

See [Message](#message) model.

### 5.7.2 Message Relations

See [Message](#message) model.

### 5.7.3 Message Business Rules

tbd

## 5.8 Operation Specification

### 5.8.1 Operation Specification Attributes

See [Operation Specification](#operation-specification) model.

### 5.8.2 Operation Specification Relations

See [Operation Specification](#operation-specification) model.

### 5.8.3 Operation Specification Business Rules

tbd

## 5.9 Portfolio

### 5.9.1 Portfolio Attributes

See [Portfolio](#portfolio) model.

### 5.9.2 Portfolio Relations

See [Portfolio](#portfolio) model.

### 5.9.3 Portfolio Business Rules

tbd

## 5.10 Qiy Node Credentials

### 5.10.1 Qiy Node Credentials Attributes

See [Qiy Node Credentials](#qiy-node-credentials) model.

### 5.10.2 Qiy Node Credentials Relations

See [Qiy Node Credentials](#qiy-node-credentials) model.

### 5.10.3 Qiy Node Credentials Business Rules

tbd

## 5.11 Service Description

### 5.11.1 Service Description Attributes

See [Service Description](#service-description) model.

### 5.11.2 Service Description Relations

See [Service Description](#service-description) model.

### 5.11.3 Service Description Business Rules

tbd


# 6 Index

## Authorization Header Parameter

Specification | Reference
------------- | ---------
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.4 Authentication](#214-authentication)

## Catalogue

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Catalogue](Definitions.md#service-catalogue)
[Qiy Node API](Qiy%20Node%20API.json)         | [Catalogue Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#CatalogueModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.1 Catalogue](#51-catalogue)

## Catalogue Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogue Details Request](Definitions.md#catalogue-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /catalogueUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#catalogueUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.1 Catalogue Details Request](#221-catalogue-details-request)

## Catalogue Service Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogue Service Details Request](Definitions.md#catalogue-service-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /catalogueServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#catalogueServiceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.2 Catalogue Service Details Request](#222-catalogue-service-details-request)

## Catalogue Service Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogue Service Register Request](Definitions.md#catalogue-service-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /cataloguesEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#cataloguesEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.3 Catalogue Service Register Request](#223-catalogue-service-register-request)

## Catalogue Service Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogue Service Unregister Request](Definitions.md#catalogue-service-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /catalogueServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#catalogueServiceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.4 Catalogue Service Unregister Request](#224-catalogue-service-unregister-request)

## Catalogues Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Catalogues Request](Definitions.md#catalogues-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /cataloguesEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#cataloguesEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.2.4 Catalogues Request](#224-catalogues-request)

## Connect Token

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token](Definitions.md#connect-token)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connect Token Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConnectTokenModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.2 Connect Token](#52-connect-token)

## Connect Token Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Create Request](Definitions.md#connect-token-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ctCreateEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.1 Connect Token Create Request](#231-connect-token-create-request)

## Connect Token Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Delete Request](Definitions.md#connect-token-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectTokenUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.2 Connect Token Delete Request](#232-connect-token-delete-request)

## Connect Token Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Details Request](Definitions.md#connect-token-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectTokenUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.3 Connect Token Details Request](#233-connect-token-details-request)

## Connect Token Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Register Request](Definitions.md#connect-token-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /ctCreateEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ctCreateEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.4 Connect Token Register Request](#234-connect-token-register-request)

## Connect Token Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Token Update Request](Definitions.md#connect-token-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /connectTokenUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectTokenUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.5 Connect Token Update Request](#235-connect-token-update-request)

## Connect Tokens Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connect Tokens Request](Definitions.md#connect-tokens-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /ctListEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ctListEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.3.6 Connect Tokens Request](#236-connect-tokens-request)

## Connection

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection](Definitions.md#connection)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connection Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConnectionModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.3 Connection](#53-connection)

## Connection Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Create Request](Definitions.md#connection-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /connectionsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionsEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.1 Connection Create Request](#241-connection-create-request)

## Connection Created Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Created Event](Definitions.md#connection-created-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Connection Created Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConnectionCreatedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.1.1 Connection Created Event](#311-connection-created-event)

## Connection Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Delete Request](Definitions.md#connection-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /connectionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.2 Connection Delete Request](#242-connection-delete-request)

## Connection Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connection Details Request](Definitions.md#connection-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectionUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.3 Connection Details Request](#243-connection-details-request)

## Connections Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Connections Request](Definitions.md#connections-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /connectionsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#connectionsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.4.4 Connections Request](#244-connections-request)

## Consent

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent](Definitions.md#consent)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConsentModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.4 Consent](#54-consent)

## Consent Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Delete Request](Definitions.md#consent-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.1 Consent Delete Request](#251-consent-delete-request)

## Consent Denied Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Denied Event](Definitions.md#consent-denied-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Denied Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConsentDeniedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.2.1 Consent Denied Event](#321-consent-denied-event)

## Consent Denied Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Denied Request](Definitions.md#consent-denied-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.2 Consent Denied Request](#252-consent-denied-request)

## Consent Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Details Request](Definitions.md#consent-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.3 Consent Details Request](#253-consent-details-request)

## Consent Granted Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Consent Granted Event](Definitions.md#consent-granted-event)
[Qiy Node API](Qiy%20Node%20API.json) | [Consent Granted Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConsentGrantedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.2.2 Consent Granted Event](#322-consent-granted-event)

## Consent Granted Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Granted Request](Definitions.md#consent-granted-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.4 Consent Granted Request](#254-consent-granted-request)

## Consent Notification Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Notification Message](Definitions.md#consent-notification-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Consent Notification Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConsentNotificationMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.1.1 Consent Notification Message](#411-consent-notification-message)

## Consent Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                       | [Consent Request Message](Definitions.md#consent-request-message)
[Qiy Node API](Qiy%20Node%20API.json) | [Consent Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ConsentRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.1.2 Consent Request Message](#412-consent-request-message)

## Consent Withdrawn Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consent Withdrawn Request](Definitions.md#consent-withdrawn-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.5 Consent Withdrawn Request](#255-consent-withdrawn-request)

## Consents Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Consents Request](Definitions.md#consents-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.5.6 Consents Request](#256-consents-request)

## Data Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Provider](Definitions.md#data-provider)

## Data Reference

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Reference](Definitions.md#data-reference)

## Data Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Data Reference Request](Definitions.md#data-reference-request)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Operation Reference Request](#operation-reference-request)

## Data Source

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Source](Definitions.md#data-source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Dynamic Path Endpoint Addresses

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [Path Endpoint Addresses](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PathEndpointAddresses)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /api](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#apiGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.1.3 Dynamic Path Endpoint Addresses](#213-dynamic-path-endpoint-addresses)

## Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Event](Definitions.md#qiy-node-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#EventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3 Events](#3-events)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.5 Event](#55-event)

## Events Request

Specification | Reference
------------- | ---------
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /eventsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#eventsEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.6.1 Events Request](#261-events-request)

## Library

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Library](Definitions.md#service-library)
[Qiy Node API](Qiy%20Node%20API.json)         | [Library Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#LibraryModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.6 Library](#56-library)

## Library Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Details Request](Definitions.md#library-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /libraryEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.1 Library Details Request](#271-library-details-request)

## Library Service Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Service Details Request](Definitions.md#library-service-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /libraryServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryServiceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.2 Library Service Details Request](#272-library-service-details-request)

## Library Service Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Service Register Request](Definitions.md#library-service-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /libraryEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.3 Library Service Register Request](#273-library-service-register-request)

## Library Service Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Service Unregister Request](Definitions.md#library-service-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /libraryServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryServiceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.4 Library Service Unregister Request](#274-library-service-unregister-request)

## Library Service Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Service Update Request](Definitions.md#library-service-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /libraryServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryServiceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.5 Library Service Update Request](#275-library-service-update-request)

## Library Services Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Library Services Request](Definitions.md#library-services-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /libraryServicesEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryServicesEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.6 Library Services Request](#276-library-services-request)

## Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Message](Definitions.md#qiy-node-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#MessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4 Messages](#4-messages)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.7 Message](#57-message)

## Message Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Delete Request](Definitions.md#message-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /messageUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#messageUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.1 Message Delete Request](#281-message-delete-request)

## Message Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Details Request](Definitions.md#message-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /messageUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#messageUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.2 Message Details Request](#282-message-details-request)

## Message Post Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Post Request](Definitions.md#message-post-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#mboxUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.3 Message Post Request](#283-message-post-request)

## Message Received Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Message Received Event](Definitions.md#message-received-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Received Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#MessageReceivedEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.3.1 Message Received Event](#331-message-received-event)

## Messages Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Messages Request](Definitions.md#messages-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /mboxUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#mboxUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.8.4 Messages Request](#284-messages-request)

## Operation Execute Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Execute Request](Definitions.md#operation-execute-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /refEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#refEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.9.1 Operation Execute Request](#291-operation-execute-request)

## Operation Reference Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Message](Definitions.md#operation-reference-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Reference Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationReferenceMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.1 Operation Reference Message](#421-operation-reference-message)

## Operation Reference Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Request](Definitions.md#operation-reference-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.9.2 Operation Reference Request](#292-operation-reference-request)

## Operation Reference Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Reference Request Message](Definitions.md#operation-reference-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Reference Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationReferenceRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.2 Operation Reference Request Message](#422-operation-reference-request-message)

## Operation Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Register Request](Definitions.md#operation-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /refsEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#refsEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.9.3 Operation Register Request](#293-operation-register-request)

## Operation Specification

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Specification](Definitions.md#operation-specification)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Specification Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationSpecificationModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.8 Operation Specification](#58-operation-specification)

## Operation Specification Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Operation Specification Request Message](Definitions.md#operation-specification-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Operation Specification Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#OperationSpecificationRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.2.3 Operation Specification Request Message](#423-operation-specification-request-message)

## Persistent Id

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Persistent Id](Definitions.md#persistent-id)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.4.1 Persistent Id Event](#341-persistent-id-event)

## Persistent Id Event

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Persistent Id Event](Definitions.md#persistent-id-event)
[Qiy Node API](Qiy%20Node%20API.json)         | [Persistent Id Event Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PersistentIdEventModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [3.4.1 Persistent Id Event](#341-persistent-id-event)

## Portfolio

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                   | [Service Portfolio](Definitions.md#service-portfolio)
[Qiy Node API](Qiy%20Node%20API.json)           | [Portfolio Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PortfolioModel)
[Qiy Node Protocol](Qiy%20Node%20Protocoyyl.md) | [5.9 Portfolio](#59-portfolio)

## Portfolio Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Details Request](Definitions.md#portfolio-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /portfolioEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#portfolioEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.1 Portfolio Details Request](#2101-portfolio-details-request)

## Portfolio Service Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Service Details Request](Definitions.md#portfolio-service-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /portfolioServiceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#portfolioServiceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.2 Portfolio Service Details Request](#2102-portfolio-service-details-request)

## Portfolio Register Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Register Message](Definitions.md#portfolio-register-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Portfolio Register Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#PortfolioRegisterMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.3.1 Portfolio Register Message](#431-portfolio-register-message)

## Portfolio Services Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Portfolio Services Request](Definitions.md#portfolio-services-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /portfolioServicesEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#portfolioServicesEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.10.3 Portfolio Services Request](#2103-portfolio-services-request)

## Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service Provider](Definitions.md#service-provider)

## Provider Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Provider Details Request](Definitions.md#provider-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /providerUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#providerUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.7 Provider Details Request](#277-provider-details-request)

## Provider Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Provider Register Request](Definitions.md#provider-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /libraryEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#libraryEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.8 Provider Register Request](#278-provider-register-request)

## Provider Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Provider Unregister Request](Definitions.md#provider-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /providerUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#providerUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.9 Provider Unregister Request](#279-provider-unregister-request)

## Provider Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Provider Update Request](Definitions.md#provider-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /providerUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#providerUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.10 Provider Update Request](#2710-provider-update-request)

## Providers Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Providers Request](Definitions.md#providers-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /providersEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#providersEndpointGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.7.11 Providers Request](#2711-providers-request)

## Qiy Node

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node](Definitions.md#qiy-node)

## Qiy Node Create Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Create Request](Definitions.md#qiy-node-create-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /createEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#createEndpointPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.11.1 Qiy Node Create Request](#2111-qiy-node-create-request)

## Qiy Node Credentials

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Credentials](Definitions.md#qiy-node-credentials)
[Qiy Node API](Qiy%20Node%20API.json)         | [Qiy Node Credentials Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#QiyNodeCredentialsModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.10 Qiy Node Credentials](#510-qiy-node-credentials)

## Qiy Node Delete Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Delete Request](Definitions.md#qiy-node-delete-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /deleteEndpoint](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#deleteEndpointDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.11.2 Qiy Node Delete Request](#2112-qiy-node-delete-request)

## Qiy Node Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Qiy Node Message](Definitions.md#qiy-node-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#MessageModel)
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
[Definitions](Definitions.md) | [Relying Party](Definitions.md#relying-party)

## Service

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service](Definitions.md#service)

## Service Catalogue

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Catalogue](Definitions.md#service-catalogue)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Catalogue](#catalogue)

## Service Credentials Request Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Credentials Request Message](Definitions.md#service-credentials-request-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Service Credentials Request Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ServiceCredentialsRequestMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.4.1 Service Credentials Request Message](#441-service-credentials-request-message)

## Service Description

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Description](Definitions.md#service-description)
[Qiy Node API](Qiy%20Node%20API.json)         | [Service Description Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#ServiceDescriptionModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [5.11 Service Description](#511-service-description)

## Service Endpoint

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Service Endpoint](Definitions.md#service-endpoint)

## Service Portfolio

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Portfolio](Definitions.md#service-portfolio)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Portfolio](#portfolio)

## Service Provider

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Service Provider](Definitions.md#service-provider)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Provider](#provider)

## Source

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Data Source](Definitions.md#data-source)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [Source](#source)

## Source Candidates Message

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Candidates Message](Definitions.md#source-candidates-message)
[Qiy Node API](Qiy%20Node%20API.json)         | [Source Candidates Message Model](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#SourceCandidatesMessageModel)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [4.5.1 Source Candidates Message](#451-source-candidates-message)

## Source Candidates Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Candidates Request](Definitions.md#source-candidates-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /candidatesUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#candidatesUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.1 Source Candidates Request](#2121-source-candidates-request)

## Source Details Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Details Request](Definitions.md#source-details-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [GET /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#sourceUrlGet)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.2 Source Details Request](#2122-source-details-request)

## Source Register Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Register Request](Definitions.md#source-register-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [POST /consentUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#consentUrlPost)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.3 Source Register Request](#2123-source-register-request)

## Source Unregister Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Unregister Request](Definitions.md#source-unregister-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [DELETE /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#sourceUrlDelete)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.4 Source Unregister Request](#2124-source-unregister-request)

## Source Update Request

Specification | Reference
------------- | ---------
[Definitions](Definitions.md)                 | [Source Update Request](Definitions.md#source-update-request)
[Qiy Node API](Qiy%20Node%20API.json)         | [PATCH /sourceUrl](http://htmlpreview.github.io/?https://github.com/qiyfoundation/Qiy-Scheme/blob/topic/qiy-node-interface/Qiy%20Node%20API.html#sourceUrlPatch)
[Qiy Node Protocol](Qiy%20Node%20Protocol.md) | [2.12.5 Source Update Request](#2125-source-update-request)


## Transport Layer

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Transport Layer](Definitions.md#transport-layer)

## Transport Protocol

Specification | Reference
------------- | ---------
[Definitions](Definitions.md) | [Transport Protocol](Definitions.md#transport-protocol)



