# colleges contain colleges - students allotted
colleges = {
    'college1': [], 'college2': [],
    'college3': [], 'college4': [], 'college5': [],
}

# students contain students(their college preferences and allotment status) sorded on their "rank"
students = {
    'stud1': {'prefs': ['college3', 'college1', 'college5'], 'status': False},
    'stud2': {'prefs': ['college4', 'college3', 'college1'], 'status': False},
    'stud3': {'prefs': ['college1', 'college5', 'college2'], 'status': False},
    'stud4': {'prefs': ['college3', 'college1', 'college4'], 'status': False},
    'stud5': {'prefs': ['college4', 'college3', 'college5'], 'status': False},
    'stud6': {'prefs': ['college4', 'college2', 'college3'], 'status': False},
    'stud7': {'prefs': ['college4', 'college2', 'college5'], 'status': False},
    'stud8': {'prefs': ['college5', 'college4', 'college2'], 'status': False},
    'stud9': {'prefs': ['college1', 'college5', 'college2'], 'status': False},
    'stud10': {'prefs': ['college2', 'college5', 'college4'], 'status': False},
    'stud11': {'prefs': ['college4', 'college5', 'college3'], 'status': False},
    'stud12': {'prefs': ['college3', 'college5', 'college2'], 'status': False},
    'stud13': {'prefs': ['college3', 'college2', 'college1'], 'status': False},
    'stud14': {'prefs': ['college4', 'college2', 'college1'], 'status': False},
    'stud15': {'prefs': ['college5', 'college4', 'college2'], 'status': False},
}


def allo_sys(students, colleges):
    for student in students:
        if students[student]['status']:
            break
        else:
            for i in students[student]['prefs']:
                if students[student]['status']:
                    break
                elif len(colleges[i]) <= 2:
                        colleges[i].append(student)
                        students[student]['status'] = True
                        break    
                    
                    
    print(colleges)

allo_sys(students, colleges)