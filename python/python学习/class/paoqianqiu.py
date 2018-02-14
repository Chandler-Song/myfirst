from Projectile1 import *
def getInputs():#库名不能为数字
    a = eval(input("Enter  the  launch angle (in degrees):"))
    v = eval(input("Enter the initial velocity (in meters/sec):"))
    h = eval(input("Enter the initial height (in meters):"))
    t = eval(input("Enter the time interval: "))
    return a,v,h,t
def main():
    angle,vel,h0,time = getInputs()
    shot = Projectile(angle,vel,h0)
    while shot.getY() >= 0:
        shot.update(time)
    print("\nDistance traveled:{0:0.1f}meters.".format(shot.getX()))
main()