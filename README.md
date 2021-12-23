## DevOps Project for the semester 7
## Authors : Paul AYZAC & Noémie DEVERGNE
## Links to the content of our project :
- [1. Description of the project](#1-description-)
- [2. Grades](#2-grades-)
- [3. CICD](#3-cicd-)
- [4. Run the application](#3-application-)
- [5. IaC](#4-vagrant-)
- [6. Docker and Docker compose](#5-docker-and-docker-compose-)
- [7. Kubernetes](#6-kubernetes-)
- [8. Istio and monitoring](#7-istio-and-monitoring-)
- [9. Bonus :](#8-bonus-)

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
| Continuous Integration and Continuous Delivery (and Deployment) |  CICD |    +2.5    | :white_check_mark: |
| Containerisation with Docker                                    |  D    |     +1     | :white_check_mark: |
| Orchestration with Docker Compose                               |  DC   |     +2     | :white_check_mark: |
| Orchestration with Kubernetes                                   |  KUB  |     +2     | :white_check_mark: |
| Service mesh using Istio                                        |  IST  |    +1.5    | :white_check_mark: |
| Infrastructure as code using Ansible                            |  IAC  |     +2     | :white_check_mark: |
| Monitoring                                                      |  MON  |    +0.5    | :white_check_mark: |
| Accurate project documentation in README.md file                |  DOC  |     +3     | :white_check_mark: |
| Use of the python-flask language for the application            |  BNS  |     +1     | :white_check_mark: |
| Using PostgreSQL for the application                            |  BNS  |     +1     | :white_check_mark: |
| Sentry implementation for monitoring                            |  BNS  |     +1     | :white_check_mark: |
| Total point                                                     |  TOT  |    18.5    | :white_check_mark: |
## 3. CICD
* #### 3.1 Python test in test.py and test-pass.py
    We realised unit test in python to check the database connection, all the test was checked before a push with github action using the .github/workflows folder but we used after the environment varible the test-pass.py file to check on push to preserve the integrity of our application and to don't create an other postgres server.
* #### CICD with github action and heroku
    We used github action for this part, on each push github action will test our app with the unit tests that we describe below and block the deployement if it was not working. After the deployment, we tryed to deploy the app on heroku and the build of the app was good but we didn't know why our deployment was not working so that is why we put 2.5 points instead of 3. You can check our deployment on this [link](https://devopsprojecteceparis.herokuapp.com/)
## 4. Run th application :
* #### 4.1 Description of the app
    This CRUD application is a very simple To do list coding in python with flask and based on a PostgreSQL database. In this application, we can add a task on the `/todo` page and see all the tasks in the `/todoList` page.
* #### 4.2 Installation
    * To install the application, first you have to clone the repo using this command line :
        ```
        git clone https://github.com/PaulAZC/DevOps_Project_S7_AYZAC_DEVERGNE
        cd DevOps_Project_S7_AYZAC_DEVERGNE
        ```
    * Once you did it, make sure you have installed **python** on your computer using [this site](https://www.python.org/downloads/) and install PostgreSQL on [this link](https://www.postgresql.org/download/).
    * After that, lets download all the dependancies with the following command lines using pip :
        ``` 
        pip install -r requirements.txt
        ```
    * The next step is to set all the environment variable with the following lines :
        * `cd DevOps_Project_S7_AYZAC_DEVERGNE/userapi`
        * `$Env: DATABASE_NAME=YOUR_DATABASE_NAME`
        * `$Env: DATABASE_USER=YOUR_DATABASE_USERNAME`
        * `$Env: DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD`
        * `$Env: DATABASE_HOST=YOUR_DATABASE_HOST_IP`
        * `$Env: DATABASE_PORT=YOUR_DATABASE_PORT`
        * PS: For **linux**, use `export` instead of `$Env`
* #### 3.4 Run it and test it !
    * Finally, you can run the app with the command :
        ``` 
        cd DevOps_Project_S7_AYZAC_DEVERGNE/userapi
        #For windows:
        python main.py
        #For linux:
        python3 main.py
        ```
        It will run on the **localhost:5000** page

    * And the tests with the command lines :
        ``` 
        cd DevOps_Project_S7_AYZAC_DEVERGNE/userapi
        pytest test.py
        ```
## 5. IaC :
* #### 5.1 IaC description
    The IaC (Infrastructure as Code) part corresponds to the virtualization of the application with a virtual machine using Vagrant and Ansible which will be used to implement the various features of the application.
* #### 5.2 Installation
    Make sure you installed [Vagrant](https://www.vagrantup.com/downloads), [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) and [Virtualbox](https://www.virtualbox.org/) to use the virtual machine. If you didn't, just click on the link of each technologies below.
* #### 5.3 Run it
    To setup the virtual machine use the following commands : 
    ```
    cd iac
    vagrant up
    vagrant ssh 
    ```
    You can see what is inside the vm with the `vagrant ssh` command. You can access to the app on the **http://localhost:8080/hello** page.
    During the setup, we used Ansible to provide all our provision like the **language run time**, the **database** and **application**.
    PS: We didn't check the app and finalise the database so that is why we marked it as 1.5 points.
## 6. Docker and Docker compose :
* First, make sure you installed [docker](https://docs.docker.com/get-docker/).
* ##### 6.1 Docker 
    * Docker, a subset of the Moby project, is a software framework for building, running, and managing containers on servers and the cloud.
    * You can run it with the commands :
    ```
    cd DevOps_Project_S7_AYZAC_DEVERGNE
    docker build -t pyapp .
    docker run -p 5000:5000 pyapp
    ```
    You will access to the site in the **localhost:5000** page.
* ##### 6.2 Docker compose
    * Docker Compose is a tool that was developed to help define and share multi-container applications. 
    * With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.
    * To run it, make sure you builded the docker image with the commands below (or change the code to use the paulazc/pyapp-devops-project image) :
    ```
    cd DevOps_Project_S7_AYZAC_DEVERGNE
    docker-compose build
    docker-compose up
    ```
    You will access to the site in the **localhost:5000** page like docker.
## 7. Kubernetes
* #### 7.1 Description and installation
    * Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.
    * Make sure you installed [minikube](https://kubernetes.io/fr/docs/tasks/tools/install-minikube/)
* #### 7.2 Use it
    * To run it, you just have to follow these command lines :
    ``` 
    cd k8s
    minikube start
    #For each files in the k8s folder
    kubectl create -f <file name>
    ```

    
## 8. Istio and monitoring
* ### 8.1 Istio
  
* #### 8.1.1 Description 
  * Istio is an open source Service Mesh platform that controls how data is shared between microservices. 
  * It includes APIs that allow Istio to be integrated with any type of logging platform, telemetry or policy system. 
  
* #### 8.1.2 Installation 
  * To install Istio, we downloaded the Istio Windows's file: `https://github.com/istio/istio/releases/tag/1.12.1`
  * We followed the installation guide `https://istio.io/latest/docs/setup/getting-started/`
  * We applied **fichiers.yaml** file to deploy a service and the **gateway.yaml** to delpoy the gateway, destination rule and the virtual service.
  
  * To deploy Kiali dashboard, we do 
  * ```kubectl apply -f samples/addons``` to deploy prometheus and grafana in our app.
  * ```kubectl rollout status deployment/kiali -n istio-system```
  * ```istioctl dashboard kiali``` to run kiali.
* ### 8.2 Monitoring
  * #### 8.2.1 Description 
  * ##### Prometheus 
  * Prometheus is an **open source monitoring system** and time series database. 
  * You can use Prometheus with Istio to record metrics that track the health of Istio and of applications within the service mesh. 

  * ##### Grafana
  * Grafana is an **open source monitoring solution** that can be used to configure dashboards for Istio. 
  * You can use Grafana to monitor the health of Istio and of applications within the service mesh.

  * #### 8.2.2 Installation 
  * To install prometheus, we run the follwing command line : 
    ```kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/prometheus.yaml```
  * To install grafana, we run the follwing command line : 
    ```kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.12/samples/addons/grafana.yaml```

  * In the prometheus' .yaml file, we added a part of code to declare our app as a job for prometheus that it will track the helth of the app. 

    ```- job_name: "devops static_configs: - targets: ["localhost:5000"]```
  
  * Then we opened `localhost:9090` to see prometheus page.  
## 9. Bonus
* #### 9.1 CRUD app
    To code this application, we only used the python language importing flask to create the app and this one was based on the PostgreSQL database.
* #### 9.2 Sentry for the monitoring
    For a little monitoring and debug of our app, we used a new technologie called sentry that detect the errors of the application and show some metrics about the speed of our app, etc...
    * To use it, register on the [sentry site](https://sentry.io/), it's free !
    * After that, create a flask project, go to your settings and take your **dsn** that you have on the tuto when you create the project.
    * Run these commands : 
    ``` 
    cd DevOps_Project_S7_AYZAC_DEVERGNE/userapi
    pip install --upgrade 'sentry-sdk[flask]'
    ```
    Then on the **main.py** file paste your dsn on the line **14** and go back to your project and that's it ! Your can monitor your app. 

