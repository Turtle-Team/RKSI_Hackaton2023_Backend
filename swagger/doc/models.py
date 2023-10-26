import swagger.doc.namespace
import flask_restplus

DOC_CREATE = swagger.doc.namespace.doc.model(
    "DOC_CREATE",
    {
        "type": flask_restplus.fields.Integer(description="Тип документа из запроса doc/type", required=True),
        "fio": flask_restplus.fields.String(description="ФИО студента", required=True),
        "from_id": flask_restplus.fields.String(description="Айди в соц сети откуда пришел запрос", required=True),
        "platform": flask_restplus.fields.String(description="Платформа соцсети", required=True),
        "description": flask_restplus.fields.String(description="Описание самого запроса (что хочет студент)", required=True)
    },
)



