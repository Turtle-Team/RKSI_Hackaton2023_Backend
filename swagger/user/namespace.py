import swagger

user = swagger.api.namespace(name='user', path="/api/user")
user.default = ""
user.description = ""