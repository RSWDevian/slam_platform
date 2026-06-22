// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice
#include "slam_interfaces/msg/detail/slam_metrics__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
slam_interfaces__msg__SLAMMetrics__init(slam_interfaces__msg__SLAMMetrics * msg)
{
  if (!msg) {
    return false;
  }
  // ate
  // rpe
  // drift
  // cpu_usage
  // memory_usage
  // runtime
  // thread_count
  return true;
}

void
slam_interfaces__msg__SLAMMetrics__fini(slam_interfaces__msg__SLAMMetrics * msg)
{
  if (!msg) {
    return;
  }
  // ate
  // rpe
  // drift
  // cpu_usage
  // memory_usage
  // runtime
  // thread_count
}

bool
slam_interfaces__msg__SLAMMetrics__are_equal(const slam_interfaces__msg__SLAMMetrics * lhs, const slam_interfaces__msg__SLAMMetrics * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ate
  if (lhs->ate != rhs->ate) {
    return false;
  }
  // rpe
  if (lhs->rpe != rhs->rpe) {
    return false;
  }
  // drift
  if (lhs->drift != rhs->drift) {
    return false;
  }
  // cpu_usage
  if (lhs->cpu_usage != rhs->cpu_usage) {
    return false;
  }
  // memory_usage
  if (lhs->memory_usage != rhs->memory_usage) {
    return false;
  }
  // runtime
  if (lhs->runtime != rhs->runtime) {
    return false;
  }
  // thread_count
  if (lhs->thread_count != rhs->thread_count) {
    return false;
  }
  return true;
}

bool
slam_interfaces__msg__SLAMMetrics__copy(
  const slam_interfaces__msg__SLAMMetrics * input,
  slam_interfaces__msg__SLAMMetrics * output)
{
  if (!input || !output) {
    return false;
  }
  // ate
  output->ate = input->ate;
  // rpe
  output->rpe = input->rpe;
  // drift
  output->drift = input->drift;
  // cpu_usage
  output->cpu_usage = input->cpu_usage;
  // memory_usage
  output->memory_usage = input->memory_usage;
  // runtime
  output->runtime = input->runtime;
  // thread_count
  output->thread_count = input->thread_count;
  return true;
}

slam_interfaces__msg__SLAMMetrics *
slam_interfaces__msg__SLAMMetrics__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  slam_interfaces__msg__SLAMMetrics * msg = (slam_interfaces__msg__SLAMMetrics *)allocator.allocate(sizeof(slam_interfaces__msg__SLAMMetrics), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(slam_interfaces__msg__SLAMMetrics));
  bool success = slam_interfaces__msg__SLAMMetrics__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
slam_interfaces__msg__SLAMMetrics__destroy(slam_interfaces__msg__SLAMMetrics * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    slam_interfaces__msg__SLAMMetrics__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
slam_interfaces__msg__SLAMMetrics__Sequence__init(slam_interfaces__msg__SLAMMetrics__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  slam_interfaces__msg__SLAMMetrics * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(slam_interfaces__msg__SLAMMetrics)) {
      return false;
    }
    data = (slam_interfaces__msg__SLAMMetrics *)allocator.zero_allocate(size, sizeof(slam_interfaces__msg__SLAMMetrics), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = slam_interfaces__msg__SLAMMetrics__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        slam_interfaces__msg__SLAMMetrics__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
slam_interfaces__msg__SLAMMetrics__Sequence__fini(slam_interfaces__msg__SLAMMetrics__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      slam_interfaces__msg__SLAMMetrics__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

slam_interfaces__msg__SLAMMetrics__Sequence *
slam_interfaces__msg__SLAMMetrics__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  slam_interfaces__msg__SLAMMetrics__Sequence * array = (slam_interfaces__msg__SLAMMetrics__Sequence *)allocator.allocate(sizeof(slam_interfaces__msg__SLAMMetrics__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = slam_interfaces__msg__SLAMMetrics__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
slam_interfaces__msg__SLAMMetrics__Sequence__destroy(slam_interfaces__msg__SLAMMetrics__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    slam_interfaces__msg__SLAMMetrics__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
slam_interfaces__msg__SLAMMetrics__Sequence__are_equal(const slam_interfaces__msg__SLAMMetrics__Sequence * lhs, const slam_interfaces__msg__SLAMMetrics__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!slam_interfaces__msg__SLAMMetrics__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
slam_interfaces__msg__SLAMMetrics__Sequence__copy(
  const slam_interfaces__msg__SLAMMetrics__Sequence * input,
  slam_interfaces__msg__SLAMMetrics__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(slam_interfaces__msg__SLAMMetrics)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(slam_interfaces__msg__SLAMMetrics);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    slam_interfaces__msg__SLAMMetrics * data =
      (slam_interfaces__msg__SLAMMetrics *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!slam_interfaces__msg__SLAMMetrics__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          slam_interfaces__msg__SLAMMetrics__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!slam_interfaces__msg__SLAMMetrics__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
