import pandas
import Tkinter
import tkFileDialog



    # I used the pandas library reference in the Python for data analysis book to load and manipulate the data.
root = Tkinter.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename(parent=root)
    # Here i tried to implement a try catch but this did not work very well. My goal was to implement
    # during file load and exercises.
try:
    File = pandas.read_csv(filename, names= ["BuyingPrice","MaintenancePrice","Doors","Persons",
                                             "LugBoot","Safety","Acceptability"])
except:
    print "There was a problem loading the file"
    # I inserted acceptable values to compare to data loaded to program.
AcceptableBuyingPrice =['vhigh','high','med','low']
AcceptableMaintenancePrice =['vhigh','high','med', 'low']
AcceptableDoors =['2','3','4','5more']
AcceptablePersons =['2','4','more']
AcceptableLugBoot =['small','med','big']
AcceptableSafety =['low','med','high']
AcceptableAcceptability =['acc','good','unacc','vgood']
    #I will check each column input vs acceptable values and display erroneous values given by file.
if File["BuyingPrice"].isin(AcceptableBuyingPrice).all():
    print "BuyingPrice data integrity ok"

else:
    print "These values are not valid for BuyingPrice"
    print File[~File.BuyingPrice.isin(AcceptableBuyingPrice)]

if File["MaintenancePrice"].isin(AcceptableMaintenancePrice).all():
    print "MaintenancePrice data integrity ok"
else:
    print "These values are not valid for MaintenancePrice"
    print File[~File.MaintenancePrice.isin(AcceptableMaintenancePrice)]

if File["Doors"].isin(AcceptableDoors).all():
    print "Doors data integrity ok"

else:
    print "These values are not valid for Doors"
    print File[~File.Doors.isin(AcceptableDoors)]

if File["Persons"].isin(AcceptablePersons).all():
    print "Persons data integrity ok"

else:
    print "These values are not valid for Persons"
    print File[~File.Persons.isin(AcceptablePersons)]

if File["LugBoot"].isin(AcceptableLugBoot).all():
    print "LugBoot data integrity ok"

else:
    print "These values are not valid for LugBoot"
    print File[~File.LugBoot.isin(AcceptableLugBoot)]

if File["Safety"].isin(AcceptableSafety).all():
    print "Safety data integrity ok"

else:
    print "These values are not valid for Safety"
    print File[~File.Safety.isin(AcceptableSafety)]

if File["Acceptability"].isin(AcceptableAcceptability).all():
    print "Acceptability data integrity ok"

else:
    print "These values are not valid for Acceptability"
    print File[~File.Acceptability.isin(AcceptableAcceptability)]
    # I start answering homework examples.
#2a Print to the console the top 10 rows of the data sorted by 'safety' in descending order

SafetyList = File.sort_values(File.columns[5], ascending=False).head(n=10)

print "The answer to question 2a is below--------------------------------------------------------------------"
print SafetyList

#2b Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order

MaintenanceList = File.sort_values(File.columns[5], ascending=True).tail(n=15)

print "The answer to question 2b is below--------------------------------------------------------------------"
print MaintenanceList

"""
2c
Print to the console all rows that are high or vhigh in fields buying, maint, and safety, sorted by doors in
ascending order using regular expression
"""
print "Answer to question 2c---------------------------------------------------------------------------------"
#http://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe
#http://stackoverflow.com/questions/25292838/applying-regex-to-a-pandas-dataframe

Question2c = File[File[['BuyingPrice', 'MaintenancePrice', 'Safety']].apply(lambda x: x.str.contains
('high|vhigh', regex=True)).any(axis=1)].sort_values('Doors', ascending=True)

#print Question2c['BuyingPrice','MaintenancePrice','Safety']

print Question2c[['BuyingPrice', 'MaintenancePrice','Doors', 'Safety']]

# question 2d
"""
save to a file all rows (in any order) that are: 'buying' Vhigh, maint med, doors 4 and persons 4 or more
"""
OutFile = File[(File['BuyingPrice'] == "vhigh") & (File['MaintenancePrice'] == "med") & (File['Doors'] == "4") &
               ((File['Persons'] == "more") | (File['Persons'] == "4"))]

print "2d---------------------------------------------------------------------------------------------------"
print OutFile

OutFile.to_csv("OutPut2d.csv")

