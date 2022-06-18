import sys
from typing import (
    Any,
    Union,
    Optional,
    Sequence,
    List,
    Dict,
    Tuple,
)
from numbers import (
    Integral,
)
from .MPI import (
    Datatype,
    BottomType,
    InPlaceType,
)
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
if sys.version_info >= (3, 12):
    from types import Buffer as _PyBuffer
else:
    _PyBuffer = Any
del sys

__all__: List[str] = ...

SupportsPyBuffer = _PyBuffer

_Stream: TypeAlias = Union[int, Any]
_PyCapsule: TypeAlias = object
_DeviceType: TypeAlias = int
_DeviceID: TypeAlias = int

class SupportsDLPack(Protocol):
    def __dlpack__(self, *, stream: Optional[_Stream] = None) -> _PyCapsule: ...
    def __dlpack_device__(self) -> Tuple[_DeviceType, _DeviceID]: ...

class SupportsCAI(Protocol):
    @property
    def __cuda_array_interface__(self) -> Dict[str, Any]: ...

Buffer = Union[
    SupportsPyBuffer,
    SupportsDLPack,
    SupportsCAI,
]

Bottom = Union[BottomType, None]

InPlace = Union[InPlaceType, None]

Aint = Integral

Count = Integral

Displ = Integral

Offset = Integral

TypeSpec = Union[Datatype, str]

BufSpec = Union[
    Buffer,
    Tuple[Buffer, Count],
    Tuple[Buffer, TypeSpec],
    Tuple[Buffer, Count, TypeSpec],
    Tuple[Bottom, Count, Datatype],
    List,
]

BufSpecB = Union[
    Buffer,
    Tuple[Buffer, Count],
    Tuple[Buffer, TypeSpec],
    Tuple[Buffer, Count, TypeSpec],
    List,
]

BufSpecV = Union[
    Buffer,
    Tuple[Buffer, Sequence[Count]],
    Tuple[Buffer, Tuple[Sequence[Count], Sequence[Displ]]],
    Tuple[Buffer, TypeSpec],
    Tuple[Buffer, Sequence[Count], TypeSpec],
    Tuple[Buffer, Tuple[Sequence[Count], Sequence[Displ]], TypeSpec],
    Tuple[Buffer, Sequence[Count], Sequence[Displ], TypeSpec],
    Tuple[Bottom, Tuple[Sequence[Count], Sequence[Displ]], Datatype],
    Tuple[Bottom, Sequence[Count], Sequence[Displ], Datatype],
    List,
]

BufSpecW = Union[
    Tuple[Buffer, Sequence[Datatype]],
    Tuple[Buffer, Tuple[Sequence[Count], Sequence[Displ]], Sequence[Datatype]],
    Tuple[Buffer, Sequence[Count], Sequence[Displ], Sequence[Datatype]],
    Tuple[Bottom, Tuple[Sequence[Count], Sequence[Displ]], Sequence[Datatype]],
    Tuple[Bottom, Sequence[Count], Sequence[Displ], Sequence[Datatype]],
    List,
]

TargetSpec = Union[
    Displ,
    Tuple[()],
    Tuple[Displ],
    Tuple[Displ, Count],
    Tuple[Displ, Count, TypeSpec],
    List,
]
