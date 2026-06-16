# manufacturing_tb

This package has be created automatically using the [RosTooling](https://github.com/ipa320/RosTooling).


It holds the launch file to run the following nodes:
- robot_state_publisher
- joint_state_publisher_gui
- bt_navigator
- relay
- gazebo
- gazebo_sensor_B1_controller
- gazebo_sensor_B4_controller
- planar_move
- gazebo_ros_joint_state_publisher
- laserscan_multi_merger
- transform_listener_impl_63dab121a590
- transform_listener_impl_586cb636ca10
- map_server
- amcl
- controller_server
- planner_server
- transform_listener_impl_62307b87cbb0
- behavior_server
- transform_listener_impl_591884f5efa0
- bt_navigator
- bt_navigator_navigate_to_pose
- bt_navigator_navigate_through_poses
- robot_state_publisher
- robot_description_publisher
- rviz
- transform_listener_impl_5f3f2f2aa6c0
- static_transform_publisher_vS7Rn4YQfVmDReBi
- static_transform_publisher_BB3LgctvQJmC8ZBZ
- static_transform_publisher_rk0xEkSw7GX3BxqV
- global_costmap/global_costmap
- local_costmap/local_costmap
- lifecycle_manager_navigation

The listed nodes offer the following connections:
- Publisher: robot_description [std_msgs/String]
- Publisher: tf [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Subscriber: clock [rosgraph_msgs/Clock]
- Subscriber: kmriiwa/arm/joint_states [sensor_msgs/JointState]
- Publisher: kmriiwa/arm/joint_states [sensor_msgs/JointState]
- Subscriber: clock [rosgraph_msgs/Clock]
- Subscriber: robot_description [std_msgs/String]
- Publisher: bt_navigator/transition_event [lifecycle_msgs/TransitionEvent]
- ServiceServer: bt_navigator/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: bt_navigator/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: bt_navigator/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: bt_navigator/get_state [lifecycle_msgs/GetState]
- ServiceServer: bt_navigator/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Publisher: cmd_vel [geometry_msgs/Twist]
- Subscriber: kmriiwa/base/command/cmd_vel [geometry_msgs/Twist]
- Publisher: clock [rosgraph_msgs/Clock]
- Publisher: performance_metrics [gazebo_msgs/PerformanceMetrics]
- Subscriber: sub_clock [rosgraph_msgs/Clock]
- ServiceServer: pause_physics [std_srvs/Empty]
- ServiceServer: reset_simulation [std_srvs/Empty]
- ServiceServer: reset_world [std_srvs/Empty]
- ServiceServer: unpause_physics [std_srvs/Empty]
- Publisher: kmriiwa/base/state/LaserB1Scan [sensor_msgs/LaserScan]
- Subscriber: clock [rosgraph_msgs/Clock]
- Publisher: kmriiwa/base/state/LaserB4Scan [sensor_msgs/LaserScan]
- Subscriber: clock [rosgraph_msgs/Clock]
- Publisher: odom [nav_msgs/Odometry]
- Publisher: tf [tf2_msgs/TFMessage]
- Subscriber: clock [rosgraph_msgs/Clock]
- Subscriber: cmd_vel [geometry_msgs/Twist]
- Publisher: joint_states [sensor_msgs/JointState]
- Subscriber: clock [rosgraph_msgs/Clock]
- Publisher: merged_cloud [sensor_msgs/PointCloud2]
- Publisher: scan_multi [sensor_msgs/LaserScan]
- Subscriber: kmriiwa/base/state/LaserB1Scan [sensor_msgs/LaserScan]
- Subscriber: kmriiwa/base/state/LaserB4Scan [sensor_msgs/LaserScan]
- Subscriber: tf [tf2_msgs/TFMessage]
- Subscriber: tf_static [tf2_msgs/TFMessage]
- Subscriber: tf [tf2_msgs/TFMessage]
- Subscriber: tf_static [tf2_msgs/TFMessage]
- Publisher: bond [bond/Status]
- Publisher: map [nav_msgs/OccupancyGrid]
- Publisher: map_server/transition_event [lifecycle_msgs/TransitionEvent]
- Subscriber: sub_bond [bond/Status]
- ServiceServer: map_server/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: map_server/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: map_server/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: map_server/get_state [lifecycle_msgs/GetState]
- ServiceServer: map_server/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: map_server/load_map [nav2_msgs/LoadMap]
- ServiceServer: map_server/map [nav_msgs/GetMap]
- Publisher: amcl/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: amcl_pose [geometry_msgs/PoseWithCovarianceStamped]
- Publisher: bond [bond/Status]
- Publisher: particle_cloud [nav2_msgs/ParticleCloud]
- Publisher: tf [tf2_msgs/TFMessage]
- Subscriber: sub_bond [bond/Status]
- Subscriber: initialpose [geometry_msgs/PoseWithCovarianceStamped]
- Subscriber: map [nav_msgs/OccupancyGrid]
- Subscriber: scan_multi [sensor_msgs/LaserScan]
- ServiceServer: amcl/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: amcl/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: amcl/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: amcl/get_state [lifecycle_msgs/GetState]
- ServiceServer: amcl/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: reinitialize_global_localization [std_srvs/Empty]
- ServiceServer: request_nomotion_update [std_srvs/Empty]
- ServiceServer: set_initial_pose [nav_msgs/SetInitialPose]
- Publisher: bond [bond/Status]
- Publisher: controller_server/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: kmriiwa/base/command/cmd_vel [geometry_msgs/Twist]
- Publisher: trajectories [visualization_msgs/MarkerArray]
- Publisher: transformed_global_plan [nav_msgs/Path]
- Subscriber: sub_bond [bond/Status]
- Subscriber: odom [nav_msgs/Odometry]
- Subscriber: speed_limit [nav2_msgs/SpeedLimit]
- ActionServer: follow_path [nav2_msgs/FollowPath]
- ServiceServer: controller_server/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: controller_server/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: controller_server/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: controller_server/get_state [lifecycle_msgs/GetState]
- ServiceServer: controller_server/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Publisher: bond [bond/Status]
- Publisher: plan [nav_msgs/Path]
- Publisher: planner_server/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: unsmoothed_plan [nav_msgs/Path]
- Subscriber: sub_bond [bond/Status]
- ActionServer: compute_path_through_poses [nav2_msgs/ComputePathThroughPoses]
- ActionServer: compute_path_to_pose [nav2_msgs/ComputePathToPose]
- ServiceServer: is_path_valid [nav2_msgs/IsPathValid]
- ServiceServer: planner_server/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: planner_server/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: planner_server/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: planner_server/get_state [lifecycle_msgs/GetState]
- ServiceServer: planner_server/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Subscriber: tf [tf2_msgs/TFMessage]
- Subscriber: tf_static [tf2_msgs/TFMessage]
- Publisher: behavior_server/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: bond [bond/Status]
- Publisher: cmd_vel [geometry_msgs/Twist]
- Subscriber: sub_bond [bond/Status]
- Subscriber: local_costmap/costmap_raw [nav2_msgs/Costmap]
- Subscriber: local_costmap/published_footprint [geometry_msgs/PolygonStamped]
- ActionServer: backup [nav2_msgs/BackUp]
- ActionServer: drive_on_heading [nav2_msgs/DriveOnHeading]
- ActionServer: spin [nav2_msgs/Spin]
- ActionServer: wait [nav2_msgs/Wait]
- ServiceServer: behavior_server/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: behavior_server/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: behavior_server/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: behavior_server/get_state [lifecycle_msgs/GetState]
- ServiceServer: behavior_server/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Subscriber: tf [tf2_msgs/TFMessage]
- Subscriber: tf_static [tf2_msgs/TFMessage]
- Publisher: bt_navigator/transition_event [lifecycle_msgs/TransitionEvent]
- ServiceServer: bt_navigator/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: bt_navigator/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: bt_navigator/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: bt_navigator/get_state [lifecycle_msgs/GetState]
- ServiceServer: bt_navigator/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Publisher: behavior_tree_log [nav2_msgs/BehaviorTreeLog]
- ActionClient: backup [nav2_msgs/BackUp]
- ActionClient: compute_path_to_pose [nav2_msgs/ComputePathToPose]
- ActionClient: follow_path [nav2_msgs/FollowPath]
- ActionClient: spin [nav2_msgs/Spin]
- ActionClient: wait [nav2_msgs/Wait]
- Publisher: behavior_tree_log [nav2_msgs/BehaviorTreeLog]
- ActionClient: backup [nav2_msgs/BackUp]
- ActionClient: compute_path_through_poses [nav2_msgs/ComputePathThroughPoses]
- ActionClient: follow_path [nav2_msgs/FollowPath]
- ActionClient: spin [nav2_msgs/Spin]
- ActionClient: wait [nav2_msgs/Wait]
- Publisher: robot_description [std_msgs/String]
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: robot_description [std_msgs/String]
- Publisher: clock [tf2_msgs/TFMessage]
- Subscriber: joint_states [sensor_msgs/JointState]
- Publisher: clicked_point [geometry_msgs/PointStamped]
- Publisher: initialpose [geometry_msgs/PoseWithCovarianceStamped]
- Publisher: move_base_simple/goal [geometry_msgs/PoseStamped]
- Subscriber: global_costmap/costmap [nav_msgs/OccupancyGrid]
- Subscriber: global_costmap/costmap_updates [map_msgs/OccupancyGridUpdate]
- Subscriber: kmriiwa/base/state/LaserB1Scan [sensor_msgs/LaserScan]
- Subscriber: kmriiwa/base/state/LaserB4Scan [sensor_msgs/LaserScan]
- Subscriber: kmriiwa/base/state/odom [nav_msgs/Odometry]
- Subscriber: kmriiwa/robot_description [std_msgs/String]
- Subscriber: plan [nav_msgs/Path]
- Subscriber: received_global_plan [nav_msgs/Path]
- Subscriber: scan_multi [sensor_msgs/LaserScan]
- Subscriber: transformed_global_plan [nav_msgs/Path]
- Subscriber: tf [tf2_msgs/TFMessage]
- Subscriber: tf_static [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: tf_static [tf2_msgs/TFMessage]
- Publisher: costmap [nav_msgs/OccupancyGrid]
- Publisher: costmap_raw [nav2_msgs/Costmap]
- Publisher: costmap_updates [map_msgs/OccupancyGridUpdate]
- Publisher: global_costmap/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: published_footprint [geometry_msgs/PolygonStamped]
- Subscriber: footprint [geometry_msgs/Polygon]
- ServiceServer: clear_around_global_costmap [nav2_msgs/ClearCostmapAroundRobot]
- ServiceServer: clear_entirely_global_costmap [nav2_msgs/ClearEntireCostmap]
- ServiceServer: clear_except_global_costmap [nav2_msgs/ClearCostmapExceptRegion]
- ServiceServer: get_costmap [nav2_msgs/GetCostmap]
- ServiceServer: global_costmap/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: global_costmap/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: global_costmap/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: global_costmap/get_state [lifecycle_msgs/GetState]
- ServiceServer: global_costmap/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Publisher: costmap [nav_msgs/OccupancyGrid]
- Publisher: costmap_raw [nav2_msgs/Costmap]
- Publisher: costmap_updates [map_msgs/OccupancyGridUpdate]
- Publisher: local_costmap/transition_event [lifecycle_msgs/TransitionEvent]
- Publisher: published_footprint [geometry_msgs/PolygonStamped]
- Subscriber: footprint [geometry_msgs/Polygon]
- ServiceServer: clear_around_local_costmap [nav2_msgs/ClearCostmapAroundRobot]
- ServiceServer: clear_entirely_local_costmap [nav2_msgs/ClearEntireCostmap]
- ServiceServer: clear_except_local_costmap [nav2_msgs/ClearCostmapExceptRegion]
- ServiceServer: get_costmap [nav2_msgs/GetCostmap]
- ServiceServer: local_costmap/change_state [lifecycle_msgs/ChangeState]
- ServiceServer: local_costmap/get_available_states [lifecycle_msgs/GetAvailableStates]
- ServiceServer: local_costmap/get_available_transitions [lifecycle_msgs/GetAvailableTransitions]
- ServiceServer: local_costmap/get_state [lifecycle_msgs/GetState]
- ServiceServer: local_costmap/get_transition_graph [lifecycle_msgs/GetAvailableTransitions]
- Publisher: bond [bond/Status]
- Publisher: diagnostics [diagnostic_msgs/DiagnosticArray]
- Subscriber: sub_bond [bond/Status]
- ServiceServer: lifecycle_manager_navigation/is_active [std_srvs/Trigger]
- ServiceServer: lifecycle_manager_navigation/manage_nodes [nav2_msgs/ManageLifecycleNodes]

## Installation

### Using release

This package can be copied to a valid ROS 2 workspace. To be sure that all the related dependencies are intalles the command **rosdep install** can be used.
Then the workspace must be compiled using the common ROS 2 build command:

```
mkdir -p ros2_ws/src
cd ros2_ws/
cp -r PATHtoTHISPackage/manufacturing_tb src/.
rosdep install --from-path src/ -i -y
colcon build
source install/setup.bash
```



## Usage


To execute the launch file, the following command can be called:

```
ros2 launch manufacturing_tb manufacturing_tb.launch.py 
```

The generated launch files requires the xterm package, it can be installed by:

```
sudo apt install xterm
```



