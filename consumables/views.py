from django.shortcuts import render, get_object_or_404
from .models import Consumables, Cart2
from items.models import Category, Item, Borrow
def consumables(request):
	all_consumables = Category.objects.all()
	context = {'all_consumables': all_consumables}
	return render(request, 'consumables/index2.html', context)

def item(request, Category_id, Item_id):
	consumables = get_object_or_404(Item, pk=Item_id)
	if request.method == 'POST':
		if request.POST.get('user_c') and request.POST.get('name_of_consum'):
			cart2 = Cart2()
			cart2.user_c = request.user
			cart2.name_of_consum = request.POST.get('name_of_consum')
			cart2.save()
	return render(request, 'consumables/item.html', {'consumables': consumables})

def cart2(request):
	user_c = request.user
	return render(request, 'consumables/cart2.html', {'user_c':user_c})

