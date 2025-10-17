from django.http import HttpResponse

#def index(response):
    #return HttpResponse("<h1>Web Development with Ike!<!h1>")

#def v1(response):
    #return HttpResponse("<h1>View 1!<!h1>")

def index(response, id):
    return HttpResponse("<h1>%s</h1>" %id)