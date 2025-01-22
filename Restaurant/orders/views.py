from django.shortcuts import render, redirect
from orders.models import TableDetails, Order
from accounts.models import Foods
from django.http import JsonResponse
import json
from django.utils import timezone



import qrcode
from io import BytesIO
from django.http import HttpResponse

def generate_qr_code(request):
    # URL for the table_entry API
    table_entry_url = request.build_absolute_uri('/orders/table-entry/')

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(table_entry_url)
    qr.make(fit=True)

    # Create an image of the QR code
    qr_image = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)

    # Return the QR code as an HTTP response
    return HttpResponse(buffer, content_type="image/png")


# Table Entry View
def table_entry(request):

# Prepare range for dropdown (accessible for both GET and POST requests)
    table_numbers = range(1, 11)
    
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
    return render(request, 'tableEntry.html', {'table_numbers': table_numbers})


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
            customer_note = data.get('customer_note', None)  # Retrieve the optional note


            # Retrieve table details from the session
            table_num = request.session.get('table_number')
            cust_name = request.session.get('customer_name')

            # Save the order to the database
            order = Order.objects.create(
                items=items,
                total_price=total_price,
                table_number=table_num,
                customer_name=cust_name,
                created_at=timezone.now(),
                customer_note=customer_note,  # Save the note

            )

            # Return success response
            return JsonResponse({
                'message': 'Order placed successfully!',
                'order_id': order.id,
                'table_number': table_num,
                'customer_name': cust_name,
                'customer_note': customer_note,  # Include the note in the response

                # 'created_at': order.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format the timestamp

            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
