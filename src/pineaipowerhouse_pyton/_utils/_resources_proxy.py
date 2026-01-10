from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `pineaipowerhouse_pyton.resources` module.

    This is used so that we can lazily import `pineaipowerhouse_pyton.resources` only when
    needed *and* so that users can just import `pineaipowerhouse_pyton` and reference `pineaipowerhouse_pyton.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("pineaipowerhouse_pyton.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
