// Generated by gencpp from file pdu_msgs/RelayStatus.msg
// DO NOT EDIT!


#ifndef PDU_MSGS_MESSAGE_RELAYSTATUS_H
#define PDU_MSGS_MESSAGE_RELAYSTATUS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pdu_msgs
{
template <class ContainerAllocator>
struct RelayStatus_
{
  typedef RelayStatus_<ContainerAllocator> Type;

  RelayStatus_()
    : value(0)  {
    }
  RelayStatus_(const ContainerAllocator& _alloc)
    : value(0)  {
  (void)_alloc;
    }



   typedef uint8_t _value_type;
  _value_type value;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(OK)
  #undef OK
#endif
#if defined(_WIN32) && defined(RELAY_COIL_OPEN)
  #undef RELAY_COIL_OPEN
#endif
#if defined(_WIN32) && defined(RELAY_COIL_SHORTED)
  #undef RELAY_COIL_SHORTED
#endif
#if defined(_WIN32) && defined(NORM_OPEN_RELAY_OPEN)
  #undef NORM_OPEN_RELAY_OPEN
#endif
#if defined(_WIN32) && defined(NORM_CLOSED_RELAY_OPEN)
  #undef NORM_CLOSED_RELAY_OPEN
#endif
#if defined(_WIN32) && defined(COIL_NOT_POWERED)
  #undef COIL_NOT_POWERED
#endif
#if defined(_WIN32) && defined(NORM_OPEN_RELAY_SHORTED)
  #undef NORM_OPEN_RELAY_SHORTED
#endif
#if defined(_WIN32) && defined(NORM_CLOSED_RELAY_SHORTED)
  #undef NORM_CLOSED_RELAY_SHORTED
#endif
#if defined(_WIN32) && defined(RESERVED_01)
  #undef RESERVED_01
#endif
#if defined(_WIN32) && defined(RESERVED_02)
  #undef RESERVED_02
#endif
#if defined(_WIN32) && defined(RESERVED_03)
  #undef RESERVED_03
#endif
#if defined(_WIN32) && defined(HIGH_SIDE_FAULT)
  #undef HIGH_SIDE_FAULT
#endif
#if defined(_WIN32) && defined(HIGH_SIDE_OPEN_LOAD)
  #undef HIGH_SIDE_OPEN_LOAD
#endif
#if defined(_WIN32) && defined(HIGH_SIDE_OVER_VOLTAGE)
  #undef HIGH_SIDE_OVER_VOLTAGE
#endif
#if defined(_WIN32) && defined(RESERVED_04)
  #undef RESERVED_04
#endif
#if defined(_WIN32) && defined(RELAY_LOCATION_NOT_USED)
  #undef RELAY_LOCATION_NOT_USED
#endif

  enum {
    OK = 0u,
    RELAY_COIL_OPEN = 1u,
    RELAY_COIL_SHORTED = 2u,
    NORM_OPEN_RELAY_OPEN = 3u,
    NORM_CLOSED_RELAY_OPEN = 4u,
    COIL_NOT_POWERED = 5u,
    NORM_OPEN_RELAY_SHORTED = 6u,
    NORM_CLOSED_RELAY_SHORTED = 7u,
    RESERVED_01 = 8u,
    RESERVED_02 = 9u,
    RESERVED_03 = 10u,
    HIGH_SIDE_FAULT = 11u,
    HIGH_SIDE_OPEN_LOAD = 12u,
    HIGH_SIDE_OVER_VOLTAGE = 13u,
    RESERVED_04 = 14u,
    RELAY_LOCATION_NOT_USED = 15u,
  };


  typedef boost::shared_ptr< ::pdu_msgs::RelayStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pdu_msgs::RelayStatus_<ContainerAllocator> const> ConstPtr;

}; // struct RelayStatus_

typedef ::pdu_msgs::RelayStatus_<std::allocator<void> > RelayStatus;

typedef boost::shared_ptr< ::pdu_msgs::RelayStatus > RelayStatusPtr;
typedef boost::shared_ptr< ::pdu_msgs::RelayStatus const> RelayStatusConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pdu_msgs::RelayStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pdu_msgs::RelayStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pdu_msgs::RelayStatus_<ContainerAllocator1> & lhs, const ::pdu_msgs::RelayStatus_<ContainerAllocator2> & rhs)
{
  return lhs.value == rhs.value;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pdu_msgs::RelayStatus_<ContainerAllocator1> & lhs, const ::pdu_msgs::RelayStatus_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pdu_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pdu_msgs::RelayStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pdu_msgs::RelayStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pdu_msgs::RelayStatus_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "747c0056a2372beaf7485ce2d5289570";
  }

  static const char* value(const ::pdu_msgs::RelayStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x747c0056a2372beaULL;
  static const uint64_t static_value2 = 0xf7485ce2d5289570ULL;
};

template<class ContainerAllocator>
struct DataType< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pdu_msgs/RelayStatus";
  }

  static const char* value(const ::pdu_msgs::RelayStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 value\n"
"\n"
"uint8 OK = 0\n"
"uint8 RELAY_COIL_OPEN = 1\n"
"uint8 RELAY_COIL_SHORTED = 2\n"
"uint8 NORM_OPEN_RELAY_OPEN = 3\n"
"uint8 NORM_CLOSED_RELAY_OPEN = 4\n"
"uint8 COIL_NOT_POWERED = 5\n"
"uint8 NORM_OPEN_RELAY_SHORTED = 6\n"
"uint8 NORM_CLOSED_RELAY_SHORTED = 7\n"
"uint8 RESERVED_01 = 8\n"
"uint8 RESERVED_02 = 9\n"
"uint8 RESERVED_03 = 10\n"
"uint8 HIGH_SIDE_FAULT = 11\n"
"uint8 HIGH_SIDE_OPEN_LOAD = 12\n"
"uint8 HIGH_SIDE_OVER_VOLTAGE = 13\n"
"uint8 RESERVED_04 = 14\n"
"uint8 RELAY_LOCATION_NOT_USED = 15\n"
;
  }

  static const char* value(const ::pdu_msgs::RelayStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RelayStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pdu_msgs::RelayStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pdu_msgs::RelayStatus_<ContainerAllocator>& v)
  {
    s << indent << "value: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PDU_MSGS_MESSAGE_RELAYSTATUS_H
