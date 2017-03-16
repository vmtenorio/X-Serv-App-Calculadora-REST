import webapp

class calc(webapp.webApp):

    def __init__(self, hostname, port):
        self.op1 = None
        self.op2 = None
        webapp.webApp.__init__(self, hostname, port)

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        return request.split()

    def getOperands(self, petBody):
        try:
            op1, op2 = petBody.split(',')
            op1 = int(op1)
            op2 = int(op2)
        except ValueError:
            op1 = None
            op2 = None
        return op1, op2

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        if (parsedRequest[0] == "PUT" and parsedRequest[1] == '/conf'):
            self.op1, self.op2 = self.getOperands(parsedRequest[-1])
            if self.op1 == None or self.op2 == None:
                return ("400 Bad Request", "<html><body><h1>We need op1 and op2 params in the body separated by commas</h1></body></html>")
            return ("200 OK", "<html><body><h1>We received your params</h1></body></html>")
        elif (parsedRequest[0] == "GET"):
            if self.op1 == None or self.op2 == None:
                return ("400 Bad Request", "<html><body><p>Operations are suma resta mult and div, " +
                                            "and you can set the operands by sending a PUT request " +
                                            "to resource /conf with the operands in its body separated by commas.</p></body></html>")
            if parsedRequest[1] == "/suma":
                return ("200 OK", "<html><body><h1>Suma!</h1><p>" + str(self.op1) + " + " + str(self.op2) +
                                    " = " + str(self.op1 + self.op2) + "</p></body></html>")
            elif parsedRequest[1] == "/resta":
                return ("200 OK", "<html><body><h1>Resta!</h1><p>" + str(self.op1) + " - " + str(self.op2) +
                                    " = " + str(self.op1 - self.op2) + "</p></body></html>")
            elif parsedRequest[1] == "/mult":
                return ("200 OK", "<html><body><h1>Multiplicacion!</h1><p>" + str(self.op1) + " * " + str(self.op2) +
                                    " = " + str(self.op1 * self.op2) + "</p></body></html>")
            elif parsedRequest[1] == "/div":
                return ("200 OK", "<html><body><h1>Division!</h1><p>" + str(self.op1) + " / " + str(self.op2) +
                                    " = " + str(self.op1 / self.op2) + "</p></body></html>")
            else:
                return ("400 Bad Request", "<html><body><p>Operations are suma resta mult and div, " +
                                            "and you can set the operands by sending a PUT request " +
                                            "to resource /conf with the operands in its body separated by commas.</p></body></html>")
        else:
            return ("405 Method Not Allowed", "<html><body><h1>We support GET and PUT to /conf methods</h1></body></html>")


if __name__ == '__main__':
    testCalc = calc('localhost', 1234)
