#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to slam_interfaces__msg__SLAMMetrics

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SLAMMetrics {

    // This member is not documented.
    #[allow(missing_docs)]
    pub ate: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rpe: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub drift: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cpu_usage: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub memory_usage: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub runtime: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub thread_count: i32,

}



impl Default for SLAMMetrics {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SLAMMetrics::default())
  }
}

impl rosidl_runtime_rs::Message for SLAMMetrics {
  type RmwMsg = super::msg::rmw::SLAMMetrics;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        ate: msg.ate,
        rpe: msg.rpe,
        drift: msg.drift,
        cpu_usage: msg.cpu_usage,
        memory_usage: msg.memory_usage,
        runtime: msg.runtime,
        thread_count: msg.thread_count,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      ate: msg.ate,
      rpe: msg.rpe,
      drift: msg.drift,
      cpu_usage: msg.cpu_usage,
      memory_usage: msg.memory_usage,
      runtime: msg.runtime,
      thread_count: msg.thread_count,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      ate: msg.ate,
      rpe: msg.rpe,
      drift: msg.drift,
      cpu_usage: msg.cpu_usage,
      memory_usage: msg.memory_usage,
      runtime: msg.runtime,
      thread_count: msg.thread_count,
    }
  }
}


