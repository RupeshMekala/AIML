
for i in range(5):
         print(f"You ran {i + 1} miles")
         reply = input("Are you tired? \n")

         if i < 4:
               if reply == "yes" or reply == "Yes":
                   print("you didn't finish the race, you pussy!")
                   break

               elif reply == "no" or reply == "No":
                   continue

               else :
                   print("Invalid input")
                   break

         if i == 4:
            print("Congratulations")
            break




