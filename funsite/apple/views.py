from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as HR
from django.http import Http404 
from django.http import HttpResponseRedirect as HRR
from .models import ToDo, Item
from .form import create_list

def index(response, id):
	lt= ToDo.objects.get(id = id)

	if lt in response.user.ToDo.all():

		if response.method == "POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in lt.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else :
						item.complete = False

					item.save()

			elif response.POST.get("newThing"):
				xt = response.POST.get("make")

				if len(xt) > 2:
					lt.item_set.create(text = xt, complete = False)

				else:
					print("rejected")

		return render(response, "apple/list.html", {'lt':lt})
	else:
		return render(response, "apple/home.html", {})

def Home(response):
	return render(response, "apple/home.html", {})

def create(response):
	response.user
	if response.method == "POST":
		form = create_list(response.POST)

		if form.is_valid():
			l = form.cleaned_data["name"]
			s = ToDo(name = l)
			s.save()
			response.user.ToDo.add(s)
		return HRR("/%i" %s.id)
	else:
		form = create_list()
	return render(response, "apple/create.html", {"form": form})


def view(response):
	return render(response, "apple/view.html", {})

# Create your views here.

