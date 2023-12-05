from waitress import serve
import loadbalancer as lb


print('LB main started')
port = 8080
host_ip = 'localhost'
serve(lb.app, host=host_ip, port=port)
print('Stopped LB server')
