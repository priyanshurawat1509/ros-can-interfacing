; Auto-generated. Do not edit!


(cl:in-package raptor_dbw_msgs-msg)


;//! \htmlinclude HighBeam.msg.html

(cl:defclass <HighBeam> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass HighBeam (<HighBeam>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HighBeam>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HighBeam)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name raptor_dbw_msgs-msg:<HighBeam> is deprecated: use raptor_dbw_msgs-msg:HighBeam instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <HighBeam>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader raptor_dbw_msgs-msg:status-val is deprecated.  Use raptor_dbw_msgs-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<HighBeam>)))
    "Constants for message type '<HighBeam>"
  '((:OFF . 0)
    (:ON . 1)
    (:FORCE_ON . 2)
    (:RESERVED . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'HighBeam)))
    "Constants for message type 'HighBeam"
  '((:OFF . 0)
    (:ON . 1)
    (:FORCE_ON . 2)
    (:RESERVED . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HighBeam>) ostream)
  "Serializes a message object of type '<HighBeam>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HighBeam>) istream)
  "Deserializes a message object of type '<HighBeam>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HighBeam>)))
  "Returns string type for a message object of type '<HighBeam>"
  "raptor_dbw_msgs/HighBeam")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HighBeam)))
  "Returns string type for a message object of type 'HighBeam"
  "raptor_dbw_msgs/HighBeam")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HighBeam>)))
  "Returns md5sum for a message object of type '<HighBeam>"
  "adbf7a951d077ba41a11250e8c7184ce")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HighBeam)))
  "Returns md5sum for a message object of type 'HighBeam"
  "adbf7a951d077ba41a11250e8c7184ce")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HighBeam>)))
  "Returns full string definition for message of type '<HighBeam>"
  (cl:format cl:nil "uint8 status~%~%uint8 OFF = 0~%uint8 ON = 1~%uint8 FORCE_ON = 2~%uint8 RESERVED = 3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HighBeam)))
  "Returns full string definition for message of type 'HighBeam"
  (cl:format cl:nil "uint8 status~%~%uint8 OFF = 0~%uint8 ON = 1~%uint8 FORCE_ON = 2~%uint8 RESERVED = 3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HighBeam>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HighBeam>))
  "Converts a ROS message object to a list"
  (cl:list 'HighBeam
    (cl:cons ':status (status msg))
))
