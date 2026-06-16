import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  frame_prefix_arg = DeclareLaunchArgument(
    "frame_prefix", default_value=TextSubstitution(text="")
  )
  ld.add_action(frame_prefix_arg)
  ignore_timestamp_arg = DeclareLaunchArgument(
    "ignore_timestamp", default_value=TextSubstitution(text="false")
  )
  ld.add_action(ignore_timestamp_arg)
  publish_frequency_arg = DeclareLaunchArgument(
    "publish_frequency", default_value=TextSubstitution(text="20.0")
  )
  ld.add_action(publish_frequency_arg)
  use_sim_time_arg = DeclareLaunchArgument(
    "use_sim_time", default_value=TextSubstitution(text="true")
  )
  ld.add_action(use_sim_time_arg)
  joint_state_publisher_gui_config = os.path.join(
    get_package_share_directory('manufacturing_tb'),
    'config',
    'joint_state_publisher_gui.yaml'
  )
  enable_performance_metrics_arg = DeclareLaunchArgument(
    "enable_performance_metrics", default_value=TextSubstitution(text="true")
  )
  ld.add_action(enable_performance_metrics_arg)
  publish_rate_arg = DeclareLaunchArgument(
    "publish_rate", default_value=TextSubstitution(text="10.0")
  )
  ld.add_action(publish_rate_arg)
  use_sim_time_arg = DeclareLaunchArgument(
    "use_sim_time", default_value=TextSubstitution(text="true")
  )
  ld.add_action(use_sim_time_arg)
  use_sim_time_arg = DeclareLaunchArgument(
    "use_sim_time", default_value=TextSubstitution(text="true")
  )
  ld.add_action(use_sim_time_arg)
  static_transform_publisher_vS7Rn4YQfVmDReBi_config = os.path.join(
    get_package_share_directory('manufacturing_tb'),
    'config',
    'static_transform_publisher_vS7Rn4YQfVmDReBi.yaml'
  )
  static_transform_publisher_BB3LgctvQJmC8ZBZ_config = os.path.join(
    get_package_share_directory('manufacturing_tb'),
    'config',
    'static_transform_publisher_BB3LgctvQJmC8ZBZ.yaml'
  )

  # *** ROS 2 nodes ***
  robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="robot_state_publisher",
    remappings=[
      ("robot_description", "robot_description"),
      ("tf", "tf"),
      ("tf_static", "tf_static"),
      ("clock", "clock"),
      ("kmriiwa/arm/joint_states", "kmriiwa/arm/joint_states")]
    ,
    parameters=[{
    "frame_prefix": LaunchConfiguration("frame_prefix"),
    "ignore_timestamp": LaunchConfiguration("ignore_timestamp"),
    "publish_frequency": LaunchConfiguration("publish_frequency"),
    "use_sim_time": LaunchConfiguration("use_sim_time"),}]
  )
  joint_state_publisher_gui = Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui",
    prefix = 'xterm -e',
    output='screen',
    name="joint_state_publisher_gui",
    remappings=[
      ("kmriiwa/arm/joint_states", "kmriiwa/arm/joint_states"),
      ("clock", "clock"),
      ("robot_description", "robot_description")]
    ,
    parameters = [joint_state_publisher_gui_config]
  )
  bt_navigator = Node(
    package="nav2_bt_navigator",
    executable="bt_navigator",
    prefix = 'xterm -e',
    output='screen',
    name="bt_navigator",
    remappings=[
      ("bt_navigator/transition_event", "bt_navigator/transition_event"),
      ("bt_navigator/change_state", "bt_navigator/change_state"),
      ("bt_navigator/get_available_states", "bt_navigator/get_available_states"),
      ("bt_navigator/get_available_transitions", "bt_navigator/get_available_transitions"),
      ("bt_navigator/get_state", "bt_navigator/get_state"),
      ("bt_navigator/get_transition_graph", "bt_navigator/get_transition_graph")]
  )
  relay = Node(
    package="topic_tools",
    executable="relay",
    prefix = 'xterm -e',
    output='screen',
    name="relay",
    remappings=[
      ("cmd_vel", "cmd_vel"),
      ("kmriiwa/base/command/cmd_vel", "kmriiwa/base/command/cmd_vel")]
  )
  gazebo = Node(
    package="gazebo",
    executable="gazebo",
    prefix = 'xterm -e',
    output='screen',
    name="gazebo",
    remappings=[
      ("clock", "clock"),
      ("performance_metrics", "performance_metrics"),
      ("clock", "sub_clock"),
      ("pause_physics", "pause_physics"),
      ("reset_simulation", "reset_simulation"),
      ("reset_world", "reset_world"),
      ("unpause_physics", "unpause_physics")]
    ,
    parameters=[{
    "enable_performance_metrics": LaunchConfiguration("enable_performance_metrics"),
    "publish_rate": LaunchConfiguration("publish_rate"),
    "use_sim_time": LaunchConfiguration("use_sim_time"),}]
  )
  gazebo_sensor_B1_controller = Node(
    package="gazebo_sensor_b1_controller",
    executable="gazebo_sensor_B1_controller",
    prefix = 'xterm -e',
    output='screen',
    name="gazebo_sensor_B1_controller",
    remappings=[
      ("kmriiwa/base/state/LaserB1Scan", "kmriiwa/base/state/LaserB1Scan"),
      ("clock", "clock")]
  )
  gazebo_sensor_B4_controller = Node(
    package="gazebo_sensor_b4_controller",
    executable="gazebo_sensor_B4_controller",
    prefix = 'xterm -e',
    output='screen',
    name="gazebo_sensor_B4_controller",
    remappings=[
      ("kmriiwa/base/state/LaserB4Scan", "kmriiwa/base/state/LaserB4Scan"),
      ("clock", "clock")]
    ,
    parameters=[{
    "use_sim_time": LaunchConfiguration("use_sim_time"),}]
  )
  planar_move = Node(
    package="planar_move",
    executable="planar_move",
    prefix = 'xterm -e',
    output='screen',
    name="planar_move",
    remappings=[
      ("odom", "odom"),
      ("tf", "tf"),
      ("clock", "clock"),
      ("cmd_vel", "cmd_vel")]
  )
  gazebo_ros_joint_state_publisher = Node(
    package="gazebo_ros_joint_state_publisher",
    executable="gazebo_ros_joint_state_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="gazebo_ros_joint_state_publisher",
    remappings=[
      ("joint_states", "joint_states"),
      ("clock", "clock")]
  )
  laserscan_multi_merger = Node(
    package="ira_laser_tools",
    executable="laserscan_multi_merger",
    prefix = 'xterm -e',
    output='screen',
    name="laserscan_multi_merger",
    remappings=[
      ("merged_cloud", "merged_cloud"),
      ("scan_multi", "scan_multi"),
      ("kmriiwa/base/state/LaserB1Scan", "kmriiwa/base/state/LaserB1Scan"),
      ("kmriiwa/base/state/LaserB4Scan", "kmriiwa/base/state/LaserB4Scan")]
  )
  transform_listener_impl_63dab121a590 = Node(
    package="transform_listener_impl",
    executable="transform_listener_impl",
    prefix = 'xterm -e',
    output='screen',
    name="transform_listener_impl_63dab121a590",
    remappings=[
      ("tf", "tf"),
      ("tf_static", "tf_static")]
  )
  transform_listener_impl_586cb636ca10 = Node(
    package="transform_listener_impl",
    executable="transform_listener_impl",
    prefix = 'xterm -e',
    output='screen',
    name="transform_listener_impl_586cb636ca10",
    remappings=[
      ("tf", "tf"),
      ("tf_static", "tf_static")]
  )
  map_server = Node(
    package="nav2_map_server",
    executable="map_server",
    prefix = 'xterm -e',
    output='screen',
    name="map_server",
    remappings=[
      ("bond", "bond"),
      ("map", "map"),
      ("map_server/transition_event", "map_server/transition_event"),
      ("bond", "sub_bond"),
      ("map_server/change_state", "map_server/change_state"),
      ("map_server/get_available_states", "map_server/get_available_states"),
      ("map_server/get_available_transitions", "map_server/get_available_transitions"),
      ("map_server/get_state", "map_server/get_state"),
      ("map_server/get_transition_graph", "map_server/get_transition_graph"),
      ("map_server/load_map", "map_server/load_map"),
      ("map_server/map", "map_server/map")]
  )
  amcl = Node(
    package="nav2_amcl",
    executable="amcl",
    prefix = 'xterm -e',
    output='screen',
    name="amcl",
    remappings=[
      ("amcl/transition_event", "amcl/transition_event"),
      ("amcl_pose", "amcl_pose"),
      ("bond", "bond"),
      ("particle_cloud", "particle_cloud"),
      ("tf", "tf"),
      ("bond", "sub_bond"),
      ("initialpose", "initialpose"),
      ("map", "map"),
      ("scan_multi", "scan_multi"),
      ("amcl/change_state", "amcl/change_state"),
      ("amcl/get_available_states", "amcl/get_available_states"),
      ("amcl/get_available_transitions", "amcl/get_available_transitions"),
      ("amcl/get_state", "amcl/get_state"),
      ("amcl/get_transition_graph", "amcl/get_transition_graph"),
      ("reinitialize_global_localization", "reinitialize_global_localization"),
      ("request_nomotion_update", "request_nomotion_update"),
      ("set_initial_pose", "set_initial_pose")]
  )
  controller_server = Node(
    package="nav2_controller",
    executable="controller_server",
    prefix = 'xterm -e',
    output='screen',
    name="controller_server",
    remappings=[
      ("bond", "bond"),
      ("controller_server/transition_event", "controller_server/transition_event"),
      ("kmriiwa/base/command/cmd_vel", "kmriiwa/base/command/cmd_vel"),
      ("trajectories", "trajectories"),
      ("transformed_global_plan", "transformed_global_plan"),
      ("bond", "sub_bond"),
      ("odom", "odom"),
      ("speed_limit", "speed_limit"),
      ("follow_path", "follow_path"),
      ("controller_server/change_state", "controller_server/change_state"),
      ("controller_server/get_available_states", "controller_server/get_available_states"),
      ("controller_server/get_available_transitions", "controller_server/get_available_transitions"),
      ("controller_server/get_state", "controller_server/get_state"),
      ("controller_server/get_transition_graph", "controller_server/get_transition_graph")]
  )
  planner_server = Node(
    package="nav2_planner",
    executable="planner_server",
    prefix = 'xterm -e',
    output='screen',
    name="planner_server",
    remappings=[
      ("bond", "bond"),
      ("plan", "plan"),
      ("planner_server/transition_event", "planner_server/transition_event"),
      ("unsmoothed_plan", "unsmoothed_plan"),
      ("bond", "sub_bond"),
      ("compute_path_through_poses", "compute_path_through_poses"),
      ("compute_path_to_pose", "compute_path_to_pose"),
      ("is_path_valid", "is_path_valid"),
      ("planner_server/change_state", "planner_server/change_state"),
      ("planner_server/get_available_states", "planner_server/get_available_states"),
      ("planner_server/get_available_transitions", "planner_server/get_available_transitions"),
      ("planner_server/get_state", "planner_server/get_state"),
      ("planner_server/get_transition_graph", "planner_server/get_transition_graph")]
  )
  transform_listener_impl_62307b87cbb0 = Node(
    package="transform_listener_impl",
    executable="transform_listener_impl",
    prefix = 'xterm -e',
    output='screen',
    name="transform_listener_impl_62307b87cbb0",
    remappings=[
      ("tf", "tf"),
      ("tf_static", "tf_static")]
  )
  behavior_server = Node(
    package="nav2_behaviors",
    executable="behavior_server",
    prefix = 'xterm -e',
    output='screen',
    name="behavior_server",
    remappings=[
      ("behavior_server/transition_event", "behavior_server/transition_event"),
      ("bond", "bond"),
      ("cmd_vel", "cmd_vel"),
      ("bond", "sub_bond"),
      ("local_costmap/costmap_raw", "local_costmap/costmap_raw"),
      ("local_costmap/published_footprint", "local_costmap/published_footprint"),
      ("backup", "backup"),
      ("drive_on_heading", "drive_on_heading"),
      ("spin", "spin"),
      ("wait", "wait"),
      ("behavior_server/change_state", "behavior_server/change_state"),
      ("behavior_server/get_available_states", "behavior_server/get_available_states"),
      ("behavior_server/get_available_transitions", "behavior_server/get_available_transitions"),
      ("behavior_server/get_state", "behavior_server/get_state"),
      ("behavior_server/get_transition_graph", "behavior_server/get_transition_graph")]
  )
  transform_listener_impl_591884f5efa0 = Node(
    package="transform_listener_impl",
    executable="transform_listener_impl",
    prefix = 'xterm -e',
    output='screen',
    name="transform_listener_impl_591884f5efa0",
    remappings=[
      ("tf", "tf"),
      ("tf_static", "tf_static")]
  )
  bt_navigator = Node(
    package="nav2_bt_navigator",
    executable="bt_navigator",
    prefix = 'xterm -e',
    output='screen',
    name="bt_navigator",
    remappings=[
      ("bt_navigator/transition_event", "bt_navigator/transition_event"),
      ("bt_navigator/change_state", "bt_navigator/change_state"),
      ("bt_navigator/get_available_states", "bt_navigator/get_available_states"),
      ("bt_navigator/get_available_transitions", "bt_navigator/get_available_transitions"),
      ("bt_navigator/get_state", "bt_navigator/get_state"),
      ("bt_navigator/get_transition_graph", "bt_navigator/get_transition_graph")]
  )
  bt_navigator_navigate_to_pose = Node(
    package="bt_navigator_navigate_to_pose",
    executable="bt_navigator_navigate_to_pose",
    prefix = 'xterm -e',
    output='screen',
    name="bt_navigator_navigate_to_pose",
    remappings=[
      ("behavior_tree_log", "behavior_tree_log"),
      ("backup", "backup"),
      ("compute_path_to_pose", "compute_path_to_pose"),
      ("follow_path", "follow_path"),
      ("spin", "spin"),
      ("wait", "wait")]
  )
  bt_navigator_navigate_through_poses = Node(
    package="bt_navigator_navigate_through_poses",
    executable="bt_navigator_navigate_through_poses",
    prefix = 'xterm -e',
    output='screen',
    name="bt_navigator_navigate_through_poses",
    remappings=[
      ("behavior_tree_log", "behavior_tree_log"),
      ("backup", "backup"),
      ("compute_path_through_poses", "compute_path_through_poses"),
      ("follow_path", "follow_path"),
      ("spin", "spin"),
      ("wait", "wait")]
  )
  robot_state_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="robot_state_publisher",
    remappings=[
      ("robot_description", "robot_description"),
      ("joint_states", "joint_states")]
  )
  robot_description_publisher = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="robot_description_publisher",
    remappings=[
      ("robot_description", "robot_description"),
      ("c", "clock"),
      ("joint_states", "joint_states")]
  )
  rviz = Node(
    package="rviz2",
    executable="rviz2",
    prefix = 'xterm -e',
    output='screen',
    name="rviz",
    remappings=[
      ("clicked_point", "clicked_point"),
      ("initialpose", "initialpose"),
      ("move_base_simple/goal", "move_base_simple/goal"),
      ("global_costmap/costmap", "global_costmap/costmap"),
      ("global_costmap/costmap_updates", "global_costmap/costmap_updates"),
      ("kmriiwa/base/state/LaserB1Scan", "kmriiwa/base/state/LaserB1Scan"),
      ("kmriiwa/base/state/LaserB4Scan", "kmriiwa/base/state/LaserB4Scan"),
      ("kmriiwa/base/state/odom", "kmriiwa/base/state/odom"),
      ("kmriiwa/robot_description", "kmriiwa/robot_description"),
      ("plan", "plan"),
      ("received_global_plan", "received_global_plan"),
      ("scan_multi", "scan_multi"),
      ("transformed_global_plan", "transformed_global_plan")]
  )
  transform_listener_impl_5f3f2f2aa6c0 = Node(
    package="transform_listener_impl",
    executable="transform_listener_impl",
    prefix = 'xterm -e',
    output='screen',
    name="transform_listener_impl_5f3f2f2aa6c0",
    remappings=[
      ("tf", "tf"),
      ("tf_static", "tf_static")]
  )
  static_transform_publisher_vS7Rn4YQfVmDReBi = Node(
    package="static_transform_publisher",
    executable="static_transform_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="static_transform_publisher_vS7Rn4YQfVmDReBi",
    remappings=[
      ("tf_static", "tf_static")]
    ,
    parameters = [static_transform_publisher_vS7Rn4YQfVmDReBi_config]
  )
  static_transform_publisher_BB3LgctvQJmC8ZBZ = Node(
    package="static_transform_publisher",
    executable="static_transform_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="static_transform_publisher_BB3LgctvQJmC8ZBZ",
    remappings=[
      ("tf_static", "tf_static")]
    ,
    parameters = [static_transform_publisher_BB3LgctvQJmC8ZBZ_config]
  )
  static_transform_publisher_rk0xEkSw7GX3BxqV = Node(
    package="static_transform_publisher",
    executable="static_transform_publisher",
    prefix = 'xterm -e',
    output='screen',
    name="static_transform_publisher_rk0xEkSw7GX3BxqV",
    remappings=[
      ("tf_static", "tf_static")]
  )
  global_costmap/global_costmap = Node(
    package="global_costmap",
    executable="global_costmap",
    prefix = 'xterm -e',
    output='screen',
    name="global_costmap/global_costmap",
    remappings=[
      ("costmap", "costmap"),
      ("costmap_raw", "costmap_raw"),
      ("costmap_updates", "costmap_updates"),
      ("global_costmap/transition_event", "global_costmap/transition_event"),
      ("published_footprint", "published_footprint"),
      ("footprint", "footprint"),
      ("clear_around_global_costmap", "clear_around_global_costmap"),
      ("clear_entirely_global_costmap", "clear_entirely_global_costmap"),
      ("clear_except_global_costmap", "clear_except_global_costmap"),
      ("get_costmap", "get_costmap"),
      ("global_costmap/change_state", "global_costmap/change_state"),
      ("global_costmap/get_available_states", "global_costmap/get_available_states"),
      ("global_costmap/get_available_transitions", "global_costmap/get_available_transitions"),
      ("global_costmap/get_state", "global_costmap/get_state"),
      ("global_costmap/get_transition_graph", "global_costmap/get_transition_graph")]
  )
  local_costmap/local_costmap = Node(
    package="local_costmap",
    executable="local_costmap",
    prefix = 'xterm -e',
    output='screen',
    name="local_costmap/local_costmap",
    remappings=[
      ("costmap", "costmap"),
      ("costmap_raw", "costmap_raw"),
      ("costmap_updates", "costmap_updates"),
      ("local_costmap/transition_event", "local_costmap/transition_event"),
      ("published_footprint", "published_footprint"),
      ("footprint", "footprint"),
      ("clear_around_local_costmap", "clear_around_local_costmap"),
      ("clear_entirely_local_costmap", "clear_entirely_local_costmap"),
      ("clear_except_local_costmap", "clear_except_local_costmap"),
      ("get_costmap", "get_costmap"),
      ("local_costmap/change_state", "local_costmap/change_state"),
      ("local_costmap/get_available_states", "local_costmap/get_available_states"),
      ("local_costmap/get_available_transitions", "local_costmap/get_available_transitions"),
      ("local_costmap/get_state", "local_costmap/get_state"),
      ("local_costmap/get_transition_graph", "local_costmap/get_transition_graph")]
  )
  lifecycle_manager_navigation = Node(
    package="nav2_lifecycle_manager",
    executable="lifecycle_manager",
    prefix = 'xterm -e',
    output='screen',
    name="lifecycle_manager_navigation",
    remappings=[
      ("bond", "bond"),
      ("diagnostics", "diagnostics"),
      ("bond", "sub_bond"),
      ("lifecycle_manager_navigation/is_active", "lifecycle_manager_navigation/is_active"),
      ("lifecycle_manager_navigation/manage_nodes", "lifecycle_manager_navigation/manage_nodes")]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(robot_state_publisher)
  ld.add_action(joint_state_publisher_gui)
  ld.add_action(bt_navigator)
  ld.add_action(relay)
  ld.add_action(gazebo)
  ld.add_action(gazebo_sensor_B1_controller)
  ld.add_action(gazebo_sensor_B4_controller)
  ld.add_action(planar_move)
  ld.add_action(gazebo_ros_joint_state_publisher)
  ld.add_action(laserscan_multi_merger)
  ld.add_action(transform_listener_impl_63dab121a590)
  ld.add_action(transform_listener_impl_586cb636ca10)
  ld.add_action(map_server)
  ld.add_action(amcl)
  ld.add_action(controller_server)
  ld.add_action(planner_server)
  ld.add_action(transform_listener_impl_62307b87cbb0)
  ld.add_action(behavior_server)
  ld.add_action(transform_listener_impl_591884f5efa0)
  ld.add_action(bt_navigator)
  ld.add_action(bt_navigator_navigate_to_pose)
  ld.add_action(bt_navigator_navigate_through_poses)
  ld.add_action(robot_state_publisher)
  ld.add_action(robot_description_publisher)
  ld.add_action(rviz)
  ld.add_action(transform_listener_impl_5f3f2f2aa6c0)
  ld.add_action(static_transform_publisher_vS7Rn4YQfVmDReBi)
  ld.add_action(static_transform_publisher_BB3LgctvQJmC8ZBZ)
  ld.add_action(static_transform_publisher_rk0xEkSw7GX3BxqV)
  ld.add_action(global_costmap/global_costmap)
  ld.add_action(local_costmap/local_costmap)
  ld.add_action(lifecycle_manager_navigation)

  return ld
