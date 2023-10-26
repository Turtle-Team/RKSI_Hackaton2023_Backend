import swagger.user.namespace
import flask_restplus

AUTH_USER = swagger.user.namespace.user.model(
    "DOC_IS_TEACHING",
    {
        "uid": flask_restplus.fields.String(description="уникальый айди в соц. платформе", required=True),
        "platform": flask_restplus.fields.String(description="платформа откуда пришел запрос", required=True),
        "from_name": flask_restplus.fields.String(description="Для кого (ФИО) выдан документ", required=True),
        "group_name": flask_restplus.fields.String(description="Группа, в которой учится студент", required=True),
    },
)


