from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse


from .models import StaticHtml, Subscribe

def content(request, id):

    page = get_object_or_404(StaticHtml, pk=id)
    context = {
            'page': page,
            }

    return render(request, 'static_html.html', context)

def subscribe(request):

	if request.method == "POST":
		email = request.POST.get('email', False)
		subscribe = Subscribe(email=email)
		subscribe.save()
	else:
		return redirect('/')


	return render(request, 'subscribe.html')
