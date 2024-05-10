from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Party, Vote
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def homepage(request):

    return render(request, 'index.html')

@login_required(login_url='el_login')
def elect_poll(request):
    parties = Party.objects.all()
    context={
           'parties': parties,
           'messages': messages.get_messages(request),
    }
    return render(request, 'elect_poll.html', context)

def el_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('el_login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('el_login')
        else:
            login(request, user)
            return redirect('elect_poll')

    return render(request, 'el_login.html')

def el_signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 

         # Check if password meets minimum length requirement
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return redirect('el_signup')
        
        if password != cpassword:
            messages.info(request, 'password did not match')
            return redirect('el_signup')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('el_signup')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            # password = password if we want add password with encryption id so ...
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('el_login')

    return render(request, 'el_signup.html')

def elect_result(request):
    parties = Party.objects.all()
    vote_counts = {}
    total_vote_count = 0
    for party in parties:
        vote_count = Vote.objects.filter(party=party).count()
        vote_counts[party.name] = vote_count
        total_vote_count += vote_count
    return render(request, 'elect_result.html', {'vote_counts': vote_counts, 'total_vote_count': total_vote_count})

@login_required(login_url='el_login')
def submit_vote(request, party_name):
    if request.method == 'POST':
        user = request.user
        
        # Check if the user has already voted for any party
        if Vote.objects.filter(user=user).exists():
            messages.error(request, 'You have already voted. You cannot vote again.')
            return redirect('elect_poll')
        
        try:
            party = Party.objects.get(name=party_name)
            vote = Vote(user=user, party=party)
            vote.save()
            messages.success(request, 'Your vote has been recorded.')
            return redirect('elect_poll')
        except Party.DoesNotExist:
            messages.error(request, 'Party does not exist')
        except Exception as e:
            messages.error(request, str(e))
        
    return redirect('elect_poll')
    

def logout_el_User(request):
    logout(request)
    return redirect('el_login')



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')