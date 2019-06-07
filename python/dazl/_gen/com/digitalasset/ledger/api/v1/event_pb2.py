# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/digitalasset/ledger/api/v1/event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/digitalasset/ledger/api/v1/event.proto',
  package='com.digitalasset.ledger.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\036com.digitalasset.ledger.api.v1B\017EventOuterClass'),
  serialized_pb=_b('\n*com/digitalasset/ledger/api/v1/event.proto\x12\x1e\x63om.digitalasset.ledger.api.v1\x1a*com/digitalasset/ledger/api/v1/value.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa5\x01\n\x05\x45vent\x12?\n\x07\x63reated\x18\x01 \x01(\x0b\x32,.com.digitalasset.ledger.api.v1.CreatedEventH\x00\x12\x41\n\x08\x61rchived\x18\x03 \x01(\x0b\x32-.com.digitalasset.ledger.api.v1.ArchivedEventH\x00\x42\x07\n\x05\x65ventJ\x04\x08\x02\x10\x03R\texercised\"\x87\x02\n\x0c\x43reatedEvent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\t\x12?\n\x0btemplate_id\x18\x03 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12@\n\x10\x63reate_arguments\x18\x04 \x01(\x0b\x32&.com.digitalasset.ledger.api.v1.Record\x12\x17\n\x0fwitness_parties\x18\x05 \x03(\t\x12\x34\n\x0e\x61greement_text\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x90\x01\n\rArchivedEvent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\t\x12?\n\x0btemplate_id\x18\x03 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12\x17\n\x0fwitness_parties\x18\x04 \x03(\t\"\x8f\x03\n\x0e\x45xercisedEvent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\t\x12?\n\x0btemplate_id\x18\x03 \x01(\x0b\x32*.com.digitalasset.ledger.api.v1.Identifier\x12\"\n\x1a\x63ontract_creating_event_id\x18\x04 \x01(\t\x12\x0e\n\x06\x63hoice\x18\x05 \x01(\t\x12>\n\x0f\x63hoice_argument\x18\x06 \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.Value\x12\x16\n\x0e\x61\x63ting_parties\x18\x07 \x03(\t\x12\x11\n\tconsuming\x18\x08 \x01(\x08\x12\x17\n\x0fwitness_parties\x18\n \x03(\t\x12\x17\n\x0f\x63hild_event_ids\x18\x0b \x03(\t\x12>\n\x0f\x65xercise_result\x18\x0c \x01(\x0b\x32%.com.digitalasset.ledger.api.v1.ValueJ\x04\x08\t\x10\nB1\n\x1e\x63om.digitalasset.ledger.api.v1B\x0f\x45ventOuterClassb\x06proto3')
  ,
  dependencies=[com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='com.digitalasset.ledger.api.v1.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='com.digitalasset.ledger.api.v1.Event.created', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='archived', full_name='com.digitalasset.ledger.api.v1.Event.archived', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='com.digitalasset.ledger.api.v1.Event.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=155,
  serialized_end=320,
)


_CREATEDEVENT = _descriptor.Descriptor(
  name='CreatedEvent',
  full_name='com.digitalasset.ledger.api.v1.CreatedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_arguments', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.create_arguments', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.witness_parties', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agreement_text', full_name='com.digitalasset.ledger.api.v1.CreatedEvent.agreement_text', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=586,
)


_ARCHIVEDEVENT = _descriptor.Descriptor(
  name='ArchivedEvent',
  full_name='com.digitalasset.ledger.api.v1.ArchivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.digitalasset.ledger.api.v1.ArchivedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.digitalasset.ledger.api.v1.ArchivedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.digitalasset.ledger.api.v1.ArchivedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.digitalasset.ledger.api.v1.ArchivedEvent.witness_parties', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=733,
)


_EXERCISEDEVENT = _descriptor.Descriptor(
  name='ExercisedEvent',
  full_name='com.digitalasset.ledger.api.v1.ExercisedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_creating_event_id', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.contract_creating_event_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choice', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.choice', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choice_argument', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.choice_argument', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acting_parties', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.acting_parties', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consuming', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.consuming', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.witness_parties', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_event_ids', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.child_event_ids', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exercise_result', full_name='com.digitalasset.ledger.api.v1.ExercisedEvent.exercise_result', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=736,
  serialized_end=1135,
)

_EVENT.fields_by_name['created'].message_type = _CREATEDEVENT
_EVENT.fields_by_name['archived'].message_type = _ARCHIVEDEVENT
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['created'])
_EVENT.fields_by_name['created'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['archived'])
_EVENT.fields_by_name['archived'].containing_oneof = _EVENT.oneofs_by_name['event']
_CREATEDEVENT.fields_by_name['template_id'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_CREATEDEVENT.fields_by_name['create_arguments'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._RECORD
_CREATEDEVENT.fields_by_name['agreement_text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ARCHIVEDEVENT.fields_by_name['template_id'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISEDEVENT.fields_by_name['template_id'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISEDEVENT.fields_by_name['choice_argument'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_EXERCISEDEVENT.fields_by_name['exercise_result'].message_type = com_dot_digitalasset_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['CreatedEvent'] = _CREATEDEVENT
DESCRIPTOR.message_types_by_name['ArchivedEvent'] = _ARCHIVEDEVENT
DESCRIPTOR.message_types_by_name['ExercisedEvent'] = _EXERCISEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'com.digitalasset.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.Event)
  ))
_sym_db.RegisterMessage(Event)

CreatedEvent = _reflection.GeneratedProtocolMessageType('CreatedEvent', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDEVENT,
  __module__ = 'com.digitalasset.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.CreatedEvent)
  ))
_sym_db.RegisterMessage(CreatedEvent)

ArchivedEvent = _reflection.GeneratedProtocolMessageType('ArchivedEvent', (_message.Message,), dict(
  DESCRIPTOR = _ARCHIVEDEVENT,
  __module__ = 'com.digitalasset.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.ArchivedEvent)
  ))
_sym_db.RegisterMessage(ArchivedEvent)

ExercisedEvent = _reflection.GeneratedProtocolMessageType('ExercisedEvent', (_message.Message,), dict(
  DESCRIPTOR = _EXERCISEDEVENT,
  __module__ = 'com.digitalasset.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.digitalasset.ledger.api.v1.ExercisedEvent)
  ))
_sym_db.RegisterMessage(ExercisedEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)