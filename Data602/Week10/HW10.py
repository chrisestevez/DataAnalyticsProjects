import pandas
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, misc
import mahotas as mh


CarsData = pandas.read_csv('Data/cars.data.csv', names=["BuyingPrice", "MaintenancePrice", "Doors", "Persons",
                                             "LugBoot", "Safety", "Acceptability"])

buying = CarsData.groupby('BuyingPrice').size().sort_values()
maint = CarsData.groupby('MaintenancePrice').size().sort_values()
safety = CarsData.groupby('Safety').size().sort_values()
doors = CarsData.groupby('Doors').size().sort_values()

plt.figure(1, tight_layout=True)
plt.subplot(221)
x1 = np.arange(len(buying))
plt.bar(x1, buying, align='center', color='b', alpha=0.5)
plt.xticks(x1, buying.index)
plt.ylabel('Frequency')
plt.title('Buying Price')

plt.subplot(222)
x2 = np.arange(len(maint))
plt.bar(x2, maint, align='center', color='b', alpha=0.5)
plt.xticks(x2, maint.index)
plt.ylabel('Frequency')
plt.title('Maintenance Price')

plt.subplot(223)
x3 = np.arange(len(safety))
plt.bar(x3, safety, align='center', color='b', alpha=.5)
plt.xticks(x3, safety.index)
plt.ylabel('Frequency')
plt.title('Safety')

plt.subplot(224)
x4 = np.arange(len(doors))
plt.bar(x4, doors, align='center', color='b', alpha=.5)
plt.xticks(x4, doors.index)
plt.ylabel('Frequency')
plt.title('Doors')

plt.show()

#-------------------------------------------------------------------------------------
# read data from folder
brain_body = pandas.read_csv('data/brainandbody.csv')
br = brain_body['brain']
bo = brain_body['body']

#regression
reg = stats.linregress(br, bo)

# get the min and the max points
x = [br.min(), br.max()]
y = [0, br.max()]

# Plotting

plt.title('Brain Weight vs. Body Weight')
plt.xlabel('Body Weight')
plt.ylabel('Brain Weight')
plt.plot(br, bo, 'o', alpha=0.5)
plt.plot(x, y, alpha=0.5)
plt.text(1000, 3000, r'y=0.97 Xbr + 91.00')

plt.show()
#------------------------------------------------------------------------------------

#I really missed the mark on the center points
objectsimg = misc.imread('data/objects.png')

thres = mh.otsu(objectsimg)
objectsTress = (objectsimg > thres)
objectsGau = mh.gaussian_filter(objectsTress, 48)
objectsRegmx = mh.regmax(objectsGau)
labels, nrObj = mh.label(objectsRegmx)
nh, TotalObjects = mh.label(objectsRegmx)
print "Total Objects"
print TotalObjects

centers = mh.center_of_mass(objectsimg, labels)[1:]


print "The centers of mass for objects are located"
print centers

xcenter = centers[:,0]
ycenter = centers[:,1]

implot = plt.imshow(objectsimg)
plt.plot(xcenter, ycenter, 'o')
plt.title("Centers of Mass in objects.png")
plt.xlim(0, 585)
plt.ylim(512, 0)
plt.grid(False)

plt.show()

#-------------------------------------------------------

#Loading data into pandas
Data = pandas.read_table('data/epa-http.txt', header=None, squeeze=True, sep='\s+', na_values="-",
                     names=['Host', 'Date', 'Request', 'HTTP_code', 'bytes'])


# I Replaced NAs with 0s
Data = Data.fillna(0)
#Formated date time field
Data['Date'] = pandas.to_datetime(Data['Date'], format='[%d:%H:%M:%S]')

Hours = pandas.DataFrame({'Hour': Data['Date'].dt.hour})

Busy_hour = Hours.groupby(by='Hour')['Hour'].count()

print Busy_hour

plt.plot(Busy_hour.index, Busy_hour, 'o-')
plt.title('Total Server Requests by Hour')
plt.xlabel('Hours')
plt.ylabel('Total Requests')
plt.xlim(0, 25)
plt.xticks(np.arange(-1, 25, 1))
plt.show()
