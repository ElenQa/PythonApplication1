
class Marks():
    def ReadFile(self, filename):
        Students = dict()
        Math = dict()
        Language = dict()
        f = open(filename, "r")
        lines = []
        final = []
        for line in f:
            lines.append(line)
            subject = lines[0]
            for i in lines[1:]:
                final.append(i)
            str1 = ''.join(final)
        Students = dict((str(x.strip()), int(y.strip())) for x, y in (i.split('-') for i in str1.split('\n')))
        if subject=="Math\n":
            Math = dict(Students)
            return Math        
        elif subject == "Language\n":
            Language = dict(Students)
            return Language
    
    def ReadMaks_and_CountAvarage(self,filename1,filename2):
        Total = {}
        Math = self.ReadFile(filename1)
        Language = self.ReadFile(filename2)
        result = open('C:/Users/OChernovolyk/Desktop/Teachers_Reports/Teachers_Reports/bin/Debug/final.txt', "w")
        result.write("Avarage" + '\n')

        for d in Math, Language:
            for k, v in d.items():
                if Total.get(k) is None:
                    Total[k] = []
                if v not in Total.get(k):
                    Total[k].append(v)
        for d in Total.keys():
            l = len(Total[d])
            if l < 2:
                Av = (Total[d][0] + 0)/2
            else:
                Av = (Total[d][0] + Total [d][1])/2
            result.write(d +" "+ "-" +" "+ str(Av)+ '\n')
        result.close()
s = Marks( )
s.ReadMaks_and_CountAvarage('C:/Users/OChernovolyk/Desktop/Teachers_Reports/Teachers_Reports/bin/Debug/subject1.txt', 'C:/Users/OChernovolyk/Desktop/Teachers_Reports/Teachers_Reports/bin/Debug/subject2.txt')



        
