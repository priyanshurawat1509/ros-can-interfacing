// Auto-generated. Do not edit!

// (in-package raptor_dbw_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class WiperRear {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status = null;
    }
    else {
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WiperRear
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WiperRear
    let len;
    let data = new WiperRear(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'raptor_dbw_msgs/WiperRear';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e49876942de059c3028a2674862072b3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 status
    
    uint8 OFF = 0
    uint8 INTERVAL_1 = 1
    uint8 CONSTANT_LOW = 11
    uint8 CONSTANT_HIGH = 12
    uint8 WASH_BRIEF = 13
    uint8 WASH_CONTINUOUS = 14
    uint8 SNA = 15
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WiperRear(null);
    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = 0
    }

    return resolved;
    }
};

// Constants for message
WiperRear.Constants = {
  OFF: 0,
  INTERVAL_1: 1,
  CONSTANT_LOW: 11,
  CONSTANT_HIGH: 12,
  WASH_BRIEF: 13,
  WASH_CONTINUOUS: 14,
  SNA: 15,
}

module.exports = WiperRear;
