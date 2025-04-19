## Student Info Database using dictionaries!!
students = {   ## just to remember dictionaries dont use "=" instead use ":"
     "Prithvi" : {
         
        "Age" : 23,
        "Grade" : "A",
        "Subject" : "Python"
    },

    "Vamsi" : {

        "Age" : 23,
        "Grade" : "A",
        "Subject" : "Data structures"
    },
    
    "Rakshit" : {
        "Age" : 23,
        "Grade" : "A",
        "Subject" : "Anything"
    },

}

studentname = input("May i know the name of the student?")
if studentname in students:
    print("Here are the details of", studentname)
    print("age:", students[studentname]["Age"])
    print("grade:", students[studentname]["Grade"])
    print("subject", students[studentname]["Subject"])
else:
    print("Im sorry student not found!")




