## Definitions:

**Asset:** anything of value, when lost would cause economic loss

**Vulnerability:** weakness in the assets that when exploited will lead to economic loss

**Threat:** anything that can exploit a vulnerability

**Risk:** the probable frequency and magnitude

**Threat Actor:** Person, group, etc responsible

**Threat Action:** what was caused or done

**Control:** preventative, detective or corrective

**Non-repudiation:** stops a subject from claiming an event or action did not occur

**Key Encryptions:**

- Requires:
    - Sender to use receivers public key to encrypt, uses senders private key to sign the message
    - Receiver to use their private key to decrypt, checks senders identity by using the senders public key

**CIA:**

- Confidentiality
    - Information security, company or individual
    - Access Controls, Encryption, Governance
- Integrity
    - Protects reliability and correctness of data, prevents unauthorised alterations of data, protection against error
- Availability
    - Authorised subjects get timely and uninterrupted access to objects, Mitigation
- Also extended to include:
    - Authentication
        - Something you know, you have or something you are/do, somewhere you are, content-aware auth
    - Authorisation
        - Determines what actions subject can carry out on an object
    - Accountability
        - Identify all relevant information regarding actions in a system
    - Non-Repudiation
    - Reliability

**Control Types:**

- Physical
- Technical
- Administrative

**Control Functions:**

- Preventative, Detective, Corrective

![[Pasted image 20231107142332.png]]

**Rules, ABAC, MAC:**

- Rule-based access control:
    - Firewalls
        - Apply a set of rules to incoming and outgoing network traffic
    - Cloud service object storage also uses policies to grant access
- Attribute Based Access Control (ABAC):
    - Restrict access based on MAC or time of day
    - Allow access from mobile devices, etc
- Mandatory Access Control (MAC):
    - Access is granted based on labels assigned to the user and object

**IP Addresses:**

- Combination of a network address and host address
- Computers can directly communicate with each other on a subnetwork without going through a router
- Everything running in a home exists on a subnetwork that is connected to the internet via a router

**Threat:**

- Anything that can exploit a vulnerability in a way that leads to a negative impact
- Threat Actor: Person, etc responsible for threats
    - Internal or external
- Threat Action: What the threat actor did

**Common Vulnerabilities:**

- Sniffing
    - Passive attack that reads all data sent over a network.
    - Protected via encryption
    - Secure socket layer, transport layer security protocols (SSL/TLS)
- Spoofing
    - Altering the network level of TCP/IP to alter who the sender appears to be
- Denial of Service (DoS)
    - Flood fake requests to stall server
- Distributed Denial of Service (DDoS)
    - Using many machines in a DoS attack
- Man-in-the-Middle Attack
    - Using spoofing to pretend to be the other individual between conversations
- Hacking
    - Initial access and lateral movement using vulnerability to gain remote access and then using that machine to pivot other machines
- Remote Shell
    - Attack that runs a shell script or command on another machine
    - Forward Shell: client runs commands and hacks a server
    - Reverse Shell: server runs commands on a clients device
- SQLi

**Malware:**

- Any malicious software, script or code that is run on a device that alters its state or function without the owner’s informed consent.
    - Virus: infects files and spreads when files are copied to new hosts
    - Remote Access Trojan: software that disguises itself as something normal or innocuous
    - Spyware: software that performs key-logging, reading messages, emails, etc
    - Worm: malware that propagates itself through the network
    - Adware: usually browser based software that displays ads
    - Scareware: displays threatening messages to the user
    - Bot: under the control of a command and control centre
    - Ransomware: encrypts files and demands payment to unencrypt
    - Cryptominer: uses computer resources to mine cryptocurrency
- Can be detected by:
    - Static Analysis (checking signatures)
    - Dynamic or behaviour analysis
- Avoids using:
    - Code obfuscation
        - Encryption
        - Polymorphism
        - Metamorphic

**Social:**

- Employ deception, manipulation, intimidation, etc
- Baiting
- Bribery/Solicitation
- Elicitation (through conversation)
- Extortion/Blackmail
- Forgery
- Influence
- Scam
- Phishing
    - Pretend to be someone/something else
    - Spearphishing = targeted at a specific victim
    - Whalephishing = target of high value (CEO etc)
    - Voice-phishing/vishing
- Pretexting
- Propaganda
- Spam
- Social Engineering WORKS, people:
    - Want to help
    - Trust people
    - Concerned about getting in trouble
    - Willing to cut corners
    - Willing to believe in good fortune
    - Don't understand how tech works

**Australian Signals Directorate (ASD) Essential Eight:**

- Application control prevent the execution of unapproved/malicious programs
- Configure Microsoft Office macro settings
- Restrict administrative privileges
- Multi-factor authentication
- Daily backups
- Patching applications
- Application hardening
- Patch operating systems

**Application Control**

- Vulnerability
    - Windows has a variety of scripting languages that can be used for malicious
- Controls
    - General users should be prevented from running scripts

**Intrusion Detection Systems**

- IDS can be network or host based
- Like anti-malware, uses knowledge-based and behavioural-based approaches to detection

**Honeypots**

- A system put on the network to lure attackers to attack it and not the real network
- Monitors attempts at probing and attacking

**Security Requirements from 3 Sources:**

- information security risks based on the organisations business
- legal, statutory, regulatory and contractual obligations
- principles, objectives and business requirements for information processing that an organisation has developed to support its operations

**Assessing risk:**

- qualitative
    - focus groups, surveys
    - can help communicate risks but cannot be used to prioritise which risk to handle first
- quantitative
    - asset valuation, exposure factor, single loss expectancy, cost/benefit etc.

**Controls:**

- Types
    - Physical
        - CCTV, lock systems, swipe cards
    - Technical
        - encryption, firewalls
    - Administrative
        - policies, procedures, hiring, training
- Functions
    - Preventative
        - fences, warnings, alarms
    - Detective
        - audit trails, logging, CCTV, honeypots
    - Corrective

**Security operations**

- need to know and least privilege
- separation of duties and responsibilities
- two-person control
- privileged account management
- change management
- personnel security
- information management lifecycle
- hardware and software

**Attack Tree:**

- Root node: describes the goal
- Child node: represents a sub goal or an attack step for overall goal
- leaf node: refers to an attack step and has not child node

**Attack Modelling:**

- a structured approach to creating a security model of a given system
- used to identify, assess and prioritise partial threats to an organisations information systems
- two methodologies:
    - DREAD
        - used for a specific threat
        - damage potential, reproducibility, exploitability, affected users, discoverability
    - STRIDE
        - used to identify and categorise all threats, then use DREAD
        - spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege
- probability of occurrence
- potential impact
- ease of mitigation
- compliance requirements

**Incident**: any event that has compromised the CIA of an organisation’s assets

**Handling an incident:**

- Prep
- Detection & Analysis
- Containment, Eradication & Recovery
- Post-incident

**CALDERA:**

- Developed to simulate and replicate real cyber scenarios, implemented by the following stages: (using a red-team and blue-team in a cyber-range)
- Adversary:
    - A profile of instructions that describe TTPs (tactics, techniques and procedures) to be performed on the targeted system
- Agent:
    - works as a spy program, executes adversary programs
- Ability:
    - an attack step in an attack
- Operation:
    - creates an adversary profile and executes via the agent
- There is also ADT (attack-defense tree tool) to model scenarios

**Locard’s Exchange Principle:**

- physical contact between objects leaves exchanges in matter, leaving traces.
- digital contact leaves traces

**Daubert Standard for scientific evidence:**

- theoretical underpinnings must yield testable predictions by means of which the theory could be falsified
- the methods should preferable be published peer-reviewed
- known rate of error
- generally accepted within the relevant scientific community

**UK Law Commision:**

- no action taken by law enforcement should change data used in court
- people collecting data should be competent
- an audit trail should be kept
- someone in charge to ensure the law and these principles are met

**State-centric:** snapshot of current system

**History-centric:** time-stamped events

**Process:**

- Collection
    - maintain integrity
    - possible sources
    - may be encrypted, deleted, tampered with
    - copy physically and reconstruct
    - value? volatility? verified?
- Examination
    - use of tools
    - recover files and information
- Analysis:
    - attribution
    - alibis and statements
    - intent
    - timeline, locations, activities, network data
    - Steganography: covered writing, concealing data in another medium
        - hidden by alignment, font, position, white space

**CI** = Critical Infrastructure:

- Physical facilities, supply chains. IT and communication networks that if destroyed or degraded, would significantly impact the social or economic wellbeing of the nation
- OT = operational technology, used to manage operations
- ICS = industrial control systems, manage monitor and control systems
    - continuous
    - discrete

**CPS** = cyber-physical systems: systems to interfere with and control the environment

**In Australia:**

- Cybercrime
    - crimes directed at computers or other ICTs, state and federal acts
        - hacking, fishing, malware, identity theft, etc
- Privacy and data breaches
- critical infrastructure legislation
- national security legislation
    - metadata retention
        - companies required to retain data for at least 2 years
        - access to 22 different agencies
    - assistance and access
        - government is allowed to break encryption
    - security agencies
- international laws, treaties and guides
    - GDPR
        - general data protection regulation (Europe)
    - convention and cybercrime
    - tallinn manual 2.0
        - cyber war

**Artificial Intelligence**

Adversarial Attack

- invisible/visible change that causes ai to misidentify it
- One-pixel, physical, adversarial patch
- To mitigate: train on adversarial inputs, model input constraints, more robust algorithms

Deep-Fake

- Applying ones likeness to create falsified content

**Commands Dictionary:**

sudo docker run -it --rm uwacyber/cits1003-labs:bash

- Open docker

pwd

- Shows us what directory we are in

ls -al

- Lists the contents of the current directory

cd /”directory”

- Change directory

DIRECTORIES:

**/bin** contains user binary executables like ps, ls, ping, grep etc. it is a symbolic link to **/usr/bin**

**/sbin** contains system binaries like iptables, reboot, fdisk, ifconfig, etc.

**/etc** contains configuration files and scripts for services running on the system. Also contains the passwd and shadow files that contain user and password information.

**/dev** contains device files that are the interface with physical devices on, or attached to, the system such as tty devices /dev/tty1.

**/proc** contains files that store information about system processes like uptime for example.

**/var** contains files like logs (/var/logs), backups (/var/backups), mail (/var/mail) and spool (printing; /var/spool). There is also a /var/tmp directory that can be used to run programs out of. This directory does survive reboots however. The directory /var/www/html is often used as the root directory of the web server.

**/tmp** contains temporary files as mentioned previously. Files get deleted on reboot.

**/usr** contains user binaries, libraries, documentation and source code

**/usr/local** contains users programs that you install from source.

**/home** contains user home directories

**/boot** contains boot loader files

**/lib** contains system libraries

**/opt** contains optional add-on applications

**/mnt** is a location for mounting temporary filesystems

**/media** is a location for mounting removable media devices like CDs

**/srv** contains specific service related data

touch file.txt

- Create file

cp file.txt file2.txt

- Copy

rm file.txt

- Remove file

cat file.txt

- Read whats in the file

wget “URL”

- Download

unzip file.txt

- Unzips

ps -AF

- Shows all processes and extended info

whoami

- Currently logged in user

chmod u+x file.txt

- Allow access to current user

ip addr

- List ip addresses

nmap -sn 172.17.0.0/24

- Perform a ping scan

nmap -sC - sV 172.17.0.1-3

- Discover what services are running on a machine

ssh 172.17.0.3/2222

- Connect to the service

find ~/ -name ‘host*’\

- Find all files that starts with the string host
- rwx rw-r—
- means regular file
- rwx first means owner has read, write and execute permissions
- rw second means the access for the group the file belongs to, only read and write
- r— last means for everyone else, only read