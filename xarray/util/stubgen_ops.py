"""Generate stub file for arithmetic operators of various xarray classes.

For internal xarray development use only.

Usage:
    python xarray/util/stubgen_ops.py > xarray/core/_typed_ops.py
"""

from typing import Dict

UNARY_OPS = (
    ("__neg__", "operator.neg"),
    ("__pos__", "operator.pos"),
    ("__abs__", "operator.abs"),
    ("__invert__", "operator.invert"),
)
BINOPS_EQNE = (("__eq__", "array_eq"), ("__ne__", "array_ne"))
BINOPS_CMP = (
    ("__lt__", "operator.lt"),
    ("__le__", "operator.le"),
    ("__gt__", "operator.gt"),
    ("__ge__", "operator.ge"),
)
BINOPS_NUM = (
    ("__add__", "operator.add"),
    ("__sub__", "operator.sub"),
    ("__mul__", "operator.mul"),
    ("__pow__", "operator.pow"),
    ("__truediv__", "operator.truediv"),
    ("__floordiv__", "operator.floordiv"),
    ("__mod__", "operator.mod"),
    ("__and__", "operator.and_"),
    ("__xor__", "operator.xor"),
    ("__or__", "operator.or_"),
)
BINOPS_REFLEXIVE = (
    ("__radd__", "operator.add"),
    ("__rsub__", "operator.sub"),
    ("__rmul__", "operator.mul"),
    ("__rpow__", "operator.pow"),
    ("__rtruediv__", "operator.truediv"),
    ("__rfloordiv__", "operator.floordiv"),
    ("__rmod__", "operator.mod"),
    ("__rand__", "operator.and_"),
    ("__rxor__", "operator.xor"),
    ("__ror__", "operator.or_"),
)
BINOPS_INPLACE = (
    ("__iadd__", "operator.iadd"),
    ("__isub__", "operator.isub"),
    ("__imul__", "operator.imul"),
    ("__ipow__", "operator.ipow"),
    ("__itruediv__", "operator.itruediv"),
    ("__ifloordiv__", "operator.ifloordiv"),
    ("__imod__", "operator.imod"),
    ("__iand__", "operator.iand"),
    ("__ixor__", "operator.ixor"),
    ("__ior__", "operator.ior"),
)
# round method and numpy/pandas unary methods which don't modify the data shape,
# so the result should still be wrapped in an Variable/DataArray/Dataset
OTHER_UNARY_METHODS = (
    ("round", "ops.round_"),
    ("argsort", "ops.argsort"),
    ("clip", "ops.clip"),
    ("conj", "ops.conj"),
    ("conjugate", "ops.conjugate"),
)

template_unaryop = """
    def {method}(self: {self_type}) -> {self_type}:
        return self._unary_op({func})"""
template_binop = """
    def {method}(self, other):
        return self._binary_op(other, {func}, reflexive={reflexive})"""
# silence mypy error that signatures of inplace and regular binops are incompatible
template_inplace = """
    def {method}(self, other):  # type: ignore
        return self._inplace_binary_op(other, {func})"""
template_unaryop_other = """
    def {method}(self: {self_type}, *args, **kwargs) -> {self_type}:
        return self._unary_op({func}, *args, **kwargs)"""

# DatasetOps (has no overloads, type hints directly included in function definition)
# For some methods override return type `bool` defined by base class `object`.
template_binop_ds = """
    def {method}(self: T_Dataset, other: DsCompatible) -> T_Dataset:{override}
        return self._binary_op(other, {func}, reflexive={reflexive})"""

template_inplace_ds = """
    def {method}(self: T_Dataset, other: DsCompatible) -> T_Dataset:  # type: ignore
        return self._inplace_binary_op(other, {func})"""

# Note: in some of the overloads below the return value in reality is
# NotImplemented, which cannot accurately be expressed with type hints,
# e.g. Literal[NotImplemented] or type(NotImplemented) are not allowed and
# NoReturn has a different meaning.
# In such cases we are lending the type checkers a hand by specifying the
# return type of the corresponding reflexive method on the other argument
# which will be called in such instances.
#
# nd.ndarray is typed as Any for older versions of numpy.
# PyCharm has issue with overloads, see https://youtrack.jetbrains.com/issue/PY-38075

# DataArrayOps
overloads_da = """
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def {method}(self, other: "DatasetGroupBy") -> "Dataset":  # type: ignore
        ...

    @overload
    def {method}(self: T_DataArray, other: DaCompatible) -> T_DataArray:  # type: ignore
        ...
"""
# VariableOps
overloads_var = """
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def {method}(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def {method}(self: T_Variable, other: VarCompatible) -> T_Variable:  # type: ignore
        ...
"""
# DatasetGroupByOps
overloads_ds_gb = """
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def {method}(self, other: "DataArray") -> "Dataset":  # type: ignore
        ...

    @overload
    def {method}(self, other: GroupByIncompatible) -> NoReturn:
        ...
"""
# DataArrayGroupByOps
overloads_da_gb = """
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset:  # type: ignore
        ...

    @overload
    def {method}(self, other: T_DataArray) -> T_DataArray:  # type: ignore
        ...

    @overload
    def {method}(self, other: GroupByIncompatible) -> NoReturn:
        ...
"""


def binops(overloads="", template=template_binop):
    TYPE_OVERRIDE = ("override", "  # type: ignore")
    REFLEXIVE = ("reflexive", "True")

    return [
        (BINOPS_NUM + BINOPS_CMP, overloads + template),
        (BINOPS_EQNE, overloads + template, TYPE_OVERRIDE),
        (BINOPS_REFLEXIVE, overloads + template, REFLEXIVE),
    ]


def inplace(overloads="", template=template_inplace):
    return [(BINOPS_INPLACE, overloads + template)]


def unops(self_type):
    return [
        (UNARY_OPS, template_unaryop, ("self_type", self_type)),
        (OTHER_UNARY_METHODS, template_unaryop_other, ("self_type", self_type)),
    ]


ops_info: Dict[str, list] = {}
ops_info["DatasetOps"] = (
    unops("T_Dataset")
    + binops(template=template_binop_ds)
    + inplace(template=template_inplace_ds)
)
ops_info["DataArrayOps"] = unops("T_DataArray") + binops(overloads_da) + inplace()
ops_info["VariableOps"] = unops("T_Variable") + binops(overloads_var) + inplace()
ops_info["DatasetGroupByOps"] = binops(overloads_ds_gb)
ops_info["DataArrayGroupByOps"] = binops(overloads_da_gb)

stubfile_preamble = '''\
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
GroupByIncompatible = Union["Variable", "GroupBy"]'''

class_preamble = """

class {cls_name}:
    __slots__ = ()

    def _unary_op(self, f, *args, **kwargs):
        raise NotImplementedError

    def _binary_op(self, other, f, reflexive=False):
        raise NotImplementedError

    def _inplace_binary_op(self, other, f):
        raise NotImplementedError"""

copy_doc_template = "    {method}.__doc__ = {func}.__doc__"

# Render stub file
if __name__ == "__main__":
    print(stubfile_preamble)
    for cls_name, method_blocks in ops_info.items():
        print(class_preamble.format(cls_name=cls_name))

        for method_func_pairs, method_template, *context_pair_args in method_blocks:
            context = {"reflexive": "False", "override": ""}  # defaults
            context.update(context_pair_args)
            for method, func in method_func_pairs:
                print(method_template.format(method=method, func=func, **context))
        print()
        for method_func_pairs, *_ in method_blocks:
            for method, func in method_func_pairs:
                print(copy_doc_template.format(method=method, func=func))
