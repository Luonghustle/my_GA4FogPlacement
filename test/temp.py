def Uniformcrossover(self,f1,f2,offs):
        c1 = list()
        c2 = list()
        for i in range(0,self.system.serviceNumber):
            temp1 = []
            temp2 = []
            for j in range(self.system.fogNumber):
                if self.rndEVOL.random() < 0.5:
                    temp1.append(f1[i][j])
                    temp2.append(f2[i][j])
                else:
                    temp1.append(f2[i][j])
                    temp2.append(f1[i][j])
            c1.append(temp1)
            c2.append(temp2)

        self.placeReplicasInCloud(c1)
        self.placeReplicasInCloud(c2)

        offs.append(c1)
        offs.append(c2)

        return c1,c2