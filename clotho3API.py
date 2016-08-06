import CidarAPI

# Socket implementation is in CidarAPI class.
# Protocol implementation is in this class.

class Clotho:
    def __init__(self):
        self.clothoClient = CidarAPI.ClientWebSocket("wss://localhost:8443/websocket")

    def _format_data(self, userEmail, password, objectId=None, status=None):
        data = {
            "username": userEmail,
            "password": password
        }
        if objectId is not None:
            data["id"] = objectId
        if status is not None:
            data["status"] = status
        return data

    def create_status(self, userEmail, password, status):
        return self.clothoClient.emit("CREATE_STATUS", self._format_data(userEmail, password,  status=status))

    def get_projects(self, userEmail, password):
        return self.clothoClient.emit("GET_PROJECTS", self._format_data(userEmail, password))

    def get_project(self, userEmail, password, projectID):
        return self.clothoClient.emit("GET_PROJECT", self._format_data(userEmail, password, projectID))

    def create_project_status(self, userEmail, password, projectID, projectStatus):
        return self.clothoClient.emit("CREATE_PROJECT_STATUS", self._format_data(userEmail, password, projectID, projectStatus))

    def get_orders(self, userEmail, password):
        return self.clothoClient.emit("GET_ORDERS", self._format_data(userEmail, password))

    def get_order(self, userEmail, password, orderID):
        return self.clothoClient.emit("GET_ORDER", self._format_data(userEmail, password, orderID))

    def change_ordering_status(self, userEmail, password, orderID, orderStatus):
        return self.clothoClient.emit("CHANGE_ORDERING_STATUS", self._format_data(userEmail, password, orderID, orderStatus))