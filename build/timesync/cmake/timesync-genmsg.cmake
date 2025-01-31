# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "timesync: 1 messages, 0 services")

set(MSG_I_FLAGS "-Itimesync:/home/casch/catkin_ws/src/timesync/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(timesync_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_custom_target(_timesync_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "timesync" "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(timesync
  "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/timesync
)

### Generating Services

### Generating Module File
_generate_module_cpp(timesync
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/timesync
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(timesync_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(timesync_generate_messages timesync_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_dependencies(timesync_generate_messages_cpp _timesync_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(timesync_gencpp)
add_dependencies(timesync_gencpp timesync_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS timesync_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(timesync
  "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/timesync
)

### Generating Services

### Generating Module File
_generate_module_eus(timesync
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/timesync
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(timesync_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(timesync_generate_messages timesync_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_dependencies(timesync_generate_messages_eus _timesync_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(timesync_geneus)
add_dependencies(timesync_geneus timesync_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS timesync_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(timesync
  "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/timesync
)

### Generating Services

### Generating Module File
_generate_module_lisp(timesync
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/timesync
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(timesync_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(timesync_generate_messages timesync_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_dependencies(timesync_generate_messages_lisp _timesync_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(timesync_genlisp)
add_dependencies(timesync_genlisp timesync_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS timesync_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(timesync
  "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/timesync
)

### Generating Services

### Generating Module File
_generate_module_nodejs(timesync
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/timesync
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(timesync_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(timesync_generate_messages timesync_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_dependencies(timesync_generate_messages_nodejs _timesync_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(timesync_gennodejs)
add_dependencies(timesync_gennodejs timesync_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS timesync_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(timesync
  "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/timesync
)

### Generating Services

### Generating Module File
_generate_module_py(timesync
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/timesync
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(timesync_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(timesync_generate_messages timesync_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/casch/catkin_ws/src/timesync/msg/TimesyncDebug.msg" NAME_WE)
add_dependencies(timesync_generate_messages_py _timesync_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(timesync_genpy)
add_dependencies(timesync_genpy timesync_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS timesync_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/timesync)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/timesync
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(timesync_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/timesync)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/timesync
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(timesync_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/timesync)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/timesync
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(timesync_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/timesync)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/timesync
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(timesync_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/timesync)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/timesync\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/timesync
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(timesync_generate_messages_py std_msgs_generate_messages_py)
endif()
