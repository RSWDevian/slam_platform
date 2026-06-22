// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

#include "slam_interfaces/msg/detail/slam_metrics__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_slam_interfaces
const rosidl_type_hash_t *
slam_interfaces__msg__SLAMMetrics__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x70, 0x09, 0xfb, 0xd7, 0xc7, 0x79, 0x61, 0xef,
      0xd4, 0x34, 0x76, 0x94, 0xf0, 0x19, 0xdb, 0xd0,
      0xaa, 0x5c, 0xad, 0xcf, 0x74, 0x7d, 0xc6, 0x53,
      0x0b, 0xdf, 0xd0, 0x02, 0x0b, 0x63, 0x7e, 0x8f,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char slam_interfaces__msg__SLAMMetrics__TYPE_NAME[] = "slam_interfaces/msg/SLAMMetrics";

// Define type names, field names, and default values
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__ate[] = "ate";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__rpe[] = "rpe";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__drift[] = "drift";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__cpu_usage[] = "cpu_usage";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__memory_usage[] = "memory_usage";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__runtime[] = "runtime";
static char slam_interfaces__msg__SLAMMetrics__FIELD_NAME__thread_count[] = "thread_count";

static rosidl_runtime_c__type_description__Field slam_interfaces__msg__SLAMMetrics__FIELDS[] = {
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__ate, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__rpe, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__drift, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__cpu_usage, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__memory_usage, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__runtime, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {slam_interfaces__msg__SLAMMetrics__FIELD_NAME__thread_count, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
slam_interfaces__msg__SLAMMetrics__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {slam_interfaces__msg__SLAMMetrics__TYPE_NAME, 31, 31},
      {slam_interfaces__msg__SLAMMetrics__FIELDS, 7, 7},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 ate\n"
  "float64 rpe\n"
  "float64 drift\n"
  "\n"
  "float64 cpu_usage\n"
  "float64 memory_usage\n"
  "float64 runtime\n"
  "\n"
  "int32 thread_count";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
slam_interfaces__msg__SLAMMetrics__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {slam_interfaces__msg__SLAMMetrics__TYPE_NAME, 31, 31},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 113, 113},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
slam_interfaces__msg__SLAMMetrics__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *slam_interfaces__msg__SLAMMetrics__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
