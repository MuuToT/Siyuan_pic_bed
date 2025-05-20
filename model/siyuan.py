import typing
from typing import NotRequired

from define.base import ResourceType


class ResourceCache(typing.TypedDict):
    filename: str
    image_path: str
    ori_image_path: str
    type: typing.Optional[ResourceType]


class DataBaseResourceInfo(typing.TypedDict):
    filename: str
    path: str
    type: typing.Optional[ResourceType]
    file: NotRequired[bytes]
    md5: NotRequired[str]
    file_size: NotRequired[int]
