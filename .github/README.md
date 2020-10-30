<h1 align="center">
  <h1 align="center" > COLAB <b>IDE</b> </h1>
    <h3 align="center">Backend for browser based collaborative code editor.</h3>
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
  <a href="#suggestion">Suggestions</a>
</p>

---

## About

A <a href="https://djangoproject.com">Django</a> based API backend for <a href="https://github.com/sinmrinal/collab-ide">COLAB **IDE**</a>.   

## Local Development

##### Developing or running locally steps:
### Step 1: Clone the repo

```bash
https://github.com/sinmrinal/collab-ide-backend.git
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

# Run the project
$ python3 manage.py runserver

# Projects runs on http://localhost:8000

```


## Features

|       Feature              |  Status  |   Stability   |
| -------------------------- | :------: |   :-------:   |
| Boilerplate                |   Done   |     Stable    |
| Compile Code               |   Done   |  Exprimental  |
| Code WebSocket             |   WIP    |       -       |
| Chat WebSocket             |   TODO   |       -       |
| CLI                        |   TODO   |       -       |
| Save Project on Server     |   TODO   |       -       |

<br>
<br>

## Language Support

|     Language      | Support |
| ----------------- | :-----: |
| C                 |   ✔️   |
| C++               |   ❌   |
| Java              |   ✔️   |
| Python            |   ✔️   |
| Go                |   ✔️   |
| Dart              |   ✔️   |
| Rust              |   ❌   |

<br>
<br>

## API Documentation

|       Request              | Protocal |   Type  |             Payload             |         Response         |
| :------------------------: | :------: | :-----: |   :-------------------------:   | :----------------------: |
| Boilerplate Code           |   HTTPS  |   GET   |                  -              |    ```boilerplate```     |
| Compile Code               |   HTTPS  |   POST  |  ```{language, code, input}```  | ```{language, output}``` |
| Code WebSocket             |    WSS   |   -     |                  -              |            -             |
| Code WebSocket             |    WSS   |   -     |                  -              |            -             |

## Suggestion

Reach out to me at one of the following places:

<!-- - Website: **[mrinal.dev](https://mrinal.dev)** -->
- LinkedIn:  **[Mrinal Singh](https://www.linkedin.com/in/sinmrinal/)**
- E-Mail: **mrinal_singh@outlook.com**
