from django.http import HttpResponse
def showhomepage(request):
    message = "<html> <body bgcolour ='red'> <h1> 'Hello everyone how u doing?' </h1> </body> </html>"
    return HttpResponse(message)
