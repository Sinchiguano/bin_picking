# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autolab_core/RigidTransformListenerRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RigidTransformListenerRequest(genpy.Message):
  _md5sum = "926bcdc77e020fe1b0dab9093941bca3"
  _type = "autolab_core/RigidTransformListenerRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string from_frame
string to_frame
"""
  __slots__ = ['from_frame','to_frame']
  _slot_types = ['string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       from_frame,to_frame

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RigidTransformListenerRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.from_frame is None:
        self.from_frame = ''
      if self.to_frame is None:
        self.to_frame = ''
    else:
      self.from_frame = ''
      self.to_frame = ''

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
      _x = self.from_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.to_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.from_frame = str[start:end].decode('utf-8')
      else:
        self.from_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.to_frame = str[start:end].decode('utf-8')
      else:
        self.to_frame = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.from_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.to_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.from_frame = str[start:end].decode('utf-8')
      else:
        self.from_frame = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.to_frame = str[start:end].decode('utf-8')
      else:
        self.to_frame = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autolab_core/RigidTransformListenerResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RigidTransformListenerResponse(genpy.Message):
  _md5sum = "7ec2b9c75e6b2bdb02f5e916c9af6eaf"
  _type = "autolab_core/RigidTransformListenerResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 x_trans
float64 y_trans
float64 z_trans
float64 w_rot
float64 x_rot
float64 y_rot
float64 z_rot
"""
  __slots__ = ['x_trans','y_trans','z_trans','w_rot','x_rot','y_rot','z_rot']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_trans,y_trans,z_trans,w_rot,x_rot,y_rot,z_rot

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RigidTransformListenerResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x_trans is None:
        self.x_trans = 0.
      if self.y_trans is None:
        self.y_trans = 0.
      if self.z_trans is None:
        self.z_trans = 0.
      if self.w_rot is None:
        self.w_rot = 0.
      if self.x_rot is None:
        self.x_rot = 0.
      if self.y_rot is None:
        self.y_rot = 0.
      if self.z_rot is None:
        self.z_rot = 0.
    else:
      self.x_trans = 0.
      self.y_trans = 0.
      self.z_trans = 0.
      self.w_rot = 0.
      self.x_rot = 0.
      self.y_rot = 0.
      self.z_rot = 0.

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
      buff.write(_get_struct_7d().pack(_x.x_trans, _x.y_trans, _x.z_trans, _x.w_rot, _x.x_rot, _x.y_rot, _x.z_rot))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 56
      (_x.x_trans, _x.y_trans, _x.z_trans, _x.w_rot, _x.x_rot, _x.y_rot, _x.z_rot,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7d().pack(_x.x_trans, _x.y_trans, _x.z_trans, _x.w_rot, _x.x_rot, _x.y_rot, _x.z_rot))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 56
      (_x.x_trans, _x.y_trans, _x.z_trans, _x.w_rot, _x.x_rot, _x.y_rot, _x.z_rot,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
class RigidTransformListener(object):
  _type          = 'autolab_core/RigidTransformListener'
  _md5sum = '1b358ad3ddaa046f03b607401db493d6'
  _request_class  = RigidTransformListenerRequest
  _response_class = RigidTransformListenerResponse
