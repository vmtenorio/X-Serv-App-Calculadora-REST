import webapp

class calc(webapp.webApp):

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""

        return request.split()

    def getOperands(parsedRequest):
        op1 = None
        op2 = None
        for i in parsedRequest:
            if i.startswith('op1'):
                op1 = i.split('=')[1]
            if i.startswith('op2'):
                op2 = i.split('=')[1]
        return op1, op2

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        if (parsedRequest[0] == "PUT" and parsedRequest[1].startswith('/conf')):
            self.op1, self.op2 = getOperands(parsedRequest)
            if self.op1 == None or self.op2 == None:
                return ("400 Bad Request", "<html><body><h1>We need op1 and op2 params</h1></body></html>")
            return ("200 OK", "<html><body><h1>We received your params</h1></body></html>")
        if (parsedRequest[0] == "GET"):
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
                return ("400 Bad Request", "<html><body><h1>Operations are suma resta mult and div</h1></body></html>")

        return ("400 Bad Request", "<html><body><h1>Bad Request</h1></body></html>")


if __name__ == '__main__':
    testCalc = calc('localhost', 1234)
