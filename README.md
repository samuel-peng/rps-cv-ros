# rps-cv-ros
Rock Paper Scissors game on ROS using machine learning.
Based on rps-cv by Julien de la Bruère-Terreault (drgfreeman@tuta.io)

# How To Use
This is intende to be used with ROS.<br />
Input a image of the gesture to be recognized.<br />
Output three strings, the result, the gesture recognized (human player), and the gesture randomly selected (the robot).<br />
Use after the following steps are correctly done:

### Dependencies

The project depends on and has been tested with the following libraries:

* OpenCV 3.3.0 with bindings for Python 3*
* Python 3.4+
* Numpy 1.13.0
* Scikit-Learn 0.18.2
* Scikit-Image 0.13.0
* Pygame 1.9.3

### Setting
Five elements can be set using the `setting.py` file. They are: 
* subscriberTopic: The topic where this ROS node gets information (the picture) from.
* talkerTopic: The topic where this ROS node will publish information (the results) to.
* cameraNum: The camera number which the program will call to use the camera (for capturing new images).
* pubRobotResult: Whether or not to publish the result of the robot to the topic.
* pubHumanResult: Whether or not to publish the result of the human player to the topic.

### Training
#### Samples
To use, first train the program with the pictures. Existing pictures can be used for training, but new pictures captured using `capture.py` is preferred. Run `capture.py` to capture sample images.
#### Train
After getting the samples, run `train.py` to generate the pattern file. Notice that the program has a relatively high requirement for memory and CPU. Processing too many samples may cause computer crash.
