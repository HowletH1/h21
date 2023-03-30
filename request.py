from typing import Dict
from abstract_storage import AbstractStorage
from exceptions import InvalidRequest, InvalidStorage


class Request:
    def __init__(self, request: str, sources: Dict[str, AbstractStorage]):
        req = request.lower().split(' ')
        if len(req) != 7:
            raise InvalidRequest

        self.count = int(req[1])
        self.product = req[2]
        self.departure = req[4]
        self.destination = req[6]

        if self.departure not in sources or self.destination not in sources:
            raise InvalidStorage
