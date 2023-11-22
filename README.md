# CS_ros2model_TBs

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

This repository holds models based on the [RosTooling](https://github.com/ipa320/RosTooling) extracted automatically using introspection tools on the TesBeds systems.

Technical Maintainer: [**ipa-nhg**](https://github.com/ipa-nhg/) (**Nadia Hammoudeh Garcia**, **Fraunhofer IPA**) - **nadia.hammoudeh.garcia@ipa.fraunhofer.de**

The code is compatible with the verison 2.0. of the RosTooling, publicly available under [RosTooling v2](https://github.com/ipa320/RosTooling/tree/master).

The models were automatically created using the following commands:

```
$ cd YourRos2WS/src
$ git clone git@github.com:ipa-nhg/ros2model.git -b RosToolingSeronetVersion
$ cd YourRos2WS
$ colcon build
$ mkdir ~/modelsToNHG
$ ros2 model running_node -ga -d ~/modelsToNHG
```
