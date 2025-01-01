from django.shortcuts import render
from django.http import JsonResponse
from orders.models import Order

# Create your views here.
def kitchen(request):
    return render(request, 'kitchen.html')

  

def kitchen_orders(request):
    if request.method == 'GET':
        try:
            # Fetch all orders
            orders = Order.objects.all().values()
            
            # Return the data as a JSON response
            return JsonResponse({'orders': list(orders)}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
from orders.models import Order

def kitchen_view(request):
    # Fetch all orders from the database
    orders = Order.objects.all().values()
    print("=========================================================")
    print(list(orders)[-1])
    print("=========================================================")
    return render(request, "kitchen.html", {"orders": list(orders)})

