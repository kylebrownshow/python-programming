full_regtime = 50
full_overtime = 60
part_regtime = 65
part_overtime = 70
contract = (120-(120*.25))

fulltime_threshold = 40
parttime_threshold = 20

worker_type = 'contract'
hours_worked = 55

weekly_wage = 0

if worker_type == 'full_time' and hours_worked < 40:
    weekly_wage = (full_regtime * hours_worked)
elif worker_type == 'full_time' and hours_worked > 40:
    weekly_wage = ((full_regtime * 40) + (full_overtime * (hours_worked - 40)))
elif worker_type == 'part_time' and hours_worked < 20:
    weekly_wage = (part_regtime * hours_worked)
elif worker_type == 'part_time' and hours_worked > 20:
    weekly_wage = ((part_regtime * 20) + (part_overtime * (hours_worked - 20)))
elif worker_type == 'contract':
    weekly_wage = (contract * hours_worked)

print (weekly_wage)