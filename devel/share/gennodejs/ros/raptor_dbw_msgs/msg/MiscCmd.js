// Auto-generated. Do not edit!

// (in-package raptor_dbw_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let TurnSignal = require('./TurnSignal.js');
let DoorRequest = require('./DoorRequest.js');
let HighBeam = require('./HighBeam.js');
let WiperFront = require('./WiperFront.js');
let WiperRear = require('./WiperRear.js');
let Ignition = require('./Ignition.js');
let LowBeam = require('./LowBeam.js');

//-----------------------------------------------------------

class MiscCmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cmd = null;
      this.door_request_right_rear = null;
      this.rolling_counter = null;
      this.high_beam_cmd = null;
      this.front_wiper_cmd = null;
      this.rear_wiper_cmd = null;
      this.ignition_cmd = null;
      this.door_request_left_rear = null;
      this.door_request_lift_gate = null;
      this.block_standard_cruise_buttons = null;
      this.block_adaptive_cruise_buttons = null;
      this.block_turn_signal_stalk = null;
      this.horn_cmd = null;
      this.low_beam_cmd = null;
    }
    else {
      if (initObj.hasOwnProperty('cmd')) {
        this.cmd = initObj.cmd
      }
      else {
        this.cmd = new TurnSignal();
      }
      if (initObj.hasOwnProperty('door_request_right_rear')) {
        this.door_request_right_rear = initObj.door_request_right_rear
      }
      else {
        this.door_request_right_rear = new DoorRequest();
      }
      if (initObj.hasOwnProperty('rolling_counter')) {
        this.rolling_counter = initObj.rolling_counter
      }
      else {
        this.rolling_counter = 0;
      }
      if (initObj.hasOwnProperty('high_beam_cmd')) {
        this.high_beam_cmd = initObj.high_beam_cmd
      }
      else {
        this.high_beam_cmd = new HighBeam();
      }
      if (initObj.hasOwnProperty('front_wiper_cmd')) {
        this.front_wiper_cmd = initObj.front_wiper_cmd
      }
      else {
        this.front_wiper_cmd = new WiperFront();
      }
      if (initObj.hasOwnProperty('rear_wiper_cmd')) {
        this.rear_wiper_cmd = initObj.rear_wiper_cmd
      }
      else {
        this.rear_wiper_cmd = new WiperRear();
      }
      if (initObj.hasOwnProperty('ignition_cmd')) {
        this.ignition_cmd = initObj.ignition_cmd
      }
      else {
        this.ignition_cmd = new Ignition();
      }
      if (initObj.hasOwnProperty('door_request_left_rear')) {
        this.door_request_left_rear = initObj.door_request_left_rear
      }
      else {
        this.door_request_left_rear = new DoorRequest();
      }
      if (initObj.hasOwnProperty('door_request_lift_gate')) {
        this.door_request_lift_gate = initObj.door_request_lift_gate
      }
      else {
        this.door_request_lift_gate = new DoorRequest();
      }
      if (initObj.hasOwnProperty('block_standard_cruise_buttons')) {
        this.block_standard_cruise_buttons = initObj.block_standard_cruise_buttons
      }
      else {
        this.block_standard_cruise_buttons = false;
      }
      if (initObj.hasOwnProperty('block_adaptive_cruise_buttons')) {
        this.block_adaptive_cruise_buttons = initObj.block_adaptive_cruise_buttons
      }
      else {
        this.block_adaptive_cruise_buttons = false;
      }
      if (initObj.hasOwnProperty('block_turn_signal_stalk')) {
        this.block_turn_signal_stalk = initObj.block_turn_signal_stalk
      }
      else {
        this.block_turn_signal_stalk = false;
      }
      if (initObj.hasOwnProperty('horn_cmd')) {
        this.horn_cmd = initObj.horn_cmd
      }
      else {
        this.horn_cmd = false;
      }
      if (initObj.hasOwnProperty('low_beam_cmd')) {
        this.low_beam_cmd = initObj.low_beam_cmd
      }
      else {
        this.low_beam_cmd = new LowBeam();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MiscCmd
    // Serialize message field [cmd]
    bufferOffset = TurnSignal.serialize(obj.cmd, buffer, bufferOffset);
    // Serialize message field [door_request_right_rear]
    bufferOffset = DoorRequest.serialize(obj.door_request_right_rear, buffer, bufferOffset);
    // Serialize message field [rolling_counter]
    bufferOffset = _serializer.uint8(obj.rolling_counter, buffer, bufferOffset);
    // Serialize message field [high_beam_cmd]
    bufferOffset = HighBeam.serialize(obj.high_beam_cmd, buffer, bufferOffset);
    // Serialize message field [front_wiper_cmd]
    bufferOffset = WiperFront.serialize(obj.front_wiper_cmd, buffer, bufferOffset);
    // Serialize message field [rear_wiper_cmd]
    bufferOffset = WiperRear.serialize(obj.rear_wiper_cmd, buffer, bufferOffset);
    // Serialize message field [ignition_cmd]
    bufferOffset = Ignition.serialize(obj.ignition_cmd, buffer, bufferOffset);
    // Serialize message field [door_request_left_rear]
    bufferOffset = DoorRequest.serialize(obj.door_request_left_rear, buffer, bufferOffset);
    // Serialize message field [door_request_lift_gate]
    bufferOffset = DoorRequest.serialize(obj.door_request_lift_gate, buffer, bufferOffset);
    // Serialize message field [block_standard_cruise_buttons]
    bufferOffset = _serializer.bool(obj.block_standard_cruise_buttons, buffer, bufferOffset);
    // Serialize message field [block_adaptive_cruise_buttons]
    bufferOffset = _serializer.bool(obj.block_adaptive_cruise_buttons, buffer, bufferOffset);
    // Serialize message field [block_turn_signal_stalk]
    bufferOffset = _serializer.bool(obj.block_turn_signal_stalk, buffer, bufferOffset);
    // Serialize message field [horn_cmd]
    bufferOffset = _serializer.bool(obj.horn_cmd, buffer, bufferOffset);
    // Serialize message field [low_beam_cmd]
    bufferOffset = LowBeam.serialize(obj.low_beam_cmd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MiscCmd
    let len;
    let data = new MiscCmd(null);
    // Deserialize message field [cmd]
    data.cmd = TurnSignal.deserialize(buffer, bufferOffset);
    // Deserialize message field [door_request_right_rear]
    data.door_request_right_rear = DoorRequest.deserialize(buffer, bufferOffset);
    // Deserialize message field [rolling_counter]
    data.rolling_counter = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [high_beam_cmd]
    data.high_beam_cmd = HighBeam.deserialize(buffer, bufferOffset);
    // Deserialize message field [front_wiper_cmd]
    data.front_wiper_cmd = WiperFront.deserialize(buffer, bufferOffset);
    // Deserialize message field [rear_wiper_cmd]
    data.rear_wiper_cmd = WiperRear.deserialize(buffer, bufferOffset);
    // Deserialize message field [ignition_cmd]
    data.ignition_cmd = Ignition.deserialize(buffer, bufferOffset);
    // Deserialize message field [door_request_left_rear]
    data.door_request_left_rear = DoorRequest.deserialize(buffer, bufferOffset);
    // Deserialize message field [door_request_lift_gate]
    data.door_request_lift_gate = DoorRequest.deserialize(buffer, bufferOffset);
    // Deserialize message field [block_standard_cruise_buttons]
    data.block_standard_cruise_buttons = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [block_adaptive_cruise_buttons]
    data.block_adaptive_cruise_buttons = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [block_turn_signal_stalk]
    data.block_turn_signal_stalk = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [horn_cmd]
    data.horn_cmd = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [low_beam_cmd]
    data.low_beam_cmd = LowBeam.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'raptor_dbw_msgs/MiscCmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1267e40afe4289757af3bbfb5a1352fe';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Turn signal command enumeration
    TurnSignal cmd
    
    DoorRequest door_request_right_rear
    
    uint8 rolling_counter
    
    HighBeam high_beam_cmd
    
    WiperFront front_wiper_cmd
    
    WiperRear rear_wiper_cmd
    
    Ignition ignition_cmd
    DoorRequest door_request_left_rear
    DoorRequest door_request_lift_gate
    
    bool block_standard_cruise_buttons
    bool block_adaptive_cruise_buttons
    bool block_turn_signal_stalk
    
    bool horn_cmd
    
    LowBeam low_beam_cmd
    
    ================================================================================
    MSG: raptor_dbw_msgs/TurnSignal
    uint8 value
    
    uint8 NONE = 0
    uint8 LEFT = 1
    uint8 RIGHT = 2
    uint8 HAZARDS = 3
    uint8 SNA = 7
    ================================================================================
    MSG: raptor_dbw_msgs/DoorRequest
    uint8 value
    
    uint8 NO_REQUEST=0
    uint8 LIFTGATE_TOGGLE=1
    uint8 LR_DOOR_TOGGLE=2
    uint8 RR_DOOR_TOGGLE=3
    ================================================================================
    MSG: raptor_dbw_msgs/HighBeam
    uint8 status
    
    uint8 OFF = 0
    uint8 ON = 1
    uint8 FORCE_ON = 2
    uint8 RESERVED = 3
    
    ================================================================================
    MSG: raptor_dbw_msgs/WiperFront
    uint8 status
    
    uint8 OFF = 0
    uint8 INTERVAL_1 = 1
    uint8 INTERVAL_2 = 2
    uint8 INTERVAL_3 = 3
    uint8 INTERVAL_4 = 4
    uint8 INTERVAL_5 = 5
    uint8 INTERVAL_6 = 6
    uint8 CONSTANT_LOW = 11
    uint8 CONSTANT_HIGH = 12
    uint8 WASH_BRIEF = 13
    uint8 WASH_CONTINUOUS = 14
    uint8 SNA = 15
    ================================================================================
    MSG: raptor_dbw_msgs/WiperRear
    uint8 status
    
    uint8 OFF = 0
    uint8 INTERVAL_1 = 1
    uint8 CONSTANT_LOW = 11
    uint8 CONSTANT_HIGH = 12
    uint8 WASH_BRIEF = 13
    uint8 WASH_CONTINUOUS = 14
    uint8 SNA = 15
    ================================================================================
    MSG: raptor_dbw_msgs/Ignition
    uint8 status
    
    uint8 NO_REQUEST = 0
    uint8 FORCE_OFF = 1
    uint8 ACCESSORY = 2
    uint8 RUN = 3
    uint8 CRANK = 4
    ================================================================================
    MSG: raptor_dbw_msgs/LowBeam
    uint8 status
    
    uint8 OFF = 0
    uint8 RESERVED = 1
    uint8 ON = 2
    uint8 RESERVED_1 = 3
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MiscCmd(null);
    if (msg.cmd !== undefined) {
      resolved.cmd = TurnSignal.Resolve(msg.cmd)
    }
    else {
      resolved.cmd = new TurnSignal()
    }

    if (msg.door_request_right_rear !== undefined) {
      resolved.door_request_right_rear = DoorRequest.Resolve(msg.door_request_right_rear)
    }
    else {
      resolved.door_request_right_rear = new DoorRequest()
    }

    if (msg.rolling_counter !== undefined) {
      resolved.rolling_counter = msg.rolling_counter;
    }
    else {
      resolved.rolling_counter = 0
    }

    if (msg.high_beam_cmd !== undefined) {
      resolved.high_beam_cmd = HighBeam.Resolve(msg.high_beam_cmd)
    }
    else {
      resolved.high_beam_cmd = new HighBeam()
    }

    if (msg.front_wiper_cmd !== undefined) {
      resolved.front_wiper_cmd = WiperFront.Resolve(msg.front_wiper_cmd)
    }
    else {
      resolved.front_wiper_cmd = new WiperFront()
    }

    if (msg.rear_wiper_cmd !== undefined) {
      resolved.rear_wiper_cmd = WiperRear.Resolve(msg.rear_wiper_cmd)
    }
    else {
      resolved.rear_wiper_cmd = new WiperRear()
    }

    if (msg.ignition_cmd !== undefined) {
      resolved.ignition_cmd = Ignition.Resolve(msg.ignition_cmd)
    }
    else {
      resolved.ignition_cmd = new Ignition()
    }

    if (msg.door_request_left_rear !== undefined) {
      resolved.door_request_left_rear = DoorRequest.Resolve(msg.door_request_left_rear)
    }
    else {
      resolved.door_request_left_rear = new DoorRequest()
    }

    if (msg.door_request_lift_gate !== undefined) {
      resolved.door_request_lift_gate = DoorRequest.Resolve(msg.door_request_lift_gate)
    }
    else {
      resolved.door_request_lift_gate = new DoorRequest()
    }

    if (msg.block_standard_cruise_buttons !== undefined) {
      resolved.block_standard_cruise_buttons = msg.block_standard_cruise_buttons;
    }
    else {
      resolved.block_standard_cruise_buttons = false
    }

    if (msg.block_adaptive_cruise_buttons !== undefined) {
      resolved.block_adaptive_cruise_buttons = msg.block_adaptive_cruise_buttons;
    }
    else {
      resolved.block_adaptive_cruise_buttons = false
    }

    if (msg.block_turn_signal_stalk !== undefined) {
      resolved.block_turn_signal_stalk = msg.block_turn_signal_stalk;
    }
    else {
      resolved.block_turn_signal_stalk = false
    }

    if (msg.horn_cmd !== undefined) {
      resolved.horn_cmd = msg.horn_cmd;
    }
    else {
      resolved.horn_cmd = false
    }

    if (msg.low_beam_cmd !== undefined) {
      resolved.low_beam_cmd = LowBeam.Resolve(msg.low_beam_cmd)
    }
    else {
      resolved.low_beam_cmd = new LowBeam()
    }

    return resolved;
    }
};

module.exports = MiscCmd;
