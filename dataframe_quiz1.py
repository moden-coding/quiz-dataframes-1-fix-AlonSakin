import pandas as pd

def get_department(df):
    return df["Department"]
       
def get_second_record(df):
    return df.iloc[1]
    
def get_info_grace(df):
    return df.loc["Grace"]

def get_experience_location(df):
    return df[["Experience", "Location"]]
    
def get_department_elena_aiden(df):   
    return df.loc[["Elena", "Aiden"]]["Department"]

def get_experience_salary_third_to_end(df):
    return df[["Experience", "Monthly Salary"]].iloc[2:len(df)]

def main():
    df = pd.read_csv("data.csv", index_col= 0)

    print("Department Column:\n", get_department(df))
    print("\nSecond Record:\n", get_second_record(df))
    print("\nGrace's Info:\n", get_info_grace(df))
    print("\nExperience and Location Columns:\n", get_experience_location(df))
    print("\nDepartment of Elena and Aiden:\n", get_department_elena_aiden(df))
    print("\nExperience and Monthly Salary of Third to End:\n", get_experience_salary_third_to_end(df))


if __name__ == "__main__":
        main()
