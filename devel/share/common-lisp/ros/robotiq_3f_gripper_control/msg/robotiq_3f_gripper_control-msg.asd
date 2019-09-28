
(cl:in-package :asdf)

(defsystem "robotiq_3f_gripper_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Robotiq3FGripper_robot_input" :depends-on ("_package_Robotiq3FGripper_robot_input"))
    (:file "_package_Robotiq3FGripper_robot_input" :depends-on ("_package"))
    (:file "Robotiq3FGripper_robot_output" :depends-on ("_package_Robotiq3FGripper_robot_output"))
    (:file "_package_Robotiq3FGripper_robot_output" :depends-on ("_package"))
  ))