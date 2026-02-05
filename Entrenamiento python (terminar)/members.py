         # Fitness Membership Console

# 3. Persistence
  # 3.1 Members - Members.csv
    # Fields:
      # member_id
      # name
      # document
      # phone
      # email
      # plan (basic | premium | full)
      # start_date
      # end_date
      # state (active | inactive)

import csv 

def load_members():
    members = []
    with open('members.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            members.append(row)
    return members


load_members()