from clapper import Clapper
from xmlrpc.server import DocXMLRPCServer


def main():
    clp = Clapper()

    with DocXMLRPCServer(('', 8000)) as server:
        # server.register_introspection_functions()
        server.register_instance(clp)
        server.serve_forever()


if __name__ == '__main__':
    main()
