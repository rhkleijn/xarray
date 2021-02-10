"""Generate stub file for arithmetic operators of various xarray classes.

FOR INTERNAL XARRAY DEVELOPMENT USE ONLY.

Usage:
    python -m xarray.util.stubgen_ops > xarray/core/_typed_ops.pyi
"""

from collections import defaultdict

unary_ops = ["__neg__", "__pos__", "__abs__", "__invert__"]

binary_ops = ["eq", "ne", "lt", "le", "gt", "ge"]
binary_ops += ["add", "sub", "mul", "pow", "truediv", "floordiv", "mod"]
binary_ops += ["radd", "rsub", "rmul", "rpow", "rtruediv", "rfloordiv", "rmod"]
binary_ops += ["and", "xor", "or"]
binary_ops += ["rand", "rxor", "ror"]
binary_ops = [f"__{op}__" for op in binary_ops]

stub_info = defaultdict(list)
METHOD_TEMPLATE_UNOPS = "    def {method}(self: T_Self) -> T_Self: ..."

method_template_binops = """\
    def {method}(self: T_Dataset, other: T_DsOther) -> T_Dataset: ...{override_misc}"""
stub_info["TypedDatasetOps"].append((METHOD_TEMPLATE_UNOPS, unary_ops))
stub_info["TypedDatasetOps"].append((method_template_binops, binary_ops))


# TypedDataArrayOps
method_template_binops = """\
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset: ...{misc}
    @overload
    def {method}(self: T_DataArray, other: T_DaOther) -> T_DataArray: ...{misc}
    @overload
    def {method}(self, other: DatasetGroupBy) -> Dataset: ...{misc}
    @overload
    def {method}(self, other: DataArrayGroupBy) -> DataArray: ...{misc}"""
stub_info["TypedDataArrayOps"].append((METHOD_TEMPLATE_UNOPS, unary_ops))
stub_info["TypedDataArrayOps"].append((method_template_binops, binary_ops))

# TypedVariableOps
method_template_binops = """\
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset: ...{misc}
    @overload
    def {method}(self, other: T_DataArray) -> T_DataArray: ...{misc}
    @overload
    def {method}(self: T_Variable, other: T_VarOther) -> T_Variable: ...{misc}"""
stub_info["TypedVariableOps"].append((METHOD_TEMPLATE_UNOPS, unary_ops))
stub_info["TypedVariableOps"].append((method_template_binops, binary_ops))


# TypedDatasetGroupByOps
method_template_binops = """\
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset: ...{misc}
    @overload
    def {method}(self, other: DataArray) -> Dataset: ...{misc}
    @overload
    def {method}(self, other: T_GroupbybIncompatible) -> NoReturn: ..."""
stub_info["TypedDatasetGroupByOps"].append((method_template_binops, binary_ops))

# TypedDataArrayGroupByOps
method_template_binops = """\
    @overload{override}
    def {method}(self, other: T_Dataset) -> T_Dataset: ...{misc}
    @overload
    def {method}(self, other: T_DataArray) -> T_DataArray: ...{misc}
    @overload
    def {method}(self, other: T_GroupbybIncompatible) -> NoReturn: ..."""
stub_info["TypedDataArrayGroupByOps"].append((method_template_binops, binary_ops))


# For some methods override return type `bool` defined by base class `object`.
def override(method):
    if method in {"__eq__", "__ne__"}:
        return "  # type: ignore[override]"
    return ""


def override_misc(method):
    if method in {"__eq__", "__ne__"}:
        return "  # type: ignore[override, misc]"
    return "  # type: ignore[misc]"


def misc():
    return "  # type: ignore[misc]"


stubfile_header = '''\
"""Stub file for arithmetic operators of various xarray classes.

This file was generated using xarray.util.stubgen_ops. Do not edit manually."""

import numbers
from typing import NoReturn, TypeVar, Union, overload

import numpy as np

from .dataarray import DataArray
from .dataset import Dataset
from .groupby import DataArrayGroupBy, DatasetGroupBy, GroupBy
from .pycompat import dask_array_type
from .variable import Variable

try:
    from dask.array import Array as DaskArray
except ImportError:
    DaskArray = np.ndarray

T_Dataset = TypeVar("T_Dataset", bound=Dataset)
T_DataArray = TypeVar("T_DataArray", bound=DataArray)
T_Variable = TypeVar("T_Variable", bound=Variable)
T_Self = TypeVar("T_Self")
T_Compatible = Union[np.ndarray, np.generic, numbers.Number, bytes, str, DaskArray]
T_DsOther = Union[Dataset, DataArray, Variable, T_Compatible, GroupBy]
T_DaOther = Union[DataArray, Variable, T_Compatible]
T_VarOther = Union[Variable, T_Compatible]
T_GroupbybIncompatible = Union[Variable, T_Compatible, GroupBy]'''


# Render stub file
if __name__ == "__main__":
    print(stubfile_header)

    for cls_name, method_blocks in stub_info.items():
        print()
        print(f"class {cls_name}:")
        for method_template, methods in method_blocks:
            for method in methods:
                print(
                    method_template.format(
                        method=method,
                        override=override(method),
                        override_misc=override_misc(method),
                        misc=misc(),
                    )
                )
