name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")

education = []
work_experience = []
skills = []

def add_education():
    degree = input("Enter your degree: ")
    major = input("Enter your major: ")
    school = input("Enter the name of the school: ")
    education.append((degree, major, school))

def add_work_experience():
    job_title = input("Enter your job title: ")
    company = input("Enter the name of the company: ")
    job_description = input("Enter a brief description of your job duties: ")
    work_experience.append((job_title, company, job_description))

def add_skills():
    skill = input("Enter a skill you have: ")
    skills.append(skill)

add_education()
add_work_experience()
add_skills()

template = f'''
CV

Name: {name}
Age: {age}
Address: {address}
Phone: {phone}
Email: {email}

Education:
'''

for edu in education:
    template += f'  {edu[0]} in {edu[1]} from {edu[2]} \n'

template += '\nWork Experience:\n'
for work in work_experience:
    template += f'  {work[0]} at {work[1]}: {work[2]} \n'

template += '\nSkills:\n'
for skill in skills:
    template += f'  - {skill}\n'

print(template)
