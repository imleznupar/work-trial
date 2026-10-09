# Apache IP-based Virtual Host Support

  * ![](../images/down.gif)What is IP-based virtual hosting
  * ![](../images/down.gif)System requirements
  * ![](../images/down.gif)How to set up Apache
  * ![](../images/down.gif)Setting up multiple daemons
  * ![](../images/down.gif)Setting up a single daemon with virtual hosts



## What is IP-based virtual hosting ¶

IP-based virtual hosting is a method to apply different directives based on the IP address and port a request is received on. Most commonly, this is used to serve different websites on different ports or interfaces.

In many cases, [name-based virtual hosts](name-based.html) are more convenient, because they allow many virtual hosts to share a single address/port. See [Name-based vs. IP-based Virtual Hosts](name-based.html#namevip) to help you decide. 

## System requirements ¶

As the term IP-based indicates, the server **must have a different IP address/port combination for each IP-based virtual host**. This can be achieved by the machine having several physical network connections, or by use of virtual interfaces which are supported by most modern operating systems (see system documentation for details, these are frequently called "ip aliases", and the "ifconfig" command is most commonly used to set them up), and/or using multiple port numbers.

In the terminology of Apache HTTP Server, using a single IP address but multiple TCP ports, is also IP-based virtual hosting.

## How to set up Apache ¶

There are two ways of configuring apache to support multiple hosts. Either by running a separate `[httpd](../programs/httpd.html)` daemon for each hostname, or by running a single daemon which supports all the virtual hosts.

Use multiple daemons when:

  * There are security partitioning issues, such as company1 does not want anyone at company2 to be able to read their data except via the web. In this case you would need two daemons, each running with different `[User](../mod/mod_unixd.html#user)`, `[Group](../mod/mod_unixd.html#group)`, `[Listen](../mod/mpm_common.html#listen)`, and `[ServerRoot](../mod/core.html#serverroot)` settings.
  * You can afford the memory and file descriptor requirements of listening to every IP alias on the machine. It's only possible to `[Listen](../mod/mpm_common.html#listen)` to the "wildcard" address, or to specific addresses. So if you have a need to listen to a specific address for whatever reason, then you will need to listen to all specific addresses. (Although one `[httpd](../programs/httpd.html)` could listen to N-1 of the addresses, and another could listen to the remaining address.)



Use a single daemon when:

  * Sharing of the httpd configuration between virtual hosts is acceptable.
  * The machine services a large number of requests, and so the performance loss in running separate daemons may be significant.



## Setting up multiple daemons ¶

Create a separate `[httpd](../programs/httpd.html)` installation for each virtual host. For each installation, use the `[Listen](../mod/mpm_common.html#listen)` directive in the configuration file to select which IP address (or virtual host) that daemon services. e.g.
    
    
    Listen 192.0.2.100:80

It is recommended that you use an IP address instead of a hostname (see [DNS caveats](../dns-caveats.html)).

## Setting up a single daemon with virtual hosts ¶

For this case, a single `[httpd](../programs/httpd.html)` will service requests for the main server and all the virtual hosts. The `[VirtualHost](../mod/core.html#virtualhost)` directive in the configuration file is used to set the values of `[ServerAdmin](../mod/core.html#serveradmin)`, `[ServerName](../mod/core.html#servername)`, `[DocumentRoot](../mod/core.html#documentroot)`, `[ErrorLog](../mod/core.html#errorlog)` and `[TransferLog](../mod/mod_log_config.html#transferlog)` or `[CustomLog](../mod/mod_log_config.html#customlog)` configuration directives to different values for each virtual host. e.g.
    
    
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

It is recommended that you use an IP address instead of a hostname in the <VirtualHost> directive (see [DNS caveats](../dns-caveats.html)).

Specific IP addresses or ports have precedence over their wildcard equivalents, and any virtual host that matches has precedence over the servers base configuration.

Almost **any** configuration directive can be put in the VirtualHost directive, with the exception of directives that control process creation and a few other directives. To find out if a directive can be used in the VirtualHost directive, check the [Context](../mod/directive-dict.html#Context) using the [directive index](../mod/quickreference.html).

`[SuexecUserGroup](../mod/mod_suexec.html#suexecusergroup)` may be used inside a VirtualHost directive if the [suEXEC wrapper](../suexec.html) is used.

_SECURITY:_ When specifying where to write log files, be aware of some security risks which are present if anyone other than the user that starts Apache has write access to the directory where they are written. See the [security tips](../misc/security_tips.html) document for details.