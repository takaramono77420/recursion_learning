def fireEmployees(employees,unemployed):
    # 関数を完成させてください

    employeeRetentionList = []

    for employee in employees:
        
        if not employee in unemployed:

            employeeRetentionList.append(employee)
    
    return employeeRetentionList