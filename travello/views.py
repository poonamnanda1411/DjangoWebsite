from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

	dest1 = Destination()
	dest1.name='Mumbai'
	dest1.desc='The city that never sleeps'
	dest1.img='destination_1.jpg'
	dest1.price=750
	dest1.offer=False

	dest2 = Destination()
	dest2.name='New Delhi'
	dest2.desc='The city of hearts'
	dest2.img='destination_2.jpg'
	dest2.price=650
	dest2.offer=True

	dest3 = Destination()
	dest3.name='Chennai'
	dest3.desc='The city of joy'
	dest3.img='destination_3.jpg'
	dest3.price=550
	dest3.offer=False
    
	dests = [dest1, dest2, dest3]

	return render(request,'index.html',{'dests':dests})

