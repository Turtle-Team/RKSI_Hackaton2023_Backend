import swagger.division.namespace
import flask_restplus

DIVISION_COLLEGE = swagger.division.namespace.division.model(
    "DIVISION_COLLEGE",
    {
        "name": flask_restplus.fields.String(description="Наименование подразделения", required=True),
        "hour_work": flask_restplus.fields.String(description="Часы работы и условия работы (строка)", required=True),
        "auditoria": flask_restplus.fields.String(description="Аудитория, где находится подразделение", required=True),
        "floor": flask_restplus.fields.String(description="Этаж, на котором находится", required=True),
        "description": flask_restplus.fields.String(description="Описание (чем занимается, зачем существует)", required=True)
    },
)


