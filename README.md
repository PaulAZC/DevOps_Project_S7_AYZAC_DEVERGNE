## DevOps Project for the semester 7
## Authors : Paul AYZAC & Noémie DEVERGNE
## Links to the content of our project :
- [DevOps Project for the semester 7](#devops-project-for-the-semester-7)
- [Authors : Paul AYZAC & Noémie DEVERGNE](#authors--paul-ayzac--noémie-devergne)
- [Links to the content of our project :](#links-to-the-content-of-our-project-)
- [1. Description :](#1-description-)
- [2. Grades :](#2-grades-)
- [3. Run th application :](#3-run-th-application-)
- [4. IaC :](#4-iac-)
- [5. Docker and Docker compose :](#5-docker-and-docker-compose-)
- [6. Kubernetes](#6-kubernetes)
- [7. Istio and monitoring](#7-istio-and-monitoring)
- [8. Bonus](#8-bonus)

## 1. Description :
The aim of this project will be to use all the tools seen in class within the same project. It will highlight a CRUD application.
The project consists of the **creation of a web application** on any programming language, storing data in a database and cover it with tests of different levels. 
For our web application, we decided to program it in **python**, and we stored the datas in a **postgres** database. 
In this project, we used different technologies as : 
    - CI/CD
    - Vagrant
    - Docker
    - Docker Compose
    - Kubernetes
    - Istio
    - Kiali
    - Prometheus

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
## 3. Run th application :
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
## 4. IaC :

## 5. Docker and Docker compose :
* #### 5.1 Description 
  * ##### Docker 
  * Docker, a subset of the Moby project, is a software framework for building, running, and managing containers on servers and the cloud.
  
  * ##### Docker compose
  * Docker Compose is a tool that was developed to help define and share multi-container applications. 
  * With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.

## 6. Kubernetes
* #### 6.1 Description
  * Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.

## 7. Istio and monitoring
* ### 7.1 Istio
  
* #### 7.1.1 Description 
  * Istio is an open source Service Mesh platform that controls how data is shared between microservices. 
  * It includes APIs that allow Istio to be integrated with any type of logging platform, telemetry or policy system. 
  
* #### 7.1.2 Installation 
  * To install Istio, we downloaded the Istio Windows's file: `https://github.com/istio/istio/releases/tag/1.12.1`
  * We followed the installation guide `https://istio.io/latest/docs/setup/getting-started/`
  * We applied **fichiers.yaml** file to deploy a service and the **gateway.yaml** to delpoy the gateway, destination rule and the virtual service.
  
  * To deploy Kiali dashboard, we do 
  * ```kubectl apply -f samples/addons``` to deploy prometheus and grafana in our app.
  * ```kubectl rollout status deployment/kiali -n istio-system```
  * ```istioctl dashboard kiali``` to run kiali.

* ### 7.2 Monitoring
  
  * #### 7.2.1 Description 
  * ##### Prometheus 
  * Prometheus is an **open source monitoring system** and time series database. 
  * You can use Prometheus with Istio to record metrics that track the health of Istio and of applications within the service mesh. 

  * ##### Grafana
  * Grafana is an **open source monitoring solution** that can be used to configure dashboards for Istio. 
  * You can use Grafana to monitor the health of Istio and of applications within the service mesh.

  * #### 7.2.2 Installation 
  * To install prometheus, we run the follwing command line : 
    ```kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/prometheus.yaml```
  * To install grafana, we run the follwing command line : 
    ```kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/grafana.yaml```

  * In the prometheus' .yaml file, we added a part of code to declare our app as a job for prometheus that it will track the helth of the app. 

    ```- job_name: "devops static_configs: - targets: ["localhost:5000"]```
  
  * Then we opened `localhost:9090` to see prometheus page. 

## 8. Bonus

