import random

a = '''@media all and (min-width: %spx) and (max-width: %spx) {
    #%s {
        background-color: black;
    }
}
@media all and (min-width: 0px) and (max-width: %spx) {
    #%s {
        position: relative;
        left: -10101px;
    }
}
@media all and (min-width: %spx) {
    #%s {
        position: relative;
        left: -10101px;
    }
}
'''

for i in range(95):
    mmin = random.randint(400, 2000)
    mmax = random.randint(mmin, 2000)
    with open('styles.css', 'a') as f:
        f.write(a % (mmin, mmax, "a%s" % (i+1), mmin - 1, "a%s" % (i + 1), mmax + 1, "a%s" % (i + 1))) 
