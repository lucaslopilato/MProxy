# Lucas Lopilato 2/28/2017
# Man in the middle Proxy Server
# CS176B HW3
from getopt import getopt, GetoptError


def main(argv):
    try:
        opt, after = getopt(argv,
                            "hvp:ntl:",
                            ["help", "version",
                             "port=", "numworker",
                             "timeout", "log"])
    except GetoptError as e:
        print(e)

if __name__ == '__main__':
    # Call Main truncating method name
    main(sys.argv[1:])
