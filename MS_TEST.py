import pymssql
conn = pymssql.connect(server='192.168.6.94', user='reportuser', password='rE0rTu)S7!b^', database='msdb', as_dict=True)
cursor = conn.cursor()
cursor.execute('''SELECT  A.DB_NAME
        ,A.[BAK_SIZE(GB)]
        ,CONVERT(CHAR(20),A.BAK_START,20) as [Backup_StartDate]
        ,CONVERT(CHAR(20),A.BAK_FINISH,20) as [Backup_Finish_Date]
        ,A.TYPE as [Type], A.RECO_MODEL as [Reco_Model], A.PHY_DEVICE_NAME as [Phy_Device_Name]
FROM (
        select A.db_name, A.type, max(CONVERT(CHAR(20),A.BAK_START,20)) as [BAK_START]
        FROM msdb.dbo.PT_BAK_HIST A
        where A.ch_date = CONVERT(date,GETDATE())
        and A.TYPE IN ('D', 'L')
        group by A.db_name, A.type
       ) [B] INNER JOIN msdb.dbo.PT_BAK_HIST [A]
ON A.DB_NAME = B.DB_NAME
AND A.BAK_START = B.BAK_START
AND A.TYPE = B.TYPE
order by A.TYPE''')
row = cursor.fetchone()
while row:
    #print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]))
    print("DB_NAME = " + str(row["DB_NAME"]) + ", BAK_SIZE(GB) = " + str(row["BAK_SIZE(GB)"]) +
          ",Backup_StartDate = " + str(row["Backup_StartDate"]) + ",Backup_Finish_Date = " + str(row["Backup_Finish_Date"])
          + ",Type = " + str(row["Type"]) + ",Reco_Model = " + str(row["Reco_Model"]) + ",Phy_Device_Name = " + str(row["Phy_Device_Name"]))
    row = cursor.fetchone()
conn.close()

