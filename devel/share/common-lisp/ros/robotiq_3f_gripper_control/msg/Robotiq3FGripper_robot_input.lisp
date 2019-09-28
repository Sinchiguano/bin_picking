; Auto-generated. Do not edit!


(cl:in-package robotiq_3f_gripper_control-msg)


;//! \htmlinclude Robotiq3FGripper_robot_input.msg.html

(cl:defclass <Robotiq3FGripper_robot_input> (roslisp-msg-protocol:ros-message)
  ((gACT
    :reader gACT
    :initarg :gACT
    :type cl:fixnum
    :initform 0)
   (gMOD
    :reader gMOD
    :initarg :gMOD
    :type cl:fixnum
    :initform 0)
   (gGTO
    :reader gGTO
    :initarg :gGTO
    :type cl:fixnum
    :initform 0)
   (gIMC
    :reader gIMC
    :initarg :gIMC
    :type cl:fixnum
    :initform 0)
   (gSTA
    :reader gSTA
    :initarg :gSTA
    :type cl:fixnum
    :initform 0)
   (gDTA
    :reader gDTA
    :initarg :gDTA
    :type cl:fixnum
    :initform 0)
   (gDTB
    :reader gDTB
    :initarg :gDTB
    :type cl:fixnum
    :initform 0)
   (gDTC
    :reader gDTC
    :initarg :gDTC
    :type cl:fixnum
    :initform 0)
   (gDTS
    :reader gDTS
    :initarg :gDTS
    :type cl:fixnum
    :initform 0)
   (gFLT
    :reader gFLT
    :initarg :gFLT
    :type cl:fixnum
    :initform 0)
   (gPRA
    :reader gPRA
    :initarg :gPRA
    :type cl:fixnum
    :initform 0)
   (gPOA
    :reader gPOA
    :initarg :gPOA
    :type cl:fixnum
    :initform 0)
   (gCUA
    :reader gCUA
    :initarg :gCUA
    :type cl:fixnum
    :initform 0)
   (gPRB
    :reader gPRB
    :initarg :gPRB
    :type cl:fixnum
    :initform 0)
   (gPOB
    :reader gPOB
    :initarg :gPOB
    :type cl:fixnum
    :initform 0)
   (gCUB
    :reader gCUB
    :initarg :gCUB
    :type cl:fixnum
    :initform 0)
   (gPRC
    :reader gPRC
    :initarg :gPRC
    :type cl:fixnum
    :initform 0)
   (gPOC
    :reader gPOC
    :initarg :gPOC
    :type cl:fixnum
    :initform 0)
   (gCUC
    :reader gCUC
    :initarg :gCUC
    :type cl:fixnum
    :initform 0)
   (gPRS
    :reader gPRS
    :initarg :gPRS
    :type cl:fixnum
    :initform 0)
   (gPOS
    :reader gPOS
    :initarg :gPOS
    :type cl:fixnum
    :initform 0)
   (gCUS
    :reader gCUS
    :initarg :gCUS
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Robotiq3FGripper_robot_input (<Robotiq3FGripper_robot_input>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Robotiq3FGripper_robot_input>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Robotiq3FGripper_robot_input)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robotiq_3f_gripper_control-msg:<Robotiq3FGripper_robot_input> is deprecated: use robotiq_3f_gripper_control-msg:Robotiq3FGripper_robot_input instead.")))

(cl:ensure-generic-function 'gACT-val :lambda-list '(m))
(cl:defmethod gACT-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gACT-val is deprecated.  Use robotiq_3f_gripper_control-msg:gACT instead.")
  (gACT m))

(cl:ensure-generic-function 'gMOD-val :lambda-list '(m))
(cl:defmethod gMOD-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gMOD-val is deprecated.  Use robotiq_3f_gripper_control-msg:gMOD instead.")
  (gMOD m))

(cl:ensure-generic-function 'gGTO-val :lambda-list '(m))
(cl:defmethod gGTO-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gGTO-val is deprecated.  Use robotiq_3f_gripper_control-msg:gGTO instead.")
  (gGTO m))

(cl:ensure-generic-function 'gIMC-val :lambda-list '(m))
(cl:defmethod gIMC-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gIMC-val is deprecated.  Use robotiq_3f_gripper_control-msg:gIMC instead.")
  (gIMC m))

(cl:ensure-generic-function 'gSTA-val :lambda-list '(m))
(cl:defmethod gSTA-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gSTA-val is deprecated.  Use robotiq_3f_gripper_control-msg:gSTA instead.")
  (gSTA m))

(cl:ensure-generic-function 'gDTA-val :lambda-list '(m))
(cl:defmethod gDTA-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gDTA-val is deprecated.  Use robotiq_3f_gripper_control-msg:gDTA instead.")
  (gDTA m))

(cl:ensure-generic-function 'gDTB-val :lambda-list '(m))
(cl:defmethod gDTB-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gDTB-val is deprecated.  Use robotiq_3f_gripper_control-msg:gDTB instead.")
  (gDTB m))

(cl:ensure-generic-function 'gDTC-val :lambda-list '(m))
(cl:defmethod gDTC-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gDTC-val is deprecated.  Use robotiq_3f_gripper_control-msg:gDTC instead.")
  (gDTC m))

(cl:ensure-generic-function 'gDTS-val :lambda-list '(m))
(cl:defmethod gDTS-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gDTS-val is deprecated.  Use robotiq_3f_gripper_control-msg:gDTS instead.")
  (gDTS m))

(cl:ensure-generic-function 'gFLT-val :lambda-list '(m))
(cl:defmethod gFLT-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gFLT-val is deprecated.  Use robotiq_3f_gripper_control-msg:gFLT instead.")
  (gFLT m))

(cl:ensure-generic-function 'gPRA-val :lambda-list '(m))
(cl:defmethod gPRA-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPRA-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPRA instead.")
  (gPRA m))

(cl:ensure-generic-function 'gPOA-val :lambda-list '(m))
(cl:defmethod gPOA-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPOA-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPOA instead.")
  (gPOA m))

(cl:ensure-generic-function 'gCUA-val :lambda-list '(m))
(cl:defmethod gCUA-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gCUA-val is deprecated.  Use robotiq_3f_gripper_control-msg:gCUA instead.")
  (gCUA m))

(cl:ensure-generic-function 'gPRB-val :lambda-list '(m))
(cl:defmethod gPRB-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPRB-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPRB instead.")
  (gPRB m))

(cl:ensure-generic-function 'gPOB-val :lambda-list '(m))
(cl:defmethod gPOB-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPOB-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPOB instead.")
  (gPOB m))

(cl:ensure-generic-function 'gCUB-val :lambda-list '(m))
(cl:defmethod gCUB-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gCUB-val is deprecated.  Use robotiq_3f_gripper_control-msg:gCUB instead.")
  (gCUB m))

(cl:ensure-generic-function 'gPRC-val :lambda-list '(m))
(cl:defmethod gPRC-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPRC-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPRC instead.")
  (gPRC m))

(cl:ensure-generic-function 'gPOC-val :lambda-list '(m))
(cl:defmethod gPOC-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPOC-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPOC instead.")
  (gPOC m))

(cl:ensure-generic-function 'gCUC-val :lambda-list '(m))
(cl:defmethod gCUC-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gCUC-val is deprecated.  Use robotiq_3f_gripper_control-msg:gCUC instead.")
  (gCUC m))

(cl:ensure-generic-function 'gPRS-val :lambda-list '(m))
(cl:defmethod gPRS-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPRS-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPRS instead.")
  (gPRS m))

(cl:ensure-generic-function 'gPOS-val :lambda-list '(m))
(cl:defmethod gPOS-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gPOS-val is deprecated.  Use robotiq_3f_gripper_control-msg:gPOS instead.")
  (gPOS m))

(cl:ensure-generic-function 'gCUS-val :lambda-list '(m))
(cl:defmethod gCUS-val ((m <Robotiq3FGripper_robot_input>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotiq_3f_gripper_control-msg:gCUS-val is deprecated.  Use robotiq_3f_gripper_control-msg:gCUS instead.")
  (gCUS m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Robotiq3FGripper_robot_input>) ostream)
  "Serializes a message object of type '<Robotiq3FGripper_robot_input>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gACT)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gMOD)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGTO)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gIMC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTS)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFLT)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUA)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUB)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUC)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRS)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOS)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUS)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Robotiq3FGripper_robot_input>) istream)
  "Deserializes a message object of type '<Robotiq3FGripper_robot_input>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gACT)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gMOD)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gGTO)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gIMC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gSTA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gDTS)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gFLT)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUA)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUB)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUC)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPRS)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gPOS)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gCUS)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Robotiq3FGripper_robot_input>)))
  "Returns string type for a message object of type '<Robotiq3FGripper_robot_input>"
  "robotiq_3f_gripper_control/Robotiq3FGripper_robot_input")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Robotiq3FGripper_robot_input)))
  "Returns string type for a message object of type 'Robotiq3FGripper_robot_input"
  "robotiq_3f_gripper_control/Robotiq3FGripper_robot_input")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Robotiq3FGripper_robot_input>)))
  "Returns md5sum for a message object of type '<Robotiq3FGripper_robot_input>"
  "4d0701156e580a420c48833f57bc83f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Robotiq3FGripper_robot_input)))
  "Returns md5sum for a message object of type 'Robotiq3FGripper_robot_input"
  "4d0701156e580a420c48833f57bc83f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Robotiq3FGripper_robot_input>)))
  "Returns full string definition for message of type '<Robotiq3FGripper_robot_input>"
  (cl:format cl:nil "uint8 gACT ~%uint8 gMOD ~%uint8 gGTO ~%uint8 gIMC ~%uint8 gSTA ~%uint8 gDTA ~%uint8 gDTB ~%uint8 gDTC ~%uint8 gDTS ~%uint8 gFLT ~%uint8 gPRA ~%uint8 gPOA ~%uint8 gCUA ~%uint8 gPRB ~%uint8 gPOB ~%uint8 gCUB ~%uint8 gPRC ~%uint8 gPOC ~%uint8 gCUC ~%uint8 gPRS ~%uint8 gPOS ~%uint8 gCUS~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Robotiq3FGripper_robot_input)))
  "Returns full string definition for message of type 'Robotiq3FGripper_robot_input"
  (cl:format cl:nil "uint8 gACT ~%uint8 gMOD ~%uint8 gGTO ~%uint8 gIMC ~%uint8 gSTA ~%uint8 gDTA ~%uint8 gDTB ~%uint8 gDTC ~%uint8 gDTS ~%uint8 gFLT ~%uint8 gPRA ~%uint8 gPOA ~%uint8 gCUA ~%uint8 gPRB ~%uint8 gPOB ~%uint8 gCUB ~%uint8 gPRC ~%uint8 gPOC ~%uint8 gCUC ~%uint8 gPRS ~%uint8 gPOS ~%uint8 gCUS~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Robotiq3FGripper_robot_input>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Robotiq3FGripper_robot_input>))
  "Converts a ROS message object to a list"
  (cl:list 'Robotiq3FGripper_robot_input
    (cl:cons ':gACT (gACT msg))
    (cl:cons ':gMOD (gMOD msg))
    (cl:cons ':gGTO (gGTO msg))
    (cl:cons ':gIMC (gIMC msg))
    (cl:cons ':gSTA (gSTA msg))
    (cl:cons ':gDTA (gDTA msg))
    (cl:cons ':gDTB (gDTB msg))
    (cl:cons ':gDTC (gDTC msg))
    (cl:cons ':gDTS (gDTS msg))
    (cl:cons ':gFLT (gFLT msg))
    (cl:cons ':gPRA (gPRA msg))
    (cl:cons ':gPOA (gPOA msg))
    (cl:cons ':gCUA (gCUA msg))
    (cl:cons ':gPRB (gPRB msg))
    (cl:cons ':gPOB (gPOB msg))
    (cl:cons ':gCUB (gCUB msg))
    (cl:cons ':gPRC (gPRC msg))
    (cl:cons ':gPOC (gPOC msg))
    (cl:cons ':gCUC (gCUC msg))
    (cl:cons ':gPRS (gPRS msg))
    (cl:cons ':gPOS (gPOS msg))
    (cl:cons ':gCUS (gCUS msg))
))
