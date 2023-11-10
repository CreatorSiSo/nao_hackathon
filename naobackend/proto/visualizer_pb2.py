# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visualizer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10visualizer.proto\x12\x13protobuf.visualizer\"\"\n\x04Head\x12\x0b\n\x03yaw\x18\x01 \x01(\x02\x12\r\n\x05pitch\x18\x02 \x01(\x02\"t\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\tintParams\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x17\n\x0b\x66loatParams\x18\x03 \x03(\x02\x42\x02\x10\x01\x12)\n\x05\x63olor\x18\x04 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\"3\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\r\x12\t\n\x01g\x18\x02 \x01(\r\x12\t\n\x01\x62\x18\x03 \x01(\r\x12\t\n\x01\x61\x18\x04 \x01(\r\"\xce\x01\n\x06Line2D\x12)\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x02 \x01(\r\x12\n\n\x02x1\x18\x03 \x01(\x02\x12\n\n\x02y1\x18\x04 \x01(\x02\x12\n\n\x02x2\x18\x05 \x01(\x02\x12\n\n\x02y2\x18\x06 \x01(\x02\x12\x32\n\x04type\x18\x07 \x01(\x0e\x32$.protobuf.visualizer.Line2D.LineType\"!\n\x08LineType\x12\n\n\x06NORMAL\x10\x00\x12\t\n\x05\x41RROW\x10\x01\"\xd0\x01\n\nEllipsis2D\x12/\n\x0b\x62orderColor\x18\x01 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12-\n\tfillColor\x18\x02 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x03 \x01(\r\x12\x0f\n\x07\x63\x65nterX\x18\x04 \x01(\x02\x12\x0f\n\x07\x63\x65nterY\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\r\n\x05\x61ngle\x18\x08 \x01(\x02\"\xc8\x01\n\x0bRectangle2D\x12/\n\x0b\x62orderColor\x18\x01 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12-\n\tfillColor\x18\x02 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x03 \x01(\r\x12\x12\n\nupperLeftX\x18\x04 \x01(\x02\x12\x12\n\nupperLeftY\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\"\xc1\x02\n\x05\x41rc2D\x12/\n\x0b\x62orderColor\x18\x01 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12-\n\tfillColor\x18\x02 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x03 \x01(\r\x12\x0f\n\x07\x63\x65nterX\x18\x04 \x01(\x02\x12\x0f\n\x07\x63\x65nterY\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\x12\x12\n\nstartAngle\x18\x08 \x01(\x02\x12\x10\n\x08\x61rcAngle\x18\t \x01(\x02\x12\x32\n\x04type\x18\n \x01(\x0e\x32$.protobuf.visualizer.Arc2D.Arc2DType\")\n\tArc2DType\x12\x08\n\x04OPEN\x10\x00\x12\t\n\x05\x43HORD\x10\x01\x12\x07\n\x03PIE\x10\x02\"y\n\x06Text2D\x12)\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x03 \x01(\r\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01y\x18\x05 \x01(\x02\x12\x0c\n\x04size\x18\x06 \x01(\x02\x12\x0c\n\x04text\x18\x07 \x01(\t\"\xad\x01\n\x08Raster2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x10\n\x08rotation\x18\x03 \x01(\x02\x12\r\n\x05scale\x18\x04 \x01(\x02\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r\x12)\n\x05\x63olor\x18\x07 \x01(\x0b\x32\x1a.protobuf.visualizer.Color\x12\x12\n\nfadingTime\x18\x08 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\t \x03(\r\"\xca\x04\n\x15VisualizerTransaction\x12?\n\x0breplacement\x18\x01 \x01(\x0e\x32*.protobuf.visualizer.VisualizerReplacement\x12G\n\x0ftransactionType\x18\x02 \x01(\x0e\x32..protobuf.visualizer.VisualizerTransactionType\x12\x0c\n\x04time\x18\x03 \x01(\x04\x12\x11\n\tsubsystem\x18\x04 \x01(\t\x12\x10\n\x08messages\x18\x05 \x03(\t\x12\'\n\x04head\x18\x06 \x01(\x0b\x32\x19.protobuf.visualizer.Head\x12\x31\n\tparameter\x18\x07 \x03(\x0b\x32\x1e.protobuf.visualizer.Parameter\x12*\n\x05lines\x18\x08 \x03(\x0b\x32\x1b.protobuf.visualizer.Line2D\x12\x31\n\x08\x65llipses\x18\t \x03(\x0b\x32\x1f.protobuf.visualizer.Ellipsis2D\x12\x34\n\nrectangles\x18\n \x03(\x0b\x32 .protobuf.visualizer.Rectangle2D\x12(\n\x04\x61rcs\x18\x0b \x03(\x0b\x32\x1a.protobuf.visualizer.Arc2D\x12*\n\x05texts\x18\x0c \x03(\x0b\x32\x1b.protobuf.visualizer.Text2D\x12-\n\x06raster\x18\r \x03(\x0b\x32\x1d.protobuf.visualizer.Raster2D*O\n\x19VisualizerTransactionType\x12\x0c\n\x08\x41\x42SOLUTE\x10\x00\x12\x11\n\rRELATIVE_HEAD\x10\x01\x12\x11\n\rRELATIVE_BODY\x10\x02*4\n\x15VisualizerReplacement\x12\x0e\n\nNO_REPLACE\x10\x00\x12\x0b\n\x07REPLACE\x10\x01\x42S\n?de.htwk_leipzig.naocontrol.backend.internal.protobuf.visualizerB\x10VisualizerProtosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visualizer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n?de.htwk_leipzig.naocontrol.backend.internal.protobuf.visualizerB\020VisualizerProtos'
  _PARAMETER.fields_by_name['intParams']._options = None
  _PARAMETER.fields_by_name['intParams']._serialized_options = b'\020\001'
  _PARAMETER.fields_by_name['floatParams']._options = None
  _PARAMETER.fields_by_name['floatParams']._serialized_options = b'\020\001'
  _VISUALIZERTRANSACTIONTYPE._serialized_start=2083
  _VISUALIZERTRANSACTIONTYPE._serialized_end=2162
  _VISUALIZERREPLACEMENT._serialized_start=2164
  _VISUALIZERREPLACEMENT._serialized_end=2216
  _HEAD._serialized_start=41
  _HEAD._serialized_end=75
  _PARAMETER._serialized_start=77
  _PARAMETER._serialized_end=193
  _COLOR._serialized_start=195
  _COLOR._serialized_end=246
  _LINE2D._serialized_start=249
  _LINE2D._serialized_end=455
  _LINE2D_LINETYPE._serialized_start=422
  _LINE2D_LINETYPE._serialized_end=455
  _ELLIPSIS2D._serialized_start=458
  _ELLIPSIS2D._serialized_end=666
  _RECTANGLE2D._serialized_start=669
  _RECTANGLE2D._serialized_end=869
  _ARC2D._serialized_start=872
  _ARC2D._serialized_end=1193
  _ARC2D_ARC2DTYPE._serialized_start=1152
  _ARC2D_ARC2DTYPE._serialized_end=1193
  _TEXT2D._serialized_start=1195
  _TEXT2D._serialized_end=1316
  _RASTER2D._serialized_start=1319
  _RASTER2D._serialized_end=1492
  _VISUALIZERTRANSACTION._serialized_start=1495
  _VISUALIZERTRANSACTION._serialized_end=2081
# @@protoc_insertion_point(module_scope)
