# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:19:59 2021

@author: User
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.science = {
            'What is the name of the male part of a flower':'Stamen', 'A group of Petals is called':'Corolla',
            'A group of Sepals is called':'Calyx', 'The S.I Unit of Temperature is':'Kelvin', 'A seed is a': 'Fertilized Ovule',
            'Which type of fruit contains only one seed':'Drupe'
                      }
        # self.label = ''
        self.maths = {
            'How many edges does a cube have':'8', 'How many lines of symmetry does a square have': '4', 'The mean of the numbers 5,2x,4, and 3 is 5. Find the value of x.':'4',
            'The two sides of a parallelogram are 4.8m and 7.2m long. Find its perimeter.':'24','If the bearing of A from B is 240<sup>0</sup>, find the bearing of B from A.':'60',
            'Find the gradient of the straight line which passes through the point (-3,4) and (3,-2)':'-1','If 6:8 = r:48, find the value of r.':'36','Express 12/25 in decimal fraction.':'0.48',
            'When 12 is subtracted from three times a certain number and the result is divided by four, the answer is eighteen. Find the number.':'28','Multiply 247 by 32':'7904',
            'Find the Least Common Multiple (L.C.M) of 2,3 and 5.':'30','Write two hundred and two million, two thousand, two hundred and two in figures.':'202,002,202',
            'Evaluate: (0.07 x 0.02) ÷ 14':'0.0001','In a class of 23 students, the girls were 7 more than the boys. How many boys were in the class?':'8', 
            'Find the least number that can be added to 207 to make the sum divisible by 17':'14', 'If P={factors of 36} and Q={multiples of 4 less than 40}, find the number of subsets in PnQ':'8',
            'Find the LCM of 10, 15 and 25':'90'
                      }
        self.questions = list(self.maths.keys())
        self.answers = list(self.maths.values())
        self.panswers = [
            ['Pistil', 'Stamen', 'Anther', 'Calyx'],['Calyx', 'Stamen', 'Corolla', 'Receptacle'],
            ['Calyx', 'Stamen', 'Corolla', 'Receptacle'], ['Watt', 'Kelvin', 'Power', 'Newton'],
            ['Fertilised ovary', 'Fertilized Ovule', 'matured flower', 'fruit'],
            ['Drupe','Anopheles','Self Pollination', 'Berry']
            ]
        self.uanswers = []
        self.score = 0
        self.count = 0

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        
        self.create_widgets()
        self.setMaximumWidth(500)
        self.setMaximumHeight(500)
        
        self.setWindowTitle('Quiz')
        self.setGeometry(500,350,400,300)
        
    def create_widgets(self):
        self.tcount = 0
        self.start = True
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        
        self.tlabel = QLabel('Timer', self)
        
        self.tlabel.setGeometry(10,20,200,50)
        self.tlabel.setStyleSheet('border: 3px solid black')
        self.tlabel.setFont(QFont('Times',15))
        
        
        self.label = QLabel(self.questions[self.count], self)
        self.label.setFont(QFont('Arial', 14))
        
        self.layout.addWidget(self.label, 0, 0,1,2)
        
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(6)
        self.layout.addWidget(self.progressbar, 6,0)
        
        self.line = QLineEdit(self)
        self.line.resize(200,70)
        self.line.move(100,100)
        self.layout.addWidget(self.line,2,0,1,2)
        self.line.setFont(QFont('Arial', 14))
        
        self.buttongroup = QButtonGroup()
        self.buttongroup.setExclusive(False)
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        
        
        button = QPushButton("Next")
        self.buttongroup.addButton(button, 1)
        self.layout.addWidget(button)
        self.layout.addWidget(button, 3, 0)
        button.setFont(QFont('Arial', 14))
        
        button = QPushButton("Previous")
        self.buttongroup.addButton(button, 2)
        self.layout.addWidget(button)
        button.setEnabled(False)
        self.layout.addWidget(button, 3, 1)
        button.setFont(QFont('Arial', 14))
        
        button = QPushButton("Finish")
        self.buttongroup.addButton(button, 3)
        self.layout.addWidget(button)
        self.layout.addWidget(button, 3, 2)
        button.setFont(QFont('Arial', 14))
    
    def showTime(self):
        self.start = True
        second = 10
        self.tcount = second * 10
        self.tlabel.setText(str(second))
        
        if self.start:
            self.tcount -= 1
            if self.tcount == 0:
                self.start = False
                self.tlabel.setText('Completed !!!')
            
        if self.start:
            text = str(self.tcount/10)
            self.tlabel.setText(text)
    
    def on_button_clicked(self, id):
        self.progressbar.setValue(self.count)
        
        def change_question():
            self.label.setText(self.questions[self.count])
            
            
        if self.maths[self.questions[self.count]].lower() == self.line.text().lower():
            self.score += 1   
            
        for button in self.buttongroup.buttons():
            
            if button is self.buttongroup.button(id):
                print("%s was clicked!" % (button.text()))

                if button.text() == 'Next' and self.count < len(self.questions)-1:
                    if self.line.text() == '':
                        alert = QMessageBox()
                        alert.setText('Please don\'t leave the space blank ')
                        alert.exec_()
                    else:
                        # if self.science[self.questions[self.count]].lower() == self.line.text().lower():
                        #     self.score += 1
                        self.count += 1
                        change_question()
                        print(self.line.text())
                        self.uanswers.append(self.line.text())
                        self.line.setText('')

                elif button.text() == 'Previous':
                    if self.count > 0:
                        self.count -= 1
                        change_question()
                else:
                    alert = QMessageBox()
                    alert.setText('<h1>You scored '+str(self.score)+' out of '+str(len(self.questions))+
                                  "</h1><center>" \
                                   "<h1>Answers</h1>" \

                                   "</center>" 
                                   +'1. ' +self.questions[0]+" <br/><b>Ans:  " + self.answers[0]+ '</b>'+
                                   '<br/>2. ' +self.questions[1]+" <br/><b>Ans:  " + self.answers[1]+'</b>'+
                                   '<br/>3. ' +self.questions[2]+" <br/><b>Ans:  " + self.answers[2]+'</b>'+
                                   '<br/>4. ' +self.questions[3]+" <br/><b>Ans:  "+ self.answers[3]+'</b>'+
                                   '<br/>5. ' +self.questions[4]+" <br/><b>Ans:  "+ self.answers[4]+'</b>'+
                                   '<br/>6. ' +self.questions[5]+" <br/><b>Ans:  "+ self.answers[5]+'</b>'+
                                   '<br/>7. ' +self.questions[6]+" <br/><b>Ans:  "+ self.answers[6]+'</b>'+
                                   '<br/>8. ' +self.questions[7]+" <br/><b>Ans:  "+ self.answers[7]+'</b>'+
                                   '<br/>9. ' +self.questions[8]+" <br/><b>Ans:  "+ self.answers[8]+'</b>'+
                                   '<br/>10. ' +self.questions[9]+" <br/><b>Ans:  "+ self.answers[9]+'</b>'+
                                   '<br/>11. ' +self.questions[10]+" <br/><b>Ans:  "+ self.answers[10]+'</b>'+
                                   '<br/>12. ' +self.questions[11]+" <br/><b>Ans:  "+ self.answers[11]+'</b>'+
                                   '<br/>13. ' +self.questions[12]+" <br/><b>Ans:  "+ self.answers[12]+'</b>'+
                                   '<br/>14. ' +self.questions[13]+" <br/><b>Ans:  "+ self.answers[13]+'</b>'+
                                   '<br/>15. ' +self.questions[14]+" <br/><b>Ans:  "+ self.answers[14]+'</b>'+
                                   # '<br/>16. ' +self.questions[15]+" <br/><b>Ans:  "+ self.answers[15]+'</b>'+
                                   # '<br/>17. ' +self.questions[16]+" <br/><b>Ans:  "+ self.answers[16]+'</b>'+
                                   #'<br/>18. ' +self.questions[12]+" <br/><b>Ans:  "+ self.answers[12]+'</b>'+
                                   
                                   
                                   "<p>Version 31.4.159.265358<br/>" \
                                   "Copyright &copy; Company Inc.</p>")
                    self.score = 0
                    alert.exec_()
                    self.close()
                    # app.exec_()
                    
                    

    
    def check_limit(self):
        return self.count == len(self.questions)
    
    # def show_time(self):
    #     if time.elapsed() > 0:
    #         priZ

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
