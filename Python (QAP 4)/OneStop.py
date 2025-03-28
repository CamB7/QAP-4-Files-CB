# Description: One Stop Insurance Company - Customer Claim Processing
# Author: Cameron Boyer
# Date(s): March 14, 2025 - March 19, 2025


# Define required libraries.
import FormatValues as FV
import datetime
import time
import sys
import os


# Define program constants.
f = open('Def.dat','r')
POLICY_NUMBER = int(f.readline().strip())  # Use .strip() to remove the any blanks spaces and newline characters.
BASIC_PREMIUM = float(f.readline().strip())
ADDITIONAL_CAR_DIS = float(f.readline().strip())
EXTRA_LIABILITY = float(f.readline().strip())
GLASS_COVERAGE = float(f.readline().strip())
LOANER_COVERAGE = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
PROCESS_FEE = float(f.readline().strip())
f.close()

CUR_DATE = datetime.datetime.now()


# Define program functions.
 
 # See FormatValues.py for the format functions.

def CalculatePremium(NumCars, ExtraLiabilityAmt, GlassCoverage, LoanerCoverage):
    BasePremium = BASIC_PREMIUM
    if NumCars > 1:
        BasePremium += (BASIC_PREMIUM * (NumCars - 1) * ADDITIONAL_CAR_DIS)
    
    ExtraLiabilityTotal = ExtraLiabilityAmt * NumCars
    GlassCoverageTotal = GlassCoverage * NumCars
    LoanerCoverageTotal = LoanerCoverage * NumCars
    
    return BasePremium + ExtraLiabilityTotal + GlassCoverageTotal + LoanerCoverageTotal

def CalculatePayments(MonthlyPremium, PayPlan):
    # Function will accept the basic premium, payment plan, and down payment - returns the monthly payment.
    
    if PayPlan == "Full":
        MonthlyPremium = 0
        return MonthlyPremium
    else:
        MonthlyPremium = (TotalPremium + PROCESS_FEE) / 8  # Down payment is deducted from total premium in calculations.
        return MonthlyPremium  

def GetFirstPayment(InvoiceDate):
    # Convert InvoiceDate to date
    if isinstance(InvoiceDate, datetime.datetime):
        InvoiceDate = InvoiceDate.date()
    
    # Calculate payment date (+20 days)
    PaymentDate = InvoiceDate + datetime.timedelta(days=20)
    
    # Get first of next month
    if PaymentDate.month == 12:
        FirstOfNext = datetime.date(PaymentDate.year + 1, 1, 1)  # Year + 1, January, 1st day
    else:
        FirstOfNext = datetime.date(PaymentDate.year, PaymentDate.month + 1, 1) # Same year, next month, 1st day
    
    # Compare only date objects
    return max(PaymentDate, FirstOfNext) # Max is used to get the later date

# For fun :)
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = (iteration / float(total)) * 100
    percent_display = f"{percent:.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent_display}% {suffix}')
    sys.stdout.flush() 


# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    while True:
        # Clear the screen.
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("One Stop Insurance Company - Customer Claim Processing")
        print()
        print()
        CustNameFirst = input("Enter the customer's first name: ").title()
        if CustNameFirst == "":
            print()
            print("Input Error - First name must be entered.")
            print()
        else:
            break
    
    while True:
        print()
        CustNameLast = input("Enter the customer's last name: ").title()
        if CustNameLast == "":
            print()
            print("Input Error - Last name must be entered.")
            print()
        else:
            break

    while True:
        print()
        Address = input("Enter the customer's address: ").title()
        if Address == "":
            print()
            print("Input Error - Address must be entered.")
            print()
        else:
            break

    while True:
        print()
        City = input("Enter the customer's city: ").title()
        if City == "":
            print()
            print("Input Error - City must be entered.")
            print()
        else:
            break

    while True:
        print()
        ProvLst = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
        Province = input("Enter the customer's province: ").upper()
        if Province == "":
            print()
            print("Input Error - Province must be entered.")
            print()
        elif Province not in ProvLst:
            print()
            print("Input Error - Province must be a valid two-letter abbreviation.")
            print()
        else:
            break

    while True:
        print()
        PostalCode = input("Enter the customer's postal code: ").upper()
        if PostalCode == "":
            print()
            print("Input Error - Postal code must be entered.")
            print()
        elif len(PostalCode) != 6:
            print()
            print("Input Error - Postal code must be 6 characters.")
            print()
        else:
            break
    
    while True:
        print()
        Phone = input("Enter the customer's phone number (10 digits): ")
        if Phone == "":
            print()
            print("Input Error - Phone number must be entered.")
            print()
        elif len(Phone) != 10:
            print()
            print("Input Error - Phone number must be 10 digits.")
            print()
        elif Phone.isdigit() == False:
            print()
            print("Input Error - Phone number must be all digits.")
            print()
        else:
            break

    while True:
        print()
        NumCars = int(input("Enter the number of cars to be insured: "))
        if NumCars == "":
            print()
            print("Input Error - Number of cars must be entered.")
            print()
        elif NumCars < 1:
            print()
            print("Input Error - Number of cars must be greater than 0.")
            print()
        else:
            break
        
    while True:
        print()
        ExtraLiability = input("Do you want extra liability coverage? (Y/N): ").upper()
        if ExtraLiability == "":
            print()
            print("Input Error - Must be entered.")
            print()
        elif ExtraLiability != "Y" and ExtraLiability != "N":
            print()
            print("Input Error - Must enter Y or N.")
            print()
        elif ExtraLiability == "N":
            break
        else:
            break
    
    while True:
        if ExtraLiability == "Y":
            print()
            ExtraLiabilityAmt = float(input("Enter the extra liability amount up to $1,000,000: "))
            if ExtraLiabilityAmt == "":
                print()
                print("Input Error - Must enter an amount.")
                print()
            elif ExtraLiabilityAmt > 1000000:
                print()
                print("Input Error - Amount must be less than or equal to $1,000,000.")
                print()
            else:
                break
        else:
            ExtraLiabilityAmt = 0
            break

    while True:
        print()
        GlassCoverage = input("Do you want glass coverage? (Y/N): ").upper()
        if GlassCoverage == "":
            print()
            print("Input Error - Must be entered.")
            print()
        elif GlassCoverage != "Y" and GlassCoverage != "N":
            print()
            print("Input Error - Must enter Y or N.")
            print()
        elif GlassCoverage == "N":
            GlassCoverage = 0
            break
        else:
            GlassCoverage = GLASS_COVERAGE
            break

    while True:
        print()
        LoanerCar = input("Would you like a loaner car? (Y/N): ").upper()
        if LoanerCar == "":
            print()
            print("Input Error - Must be entered.")
            print()
        elif LoanerCar != "Y" and LoanerCar != "N":
            print()
            print("Input Error - Must enter Y or N.")
            print()
        elif LoanerCar == "N":
            LoanerCoverage = 0
            break
        else:
            LoanerCoverage = LOANER_COVERAGE
            break
    
    while True:
        DownPayment = 0
        print()
        PayPlanLst = ["Full", "Monthly", "Down Pay"]
        PayPlan = input("Enter the payment plan (Full, Monthly, Down Pay): ").title()
        if PayPlan == "":
            print()
            print("Input Error - Must be entered.")
            print()
        elif PayPlan not in PayPlanLst:
            print()
            print("Input Error - Must enter Full, Monthly, or Down Pay.")
            print()
        elif PayPlan == "Down Pay":
            print()
            DownPayment = float(input("Enter the down payment amount: "))
            break
        else:
            break
    
    PrevClaimLst = [['0642', '2020-03-01', 5137.86], ['0817', '2022-05-11', 13725.51]]

    while True:
        print()
        PrevClaims = input("Enter Customer's Previous Claims (Y/N): ").upper()
        if PrevClaims == "Y":  
            while True:
                print()
                PrevClaimNums = input("Enter the claim number: ")
                if PrevClaimNums == "":
                    print()
                    print("Input Error - Must be entered.")
                    print()
                else:
                    break
            
            while True:
                print()
                PrevClaimDates = input("Enter the claim date (yyyy-mm-dd): ")
                if PrevClaimDates == "":
                    print()
                    print("Input Error - Must be entered.")
                    print()
                else:
                    break
            
            while True:
                print()
                PrevClaimAmts = float(input("Enter the claim amount: "))
                if PrevClaimAmts == "":
                    print()
                    print("Input Error - Must be entered.")
                    print()
                else:
                    break

            # Create a list for the current claim and append to PrevClaimLst
            ClaimDetails = [PrevClaimNums, PrevClaimDates, PrevClaimAmts]
            PrevClaimLst.append(ClaimDetails)        
        else:
            break        

    
    # Clear the screen and show the progress bar.
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("Saving customer claim and preparing insurance policy...")
    print()
    
    TotalIterations = 45 # The more iterations, the more time is takes.
    Message = "Processing..."

    for i in range(TotalIterations + 1):
        time.sleep(0.1)  
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
    
    
    # Perform required calculations.
    InsurancePremium = CalculatePremium(NumCars, ExtraLiabilityAmt, GlassCoverage, LoanerCoverage)

    HST = InsurancePremium * HST_RATE
    TotalPremium = InsurancePremium + HST - DownPayment 

    MonthlyPremium = CalculatePayments(TotalPremium, PayPlan)
    ProcessFee = PROCESS_FEE

    InvoiceDate = CUR_DATE
    FirstPayDate = GetFirstPayment(InvoiceDate)
    
    ExtraLiabilityTotal = ExtraLiabilityAmt * NumCars
    GlassCoverageTotal = GlassCoverage * NumCars
    LoanerCoverageTotal = LoanerCoverage * NumCars

    ExtraCarCost = (NumCars - 1) * BASIC_PREMIUM * ADDITIONAL_CAR_DIS 

    
    # Format results for display    
    InvoiceDateDsp = FV.FDateM(InvoiceDate)
    FirstPayDateDsp = FV.FDateS(FirstPayDate)
    
    CustName = CustNameFirst + " " + CustNameLast
    AddressDsp = Address + ", " + City + ", " + Province + " " + PostalCode
    PhoneDsp = FV.FPhone14(Phone)

    BasicPremiumDsp = FV.FDollar2(BASIC_PREMIUM)
    ExtraCarCostDsp = FV.FDollar2(ExtraCarCost)
    ExtraLiabilityAmtDsp = FV.FDollar2(ExtraLiabilityTotal)
    GlassCoverageDsp = FV.FDollar2(GlassCoverageTotal)
    LoanerCoverageDsp = FV.FDollar2(LoanerCoverageTotal)
    
    InsurancePremiumDsp = FV.FDollar2(InsurancePremium)
    HSTDsp = FV.FDollar2(HST)
    TotalPremiumDsp = FV.FDollar2(TotalPremium)
    MonthlyPremiumDsp = FV.FDollar2(MonthlyPremium)
 
    
    # Clear the screen and display the results.
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print()
    print(f"One Stop Insurance Company                  Policy Number:     {POLICY_NUMBER:>5d}")
    print(f"--------------------------                  Invoice Date:  {InvoiceDateDsp}")
    print()
    print(f"Customer:   {CustName:<30s}")
    print(f"            {PhoneDsp:<13s}")
    print()
    print(f"Address:    {AddressDsp:<30s}")
    print()
    print("--------------------------------------------------------------------")
    print()
    print("Insurance Premium Breakdown:")
    print()
    print(f"Payment Plan: {PayPlan:<8s}")
    print()
    print(f"Basic Premium:      {BasicPremiumDsp:>10s}        Extra Liability: {ExtraLiabilityAmtDsp:>13s}")
    print(f"Extra Vehicle Cost: {ExtraCarCostDsp:>10s}")
    print(f"Glass Coverage:     {GlassCoverageDsp:>10s}")
    print(f"Loaner Coverage:    {LoanerCoverageDsp:>10s}")
    print()
    print(f"Insurance Premium:  {InsurancePremiumDsp:>13s}     HST:               {HSTDsp:>11s}")

    if PayPlan == "Down Pay":
        print(f"Down Payment:       {FV.FDollar2(DownPayment):>13s}")
    
    print(f"Total Premium:      {TotalPremiumDsp:>13s}     Monthly Premium:   {MonthlyPremiumDsp:>11s}")
    print()
    print("--------------------------------------------------------------------")
    print()
    print(f"                   First Payment Due:  {FirstPayDateDsp}")
    print()
    print("        ---------------------------------------------------")
    print()
    print("          Previous Claims:")
    print()
    print("             Claim #        Claim  Date        Amount")
    print("            ------------------------------------------")
    
    for claim in PrevClaimLst:
        PrevClaimNum = claim[0]
        PrevClaimDate = claim[1]
        PrevClaimAmt = claim[2]
        print(f"             {PrevClaimNum:>5s}          {PrevClaimDate:>10s}      {FV.FDollar2(PrevClaimAmt):>10s}")
        
           
    print("        ---------------------------------------------------")
    print()
    print("            Thank you for choosing One Stop Insurance!")
    print()

              
    # Write the values to a data file for storage.
    f = open("InsuranceData.dat", "a")
    
    f.write(f"{POLICY_NUMBER}, ")
    f.write(f"{CustName}, ")
    f.write(f"{Phone}, ")
    f.write(f"{Address}, ")
    f.write(f"{City}, ")
    f.write(f"{Province}, ")
    f.write(f"{PostalCode}, ")
    f.write(f"{FV.FNumber0(NumCars)}, ")
    f.write(f"{PayPlan}, ")
    f.write(f"{FV.FDollar2(ExtraLiabilityTotal)}, ")
    f.write(f"{FV.FDollar2(GlassCoverageTotal)}, ")
    f.write(f"{FV.FDollar2(LoanerCoverageTotal)}, ")
    f.write(f"{FV.FDollar2(InsurancePremium)}, ")
    f.write(f"{FV.FDollar2(DownPayment)}, ")
    f.write(f"{FV.FDollar2(TotalPremium)}, ")
    f.write(f"{FV.FDateM(InvoiceDate)}, ")
    f.write(f"{FV.FDateS(FirstPayDate)}\n")

    f.close()


    # Increment the policy number.
    POLICY_NUMBER += 1
  
   
   # Write the values to Def.dat file for storage.
    f = open('Def.dat','w')
    f.write(f"{POLICY_NUMBER}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{ADDITIONAL_CAR_DIS}\n")
    f.write(f"{EXTRA_LIABILITY}\n")
    f.write(f"{GLASS_COVERAGE}\n")
    f.write(f"{LOANER_COVERAGE}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")
    f.close()
        
          
   # Ask user if they would like to process another customer claim. 
    print()   
    Continue = input("     Would you like to process another customer claim? (Y/N): ").upper()
    if Continue != "Y":
        print()
        print("                          ***  Goodbye!  ***")
        print()
        break
    else:
        # For some more fun :)
        for _ in range(5):  # Change to control no. of 'blinks'
            print("                 \033[1mPreparing another customer claim...\033[0m", end='\r') # Bold text
            time.sleep(.3)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            time.sleep(.3)
            print("                 ", end='\r')
      
# Any housekeeping duties at the end of the program.