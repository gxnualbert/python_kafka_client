# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fsp-gs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fsp_common_pb2oooo as fsp__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fsp-gs.proto',
  package='com.fsmeeting.fsp.proto.gs',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x66sp-gs.proto\x12\x1a\x63om.fsmeeting.fsp.proto.gs\x1a\x10\x66sp-common.proto\"\xba\x01\n\x13NotifyPublishStream\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x1c\n\x14stream_publish_token\x18\x02 \x01(\t\x12\x10\n\x08group_id\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x10\n\x08media_id\x18\x05 \x01(\x05\x12=\n\nmedia_type\x18\x06 \x01(\x0e\x32).com.fsmeeting.fsp.proto.common.MediaType\"Z\n\x16NotifyPublishStreamRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"E\n\x18NotifyStreamSendingStart\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12\x16\n\x0erecv_client_id\x18\x01 \x01(\t\"_\n\x1bNotifyStreamSendingStartRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse\"D\n\x17NotifyStreamSendingStop\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x16\n\x0erecv_client_id\x18\x02 \x01(\t\"^\n\x1aNotifyStreamSendingStopRsp\x12@\n\x08response\x18\x01 \x01(\x0b\x32..com.fsmeeting.fsp.proto.common.CommonResponse*\x81\x02\n\x0fProtoDictionary\x12\x19\n\x15\x45num2UnknownInterface\x10\x00\x12\x1d\n\x18\x45num2NotifyPublishStream\x10\xa0\x1f\x12 \n\x1b\x45num2NotifyPublishStreamRsp\x10\xa1\x1f\x12\"\n\x1d\x45num2NotifyStreamSendingStart\x10\xa2\x1f\x12%\n Enum2NotifyStreamSendingStartRsp\x10\xa3\x1f\x12!\n\x1c\x45num2NotifyStreamSendingStop\x10\xa4\x1f\x12$\n\x1f\x45num2NotifyStreamSendingStopRsp\x10\xa5\x1f\x42\'\n\x1a\x63om.fsmeeting.fsp.proto.gsP\x01\xf8\x01\x01\xa2\x02\x03GPBb\x06proto3')
  ,
  dependencies=[fsp__common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PROTODICTIONARY = _descriptor.EnumDescriptor(
  name='ProtoDictionary',
  full_name='com.fsmeeting.fsp.proto.gs.ProtoDictionary',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Enum2UnknownInterface', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyPublishStream', index=1, number=4000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyPublishStreamRsp', index=2, number=4001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStart', index=3, number=4002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStartRsp', index=4, number=4003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStop', index=5, number=4004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enum2NotifyStreamSendingStopRsp', index=6, number=4005,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=678,
  serialized_end=935,
)
_sym_db.RegisterEnumDescriptor(_PROTODICTIONARY)

ProtoDictionary = enum_type_wrapper.EnumTypeWrapper(_PROTODICTIONARY)
Enum2UnknownInterface = 0
Enum2NotifyPublishStream = 4000
Enum2NotifyPublishStreamRsp = 4001
Enum2NotifyStreamSendingStart = 4002
Enum2NotifyStreamSendingStartRsp = 4003
Enum2NotifyStreamSendingStop = 4004
Enum2NotifyStreamSendingStopRsp = 4005



_NOTIFYPUBLISHSTREAM = _descriptor.Descriptor(
  name='NotifyPublishStream',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_publish_token', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.stream_publish_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.group_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.media_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_type', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStream.media_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=249,
)


_NOTIFYPUBLISHSTREAMRSP = _descriptor.Descriptor(
  name='NotifyPublishStreamRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=341,
)


_NOTIFYSTREAMSENDINGSTART = _descriptor.Descriptor(
  name='NotifyStreamSendingStart',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart.stream_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart.recv_client_id', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=412,
)


_NOTIFYSTREAMSENDINGSTARTRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStartRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=509,
)


_NOTIFYSTREAMSENDINGSTOP = _descriptor.Descriptor(
  name='NotifyStreamSendingStop',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop.stream_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recv_client_id', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop.recv_client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=579,
)


_NOTIFYSTREAMSENDINGSTOPRSP = _descriptor.Descriptor(
  name='NotifyStreamSendingStopRsp',
  full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=675,
)

_NOTIFYPUBLISHSTREAM.fields_by_name['media_type'].enum_type = fsp__common__pb2._MEDIATYPE
_NOTIFYPUBLISHSTREAMRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTARTRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
_NOTIFYSTREAMSENDINGSTOPRSP.fields_by_name['response'].message_type = fsp__common__pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['NotifyPublishStream'] = _NOTIFYPUBLISHSTREAM
DESCRIPTOR.message_types_by_name['NotifyPublishStreamRsp'] = _NOTIFYPUBLISHSTREAMRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStart'] = _NOTIFYSTREAMSENDINGSTART
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStartRsp'] = _NOTIFYSTREAMSENDINGSTARTRSP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStop'] = _NOTIFYSTREAMSENDINGSTOP
DESCRIPTOR.message_types_by_name['NotifyStreamSendingStopRsp'] = _NOTIFYSTREAMSENDINGSTOPRSP
DESCRIPTOR.enum_types_by_name['ProtoDictionary'] = _PROTODICTIONARY

NotifyPublishStream = _reflection.GeneratedProtocolMessageType('NotifyPublishStream', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYPUBLISHSTREAM,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyPublishStream)
  ))
_sym_db.RegisterMessage(NotifyPublishStream)

NotifyPublishStreamRsp = _reflection.GeneratedProtocolMessageType('NotifyPublishStreamRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYPUBLISHSTREAMRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyPublishStreamRsp)
  ))
_sym_db.RegisterMessage(NotifyPublishStreamRsp)

NotifyStreamSendingStart = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStart', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTART,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStart)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStart)

NotifyStreamSendingStartRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStartRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTARTRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStartRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStartRsp)

NotifyStreamSendingStop = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStop', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStop)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStop)

NotifyStreamSendingStopRsp = _reflection.GeneratedProtocolMessageType('NotifyStreamSendingStopRsp', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSTREAMSENDINGSTOPRSP,
  __module__ = 'fsp_gs_pb2'
  # @@protoc_insertion_point(class_scope:com.fsmeeting.fsp.proto.gs.NotifyStreamSendingStopRsp)
  ))
_sym_db.RegisterMessage(NotifyStreamSendingStopRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.fsmeeting.fsp.proto.gsP\001\370\001\001\242\002\003GPB'))
# @@protoc_insertion_point(module_scope)
