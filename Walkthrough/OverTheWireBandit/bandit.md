https://overthewire.org/wargames/bandit/

## Introduction
* The OverTheWire Bandit wargame is aimed at absolute beginners.
* It will teach the basics needed to be able to play other wargames.
* You will learn to use basic Linux commands and how to interact with the system.
* To start the game, you need to connect to the Bandit server using SSH.
#### for ssh used i mremoteng (can use anything of your choice )
* Each level has a goal, which is usually to find a password for the next level.


# Level0
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.
* Connection details:  ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/e1e4a9e5-016e-48c3-bc91-1a86ec6567a5)


# Level0-Level1
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game
* Process: use cat command to view the readme file
*  ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/8552029c-cbbb-45f1-be73-bfbc8ba82f3c)

# Level1-Level2:
The password for the next level is stored in a file called - located in the home directory
* ref: https://medium.com/@.Qubit/how-to-create-open-find-remove-dashed-filename-in-linux-27ee297d1740
* to open a file with -, you can use cat < - or cat ./- or more ./-
* Process: ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/7df76e6c-ff5e-4632-bdd2-ad5a4714bafc)

# Level2-Level3:
The password for the next level is stored in a file called spaces in this filename located in the home directory
* Process: Use tab after cat command: cat sp[PressedTab]
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/f913f9aa-e112-4c90-bac2-6fdd95878537)

# Level3-Level4:
The password for the next level is stored in a hidden file in the inhere directory.
* Process: ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/435719a5-783d-42e6-ac1d-95b57361c135)

# Level4-Level5:
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.
* Process: try cat command on the files in inhere dir. As the files have -, the prev level learnings comes to rescue.
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/2d2b8c34-882b-452c-828e-09232335a262)

# Level5-Level6:
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
human-readable, 1033 bytes in size, not executable
* Ref: https://linuxconfig.org/how-to-use-find-command-to-search-for-files-based-on-file-size
* Process: use find command to search for a specific file size. > file . -size 1033c
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/09d2e269-a54d-45d1-ae59-1a24973f6391)

# Level6-Level7:
The password for the next level is stored somewhere on the server and has all of the following properties: owned by user bandit7, owned by group bandit6, 33 bytes in size
* Ref: https://www.cyberciti.biz/faq/how-do-i-find-all-the-files-owned-by-a-particular-user-or-group/
* Process : Similar to prev level, use find command. > find / -size 33c -user bandit7 -group bandit6
* skim through through the output and cat the file that matches the criteria
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/0faad0be-0ec0-403f-bde2-d255949ef49f)
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/edf6d502-ff77-4365-bcfc-7536d6ed6f8e)

# Level7-Level8:
The password for the next level is stored in the file data.txt next to the word millionth
* Process: Use grep command for fetching through the file
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/acaace9f-271b-4fbd-a884-ff79801de8b7)

# Level8-Level9
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
* Ref: https://www.javatpoint.com/linux-uniq#:~:text=The%20'%2Du'%20option%20is,the%20result%20to%20standard%20output.
* Process: Use sort and uniq commands
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/a85881c2-6b1a-456b-9636-5034b6a87ada)

# Level9-Level10
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
* process:  just do cat and skim through the output
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/e57b6ddf-11d4-44b1-b65b-61c6dfa3dc2a)

# Level10-level11:
The password for the next level is stored in the file data.txt, which contains base64 encoded data
* Process: get the encoded data by using cat on data.txt and use an online base64 decoder for password.
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/e0e6f505-ba4b-4185-86de-ea629ea55517)
* ![image](https://github.com/Rohitha-Karumanchi/cyberSecurity/assets/88244973/b25f7b07-ce6e-481d-a33d-c45ade8ad149)

# Level11-Level12:
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
* Process: description says password is ROT13 encoded. Google for ROT13 decoder and paste the content in data.txt.
* ![image](https://github.com/user-attachments/assets/7308bfcb-a43b-43c5-bb75-41b10470cd13)
* ![image](https://github.com/user-attachments/assets/7929cd57-f51d-4093-8a96-ef8e58a28c2e)

# Level12-Level13:
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
* Process: As mentioned proceed with creating a directory [mkdir /tmp/extract] and move to the new directory [cd /tmp/extract]
* copy the data file to the newly created directory [cp ~/data.txt data]
* The file has been compressed repeatedly, so the key here is to check the file type [file filename] and decompress it based on the file type [google the needed commands]
* Repeat the above, until we achieve ASCII Text file type.
* The decompression commands that are useful in this level are : for gzip file type[mv filename filename.gz , gunzip filename.gz],  for tar file type [tar -xf filename], for hexdunp [xxd -r filename > binaryextractedfilename], for bzip2 [bunzip2 filename]
* ![image](https://github.com/user-attachments/assets/3985e4f3-fb4f-4b94-bd0a-bbdb6f377204)

# Level13-Level14:
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on
* Process: use the sshkey file and the hostname localhost to login as bandit14 and view the password file.
* commands useful: ssh -i privateKeyFile -p portNum usrname@hostname
* ![image](https://github.com/user-attachments/assets/0bd747fa-b719-4e89-8b77-520482a3c9aa)
* ![image](https://github.com/user-attachments/assets/7eed3ddd-73f6-48f5-a8b4-292167ca9dc5)

# Level14-Level15:
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
* Process: for doing so can use command > netcat hostname portname and hit enter and then give current level password
* ![image](https://github.com/user-attachments/assets/0c8aa556-b86c-4ec9-9a9f-ab91fcc20e2f)

# Level15-Level16:
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.
* Process: Use the command: openssl s_client -connect host:port and give the password of current level
* ![image](https://github.com/user-attachments/assets/8266f1e3-7f3d-40d5-be85-f7bafa39e26f)
* ![image](https://github.com/user-attachments/assets/de37332e-1f9f-4512-97a0-222a42157342)

# Level16-Level17:
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.
* Process: First we need to find which ports is server listening: this command gives listening ports: nmap localhost -p 31000-32000
* Now we'll find out which of the listening ports speak SSL: use this command on each of the listening port and enter l16 password : ncat - ssl localhost <port>
* The correct one will give RSA private key
* navigate to tmp : cd tmp :and create a file to store the RSA private key : touch key16.key : add the private key in the file : nano key16.key (ctrl+x to save, Y , enter)
* use the private key to login to next level using ssh command similar to prev levels(l14-l15)
* ![image](https://github.com/user-attachments/assets/acc6d4c5-2c7d-4000-a5eb-ab8492822161)
* ![image](https://github.com/user-attachments/assets/524e0bc8-019d-4ae3-817a-ecd50fb7751f)

# Level17-Level18:
* There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new
NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19
* Process: you can use diff command : diff file1 file2 : output has differences, content after < belongs to file1 and content after > belongs to file2
* ![image](https://github.com/user-attachments/assets/e61c61b7-c7b0-4512-899e-da2647629325)
* When correct password is entered for l18, the terminal closes.

# Level18-Level19:
* The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
* Process: so we need to login using the same process as we did for other levels but we need a bash other than l18
* can use the command on a terminal/cmd(other than bandit): ssh bandit18@bandit.labs.overthewire.org -p 2220 -t "/bin/sh"
* ![image](https://github.com/user-attachments/assets/5fbf6698-59d4-45fd-8e92-7677af0f5810)

# Level19-Level20:
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
* Process: s in permissions means, setuid bit is set
* the file bandit20-do runs command as other user. Using the read the password for next level in (/etc/bandit_pass/bandit20)
* ![image](https://github.com/user-attachments/assets/e95b326b-9d62-47f8-aa00-79a1be7c6def)

# Level20-Level21:
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
NOTE: Try connecting to your own network daemon to see if it works as you think
* Process: netcat: -l for listening
* use pipe and automate the process to check and run the suconnect on the specified port
* ![image](https://github.com/user-attachments/assets/9b49e09c-4b8c-48cc-8283-7e2971ffb479)

# Level21-Level22:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
* Process: go to etc/cron.d and open the cronjob_bandit22 where you can see the path /usr/bin/cronjob_bandit22.sh, open that file and you can notice another path(basically saving the password), open the /tmp/**** file and you can get the password for next level
* ref: https://www.linode.com/docs/guides/how-to-list-cron-jobs/ 
* ![image](https://github.com/user-attachments/assets/e729d505-0aed-432b-aaa4-52530e013e54)

# Level22-Level23:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.
* Process: Similar to above level
* in second step, /usr/bin/cronjob_bandit23.sh understand the code. Based on current user, it is creating target and saving the password in /tmp/target
* change username to "bandit23" in the command and get the target. Open the /tmp/target where you can find the password for next level.
* ![image](https://github.com/user-attachments/assets/64b752fc-c4b1-483a-b5b9-ac35e831d339)

# Level23-Level24:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!
NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…
* Process:  Follow the same steps as prev level and you'll get a code in /usr/bin/cronjob_bandit24.sh which shows a path /var/spool/bandit24 which do not have perm for bandit23 user and it will have the files in it deleted every 1min.
* create a dir in /tmp and in that dir have a file to store the password.
* Now create a shell script in the /var/spool/bandit24 which will execute when cron job runs and saves the password in /tmp/our_folder/password
* the content of the shell script is as simple as
* #!/bin/bash
* cat /etc/bandit_pass/bandit24 > /tmp/test24/password
* give it +x perm
* chmod +x /var/spool/bandit24/foo/getscript.sh
* creating the file and giving the permissions should be done quickly (coz cron job runs every min and deletes the files)
* check the pasword file for next levels entry
* ![image](https://github.com/user-attachments/assets/9eed4de7-451d-471e-955c-b23f69efbf04)

# Level24-Level25:
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time
* Process: nc localhost 30002 asks for a pwd and 4 digit pin seperated by space. To get the pin we can use for loop and pipe.
* syntax of for loop: for i in {starting..ending}; do "any operation you want to do"; done
* in our case the command using for loop will be : for i in {0000..9999}; do echo"pwdofLevel24 $1"; done | nc localhost 30002
* ![image](https://github.com/user-attachments/assets/274a4a96-158b-4c56-9732-ba7b7bc0dbf3)

# Level25-Level26:
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.
* Process:
* ![image](https://github.com/user-attachments/assets/b3a9cc2d-4205-4f14-ae92-067d5b847bdd)
* ![image](https://github.com/user-attachments/assets/d3d79365-f475-497f-94cf-b73764e3b74d)
* The ssh closes immediately after successfull login
* ![image](https://github.com/user-attachments/assets/c116e56c-cf48-416b-98f6-9d84d4b8711f)
* see /etc/passwd which has bandit26
* it shows a path, see the file in the path, the file has content which has usage of "more" command.
* So because of this file, the shell is closing. (google on functionality of more command)
* now make the terminal window small and run the ssh command
* you can see it is not exited, noe keep on pressing "v" which opens a editor-vim
* : in vim is a command mode
* now run 2 commands to get shell access as bandit26
* :set shell=/bin/bash
* :shell
* ![image](https://github.com/user-attachments/assets/d238e98e-4e92-4b4d-89de-7f940bcc5b6d)

# Level26-Level27:
Good job getting a shell! Now hurry and grab the password for bandit27!
* Process: can see a file bandit27-do, see the file type, its an exec.
* execute it using ./ , it says "run command as another user" .
* Now we can view password of bandit27 using this file.
* ![image](https://github.com/user-attachments/assets/b50753b1-12f2-4c2e-ab68-0ee24969c013)

# Level27-Level28:
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. The password for the user bandit27-git is the same as for the user bandit27.
Clone the repository and find the password for the next level.
* process: create a dir in tmp dir.
* use the command to clone the repo using port 2220(default is 22):  git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo 
* ![image](https://github.com/user-attachments/assets/1de4d9b5-c15e-4b3b-b7aa-9293f391e5e7)
* ![image](https://github.com/user-attachments/assets/ef83c6ac-1b11-43a4-ae12-d6f7ea68916a)

# Level28-Level29:
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.
Clone the repository and find the password for the next level.
* Process: same as above level, but we can see the password is not visible.
* use > git log to see previous commits and you can see a commit saying "fixing info leak".
* Use > git checkout command to move to the commit before the fix and see the README.md file which shows the password for bandit29
* ![image](https://github.com/user-attachments/assets/acce8f1c-6047-4f4f-8b91-83f11da5c21d)
* ![image](https://github.com/user-attachments/assets/283a4221-cbc9-4ac4-8b0f-a8311f082c13)
* ![image](https://github.com/user-attachments/assets/a11c4f83-f0f3-43bb-8a7f-f1b19d842526)

# Level29-Level30
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.
Clone the repository and find the password for the next level.
* Process: similar to prev level, but here we need to switch branch, as they mentioned pwd is not in prod.
* check for branches > git branch -a
* Check for dev branches and using > git checkout switch to the dev branch and see the README.md file for password.
* ![image](https://github.com/user-attachments/assets/e2a25b1a-7e6f-4df4-b729-37e63398eb9a)
* ![image](https://github.com/user-attachments/assets/78ec5550-791c-47f5-adf1-f5966c4c43fc)
* ![image](https://github.com/user-attachments/assets/af03fc27-7cf2-429a-a66a-1294bec2cef9)

# Level30-Level31:
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.
Clone the repository and find the password for the next level.
* Process: try checking out branches and commites but there is no password.
* git has a feature called "tags"
* use command > git tag to see what it shows.
* Then use command > git show tagName which reveals the password
* ![image](https://github.com/user-attachments/assets/bd91759a-988f-4270-b9d1-8695abebfb29)
* ![image](https://github.com/user-attachments/assets/bbf4fd84-7891-4d5d-983f-d7c54d907eae)

# Level31-Level32:
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.
Clone the repository and find the password for the next level.
* Process: Similar to prev levels, clone the repo and see the README.md file.
* Follow the steps: create a file key.txt and add content 'May i come in?' in it (note do not add '')
* notice that .txt files are ignored via .gitignore file
* delete the file and add normally > git add . or keep the file and add force > git add -f key.txt
* git commit -m "message for commit"
* git push origin master
* ![image](https://github.com/user-attachments/assets/c7dfbc76-360c-4ae6-b977-eef03de3736b)
* ![image](https://github.com/user-attachments/assets/5f7b52ea-a749-4ca1-a40d-20b26919cf25)
* ![image](https://github.com/user-attachments/assets/8ec9fd57-2877-4c97-a276-eed8b34406a1)

# Level32-Level33:
After all this git stuff, it’s time for another escape. Good luck!
* Process: After executing some commands and seeing the output, you can see that shell is converting everything into uppercase and executing it.
* $0 variable holds the name of the file/ script that is being executed
* echo $0 in the terminal gives the name of the currently used shell.
* $0 in the shell will spawn a new shell.
* $0 can be used to break out of the uppercase
* ![image](https://github.com/user-attachments/assets/e69bbded-0e9f-4f60-abac-7795689a6c0f)

# Level33-Level34:
At this moment, level 34 does not exist yet.
* ![image](https://github.com/user-attachments/assets/af6e7735-1030-4678-aa76-e0ff0d560b14)

























