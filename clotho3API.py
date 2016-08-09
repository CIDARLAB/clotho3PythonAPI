import CidarAPI

# self.clothoClient implementation is in CidarAPI class.
# Protocol implementation is in this class.

class Clotho:
    def __init__(self):
        self.clothoClient = CidarAPI.ClientWebSocket("wss://localhost:8443/websocket")

    def _parse_query_args(self, schema, name, options):
        if type(schema) is str:
            return { "obj":{ schema:name }, "options":options }
        else:
            return { "obj":schema, "options":name }

    def create(self, object, options=None):
        if len(object) is None:
            return self.clothoClient.emit("create", object, options)
        elif len(object) is 1:
            return self.clothoClient.emit("create", object[0], options)
        else:
            return self.clothoClient.emit("createAll", object, options)

    def destroy(self, name, options=None):
        if type(name) is str:
            return self.clothoClient.emit("destroy", name, options)
        else:
            return self.clothoClient.emit("destroyAll", name, options)

    def set(self, object, options=None):
        if len(object) is None:
            return self.clothoClient.emit("set", object, options)
        else:
            return self.clothoClient.emit("setAll", object, options)

    def get(self, name, options=None):
        if type(name) is str:
            return self.clothoClient.emit("get", name, options)
        else:
            return self.clothoClient.emit("getAll", name, options)

    def query(self, schema, name, options=None):
        args = self._parse_query_args(schema,name,options)
        return self.clothoClient.emit("query", args["obj"], args["options"])

    def queryOne(self, schema, name, options):
        args = self._parse_query_args(schema,name,options)
        return self.clothoClient.emit("queryOne", args["obj"], args["options"])

    def run(self, object, options=None):
        if object.get("args") is None:
            object["args"] = []

        if object["module"] is None:
            return self.clothoClient.emit("run",{"id":object["function"], "args":object["args"]}, options)
        else:
            return self.clothoClient.emit("run",{"id":object["module"], "function":object["function"], "args":object["args"]}, options)
        
    def submit(self, script, options=None):
        return self.clothoClient.emit("submit", script, options)

    def validate(self, object, options=None):
        return self.clothoClient.emit("validate", object, options)

    def createUser(self, userEmail, password):
        return self.clothoClient.emit("createUser",{"username":userEmail, "password":password})

    def login(self, userEmail, password):
        return self.clothoClient.emit("login",{"username":userEmail, "credentials":password})

    def logout(self):
        return self.clothoClient.emit("logout", "")

    def grant(self, user, id, add, remove):
        if len(id) is None or type(id) is str:
            return self.clothoClient.emit("grant",{"user":user, "id":id, "add":add, "remove":remove})
        else:
            return self.clothoClient.emit("grantAll",{"user":user, "id":id, "add":add, "remove":remove})

    def autocomplete(self, substring, options=None):
        if substring is not "" and substring is not None:
            return self.clothoClient.emit("autocomplete",{"query":substring},options)
        