# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from raptor_dbw_msgs/GearReport.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import raptor_dbw_msgs.msg
import std_msgs.msg

class GearReport(genpy.Message):
  _md5sum = "58fab7f1901e8cb7a5ef240558513b10"
  _type = "raptor_dbw_msgs/GearReport"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

# Current gear enumeration
Gear state

# Gear reject flag
bool reject

# Status
bool driver_activity
bool enabled

# Faults
bool gear_select_system_fault
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
MSG: raptor_dbw_msgs/Gear
uint8 gear

uint8 NONE=0
uint8 PARK=1
uint8 REVERSE=2
uint8 NEUTRAL=3
uint8 DRIVE=4
uint8 LOW=5
"""
  __slots__ = ['header','state','reject','driver_activity','enabled','gear_select_system_fault']
  _slot_types = ['std_msgs/Header','raptor_dbw_msgs/Gear','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,state,reject,driver_activity,enabled,gear_select_system_fault

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GearReport, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.state is None:
        self.state = raptor_dbw_msgs.msg.Gear()
      if self.reject is None:
        self.reject = False
      if self.driver_activity is None:
        self.driver_activity = False
      if self.enabled is None:
        self.enabled = False
      if self.gear_select_system_fault is None:
        self.gear_select_system_fault = False
    else:
      self.header = std_msgs.msg.Header()
      self.state = raptor_dbw_msgs.msg.Gear()
      self.reject = False
      self.driver_activity = False
      self.enabled = False
      self.gear_select_system_fault = False

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
      buff.write(_get_struct_5B().pack(_x.state.gear, _x.reject, _x.driver_activity, _x.enabled, _x.gear_select_system_fault))
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
      if self.state is None:
        self.state = raptor_dbw_msgs.msg.Gear()
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
      end += 5
      (_x.state.gear, _x.reject, _x.driver_activity, _x.enabled, _x.gear_select_system_fault,) = _get_struct_5B().unpack(str[start:end])
      self.reject = bool(self.reject)
      self.driver_activity = bool(self.driver_activity)
      self.enabled = bool(self.enabled)
      self.gear_select_system_fault = bool(self.gear_select_system_fault)
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
      buff.write(_get_struct_5B().pack(_x.state.gear, _x.reject, _x.driver_activity, _x.enabled, _x.gear_select_system_fault))
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
      if self.state is None:
        self.state = raptor_dbw_msgs.msg.Gear()
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
      end += 5
      (_x.state.gear, _x.reject, _x.driver_activity, _x.enabled, _x.gear_select_system_fault,) = _get_struct_5B().unpack(str[start:end])
      self.reject = bool(self.reject)
      self.driver_activity = bool(self.driver_activity)
      self.enabled = bool(self.enabled)
      self.gear_select_system_fault = bool(self.gear_select_system_fault)
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
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B