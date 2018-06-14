# rps-cv-ros
Rock Paper Scissors on ROS

# How To Use
This is intende to be used with ROS.<br />
Input is a image of the gesture to be recognized.<br />
Output is three strings, the result, the gesture recognized (of the human player), and the gesture randomly selected (for the robot).<br />

### Setting
Five elements can be set using the `setting.py` file. They are: 
* subscriberTopic: The topic where this ROS node gets information (the picture) from.
* talkerTopic: The topic where this ROS node will publish information (the results) to.
* cameraNum: The camera number which the program will call to use the camera (for capturing new images).
* pubRobotResult: Whether or not to publish the result of the robot to the topic.
* pubHumanResult: Whether or not to publish the result of the human player to the topic.
