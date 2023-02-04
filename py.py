import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neural_network import MLPClassifier  #multi layer perception classifier

import matplotlib.pyplot as plt
import numpy as np

var = False

while var==False:
  try:
    headacheS = int(input("Are you experiencing headaches? Please enter 0 for none, or rate it from 1 to 10, with 10 being severe.")) #
    nauseaS = int(input("Are you experiencing nausea? Please enter 0 for none, or rate it from 1 to 10, with 10 being severe.")) #
    haloS = int(input("Are you seeing halos? These are bright circles around lights. Please enter 0 for none, or rate it from 1 to 10, with 10 seeing the most halos."))
    familyHisotryS = int(input("Do you have a family history of cataracts or any type of glaucoma? Please enter 0 for none, or 1 for yes."))
    blurryVisionS = int(input("Is your vision blurry? Enter 0 if not blurry, or rate it from 1 to 10, with 10 being blurriest."))
    blindSpotS = int(input("Have you noticed any blind spots in your side vision? Enter 0 for none, 1 for less than 3, 2 for a few, and 3 for many."))
    hypertensionS = int(input("Do you suffer from high blood pressure? 0 for none, 1 for yes"))
    eyePainS = int(input("Do you feel any eye pains? 0 for none, or rate from 1 to 10, with 10 being the most pain."))
    hypotensionS = int(input("Do you suffer from low blood pressure? 0 for No, 1 for Yes."))
    CentralLosS = int(input("Do you still see what's in the center of your vision? If yes, enter 0. If no, please rate it from 1 to 10, with 10 seeing nothing."))
    var = True
  except:
    print('\033[92m','\033[1m',"Please only enter numbers according to the instructions!",'\033[0m2')

patientData = np.array([[headacheS,nauseaS,haloS,familyHisotryS,blurryVisionS,blindSpotS,hypertensionS,eyePainS,hypotensionS,CentralLosS]])

features = np.array([[8,7,3,1,6,1,0,9,0,0],[0,0,1,1,3,3,1,0,0,2],[0,0,4,1,6,0,0,1,0,0],[8,3,0,0,4,2,0,0,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,6,0,0,0,0,0],[2,1,2,1,6,3,1,9,0,0],[1,0,1,1,8,2,1,0,0,5],[0,0,3,0,9,1,0,0,0,0],[6,0,1,0,8,1,1,0,1,2],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,3,1,1,0,0,0],[4,0,0,0,3,0,0,0,1,0],[0,0,0,0,3,0,0,5,0,0],[0,0,7,0,9,0,0,0,0,0],[4,4,0,0,7,0,6,0,0,0],[1,0,0,0,6,0,0,0,0,0],[0,0,3,0,6,0,0,0,0,0],[5,0,0,0,6,0,1,5,0,0],[2,0,0,0,5,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0]])
labels = np.array([2,1,5,3,0,4,1,4,4,3,0,1,3,5,4,2,4,4,5,3,0])

NBclassifier = GaussianNB() # parameters for later, GNB
NBclassifier.fit(features, labels)
##
KNNclassifier = KNeighborsClassifier(n_neighbors=3)
KNNclassifier.fit(features, labels)
##
TRclassifier = DecisionTreeClassifier()
TRclassifier.fit(features, labels)
##
MLclassifier = MLPClassifier(hidden_layer_sizes=20)
MLclassifier.fit(features, labels)
########
NBresult = NBclassifier.predict(patientData)
print(NBresult)
##
KNresult = KNNclassifier.predict(patientData)
print(KNresult)
##
TRresult = TRclassifier.predict(patientData)
print(TRresult)
##
MLresult = MLclassifier.predict(patientData)
print(MLresult)
####
disease = {0:"no disease", 1:"open angle glaucoma", 2:"closed angle glaucoma", 3:"normal tension glaucoma", 4:"cataracts", 5:"diabetic retinopathy"}
print(disease[NBresult[0]],"nb")
print(disease[KNresult[0]],"kn")
print(disease[TRresult[0]],"tr")
print(disease[MLresult[0]],"mlp")

#plot_tree(TRclassifier)
