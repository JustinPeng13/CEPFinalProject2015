from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from accounts.forms import UserForm, UserProfileForm

# Create your views here.
def registration(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm( data = request.POST )

        # If the two forms are valid...
        if user_form.is_valid() and user_profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            profile = user_profile_form.save( commit = False )
            profile.user = user
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, user_profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'accounts/register.html',
            {'user_form': user_form, 'user_profile_form': user_profile_form, 'registered': registered} )