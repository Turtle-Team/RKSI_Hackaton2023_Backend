import swagger.homework.namespace
import flask_restplus

HOMEWORK_TABLE = swagger.homework.namespace.homework.model(
    "HOMEWORK_TABLE",
    {
        "data": flask_restplus.fields.String(description="Дата когда было загружено", required=True),
        "group": flask_restplus.fields.String(description="Группа", required=True),
        "item": flask_restplus.fields.String(description="Предмет", required=True),
        "homework": flask_restplus.fields.String(description="Сама домашка", required=True),
    },
)


