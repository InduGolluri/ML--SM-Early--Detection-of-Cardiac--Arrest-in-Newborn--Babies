def View_Prediction_Of_Cardiac_Arrest_Type_Ratio(request):
 detection_ratio.objects.all().delete()
 #ratio = ""
 kword = 'No Cardiac Arrest Found'
 print(kword)
 obj = cardiac_arrest_prediction.objects.all().filter(Q(Prediction=kword))
 obj1 = cardiac_arrest_prediction.objects.all()
 count = obj.count();
 count1 = obj1.count();
 ratio = (count / count1) * 100
 if ratio != 0:
 detection_ratio.objects.create(names=kword, ratio=ratio)
 ratio1 = ""
 kword1 = 'Cardiac Arrest Found'
 print(kword1)
 obj1 = cardiac_arrest_prediction.objects.all().filter(Q(Prediction=kword1))
 obj11 = cardiac_arrest_prediction.objects.all()
 count1 = obj1.count();
 count11 = obj11.count();
 ratio1 = (count1 / count11) * 100
 if ratio1 != 0:
 detection_ratio.objects.create(names=kword1, ratio=ratio1)
 obj = detection_ratio.objects.all()
 return render(request, 
'SProvider/View_Prediction_Of_Cardiac_Arrest_Type_Ratio.html', {'objs': obj})
def View_Remote_Users(request):
 obj=ClientRegister_Model.objects.all()
 return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})
40
def ViewTrendings(request):
 topic = 
cardiac_arrest_prediction.objects.values('topics').annotate(dcount=Count('topics')).order_by
('-dcount')
 return render(request,'SProvider/ViewTrendings.html',{'objects':topic})
def charts(request,chart_type):
 chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
 return render(request,"SProvider/charts.html", {'form':chart1, 
'chart_type':chart_type}
)
def charts1(request,chart_type):
 chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
 return render(request,"SProvider/charts1.html", {'form':chart1, 
'chart_type':chart_type})
def View_Prediction_Of_Cardiac_Arrest_Type(request):
 obj =cardiac_arrest_prediction.objects.all()
 return render(request, 'SProvider/View_Prediction_Of_Cardiac_Arrest_Type.html', 
{'list_objects': obj})
def likeschart(request,like_chart):
 charts =detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
 return render(request,"SProvider/likeschart.html", {'form':charts, 
'like_chart':like_chart})
