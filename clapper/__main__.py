from clapper import Clapper
from xmlrpc.server import DocXMLRPCServer


def get_my_ip(talking_to="8.8.8.8"):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((talking_to, 80))
    ret = s.getsockname()[0]
    s.close()
    return ret

def main():
    from disco import DiscoClient

    clp = Clapper()
    dc = DiscoClient('http://44.0.0.181:8888')

    with DocXMLRPCServer(('', 8000)) as server:
        # server.register_introspection_functions()
        dc.announce('clapper','http://{}:8000'.format(get_my_ip()))
        server.register_instance(clp)
        server.serve_forever()


if __name__ == '__main__':
    main()
