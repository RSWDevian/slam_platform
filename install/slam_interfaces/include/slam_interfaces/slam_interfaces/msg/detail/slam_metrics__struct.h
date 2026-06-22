// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_interfaces/msg/slam_metrics.h"


#ifndef SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_H_
#define SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/SLAMMetrics in the package slam_interfaces.
typedef struct slam_interfaces__msg__SLAMMetrics
{
  double ate;
  double rpe;
  double drift;
  double cpu_usage;
  double memory_usage;
  double runtime;
  int32_t thread_count;
} slam_interfaces__msg__SLAMMetrics;

// Struct for a sequence of slam_interfaces__msg__SLAMMetrics.
typedef struct slam_interfaces__msg__SLAMMetrics__Sequence
{
  slam_interfaces__msg__SLAMMetrics * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} slam_interfaces__msg__SLAMMetrics__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_H_
