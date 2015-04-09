Title: Logging Connections With firewalld
Date: 2015-04-09T14:59:03+01:00
Author: Russell Gray
Slug: logging-connections-with-firewalld
Tags: firewalld, centos

I was recently trying to diagnose a production connectivity issue on a CentOS 7 box and found it a bit non-obvious how to get the firewall to log connection attempts. It is in fact documented in [section 4.5.15.4.3][1] (how about that for a document subsection?!) but for ease of reference I'm putting it here.

Basically, add a rich rule that includes log level details. For example, to open port 10000 for IP address 198.51.100.0, use the following:

    :::bash
    $ sudo firewall-cmd --zone=public --add-rich-rule="rule family="ipv4" source address="198.51.100.0/32" port protocol="tcp" port="10000" log prefix="test-firewalld-log" level="info" accept"

Connection attempts from that IP address will then be logged in /var/log/messages:

    :::bash
    $ sudo tail -f /var/log/messages |grep test-firewalld-log


[1]: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Security_Guide/sec-Using_Firewalls.html#Configuring_Complex_Firewall_Rules_with_the_Rich-Language_Syntax