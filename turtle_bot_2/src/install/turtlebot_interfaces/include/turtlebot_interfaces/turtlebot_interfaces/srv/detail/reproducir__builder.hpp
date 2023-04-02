// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlebot_interfaces:srv/Reproducir.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__BUILDER_HPP_
#define TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtlebot_interfaces/srv/detail/reproducir__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtlebot_interfaces
{

namespace srv
{

namespace builder
{

class Init_Reproducir_Request_nombre
{
public:
  Init_Reproducir_Request_nombre()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlebot_interfaces::srv::Reproducir_Request nombre(::turtlebot_interfaces::srv::Reproducir_Request::_nombre_type arg)
  {
    msg_.nombre = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_interfaces::srv::Reproducir_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_interfaces::srv::Reproducir_Request>()
{
  return turtlebot_interfaces::srv::builder::Init_Reproducir_Request_nombre();
}

}  // namespace turtlebot_interfaces


namespace turtlebot_interfaces
{

namespace srv
{

namespace builder
{

class Init_Reproducir_Response_respuesta
{
public:
  Init_Reproducir_Response_respuesta()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlebot_interfaces::srv::Reproducir_Response respuesta(::turtlebot_interfaces::srv::Reproducir_Response::_respuesta_type arg)
  {
    msg_.respuesta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlebot_interfaces::srv::Reproducir_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlebot_interfaces::srv::Reproducir_Response>()
{
  return turtlebot_interfaces::srv::builder::Init_Reproducir_Response_respuesta();
}

}  // namespace turtlebot_interfaces

#endif  // TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__BUILDER_HPP_
