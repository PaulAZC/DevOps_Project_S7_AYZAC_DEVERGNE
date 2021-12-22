## DevOps Project for the semester 7
## Authors : Paul AYZAC & Noémie DEVERGNE
## Links to the content of our project :
- [1. Description of the project](#1-description-)
- [2. Grades](#2-grades-)
- [3. Application](#3-application-)
- [4. Vagrant](#4-vagrant-)
- [5. Docker and Docker compose](#5-docker-and-docker-compose-)
- [6. Kubernetes :](#6-kubernetes-)
- [7. Istio and monitoring :](#7-istio-and-monitoring-)
- [8. Bonus :](#7-bonus-)

## 1. Description :
The aim of this project will be to use all the tools seen in class within the same project. It will highlight a CRUD application.
## 2. Grades :
| Subject                                                         | Code  | Max. grade |      Task done     |
| :-------------------------------------------------------------- | :---: | :--------: | :----------------: |
| Enriched web application with automated tests                   |  APP  |     +1     | :white_check_mark: |
| Continuous Integration and Continuous Delivery (and Deployment) |  CICD |     +3     | :white_check_mark: |
| Containerisation with Docker                                    |  D    |     +1     | :white_check_mark: |
| Orchestration with Docker Compose                               |  DC   |     +2     | :white_check_mark: |
| Orchestration with Kubernetes                                   |  KUB  |     +3     |        :x:         |
| Service mesh using Istio                                        |  IST  |     +2     | :white_check_mark: |
| Infrastructure as code using Ansible                            |  IAC  |     +3     |        :x:         |
| Monitoring                                                      |  MON  |     +2     |        :x:         |
| Accurate project documentation in README.md file                |  DOC  |     +3     | :white_check_mark: |
| Use of the python language for the CRUD application             |  BNS  |     +1     | :white_check_mark: |
| Using PostgreSQL for the CRUD application                       |  BNS  |     +1     | :white_check_mark: |
| Sentry implementation for monitoring                            |  BNS  |     +1     | :white_check_mark: |
| Total point                                                     |  TOT  |     15     | :white_check_mark: |
## 3. Application :
* #### 3.1 Description
   
* #### 3.2 Installation
    * 
    * 
* #### 3.3 Usage
    * To run the application enter the following command in your terminal `python main.py` 
    * If the server is running, it will invite you to go to http://172.0.0.3:5000/
* #### 3.4 Testing
    * To perfom test you need to have pytest , If not please enter the following command line in your terminal `pip install pytest`
    * To start test, enter in your terminal the following command line  `pytest test.py` for all the functionnalities
## 4. Vagrant :
* #### 4.1 Description
  
* #### 4.2 Installation

* #### 4.3 Usage
    * 
* #### 4.4 Testing
    * 
* #### 4.5 Content
    *
## 5. Docker and Docker compose :
* #### 5.1 Description
Docker is an open source software that allows you to launch applications in software containers. 
The docker-compose build the dockerfile in the repository. 
* #### 5.2 Installation

* #### 5.3 Usage
Run 'Docker-compose up -d' to build and run the application. 
You can find it on the address '127.0.0.1:80/hello' in your browser. 
To stop the service, you only have to do 'docker-compose stop'
To remove all the daata and the previous services, you have to do 'docker-compose down' It will erase all the data. 
* #### 5.4 Kubernet
K8s folder contains all the file for kubernet to be run in minikube. 
## 6. Tool integreted :
* #### 6.1 CI/CD with Github and Gihub Action 
 

