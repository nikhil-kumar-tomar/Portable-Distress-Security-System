from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from .business_logic import *
from django.contrib.auth.decorators import login_required
from .miscellaneous import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def registration(request):
    form=user_create()
    if request.method=="POST":
        form=user_create(request.POST)
        if object_exists(factor={'email':request.POST["email"]},model="User") or object_exists(factor={'username':request.POST["username"]},model="User"):
            messages.error(request,"Email or Username Already Exists, Please use a different email")
            return HttpResponseRedirect("/registration/")
        if form.is_valid():
            form.save()
            user=object_get({'username':request.POST["username"]},"User")
            object_creator(factor={"roll_id":user.id,'phone':request.POST["phone"],'email':request.POST["email"]},model="contact_info")
            token_generate(user)
            cache_object_delete("all_users")
            messages.success(request,"Signed-Up Succesfully")
            return HttpResponseRedirect("/login/")
    context={
        'form':form,
    }
    return render(request,"security/registration.html",context)

def home(request):
    context={}
    if cache_object_exists(f"django.contrib.sessions.cache{request.session.session_key}"):
        context={
            "data":cache_object_get_or_set(f"user_home:{request.user.id}",object_filter_orderby(factor={"roll_id":request.user.id},model="incoming_info",orderby="-id"),settings.CACHES_TTL),
            "authenticated":1, 
            "token": token_get(request.user.id),
        }
    return render(request,"security/home.html",context)

def root(request):
    return HttpResponseRedirect("/home/")

def logins(request):
    form=user_sign()
    if request.method=="POST":
        users=authenticate(username=request.POST["username"],password=request.POST["password"])
        if users != None:
            login(request,users)
            messages.success(request,f"Welcome {request.user.first_name}, You have Logged In Succesfully")
            return HttpResponseRedirect("/")
        else:
            messages.error(request,"Email/Password does not exist")
            return HttpResponseRedirect("/login/")
    context={
        "form":form,
        }
    return render(request,"security/login.html",context)

def logouts(request):
    if cache_object_exists(f"django.contrib.sessions.cache{request.session.session_key}"):
        logout(request)
        messages.success(request,"Logout Successfull")
        return HttpResponseRedirect("/login/")
    else:
        messages.error(request,"Logout failed, Not Logged in currently")
        return HttpResponseRedirect("/login/")

def add_relatives(request):
    context={
        "people":cache_object_get_or_set(f"all_users",object_all("User"),settings.CACHES_TTL),
        }
    if request.method=="POST":
        try:
            if str(request.POST["relatives"]) in [str(x.relation_id) for x in object_filter(factor={"roll_id":request.user.id},model="relation_users")]:
                raise Exception([1062,"Duplication found"])
            object_creator(factor={"roll_id":request.user.id,"relation_id":request.POST["relatives"]},model="relation_users")
            messages.success(request,"Relations added Successfully")
            return HttpResponseRedirect("/add_relatives/")
        except Exception as e:
            if e.args[0]==1062 or e.args[0][0]==1062:
                messages.error(request,"This relation already exists, Please try someone else")
                return HttpResponseRedirect("/add_relatives/")                
    return render(request,"security/relatives_add.html",context)

def search(request):
    form=search_form()
    context={"form":form}
    if request.method=="POST":
        context["query"]=full_text_search(["username","first_name","last_name","email"],model="User",search_term=request.POST['search'])
    return render(request,"security/search.html",context)

def profile(request,relation_id):
    if cache_object_exists(f"django.contrib.sessions.cache{request.session.session_key}"):
        if object_exists({"id":relation_id},"User"):
            context={"object":object_get({"id":relation_id},"User"),"relative_exists":object_exists({"roll_id":request.user.id,"relation_id":relation_id},"relation_users"),"same_user":(request.user.id==relation_id)}
            if request.method=="POST":
                if context["relative_exists"]!=True:
                    if not(object_exists({"user_from_id":request.user.id,"user_to_id":relation_id},"friend_requests")) and send_friend_request(request.user.id,relation_id):
                        messages.success(request,"Friend request sent Successfully")
                    else:
                        messages.error(request,"This relation already exists or a friend request is already sent, Please try someone else")
                    return HttpResponseRedirect(f"/profile/{relation_id}")
                else:
                    if remove_relative(request.user.id,relation_id):
                        messages.success(request,"Relative removed successfully")
                    else:
                        messages.error(request,"Relation couldn't be removed successfully")
                    return HttpResponseRedirect(f"/profile/{relation_id}")
            return render(request,"security/profile.html",context)
        else:
            return HttpResponseRedirect("/home/") 
    else:
        return HttpResponseRedirect("/login/")

def notifications(request):
    context={"requests":object_filter_orderby({"user_to_id":request.user.id},"friend_requests","date")}
    if request.method=="POST":
        for relation_id in list(request.POST)[1:]:
            add_specific_relative(request.user.id,relation_id)
            object_remove({"user_from_id":relation_id,"user_to_id":request.user.id},"friend_requests")   
        messages.success(request,"All requests accepted")
        return render(request,"security/notifications.html",context)    
    return render(request,"security/notifications.html",context)

def rem_relatives(request):
    if cache_object_exists(f"django.contrib.sessions.cache{request.session.session_key}"):
        relatives=[x for x in object_filter(factor={"roll_id":request.user.id},model="relation_users")]
        if request.method=="POST":
            relatives=[object_get(factor={"roll_id":request.user.id,"relation_id":x},model="relation_users").delete() for x in request.POST if request.POST[x]=="on"]
            return HttpResponseRedirect("/rem_relatives/")  
        context={
            "relatives":relatives,
            "authenticated":1,
            }
    else:
        context={}
    return render(request,"security/rem_relatives.html",context)










