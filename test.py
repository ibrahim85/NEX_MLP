from time import sleep

for i in xrange(0, 10):
    print("\r{0}".format(i)),
    sleep(.5)

print("...DONE!")