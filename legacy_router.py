#!/usr/bin/python
# File: legacy_router.py
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
	net = Mininet( topo=None, build=False, ipBase='10.20.1.0/24')

	info( '*** Adding controller\n' )
	info( '*** Add switches\n')
	r1 = net.addHost('r1', cls=Node, ip='10.20.1.1/24')
	#r1.cmd('sysctl -w net.ipv4.ip_forward=1')

	info( '*** Add hosts\n')
	h1 = net.addHost('h1', cls=Host, ip='10.20.1.2/24', defaultRoute='via 10.20.1.1')
	h2 = net.addHost('h2', cls=Host, ip='10.20.2.2/24', defaultRoute='via 10.20.2.1')

	info( '*** Add links\n')
	net.addLink(h1, r1, params2={ 'ip' : '10.20.1.1/24'})
	net.addLink(h2, r1, params2={ 'ip' : '10.2.2.1/24'})

	info( '*** Starting network\n')
	net.build()
	info('*** Starting controllers\n')
	for controllers in net.controllers:
		controller.start()

	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
