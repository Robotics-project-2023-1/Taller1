// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from turtlebot_interfaces:srv/Reproducir.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__FUNCTIONS_H_
#define TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "turtlebot_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "turtlebot_interfaces/srv/detail/reproducir__struct.h"

/// Initialize srv/Reproducir message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * turtlebot_interfaces__srv__Reproducir_Request
 * )) before or use
 * turtlebot_interfaces__srv__Reproducir_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__init(turtlebot_interfaces__srv__Reproducir_Request * msg);

/// Finalize srv/Reproducir message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Request__fini(turtlebot_interfaces__srv__Reproducir_Request * msg);

/// Create srv/Reproducir message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * turtlebot_interfaces__srv__Reproducir_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
turtlebot_interfaces__srv__Reproducir_Request *
turtlebot_interfaces__srv__Reproducir_Request__create();

/// Destroy srv/Reproducir message.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Request__destroy(turtlebot_interfaces__srv__Reproducir_Request * msg);

/// Check for srv/Reproducir message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__are_equal(const turtlebot_interfaces__srv__Reproducir_Request * lhs, const turtlebot_interfaces__srv__Reproducir_Request * rhs);

/// Copy a srv/Reproducir message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__copy(
  const turtlebot_interfaces__srv__Reproducir_Request * input,
  turtlebot_interfaces__srv__Reproducir_Request * output);

/// Initialize array of srv/Reproducir messages.
/**
 * It allocates the memory for the number of elements and calls
 * turtlebot_interfaces__srv__Reproducir_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__Sequence__init(turtlebot_interfaces__srv__Reproducir_Request__Sequence * array, size_t size);

/// Finalize array of srv/Reproducir messages.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Request__Sequence__fini(turtlebot_interfaces__srv__Reproducir_Request__Sequence * array);

/// Create array of srv/Reproducir messages.
/**
 * It allocates the memory for the array and calls
 * turtlebot_interfaces__srv__Reproducir_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
turtlebot_interfaces__srv__Reproducir_Request__Sequence *
turtlebot_interfaces__srv__Reproducir_Request__Sequence__create(size_t size);

/// Destroy array of srv/Reproducir messages.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Request__Sequence__destroy(turtlebot_interfaces__srv__Reproducir_Request__Sequence * array);

/// Check for srv/Reproducir message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__Sequence__are_equal(const turtlebot_interfaces__srv__Reproducir_Request__Sequence * lhs, const turtlebot_interfaces__srv__Reproducir_Request__Sequence * rhs);

/// Copy an array of srv/Reproducir messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Request__Sequence__copy(
  const turtlebot_interfaces__srv__Reproducir_Request__Sequence * input,
  turtlebot_interfaces__srv__Reproducir_Request__Sequence * output);

/// Initialize srv/Reproducir message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * turtlebot_interfaces__srv__Reproducir_Response
 * )) before or use
 * turtlebot_interfaces__srv__Reproducir_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__init(turtlebot_interfaces__srv__Reproducir_Response * msg);

/// Finalize srv/Reproducir message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Response__fini(turtlebot_interfaces__srv__Reproducir_Response * msg);

/// Create srv/Reproducir message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * turtlebot_interfaces__srv__Reproducir_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
turtlebot_interfaces__srv__Reproducir_Response *
turtlebot_interfaces__srv__Reproducir_Response__create();

/// Destroy srv/Reproducir message.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Response__destroy(turtlebot_interfaces__srv__Reproducir_Response * msg);

/// Check for srv/Reproducir message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__are_equal(const turtlebot_interfaces__srv__Reproducir_Response * lhs, const turtlebot_interfaces__srv__Reproducir_Response * rhs);

/// Copy a srv/Reproducir message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__copy(
  const turtlebot_interfaces__srv__Reproducir_Response * input,
  turtlebot_interfaces__srv__Reproducir_Response * output);

/// Initialize array of srv/Reproducir messages.
/**
 * It allocates the memory for the number of elements and calls
 * turtlebot_interfaces__srv__Reproducir_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__Sequence__init(turtlebot_interfaces__srv__Reproducir_Response__Sequence * array, size_t size);

/// Finalize array of srv/Reproducir messages.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Response__Sequence__fini(turtlebot_interfaces__srv__Reproducir_Response__Sequence * array);

/// Create array of srv/Reproducir messages.
/**
 * It allocates the memory for the array and calls
 * turtlebot_interfaces__srv__Reproducir_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
turtlebot_interfaces__srv__Reproducir_Response__Sequence *
turtlebot_interfaces__srv__Reproducir_Response__Sequence__create(size_t size);

/// Destroy array of srv/Reproducir messages.
/**
 * It calls
 * turtlebot_interfaces__srv__Reproducir_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
void
turtlebot_interfaces__srv__Reproducir_Response__Sequence__destroy(turtlebot_interfaces__srv__Reproducir_Response__Sequence * array);

/// Check for srv/Reproducir message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__Sequence__are_equal(const turtlebot_interfaces__srv__Reproducir_Response__Sequence * lhs, const turtlebot_interfaces__srv__Reproducir_Response__Sequence * rhs);

/// Copy an array of srv/Reproducir messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_turtlebot_interfaces
bool
turtlebot_interfaces__srv__Reproducir_Response__Sequence__copy(
  const turtlebot_interfaces__srv__Reproducir_Response__Sequence * input,
  turtlebot_interfaces__srv__Reproducir_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__FUNCTIONS_H_
