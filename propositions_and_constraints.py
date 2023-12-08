from nnf import Var
from lib204 import Encoding

# Define propositions
Auth1 = Var('Auth1')
Auth2 = Var('Auth2')
Auth3 = Var('Auth3')
Clear_face = Var('Clear_face')
Light = Var('Light')
Face_in_front = Var('Face_in_front')
One_person_frame = Var('One_person_frame')
Access_granted = Var('Access_granted')
Flag = Var('Flag')
Add_flag = Var('Add_flag')
Flag_highest = Var('Flag_highest')
Show_error = Var('Show_error')
Check_database = Var('Check_database')
Intoxicated = Var('Intoxicated')
Sleepy = Var('Sleepy')
New_face = Var('New_face')
New_face_adding = Var('New_face_adding')
Software_error = Var('Software_error')
Face_scanned = Var('Face_scanned')
Meltdown = Var('Meltdown')
Meltdown_initiated = Var('Meltdown_initiated')
Retry = Var('Retry')
Security_alert = Var('Security_alert')
Database1 = Var('Database1')
System_shut = Var('System_shut')
Spectacles = Var('Spectacles')
Hair_Colour = Var('Hair_Colour')
Skin_Color = Var('Skin_Color')
Mustache = Var('Mustache')
Beard = Var('Beard')
Eye_Color = Var('Eye_Color')
EmployeeID = Var('EmployeeID')
Initial_access = Var('Initial_access')

# Add constraints
# Authorization constraints
constraints_auth1 = (New_face & Auth1) >> New_face_adding
constraints_auth2 = (Meltdown & Auth1) >> Meltdown_initiated
constraints_auth3 = ~Meltdown_initiated >> Security_alert

# Scan constraints
constraints_scan = Clear_face & Light & Face_in_front & One_person_frame & Initial_access >> Face_scanned
constraints_error = (~(Clear_face & Light & Face_in_front & One_person_frame) & ~Flag_highest) >> (Add_flag & Show_error)
constraints_security_alert = (~(Clear_face & Light & Face_in_front & One_person_frame) & Flag_highest) >> (Show_error & Security_alert)

# Access check constraints
constraints_access_check = Spectacles & Hair_Colour & Skin_Color & Mustache & Beard & Eye_Color >> Check_database
constraints_access_granted = Face_scanned & ~Show_error & Check_database >> Access_granted
constraints_no_access_granted = Face_scanned & ~Show_error & Check_database >> ~Access_granted

# Inform security constraints
constraints_inform_security = Flag_highest >> (Security_alert & System_shut)

# Intoxication and Sleepiness constraints
constraints_intoxication_sleepy = (Intoxicated | Sleepy) >> (~Access_granted & Security_alert)

# Software error constraints
constraints_software_error = Face_scanned & Show_error & ~Check_database

# New face adding constraints
constraints_new_face_adding = New_face_adding & Check_database >> Show_error

# Add constraints to the encoding
E = Encoding()
E.add_constraint(constraints_auth1)
E.add_constraint(constraints_auth2)
E.add_constraint(constraints_auth3)
E.add_constraint(constraints_scan)
E.add_constraint(constraints_error)
E.add_constraint(constraints_security_alert)
E.add_constraint(constraints_access_check)
E.add_constraint(constraints_access_granted)
E.add_constraint(constraints_no_access_granted)
E.add_constraint(constraints_inform_security)
E.add_constraint(constraints_intoxication_sleepy)
E.add_constraint(constraints_software_error)
E.add_constraint(constraints_new_face_adding)

# Solve the encoding
print("Satisfiable:", E.is_satisfiable())
print("Model:", E.solve())
