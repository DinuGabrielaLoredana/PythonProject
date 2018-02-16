import re
import numpy as np
import pprint
#class for creating, printing and implementing operation with matrices
class Matrix:
    option =0
    i1=0
    j1=0
    k1=0
    matrice1=[]
#class constructor. creates a matrix and finds its dimension
    def __init__(self, option):
        self.matrice1 = []

        self.option = option
        if option==1:
            f = open('matrice1', 'r')
        else:
            f = open('matrice2', 'r')
        temp1 = []
        temp2 = []
        for s in f.readlines():

            s = s.strip()
            s = s
            if s == '':
                temp2 = temp2
                self.matrice1.append(temp2)
                temp2 = []

            else:

                temp1 = re.split('\s+', s)
                temp2.append(temp1)
        self.i1 = len(temp2)
        if len(temp2) > 0:
            self.matrice1.append(temp2)

        f.close()
        self.k1 = len(self.matrice1)
        self.j1 = len(temp1)
        for iterator1 in range(0, self.i1):
            for iterator2 in range(0, self.j1):
                for iterator3 in range(0, self.k1):
                    self.matrice1[iterator3][iterator1][iterator2] = float(self.matrice1[iterator3][iterator1][iterator2])

    def getMatrix(self):
        return self.matrice1

    def getNrOfRows(self):
        return self.i1

    def getNrOfCollums(self):
        return self.j1
    def getNrOfFaces(self):
        return self.k1

    #Function writeMatrix(option)calls the readMatrix function and uses the pprint module in order to list a tridimensional matrix in a friendly-readable way.

    def writeMatrix(self):

        pprint.pprint(self.matrice1)





    """The printDimensionsMatrix prints the dimensions of the matrix."""
    def printDimensionsMatrix(self):

                print ("i = %s" % self.i1)
                print ("j = %s" % self.j1)
                print ("k = %s" % self.k1)



    """""""""Function addMatrices() tests if the 2 matrices have the same dimensions and
    if so, it uses the numpy module to add the 2 matrices(one of the sent as parameter) and the
    pprint module in order to print the resulting matrix"""

    def addMatrices(self , matrice2):
        q = []
        if self.i1 != matrice2.getNrOfRows() or self.j1 != matrice2.getNrOfCollums() or self.k1 != matrice2.getNrOfFaces():
            print "Nu se pot scadea pentru ca au dimensiuni diferite"
        else:
            self.matrice2 = matrice2.getMatrix()
        q = np.add(self.matrice1, self.matrice2)
        pprint.pprint(q)

    """""""""Function returnByIndex(option)reads 3 integers and prints the element found
    at the position corresponding to the 3 values read or writes a message if at least one of the indexes is out of range"""
    def returnByIndex(self, option):

        i1 = input("i=")
        j1 = input("j=")
        k1 = input("k=")

        if i1>self.i1-1 or j1>self.j1-1 or k1>self.k1-1:
             print ("index depasit")
        else:
             print self.matrice1[k1][i1][j1]


    """""""""Function createNullMatrix() reads 3 integers and uses the numpy module to
    create and print a matrix in which all elements are 0."""
    def createNullMatrix(self):
        i1 = input("i=")
        j1 = input("j=")
        k1 = input("k=")

        null = np.zeros((k1, i1, j1))
        pprint.pprint(null)


    def reshape(self):
        i1 = input("i=")
        j1 = input("j=")
        k1 = input("k=")

        if i1 * j1 * k1 == self.i1 * self.j1 * self.k1:
            self.matrice1 = np.reshape(self.matrice1, (k1, i1, j1))
            pprint.pprint(self.matrice1)
        else:
            print("noua dimensiune nu este in conformitate cu numarul de elemente actuale")

    """""""""Function subtractMatrices() tests if the 2 matrices have the same dimensions and
    if so, it uses the numpy module to subtract the 2 matrices(one of the sent as parameter) and the
    pprint module in order to print the resulting matrix"""

    def subtractiMatrices(self, matrice2):
        q = []
        self.matrice2 = matrice2.getMatrix()
        if self.i1 != matrice2.getNrOfRows() or self.j1 != matrice2.getNrOfCollums() or self.k1 != matrice2.getNrOfFaces():
            print "Nu se pot scadea pentru ca au dimensiuni diferite"
        else:
            q = np.subtract(self.matrice1, self.matrice2)
        pprint.pprint(q)



def main():
    matrice1 = Matrix(1)
    matrice2 = Matrix(2)
    print(
            "1.Afisati prima matrice\n2.Afisati a doua matrice\n3.Adunati cele doua matrici si "
            "afisati rezultatul\n4.Accesati un element din prima matrice prin indexi si afisati-l\n5.Accesati un element din a doua matrice prin indexi si afisati-l\n6."
        "Redinensionati prima matrice\n7.Redimensionati a doua matrice\n8.Creati o matrice nula de dimensiuni"
        " date\n9.Aflati dimensiunea primei matrici\n10Aflati dimensiunea celei de a doua matrice\n11.Scadeti cele doua matricisi afisati rezultatul\n12.Iesiti")
    option = input("optiunea dumneavoastra este: ")


    while option >0 :
        if option == 1:
            matrice1.writeMatrix()
        else:
                    if option==2:
                         matrice2.writeMatrix()
                    else:
                     if option==3:
                         matrice1.addMatrices(matrice2)
                     else:
                        if option==4:
                         matrice1.returnByIndex(1)
                        else:
                            if option==5:
                                 matrice2.returnByIndex(2)
                            else:
                                if option==6:
                                 matrice1.reshape()
                                else:
                                    if option==7:
                                            matrice2.reshape()
                                    else:
                                        if option==8:
                                          matrice1.createNullMatrix()
                                        else:
                                            if option==9:
                                                matrice1.printDimensionsMatrix()
                                            else:
                                                if option==10:
                                                    matrice2.printDimensionsMatrix()
                                                else:
                                                    if option==11:
                                                         matrice1.subtractiMatrices(matrice2)
                                                    else:
                                                        if option==12:
                                                             exit()
        print(
                "1.Afisati prima matrice\n2.Afisati a doua matrice\n3.Adunati cele doua matrici si "
                "afisati rezultatul\n4.Accesati un element din prima matrice prin indexi si afisati-l\n5.Accesati un element din a doua matrice prin indexi si afisati-l\n6."
                "Redinensionati prima matrice\n7.Redimensionati a doua matrice\n8.Creati o matrice nula de dimensiuni"
                " date\n9.Aflati dimensiunea primei matrici\n10Aflati dimensiunea celei de a doua matrice\n11.Scadeti cele doua matricisi afisati rezultatul\n12.Iesiti")
        option = input("optiunea dumneavoastra este: ")


main()
