from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from foobar.models import User
from foobar.forms import UserForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.template import loader, Context
import csv

def list_users(request, csv=False):
    '''
    Returns templte listing all user information
    '''
    users = list(User.objects.all())
    if not csv:
        return render(request, 'list.html', {'users': users})
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="users.csv"'
    t = loader.get_template('generate_csv.txt')
    c = Context({'users': users})
    response.write(t.render({'users': users}))
    return response

def view_user(request, user_id):
    '''
    :param request: HttpRequest object
    :param user_id: id of user to show

    Returns
    =======
    Template containing user information.

    If error occured, it redirects to '/' with an error message.

    '''
    try:
        user = User.objects.get(pk=user_id)
    except:
        messages.error(request, 'There is no user with id {id}.'.format(id=user_id))
        return HttpResponseRedirect('/')
    return render(request, 'view.html', {'user': user})

def add_user(request):
    '''
    :param request: HttpRequest object

    Returns
    =======
    Renrered user form if request was valid, else returns HttpResponseRedirect to '/' with an error message.

    If user was added normally, it redirects to '/' too, but with different message using messages framework.
    '''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data
            try:
                user = User(
                        birthday=post['birthday'],
                        username=post['username'],
                        email=post['email']
                        )
                user.set_password(post['password'])
                user.full_clean()
                user.save()
            except Exception as e:
                messages.error(request, 'Cannot add user like that because {error}'.format(error=str(e)))
                return HttpResponseRedirect('/')
            messages.success(request, 'User added!')
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'action': 'add', 'form': form})

def edit_user(request, user_id):
    '''
    :param request: HttpRequest object
    :param user_id: Id of user to edit

    Redirects to '/' if error ocured, or if user was edited. Result message is passed using messages framework

    GET to this view returns view with user form.
    POST updated user info
    '''
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        messages.error(request, 'There is no user with is {id}'.format(id=user_id))
        return HttpResponseRedirect('/')
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'User edited!')
        return HttpResponseRedirect('/')
    return render(request, 'user_form.html', {'action': 'edit', 'form': form})
