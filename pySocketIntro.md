#An Introduction to Python Sockets

### Sockets - What are they and why do I care?

In the realms of networks and programming, you'll often run across or use sockets.

The docs for these interfaces can often be nebulous and a deterrent from digging into this weird and wonderful world.

Many developers new to sockets may understand that sockets let them communicate over networks, but what does that have to do with anything? It turns out, it has to do with quite a lot.

Virtually every server the average user will visit on the internet uses sockets for communication. Sockets allow computers of different designs and operating systems to transfer data between themselves with relative ease. Programmers don't have to care if they're talking to a Microsoft Windows computer or to a FreeBSD computer. They don't have to care if they need to talk to 10 month old hardware or 10 year old hardware. Other protocols like IPX or NetBIOS require a native Microsoft Windows application, or a ported version, if the user is on a different operating system.

So sockets are nice and make lives easier. How does that help with using them?

Admittedly, not a lot. It gives the developer (or anyone curious enough) an idea of why sockets are so universal in our programming languages. There's a whole world revolving around sockets, but that goes too in depth for most people. For the insanely curious, look [here](http://compnetworking.about.com/od/itinformationtechnology/l/aa083100a.htm) for more on the socket world.

### Time to get to the good stuff!

Python is known for simplifying things, but in the case of sockets, it's actually quite low level. And to understand "low level", you'll need to understand "high level". "High level" is something that you do understand, you just don't understand it yet. ;-)

To do a quick explanation of "high level", take a look at Siri or Google Now. You just speak to it and it will check Google for you. Easy, right?

An explanation of "Low level" could be you crafting the packet before sending it on its merry way to Google's servers to request the information you want. Not nearly as easy to do. (And if you don't know what packets are, check [this](http://computer.howstuffworks.com/question525.htm). Its a good thing to know how a bomb works if you're going to defuse it.)

[PICTURE]

The last point I need to make before you see any code is that there are two types of sockets we'll be using.

1. Client sockets
2. Server sockets

##### Client sockets

Client sockets make requests to server sockets in exchange for information. The only two things you need to know before you make a client socket is the server IP and the server port. In this case I will use Scotch.io and port 80.

```
import socket
sock = socket.socket()
ip = socket.gethostbyname('www.scotch.io')
sock.connect((ip, 80))
sock.close()
```
Now this code won't do much if you run it. It will only open a connection to Scotch.io's IP and close it immediately after. (Not closing sockets can cause issues with poorly written code. Modern webservers should be able to handle hanging socket connections, though.)

##### Explanations

Explanation time! Writing the program is all well and good, but what actually happened when you ran it?
Here's the code again with line numbers.
```
1 | import socket
2 | sock = socket.socket()
3 | ip = socket.gethostbyname('www.scotch.io')
4 | sock.connect((ip, 80))
5 | sock.close()
```

###### Line 1
Line 1 should be pretty obvious. It imports the socket library. Yay!

###### Line 2
Line 2 is where things really get started. What happens is we create a variable to contain the function "socket.socket()". (Otherwise, we'd have to type everything out. Instead of being "sock.connect((ip, 80))", we would have to type "socket.socket().connect((ip, 80))". It saves our wrists from doing too much work.)

Now, what happens inside "socket.socket()"? Why do we need it?

It is a function that contains several hidden parameters which define what kind of socket it will be. The full list of hidden parameters is found in the docs (ugh!). By typing in "socket.socket()" we initialized this. 

```
socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
```

Breaking it down, we'll start with the family parameter.

Using the family "AF_INET" means that we'll be using the normal IPv4 addresses we are used to. IPv4 is what we will focus on; however, there are other families that are available. It is best to be aware of them.

 - AF_INET6 is used mainly for IPv6, which will become more prevelant in the future.

 - AF_UNIX, which is used for different processes on the machine to communicate to each other. This family generally does not communicate beyond their host machine.

 - AF_CAN allows communication over CAN interfaces.

 - AF_RDS (which stands for Reliable Datagram Sockets (RDS)), is a protocol for delivering datagrams. (Rather reliably, it seems.)

As a note, there are also PF_* prefixes. The main difference between AF and PF is that AF stands for "Address Family" and PF for "Protocol Family".

