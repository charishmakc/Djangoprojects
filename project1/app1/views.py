from django.http import HttpResponse
def display(req):
    message = "Hello world"
    return HttpResponse(message)

