from random import random
import clotho3API
import time

clotho = clotho3API.Clotho()
username = "1234@qwer.com"
password = 1234

def projects_callback(data):
    global username
    global password
    print("Received Projects: " + str(data))
    clotho.get_project(username,password,data[0]["projectId"]).then(print)
    clotho.create_project_status(username,password,data[0]["projectId"],"Project status # %f" % random()).then(print)

def orders_callback(data):
    global username
    global password
    print("Received Orders: " + str(data))
    clotho.get_order(username,password,data[0]["orderId"]).then(print)
    clotho.change_ordering_status(username, password, data[0]["orderId"], clotho.APPROVED).then(print)

print("!!!!!!!! Start protocol !!!!!!!!!\n")
start = time.time()

clotho.create_status(username,password,"Weehee PB API Works! ID: %f" % random()).then(print)
clotho.get_projects(username,password).then(projects_callback)
clotho.get_orders(username,password).then(orders_callback)

while clotho.clothoClient.socket.pendingRequests:
    pass

print('took %.2f seconds' % (time.time() - start))