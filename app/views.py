# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .models import UserInfo
# from django.utils import timezone
# # Create your views here.
# def home(request):
#     return render(request, "app/index.html")

# from django.contrib import messages

# # Define your admin credentials
# ADMIN_USERNAME = 'projectadmin@'
# ADMIN_PASSWORD = '1234!$'



# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Check username and password
#         if username == 'projectadmin@' and password == '1234!$':
#             return redirect('admin_dashboard')
#         else:
#             # Check if the user is a registered regular user
#             try:
#                 user = UserInfo.objects.get(username=username, password=password)
#                 request.session['username'] = username  # Store in session
                
#                 # Redirect to user dashboard (you can define this view)
#                 return render(request, 'app/index.html', {'username': username}) # Replace with your user dashboard view
#             except UserInfo.DoesNotExist:
#                 # Handle invalid login for both admin and users
#                 return render(request, 'app/loginform.html', {'error': 'Invalid username or password'})
    
    
#     return render(request, 'app/loginform.html')

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')

#         # Check if the username is unique
#         if UserInfo.objects.filter(username=username).exists():
#             return render(request, 'app/loginform.html', {'signup_error': 'Username already exists.'})
        
#         # Create a new user
#         user = UserInfo(username=username, password=password, phone=phone, address=address)
#         user.save()  # Save the new user to the database
#         messages.success(request, "Sign up successful! You can now log in.")
#         return redirect('admin_login')  # Redirect to login after sign-up
#     return render(request, 'app/loginform.html')
# def admin_dashboard(request):
#     orders = Order.objects.all()  # Fetch all orders
#     return render(request, 'app/admin.html', {'orders': orders})
# def user_dashboard(request):
#     return render(request, 'app/user.html', {'user': request.user})

# def cupcake_view(request):
#     return render(request, 'app/cupcake.html') 
# def brownie_view(request):
#     return render(request, 'app/brownie.html')
# def donut_view(request):
#     return render(request, 'app/donut.html')
# def cart_view(request):
#     return render(request, 'app/cart.html')
# def view_ourcake(request):
#     return render(request,'app/ourcake.html')

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils import timezone
# import json
# from .models import Order, OrderDetail, UserInfo  # Using Order instead of Orders

# @csrf_exempt  # If you're handling CSRF with JavaScript tokens
# def place_order(request):
#     if request.method == 'POST':
#         try:
#             print("POST data received:", request.body)  # Debugging incoming POST request
#             data = json.loads(request.body)

#             # Fetch username and cart data from the request body
#             username = data.get('username')
#             cart = data.get('cart')
#             total_price = data.get('total_price')

#             # Retrieve user instance from UserInfo
#             user = UserInfo.objects.get(username=username)
            
#             # Debugging information to verify received data
#             print("Username:", username, "Cart Items:", cart, "Total Price:", total_price)

#             # Create an order record in the Order table
#             order = Order.objects.create(
#                 username=user,
#                 total_price=total_price,
#                 order_date=timezone.now()
#             )

#             # Loop through the cart items and create order details for each
#             for item in cart:
#                 OrderDetail.objects.create(
#                     order=order,
#                     product_name=item['name'],
#                     quantity=item['quantity']
#                 )

#             return JsonResponse({'success': True})

#         except UserInfo.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'User not found'})
#         except Exception as e:
#             print("Error:", str(e))  # Log error details
#             return JsonResponse({'success': False, 'error': str(e)})
    
#     return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

# def view_orders(request):
#     orders = Order.objects.all().prefetch_related('orderdetail_set')  # Get all orders with their details
#     return render(request, 'app/admin.html', {'orders': orders})



from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UserInfo
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, "app/index.html")
def shop(request):
    return render(request, 'app/shop.html')
def about(request):
    return render(request, 'app/about.html')
def contact(request):
    return render(request, 'app/contact.html')

from django.contrib import messages

# Define your admin credentials
ADMIN_USERNAME = 'projectadmin@'
ADMIN_PASSWORD = '1234!$'



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check username and password
        if username == 'projectadmin@' and password == '1234!$':
            return redirect('admin_dashboard')
        else:
            # Check if the user is a registered regular user
            try:
                user = UserInfo.objects.get(username=username, password=password)
                request.session['username'] = username  # Store in session
                
                # Redirect to user dashboard (you can define this view)
                return render(request, 'app/index.html', {'username': username}) # Replace with your user dashboard view
            except UserInfo.DoesNotExist:
                # Handle invalid login for both admin and users
                return render(request, 'app/loginform.html', {'error': 'Invalid username or password'})
    
    
    return render(request, 'app/loginform.html')

from django.shortcuts import render, redirect
from .models import UserInfo

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Check if the username is unique
        if UserInfo.objects.filter(username=username).exists():
            return render(request, 'app/loginform.html', {'signup_error': 'Username already exists.'})
        if not phone.isdigit() or len(phone) != 11:
            return render(request, 'app/loginform.html', {
        'signup_error': 'Phone number must be 11 digits and contain only numbers.'
    })
        # Create a new user
        user = UserInfo(username=username, password=password, phone=phone, address=address)
        user.save()  # Save the new user to the database
        messages.success(request, "Sign up successful! You can now log in.")
        return redirect('admin_login')  # Redirect to login after sign-up
    return render(request, 'app/loginform.html')
   
def admin_dashboard(request):
    orders = Order.objects.all()  # Fetch all orders
    return render(request, 'app/admin.html', {'orders': orders})
def user_dashboard(request):
    # Fetch all orders, regardless of the user
    orders = Order.objects.select_related('username').prefetch_related('orderdetail_set').all()
    # Pass all orders to 'user.html'
    return render(request, 'app/user.html', {'orders': orders})

# def cupcake_view(request):
#     return render(request, 'app/cupcake.html') 
# def brownie_view(request):
#     return render(request, 'app/brownie.html')
# def donut_view(request):
#     return render(request, 'app/donut.html')
# def cart_view(request):
#     return render(request, 'app/cart.html')
# def view_ourcake(request):
#     return render(request,'app/ourcake.html')

from .models import Products 

def cupcake_view(request):
    products = Products.objects.filter(category="Cupcakes")  # Fetch only cupcakes
    return render(request, 'app/cupcake.html', {'products': products})

def brownie_view(request):
    products = Products.objects.filter(category="Brownies")  # Fetch only brownies
    return render(request, 'app/brownie.html', {'products': products})

def donut_view(request):
    products = Products.objects.filter(category="Donuts")  # Fetch only donuts
    return render(request, 'app/donut.html', {'products': products})

def view_ourcake(request):
    products = Products.objects.filter(category="Cakes")  # Fetch only cakes
    return render(request, 'app/ourcake.html', {'products': products})



def product_view(request):
    products = Products.objects.all() # Fetch only cupcakes
    return render(request, 'app/products.html', {'products': products})

def cart_view(request):
    return render(request, 'app/cart.html')  # Cart doesn't need filtering

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import Order, OrderDetail, UserInfo  # Using Order instead of Orders

@csrf_exempt  # If you're handling CSRF with JavaScript tokens
def place_order(request):
    if request.method == 'POST':
        try:
            print("POST data received:", request.body)  # Debugging incoming POST request
            data = json.loads(request.body)

            # Fetch username and cart data from the request body
            username = data.get('username')
            cart = data.get('cart')
            total_price = data.get('total_price')

            # Retrieve user instance from UserInfo
            user = UserInfo.objects.get(username=username)
            
            # Debugging information to verify received data
            print("Username:", username, "Cart Items:", cart, "Total Price:", total_price)

            # Create an order record in the Order table
            order = Order.objects.create(
                username=user,
                total_price=total_price,
                order_date=timezone.now()
            )

            # Loop through the cart items and create order details for each
            for item in cart:
                OrderDetail.objects.create(
                    order=order,
                    product_name=item['name'],
                    quantity=item['quantity']
                )

            return JsonResponse({'success': True})

        except UserInfo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found'})
        except Exception as e:
            print("Error:", str(e))  # Log error details
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

def view_orders(request):
    orders = Order.objects.select_related('username').prefetch_related('orderdetail_set').all()  # Fetch related user and order details
    return render(request, 'app/admin.html', {'orders': orders})



from django.http import JsonResponse

from django.shortcuts import render
from .models import Order, OrderDetail

# def view_user_orders(request):
#     # Get the logged-in user's username from the request
#     username = request.GET.get('username')
    
#     if username:
#         # Fetch orders only for the specified user
#         orders = Order.objects.select_related('username').prefetch_related('orderdetail_set').filter(username__username=username)
#     else:
#         # No username provided, return an empty order list
#         orders = []

#     # Render the user dashboard template and pass the orders
#     return render(request, 'app/user.html', {'orders': orders})


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products  # Assuming you have a Product model

@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = Products.objects.get(name=data['name'])  # Identify product by name
            product.image = data['image']
            product.desc = data['description']
            product.price = data['price']
            product.category = data['category']
            product.save()

            return JsonResponse({'success': True})
        except Products.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt

def delete_product(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        product_name = data.get('name')

        try:
            product = Products.objects.get(name=product_name)
            product.delete()
            return JsonResponse({'success': True})
        except Products.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        image = data.get("image")
        desc = data.get("desc")
        price = data.get("price")
        category = data.get("category")

        
        if not all([name, image, desc, price, category]):
            return JsonResponse({"success": False, "error": "All fields are required!"})

        
        # Ensure name & category do not already exist
        if Products.objects.filter(name=name, category=category).exists():
            return JsonResponse({"success": False, "error": "Product already exists!"})
        
        # Insert into database
        new_product = Products(name=name, image=image, desc=desc, price=price, category=category)
        new_product.save()

        return JsonResponse({"success": True})
    
    return JsonResponse({"success": False, "error": "Invalid request method!"})


from django.http import JsonResponse
from .models import UserInfo

def get_user_details(request):
    username = request.GET.get("username")
    if username:
        try:
            user = UserInfo.objects.get(username=username)
            return JsonResponse({
                "success": True,
                "address": user.address,
                "phone": user.phone
            })
        except UserInfo.DoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})
