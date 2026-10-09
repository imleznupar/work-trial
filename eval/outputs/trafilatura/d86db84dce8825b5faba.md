Apache HTTP Server Version 2.4

IP-based virtual hosting is a method to apply different directives based on the IP address and port a request is received on. Most commonly, this is used to serve different websites on different ports or interfaces.

In many cases, [name-based
virtual hosts](https://httpd.apache.org/name-based.html) are more convenient, because they allow
many virtual hosts to share a single address/port.
See [Name-based vs. IP-based
Virtual Hosts](https://httpd.apache.org/name-based.html#namevip) to help you decide.

As the term IP-based indicates, the server
    **must have a different IP address/port combination for each IP-based
    virtual host**. This can be achieved by the machine
    having several physical network connections, or by use of
    virtual interfaces which are supported by most modern operating
    systems (see system documentation for details, these are
    frequently called "ip aliases", and the "ifconfig" command is
    most commonly used to set them up), and/or using multiple
    port numbers.

In the terminology of Apache HTTP Server, using a single IP address but multiple TCP ports, is also IP-based virtual hosting.

There are two ways of configuring apache to support multiple
    hosts. Either by running a separate [httpd](https://httpd.apache.org/programs/httpd.html)

Use multiple daemons when:

[User](https://httpd.apache.org/mod/mod_unixd.html#user)[Group](https://httpd.apache.org/mod/mod_unixd.html#group)[Listen](https://httpd.apache.org/mod/mpm_common.html#listen)[ServerRoot](https://httpd.apache.org/mod/core.html#serverroot)[httpd](https://httpd.apache.org/programs/httpd.html)
Use a single daemon when:

Create a separate [httpd](https://httpd.apache.org/programs/httpd.html)[Listen](https://httpd.apache.org/mod/mpm_common.html#listen)

Listen 192.0.2.100:80

It is recommended that you use an IP address instead of a
    hostname (see [DNS caveats](https://httpd.apache.org/dns-caveats.html)).

For this case, a single [httpd](https://httpd.apache.org/programs/httpd.html)[VirtualHost](https://httpd.apache.org/mod/core.html#virtualhost)[ServerAdmin](https://httpd.apache.org/mod/core.html#serveradmin)[ServerName](https://httpd.apache.org/mod/core.html#servername)[DocumentRoot](https://httpd.apache.org/mod/core.html#documentroot)[ErrorLog](https://httpd.apache.org/mod/core.html#errorlog)[TransferLog](https://httpd.apache.org/mod/mod_log_config.html#transferlog)[CustomLog](https://httpd.apache.org/mod/mod_log_config.html#customlog)

```
<VirtualHost 172.20.30.40:80>
    ServerAdmin webmaster@www1.example.com
    DocumentRoot "/www/vhosts/www1"
    ServerName www1.example.com
    ErrorLog "/www/logs/www1/error_log"
    CustomLog "/www/logs/www1/access_log" combined
</VirtualHost>
<VirtualHost 172.20.30.50:80>
    ServerAdmin webmaster@www2.example.org
    DocumentRoot "/www/vhosts/www2"
    ServerName www2.example.org
    ErrorLog "/www/logs/www2/error_log"
    CustomLog "/www/logs/www2/access_log" combined
</VirtualHost>
```
    It is recommended that you use an IP address instead of a
    hostname in the \<VirtualHost> directive
    (see [DNS caveats](https://httpd.apache.org/dns-caveats.html)).

Specific IP addresses or ports have precedence over their wildcard equivalents, and any virtual host that matches has precedence over the servers base configuration.

Almost **any** configuration directive can be
    put in the VirtualHost directive, with the exception of
    directives that control process creation and a few other
    directives. To find out if a directive can be used in the
    VirtualHost directive, check the [Context](https://httpd.apache.org/mod/directive-dict.html#Context) using the
    [directive index](https://httpd.apache.org/mod/quickreference.html).

[SuexecUserGroup](https://httpd.apache.org/mod/mod_suexec.html#suexecusergroup)[suEXEC
    wrapper](https://httpd.apache.org/suexec.html) is used.

*SECURITY:* When specifying where to write log files,
    be aware of some security risks which are present if anyone
    other than the user that starts Apache has write access to the
    directory where they are written. See the [security tips](https://httpd.apache.org/misc/security_tips.html) document
    for details.