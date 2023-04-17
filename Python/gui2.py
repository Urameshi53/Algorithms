# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:32:43 2022

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:15:35 2022

@author: User
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sqlite3
import sys

headers = ["Staff Name","Num of Children","Hours Worked","Gross Pay","Net Pay","Deductions"]
rows = [("Emmanuel Zigah",2,53,20,20,10),
        ("Derrick",4, 44, 20,20,32)]

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    
    def columnCount(self, parent):
        return len(headers)
    
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return headers[section]
    

class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer example')
        self.resize(500, 200)
        
        
        self.listFile = QListWidget()
        self.label = QLabel('Search')
        self.nameLabel = QLabel('Name')
        self.timeLabel = QLabel('Time')
        self.childrenLabel = QLabel('Number of Children')
        
        self.nameLine = QLineEdit()
        self.timeLine = QLineEdit()
        self.childLine = QLineEdit()
        self.searchLine = QLineEdit()
        
        self.searchBtn = QPushButton('Search')
        self.doneBtn = QPushButton('Done')
        self.tableBtn = QPushButton('Show table')
        
        layout = QGridLayout()
        
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.searchLine, 0,2)
        layout.addWidget(self.nameLabel, 1,0)
        layout.addWidget(self.nameLine, 1,2)
        layout.addWidget(self.timeLabel, 2,0)
        layout.addWidget(self.timeLine, 2, 2)
        layout.addWidget(self.childrenLabel, 3,0)
        layout.addWidget(self.childLine, 3, 2)
        layout.addWidget(self.searchBtn, 4, 0)
        layout.addWidget(self.doneBtn, 4, 1)
        layout.addWidget(self.tableBtn, 4, 2)
        
        self.searchBtn.clicked.connect(self.search)
        self.doneBtn.clicked.connect(self.storeData)
        self.tableBtn.clicked.connect(self.showTable)    
        self.setLayout(layout)
        
    def storeData(self):
        name = self.nameLine.text()
        hours = self.timeLine.text()
        numChildren = self.childLine.text()
        gp = int(hours)*0.5
        d = gp*0.27
        np =gp - d
        rows.append((name,numChildren,hours,gp,np,d))
        db.open()
        
        cursor.execute(f"""INSERT INTO project VALUES ('{name}','{numChildren}','{hours}','{gp}','{np}','{d}')""")
        connection.commit()    
        db.close()
        # mydb = db.connect()
        # cursor = mydb.cursor()
        
        # mydb.commit()
        print(rows)
        self.nameLine.setText("")
        self.timeLine.setText("")
        self.childLine.setText("")
        
    def showTable(self):
        '''view.resize(800,500)
        view.show()
        model = TableModel()
        view.setModel(model)'''
        view.resize(800,500)
        view.show()
        
        db.setDatabaseName("project.db")
        db.open()
        
        model = QSqlTableModel(None, db)
        model.setTable("project")
        model.select()
        
        view.setModel(model)
        
        
    def search(self):
        if(self.searchLine.text()):
            n = self.searchLine.text()
            data = cursor.execute(f"""SELECT Staff, Num, Hours FROM project WHERE Staff='{n}'""")
            # data = list(d)
            # print(data)
            if n == data[0]: 
                for i in d:
                    QMessageBox.information(self, "Search", f"Name: {data[0]}\nnumChildren: {data[1]}\nNet Pay: {data[2]}")
            else:
                    QMessageBox.information(self, "Search",n+" was not found")
                    
                
        # data = cursor.execute("""SELECT * FROM project""")
        # if(self.nameLine.text()):
        #     for i in data:
        #         for j in i:
        #             if j == self.nameLine.text():
        #                 d = i
        #                 QMessageBox.information(self, "Search", f"Name: {i[0]}\nnumChildren: {i[1]}\nNet Pay: {i[4]}")
        #                 '''
        #                 n = list(i)
        #                 n = [str(i) for i in n]
        #                 model = QStringListModel(n)
                        
        #                 view.setModel(model)
        #                 view.show()'''
        #                 return 
        #     else:
        #         QMessageBox.information(self, "Search",self.nameLine.text()+
        #             " was not found")
        #         return
    
    def edit(self):
        db.open()
        new = "Renaissance"
        name = "Rene"
        numChildren = 3
        hours = 63
        cursor.execute(f"""UPDATE project SET Staff='{new}' WHERE Staff='{name}'""")
        connection.commit()
        db.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    db = QSqlDatabase.addDatabase("QSQLITE")
    
    connection = sqlite3.connect("project.db")
    cursor = connection.cursor()
    
    # view = QListView()
    view = QTableView()
    
    sys.exit(app.exec_())


