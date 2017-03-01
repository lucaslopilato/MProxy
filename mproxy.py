# Lucas Lopilato 2/28/2017
# Man in the middle Proxy Server
# CS176B HW3
from getopt import getopt, GetoptError
import sys


# Print Help Message
def help():
    print("Help Message")
    exit(0)


def version():
    print("Version Message")
    exit(0)


def main(argv):
    try:
        # Scan for Help Version Port Workers Time and Log
        opt, after = getopt(argv,
                            "hvp:ntl:",
                            ["help", "version",
                             "port=", "numworker",
                             "timeout", "log="])
    except GetoptError as e:
        print(e)
        exit(2)

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
