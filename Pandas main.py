import pandas as pd

students = {
    "name": ["Ahmed", "Hamza","Ali"],
    "Age": [20,21,19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(students)

print(df)
