# BringEmNear

Prt's toolbox for OSINT investigations.

### Installation

```
git clone https://github.com/prtcanfly/BringEmNear.git
cd BringEmNear
pip install -r requirements.txt
```

### Usage

First you will have to edit the ip.py and the snus.py files in the tools folder. Add in your own API keys for IpInfo and Snusbase.

Once you have added your API keys, run the main program using:

```
python BringEmNear.py
```
From there, you have three commands available to use, they are as follows:

```
user
```
This command will ask for a username to search. It operates very similar to Sherlock, but only includes the main social media platforms.

```
snus
```
Searches Snusbase, it will ask for which sort of search you would like to perform, and then ask for the parameters.

```
ip
```
Performs a simple search to find the approximate location of any given IP address.
