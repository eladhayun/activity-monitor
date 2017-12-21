# Activity Monitor
#### A Simple Monitoring Application

```
Install: python setup.py install
Run: python /usr/lib/python2.6/site-packages/cinnamon-1.0.0.0-py2.6.egg/cinnamon/repository.pyc
```

This application listens on port 5000 by default, you can either open this port on the server's firewall, use port forwarding on your router to expose it to the world, or if you are already running an apache server, copy the cinnamon.conf script inside *config* to */etc/httpd/conf.d/* (in Redhat/Centos/Fedora) to redirect port 80 to 5000
you would access you server from the phone app this way --> http://www.mypublicipaddress.com/cinnamon

###### This app uses the following libraries:
* [Flask](http://flask.pocoo.org)
* [psutil](https://pypi.python.org/pypi/psutil)

![alt tag](https://lh3.googleusercontent.com/8Gwl2cXaAXXoeuuxRpMO1R6kHgVjg07EmPFPPSpwbL3Xg0AcpLINxgNCksCLKcB2Yw=h310)
![alt tag](https://lh3.googleusercontent.com/U4vLDSF4q1CdsGJYbUvWSaHpAUW1YDeEcKlKzhk9XCw5VbddwhjQ0RpcUNG29D_hJm0x=h310)
![alt tag](https://lh3.googleusercontent.com/oQ7FAn3AGdAJghBCEWKxwgsXdXFJG3zeJkMz3_K54GmhhotOMNxnLYNhXUjtpQAVc7g=h310)
![alt tag](https://lh3.googleusercontent.com/YMAb-gPu0Jnx5KcoA245k_ffs_CF4QxMjIcRfdOenD00oQulb78gpVot4aELgTYWBcI=h310)
