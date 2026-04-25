original_bill_amount = int(input("Enter original bill amount:\n"))

tax = int(input("Enter tax percentage(5, 12, 18):\n"))

tip = int(input("Enter tip percentage(0, 5, 10, 15, 20):\n"
""))

tax_amount = original_bill_amount*(tax/100)
tip_amount = original_bill_amount*(tip/100)

if tax not in [5, 12, 18]:
   print("Invalid percentage")
   exit()



if tip == 0: 
   Total_amount = original_bill_amount + tax_amount+tip_amount
   print("\n-------- BILL SUMMARY --------")
   print(f"Total Amount:Rs. {Total_amount}\n")


   
elif tip in [5, 10, 15, 20]:
    Total_amount = original_bill_amount+  tip_amount +  tax_amount

    print(f"Total Amount(tax+tip(if any)): Rs {Total_amount}\n")

split= input("1.Print final amount\n2.Split amount?\n")

if split=="1":
 print("\n-------- BILL SUMMARY --------")
 print(f"Final amount: Rs. {Total_amount:.2f}\n")
 print(f"Tax ({tax}%)       : Rs. {tax_amount:.2f}")
 print(f"Tip ({tip}%)       : Rs. {tip_amount:.2f}")
 print("------------------------------")
 print(f"Total Amount    : Rs. {Total_amount:.2f}")

if split == "2":
   splitting=(input("1. Split equally \n 2.Split Unequally\n"))

   if splitting == "1":
        no_of_ppl =int(input( "Enter total number of people:\n"))
        split_eq = Total_amount/no_of_ppl
        print("\n-------- BILL SUMMARY --------")
        print(f"Final amount: Rs. {Total_amount:.2f}\n")
        print(f"Tax ({tax}%)       : Rs. {tax_amount:.2f}")
        print(f"Tip ({tip}%)       : Rs. {tip_amount:.2f}")
        print("------------------------------")
        print(f"Total Amount    : Rs. {Total_amount:.2f}")
        print("--------------SPLIT EQUALLY--------------")
        print(f"Number of people : {no_of_ppl}")
        print(f"Each person pays : {split_eq:.2f}")

   else:
      number = int(input("Enter total number of people:\n"))
      list_of_spending =[]
      
      for i in range(number):
        
          per_person=(int(input(f"Enter amount for {i+1} person:\n")))
          list_of_spending.append(per_person)
          
      print("--------------SPLIT UNEQUALLY--------------")
      print(f"Number of people : {number}")

      for i in range(number):
       per_person= list_of_spending[i]
       final_eachperson_amt = (per_person/original_bill_amount) * Total_amount
       
       
       print(f"User {i+1} pays {final_eachperson_amt:.2f}")
       

    