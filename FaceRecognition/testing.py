from mor3 import Database
db=Database()
#db.drop_create()

db.employee_disable(int(1006))

#print("Id ----> "+str(db.employee_add("shah","bad work")))

db.attendance_remove(1028)

#print(db.employee_add("Mrs.  SONIGA","staff"))
#print(db.attendance_insert(1002))
#print(db.employee_status(12))
db.employee_disable(1013)
data=db.employee_fetch()
print(data["sno"])
print(data["id"])
print(data["name"])
print(data["position"])
print(data["in"])
print(data["out"])
print(data["status"])

