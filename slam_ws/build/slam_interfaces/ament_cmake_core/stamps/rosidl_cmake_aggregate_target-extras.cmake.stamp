# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target slam_interfaces::slam_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${slam_interfaces_TARGETS}.
if(slam_interfaces_TARGETS AND NOT TARGET slam_interfaces::slam_interfaces)
  add_library(slam_interfaces::slam_interfaces INTERFACE IMPORTED)
  set_target_properties(slam_interfaces::slam_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${slam_interfaces_TARGETS}")
endif()
