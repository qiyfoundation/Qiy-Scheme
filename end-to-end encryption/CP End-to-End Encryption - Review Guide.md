# Change Proposal 'End-to-End Encryption'
## Review Guide

# Abstract

On Thursday June 6th 2019 the Qiy Scheme Work Stream Functionality & Technology (QSWS-F&T) presented a change proposal (CP) entitled 'End-to-End Encryption' for review.
This document provides guidance for those who are willing to do or are interested in this.

freek.driesenaar@qiyfoundation.org

# Contents

1. [Introduction](#introduction)
1. [Presentation](#presentation)
1. [Collaboration](#collaboration)
1. [Qiy Scheme](#qiy-scheme)
1. [fiKks](#fiKks)
1. [Digital Me](#digital-me)
1. [Next steps](#next-steps)


# Introduction

The Qiy Scheme currently supports the secure end-to-end exchange between organisations (Service Providers) of unencrypted Personal Data.
This is perfectly fine for use cases as used by fiKks in which a backoffice enriches the data.
However, in use cases where a user application such as the Financial Passport App enriches the data, exchanging the data encryptedly reduces the privacy risks at the backoffice.

During the Work Stream session the following solution was presented:
* Service Providers can agree on encryption methods.
* The Qiy Scheme will enable the implementation of these.

An example was also given during the presentation.


# Presentation

The presentation that was used during the Working Stream session is publicly available on github, see: [QS WSFT Meeting 2019-06-06.pptx](QS%20WSFT%20Meeting%202019-06-06.pptx)


# Collaboration

This CP is a collaborative effort of the following organisations:
* the Qiy Foundation: as the keeper of the Qiy Scheme.
* fiKks: as a community of organisations joining forces for the poor.
* Digital Me: as a Qiy Access Provider and driver of the Qiy Trust Network.


# Qiy Scheme

The implication for the Qiy Scheme is purely technical:
* The Qiy Node Interface will be enhanced with dedicated request parameters enabling Service Providers to implement schemes like the ones envisioned in this CP.

The QSWS-F&T uses the branch [Topic/Free Parameters](https://github.com/qiyfoundation/Qiy-Scheme/tree/topic/free-parameters) to further this enhancement.


# fiKks

The fiKks community is introducing end-to-end encryption in their standards.
Please refer to [fiKks on Github](https://github.com/qiyfoundation/fiKks) for more information.


# Digital Me

Digital Me has been found willing to support the development and implementation of end-2-end encryption.
Digital Me provides a Qiy Node Implementation in a DTAP, the API of which can be found here: [DM Qiy Node API](https://qiy.api.digital-me.nl/?version=latest)

The api has dedicated a section for this topic, see the ['End-to-end encryption (draft)' folder](https://qiy.api.digital-me.nl/?version=latest#2873317f-816b-4ba9-9492-fd8515881fd8).


# Next steps

Please feel free to study the drafts and provide your review comments, for example via e-mail or pull requests, and join the committing meeting during our [August Work Stream session](https://www.qiyfoundation.org/nl/qiynotes-live-signup/).


# Questions

Please contact freek.driesenaar@qiyfoundation.org for your questions.

