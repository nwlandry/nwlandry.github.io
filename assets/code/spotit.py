
import numpy as np
import webweb
import matplotlib.pyplot as plt

card1 = ["car","frog","giraffe","monkey","turtle","zebra"]
card2 = ["chameleon","frog","owl","paw print","snail","tiger"]
card3 = ["fish","flamingo","lion","sun","tiger","turtle"]
card4 = ["banana","butterfly","giraffe","lion","owl","palm tree"]
card5 = ["compass","palm tree","rhino","snail","toucan","turtle"]
card6 = ["boot","compass","hat","lion","paw print","zebra"]
card7 = ["banana","compass","elephant","ladybug","monkey","tiger"]
card8 = ["alligator","boot","butterfly","chameleon","ladybug","turtle"]
card9 = ["butterfly","fish","flower","monkey","paw print","rhino"]
card10 = ["alligator","flower","kangaroo","palm tree","tiger","zebra"]
card11 = ["fish","giraffe","hat","kangaroo","ladybug","snail"]
card12 = ["boot","camera","elephant","fish","frog","palm tree"]
card13 = ["alligator","camera","fox","lion","monkey","snail"]
card14 = ["binoculars","chameleon","hat","monkey","palm tree","sun"]
card15 = ["binoculars","flower","frog","ladybug","lion","toucan"]
card16 = ["alligator","binoculars","car","compass","fish","owl"]
card17 = ["alligator","elephant","giraffe","paw print","sun","toucan"]
card18 = ["binoculars","butterfly","elephant","flamingo","snail","zebra"]
card19 = ["binoculars","boot","fox","giraffe","rhino","tiger"]
card20 = ["butterfly","camera","car","hat","tiger","toucan"]

listOfCards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,
               card11,card12,card13,card14,card15,card16,card17,card18,card19,
               card20]

listOfNames = sorted(set([item for sublist in listOfCards for item in sublist]))
print(listOfNames)

n = len(listOfNames)
A = np.zeros([n,n])

displayNames = dict()
names = dict()
for i in range(n):
    names[i] = {"name":listOfNames[i]}
displayNames["nodes"] = names

for name in listOfNames:
    i = listOfNames.index(name)
    for card in listOfCards:
        if name in set(card):

            for character in set(card).difference({name}):
                j = listOfNames.index(character)
                A[i,j] = A[i,j] + 1
print(A)
plt.figure()
plt.pcolor(A)
plt.colorbar()
plt.show()

web = webweb.Web(A, display=displayNames)
web.display.charge = 1000
web.display.linkLength = 200
web.display.colorBy = 'degree'
web.display.sizeBy = 'degree'
web.display.showNodeNames = True
web.display.attachWebwebToElementWithId = 'spotit'
web.show()
