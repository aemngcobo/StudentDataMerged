
import pandas as pd 
import openpyxl as xl

data1 = pd.read_excel(r'C:\Users\Anele Ngcobo\Desktop\Basic2AdvancedPythonII\CampaignData\output2.xlsx',sheet_name="X3")

dict1=({'ID':[1000,2222,4433,222],'StudentName':["Amy","Julie","Kia","Jackson"],'Open':[3,2,33,23],'Gender':["Female","Female","NA","Male"]})

dict2=({'ID':[1000,222,443,100],'Qualification':["Grad","Postgrad","Job","Grad"],'Open':[3,112,113,113],'Result':["Pass","Reattempt","Waiting","Pass"]})

df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)

print(df1,df2)

df3=pd.merge(df1,df2,how="inner",on="ID")
print(df3)