import swagger.user.namespace
import flask_restplus

AUTH_USER = swagger.user.namespace.user.model(
    "USER_AUTH",
    {
        "login": flask_restplus.fields.String(description="login", required=True),
        "password": flask_restplus.fields.String(description="password", required=True),
    },
)


