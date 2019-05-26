# AD-HOC protocols
Wireless and Mobile Networking Course Project

The code is used to run the simulation and provide 3 different types of outputs:

A .routes file containing routing tables of each nodes,
A .tr file containing all transmissions and receptions on the network,
A .csv file containing a summary of successful transmitted packets
We want to be able to see how many packet are successfully received. This information was obtained from the .csv file. We wrote a Python code that parses the .csv file to calculate the total number of packets received during the simulations and we named it TotalPackets.py.

We used IPTracer.tr file to and parsed it for different protocols (AODV,DSDV,DSR) using python scripts (delay.py) and calculated the max delay and average for each type of protocols

We then performed performance analysis on the nodes on:

Effect of mobility on nodes with pause time as 1 sec
Effect on performance (Average Delay, Max Delay and Total packet received) when number of nodes are increased and mobility introduced.
Performace is evaluated and compared

Excecution Environment : C++ Ubuntu 14 ns3.25 python 3
