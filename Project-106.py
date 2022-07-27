import plotly.express as px
import csv
import numpy as np

def setup(dictdata, param1, param2):
    row1 = []
    row2 = []

    for row in dictdata:
        row1.append(float(row[param1]))
        row2.append(float(row[param2]))

    return {"x": row1, "y": row2}


with open("Student Marks.csv", newline="") as marks:
    marks_data = csv.DictReader(marks)
    s1 = setup(marks_data, "Marks In Percentage", "Days Present")
    marks_correlation = np.corrcoef(s1["x"], s1["y"])
    print(f"Correlation between Students Marks and Number Of Days Present = { marks_correlation[0, 1] }" )

with open("Student Marks.csv", newline="") as mark:
    mark_data = csv.DictReader(mark)     
    pic = px.scatter(mark_data, x="Marks In Percentage", y="Days Present")
    pic.show()

with open("cups of coffee.csv", newline="") as coffee:
    coffee_data = csv.DictReader(coffee)
    s2 = setup(coffee_data, "Coffee in ml", "sleep in hours")
    coffee_correlation = np.corrcoef(s2["x"], s2["y"])
    print(f"Correlation between Cups of Coffe and Number Of Hours Slept = { coffee_correlation[0, 1] }" )

with open("cups of coffee.csv", newline="") as coffe:
    coffe_data = csv.DictReader(coffe)
    plot_data2 = px.scatter(coffe_data, x = "Coffee in ml", y = "sleep in hours")
    plot_data2.show()