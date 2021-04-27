# Python-Example-Code
Some of my Python projects throughout the years.

My first encounter with Python were in the early stages of my bachelor thesis were me and my group had the task of creating an automates sea vessel (ASV) for an national competition, Autodrone. My main focus of this were on creating the ASV's "eyes" so it could detect the different obstacles throughout the course. Due to the Covid-19 outbreak the competition were cancelled and the schools shut down. This lead to us moving away from an physical ASV and rather create an simulated one. Thus, only providing pieces of an fully operational ASV.

I first started with OpenCV in Python on an Nvidia Jetson TX2 using Linux. Here I worked on creating an object detection algorithm, which soon got scrapped due to other interests for the project. This lead me to create an program that simply could collect images for machine learning, dataCollection.py.

In the dataCollection.py my goal were to use an ZED 2 Camera to simply collect images later used for machine learning. 
The task were to collect images of three different buoys, yellow, red and green. And to save additionaly work, automaticly store them in each folder 
with a name corresponding to their color and an number.
This were done using the OpenCV libary. 
