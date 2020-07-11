EMYL Instagram PhosGraph

We define Free Software Revolution 1.0 (FSR1) as the period encompassing the creation of GNU Linux and tools to Google's acquisition of the Android operating system. The mobile computing era, empowered by Android and iOS, saw the rise of tech giants and start-ups worth trillions of USD, as well as cryptocurrencies. 

We may say FSR1 is essentially CLONING the then proprietary Unix operating systems and tools.

Free Software Revolution 2.0 (FSR2) will then be the CLONING of MAGAF social networks, where MAGAF stands for Microsoft Apple Google Amazon Facebook. It is a pun to MAGA+F, everyone's favorite derogatory letter.

Cloning MAGAF is not rocket science. There are enough free software programmers to do so. However, they move like random air particles. We need SEVERAL BREAKTHROUGH MECHANISMS to make these most talented individuals on Earth to become "self organized". Phosway is the name of this comprehensive suite of projects. (Click [here](https://github.com/udexon/Phosway/blob/master/README.md) for details.)


## B. PhosGraph Instagram Examples

Let us illustrate the philosophy and benefits of EMYL using the following example:

The number of followers of an Instagram user is extracted and saved on a publicly accessible web server, PhosGraph.
Anyone may be able to query the PhosGraph server, as well as contribute code to enhance its functionalities.
Donors may pay contributors of PhosGraph using PhosPay, a novel ID-less online payment system system based on transient key cryptography.

https://github.com/udexon/Phosway/blob/master/PhosGraph_Instagram.md

The example given in the link above seems completely counterintuitive compared to the "mainstream" web programming solutions in recent years. i.e. One expects to see a node.js or yarn project with a beautiful front end and a sophisticated back end which consume no less than 500MB or disk space.

There are 2 primary reasons for this:

To demonstrate the features of  transient key cryptography graph database
Zero investment bootstrap

Transient key cryptography has gained some exposure indirectly in recent years due to the popularity of blockchain technologies. However, due to the lack of easy to use tools and easy to understand theories and use cases, TKC and blockchain technologies have remained as niche areas accessible to several small circles of elite cryptographers and programmers. 

While the definitions of transient key cryptography and graph database given in the literature may be over complicated for most readers, we shall attempt to present a simplified version:

Transient key cryptography: algorithms based on asymmetric cryptography where the key pairs generated for a user, device or process (owner) change over a short period of time.

Graph database: a database whose structure is represented as a graph, by definition, made up of vertices (nodes) and edges.

- Question: Why are we using space delimited text files as database in the age of so many "proper" graph database software?

Answer: the conventional graph database software have too many outdated assumptions which may hinder Phosway.

The most important difference between graph database and conventional SQL database is often muddled by other technical issues: the key of an object, equivalent to the field or column in SQL database, can be defined on the fly. This feature makes a text file of JSON data a graph database, more flexible than any multi gigabytes SQL installation. This conclusion however may be too embarrassing for DB admins, hence perhaps intentionally subdued over the years.

We may still use them as and when needed.

:: N3

The core issue here is not whether theoretically a JSON data file is a graph database, as we could easily write a wrapper module to convert the JSON data into any format required by established graph database software. The core issue here is how to incorporate TKC into GDB ….  And train new free software programmers, and make them earn money as they learn ….


## C. Structure of Phosway

In order to present an overview of Phosway, we categorize the various modules of Phosway according to a model similar to the OSI layers, from low level to high level:

1. Phoscript / Phoshell

Phoscript is a Reverse Polish Notation, stack machine programming language, derived from the Forth programming language.

Phoshell is a stack machine shell employing Phoscript, implementable in ANY known programming language and framework.

Let us compare the roles of programming langauges in other project in order to highlight the significance of Phoscript by look at the following project:

https://github.com/udexon/Phoshell/blob/master/PhosIDE_Part_III.md

Jitsi Meet is a well established and popular open source video conferencing app. Video conferencing apps have gained unexpected popularity recently as the COVID19 pandemic looms. Jitsi Meet uses the React Redux framework and has source code for web client, Android and iOS apps respectively.

While we are not aware of any recent systematic studies into this problem, we may assume that difficulties in training developers due to unfamiliarity with new programming languages and frameworks, e.g. Jitsi Meet, would have prevented more free software programmers to participate. The readers are welcome to investigate this issue.

Phoshell is not just a user interface, i.e. how users use a program. It is also a programming interface i.e. it enables programmers to reprogram the program via the shell. With Phoshell, programmers and users have an interface to think about the possibilities of FURTHER developing Jitsi Meet or any app. Interface is an important element for users and programmers to think what can be done with a porgram. e.g. The inventions of 2D screen, color screen, mouse, input devices etc. gave rise to new generation of applications.

Phoshell have integrated the functionalities of shell (to access high level commands), interpreters (to access low level functions) as well as GUI (Phoshell is integrated into GUI of any app). Through networks, Phoshell can extend function libraries live on the fly, just like JavaScript front end. 

## "Superapp" 

Although JavaScript can update function libraries on the fly via networks, but the programming language itself is too cumbersome to be used on the fly, via GUI. Phoshell is another layer added on top of web and mobile apps to enable extensible libraries (live loading) and live reprogramming. 

Just like bash shell where new commands and libraries are added continuously, instead of installing new games as new mobile apps, Phoshell enables the function libraries of new games or apps to be added, integrated, reused and reprogrammed!

It's like a superhero who can become anyone, Mystique or [Apocalypse En Sabah Nur](https://en.m.wikipedia.org/wiki/Apocalypse_(comics)) in X Men.

While Phoshell provides a "superapp" platform to merge all apps and games into one, we believe merging games is a good start as the goals are well defined. While merging games, we build up function libraries for other apps at the same time. It is easier to figure out game logic than integrating social media apps as real world logic may be more restrictive.

By adding Facebook functionalities to Jitsi Meet using Phoshell, we may create "universal social media app", Phosbook, for the sake of argument. We may add Reddit upvotes and karma functions to Phosbook. These are no longer unrealistic goals as Phoshell greatly simplifies the development work, via the PhosPay EMYL (Earn Money as You Learn) training framework outlined later in this article.


2. PhosKey, PhosGraph, PhosTunnel: critical components in distributed cloud, blockchain etc. 

As we have outlined in the previous section, Phoshell is a universal interface for porting various existing function libraries and apps. Here we briefly outline 3 modules that enable us to create a new type of cloud computing platform: PhosCloud.

We postulate that the conventional cloud computing infrastructure is very much centred upon the Unix style user authentication paradigm, where there is always a central authority who can override everything else within the system. 

Based on a fundamental breakthrough in the application of transient key cryptography, which we call PhosKey, where a user may generate a new pair of public and private keys for every transaction, we overcome the fundamental restriction of the conventional, centralized cloud computing paradigm.

Starting with this breakthrough, we may then redesign almost all cloud computing applications with a new paradigm.

Besides PhosKey and PhosGraph (outlined earlier), we need another essential element to complete our new cloud computing platform: SSH tunnel.

SSH tunnel can be activated at VPS (virtual private servers) which cost around USD10 per month (MYR30). We believe the BitTorrent network is a variation of SSH tunnel. By using SSH tunnel (PhosTunnel), we enable a large number of mobile devices and home computers to be accessible as PhosCloud nodes.

- PhosCloud = PhosKey + PhosGraph + PhosTunnel

PhosCloud could be seen as an enhanced version of BitTorrent, where its functionalities are no restricted to only file transfer, but the whole of conventional cloud computing, except that this time, the infrastructure is literally and physically owned by individuals.

<!-- 

:: Merge PhosApps into next section -- stages of development

:: At end of list, need a new leading expressive paragraph.

SSH tunnel is also based on TKC?

How might one make use of the data in PhosGraph?

PhosCloud needs ssh tunnel shared vps. BitTorrent ++.

:: N4 explaining why CLONING ... not that bad ... every section needs ONLY ONE EXPRESSIVE LEADING paragraph that reads natural to readers, to convey the contents of that section. The rest of the section are either subsections (list of paragraphs, not expressive), or expansion from the LEADING paragraph. The a complete article is made up of sections. A section is a list of expressive (leading) paragraph plus non-expressive paragraphs.

:: 1 2 3 4 are 4 different layers of OSI, from low to high.

Explain costs later. First explain relations of phos modules and how do they clone magaf. 

A to Z
- A = Start from Online tipping (EMYL Instagram Social Networks).
- Z = So main activity is clone MAGAF. 

2 aspects: 
1. final aim is to clone MAGAF. 
2. how to execute modules of Phosway in sequence?

-->

### PhosApps: Stages of Development

As readers would have noticed, Phos is a rather versatile prefix, originated from the Greek word for "light", which also rhymes with Forth, the original inspiration for this project. As such, we may term all Phosway Applications as PhosApps.

Having understood the overall structure of Phosway, the timelines of development of various Phosway modules are decribed below:

1. Extending PhosGraph

Database is perhaps the foundation to all applications. As such, PhosGraph, a graph database for Phosway, is the foundation to all Phosway applications.

The following could be the simplest and yet illustrative operation that can be performed on PhosGraph:

- User A1 adds location information F1 for Instagrammer IG1.

Any user AX can update any information FX about Instagrammer IGX.

PhosGraph thus becomes a collective database of personal information for any Instagrammer, or in fact, any user on any social network. PhosGraph will essentially be the super database for everyone on the Internet.

By law of slow change of popularity, a famous person will stay famous over a certain period of time. A less famous person may become more famous. As such, their personal information will become valuable.

How can we make use of such information? Enter PhosPay: a micropayment system PhosPay to monetize information in PhosGraph, just like how MAGAF make money, but more transparent, open, in small amounts.


2. PhosPay

- User B tips IG1 using PhosPay.

https://github.com/udexon/PhosPay

Tipping on any social network and EMYL coaching for Phosway.

:: List to do until PhosPay is usable …. This is the MOST IMPORTANT SECTION OF THE WHOLE ARTICLE!!!

PhosPay PhosChat are critical for social networks? Forum comments, database are based on PhosGraph.

Just describe how Phosway components replicate list of MAGAF, Twitter etc. 

- Need more factors to conclude how EMYL Phosway will change FSR1 to FSR2: Just use Phosway to clone MAGAF!!



3. IG1 holds meet the fans parties

PhosChat anonymous chat between fans and celebrities, very important, huge demand, captive market. Fraud from hacking dating websites.


4. Local sponsors hire IG1 to make advertisement videos.

Other talents like video editing etc. are needed.

All paid using PhosPay.




## D. Benefits of Earn Money as You Learn to Free Software Revolution 2.0

- Purpose of EMYL is to provide training

Consider this question:

- Are contributors to free software fairly rewarded?

Although it may be time consuming and labourious to conduct a comprehensive survey to answer this question, we can easily find many free software contributors who receive no moentary rewards, while there are plenty highly paid programmers within MAGAF who in turn make use of various types of free software.

We believe PhosPay will provide a fundamental solution to this problem.

How?

Currently, most free software programmers contribute without receiving any monetary rewards. On the other hand, many programmers who are employed by various companies, large and small, specializing in software or other industries, receive various levels of salaries, while making use of free software. PhosPay offers a third mode of payment besides these two conventional models.

PhosPay aims to overcome this bottleneck by enabling online micropayment, so that anyone can reward programmers a small amount on their contribution to free software, instead of relying on investors to invest large sums of money.

As such, the software evaluation period becomes shorter. Typical start up projects take 3 months. PhosPay free software can be evaluated weekly. Hence improved transparency and productivity.

Imagine this: paying the top 1000 free software programmers USD1000 per week only needs USD 1 million. This is small  change for millionaires around the world, not even tips for a drinking party. It did not happen just because no platform exists for such mode of tipping.

EMYL vs. conventional start up funding

- EMYL: weekly, one programmer, free time after work, cost = tipping amount. More free man power during COVID19 crisis.

- Conventional start up: minimum 3 months, 5 people team, Investment?


### Scenarios and benefits using PhosPay.

### EMYL Earn Money as You Learn

- Apply PhosPay to students
- Generalize EMYL to all industries, other fields of education, beyond computer programming

Students are always the best source of labour as far as free software is concerned, as they are subsidized by parents or state. In fact, although there has been a lack of comprehensive surveys on the effects of free software on the education of students, some random samples would affirm the huge benefits.

Through examples in literature and surviving practices from pre industrialized era, we derived a training scheme known as " Earn Money as You Learn" (EMYL), which we believe will be effective in ...

... fighting workplace discrimination.

Our purpose is to educate the next generation of free software programmers, Earn Money as You Learn. Goal is to make everyone earn as much as shareholders of MAGAF, by creating a fair platform for all developers and users to participate.

It doesn't matter how good a programmer is. Software development is labour intensive therefore capital intensive. PhosPay enables replication and directions with monetary incentives, more programmers are attracted if a certain project receives large sums of weekly online tippings. Without PhosPay, free software development stagnates as they are currently.


### Phosway A to Z

Just like GNU projects' major achievements lied in cloning Unix, Phosway may create great values to society just by  cloning MAGAF social networks.

Most of the components needed for PhosPay already exist. We just need to clone them and make modifications.

Cloning MAGAF is not rocket science. There are enough free software programmers to do so. They only need PhosPay so that their efforts can be directed, instead of Brownian random directions at the moment.




## E. Investment needed for Phosway ... Search Engine or PhosKnow

:: N6

PhosEngine or PhosKnow are more complicated to grasp for users … ??

1. Otherwise, how much money is needed to build a NEW commercially sustainable search engine in 2020?

2. Merge data from everywhere, then search. Big data?

3. PhosKnow. Better Wikipedia?

Analyze the benefits of one particular aspect, e.g. PhosKnow, compared to other aspects, to give readers a comprehensive picture.


Workplace discrimination means plenty of work force for Phosway at all ages, anywhere in the world.

What can PhosGraph PhosKnow achieve?

A super social network owned by everyone and rewards everyone fairly. Has built in mechanism for fairness via competition.



