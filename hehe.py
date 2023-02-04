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
