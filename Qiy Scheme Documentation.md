# Qiy Scheme Documentation

## Abstract
The [Qiy Scheme](Definitions.md#qiy-scheme) defines a framework for individual users, companies and governmental organisations to safely control and exchange personal data. This document describes the development process of the [Qiy Scheme](Definitions.md#qiy-scheme) documents.

# 1 Development process
The development process starts at the level of Work Streams. Everyone is free to contribute their suggestions to the Work Streams.The process ends by an instruction of the [Executive Board](Definitions.md#executive-board) to merge new elements with the existing version of the [Qiy Scheme](Definitions.md#qiy-scheme).

## 1.2 Parties fulfilling a role in the process

### 1.2.1 Contributor
Any individual person who wishes to do so can make suggestions for the further development of the [Qiy Scheme](Definitions.md#qiy-scheme) by sending a pull request. The GitHub Terms of Service apply, notably Section D thereof dealing with User-Generated Content. However, Contributors of possibly copyrighted materials must first sign a Contributor License Agreement. And, in the case where an individual is an employee in a country where intellectual property created by employees automatically becomes the property of the employer, this person will need to sign in advance a Contributor License Agreement for individuals with an employment relationship and to submit a signed Employer's Declaration by which the employer grants the [Qiy Foundation](Definitions.md#qiy-foundation) an irrevocable license to use that intellectual property, as set out in the said Contributor License Agreement.

### 1.2.2 Work Stream
Work Streams provide a forum for discussion and have as their main tasks the preparation of relevant work programmes and to contribute to the further development of the [Qiy Scheme](Definitions.md#qiy-scheme). A Work Stream is the primary decision making centre for all matters that fall within its Terms of Reference.

It is the responsibility of the [Executive Board](Definitions.md#executive-board) of the [Qiy Foundation](Definitions.md#qiy-foundation) to create or dissolve a Work Stream and to approve its Terms of Reference.

A Work Stream prepares drafts concerning the management, further development and maintenance of the [Qiy Scheme](Definitions.md#qiy-scheme) for consideration by the [Executive Board](Definitions.md#executive-board).

A Work Stream may establish working groups, if required. When this is the case, the Work Stream shall decide on the rules for the working group, within the scope of the [Qiy Foundation](Definitions.md#qiy-foundation)'s Rules & Regulations and the Work Stream Procedures.

Participation in a Work Stream or working group is by invitation by the Chairperson only. Non-Members with a special expertise may be invited to participate in working groups or even in a Work Stream. Where deemed necessary by the Chairperson of a Work Stream, participants in Work Streams or working groups will be asked to sign a Mutual Confidentiality and Non-Disclosure Agreement with the [Qiy Foundation](Definitions.md#qiy-foundation).

Counselors of the [Qiy Foundation](Definitions.md#qiy-foundation) may attend meetings of a Work Stream and participate in the work without the right to vote.

The Chairpersons of each Work Stream ensure that all pull requests suggested by Contributors are reviewed in the Work Stream.

The Work Stream Procedures adopted by the [Executive Board](Definitions.md#executive-board) of the [Qiy Foundation](Definitions.md#qiy-foundation) apply.

### 1.2.3 Review Board
It is the task of the [Review Board](Definitions.md#review-board) to review the work of the different Work Streams and to seek the advice of both the [User Voice](Definitions.md#user-voice) and the [Council of Regional Authorities](Definitions.md#council-of-regional-authorities). Where necessary, the [Review Board](Definitions.md#review-board) will ask the Work Stream to reconsider their proposals in the light of the advice received. The procedural rules for the adoption of Work Stream pull requests apply.

Members of the [Review Board](Definitions.md#review-board) are nominated by the [Executive Board](Definitions.md#executive-board) of the [Qiy Foundation](Definitions.md#qiy-foundation), but selected and appointed by the [Executive Board](Definitions.md#executive-board). The Rules on the Selection and Appointment of members of the [Review Board](Definitions.md#review-board) apply.

### 1.2.4 User Voice
The [User Voice](Definitions.md#user-voice) is an advisory panel of the [Qiy Foundation](Definitions.md#qiy-foundation). Its members represent the interests of the different user groups of the [Qiy Scheme](Definitions.md#qiy-scheme). Its role is to advise the [Executive Board](Definitions.md#executive-board) on proposals made by Work Streams.

The Rules on the Selection and Appointment of members of the [User Voice](Definitions.md#user-voice) apply.

### 1.2.5 Council of Regional Authorities
The [Council of Regional Authorities](Definitions.md#council-of-regional-authorities) consists of representatives of the [Regional Authorities](Definitions.md#regional-authority). Its members represent the interests of the [Regional Authorities](Definitions.md#regional-authority). Its role is to advise the [Executive Board](Definitions.md#executive-board) on proposals made by Work Streams.

The Rules on the Selection and Appointment of members of the [Council of Regional Authorities](Definitions.md#council-of-regional-authorities) apply.

### 1.2.6 Executive Board
The [Executive Board](Definitions.md#executive-board) is responsible for the management, further development and maintenance of the [Qiy Scheme](Definitions.md#qiy-scheme). Once it has accepted a new deliverable for the [Qiy Scheme](Definitions.md#qiy-scheme), it shall instruct the [Review Board](Definitions.md#review-board) to merge the deliverable with the existing version of the [Qiy Scheme](Definitions.md#qiy-scheme). It will also assign a version number to each new deliverable, for more information see [Qiy Scheme Releases](Qiy%20Scheme%20Releases.md).

The Rules on the Selection and Appointment of members of the [Executive Board](Definitions.md#executive-board) apply.


## 2 Process

![Qiy Scheme documentation process](./images/qiy-scheme-documentation.png)

Contributors can create pull requests at any time. All pull requests will be reviewed by the Work Stream that is most relevant to the pull request in question. The Chairperson of a Work Streams will decide which of the pull requests is relevant to their work.

The deliberations in a Work Stream result in a review request made to the [Review Board](Definitions.md#review-board). The [Review Board](Definitions.md#review-board) will consider the review requests made by the different Work Streams in conjunction with each other. It will also verify whether all pull requests made by Contributors have been reviewed by the relevant Work Streams. The next step is that the [Review Board](Definitions.md#review-board) initiates a review in conjunction with the [User Voice](Definitions.md#user-voice) and the [Council of Regional Authorities](Definitions.md#council-of-regional-authorities). If necessary the [Review Board](Definitions.md#review-board) can request changes to the pull request. If no changes are requested the [Review Board](Definitions.md#review-board) will request the [Executive Board](Definitions.md#executive-board) for approval. Once approved, the [Review Board](Definitions.md#review-board) will merge the pull request.


# Annex Diagram source code
```
title Qiy Scheme Documentation

Contributor -> Work Stream: Pull request
Work Stream -> Work Stream: Review
Work Stream -> Review Board: 
note over Review Board, User Voice, Council: Review
Review Board -> Executive Board:
Executive Board -> Review Board:
Review Board -> Review Board: Merge
```
