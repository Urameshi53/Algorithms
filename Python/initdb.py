# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:47:48 2022

@author: User
"""

import sqlite3 
connection = sqlite3.connect("project.db")
cursor = connection.cursor()
cursor.execute("""
               CREATE TABLE project
               (Staff Name,Num of Children,Hours Worked,Gross Pay,Net Pay,Deductions)
               """)
               
cursor.execute("""INSERT INTO project VALUES
               ("Emmanuel Zigah",2,53,20,20,10),
               ("Derrick",4, 44, 20,20,32)
               """)

connection.commit()