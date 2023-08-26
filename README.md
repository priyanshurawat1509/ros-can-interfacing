# ros-can-interfacing (deeporange14_control Package)

# Deep Orange DBW Controls Interface Package for Autonomous Driving

### Functionality:

- DeepOrangeDbwCan.cpp: Enable passing the ROS topics to the Raptor DBW controller via SocketCAN, which executes the commands for the platform to move. Additionally monitors rtk fix, logging status
- VelocityController.cpp: Use the vehicle dynamics model to convert vehicle velocity to left and right track velocity/torques.
- StateMachine.cpp: A ROS state machine in sync with the Raptor controller state machine.
- RosHealthMonitor.cpp: A node that Monitor health of raptor hanshake, brake acknowledgement from raptor , autonomy stack fault and dbw ros mode
- DataLoggerNode.cpp: logging CAN and ROS data while monitoring logging status active or Fail
- Node.cpp - Instantiates the three objects in a single node (as of now).

### How to Use:
- To add/update CAN msg IDs- update these in the dbc in the `dbc` folder as well as `dispatch_can_msgs.h` include file
- Vehicle and subsystem states are enumerated in `DeeporangeStateEnums.h`


### Dependencies:
- `can_dbc_parser`: Developed by New Eagle as part of metapackage - https://github.com/NewEagleRaptor/raptor-dbw-ros
- `deeporange14_msgs` : Package for custom messages for DO13 DBW operation
- `socketcan_bridge` : Package for interfacing CAN to ROS on Linux - https://github.com/ros-industrial/ros_canopen
- `can_msgs` : Package to support CAN msg format on ROS topics. - https://github.com/ros-industrial/ros_canopen
- rosdep install --from-paths src --ignore-src -r -y
- 
https://user-images.githubusercontent.com/83747696/218282545-b7866018-1204-43ab-95dd-8d5529b7f709.mp4

https://user-images.githubusercontent.com/83747696/218282768-7146f018-bf9b-4c82-bbcd-ebd90121e420.mp4

