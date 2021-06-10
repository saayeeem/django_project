from django.http import HttpResponse

# Create your views here.

def myview(request):
    print(request.COOKIES)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 2 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '6349ccd8', max_age=1000)

    return resp




