# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/mod/v1/another.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="example/mod/v1/another.proto",
    package="example.mod.v1",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1c\x65xample/mod/v1/another.proto\x12\x0e\x65xample.mod.v1"K\n\x0c\x44ummyMessage\x12\x0b\n\x03one\x18\x01 \x01(\x05\x12\r\n\x05thing\x18\x02 \x01(\x03\x12\x11\n\tsomething\x18\x03 \x01(\r\x12\x0c\n\x04\x65lse\x18\x04 \x01(\x04*)\n\x08SomeEnum\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03ONE\x10\x01\x12\x07\n\x03TWO\x10\x02\x32S\n\x0c\x44ummyService\x12\x43\n\x05\x44ummy\x12\x1c.example.mod.v1.DummyMessage\x1a\x1c.example.mod.v1.DummyMessageb\x06proto3',
)

_SOMEENUM = _descriptor.EnumDescriptor(
    name="SomeEnum",
    full_name="example.mod.v1.SomeEnum",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UNKNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ONE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TWO",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=125,
    serialized_end=166,
)
_sym_db.RegisterEnumDescriptor(_SOMEENUM)

SomeEnum = enum_type_wrapper.EnumTypeWrapper(_SOMEENUM)
UNKNOWN = 0
ONE = 1
TWO = 2


_DUMMYMESSAGE = _descriptor.Descriptor(
    name="DummyMessage",
    full_name="example.mod.v1.DummyMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="one",
            full_name="example.mod.v1.DummyMessage.one",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="thing",
            full_name="example.mod.v1.DummyMessage.thing",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="something",
            full_name="example.mod.v1.DummyMessage.something",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="else",
            full_name="example.mod.v1.DummyMessage.else",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=48,
    serialized_end=123,
)

DESCRIPTOR.message_types_by_name["DummyMessage"] = _DUMMYMESSAGE
DESCRIPTOR.enum_types_by_name["SomeEnum"] = _SOMEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DummyMessage = _reflection.GeneratedProtocolMessageType(
    "DummyMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DUMMYMESSAGE,
        "__module__": "example.mod.v1.another_pb2"
        # @@protoc_insertion_point(class_scope:example.mod.v1.DummyMessage)
    },
)
_sym_db.RegisterMessage(DummyMessage)


_DUMMYSERVICE = _descriptor.ServiceDescriptor(
    name="DummyService",
    full_name="example.mod.v1.DummyService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=168,
    serialized_end=251,
    methods=[
        _descriptor.MethodDescriptor(
            name="Dummy",
            full_name="example.mod.v1.DummyService.Dummy",
            index=0,
            containing_service=None,
            input_type=_DUMMYMESSAGE,
            output_type=_DUMMYMESSAGE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_DUMMYSERVICE)

DESCRIPTOR.services_by_name["DummyService"] = _DUMMYSERVICE

# @@protoc_insertion_point(module_scope)
