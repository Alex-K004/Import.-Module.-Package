import datetime
from application.db.people import get_employes
from application.salary import calculate_salary

dt = datetime.datetime.today()

if __name__ == '__main__':
    calculate_salary(2,2)
    get_employes(3)
    print(dt)
