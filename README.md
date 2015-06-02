# CinnaMON Server
#### A Simple Monitoring Application
![alt tag](https://raw.github.com/eladhayun/CinnaMON/master/resources/logos/github.png)
```
Install: python setup.py install
Run: python /usr/lib/python2.6/site-packages/cinnamon-1.0.0.0-py2.6.egg/cinnamon/repository.pyc
```

This application listens on port 5000 by default, you can either open this port on the server's firewall, use port forwarding on your router to expose it to the world, or if you are already running an apache server, copy the cinnamon.conf script inside *config* to */etc/httpd/conf.d/* (in Redhat/Centos/Fedora) to redirect port 80 to 5000
you would access you server from the phone app this way --> http://www.mypublicipaddress.com/cinnamon

###### This app uses the following libraries:
* [Flask](http://flask.pocoo.org)
* [psutil](https://pypi.python.org/pypi/psutil)

###### The Client's Repository:
* [cinnamon-client](https://github.com/eladhayun/cinnamon-client)

![alt tag](https://raw.github.com/eladhayun/CinnaMON/master/resources/screenshots/screenshots.png)
