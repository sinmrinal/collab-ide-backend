<h1 align="center">
  <h1 align="center" > COLLAB <b>IDE</b> </h1>
    <h3 align="center">Backend for in-browser collaborative code editor.</h3>
</h1>

<p align="center">
    <img src="https://flat.badgen.net/badge/stability/beta/yellow?icon=github">
    <img src="https://img.shields.io/badge/OS-Linux-red?style=flat&logo=linux">
    <img src="https://flat.badgen.net/github/commits/sinmrinal/collab-ide-backend?icon=github">
    <img src="https://flat.badgen.net/github/last-commit/sinmrinal/collab-ide-backend?icon=github">
</p>
      
<p align="center">
  <a href="#about">About</a> •
  <a href="#local-development">Local Development</a> •
  <a href="#features">Features</a> •
  <a href="#language-support">Language Support</a> •
  <a href="#api-documentation">Documentation</a> •
  <a href="#suggestion">Suggestions</a>
</p>

---

## About

A <a href="https://djangoproject.com">Django</a> based API backend for <a href="https://github.com/sinmrinal/collab-ide">COLAB-IDE</a>.   

## Local Development

##### Developing or running locally steps:
### Step 1: Clone the repo and get inside the repo

```bash
$ git clone https://github.com/sinmrinal/collab-ide-backend.git && cd collab-ide-backend
```
### Step 2: **[OPTIONAL]** Create virtual enviroment

1. Install virtualenv

    ```bash
    $ pip install virtualenv
    ```

2. Create Enviroment

    ```bash
    $ virtualenv env
    ```

3. Activate Enviroment
   
   ```bash
   $ source env/bin/activate
   ```


### Step 3: Install dependencies

##### Dependencies are in requirements.txt file. Just run- 

```bash

# Install dependencies
$ pip install -r requirements.txt

```

### Step 4: Usage

Now you can run the application by :

```bash
# Set TOKEN
$ export TOKEN="add your token here without quotes."

# Run the project
$ python3 manage.py runserver

# Projects runs on http://localhost:8000

```

### OR Using Docker

#### Step 1: Clone the repo and get inside the repo

```bash
$ git clone https://github.com/sinmrinal/collab-ide-backend.git && cd collab-ide-backend
```

### Step 2: Build the image

```bash
$ docker build -t collab-backend-image .
```

### Step 3: Run container/app

```bash
$ docker run -d --name collab-backend -p 8000:8080 collab-backend-image
```



## Features

|       Feature              |  Status  |   Stability   |
| -------------------------- | :------: |   :-------:   |
| <s>Boilerplate</s> ~Depricated~ |   Done   |     Stable    |
| Compile Code               |   Done   |  Stable  |
| Collaborate                |   Done   |  Exprimental  |
| Chat WebSocket             |   TODO   |       -       |
| CLI                        |   WIP    |       -       |
| Save Project on Server     |   TODO   |       -       |

<br>
<br>

## Language Support

|     Language      | Support |
| ----------------- | :-----: |
| C                 |   ✔️   |
| C++               |   ✔️   |
| Java              |   ✔️   |
| python            |   ✔️   |
| Go                |   ✔️   |
| <s>Dart</s> ~Depricated~             |   ✔️   |
| Rust              |   ✔️   |

<br>
<br>

## API Documentation

|       Request              | Protocal |   Type  |             Payload             |         Response         |
| :------------------------: | :------: | :-----: |   :-------------------------:   | :----------------------: |
|<s>Boilerplate Code </s> ~Depricated~ |   HTTP  |   GET   |                  -              |    ```boilerplate```     |
| Compile Code               |   HTTP  |   POST  |  ```{language, code, input}```  | ```{language, output}``` |
| Create Room               |   HTTP  |   POST  |  ```{roomName, adminName, token}```  | ```{roomID, roomName, createdBy, createdOn}``` |
| Join Room               |   HTTP  |   POST  |  ```{roomID, userName, token}```  | ```{roomID, roomName, createdBy, createdOn, joinedBy}``` |


## Suggestion

Reach out to me at one of the following places:

<!-- - Website: **[mrinal.dev](https://mrinal.dev)** -->
- LinkedIn:  **[Mrinal Singh](https://www.linkedin.com/in/sinmrinal/)**
- E-Mail: **mrinal_singh@outlook.com**
