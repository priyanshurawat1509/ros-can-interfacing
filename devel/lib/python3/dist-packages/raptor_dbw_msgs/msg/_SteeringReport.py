# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from raptor_dbw_msgs/SteeringReport.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import raptor_dbw_msgs.msg
import std_msgs.msg

class SteeringReport(genpy.Message):
  _md5sum = "591f9fcdf310bb0c5cda95f4d6f03ec2"
  _type = "raptor_dbw_msgs/SteeringReport"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

# Steering Wheel
float32 steering_wheel_angle      # degrees
float32 steering_wheel_angle_cmd  # degrees
float32 steering_wheel_torque     # 0 to 100%

# Status
bool enabled  
bool driver_activity

bool fault_steering_system

bool overheat_prevention_mode

uint8 rolling_counter

ActuatorControlMode control_type

bool steering_overheat_warning

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: raptor_dbw_msgs/ActuatorControlMode
uint8 value

uint8 open_loop = 0
uint8 closed_loop_actuator = 1
uint8 closed_loop_vehicle = 2
uint8 none = 255"""
  __slots__ = ['header','steering_wheel_angle','steering_wheel_angle_cmd','steering_wheel_torque','enabled','driver_activity','fault_steering_system','overheat_prevention_mode','rolling_counter','control_type','steering_overheat_warning']
  _slot_types = ['std_msgs/Header','float32','float32','float32','bool','bool','bool','bool','uint8','raptor_dbw_msgs/ActuatorControlMode','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,steering_wheel_angle,steering_wheel_angle_cmd,steering_wheel_torque,enabled,driver_activity,fault_steering_system,overheat_prevention_mode,rolling_counter,control_type,steering_overheat_warning

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SteeringReport, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.steering_wheel_angle is None:
        self.steering_wheel_angle = 0.
      if self.steering_wheel_angle_cmd is None:
        self.steering_wheel_angle_cmd = 0.
      if self.steering_wheel_torque is None:
        self.steering_wheel_torque = 0.
      if self.enabled is None:
        self.enabled = False
      if self.driver_activity is None:
        self.driver_activity = False
      if self.fault_steering_system is None:
        self.fault_steering_system = False
      if self.overheat_prevention_mode is None:
        self.overheat_prevention_mode = False
      if self.rolling_counter is None:
        self.rolling_counter = 0
      if self.control_type is None:
        self.control_type = raptor_dbw_msgs.msg.ActuatorControlMode()
      if self.steering_overheat_warning is None:
        self.steering_overheat_warning = False
    else:
      self.header = std_msgs.msg.Header()
      self.steering_wheel_angle = 0.
      self.steering_wheel_angle_cmd = 0.
      self.steering_wheel_torque = 0.
      self.enabled = False
      self.driver_activity = False
      self.fault_steering_system = False
      self.overheat_prevention_mode = False
      self.rolling_counter = 0
      self.control_type = raptor_dbw_msgs.msg.ActuatorControlMode()
      self.steering_overheat_warning = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f7B().pack(_x.steering_wheel_angle, _x.steering_wheel_angle_cmd, _x.steering_wheel_torque, _x.enabled, _x.driver_activity, _x.fault_steering_system, _x.overheat_prevention_mode, _x.rolling_counter, _x.control_type.value, _x.steering_overheat_warning))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.control_type is None:
        self.control_type = raptor_dbw_msgs.msg.ActuatorControlMode()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 19
      (_x.steering_wheel_angle, _x.steering_wheel_angle_cmd, _x.steering_wheel_torque, _x.enabled, _x.driver_activity, _x.fault_steering_system, _x.overheat_prevention_mode, _x.rolling_counter, _x.control_type.value, _x.steering_overheat_warning,) = _get_struct_3f7B().unpack(str[start:end])
      self.enabled = bool(self.enabled)
      self.driver_activity = bool(self.driver_activity)
      self.fault_steering_system = bool(self.fault_steering_system)
      self.overheat_prevention_mode = bool(self.overheat_prevention_mode)
      self.steering_overheat_warning = bool(self.steering_overheat_warning)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3f7B().pack(_x.steering_wheel_angle, _x.steering_wheel_angle_cmd, _x.steering_wheel_torque, _x.enabled, _x.driver_activity, _x.fault_steering_system, _x.overheat_prevention_mode, _x.rolling_counter, _x.control_type.value, _x.steering_overheat_warning))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.control_type is None:
        self.control_type = raptor_dbw_msgs.msg.ActuatorControlMode()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 19
      (_x.steering_wheel_angle, _x.steering_wheel_angle_cmd, _x.steering_wheel_torque, _x.enabled, _x.driver_activity, _x.fault_steering_system, _x.overheat_prevention_mode, _x.rolling_counter, _x.control_type.value, _x.steering_overheat_warning,) = _get_struct_3f7B().unpack(str[start:end])
      self.enabled = bool(self.enabled)
      self.driver_activity = bool(self.driver_activity)
      self.fault_steering_system = bool(self.fault_steering_system)
      self.overheat_prevention_mode = bool(self.overheat_prevention_mode)
      self.steering_overheat_warning = bool(self.steering_overheat_warning)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3f7B = None
def _get_struct_3f7B():
    global _struct_3f7B
    if _struct_3f7B is None:
        _struct_3f7B = struct.Struct("<3f7B")
    return _struct_3f7B