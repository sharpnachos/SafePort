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
| **Revision History**         **3** |
| **1.**        **Introduction**        **4** |
| 1.1        Purpose     4 |
| 1.2        Document Conventions     4 |
| 1.3        Intended Audience and Reading Suggestions     4 |
| 1.4        Product Scope     4 |
| 1.5        References     4 |
| **2.**        **Overall Description**         **5** |
| 2.1        Product Perspective     5 |
| 2.2        Product Functions     5 |
| 2.3        User Classes and Characteristics      5 |
| 2.4        Operating Environment     5 |
| 2.5        Design and Implementation Constraints     6 |
| 2.6        User Documentation     6 |
| 2.7        Assumptions and Dependencies     6 |
| **3.**        **External Interface Requirements**      **6** |
| 3.1        User Interfaces     6 |
| 3.2        Hardware Interfaces     6 |
| 3.3        Software Interfaces     7 |
| 3.4        Communications Interfaces     7 |
| **4.**        **System Features**       **7** |
| 4.1        TCP Self Port Scan     7 |
| 4.2        TCP Personal Server Port Scan   8 |
| **5.**        **Other Nonfunctional Requirements**    **8** |
| 5.1        Performance Requirements     8 |
| 5.2        Safety and Security Requirement     8 |
| 5.3        Software Quality Attributes     8 |
| **6.**        **Other Requirements**         **9** |
| **Appendix A: Glossary**         **9** |
| **Appendix B: Analysis Models**         **9** |
| **Appendix C: To Be Determined List**         **11** |

**Revision History**

| **Name** | **Date** | **Reason For Changes** | **Version** |
| --- | --- | --- | --- |
|   |   |   |   |
|   |   |   |   |

**1.** **Introduction**

  **1.1** **Purpose**

  The purpose of SafePort is to provide an accessible way for the ordinary person to test the security of their own devices. The system will be a simplified version of a regular _port scanner_ like _Zenmap_ with a _GUI_ for easy user interaction. SafePort will then send _TCP connection requests_ to its own _ports_ (via the user&#39;s personal _IP address_) and then will determine whether the device is at risk and recommend a course of action to better protect the device.

  **1.2** **Document Conventions**

  All italicized terms are defined in Appendix A.

  **1.3** **Intended Audience and Reading Suggestions**

  The intended audience for this project is exactly the kind of person that would NOT read this document. An extremely large population of people in today&#39;s society are mostly in the dark when it comes to modern technology. Because of their lack of experience in this field, they are highly susceptible to cyber-attacks.  Many people desire to know how to keep their devices safe, but they don&#39;t have the cybersecurity know-how to use a professional _port scanner_ like _Zenmap_. If they were to look at that interface (or this document), they would immediately see several terms they do not understand and give up. Our team intends to capture this lay audience with simplicity and a sleek design as a gateway into the subject.  Individuals reading this document should be other developers seeking to improve this product.  Additionally, the document should be read in the order that information is presented.

  **1.4** **Product Scope**

  We are essentially making a software program that makes a computer send _TCP connection requests_ to itself - specifically to all its _ports._ The data received from doing this will determine whether or not each _port_ is open. The purpose is to provide the average person an easy way to defend themselves against cyber-attacks. Our main objective is to make our scanner&#39;s interface simple enough so the average person can understand and protect themselves.

  **1.5** **References**

  This document references the program ZenMap multiple times.  The application can be found here: [https://nmap.org/zenmap/](https://nmap.org/zenmap/)

**2.** **Overall Description**

  **2.1** **Product Perspective**

  This product could best be described as the abridged version of the existing product _Zenmap_ (and others like it). _Port scanning_ tools are currently available, but they are only accessible to cybersecurity and software development professionals who already understand the subject. The amount of options available in these products is not necessary for the average person, and the _UI_ is far from user-friendly. We intend to make the process of network scanning much simpler.

  **2.2** **Product Functions**

  There are four main functions so far:
    
    ➔Explain the concept of port scanning and why it is necessary
    ➔Perform a port scan on the device and determine if there are ports at risk
    ➔Return data regarding each port's activity and status
    ➔Help the user secure their ports

  **2.3** **User Classes and Characteristics**

  The first class of users is the senior citizen community.  Older individuals are inexperienced with technology and thus are more vulnerable to attacks. This product will help these people by explaining the issue in simple terms, helping them in identifying problems in their system, and giving them the information and tools to fix it in a straightforward, palatable way.

  The second class of users is small businesses that have a website with relatively low traffic. A small website may not require an entire cybersecurity team but could benefit from a port scan. This product could scan their server and keep their business safe from hackers, and the business does not need to hire a software engineer to accomplish this.

  The last group of people in our audience is the average adult that does not identify as &quot;tech-savvy&quot; but is still interested in keeping their devices secure. This class is similar to the first class but has a wider age range.

  **2.4** **Operating Environment**

  Our goal is to create our program in _Python 3_ and then allow it to be installed and run on the user&#39;s computer.  Python 3 will allow us to run SafePort from any operating system.

  **2.5** **Design and Implementation Constraints**

  The main constraint for this product is that the audience for this software does not have much experience with software, so every step of using this product has to be simple and easy to follow. The options for the _port scan_ will be severely limited as to simplify the process and the _UI_ needs to be extremely user friendly. Also, we face the constraint of inexperience as a software development team as we are not professionals.

  **2.6** **User Documentation**

  A detailed markdown document will be provided in GitHub as a README for developers wishing to run or edit the program.  There will additionally be a user manual provided for users with easy-to-follow instructions on how to use the program and how it works.

  **2.7** **Assumptions and Dependencies**

  The main assumption we are making with this project is that _Python_ will have a robust enough _GUI_ implementation to create a good enough looking design for the interface of our product.  If this is not the case, then we will have to look into third-party components to meet expectations for the graphic design.

**3.** **External Interface Requirements**

  **3.1** **User Interfaces**

  The SafePort application will open up to a home screen prompting the user to scan their network by clicking a button.  Once they click this, they will be led to the &#39;Scan&#39; page with the results of their scan.  All page links will be held by a navigation bar at the top of the application.  The &#39;Scan&#39; page will continue to hold the results of the most recent scan.  Once the results of the scan are displayed, the user will be prompted to fix any issues that the scan has found.  The &#39;Tools&#39; page will also have options for the user to scan or fix their network.  The &#39;Profile&#39; page will contain network information and logs from previous scans and fixes.  Finally, the &#39;Help&#39; page will contain a short tutorial for the user if they have any troubles navigating the program and an additional link to the user manual for further inquiries.  For visualization of these features, please see mockups displayed in Appendix B.

  **3.2** **Hardware Interfaces**

  Our goal is to have the application be able to run any operating system, and this to doable with Python 3.

  **3.3** **Software Interfaces**

  SafePort will be able to run on any operating system. All that is required is the latest version of _Python 3_ and its libraries.

  **1.4** **Communications Interfaces**

  TBD - As of now, no communication interface is planned for this project.

**4.** **System Features**

  **4.1** **TCP Self Port Scan**

  4.1.1        Description and Priority

  The program creates a _socket_ which sends a connection request to the _host&#39;s port_. If the _port_ is open and available for connections, it will respond to the request with an acknowledgement that is it open and ready to receive a connection. The scanner will return information on the _host&#39;s port_ status, as well as services, versions and operating systems being ran on that _port_.

  4.1.2        Stimulus/Response Sequences

  We will do as much as possible to minimize the user actions required to start the _port_ scan, since this is the main function of the product it will be easy to do, and the first thing to pop up.

  4.1.3        Functional Requirements

    REQ-1:        Send TCP requests to all ports
    REQ-2:        Compile information on all ports that don't respond with "closed"
    REQ-3:        Report findings to the user
    REQ-4:        Provide specific information as to the safety concerns of each open port

  **4.2** **TCP Personal Server Port Scan**

  4.2.1 Description and Priority

  The program creates a _socket_ which sends a connection request to a _host&#39;s ports_ determined by the _IP address_ inputted by the user. If the _port_ is open and available for connections, it will respond to the request with an acknowledgement that is it open and ready to receive a connection. The scanner will return information on the _host&#39;s port_ status, as well as services, versions and operating systems being ran on that _port._

  4.2.2 Stimulus/Response Sequences

  We will create an advanced settings option in which the user can input an _IP address_ for a device they own and run the scan against that. This will only require an extra text box below the regular button

  4.2.3 Functional Requirements

    REQ-1:        Send TCP requests to all ports
    REQ-2:        Compile information on all ports that don't respond with "closed"
    REQ-3:        Report findings to the user
    REQ-4:        Provide specific information as to the safety concerns of each open port

**5.** **Other Nonfunctional Requirements**

  **5.1** **Performance Requirements**

  Scans need to take less than a minute and preferably less than 30 seconds. This should be pretty easy to achieve.

  **5.2** **Safety and Security Requirements**

  There must be a disclaimer provided to inform the user that if they do not own the device they intend to scan they must have permission under penalty of law. We must assert that we are not liable for the misuse of our product.

  **5.3** **Software Quality Attributes**

  This application will be accessible from a user interface after being installed on the user&#39;s computer.  Accessibility for inexperienced users is key for this project.  Reliability will of course be important as well since an improper port scan can lead to missed security vulnerabilities.  Additionally, maintainability will be essential for development in order to be able to properly update SafePort as any bugs arise.

**Appendix A: Glossary**

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

**IP Address:** A unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network.

**Appendix B: Analysis Models and Mockups**

[Mockups can be found here](https://docs.google.com/document/d/1Zn_2dSaHNwxe3lKChSdKnZZRicK7E9dXedQssxHZNiA/edit?usp=sharing)

**Appendix C: To Be Determined List**

1. Communications Interface not planned yet for this project but could potentially be added later on depending on where this project goes.
