TVShowsManager
============

> What is it ? 

TVShowManager is a *simple* tool to download automatically your TV Shows. 

Quick remark before giving more details : Code still needs refactoring. This is a 'Quick & Dirty' version developed in few minutes but _working_ great ! 

> What is that magic ? 

Basically, this project uses different components :
- **_Transmission remote_** to download the torrents 
- (Unofficial) **_EZTV API_** I developed few months ago

> Ok, so how to use it ? 

To use it, you have to create a configuration file, let's take an example :

```
[config]
username = transmission
password = password
ip = 192.168.176.15
timer = 5

[Vikings]
season = 1
episode = 7
```

The first section is the _*config*_ one. 
You define different fields such as :

- _Username_: Credentials to connect to your transmission. 
- _Password_: Bis. 
- _IP_: IP where your Transmission-remote is running
- _timer_: How many minutes you want to wait between 2 re-try. 


Then, the other sections are for your different tv show. 
Based on this example, you're watching _Vikings_ and stopped at the episode 7, season 1. 

This tool will check for new existing episodes, download them by sending RPC commands to your Tranmission instance and finally, update your *config.ini* file. 

Easy, uh ? 

> Ok, I want to launch it now !

No problem for that. 
If you created your _config.ini_ file in the same directory, then launch : 

```
$ python TVShowsManager.py
```

> That's nice but I want to run it in background

Yup, I got a solution. 
To do so, use _screen_ on Linux. 

Launch it like this : 

``` 
$ screen python TVShowsManager.py
```

Then, you can do ctrl-A, ctrl-D to make it run in background.

And I'm sure you want to know how to come back in the screen's session ? 

Type : 

```
$ screen -r 
```

If there are several sessions, just do this :

```
$ screen -r <id>
```

And Boom, you're _back in_ !

> How do you manage to send your magnet link ? 

I was looking on the Internet and I found this : 

```bash
transmission-remote <IP> -n <USER>:<PORT> --add '<MAGNET>'
```

Using this command you'll be able to send to **<IP>** a magnet link really easily. 

> License ? 

This project has been released under MIT License. 

Feel free to fork the code and have fun. 