"""Stub file for arithmetic operators of various xarray classes.

This file was generated using xarray.util.stubgen_ops. Do not edit manually."""

import operator
from typing import TYPE_CHECKING, NoReturn, TypeVar, Union, overload

import numpy as np

from . import ops
from .nputils import array_eq, array_ne

if TYPE_CHECKING:
    from .dataarray import DataArray
    from .dataset import Dataset
    from .groupby import DataArrayGroupBy, DatasetGroupBy, GroupBy
    from .variable import Variable

    try:
        from dask.array import Array as DaskArray
    except ImportError:
        DaskArray = np.ndarray

T_Dataset = TypeVar("T_Dataset", bound="DatasetOps")
T_DataArray = TypeVar("T_DataArray", bound="DataArrayOps")
T_Variable = TypeVar("T_Variable", bound="VariableOps")

# Note: ScalarOrArray (and types involving ScalarOrArray) is to be used last in overloads,
# since nd.ndarray is typed as Any for older versions of numpy.
ScalarOrArray = Union[complex, bytes, str, np.generic, np.ndarray, "DaskArray"]
DsCompatible = Union["Dataset", "DataArray", "Variable", "GroupBy", ScalarOrArray]
DaCompatible = Union["DataArray", "Variable", "DataArrayGroupBy", ScalarOrArray]
VarCompatible = Union["Variable", ScalarOrArray]
GroupByIncompatible = Union["Variable", "GroupBy"]


class DatasetOps:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError

    def __neg__(self: T_Dataset) -> T_Dataset:
        return self._unary_op(operator.neg)

    def __pos__(self: T_Dataset) -> T_Dataset:
        return self._unary_op(operator.pos)

    def __abs__(self: T_Dataset) -> T_Dataset:
        return self._unary_op(operator.abs)

    def __invert__(self: T_Dataset) -> T_Dataset:
        return self._unary_op(operator.invert)

    def round(self: T_Dataset, *args, **kwargs) -> T_Dataset:
        return self._unary_op(ops.round_, *args, **kwargs)

    def argsort(self: T_Dataset, *args, **kwargs) -> T_Dataset:
        return self._unary_op(ops.argsort, *args, **kwargs)

    def clip(self: T_Dataset, *args, **kwargs) -> T_Dataset:
        return self._unary_op(ops.clip, *args, **kwargs)

    def conj(self: T_Dataset, *args, **kwargs) -> T_Dataset:
        return self._unary_op(ops.conj, *args, **kwargs)

    def conjugate(self: T_Dataset, *args, **kwargs) -> T_Dataset:
        return self._unary_op(ops.conjugate, *args, **kwargs)

    def __add__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.add, reflexive=False)

    def __sub__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.sub, reflexive=False)

    def __mul__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.mul, reflexive=False)

    def __pow__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.pow, reflexive=False)

    def __truediv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.truediv, reflexive=False)

    def __floordiv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.floordiv, reflexive=False)

    def __mod__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.mod, reflexive=False)

    def __and__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.and_, reflexive=False)

    def __xor__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.xor, reflexive=False)

    def __or__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.or_, reflexive=False)

    def __lt__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.lt, reflexive=False)

    def __le__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.le, reflexive=False)

    def __gt__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.gt, reflexive=False)

    def __ge__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.ge, reflexive=False)

    def __eq__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._binary_op(other, array_eq, reflexive=False)

    def __ne__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._binary_op(other, array_ne, reflexive=False)

    def __radd__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.add, reflexive=True)

    def __rsub__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.sub, reflexive=True)

    def __rmul__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.mul, reflexive=True)

    def __rpow__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.pow, reflexive=True)

    def __rtruediv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.truediv, reflexive=True)

    def __rfloordiv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.floordiv, reflexive=True)

    def __rmod__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.mod, reflexive=True)

    def __rand__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.and_, reflexive=True)

    def __rxor__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.xor, reflexive=True)

    def __ror__(self: T_Dataset, other: DsCompatible) -> T_Dataset:
        return self._binary_op(other, operator.or_, reflexive=True)

    def __iadd__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.iadd)

    def __isub__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.isub)

    def __imul__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.imul)

    def __ipow__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.ipow)

    def __itruediv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.itruediv)

    def __ifloordiv__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.ifloordiv)

    def __imod__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.imod)

    def __iand__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.iand)

    def __ixor__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.ixor)

    def __ior__(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, operator.ior)

    __neg__.__doc__ = operator.neg.__doc__
    __pos__.__doc__ = operator.pos.__doc__
    __abs__.__doc__ = operator.abs.__doc__
    __invert__.__doc__ = operator.invert.__doc__
    round.__doc__ = ops.round_.__doc__
    argsort.__doc__ = ops.argsort.__doc__
    clip.__doc__ = ops.clip.__doc__
    conj.__doc__ = ops.conj.__doc__
    conjugate.__doc__ = ops.conjugate.__doc__
    __add__.__doc__ = operator.add.__doc__
    __sub__.__doc__ = operator.sub.__doc__
    __mul__.__doc__ = operator.mul.__doc__
    __pow__.__doc__ = operator.pow.__doc__
    __truediv__.__doc__ = operator.truediv.__doc__
    __floordiv__.__doc__ = operator.floordiv.__doc__
    __mod__.__doc__ = operator.mod.__doc__
    __and__.__doc__ = operator.and_.__doc__
    __xor__.__doc__ = operator.xor.__doc__
    __or__.__doc__ = operator.or_.__doc__
    __lt__.__doc__ = operator.lt.__doc__
    __le__.__doc__ = operator.le.__doc__
    __gt__.__doc__ = operator.gt.__doc__
    __ge__.__doc__ = operator.ge.__doc__
    __eq__.__doc__ = array_eq.__doc__
    __ne__.__doc__ = array_ne.__doc__
    __radd__.__doc__ = operator.add.__doc__
    __rsub__.__doc__ = operator.sub.__doc__
    __rmul__.__doc__ = operator.mul.__doc__
    __rpow__.__doc__ = operator.pow.__doc__
    __rtruediv__.__doc__ = operator.truediv.__doc__
    __rfloordiv__.__doc__ = operator.floordiv.__doc__
    __rmod__.__doc__ = operator.mod.__doc__
    __rand__.__doc__ = operator.and_.__doc__
    __rxor__.__doc__ = operator.xor.__doc__
    __ror__.__doc__ = operator.or_.__doc__
    __iadd__.__doc__ = operator.iadd.__doc__
    __isub__.__doc__ = operator.isub.__doc__
    __imul__.__doc__ = operator.imul.__doc__
    __ipow__.__doc__ = operator.ipow.__doc__
    __itruediv__.__doc__ = operator.itruediv.__doc__
    __ifloordiv__.__doc__ = operator.ifloordiv.__doc__
    __imod__.__doc__ = operator.imod.__doc__
    __iand__.__doc__ = operator.iand.__doc__
    __ixor__.__doc__ = operator.ixor.__doc__
    __ior__.__doc__ = operator.ior.__doc__


class DataArrayOps:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError

    def __neg__(self: T_DataArray) -> T_DataArray:
        return self._unary_op(operator.neg)

    def __pos__(self: T_DataArray) -> T_DataArray:
        return self._unary_op(operator.pos)

    def __abs__(self: T_DataArray) -> T_DataArray:
        return self._unary_op(operator.abs)

    def __invert__(self: T_DataArray) -> T_DataArray:
        return self._unary_op(operator.invert)

    def round(self: T_DataArray, *args, **kwargs) -> T_DataArray:
        return self._unary_op(ops.round_, *args, **kwargs)

    def argsort(self: T_DataArray, *args, **kwargs) -> T_DataArray:
        return self._unary_op(ops.argsort, *args, **kwargs)

    def clip(self: T_DataArray, *args, **kwargs) -> T_DataArray:
        return self._unary_op(ops.clip, *args, **kwargs)

    def conj(self: T_DataArray, *args, **kwargs) -> T_DataArray:
        return self._unary_op(ops.conj, *args, **kwargs)

    def conjugate(self: T_DataArray, *args, **kwargs) -> T_DataArray:
        return self._unary_op(ops.conjugate, *args, **kwargs)

    @overload
    def __add__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __add__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __add__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __add__(self, other):
        return self._binary_op(other, operator.add, reflexive=False)

    @overload
    def __sub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __sub__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __sub__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __sub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=False)

    @overload
    def __mul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mul__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __mul__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __mul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=False)

    @overload
    def __pow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __pow__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __pow__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __pow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=False)

    @overload
    def __truediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __truediv__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __truediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=False)

    @overload
    def __floordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __floordiv__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __floordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=False)

    @overload
    def __mod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mod__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __mod__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __mod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=False)

    @overload
    def __and__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __and__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __and__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __and__(self, other):
        return self._binary_op(other, operator.and_, reflexive=False)

    @overload
    def __xor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __xor__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __xor__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __xor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=False)

    @overload
    def __or__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __or__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __or__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __or__(self, other):
        return self._binary_op(other, operator.or_, reflexive=False)

    @overload
    def __lt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __lt__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __lt__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __lt__(self, other):
        return self._binary_op(other, operator.lt, reflexive=False)

    @overload
    def __le__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __le__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __le__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __le__(self, other):
        return self._binary_op(other, operator.le, reflexive=False)

    @overload
    def __gt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __gt__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __gt__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __gt__(self, other):
        return self._binary_op(other, operator.gt, reflexive=False)

    @overload
    def __ge__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ge__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ge__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __ge__(self, other):
        return self._binary_op(other, operator.ge, reflexive=False)

    @overload  # type: ignore
    def __eq__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __eq__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __eq__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __eq__(self, other):
        return self._binary_op(other, array_eq, reflexive=False)

    @overload  # type: ignore
    def __ne__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ne__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ne__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __ne__(self, other):
        return self._binary_op(other, array_ne, reflexive=False)

    @overload
    def __radd__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __radd__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __radd__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __radd__(self, other):
        return self._binary_op(other, operator.add, reflexive=True)

    @overload
    def __rsub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rsub__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rsub__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rsub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=True)

    @overload
    def __rmul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmul__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rmul__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rmul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=True)

    @overload
    def __rpow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rpow__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rpow__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rpow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=True)

    @overload
    def __rtruediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rtruediv__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rtruediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=True)

    @overload
    def __rfloordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rfloordiv__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rfloordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=True)

    @overload
    def __rmod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmod__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rmod__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rmod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=True)

    @overload
    def __rand__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rand__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rand__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rand__(self, other):
        return self._binary_op(other, operator.and_, reflexive=True)

    @overload
    def __rxor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rxor__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rxor__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __rxor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=True)

    @overload
    def __ror__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ror__(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ror__(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...

    def __ror__(self, other):
        return self._binary_op(other, operator.or_, reflexive=True)

    def __iadd__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.iadd)

    def __isub__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.isub)

    def __imul__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.imul)

    def __ipow__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ipow)

    def __itruediv__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.itruediv)

    def __ifloordiv__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ifloordiv)

    def __imod__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.imod)

    def __iand__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.iand)

    def __ixor__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ixor)

    def __ior__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ior)

    __neg__.__doc__ = operator.neg.__doc__
    __pos__.__doc__ = operator.pos.__doc__
    __abs__.__doc__ = operator.abs.__doc__
    __invert__.__doc__ = operator.invert.__doc__
    round.__doc__ = ops.round_.__doc__
    argsort.__doc__ = ops.argsort.__doc__
    clip.__doc__ = ops.clip.__doc__
    conj.__doc__ = ops.conj.__doc__
    conjugate.__doc__ = ops.conjugate.__doc__
    __add__.__doc__ = operator.add.__doc__
    __sub__.__doc__ = operator.sub.__doc__
    __mul__.__doc__ = operator.mul.__doc__
    __pow__.__doc__ = operator.pow.__doc__
    __truediv__.__doc__ = operator.truediv.__doc__
    __floordiv__.__doc__ = operator.floordiv.__doc__
    __mod__.__doc__ = operator.mod.__doc__
    __and__.__doc__ = operator.and_.__doc__
    __xor__.__doc__ = operator.xor.__doc__
    __or__.__doc__ = operator.or_.__doc__
    __lt__.__doc__ = operator.lt.__doc__
    __le__.__doc__ = operator.le.__doc__
    __gt__.__doc__ = operator.gt.__doc__
    __ge__.__doc__ = operator.ge.__doc__
    __eq__.__doc__ = array_eq.__doc__
    __ne__.__doc__ = array_ne.__doc__
    __radd__.__doc__ = operator.add.__doc__
    __rsub__.__doc__ = operator.sub.__doc__
    __rmul__.__doc__ = operator.mul.__doc__
    __rpow__.__doc__ = operator.pow.__doc__
    __rtruediv__.__doc__ = operator.truediv.__doc__
    __rfloordiv__.__doc__ = operator.floordiv.__doc__
    __rmod__.__doc__ = operator.mod.__doc__
    __rand__.__doc__ = operator.and_.__doc__
    __rxor__.__doc__ = operator.xor.__doc__
    __ror__.__doc__ = operator.or_.__doc__
    __iadd__.__doc__ = operator.iadd.__doc__
    __isub__.__doc__ = operator.isub.__doc__
    __imul__.__doc__ = operator.imul.__doc__
    __ipow__.__doc__ = operator.ipow.__doc__
    __itruediv__.__doc__ = operator.itruediv.__doc__
    __ifloordiv__.__doc__ = operator.ifloordiv.__doc__
    __imod__.__doc__ = operator.imod.__doc__
    __iand__.__doc__ = operator.iand.__doc__
    __ixor__.__doc__ = operator.ixor.__doc__
    __ior__.__doc__ = operator.ior.__doc__


class VariableOps:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError

    def __neg__(self: T_Variable) -> T_Variable:
        return self._unary_op(operator.neg)

    def __pos__(self: T_Variable) -> T_Variable:
        return self._unary_op(operator.pos)

    def __abs__(self: T_Variable) -> T_Variable:
        return self._unary_op(operator.abs)

    def __invert__(self: T_Variable) -> T_Variable:
        return self._unary_op(operator.invert)

    def round(self: T_Variable, *args, **kwargs) -> T_Variable:
        return self._unary_op(ops.round_, *args, **kwargs)

    def argsort(self: T_Variable, *args, **kwargs) -> T_Variable:
        return self._unary_op(ops.argsort, *args, **kwargs)

    def clip(self: T_Variable, *args, **kwargs) -> T_Variable:
        return self._unary_op(ops.clip, *args, **kwargs)

    def conj(self: T_Variable, *args, **kwargs) -> T_Variable:
        return self._unary_op(ops.conj, *args, **kwargs)

    def conjugate(self: T_Variable, *args, **kwargs) -> T_Variable:
        return self._unary_op(ops.conjugate, *args, **kwargs)

    @overload
    def __add__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __add__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __add__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __add__(self, other):
        return self._binary_op(other, operator.add, reflexive=False)

    @overload
    def __sub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __sub__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __sub__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __sub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=False)

    @overload
    def __mul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mul__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __mul__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __mul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=False)

    @overload
    def __pow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __pow__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __pow__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __pow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=False)

    @overload
    def __truediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __truediv__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __truediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=False)

    @overload
    def __floordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __floordiv__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __floordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=False)

    @overload
    def __mod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mod__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __mod__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __mod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=False)

    @overload
    def __and__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __and__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __and__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __and__(self, other):
        return self._binary_op(other, operator.and_, reflexive=False)

    @overload
    def __xor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __xor__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __xor__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __xor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=False)

    @overload
    def __or__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __or__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __or__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __or__(self, other):
        return self._binary_op(other, operator.or_, reflexive=False)

    @overload
    def __lt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __lt__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __lt__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __lt__(self, other):
        return self._binary_op(other, operator.lt, reflexive=False)

    @overload
    def __le__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __le__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __le__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __le__(self, other):
        return self._binary_op(other, operator.le, reflexive=False)

    @overload
    def __gt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __gt__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __gt__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __gt__(self, other):
        return self._binary_op(other, operator.gt, reflexive=False)

    @overload
    def __ge__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ge__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ge__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __ge__(self, other):
        return self._binary_op(other, operator.ge, reflexive=False)

    @overload  # type: ignore
    def __eq__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __eq__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __eq__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __eq__(self, other):
        return self._binary_op(other, array_eq, reflexive=False)

    @overload  # type: ignore
    def __ne__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ne__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ne__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __ne__(self, other):
        return self._binary_op(other, array_ne, reflexive=False)

    @overload
    def __radd__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __radd__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __radd__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __radd__(self, other):
        return self._binary_op(other, operator.add, reflexive=True)

    @overload
    def __rsub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rsub__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rsub__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rsub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=True)

    @overload
    def __rmul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmul__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rmul__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rmul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=True)

    @overload
    def __rpow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rpow__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rpow__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rpow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=True)

    @overload
    def __rtruediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rtruediv__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rtruediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=True)

    @overload
    def __rfloordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rfloordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=True)

    @overload
    def __rmod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmod__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rmod__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rmod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=True)

    @overload
    def __rand__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rand__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rand__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rand__(self, other):
        return self._binary_op(other, operator.and_, reflexive=True)

    @overload
    def __rxor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rxor__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rxor__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __rxor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=True)

    @overload
    def __ror__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ror__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ror__(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...

    def __ror__(self, other):
        return self._binary_op(other, operator.or_, reflexive=True)

    def __iadd__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.iadd)

    def __isub__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.isub)

    def __imul__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.imul)

    def __ipow__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ipow)

    def __itruediv__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.itruediv)

    def __ifloordiv__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ifloordiv)

    def __imod__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.imod)

    def __iand__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.iand)

    def __ixor__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ixor)

    def __ior__(self, other):  # type: ignore
        return self._inplace_binary_op(other, operator.ior)

    __neg__.__doc__ = operator.neg.__doc__
    __pos__.__doc__ = operator.pos.__doc__
    __abs__.__doc__ = operator.abs.__doc__
    __invert__.__doc__ = operator.invert.__doc__
    round.__doc__ = ops.round_.__doc__
    argsort.__doc__ = ops.argsort.__doc__
    clip.__doc__ = ops.clip.__doc__
    conj.__doc__ = ops.conj.__doc__
    conjugate.__doc__ = ops.conjugate.__doc__
    __add__.__doc__ = operator.add.__doc__
    __sub__.__doc__ = operator.sub.__doc__
    __mul__.__doc__ = operator.mul.__doc__
    __pow__.__doc__ = operator.pow.__doc__
    __truediv__.__doc__ = operator.truediv.__doc__
    __floordiv__.__doc__ = operator.floordiv.__doc__
    __mod__.__doc__ = operator.mod.__doc__
    __and__.__doc__ = operator.and_.__doc__
    __xor__.__doc__ = operator.xor.__doc__
    __or__.__doc__ = operator.or_.__doc__
    __lt__.__doc__ = operator.lt.__doc__
    __le__.__doc__ = operator.le.__doc__
    __gt__.__doc__ = operator.gt.__doc__
    __ge__.__doc__ = operator.ge.__doc__
    __eq__.__doc__ = array_eq.__doc__
    __ne__.__doc__ = array_ne.__doc__
    __radd__.__doc__ = operator.add.__doc__
    __rsub__.__doc__ = operator.sub.__doc__
    __rmul__.__doc__ = operator.mul.__doc__
    __rpow__.__doc__ = operator.pow.__doc__
    __rtruediv__.__doc__ = operator.truediv.__doc__
    __rfloordiv__.__doc__ = operator.floordiv.__doc__
    __rmod__.__doc__ = operator.mod.__doc__
    __rand__.__doc__ = operator.and_.__doc__
    __rxor__.__doc__ = operator.xor.__doc__
    __ror__.__doc__ = operator.or_.__doc__
    __iadd__.__doc__ = operator.iadd.__doc__
    __isub__.__doc__ = operator.isub.__doc__
    __imul__.__doc__ = operator.imul.__doc__
    __ipow__.__doc__ = operator.ipow.__doc__
    __itruediv__.__doc__ = operator.itruediv.__doc__
    __ifloordiv__.__doc__ = operator.ifloordiv.__doc__
    __imod__.__doc__ = operator.imod.__doc__
    __iand__.__doc__ = operator.iand.__doc__
    __ixor__.__doc__ = operator.ixor.__doc__
    __ior__.__doc__ = operator.ior.__doc__


class DatasetGroupByOps:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError

    @overload
    def __add__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __add__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __add__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __add__(self, other):
        return self._binary_op(other, operator.add, reflexive=False)

    @overload
    def __sub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __sub__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __sub__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __sub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=False)

    @overload
    def __mul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mul__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __mul__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __mul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=False)

    @overload
    def __pow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __pow__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __pow__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __pow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=False)

    @overload
    def __truediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __truediv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __truediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=False)

    @overload
    def __floordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __floordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=False)

    @overload
    def __mod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mod__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __mod__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __mod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=False)

    @overload
    def __and__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __and__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __and__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __and__(self, other):
        return self._binary_op(other, operator.and_, reflexive=False)

    @overload
    def __xor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __xor__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __xor__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __xor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=False)

    @overload
    def __or__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __or__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __or__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __or__(self, other):
        return self._binary_op(other, operator.or_, reflexive=False)

    @overload
    def __lt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __lt__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __lt__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __lt__(self, other):
        return self._binary_op(other, operator.lt, reflexive=False)

    @overload
    def __le__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __le__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __le__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __le__(self, other):
        return self._binary_op(other, operator.le, reflexive=False)

    @overload
    def __gt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __gt__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __gt__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __gt__(self, other):
        return self._binary_op(other, operator.gt, reflexive=False)

    @overload
    def __ge__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ge__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ge__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ge__(self, other):
        return self._binary_op(other, operator.ge, reflexive=False)

    @overload  # type: ignore
    def __eq__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __eq__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __eq__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __eq__(self, other):
        return self._binary_op(other, array_eq, reflexive=False)

    @overload  # type: ignore
    def __ne__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ne__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ne__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ne__(self, other):
        return self._binary_op(other, array_ne, reflexive=False)

    @overload
    def __radd__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __radd__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __radd__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __radd__(self, other):
        return self._binary_op(other, operator.add, reflexive=True)

    @overload
    def __rsub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rsub__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rsub__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rsub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=True)

    @overload
    def __rmul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmul__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rmul__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rmul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=True)

    @overload
    def __rpow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rpow__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rpow__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rpow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=True)

    @overload
    def __rtruediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rtruediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=True)

    @overload
    def __rfloordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rfloordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=True)

    @overload
    def __rmod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmod__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rmod__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rmod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=True)

    @overload
    def __rand__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rand__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rand__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rand__(self, other):
        return self._binary_op(other, operator.and_, reflexive=True)

    @overload
    def __rxor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rxor__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __rxor__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rxor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=True)

    @overload
    def __ror__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ror__(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def __ror__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ror__(self, other):
        return self._binary_op(other, operator.or_, reflexive=True)

    __add__.__doc__ = operator.add.__doc__
    __sub__.__doc__ = operator.sub.__doc__
    __mul__.__doc__ = operator.mul.__doc__
    __pow__.__doc__ = operator.pow.__doc__
    __truediv__.__doc__ = operator.truediv.__doc__
    __floordiv__.__doc__ = operator.floordiv.__doc__
    __mod__.__doc__ = operator.mod.__doc__
    __and__.__doc__ = operator.and_.__doc__
    __xor__.__doc__ = operator.xor.__doc__
    __or__.__doc__ = operator.or_.__doc__
    __lt__.__doc__ = operator.lt.__doc__
    __le__.__doc__ = operator.le.__doc__
    __gt__.__doc__ = operator.gt.__doc__
    __ge__.__doc__ = operator.ge.__doc__
    __eq__.__doc__ = array_eq.__doc__
    __ne__.__doc__ = array_ne.__doc__
    __radd__.__doc__ = operator.add.__doc__
    __rsub__.__doc__ = operator.sub.__doc__
    __rmul__.__doc__ = operator.mul.__doc__
    __rpow__.__doc__ = operator.pow.__doc__
    __rtruediv__.__doc__ = operator.truediv.__doc__
    __rfloordiv__.__doc__ = operator.floordiv.__doc__
    __rmod__.__doc__ = operator.mod.__doc__
    __rand__.__doc__ = operator.and_.__doc__
    __rxor__.__doc__ = operator.xor.__doc__
    __ror__.__doc__ = operator.or_.__doc__


class DataArrayGroupByOps:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError

    @overload
    def __add__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __add__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __add__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __add__(self, other):
        return self._binary_op(other, operator.add, reflexive=False)

    @overload
    def __sub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __sub__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __sub__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __sub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=False)

    @overload
    def __mul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mul__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __mul__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __mul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=False)

    @overload
    def __pow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __pow__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __pow__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __pow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=False)

    @overload
    def __truediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __truediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=False)

    @overload
    def __floordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __floordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=False)

    @overload
    def __mod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __mod__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __mod__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __mod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=False)

    @overload
    def __and__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __and__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __and__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __and__(self, other):
        return self._binary_op(other, operator.and_, reflexive=False)

    @overload
    def __xor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __xor__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __xor__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __xor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=False)

    @overload
    def __or__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __or__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __or__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __or__(self, other):
        return self._binary_op(other, operator.or_, reflexive=False)

    @overload
    def __lt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __lt__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __lt__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __lt__(self, other):
        return self._binary_op(other, operator.lt, reflexive=False)

    @overload
    def __le__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __le__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __le__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __le__(self, other):
        return self._binary_op(other, operator.le, reflexive=False)

    @overload
    def __gt__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __gt__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __gt__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __gt__(self, other):
        return self._binary_op(other, operator.gt, reflexive=False)

    @overload
    def __ge__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ge__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ge__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ge__(self, other):
        return self._binary_op(other, operator.ge, reflexive=False)

    @overload  # type: ignore
    def __eq__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __eq__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __eq__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __eq__(self, other):
        return self._binary_op(other, array_eq, reflexive=False)

    @overload  # type: ignore
    def __ne__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ne__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ne__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ne__(self, other):
        return self._binary_op(other, array_ne, reflexive=False)

    @overload
    def __radd__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __radd__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __radd__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __radd__(self, other):
        return self._binary_op(other, operator.add, reflexive=True)

    @overload
    def __rsub__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rsub__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rsub__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rsub__(self, other):
        return self._binary_op(other, operator.sub, reflexive=True)

    @overload
    def __rmul__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmul__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rmul__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rmul__(self, other):
        return self._binary_op(other, operator.mul, reflexive=True)

    @overload
    def __rpow__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rpow__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rpow__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rpow__(self, other):
        return self._binary_op(other, operator.pow, reflexive=True)

    @overload
    def __rtruediv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rtruediv__(self, other):
        return self._binary_op(other, operator.truediv, reflexive=True)

    @overload
    def __rfloordiv__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rfloordiv__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rfloordiv__(self, other):
        return self._binary_op(other, operator.floordiv, reflexive=True)

    @overload
    def __rmod__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rmod__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rmod__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rmod__(self, other):
        return self._binary_op(other, operator.mod, reflexive=True)

    @overload
    def __rand__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rand__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rand__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rand__(self, other):
        return self._binary_op(other, operator.and_, reflexive=True)

    @overload
    def __rxor__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __rxor__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __rxor__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __rxor__(self, other):
        return self._binary_op(other, operator.xor, reflexive=True)

    @overload
    def __ror__(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def __ror__(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def __ror__(self, other: GroupByIncompatible) -> NoReturn:
        ...

    def __ror__(self, other):
        return self._binary_op(other, operator.or_, reflexive=True)

    __add__.__doc__ = operator.add.__doc__
    __sub__.__doc__ = operator.sub.__doc__
    __mul__.__doc__ = operator.mul.__doc__
    __pow__.__doc__ = operator.pow.__doc__
    __truediv__.__doc__ = operator.truediv.__doc__
    __floordiv__.__doc__ = operator.floordiv.__doc__
    __mod__.__doc__ = operator.mod.__doc__
    __and__.__doc__ = operator.and_.__doc__
    __xor__.__doc__ = operator.xor.__doc__
    __or__.__doc__ = operator.or_.__doc__
    __lt__.__doc__ = operator.lt.__doc__
    __le__.__doc__ = operator.le.__doc__
    __gt__.__doc__ = operator.gt.__doc__
    __ge__.__doc__ = operator.ge.__doc__
    __eq__.__doc__ = array_eq.__doc__
    __ne__.__doc__ = array_ne.__doc__
    __radd__.__doc__ = operator.add.__doc__
    __rsub__.__doc__ = operator.sub.__doc__
    __rmul__.__doc__ = operator.mul.__doc__
    __rpow__.__doc__ = operator.pow.__doc__
    __rtruediv__.__doc__ = operator.truediv.__doc__
    __rfloordiv__.__doc__ = operator.floordiv.__doc__
    __rmod__.__doc__ = operator.mod.__doc__
    __rand__.__doc__ = operator.and_.__doc__
    __rxor__.__doc__ = operator.xor.__doc__
    __ror__.__doc__ = operator.or_.__doc__
