from datetime import datetime
from json import dumps
from typing import Any, Dict
from uuid import UUID


def serializer(value: Dict[str, Any]) -> bytes:
    """Convert a Dictionary to JSON Bytes String."""
    value = value.copy()

    for k, v in value.items():
        if isinstance(v, UUID):
            value[k] = str(v)

        if isinstance(v, datetime):
            value[k] = v.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(v, bool):
            value[k] = int(v)

    return dumps(value).encode()
