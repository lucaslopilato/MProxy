# Class Implementing a basic HTTP Server
import socket
import _thread
import logging
import select


class HttpProxy(object):

    """docstring for HttpServer"""

    def __init__(self, options):
        super(HttpProxy, self).__init__()

        # Setup Logger
        logging.getLogger().setLevel(options['logger'])

        # Initialize Incoming Port Info
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = options['bufferSize']  # Size of the buffer
        self.port = options['port']  # Set Port Number

        # Initialize Threads and FD Lists
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.timeout = options['timeout']

        # Initialize Workers
        logging.info('Creating %d worker threads', options['numworker'])
        for i in range(0, options['numworker']):
            _thread.start_new_thread(self.handleRequests, ())
            print("new thread")

        # Listen & Accept on the specified port
        self.listen()
        logging.info('Listening for connections')
        while True:
            self.rlist.append(self.listener.accept())
            logging.info('New connection added to read FDs')

    # Close All Connections
    def __del__(self):
        self.listener.close()
        logging.info('Listener connection closed')

    # Listen for connections on a specified socket & port
    def listen(self):

        # Bind the port
        try:
            self.listener.bind(('localhost', self.port))
            logging.info("Listener on localhost at port %d" % self.port)
        except:
            logging.info("Listener failed to bind port %d" % self.port)
            try:
                badPort = self.port

                # If the port is taken, assign one by OS
                self.listener.bind(('localhost', 0))

                # Update the Object's Port Reference
                self.port = self.listener.getsockname()[1]

                # Notify User the Port has been changed
                print("Port %d unavailable, server now listening on port %d" %
                      (badPort, self.port))
            except:
                print("Error: Failed to bind a port, exiting.")

        # Listen on the port for connections
        self.listener.listen(0)  # Backlog == 0

    # Handle all read, write, and error FDs
    def handleRequests(self):
        logging.info('Worker %d created', _thread.get_ident())

        rlist, wlist, xlist = select.select(self.rlist,
                                            self.wlist,
                                            self.xlist,
                                            self.timeout)
        # If there is a request to read, read it
        if len(rlist) > 0:
            addr, msg = logging.log(rlist[0].recv(self.buffer))
            logging.info('Message %s received from %s', msg, addr)

        logging.info('Worker %d exiting', _thread.get_ident())
