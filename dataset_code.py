import pandas as pd

# Defining the data as a list of dictionaries
data = [
    {"Company Name": "TCS", "Required CGPA": 7.0, "Required Skills": "Java, SQL"},
    {"Company Name": "Google", "Required CGPA": 8.5, "Required Skills": "Python, Algorithms, Distributed Systems"},
    {"Company Name": "Infosys", "Required CGPA": 6.5, "Required Skills": "C++, Python, Basic Networking"},
    {"Company Name": "Amazon", "Required CGPA": 8.0, "Required Skills": "Java, Data Structures, AWS"},
    {"Company Name": "Tech Mahindra", "Required CGPA": 7.0, "Required Skills": "Technical Knowlegde, C++, Python"},
    {"Company Name": "Wipro", "Required CGPA": 7.0, "Required Skills": "Communication, Python, Data Analysis "},
    {"Company Name": "Accenture", "Required CGPA": 7.0, "Required Skills": "Communication, Cloud Computing, SQL"},
    {"Company Name": "HCL", "Required CGPA": 7.5, "Required Skills": "Java,Python,Cloud Computing"},
    {"Company Name": "Paytm", "Required CGPA": 7.0, "Required Skills": "Data Structure, Algorithms, System Design, Java/Python"},
    {"Company Name": "Deloitte", "Required CGPA": 7.5, "Required Skills": "Communication, Java/Python, Data Structures, SQL, OOPS"},
    {"Company Name": "Juspay", "Required CGPA": 7.0, "Required Skills": "Data Structures, Algorithms, Python/Java, SQL"},
    {"Company Name": "Cognizant", "Required CGPA": 7.0, "Required Skills": "OOPS, Data Structures, Algorithms, Java/C++, SQL"},
    {"Company Name": "IBM", "Required CGPA": 7.0, "Required Skills": "Communication, Python, Node.js, SDLC, Operating Systems, DBMS"},

]
   
# Creating the DataFrame
df = pd.DataFrame(data)

# Saving to CSV
df.to_csv('placement_data.csv', index=False)

print("File 'placement_data.csv' has been created successfully!")