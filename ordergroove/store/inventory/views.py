from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from inventory.models import Category, Store, Product
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from django.contrib import messages
from django.contrib.auth.models import User
import pdb

def database_selector(store_subdomain):
	store_dict = {} 
	#creates dictionary of store names paired with their joined lower-case strings
	for store in Store.objects.all():
		store_dict[store.name.replace(' ','').lower()] = store.name
	if store_subdomain in store_dict:
		store_db = Store.objects.get(name=store_dict[store_subdomain]) 
		store_products = Product.objects.filter(store_name = store_db.id) 
		#gets products associated with chosen store
		return store_db, store_products
	else:
		raise Http404

def homepage(request, store_subdomain):
	store_db, store_products = database_selector(store_subdomain)
	return render_to_response('base.html', 
			{'store_name': store_db.name, 'store_subdomain':store_subdomain})
		
def products(request, store_subdomain):
	store_db, store_products = database_selector(store_subdomain)
	context = RequestContext(request)
	if request.method == 'POST': #load catalog page with "item added"
		product = store_products.get(pk=request.POST['product_id'])
		try:
			cart
		except:
			cart = request.session
		if cart.get(product):
			cart[product] += 1
		else:
			cart[product] = 1
		request.session.modified = True
		return render_to_response('catalog.html', 
				{'store_name': store_db.name, 
				'store_products': store_products, 
				'store_subdomain': store_subdomain,
				'message':'%s Added'%product.name}, context_instance=context)
	return render_to_response('catalog.html', 
				{'store_name': store_db.name, 
				'store_products': store_products,
				'store_subdomain': store_subdomain}, 
				context_instance=RequestContext(request))

def shoppingcart(request, store_subdomain):
	#load page of all shopping cart items
	store_db, store_products = database_selector(store_subdomain)
	cart = request.session
	return render_to_response('shoppingcart.html', 
			{'store_name': store_db.name, 
			'store_products': store_products,
			'store_subdomain': store_subdomain, 
			'cart' : cart}, context_instance=RequestContext(request))
	

def checkout(request, store_subdomain):
	store_db, store_products = database_selector(store_subdomain)
	request.session.clear()
	return render_to_response('checkout.html', 
			{'store_name': store_db.name,
			'store_subdomain': store_subdomain})



# Create your views here.
