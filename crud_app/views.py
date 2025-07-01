from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect 
from django.contrib.auth.decorators import login_required
from .models import StudentsData
from .forms import StudentsDataForm


def log_view(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username').strip()
            password = data.get('password').strip()

            user = authenticate(username=username, password=password)
            if user is None:
                return JsonResponse({'message': "Invalid credentials"}, status=401)

            login(request, user)  
            return JsonResponse({'message': "Login successful", 'redirect':'/home/'}, status=200)

        return render(request, 'log.html')    
    except Exception as e:
        return JsonResponse({'message':f'Something went wrong {e}'}, status=500)

@login_required
@csrf_protect    
def add_student(request):
    try:
        if request.method =='POST':

            data = json.loads(request.body)
            form_data = {
                'student_name': data.get('student_name'),
                'subject': data.get('subject'),
                'marks': data.get('marks'),
            }
            form = StudentsDataForm(form_data)

            if not form.is_valid():
                errors = {'message': error for field, error in form.errors.items()}
                return JsonResponse({"message":errors['message']})
            
            if StudentsData.objects.filter(student_name=data.get('student_name'), subject=data.get('subject')).first():
                return JsonResponse({"message":'This subject is already exists for this student..!'}, status=409)
                
            form.save()
            return JsonResponse({'message':'Subject Added Successfully..!', 'redirect':'/home/'}, status=201)
            
    except Exception as e:
        return JsonResponse({"message":f'Something went wrong {e}'}, status=500)

@login_required
@csrf_exempt
def home_view(request):
    try:
        if request.method == 'GET':
            user_data = StudentsData.objects.all()
            return render(request, 'table.html', {"data":user_data})
    except Exception as e:
        return JsonResponse({"message":f"Something went wrong {e}"}, status=500)
    
@login_required
@csrf_protect
def update_view(request, id):
    try:
        user = get_object_or_404(StudentsData, id=id)
        if request.method == 'UPDATE':
            data = json.loads(request.body)

            form_data = {
                'student_name': data.get('student_name'),
                'subject': data.get('subject'),
                'marks': data.get('marks'),  
            }
            form = StudentsDataForm(form_data, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                
                return JsonResponse({"message":'Data updated successfully..!', 'redirect':'/home/'}, status=200)
            else:
                errors = {'message': error for field, error in form.errors.items()}
                return JsonResponse({"message":errors['message']}, status=400)
        else:
            form = StudentsDataForm(instance=user)

        return render(request, 'table.html', {'form': form, 'user': user })

    except Exception as e:
        return JsonResponse({"error":f'Something went wrong..{e}'}, status=500)
   
@login_required
@csrf_exempt
def delete_view(request, id):
    try:
        if request.method == 'DELETE':
            user = get_object_or_404(StudentsData, id=id)
            user.delete()
            return JsonResponse({"message":'Data deleted successfully..!', 'redirect':'/home/'}, status=200)
        else:
            return JsonResponse({"message": "Method not allowed."}, status=405)
    except Exception as e:
        return JsonResponse({"message": f"Something went wrong: {e}"}, status=500)

@login_required
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({'message':'Successfully logged out..!', 'redirect':'/login/'}, status=200)
    except Exception as e:
        return JsonResponse({"message": f"Something went wrong: {e}"}, status=500)  