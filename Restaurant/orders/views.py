from django.shortcuts import render, redirect
from orders.models import TableDetails, Order
from accounts.models import Foods
from django.http import JsonResponse
import json

# Table Entry View
def table_entry(request):
    if request.method == 'POST':
        # Get data from the form
        table_number = request.POST.get('table_number')
        customer_name = request.POST.get('customer_name')

        # Save table details to the database
        TableDetails.objects.create(table_number=table_number, customer_name=customer_name)

        # Store table details in session
        request.session['table_number'] = table_number
        request.session['customer_name'] = customer_name

        # Redirect to the menu page
        return redirect('/orders/menu/')

    # Render the form page
    return render(request, 'tableEntry.html')


# Menu View
def menu(request):
    # Retrieve table details from the session
    table_number = request.session.get('table_number')
    customer_name = request.session.get('customer_name')

    # Fetch food items
    foods = Foods.objects.all()

    # Pass table details and foods to the template
    return render(request, 'menu.html', {
        'foods': foods,
        'table_number': table_number,
        'customer_name': customer_name
    })


# Place Order View
def place_order(request):
    if request.method == 'POST':
        try:
            # Parse the request body
            data = json.loads(request.body)
            items = data.get('items', {})
            total_price = data.get('total_price', 0)

            # Retrieve table details from the session
            table_num = request.session.get('table_number')
            cust_name = request.session.get('customer_name')

            # Save the order to the database
            order = Order.objects.create(
                items=items,
                total_price=total_price,
                table_number=table_num,
                customer_name=cust_name
            )

            # Return success response
            return JsonResponse({
                'message': 'Order placed successfully!',
                'order_id': order.id,
                'table_number': table_num,
                'customer_name': cust_name
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
