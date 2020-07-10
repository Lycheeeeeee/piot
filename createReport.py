
from databaseConnection import MySQLConn
import json
class Report:
    mysqlconn = MySQLConn()
    mydb = mysqlconn.conn
    
    mycursor = mysqlconn.cursor
    def writeReport(self):
        dayList = "Select distinct records.date from records"
        self.mycursor.execute(dayList)
        alldayResult = self.mycursor.fetchall()
        badday = "Select records.date, group_concat(records.temperature) from records where records.comfortable is false group by records.date"
        self.mycursor.execute(badday)
        baddayResult = self.mycursor.fetchall()
        diction = self.goodNBad(alldayResult,baddayResult)
        print(diction["goodDay"])
        print(diction["badDay"])
        file = open('report.csv','w')
        file.write("Date, Status \n")
        file.close()
        for i in alldayResult:
            if i[0] in diction['badDay']:
                with open('config.json') as configFile:
                    data = json.load(configFile)
                index = diction['badDay'].index(i[0])
                file_object = open('report.csv', 'a')

                if int(baddayResult[index][1][0])<data['cold_max']:
                    diff = data['cold_max']-int(baddayResult[index][1][0])
                    file_object.write(i[0]+" BAD: "+str(diff)+ " C degree below the comfort temperature\n")
                    file_object.close()
                if int(baddayResult[index][1][0]) > data['hot_min']:
                    diff = int(baddayResult[index][1][0])-data['hot_min']
                    file_object.write(i[0]+" BAD: "+str(diff)+ "C degree above the comfort temperature\n")
                    file_object.close()

            if i[0] in diction['goodDay']:
                file_object = open('report.csv', 'a')
                file_object.write(i[0]+" OK \n")
                file_object.close()
           
    def goodNBad(self,allday, badday):
        d = dict()
        goodDay=[]
        listContentBadDayOnly=[]
        for i in badday:
            listContentBadDayOnly.append(i[0])
        for j in allday:
            if j[0] not in listContentBadDayOnly:
                goodDay.append(j[0])
        d['goodDay'] = goodDay
        d['badDay'] = listContentBadDayOnly
        return d

report = Report()
report.writeReport()