# Author:  Lisandro Dalcin
# Contact: dalcinl@gmail.com
"""Typing support."""
# pylint: disable=ungrouped-imports
# pylint: disable=no-name-in-module

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

__all__ = [
    'SupportsPyBuffer',
    'SupportsDLPack',
    'SupportsCAI',
    'Buffer',
    'Bottom',
    'InPlace',
    'Aint',
    'Count',
    'Displ',
    'Offset',
    'TypeSpec',
    'BufSpec',
    'BufSpecB',
    'BufSpecV',
    'BufSpecW',
    'TargetSpec',
]


SupportsPyBuffer = _PyBuffer
"""
`Python buffer <pybuf_>`_ protocol.

.. _pybuf: https://docs.python.org/3/c-api/buffer.html
"""


class SupportsDLPack(Protocol):
    """
    `DLPack`_ data interchange protocol.

    .. _DLPack: https://data-apis.org/array-api/latest/
                design_topics/data_interchange.html
    """
    # pylint: disable=too-few-public-methods

    _Stream: TypeAlias = Union[int, Any]
    _PyCapsule: TypeAlias = object
    _DeviceType: TypeAlias = int
    _DeviceID: TypeAlias = int

    def __dlpack__(self, *, stream: Optional[_Stream] = None) -> _PyCapsule: ...
    def __dlpack_device__(self) -> Tuple[_DeviceType, _DeviceID]: ...


class SupportsCAI(Protocol):
    """
    `CUDA Array Interface <CAI_>`_ protocol.

    .. _CAI: https://numba.readthedocs.io/en/stable/
             cuda/cuda_array_interface.html
    """
    # pylint: disable=too-few-public-methods

    @property
    def __cuda_array_interface__(self) -> Dict[str, Any]: ...


Buffer = Union[
    SupportsPyBuffer,
    SupportsDLPack,
    SupportsCAI,
]
"""
Buffer-like object.
"""


Bottom = Union[BottomType, None]
"""
Start of the address range.
"""


InPlace = Union[InPlaceType, None]
"""
In-place buffer argument.
"""


Aint = Integral
"""
Address-sized integral type.
"""


Count = Integral
"""
Integral type for counts.
"""


Displ = Integral
"""
Integral type for displacements.
"""


Offset = Integral
"""
Integral type for offsets.
"""


TypeSpec = Union[Datatype, str]
"""
Datatype specification.
"""


BufSpec = Union[
    Buffer,
    Tuple[Buffer, Count],
    Tuple[Buffer, TypeSpec],
    Tuple[Buffer, Count, TypeSpec],
    Tuple[Bottom, Count, Datatype],
    List,
]
"""
Buffer specification.

* `Buffer`
* Tuple[`Buffer`, `Count`]
* Tuple[`Buffer`, `TypeSpec`]
* Tuple[`Buffer`, `Count`, `TypeSpec`]
* Tuple[`Bottom`, `Count`, `Datatype`]
"""


BufSpecB = Union[
    Buffer,
    Tuple[Buffer, Count],
    Tuple[Buffer, TypeSpec],
    Tuple[Buffer, Count, TypeSpec],
    List,
]
"""
Buffer specification (block).

* `Buffer`
* Tuple[`Buffer`, `Count`]
* Tuple[`Buffer`, `TypeSpec`]
* Tuple[`Buffer`, `Count`, `TypeSpec`]
"""


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
"""
Buffer specification (vector).

* `Buffer`
* Tuple[`Buffer`, Sequence[`Count`]]
* Tuple[`Buffer`, Tuple[Sequence[`Count`], Sequence[`Displ`]]]
* Tuple[`Buffer`, `TypeSpec`]
* Tuple[`Buffer`, Sequence[`Count`], `TypeSpec`]
* Tuple[`Buffer`, Tuple[Sequence[`Count`], Sequence[`Displ`]], `TypeSpec`]
* Tuple[`Buffer`, Sequence[`Count`], Sequence[`Displ`], `TypeSpec`]
* Tuple[`Bottom`, Tuple[Sequence[`Count`], Sequence[`Displ`]], `Datatype`]
* Tuple[`Bottom`, Sequence[`Count`], Sequence[`Displ`], `Datatype`]
"""


BufSpecW = Union[
    Tuple[Buffer, Sequence[Datatype]],
    Tuple[Buffer, Tuple[Sequence[Count], Sequence[Displ]], Sequence[Datatype]],
    Tuple[Buffer, Sequence[Count], Sequence[Displ], Sequence[Datatype]],
    Tuple[Bottom, Tuple[Sequence[Count], Sequence[Displ]], Sequence[Datatype]],
    Tuple[Bottom, Sequence[Count], Sequence[Displ], Sequence[Datatype]],
    List,
]
"""
Buffer specification (generalized).

* Tuple[`Buffer`, Sequence[`Datatype`]]
* Tuple[`Buffer`, \
        Tuple[Sequence[`Count`], Sequence[`Displ`]], Sequence[`Datatype`]]
* Tuple[`Buffer`, Sequence[`Count`], Sequence[`Displ`], Sequence[`Datatype`]]
* Tuple[`Bottom`, \
        Tuple[Sequence[`Count`], Sequence[`Displ`]], Sequence[`Datatype`]]
* Tuple[`Bottom`, Sequence[`Count`], Sequence[`Displ`], Sequence[`Datatype`]]
"""


TargetSpec = Union[
    Displ,
    Tuple[()],
    Tuple[Displ],
    Tuple[Displ, Count],
    Tuple[Displ, Count, TypeSpec],
    List,
]
"""
Target specification.

* `Displ`
* Tuple[()]
* Tuple[`Displ`]
* Tuple[`Displ`, `Count`]
* Tuple[`Displ`, `Count`, `Datatype`]
"""
