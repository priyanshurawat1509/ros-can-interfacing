; Auto-generated. Do not edit!


(cl:in-package raptor_dbw_msgs-msg)


;//! \htmlinclude LowBeam.msg.html

(cl:defclass <LowBeam> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass LowBeam (<LowBeam>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LowBeam>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LowBeam)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name raptor_dbw_msgs-msg:<LowBeam> is deprecated: use raptor_dbw_msgs-msg:LowBeam instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <LowBeam>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader raptor_dbw_msgs-msg:status-val is deprecated.  Use raptor_dbw_msgs-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<LowBeam>)))
    "Constants for message type '<LowBeam>"
  '((:OFF . 0)
    (:RESERVED . 1)
    (:ON . 2)
    (:RESERVED_1 . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'LowBeam)))
    "Constants for message type 'LowBeam"
  '((:OFF . 0)
    (:RESERVED . 1)
    (:ON . 2)
    (:RESERVED_1 . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LowBeam>) ostream)
  "Serializes a message object of type '<LowBeam>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LowBeam>) istream)
  "Deserializes a message object of type '<LowBeam>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LowBeam>)))
  "Returns string type for a message object of type '<LowBeam>"
  "raptor_dbw_msgs/LowBeam")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LowBeam)))
  "Returns string type for a message object of type 'LowBeam"
  "raptor_dbw_msgs/LowBeam")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LowBeam>)))
  "Returns md5sum for a message object of type '<LowBeam>"
  "8826c7708bf89daa736515ad7f74a875")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LowBeam)))
  "Returns md5sum for a message object of type 'LowBeam"
  "8826c7708bf89daa736515ad7f74a875")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LowBeam>)))
  "Returns full string definition for message of type '<LowBeam>"
  (cl:format cl:nil "uint8 status~%~%uint8 OFF = 0~%uint8 RESERVED = 1~%uint8 ON = 2~%uint8 RESERVED_1 = 3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LowBeam)))
  "Returns full string definition for message of type 'LowBeam"
  (cl:format cl:nil "uint8 status~%~%uint8 OFF = 0~%uint8 RESERVED = 1~%uint8 ON = 2~%uint8 RESERVED_1 = 3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LowBeam>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LowBeam>))
  "Converts a ROS message object to a list"
  (cl:list 'LowBeam
    (cl:cons ':status (status msg))
))
