admitted = []
not_admitted = []


def check_admission(name, department, jamb_score, credits, passed_interview):
    department = department.lower()
    admitted_status = False

print("\nEnter candidate details:")
name = input("Name:")
department = input("Department (Computer Science/Mass Communication):")
jamb_score = int(input("JAMB Score: "))
credits= int(input("Number of Credits"))
Interview_input = input("Did the candidate pass the interview? (yes/no):"). strip().lower()
passed_interview = Interview_input == 'yes'

check_admission(name, department, jamb_score, credits, passed_interview)

cont = input("\nAdd another candidate? (yes/no):").strip().lower()
if cont != 'yes':

if department == "computer science":
   if jamb_score >= 250 and credits >= 5 and passed_interview:
      admitted_status = True
elif department == "mass communication":
 if jamb_score >= 230 and credits >= 5 and passed_interview:
            admitted_status = True
else:
    print(f"Invalid department: {department}")
    return

candidate_info = {
    "name": name,
    "department": department.title(),
    "jamb_score": jamb_score,
    "credits": credits,
    "passed interview": passed_interview
}

if admitted_status:
    admitted.append(candidate_info)
    print(f"{name} has been ADMITTED into {department.title()}")
else:
    not_admitted.append(candidate_info)
    print(f"{name} has been ADMITTED into {department.title()}")

print("\nAdmitted Candidates:")
for candidate in admitted:
    print(candidate)

print("\nNot Admitted Candidates:")
for candidate in not_admitted:
    print(candidate)
