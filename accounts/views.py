from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt

import json

User = get_user_model()


# Create your views here.
@csrf_exempt
def register_user(req):
    """
    This view is used to register a new user to the system.
    It takes an HTTP request object as an argument and returns
    an HTTP response object.
    The view is responsible for rendering the registration form
    and handling the registration process.
    """

    if req.method == "POST":
        data = json.loads(req.body)
        email = data.get("email")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        user = User.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name)
        return JsonResponse({"message": f"User created successfully , user_name={user.first_name}"}, status=201)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def login_user(req):
    """
    This view is used to log a user into the system.
    It takes an HTTP request object as an argument and returns
    an HTTP response object.
    The view is responsible for rendering the login form
    and handling the login process.
    """

    if req.method == "POST":
        data = json.loads(req.body)
        email = data.get("email")
        password = data.get("password")

        user = authenticate(req, email=email, password=password)
        if user is not None:
            return JsonResponse({"message": f"User logged in successfully , email={user.email}"}, status=200)

        return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required(login_url="/accounts/login")
def logout_user(req):
    """
    This view is used to log a user out of the system.
    It takes an HTTP request object as an argument and returns
    an HTTP response object.
    The view is responsible for handling the logout process.
    """
    logout(req)
    return JsonResponse({"message": "User logged out successfully"}, status=200)


@login_required(login_url="/accounts/login")
def profile_view(req):
    """
    This view is used to show the user's profile page.
    It takes an HTTP request object as an argument and returns
    an HTTP response object.
    The view is responsible for rendering the profile page
    and handling any necessary logic.
    """
    user = req.user
    return JsonResponse({"first_name": user.first_name, "email": user.email, "is_staff": user.is_staff, "is_superuser": user.is_superuser, "permissions": list(user.get_all_permissions())}, status=200)
    pass
