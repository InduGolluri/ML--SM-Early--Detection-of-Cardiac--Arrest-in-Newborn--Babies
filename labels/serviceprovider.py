def serviceproviderlogin(request):
 if request.method == "POST":
 admin = request.POST.get('username')
 password = request.POST.get('password')
 if admin == "Admin" and password =="Admin":
 detection_accuracy.objects.all().delete()
 return redirect('View_Remote_Users')
  return render(request,'SProvider/serviceproviderlogin.html')
