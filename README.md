# 0x00. AirBnB clone - The console

![hbnb](hbnb.png)

<!-- Image not displaying on Github yet -->

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



## Commands
* create - Create and object.
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* update - Updates an instance based on the class name and id
* quit/EOF - quit the console
* help - see descriptions of commands

To start console type in shell
``` bash
AirBnB_clone$ ./console.py
(hbnb) 
```

## Create
To create an object use format "create " ex:
```bash
    (hbnb) create BaseModel
```

## Show
To show an instance based on the class name and id. Ex:
```bash
    (hbnb) show BaseModel 2344-5567-9845-46252j.
```

## Destroy
To Delete an instance of an object use "destroy id". Ex:
```bash
    (hbnb) destroy BaseModel 2344-5567-9845-46252j.
```
## All
all or all Ex:
```bash
    (hbnb) all or all Place
```
## Update
Updates an instance based on the class name and id:
```bash
    (hbnb) update BaseModel 2344-5567-9845-46252j email "alxafrica@gmail.com"
```

## Quit
quit() or EOF

## Help
help or help Ex:
```bash
    (hbnb) help or help quit
    Defines quit option
    (hbnb) 
```

## Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review




## Authors
| NAME  | EMAIL       |
|-------|-------------|
| Frank Ugwu Williams| frankuwill101@gmail.com|
| Gold Israel| techiegold101@gmail.com| 



<!-- Rest will be added later -->
