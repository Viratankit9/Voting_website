from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreatePollForm
from .models import Poll, Category, UserVote
from django.contrib import messages



@login_required(login_url='login')
def home(request):
    polls = Poll.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        poll_id = request.POST.get("id")  # Corrected to "id" from "id"
        poll = get_object_or_404(Poll, id=poll_id)
        poll.delete()
        messages.success(request, "Poll deleted successfully")

        # Redirect after successful deletion, if desired
        return redirect('home')

    context = {
        'polls': polls
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            # Get the category data from the form
            category_id = request.POST.get('category')
            new_category_name = request.POST.get('new_category')
            
            # Check if the user selected an existing category or entered a new one
            if category_id:
                category = Category.objects.get(id=category_id)
            elif new_category_name:
                # Create a new category if the user entered a new one
                category = Category.objects.create(name=new_category_name)
            
            # Save the poll with the selected category
            poll = form.save(commit=False)
            poll.category = category
            poll.save()
            
            return redirect('home')
    else:
        form = CreatePollForm()
    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    # Check if the user has already voted for this poll
    if UserVote.objects.filter(user=request.user, poll=poll).exists():
        messages.error(request, "You have already voted for this poll.")
        return redirect('results', poll_id=poll.id)

    if request.method == 'POST':
        selected_option = request.POST.get('poll')

        # Validate selected option
        if selected_option not in ['option1', 'option2', 'option3']:
            messages.error(request, "Invalid form submission.")
            return redirect('vote', poll_id=poll_id)

        # Increment the count of the selected option
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1

        # Save the poll object
        poll.save()

        # Save the user's vote
        UserVote.objects.create(user=request.user, poll=poll)

        messages.success(request, "Your vote has been recorded.")
        return redirect('results', poll_id=poll.id)

    context = {
        'poll': poll,
    }
    return render(request, 'vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('/poll/')

    return render(request, 'login.html')

def signup_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 

       

         # Check if password meets minimum length requirement
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return redirect('signup')
        
        if password != cpassword:
            messages.info(request, 'password did not match')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('signup')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            # password = password if we want add password with encryption id so ...
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('signup')

    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return redirect('login')