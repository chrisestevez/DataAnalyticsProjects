import scipy.misc as misc
from PIL import Image
import mahotas as mh

circlesimg = misc.imread('./images.for.lesson.8/circles.png')
objectsimg = misc.imread('./images.for.lesson.8/objects.png')
peppersimg = misc.imread('./images.for.lesson.8/peppers.png')

#img = Image.open('./images.for.lesson.8/circles.png')
#img.show()


def circles():
    thres = mh.otsu(circlesimg)
    circlesTress = (circlesimg > thres)
    circlesGau = mh.gaussian_filter(circlesTress, 25)
    circlesRegmx = mh.regmax(circlesGau)
    labels, nrObj = mh.label(circlesRegmx)
    nh, TotalCircles = mh.label(circlesRegmx)
    print "Total Circles"
    print TotalCircles

    centers = mh.center_of_mass(circlesimg, labels)[1:]
    print "The centers of mass for circle are located"
    print centers

#circles()


def objects():
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

objects()


def peppers():

    thres = mh.otsu(peppersimg)
    peppersTress = (peppersimg > thres)
    peppersGau = mh.gaussian_filter(peppersTress, 20)
    peppersRegmx = mh.regmax(peppersGau)
    labels, nrObj = mh.label(peppersRegmx)
    nh, TotalObjects = mh.label(peppersRegmx)
    print "Total peppers"
    print TotalObjects

    centers = mh.center_of_mass(peppersimg, labels)[1:]
    print "The centers of mass for peppers are located"
    print centers


#peppers()
