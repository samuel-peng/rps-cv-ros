# rps-cv-ros
Rock Paper Scissors on ROS

# How To Use
This is intende to be used with ROS.<br />
Input a image of the gesture to be recognized.<br />
Output three strings, the result, the gesture recognized (human player), and the gesture randomly selected (the robot).<br />

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
