students=[]
complaints=[]
companies=[
    {
        "name":"TCS",
        "package":7.5,
        "eligibility_cgpa":7.0
    },
    {
        "name":"Infosys",
        "package":6.0,
        "eligibility_cgpa":6.5
    },
    {
        "name":"Google",
        "package":18.0,
        "eligibility_cgpa":9.0
    }, 
    {
        "name":"Wipro",
        "package":5.5,
        "eligibility_cgpa":8.5
    }
]              
logged_in_stu=None

def my_profile(student):
    while True:
        print("="*60)
        print("                  👤 MY PROFILE 👤               ")
        print("="*60)
        print()
        print("🆔 Student ID:",student["roll_number"])
        print("👨‍🎓 Name:",student["name"])
        print("🏢 Department:",student["dep"])
        print("📚 Year:",student["year"])
        print("🔤 Section:",student["branch"])
        print("📧 Email:",student["email"])
        print("📱 Mobile:",student["phone_no"])
        print("🎓 Admission:",student["ad_year"])
        print("="*60)
        print()
        print()
        print("1.refresh profile")
        print("2.Back")
        c=input("enter your choice:")
        if c=="1":
            continue
        elif c=="2":
            return
        else:
            print("⚠️ Invalid choice. Try again.")

def registration():
    print("="*60)
    print(" 🔐 STUDENT REGISTRATION 🔐 ")
    print("="*60)
    while True:
        name=input("enter your name as per your records:")
        if name.strip()!="":
            break
        print("⚠️ Name cannot be empty. Please enter again.")
    while True:
        rollnum=input("enter your roll number:")
        if rollnum.strip()!="":
            break
        print("⚠️ Roll number cannot be empty. Please enter again.")
    while True:
        age=input("enter your age:")
        if age.isdigit():
            age=int(age)
            if age>0:
                break
            print("⚠️ Age must be greater than 0.")
        else:
            print("⚠️ please enter numbers only.")
    while True:
        gender=input("enter your gender like M/F:")
        if gender.strip()!="":
            break
        print("⚠️ Gender cannot be empty. Please enter again.")
    while True:
        dep=input("enter your department:")
        if dep.strip()!="":
            break
        print("⚠️ Department cannot be empty. Please enter again.")    
    while True:
        branch=input("enter your branch:")
        if branch.strip()!="":
            break
        print("⚠️ Branch cannot be empty. Please enter again.")        
    while True:
        year=int(input("enter your studyding year(1/2/3/4):"))
        if year>=1 or year<=4:
            break
        print("year must be b/w 1 and 4 years.")
    while True:    
        email=input("enter your email ID:")
        if "@" not in email or "." not in email or email.strip()=="":
            print("⚠️ Invalid email format.")
        else:    
            break    
    while True:
        phone_no=input("enter your phone number:")
        if not phone_no.isdigit() or len(phone_no) != 10:
            print("⚠️ Mobile number must contain exactly 10 digits.")
        break
    while True:
        password=input("enter a strong password:")
        if password.strip()=="":
            print("⚠️ Password cannot be empty.")
        break    
    while True:
        cgpa=float(input("Entey CGPA:"))
        if cgpa>=0 and cgpa<=10:
            print("Valid CGPA")
            break
        print("Invalid CGPA") 
    while True:
        ad_year=input("enter your admission year:")
        if ad_year.strip()=="":
            print("⚠️ Required fields cannot be empty.")
        break    
    if student_exists(rollnum,email,phone_no):
        print("Student already exits.")
        return
    stu={
        "name":name,
        "roll_number":rollnum,
        "age":age,
        "gender":gender,
        "dep":dep,
        "branch":branch,
        "year":year,
        "email":email,
        "phone_no":phone_no,
        "password":password,
        "ad_year":ad_year,
        "cgpa":cgpa
    }
    students.append(stu) 
    add_activity(stu,"Student Registered")
    print("          ✅ Registration successful✅")
    print("         👋 Welcome to CAMPUS 360!👋")


def academic_performance(student):  
    subjects = {
    "Python": [18, 16, 9, 72],
    "Java": [17, 15, 8, 68],
    "Data Structures": [18, 16, 9, 72],
    "DBMS": [16, 17, 9, 70],
    "Computer Networks": [15, 16, 8, 65]}
    while True:
        print("="*60)
        print("                 📚 MY ACADEMICS 📚              ")
        print("="*60)
        print()
        print("1. Python")
        print("2. Java")
        print("3. Data Structures")
        print("4. DBMS")
        print("5. Computer Networks")
        print("6. Back")
        sub_choice=int(input("enter subject choice:"))
        if sub_choice==6:
            return
        elif sub_choice==1:
            subject="Python"
        elif sub_choice==2:
            subject="Java"
        elif sub_choice==3:
            subject="Data Structures"
        elif sub_choice==4:
            subject="DBMS" 
        elif sub_choice==5:
            subject="Computer Networks"
        else:
            print("Invalid subject choice try again")
            return
        marks=subjects[subject]
        i1,i2,ass,m=marks
        total=i1+i2+ass+m
        maxi=150
        per=(total/maxi)*100
        print("Subject:",subject)
        print("Internal1",i1,"/20")
        print("Internal2",i2,"/20")
        print("Assignment",ass,"/10")
        print("Model Exam",m,"/100")

        print("Total",total,"/",maxi)
        print("percentage:",per,"%")
        if per>=90:
            print("Grade: A+ ")
        elif per>=80:
            print("Grade: A ")
        elif per>=70:
            print("Grade: B ")
        elif per>=60:
            print("Grade: C ") 
        elif per>=50:
            print("Grade: D ")
        else:
            print("Grade: F ")  
        print()
        if per>=70:
            print("performance= Good")
        elif per>=50:
            print("performance=Average")
        else:
            print("performance=Needs Improvement")                     

def student_login():
    print("="*60)
    print(" 🔐 STUDENT LOGIN 🔐 ")
    print("="*60)
    if len(students)==0:
        print("⚠️ No students are registered yet.")
        print("➡️ Please register first.")
        return
    attempts=0
    max_attempts=3
    found=False
    while attempts<max_attempts:
        login_roll_no=input("🆔enter your roll number:")
        login_Password=input("🔑enter your password:")
        print("Verifying...")
        found=False
        for i in students:
            if login_roll_no==i["roll_number"] and login_Password==i["password"]:
                print("                                    ✅ Login Successful!")
                print("                                    👋 Welcome to CAMPUS 360!")
                print("                                    ➡️ Opening Student Dashboard...")
                logged_in_stu=i
                found=True
                add_activity(i,"logged into portal")
                stu_dashboard(logged_in_stu)
                break
        if found:
            break 
        attempts+=1
        print("⚠️ Invalid Student ID or Password.")
        print("🔄 Please try again.")  
    if not found:
        print("Maximum login attempts reached.")          

def faculty_login():
    faculty = {
        "faculty_id": "F101",
        "password": "1234",
        "name": "Pavan Kalyan",
        "dep": "DSA"
    }
    print("=" * 60)
    print(" 🔐 FACULTY LOGIN 🔐 ")
    print("=" * 60)
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        login_faculty_id = input("🆔 Enter Faculty ID: ")
        login_password = input("🔑 Enter Password: ")
        print("Verifying...")
        found = False
        if login_faculty_id == faculty["faculty_id"]and login_password == faculty["password"]:
            print("✅ Login Successful!")
            print("👋 Welcome to CAMPUS 360!")
            print("➡️ Opening Overview...")           
            found = True
            break
        if found:
            return 
        attempts += 1
        print("⚠️ Invalid Faculty ID or Password.")
        print("🔄 Please try again.")
    print("❌ Maximum login attempts reached.")
def admin_login():
    admin = {
    "admin_id": "A101",
    "password": "admin123",
    "name": "Uppender Reddy"
}
    print("=" * 60)
    print(" 🔐 ADMIN LOGIN 🔐 ")
    print("=" * 60)
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        login_admin_id = input("🆔 Enter Admin ID: ")
        login_password = input("🔑 Enter Password: ")
        print("Verifying...")
        if login_admin_id == admin["admin_id"]and login_password == admin["password"]:
            print("✅ Login Successful!")
            print("👋 Welcome to CAMPUS 360!")
            return 
        attempts += 1
        print("⚠️ Invalid Admin ID or Password.")
        print("🔄 Please try again.")
    print("❌ Maximum login attempts reached.")
            
def attendance():
    att_data={
        "python":[42,45],
        "java":[38,45],
        "dsa":[35,45],
        "dbms":[40,45],
    }
    while True:
        print("="*60)
        print("                  📅 STUDENT ATTENDANCE 📅              ")
        print("="*60)
        print()
        print("Attendance feature")
        total_present=0
        total_class=0
        for i in att_data:
            p,t=att_data[i]
            per=(p/t)*100
            print(i,":",p,"/",t,round(per,2),"%")
            total_present+=p
            total_class+=t

        total=(total_present/total_class)*100
        print()
        print("Overall Attendance:",round(total,2),"%")   

        if total>=75:
            print("Status: Eligible")
        else:
            print("Status: Shortage")
        print()
        print("1.refresh Attendance")
        print("2.Back")
        c=input("enter your choice:")
        if c=="1":
            continue
        elif c=="2":
            return
        else:
            print("⚠️ Invalid choice. Try again.")         

def att_shortage(student):
    while True:
        curr=float(input("enter your current attendance per% :"))
        req=75
        if curr>=req:
            print("No additional Classes required.")
        else:
            print("Current attendance is below required attendance.")
            present=int(input("enter how many classes you attendended:"))
            total=int(input("enter total classes:"))
            per=(present*100)/total
            addi_per=75-per
            addi=(total*addi_per)//100

            print("Additional classes required:",addi)   

            print()
            print("1.refresh Attendance")
            print("2.Back")
            c=input("enter your choice:")
            if c=="1":
                continue
            elif c=="2":
                return
            else:
                print("⚠️ Invalid choice. Try again.") 

def internal_assessment(student):
    asses={
        "int_asses1":{"Python":18,"java":16,"ds":17,"dbms":15,"cn":16},
        "int_asses2":{"Python":19,"java":17,"ds":18,"dbms":16,"cn":17},
        "assign":{"Python":9,"java":8,"ds":9,"dbms":8,"cn":9},
        "model_exam":{"Python":72,"java":68,"ds":74,"dbms":70,"cn":66}
    }  
    while True:
        print("="*60)
        print("                  📅 ASSESSMENT PORTAL 📅              ")
        print("="*60)  
        print("1. 📄Internal Assessment 1")
        print("2. 📄Internal Assessment 2")
        print("3. 📚Assignments")
        print("4. 📝Model Examination")
        print("5. 📊View Overall Result")
        print("6. ⬅️Back")
        choice=int(input("enter your choice:"))
        if choice==6:
            break
        if choice in [1,2,3,4]:
            asses_names={
                1:("Internal Assessment 1","int_asses1"),
                2:("Internal Assessment 2","int_asses2"),
                3:("Assignments","assign"),
                4:("Model Examination","model_exam")
            }   
            select,key=asses_names[choice]
            marks=asses[key]
            print()
            print(select)
            t=0
            for i in marks:
                print(i,":",marks[i])
                t+=marks[i]
            avg=t/len(marks)
            print("Total Marks:",t)
            print("Average:",round(avg,2))
        elif choice==5:
            total=0
            total_max_marks=750
            for i in asses:
                marks=asses[i]
                for j in marks:
                    total+=marks[j]            
            avg=(total/total_max_marks)*100 
            print()
            print("📊 Overall Average:",round(avg,2))
            if avg>=85:
                print("Performance:Excellent") 
            elif avg>=70:
                print("Performance:Good") 
            elif avg>=50:
                print("Performance:Average") 
            else:
                print("Performance:Needs Improvement") 
          
def fee_management(student):
    fees={
        "tution_fee": 100000,
        "trnsport_fee": 20000,
        "exam_fee": 2000,
        "library_fee": 16000,
        "special_fee":20000
    }

    paid=student.get("paid_fee",10000)
    transactions=student.get("transactions",[])

    while True:
        print("="*60)
        print("                 💰 FEE MANAGEMENT 💰             ")
        print("="*60)
        print()
        print("🎓 Tuition Fee :", fees["tution_fee"])
        print("🚌 Transport Fee:", fees["trnsport_fee"])
        print("📝 Exam Fee    :", fees["exam_fee"])
        print("📚 Library Fee:", fees["library_fee"])
        print("💳 Special Fee:", fees["library_fee"])
        print("="*60)

        total = sum(fees.values())
        pending = total - paid

        print("💰 Total   :", total)
        print("✅ Paid    :", paid)
        print("⚠️ Pending :", pending)

        print("="*60)
        print("1. 📋View Details")
        print("2. 💳Payment")
        print("3. 🧾Payment History")
        print("4. ⬅️Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print()
            print("          FEE DETAILS         ")
            for i in fees:
                print(i, ":", fees[i])
            print("💰Total Fee:", total)
            print("✅Paid Fee:", paid)
            print("⚠️Pending Fee:", pending)

        elif choice == 2:
            if pending == 0:
                print("No pending fee.")
            else:
                amount = int(input("💵Enter Amount: "))

                if amount <= 0:
                    print("Enter a valid amount.")
                elif amount > pending:
                    print("Amount is greater than pending fee.")
                else:
                    print("Confirm Payment?")
                    print("1. ✅Yes")
                    print("2. ❌No")

                    conform = int(input("Enter your choice: "))

                    if conform == 1:
                        paid += amount
                        student["paid_fee"]=paid
                        student["transactions"]=transactions
                        pending = total - paid

                        trans_id ="TXT101"+str(len(transactions)+1)

                        transaction = {
                            "id": trans_id,
                            "amount": amount,
                            "status": "PAID"
                        }

                        transactions.append(transaction)

                        print()
                        print("🎉PAYMENT SUCCESSFUL🎉")
                        print("🧾Transaction ID:", trans_id)
                        print("💰Amount:", amount)
                        print("✅Status: PAID")

                    else:
                        print("Payment cancelled.")

        elif choice == 3:
            if len(transactions) == 0:
                print("No payment history available.")
            else:
                print()
                print("PAYMENT HISTORY")

                for i in transactions:
                    print("Transaction ID:", i["id"])
                    print("Amount:", i["amount"])
                    print("Status:", i["status"])
                    print("="*60)

        elif choice == 4:
            break

        else:
            print("Invalid choice try again")

def events_clubs(student):
    events={
    1:{"name":"Hackathon","date":"10-10-2026","venue":"Canteen","total_seats":50,"registered":20},
    2:{"name":"Technical Fest","date":"15-10-2026","venue":"Canteen","total_seats":100,"registered":98},
    3:{"name":"Cultural Fest","date":"20-10-2026","venue":"Canteen","total_seats":120,"registered":66},
    4:{"name":"Sports Meet","date":"25-10-2026","venue":"Canteen","total_seats":200,"registered":154},
    5:{"name":"Workshop","date":"28-10-2026","venue":"Canteen","total_seats":30,"registered":12},
    6:{"name":"Seminar","date":"30-10-2026","venue":"Canteen","total_seats":45,"registered":39},     
    } 

    registered_events =student.get("registered_events",[])

    while True:
        print("="*60)
        print("                  🎉 EVENTS & CLUBS 🎉              ")
        print("="*60)
        print()
        print("1.💻 Hackathon")
        print("2.🛠️ Technical Fest")
        print("3.🎭 Cultural Fest")
        print("4.⚽ Sports Meet")
        print("5.🧑‍🏫 Workshop")
        print("6.🎤 Seminar")
        print("7.⬅️ Back")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        if i in events:
            i= events[i]
            available = i["total_seats"] - i["registered"]
            print()
            print("Event:", i["name"])
            print("Date:", i["date"])
            print("Venue:", i["venue"])
            print("Available Seats:", available)
            print("Registered Count:", i["registered"])
            print()
            print("1. Register")
            print("2. Back")

            action = int(input("Enter your choice: "))

            if action == 1:
                if i["name"] in registered_events:
                    print("You already registered for this event.")

                elif available == 0:
                    print("No seats available for this event try for another event.")

                else:
                    i["registered"] += 1
                    registered_events.append(i["name"])
                    student["registered_events"]=registered_events

                    print("Registration successful.")
                    print("Remaining Seats:", i["total_seats"] - i["registered"])

        else:
            print("Invalid choice try again")

def club_management(student):
    clubs={1:{"name":"CodingClub","capacity":50,"members":20},
           2:{"name":"Robotics Club","capacity":50,"members":10},
           3:{"name":"AI Club","capacity":50,"members":35},
           4:{"name":"Literary Club","capacity":50,"members":20},
           5:{"name":"Photography Club","capacity":50,"members":41},
           6:{"name":"Sports Club","capacity":50,"members":43},
           7:{"name":"Entrepreneurship Club","capacity":50,"members":18},
           }
    joined_clubs=student.get("joined_clubs",[])
    while True:
        print("1.💻 CodingClub")
        print("2.🤖 Robotics Club")
        print("3.🧠 AI Club")
        print("4.📖 Literary Club")
        print("5.📸 Photography Club")
        print("6.⚽ Sports Club")
        print("7.🚀 Entrepreneurship Club")
        print("8.⬅️ back")

        choice=int(input("enter your choice:"))
        if choice==8:
            break
        if choice in clubs:
            club=clubs[choice]
            available=club["capacity"]-club["members"]
            print()
            print("⬅️ club:",club["name"])
            print("👥 Capacity:",club["capacity"])
            print("👥 Registered Members:",club["members"])
            print("💺 Available:",available)
            print()
            print("1.join club:")
            print("2.back")
            choi=int(input("enter your choice:"))

            if choi==1:
                if club["name"] in joined_clubs:
                    print("you already joined this club.")
                elif available==0:
                    print("Club capacity is full.")
                else:
                    club["members"]+=1
                    joined_clubs.append(club["name"])
                    student["joined_clubs"]=joined_clubs

                    print("✅ Succesfully joined",club["name"],"!!!")
                    print("💺 Available Seats:",club["capacity"]-club["members"])
            else:
                print("invalid choice")                

def notification(student):
    print("="*60)
    print("                 🔔 NOTIFICATIONS 🔔              ")
    print("="*60)
    found=False
    att_per=70
    fee_pending=10000
    int_ass_started=False
    hackathon=True
    place_elig=True
    if att_per<75:
        print("1.your DSA attendenct is b/w 75%.")
        found=True
    if not int_ass_started:
        print("2.Internal Assessment 2 starts next week.")
        found=True
    if hackathon:
        print("3.Hacktathon registrations are open please go to club &events menu") 
        found=True
    if fee_pending>0:
        print("4.Your fee payment is pending.")
        found=True
    if place_elig:
        print("5.you are eleigible for upcoming placement drrive.")
        found=True
    if not found:
        print("No new notifications.")

def placement_portal(student):
    companies={
        1:{"name":"Software Company A","role": "Software Developer","package": "8 LPA","cgpa": 7.5,"backlogs": 1,"attendance": 80},
        2:{"name":"Software Company B","role": "Web Developer","package": "5.5 LPA","cgpa": 8.0,"backlogs": 1,"attendance": 75},
        3:{"name":"Product Company C","role": "Python Developer","package": "6.5 LPA","cgpa": 6.5,"backlogs": 2,"attendance": 64},
        4:{"name":"Service Company D","role": "Data Scietiest","package": "12 LPA","cgpa": 8.5,"backlogs": 0,"attendance": 85},
    }
    applications=student.get("applications",[])

    while True:
        print("="*60)
        print("                 📊  PLACEMENT PORTAL 📊              ")
        print("="*60) 
        print()
        print("1. Software Company A")
        print("2. Software Company B")
        print("3. Product Company C")
        print("4. Service Company D")
        print("5. My Applications")
        print("6. Back")

        choice=int(input("enter your choice:"))
        if choice==6:
            break
        elif choice in [1,2,3,4]:
            company=companies[choice] 
            print()
            print("Company:",company["name"])
            print("Role:",company["role"])
            print("Package:",company["package"])
            print("Mininum CGPA:",company["cgpa"])
            print("Backlogs:",company["backlogs"])
            print("Attendance:",company["attendance"],"%")
            print()
            print("1.Check Eligibility")
            print("2.Apply")
            print("3.Back")

            act=int(input("Enter your choice:"))
            if act==1 or act==2:
                cgpa=float(input("enter your CGPA:"))
                backlogs=int(input("Backlogs:"))
                attendance=float(input("Attendance:"))
                reasons=[]

                if cgpa<company["cgpa"]:
                    reasons.append("CGPA is below the required CGPA")
                if backlogs>company["backlogs"]:
                    reasons.append("Backlogs are above the allowed limit")  
                if attendance<company["attendance"]:
                    reasons.append("Attendance is below the required percentage.")
                if len(reasons)==0:
                    print()
                    print("                    !!!YOU ARE ELIGIBLE!!!                ")
                    if act==2:
                        if company["name"] not in applications:
                            applications.append(company["name"])
                            student["applications"]=applications
                            add_activity(student,"Applied for placement")
                            print("Application submitted successfully.")
                        else:
                            print("you already applied to this company.")
                else:
                    print()
                    print("YOU ARE NOT ELIGIBLE.")
                    print("Reasons:")
                    for i in reasons:
                        print("-",i)
            else:
                print("Invalid choice.")            
        elif choice==5:
            print()
            print("MY APPLICATIONS")
            if len(applications)==0:
                print("No applications submitted.")
            else:
                for i in applications:
                    print(i)
        else:
            print("Invalid entry try again")                                                                 

def complaint_feedback(student):
    if "complaints" not in student:
        student["complaints"]=[]
    complaints=student["complaints"]
    categories={
        1: "Academics",
        2: "Hostel",
        3: "Transport",
        4: "Library",
        5: "Infrastructure",
        6: "Canteen",
        7: "Other",
        8:"Back"
    }
    while True:
        print("="*60)
        print("                 📊  COMPLAINT / FEEDBACK SYSTEM 📊              ")
        print("="*60)  
        for i,j in categories.items():
            print(i,".",j) 
        choice=int(input("enter your choice:"))
        if choice==8:
            break
        if choice not in categories:
            print("Invalid choice try again")
            continue
        complaint=input("Enter Complaints:")
        complain_id="CMP"+str(143+len(complaints))
        details={
            "id":complain_id,
            "category":categories[choice],
            "complaint":complaint,
            "status":"SUBMITTED"
        }   
        complaints.append(details)
        add_activity(student,"Submitted"+categories[choice]+"complaint")
        print()
        print("Complaint Submitted") 
        print("Complaint ID:",complain_id) 
        print("Status:",details["status"])

def add_activity(student,activity):
    if "activity_history" not in student:
        student["activity_history"]=[]
    student["activity_history"].append(activity)
def student_activity_history(student):
    print("="*60)
    print("                 📊 ACTIVITY HISTORY 📊              ")
    print("="*60)  
    if "activity_history" not in student or len(student["activity_history"])==0:
        print("No activity history found.")
        return
    for i,activity in enumerate(student["activity_history"],1):
        print(i,".",activity)  
    

def college_overview():
    print("="*60)
    print("                 📊 COLLEGE OVERVIEW 📊              ")
    print("="*60)
    print()
    print("Total Students : 1250 ")
    print("Total Faculty : 85")
    print("Departments : 8 ")
    print("Active Clubs : 12 ")
    print("Events This Year : 24")
    print("Placement Eligible : 842")
    print("Students Placed : 638 ")
    print("Avg Attendance : 87.4% ")
    print("Fee Collection : 4.8 Cr ")
    print("Pending Complaints : 18")
    
def calculate_attendance():
    att_data = {
        "python": [42, 45],
        "java": [38, 45],
        "dsa": [35, 45],
        "dbms": [40, 45]
    }

    total_present = 0
    total_classes = 0

    for subject in att_data:
        total_present += att_data[subject][0]
        total_classes += att_data[subject][1]

    percentage = (total_present / total_classes) * 100

    return round(percentage, 2)

def student_summary(student):
        print("="*60)
        print("                 📊 STUDENT SUMMARY 📊              ")
        print("="*60)  
        print("Student:",student["name"])
        print("Roll Number:",student["roll_number"])
        print("Department:",student["dep"])
        print("Branch:",student["branch"])
        print("Email:",student["email"])
        print("Mobile",student["phone_no"])
        print("Year",student["year"])
        print("CGPA:", student.get("cgpa", "Not available"))
        print()
        print("----------ACADAMIC DETAILS---------")

        subjects={
            "Python":[18,16,9,72],
            "Java":[17,15,8,68],
            "DataStructure":[18,16,9,72],
            "DBMS":[16,17,9,70],
            "CN":[15,16,8,65]
        
        }
        total_marks=0
        total_max_marks=0

        for i in subjects:
            marks=subjects[i]
            total=sum(marks)
            total_marks+=total
            total_max_marks+=150
        acad_per=(total_marks/total_max_marks)*100

        print("Subjects:", len(subjects))
        print("Acadamic percentage:",acad_per,"%")
        print()
        print("------------ATTENDANCE DETAILS------------")
        att_per=calculate_attendance()
        print("Overall Attendance:",att_per,"%")
        if att_per>=75:
            print("Attendance Status:Eligible")
        else:
            print("Attendance Status:Not Eligible")
        print()

        print("-------------FEE DETAILS-----------")        

        fees={
            "tution_fee":54000,
            "transport_fee":20000,
            "exam-fee":2000,
            "library_fee":16000
        }
        total_fee=sum(fees.values())
        paid_fee=student.get("paid_fee",50000)
        pending_fee=total_fee-paid_fee
        print("Total Fee:",total_fee)
        print("Paid Fee:",paid_fee)
        print("Pending Fee:",pending_fee)
        complaints = student.get("complaints", [])
        print("Complaints:", len(complaints))
        if student.get("placement_eligible", False):
            print("Placement: ELIGIBLE")
        else:
            print("Placement: NOT ELIGIBLE")

        print("=" * 60)            
               
def stu_dashboard(student):
    while True:
        print("="*60)
        print("                 📊 STUDENT DASHBOARD 📊              ")
        print("="*60)
        print()
        print("👤 1. My Profile")
        print("📚 2. Academic Performance")
        print("📅 3. Attendance")
        print("📊 4. Attendance Shortage Calculator")
        print("📝 5. Internal Assessments")
        print("💰 6. Fee Status")
        print("🎉 7. Events & Clubs ")
        print("🎉 8. club management")
        print("🔔 9. Notifications")
        print("💼 10. Placements")
        print("📢 11. Complaints")
        print("📜 12. My Activity ")
        print("⭐ 13. My Overall Summary  ")
        print("🚪 14. Logout")
        print("="*60)
        dashboard_choice = int(input("👉 Enter your choice: "))
        if dashboard_choice==1:
           my_profile(student)
        elif dashboard_choice==2:
            academic_performance(student) 
        elif dashboard_choice==3:
            attendance()  
        elif dashboard_choice==4:
            att_shortage(student)  
        elif dashboard_choice==5:
            internal_assessment(student) 
        elif dashboard_choice==6:
            fee_management(student) 
        elif dashboard_choice==7:
            events_clubs(student) 
        elif dashboard_choice==8:
            club_management(student) 
        elif dashboard_choice==9:
            notification(student)  
        elif dashboard_choice==10:
            placement_portal(student)
        elif dashboard_choice==11:
            complaint_feedback(student)
        elif dashboard_choice==12:
            student_activity_history(student)
        elif dashboard_choice==13:
            student_summary(student)                                      
        elif dashboard_choice==14:
            print("Logged out Successfully.")
            break
        else:
            print("This dashboard option is coming soon.")        
        print()
def sorting_filtering():
    print("="*60)
    print("                       SORTING & FILTERING               ")
    print("="*60)   
    print("1. Students by CGPA")
    print("2. Students by Attendance")
    print("3. Students by Department")
    print("4. Students by Year")
    print("5. Companies by Package")
    print("6. Events by Available Seats")
    print("7. Applications by Status")
    print("8. Complaints by Category")
    print("9. Students Eligible for a Company")
    print("10. Back")

    choice=int(input("enter your choice:"))

    if choice==1:
        cgpa=[]
        for i in students:
            cgpa.append(i.get("cgpa",0))
        cgpa.sort(reverse=True)

        for i in cgpa:
            for j in students:
                if j.get("cgpa",0)==i:
                    print(j["name"],j.get("cgpa",0))

    elif choice==2:
        attendance=[]
        for i in students:
            attendance.append(i.get("attendance",0))
        attendance.sort()#lowest attendence
        for i in attendance:
            for j in students:
                if j.get("attendance",0)==i:
                    print(j["name"],j.get("attendance",0),"%")    
    elif choice==3:
        dept=input("enter your departement:")
        deptment=[]
        for i in students:
            if i["dep"].lower()==dept.lower():
                deptment.append(i)
        for i in deptment:
            print(i["name"],i["dep"])
    elif choice==4:
        year=int(input("enter your year of studing:"))
        year_list=[]
        for i in students:
            if i["year"]==year:
                year_list.append(i)
        for i in year_list:
            print(i["name"],i["year"])         
    elif choice==5:
        package_list=[]
        for i in companies:
            package_list.append(i["package"])
        package_list.sort(reverse=True)
        for i in package_list:
            for j in companies:
                if j["package"]==i:
                    print(j["name"],j["package"],"LPA")

    elif choice==6:
        events={"Hackathon":30,"Technical_fest":40,"Cultural Fest":60,"Sports_Meet":75,"Workshop":25,"Seminar":60}
        sorted_events=list(events.items())
        def get_seats(item):
            return item[1]
        sorted_events.sort(key=get_seats,reverse=True)
        for i,j in sorted_events:
            print(i,j,"seats available")


    elif choice==7:
        print("Application sorting is available inside the Placement Portal")
        

    elif choice==8:
        print("Complaints filtering is avaible inside the student complaint menu.")    
    elif choice==9:
        company_name=input("Enter company name:")
        selected=None
        for i in companies:
            if i["name"].lower()==company_name.lower():
                selected=i
                break
        if selected==None:
            print("Company not Found")
        else:
            print("Eligible students:")
            found=False
            for i in students:
                if i.get("cgpa",0)>=selected["eligibility_cgpa"]:
                    print(i["name"],i["cgpa"])
                    found=True
            if found==False:
                print("No eligible student found")                
    elif choice==10:
        return 
    else:
        print("invalid entry,try again")   
def student_exists(rollnum,email,phone_no):
    for i in students:
        if i["roll_number"]==rollnum or i["email"]==email or i["phone_no"]==phone_no:
            return True
    return False
while True:
    print("="*60)
    print("                       🏫CAMPUS360🏫               ")
    print("                   🎓smart college portal🎓         ")
    print("="*60)
    print()
    print("🔐 1.Student Login")
    print("👨 2.Faculty Login")
    print("🛠️ 3.Admin Login")
    print("📝 4.New Student Registration")
    print("🌐 5.Explore College")
    print("📊 6.Sorting & Filtering")
    print("❓ 7.Help")
    print("🚪 8.Exit")
    print("="*60)
    choice=input("👉enter your choice from the above options:")
    if choice.isdigit():
        choice=int(choice)
    else:
        print("Invalid input.Please enter a valid option.")
        continue    
    if choice==1:
        student_login()      
    elif choice==2:
        faculty_login()
    elif choice==3:
        admin_login() 
    elif choice==4:
        registration()
    elif choice==5:
        print("you selected Explore College") 
        college_overview()
    elif choice==6:
        sorting_filtering()    
    elif choice==7:
        print("how can we help you?")
        print("if you want any help please contact this number 91+9897969594")  
    elif choice==8:
        print("Thank you for using Campus 360")
        print("Goodbye! 👋") 
        break    
    else:
        print("❌ Invalid choice. Please enter 1 to 8.")  
        continue                    
    print()
