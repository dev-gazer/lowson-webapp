# Lowson-Webapp (Version 1.0)

As estimator of airfoil turbulent inflow noise based on the owner PhD's study.

You can access this version if you like. It is actively running on an AWS EC2 Instance.
http://ec2-54-167-116-126.compute-1.amazonaws.com:8888/

### It will appear something like:
(I know, I know, I need to expend more time on css.)
![alt text](https://github.com/martuscellifaria/lowson_webapp/blob/master/Captura%20de%20tela%20de%202021-04-16%2018-27-56.png)



### Installation
##### Prerequisites
- [Docker]
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

##### Clone the project

```sh
$ git clone https://github.com/martuscellifaria/lowson_webapp.git
```


##### Go to the folder
```sh
$ cd lowson_webapp
```

##### Build the Docker image
```sh
$ sudo docker build -t lowson_webapp .
```

##### Run the Docker image
```sh
$ sudo docker run -it -p 5000:5000 --rm lowson_webapp bin/bash
```

##### Access through your browser
```sh
http://0.0.0.0:5000/
```

### How to use
There you'll have the several inputs to calculate turbulent inflow noise such as airfoil geometric aspects, flow conditions and distance from source and receiver. The output is a self updateable plot that estimates the sound spectrum (sound pressure level) along an audible frequency range.

### Contact
Any questions, you may see at the About section of the Web Application a few contacts like my e-mail (martuscellifaria@gmail.com) or my research group website (https://sites.usp.br/poli-wind/), where you will find information about any of Poli Wind members and our research.