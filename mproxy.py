# Lucas Lopilato 2/28/2017
# Man in the middle Proxy Server
# CS176B HW3
from getopt import getopt, GetoptError
import sys


# Print Help Message
def help():
    print("Usage: python mproxy.py [options] [port]")
    print()
    print("Timeout option assumes seconds.")
    print(" -h, --help                        Prints this message.")
    print(" -v, --version                     Prints version information.")
    print(" -p, --port port                   Specify port to listen on.")
    print("                                     If specified port is")
    print("                                     occupied, will try another port.")
    print(" -n, --numworker num_of_worker     Number of workers in thread")
    print("                                     pool handling concurrent")
    print("                                     requests. Defaults to 10.")
    print(" -t, --timeout <time>              Time(sec) to wait before giving")
    print("                                     up waiting for server")
    print("                                     response. Defaults to infinity.")
    print(" -l, --log directory               Log HTTP requests and responses")
    print("                                     under specified directory.")
    exit(0)


def version():
    print("Version Message")
    exit(0)


# TODO figure out desired behavior for both short and long provided
def main(argv):
    try:
        # Scan for Help Version Port Workers Time and Log
        opt, after = getopt(argv,
                            "hvp:ntl:",
                            ["help", "version",
                             "port=", "numworker",
                             "timeout", "log="])
    except:
        help()

    # Initialize Options
    options = {
        "numworker": 10,
        "timeout": -1,
    }
    try:
        # Parse Each Argument
        for o, a in opt:
            if o in ("-h", "--help"):
                help()
            elif o in ("-v", "--version"):
                version()
            elif o in ("-p", "--port"):
                options["port"] = int(a)
            elif o in ("-n", "--numworker"):
                options["numworker"] = int(a)
            elif o in ("-t", "--timeout"):
                options["timeout"] = int(a)
            elif o in ("-l", "--log"):
                options["log"] = a  # TODO Check for validity
            else:
                help()
    except:
        help()

    # Assert Port Number Supplied
    if "port" not in options:
        help()


if __name__ == '__main__':
    # Call Main truncating method name
    main(sys.argv[1:])
