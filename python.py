import pandas as pd

# Data: Replace or extend this with your actual student data
data = {
    "Name": ["Amit", "Sara", "John"],
    "Math": [78, 92, 65],
    "Science": [88, 81, 72],
    "English": [90, 85, 70],
    "History": [76, 89, 68],
    "Computer": [95, 91, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks and percentage
df["Total"] = df[["Math", "Science", "English", "History", "Computer"]].sum(axis=1)
df["Percentage"] = (df["Total"] / 500) * 100

# Add performance feedback
def feedback(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 50:
        return "Average"
    else:
        return "Needs Improvement"

df["Feedback"] = df["Percentage"].apply(feedback)

# Print report card summary
for index, row in df.iterrows():
    print(f"Name: {row['Name']}")
    print(f"Math: {row['Math']}")
    print(f"Science: {row['Science']}")
    print(f"English: {row['English']}")
    print(f"History: {row['History']}")
    print(f"Computer: {row['Computer']}")
    print(f"Total: {row['Total']}")
    print(f"Percentage: {row['Percentage']:.2f}%")
    print(f"Feedback: {row['Feedback']}")
    print("------------------------")

# Save report cards as a new CSV file
df.to_csv("final_report_card.csv", index=False)