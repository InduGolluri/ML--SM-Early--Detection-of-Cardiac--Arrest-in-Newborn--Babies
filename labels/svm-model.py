# SVM Model
 print("SVM")
 from sklearn import svm
 lin_clf = svm.LinearSVC()
 lin_clf.fit(X_train, y_train)
 predict_svm = lin_clf.predict(X_test)
 svm_acc = accuracy_score(y_test, predict_svm) * 100
 print("ACCURACY")
 print(svm_acc)
 print("CLASSIFICATION REPORT")
 print(classification_report(y_test, predict_svm))
 print("CONFUSION MATRIX")
 print(confusion_matrix(y_test, predict_svm))
 detection_accuracy.objects.create(names="SVM", ratio=svm_acc)
 print("Logistic Regression")
 from sklearn.linear_model import LogisticRegression
 reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
 y_pred = reg.predict(X_test)
 print("ACCURACY")
 print(accuracy_score(y_test, y_pred) * 100)
 print("CLASSIFICATION REPORT")
 print(classification_report(y_test, y_pred))
 print("CONFUSION MATRIX")
 print(confusion_matrix(y_test, y_pred))
 detection_accuracy.objects.create(names="Logistic Regression", 
ratio=accuracy_score(y_test, y_pred) * 100)
 print("Decision Tree Classifier")
 dtc = DecisionTreeClassifier()
44
 dtc.fit(X_train, y_train)
 dtcpredict = dtc.predict(X_test)
 print("ACCURACY")
 print(accuracy_score(y_test, dtcpredict) * 100)
 print("CLASSIFICATION REPORT")
 print(classification_report(y_test, dtcpredict))
 print("CONFUSION MATRIX")
 print(confusion_matrix(y_test, dtcpredict))
 detection_accuracy.objects.create(names="Decision Tree Classifier", 
ratio=accuracy_score(y_test, dtcpredict) * 100)
 labeled = 'labeled_data.csv'
 data.to_csv(labeled, index=False)
 data.to_markdown
 obj = detection_accuracy.objects.all()
 return render(request,'SProvider/train_model.html', {'objs': obj})
