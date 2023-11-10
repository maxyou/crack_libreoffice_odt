## crack_libreoffice_odt
crack encrypted LibreOffice odt file

### install and run

- Install LibreOffice SDK.
- Start libreoffice server in headless mode.

```
nohup soffice --headless --accept="socket,host=0.0.0.0,port=8100;urp;" &
```

- Modify gen.py and run main.py to try you password.

I tried above steps in a Ubuntu 22.04 virtual machine.

### my story

I had a important ODT file which was created with LibreOffice writer. This file is encrypted with one of my often used password combination, but I forget the combination.

I try to crack this ODT file because the combination can be iterated and it is possible to find the password out.

The key step is to use the API to call the load function lightweightly. Thanks to chatGPT, it tell me how to call the load function without trggiring the grahpical UI which cost a lot of time.

Finally, I compeleted this project. It can try about 3-4 passwords per second on my slow virtual machine. Therefore, the program can only crack a very limited amount of passwords. Why the attempts of password is very slow, my guess is that, this load function need to communicate with the libreoffice server and ask the server to load the ODT file.

Funnily enough, after spending a lot of time to digging LibreOffice document and write the program, just before I was going to try all the possible combinations, I manually made one last attempt and figured out the password, surprisingly.

It turned out that I had just forgot to capitalize the first letter of my password, and I made one of the most classic password mistakes.



