# generated from rosidl_generator_py/resource/_idl.py.em
# with input from slam_interfaces:msg/SLAMMetrics.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SLAMMetrics(type):
    """Metaclass of message 'SLAMMetrics'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('slam_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'slam_interfaces.msg.SLAMMetrics')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__slam_metrics
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__slam_metrics
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__slam_metrics
            cls._TYPE_SUPPORT = module.type_support_msg__msg__slam_metrics
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__slam_metrics

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SLAMMetrics(metaclass=Metaclass_SLAMMetrics):
    """Message class 'SLAMMetrics'."""

    __slots__ = [
        '_ate',
        '_rpe',
        '_drift',
        '_cpu_usage',
        '_memory_usage',
        '_runtime',
        '_thread_count',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'ate': 'double',
        'rpe': 'double',
        'drift': 'double',
        'cpu_usage': 'double',
        'memory_usage': 'double',
        'runtime': 'double',
        'thread_count': 'int32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.ate = kwargs.get('ate', float())
        self.rpe = kwargs.get('rpe', float())
        self.drift = kwargs.get('drift', float())
        self.cpu_usage = kwargs.get('cpu_usage', float())
        self.memory_usage = kwargs.get('memory_usage', float())
        self.runtime = kwargs.get('runtime', float())
        self.thread_count = kwargs.get('thread_count', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.ate != other.ate:
            return False
        if self.rpe != other.rpe:
            return False
        if self.drift != other.drift:
            return False
        if self.cpu_usage != other.cpu_usage:
            return False
        if self.memory_usage != other.memory_usage:
            return False
        if self.runtime != other.runtime:
            return False
        if self.thread_count != other.thread_count:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def ate(self):
        """Message field 'ate'."""
        return self._ate

    @ate.setter
    def ate(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'ate' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ate' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ate = value

    @builtins.property
    def rpe(self):
        """Message field 'rpe'."""
        return self._rpe

    @rpe.setter
    def rpe(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'rpe' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'rpe' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._rpe = value

    @builtins.property
    def drift(self):
        """Message field 'drift'."""
        return self._drift

    @drift.setter
    def drift(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'drift' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'drift' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._drift = value

    @builtins.property
    def cpu_usage(self):
        """Message field 'cpu_usage'."""
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'cpu_usage' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cpu_usage' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cpu_usage = value

    @builtins.property
    def memory_usage(self):
        """Message field 'memory_usage'."""
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'memory_usage' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'memory_usage' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._memory_usage = value

    @builtins.property
    def runtime(self):
        """Message field 'runtime'."""
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'runtime' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'runtime' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._runtime = value

    @builtins.property
    def thread_count(self):
        """Message field 'thread_count'."""
        return self._thread_count

    @thread_count.setter
    def thread_count(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'thread_count' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'thread_count' field must be an integer in [-2147483648, 2147483647]"
        self._thread_count = value
