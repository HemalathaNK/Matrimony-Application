from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, VideoForm
from .models import Signup
from django.db.models import Q



def login_fun(request):
    if request.method == "POST":
        email=request.POST['txtmail']
        password=request.POST["txtpswd"]

        user = User.objects.get(email=email)
        user = authenticate(request,username=user.username,email=email,password=password)
        if user is not None:
            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_authenticated:
                login(request, user)

                profile = Signup.objects.get(user=user)

                if profile.gender.lower() == 'male':
                    return redirect('brides_profiles')

                elif profile.gender.lower() == 'female':
                    return redirect('grooms_profiles')
                else:
                    return redirect('home')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup_fun(request):
    if request.method == 'POST':

        # Retrieve form data
        name = request.POST["txtname1"]
        email = request.POST["txtmail1"]
        password = request.POST["pswd"]
        mobile = request.POST["txtmob"]
        age = request.POST["txtage"]
        gender = request.POST["gender"]
        height = request.POST['height']
        marital_status = request.POST["maritalStatus"]
        religion = request.POST["religion"]
        mother_tongue = request.POST["motherTongue"]
        family_type = request.POST["familyType"]
        job_details = request.POST["jobDetails"]
        salary = request.POST["salary"]
        address = request.POST["txtaddrs"]
        profile_picture = request.FILES['photo']
        video= request.FILES['video']

        # Check if username or email already exists
        if User.objects.filter(email=email).exists():
            data = {"msg": " Email already exists"}
            return render(request, 'signup.html', data)
        else:
            # Create a user object in the User model
            user1 = User.objects.create_user(username=name, email=email, password=password)
            user1.save()

            # Create a corresponding entry in the Signup model
            signup = Signup(
                user=user1,          # Link the signup to the created user
                name=name,
                email=email,
                password=password,
                mobile=mobile,
                age=age,
                gender=gender,
                height=height,
                marital_status=marital_status,
                religion=religion,
                mother_tongue=mother_tongue,
                family_type=family_type,
                job_details=job_details,
                salary=salary,
                address=address,
                profile_picture=profile_picture,
                video=video
            )
            signup.save()

            login(request, user1)

            # Redirect to login or success page
            return redirect('login')
    else:
        return render(request, 'signup.html')

def video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)  # Handle form and files
        if form.is_valid():
            form.save()  # Save the new signup with image
            return redirect('login')  # Redirect to homepage or success page
    else:
        form = VideoForm()
    return render(request, 'signup.html', {'form': form})



def home_page(request):
    profiles = Signup.objects.all()
    return render(request, 'home.html', {'profiles': profiles})

def brides_profiles(request):
    brides = Signup.objects.filter(gender='Female')
    return render(request, 'brides_profiles.html', {'brides': brides})


def grooms_profiles(request):
    grooms = Signup.objects.filter(gender='Male')
    return render(request, 'grooms_profiles.html', {'grooms': grooms})


def bride_details(request,id):
    bride = Signup.objects.get(id=id)
    context = {
        "id": id,
        "bride": bride
    }
    return render(request, "bride_details.html", context)


def groom_details(request,id):
    groom = Signup.objects.get(id=id)
    context = {
        "id": id,
        "groom": groom
    }
    return render(request, "groom_details.html", context)


def see_details(request, id,):
        profile = Signup.objects.get(id=id)
        # Pass the user and profile to the template
        context = {
            "id": id,
            "profile": profile
        }
        return render(request, "see_details.html", context)


def profile_fun(request):
    profile = Signup.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

def update_profile(request):
    user = request.user
    profile_edit = Signup.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_edit)
        if form.is_valid():
            form.save()

            user.username = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.save()

            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile_edit)
    return render(request, 'update_profile.html', {'form': form},)


def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')

def logout_fun(request):
    logout(request)  # Log out the user
    return redirect('login')

def search_profiles(request):
    query = request.GET.get('q', '')
    job_details = request.GET.get('job_details', '')
    salary = request.GET.get('salary', '')
    religion = request.GET.get('religion', '')
    marital_status = request.GET.get('marital_status', '')
    mother_tongue = request.GET.get('mother_tongue', '')
    family_type = request.GET.get('family_type', '')


    profiles = Signup.objects.all()

    #search by name, age, height, or address
    if query:
        profiles = profiles.filter(
            Q(name__icontains=query) |
            Q(age__icontains=query) |
            Q(height__icontains=query) |
            Q(address__icontains=query)
        )

    if job_details:
        profiles = profiles.filter(job_details=job_details)
    if salary:
        profiles = profiles.filter(salary=salary)
    if religion:
        profiles = profiles.filter(religion=religion)
    if marital_status:
        profiles = profiles.filter(marital_status=marital_status)
    if mother_tongue:
        profiles = profiles.filter(mother_tongue=mother_tongue)
    if family_type:
        profiles = profiles.filter(family_type=family_type)


    if request.user.is_authenticated:
        current_profile = Signup.objects.get(user=request.user)
        current_gender = current_profile.gender.lower()

        if current_gender == 'male':
            profiles = profiles.filter(gender__iexact='female')
         
        elif current_gender == 'female':
            profiles = profiles.filter(gender__iexact='male')


    return render(request, 'search_profiles.html', {'profiles': profiles, 'query': query})

