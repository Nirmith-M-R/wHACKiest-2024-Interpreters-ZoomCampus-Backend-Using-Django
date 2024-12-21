from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SignUP,Rider,ActiveUser
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            # print(request.body)
            data = request.POST

            # Extract user details
            mail = data.get('mail')
            password = data.get('password')
            name = data.get('name')
            phNo = data.get('phNo')
            gender = data.get('gender')
            program = data.get('program')
            route = data.get('route', [])  # Default to an empty list if not provided

            # Validate mandatory fields
            if not (mail and password and name and phNo and gender and program):
                return JsonResponse({'error': 'All fields except route are required.'}, status=400)

            # Create the user
            user = SignUP.objects.create(
                mail=mail,
                password=password,
                name=name,
                phNo=phNo,
                gender=gender,
                program=program,
                route=route
            )

            # Return success response
            return JsonResponse({'success': f'User {user.name} added successfully!'}, status=201)

        except Exception as e:
            # Handle errors
            return JsonResponse({'error': str(e)}, status=500)

    # If the method is not POST
    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

def activeRider(request):
    mail = request.POST.get('mail')
    
@csrf_exempt
def riderregistercheck(request):
    if request.method == "POST":
        try:
            data = request.POST
            mail = data.get('mail')
            data = SignUP.objects.get(mail=mail)
            if(mail == data.mail):
                return JsonResponse({"Status":"Registered"}, status=200)                
        except:
            return JsonResponse({"Status":"Not Registered"}, status=205)
        
@csrf_exempt
def riderregister(request):
    if request.method == "POST":
        try:
            data = request.POST
            mail = data.get('mail')
            seats = data.get('seats')
            regno = data.get('regno')
            ob = Rider(mail=mail, seats=seats, regNo = regno)
            ob.save()
            return JsonResponse({"Status":"Registration Done"}, status = 200)
        except:
            return JsonResponse({"Status":"Error"}, status=205)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
        

@csrf_exempt
def request_ride(request):
    if request.method == "POST":
        try:
            data = request.POST
            mail = data.get("mail")
            passenger = SignUP.objects.get(mail=mail)
            passenger_route = passenger.route

            rider = ActiveUser.objects.all()

        except:
            pass