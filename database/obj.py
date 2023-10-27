import dataclasses
import json
import  datetime

@dataclasses.dataclass
class Division:
    div_id: int
    name: str
    hour_work: str
    auditoria: str
    floor: str
    description: str

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def to_dict(self):
        return self.__dict__


@dataclasses.dataclass
class Homework:
    hw_id: int
    date_homework: datetime
    group: str
    item: str
    homework: str

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def to_dict(self):
        return self.__dict__