##

# **Software Requirements Specification**

## for

# SafePort

**Version 1.0 approved**

**Prepared by** : _Eric Hoffman, Thomas Walsh, Dexter Oyewo, and Joe Wolke_

**Software Engineering Project 3 Team 2**

**March 27, 2019**

| **Table of Contents**         |
| --- |
| [**Revision History**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#revision-history)          |
| [**1.**        **Introduction**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#1-introduction)         |
| [1.1        Purpose](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#11-purpose)      |
| [1.2        Document Conventions](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#12-document-conventions)      |
| [1.3        Intended Audience and Reading Suggestions](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#13-intended-audience-and-reading-suggestions)      |
| [1.4        Product Scope](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#14-product-scope)      |
| [1.5        References](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#15-references)      |
| [**2.**        **Overall Description**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#2-overall-description)          |
| [2.1        Product Perspective](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#21-product-perspective)      |
| [2.2        Product Functions](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#22-product-functions)      |
| [2.3        User Classes and Characteristics](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#23-user-classes-and-characteristics)       |
| [2.4        Operating Environment](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#24-operating-environment)      |
| [2.5        Design and Implementation Constraints](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#25-design-and-implementation-constraints)      |
| [2.6        User Documentation](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#26-user-documentation)      |
| [2.7        Assumptions and Dependencies](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#27-assumptions-and-dependencies)      |
| [**3.**        **External Interface Requirements**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#3-external-interface-requirements)       |
| [3.1        User Interfaces](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#31-user-interfaces)      |
| [3.2        Hardware Interfaces](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#32-hardware-interfaces)      |
| [3.3        Software Interfaces](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#33-software-interfaces)      |
| [3.4        Communications Interfaces](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#34-communications-interfaces)      |
| [**4.**        **System Features**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#4-system-features)        |
| [4.1        TCP Self Port Scan](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#41-tcp-self-port-scan)      |
| [4.2        TCP Personal Server Port Scan](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#42-tcp-personal-server-port-scan)    |
| [**5.**        **Other Nonfunctional Requirements**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#5-other-nonfunctional-requirements)     |
| [5.1        Performance Requirements](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#51-performance-requirements)      |
| [5.2        Safety and Security Requirement](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#52-safety-and-security-requirements)      |
| [5.3        Software Quality Attributes](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#53-software-quality-attributes)      |
| [**Appendix A: Glossary**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#appendix-a-glossary)          |
| [**Appendix B: Analysis Models**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#appendix-b-analysis-models-and-mockups)          |
| [**Appendix C: To Be Determined List**](https://github.com/sharpnachos/comp330sp19p3/blob/master/SRD.md#appendix-c-to-be-determined-list)          |

# Revision History

| **Name** | **Date** | **Reason For Changes** | **Version** |
| --- | --- | --- | --- |
|   |   |   |   |
|   |   |   |   |

# 1. Introduction

  ## 1.1 Purpose

  The purpose of SafePort is to provide an accessible way for the ordinary person to test the security of their own devices. The system is a simplified version of a regular _port scanner_ like _Zenmap_ with a _GUI_ for easy user interaction. SafePort sends _TCP connection requests_ to its own _ports_ (via the user&#39;s personal _IP address_) and determines whether the device is at risk and recommends a course of action to better protect the device.

  ## 1.2 Document Conventions

  All italicized terms are defined in Appendix A.

  ## 1.3 Intended Audience and Reading Suggestions

  The intended audience for this project is exactly the kind of person that would NOT read this document. An extremely large population of people in today&#39;s society are mostly in the dark when it comes to modern technology. Because of their lack of experience in this field, they are highly susceptible to cyber-attacks.  Many people desire to know how to keep their devices safe, but they don&#39;t have the cybersecurity know-how to use a professional _port scanner_ like _Zenmap_. If they were to look at that interface (or this document), they would immediately see several terms they do not understand and give up. SafePort targets this lay audience with simplicity and a sleek design as a gateway into the subject.  Individuals reading this document should be other developers seeking to improve this product.  Additionally, the document should be read in the order that information is presented.

  ## 1.4 Product Scope

  SafePort is a software program that makes a computer send _TCP connection requests_ to itself - specifically to all its _ports._ The data received from doing this determines whether or not each _port_ is open. The purpose is to provide the average person an easy way to defend themselves against cyber-attacks. SafePort's main objective is having its interface be simple enough for the average person to understand and protect themselves.

  ## 1.5 References

  This document references the program ZenMap multiple times.  The application can be found here: [https://nmap.org/zenmap/](https://nmap.org/zenmap/)

# 2. Overall Description

  ## 2.1 Product Perspective

  This product could best be described as the abridged version of the existing product _Zenmap_ (and others like it). _Port scanning_ tools are currently available, but they are only accessible to cybersecurity and software development professionals who already understand the subject. The amount of options available in these products is not necessary for the average person, and the _UI_ is far from user-friendly. SafePort makes the process of network scanning much simpler.

  ## 2.2 Product Functions

  There are four main functions so far:
    
    ➔ Explain the concept of port scanning and why it is necessary
    ➔ Perform a port scan on the device and determine if there are ports at risk
    ➔ Return data regarding each port's activity and status
    ➔ Help the user secure their ports

  ## 2.3 User Classes and Characteristics

  The first class of users is the senior citizen community.  Older individuals are inexperienced with technology and thus are more vulnerable to attacks. SafePort helps these people by explaining the issue in simple terms, helping them in identifying problems in their system, and giving them the information and tools to fix it in a straightforward, palatable way.

  The second class of users is small businesses that have a website with relatively low traffic. A small website may not require an entire cybersecurity team but could benefit from a port scan. This product could scan their server and keep their business safe from hackers without needing to hire a software engineer to accomplish this.

  The last group of people in our audience is the average adult who does not identify as &quot;tech-savvy&quot; but is still interested in keeping their devices secure. This class is similar to the first class but has a wider age range.

  ## 2.4 Operating Environment

  SafePort is created in _Python 3_ and can be installed and run on the user&#39;s computer.  Python 3 allows SafePort to be run from any operating system.

  ## 2.5 Design and Implementation Constraints

  The main constraint for this product is that the audience for this software does not have much experience with software, so every step of using this product has to be simple and easy to follow. The options for the _port scan_ are severely limited as to simplify the process, and the _UI_ is extremely user friendly.

  ## 2.6 User Documentation

  A detailed markdown document is provided in GitHub as a README for developers wishing to run or edit the program.  There is additionally a user manual provided for users with easy-to-follow instructions on how to use the program and how it works.

  ## 2.7 Assumptions and Dependencies

  The main assumption made with this project is that _Python_ has a robust enough _GUI_ implementation to create a good enough looking design for the interface of our product.  If this is not the case, then our team will have to look into third-party components to meet expectations for the graphic design.

# 3. External Interface Requirements

  ## 3.1 User Interfaces

  The SafePort application opens up to a home screen prompting the user to scan their network by clicking a button.  Once they click this, they are then led to the &#39;Scan&#39; page with the results of their scan.  All page links are held by a navigation bar at the top of the application.  The &#39;Scan&#39; page will continue to hold the results of the most recent scan.  Once the results of the scan are displayed, the user is prompted to fix any issues that the scan has found.  The &#39;Tools&#39; page also has options for the user to scan or fix their network.  The &#39;Profile&#39; page contains network information and logs from previous scans and fixes.  Finally, the &#39;Help&#39; page contains a short tutorial for the user if they have any troubles navigating the program and an additional link to the user manual for further inquiries.  For visualization of these features, please see mockups displayed in Appendix B.

  ## 3.2 Hardware Interfaces

  Through the use of Python 3, SafePort is able to run on any operating system.

  ## 3.3 Software Interfaces

  As stated previously, SafePort is able to run on any operating system. All that is required is the latest version of _Python 3_ and its libraries.

  ## 3.4 Communications Interfaces

  TBD - As of now, no communication interface is planned for this project.

# 4. System Features

  ## 4.1 TCP Self Port Scan

  ### 4.1.1        Description and Priority

  The program creates a _socket_ which sends a connection request to the _host&#39;s port_. If the _port_ is open and available for connections, it responds to the request with an acknowledgement that is it open and ready to receive a connection. The scanner then returns information on the _host&#39;s port_ status, as well as services, versions and operating systems being ran on that _port_.

  ### 4.1.2        Stimulus/Response Sequences

  SafePort does as much as possible to minimize the user actions required to start the _port_ scan; since this is the main function of the product, it is easy to do, and it is the first thing to appeaer on the screen.

  ### 4.1.3        Functional Requirements

    REQ-1:        Send TCP requests to all ports
    REQ-2:        Compile information on all ports that don't respond with "closed"
    REQ-3:        Report findings to the user
    REQ-4:        Provide specific information as to the safety concerns of each open port

  ## 4.2 TCP Personal Server Port Scan

  ### 4.2.1 Description and Priority

  The program creates a _socket_ which sends a connection request to a _host&#39;s ports_ determined by the _IP address_ inputted by the user. If the _port_ is open and available for connections, it responds to the request with an acknowledgement that is it open and ready to receive a connection. The scanner then returns information on the _host&#39;s port_ status, as well as services, versions and operating systems being ran on that _port._

  ### 4.2.2 Stimulus/Response Sequences

  SafePort has an advanced settings option in which the user can input an _IP address_ for a device they own and run the scan against that. This requires only an extra text box below the regular scan button.

  ### 4.2.3 Functional Requirements

    REQ-1:        Send TCP requests to all ports
    REQ-2:        Compile information on all ports that don't respond with "closed"
    REQ-3:        Report findings to the user
    REQ-4:        Provide specific information as to the safety concerns of each open port

# 5. Other Nonfunctional Requirements

  ## 5.1 Performance Requirements

  Scans need to take less than a minute to execute and preferably less than 30 seconds.

  ## 5.2 Safety and Security Requirements

  There must be a disclaimer provided to inform the user that if they do not own the device they intend to scan they must have permission under penalty of law. We must assert that we are not liable for the misuse of our product.

  ## 5.3 Software Quality Attributes

  This application is accessible from a user interface after being installed on the user&#39;s computer.  Accessibility for inexperienced users is key for this project.  Reliability is, of course, important as well since an improper port scan can lead to missed security vulnerabilities.  Additionally, maintainability is essential for development in order to be able to properly update SafePort as any bugs arise.

# Appendix A: Glossary

**Port Scanner** : An application designed to probe a server/host for open ports

**GUI** : Graphical user interface

**TCP Connection Requests** : Transmission control protocol, enables two hosts to establish a connection and exchange data.

**Ports** : A specific place for being connected to another device

**ZenMap** : Official cross-platform GUI for the Nmap security scanner

**UI** : User Interface

**Python 3:** A high-level general purpose programming language

**Software Interfaces** : Languages, codes, and messages used by programs to communicate with hardware

**Socket** : One endpoint of a two-way communication link between two programs running on the network.

**Host** : A computer or other device connected to a computer network

**Functional Requirements** : Requirement related directly to the functionality to the system

**Nonfunctional Requirements:** define system attributes such as security, reliability, performance, usability, and maintainability

**IP Address:** A unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a 
network.

# Appendix B: Analysis Models and Mockups

[Mockups can be found here](https://docs.google.com/document/d/1Zn_2dSaHNwxe3lKChSdKnZZRicK7E9dXedQssxHZNiA/edit?usp=sharing)

# Appendix C: To Be Determined List

1. Communications Interface not planned yet for this project but could potentially be added later on depending on where this project goes.
