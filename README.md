# 0x00. AirBnB clone - The console

![hbnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231010T004208Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b17a1e4a72d4d287aa6f92e7b1cebc04701b68f400469590c9ce41e3c9ba9880)

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…


## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Execution
Your shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

To start console type in shell
``` bash
AirBnB_clone$ ./console.py
(hbnb) 
```

## Authors
| NAME  | EMAIL       |
|-------|-------------|
| Frankie Ukwu| youremail@gmail.com|
| Gold Israel| techiegold101@gmail.com| 



<!-- Rest will be added later -->