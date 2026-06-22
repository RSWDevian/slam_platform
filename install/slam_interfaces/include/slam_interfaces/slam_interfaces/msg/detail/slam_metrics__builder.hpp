// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_interfaces/msg/slam_metrics.hpp"


#ifndef SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__BUILDER_HPP_
#define SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "slam_interfaces/msg/detail/slam_metrics__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace slam_interfaces
{

namespace msg
{

namespace builder
{

class Init_SLAMMetrics_thread_count
{
public:
  explicit Init_SLAMMetrics_thread_count(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  ::slam_interfaces::msg::SLAMMetrics thread_count(::slam_interfaces::msg::SLAMMetrics::_thread_count_type arg)
  {
    msg_.thread_count = std::move(arg);
    return std::move(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_runtime
{
public:
  explicit Init_SLAMMetrics_runtime(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  Init_SLAMMetrics_thread_count runtime(::slam_interfaces::msg::SLAMMetrics::_runtime_type arg)
  {
    msg_.runtime = std::move(arg);
    return Init_SLAMMetrics_thread_count(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_memory_usage
{
public:
  explicit Init_SLAMMetrics_memory_usage(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  Init_SLAMMetrics_runtime memory_usage(::slam_interfaces::msg::SLAMMetrics::_memory_usage_type arg)
  {
    msg_.memory_usage = std::move(arg);
    return Init_SLAMMetrics_runtime(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_cpu_usage
{
public:
  explicit Init_SLAMMetrics_cpu_usage(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  Init_SLAMMetrics_memory_usage cpu_usage(::slam_interfaces::msg::SLAMMetrics::_cpu_usage_type arg)
  {
    msg_.cpu_usage = std::move(arg);
    return Init_SLAMMetrics_memory_usage(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_drift
{
public:
  explicit Init_SLAMMetrics_drift(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  Init_SLAMMetrics_cpu_usage drift(::slam_interfaces::msg::SLAMMetrics::_drift_type arg)
  {
    msg_.drift = std::move(arg);
    return Init_SLAMMetrics_cpu_usage(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_rpe
{
public:
  explicit Init_SLAMMetrics_rpe(::slam_interfaces::msg::SLAMMetrics & msg)
  : msg_(msg)
  {}
  Init_SLAMMetrics_drift rpe(::slam_interfaces::msg::SLAMMetrics::_rpe_type arg)
  {
    msg_.rpe = std::move(arg);
    return Init_SLAMMetrics_drift(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

class Init_SLAMMetrics_ate
{
public:
  Init_SLAMMetrics_ate()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SLAMMetrics_rpe ate(::slam_interfaces::msg::SLAMMetrics::_ate_type arg)
  {
    msg_.ate = std::move(arg);
    return Init_SLAMMetrics_rpe(msg_);
  }

private:
  ::slam_interfaces::msg::SLAMMetrics msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::slam_interfaces::msg::SLAMMetrics>()
{
  return slam_interfaces::msg::builder::Init_SLAMMetrics_ate();
}

}  // namespace slam_interfaces

#endif  // SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__BUILDER_HPP_
