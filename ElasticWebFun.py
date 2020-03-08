# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:47:23 2019

@author: Vector30
"""

from elasticsearch import Elasticsearch,helpers
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import ElasticWebIndex
import ElasticWeb
import ElasticWaitFunc
import ElasticCourseFunc
class MyWindow(QtWidgets.QMainWindow):
    es = Elasticsearch("http://localhost:9200")
    def __init__(self,parent=None):
        if self.es.indices.exists("nptel"):
            pass
        else:
            self.wait=ElasticWaitFunc.MyWindow()
            self.wait.show()
            ElasticWebIndex.WebIndex()
            self.wait.close()
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = ElasticWeb.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.search)
        self.ui.checkBox_1.clicked.connect(self.search)
        self.ui.checkBox_2.clicked.connect(self.search)
        self.ui.checkBox_3.clicked.connect(self.search)
        self.ui.checkBox_4.clicked.connect(self.search)
        self.ui.checkBox_5.clicked.connect(self.search)
        self.ui.checkBox_6.clicked.connect(self.search)
        self.ui.checkBox_7.clicked.connect(self.search)
        self.ui.checkBox_8.clicked.connect(self.search)
        self.ui.checkBox_10.clicked.connect(self.search)
        self.ui.checkBox_11.clicked.connect(self.search)
        self.ui.checkBox_12.clicked.connect(self.search)
        self.ui.checkBox_13.clicked.connect(self.search)
        self.ui.checkBox_14.clicked.connect(self.search)
        self.ui.checkBox_15.clicked.connect(self.search)
       # self.ui.checkBox_16.clicked.connect(self.search)
        self.ui.checkBox_17.clicked.connect(self.search)
        self.ui.checkBox_19.clicked.connect(self.search)
        self.ui.listWidget.itemClicked.connect(self.getCourseDetail)
        
    def search(self):
        query=[]
        search_txt=self.ui.lineEdit.text()
    

        if(self.ui.checkBox_1.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_1.text()}})
        if(self.ui.checkBox_2.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_2.text()}})
        if(self.ui.checkBox_3.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_3.text()}})
        if(self.ui.checkBox_4.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_4.text()}})
        if(self.ui.checkBox_5.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_5.text()}})
        if(self.ui.checkBox_6.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_6.text()}})
        if(self.ui.checkBox_7.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_7.text()}})
        if(self.ui.checkBox_8.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_8.text()}})
   
        if(self.ui.checkBox_10.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_10.text()}})
        if(self.ui.checkBox_11.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_11.text()}})
        if(self.ui.checkBox_12.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_12.text()}})
        if(self.ui.checkBox_13.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_13.text()}})
        if(self.ui.checkBox_14.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_14.text()}})
        if(self.ui.checkBox_15.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_15.text()}})

        if(self.ui.checkBox_17.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_17.text()}})
      
        if(self.ui.checkBox_19.checkState()):
            query.append({'match_phrase':{"Category :":self.ui.checkBox_19.text()}})
        
       # print(not(self.ui.checkBox.checkState()))
        #print(self.ui.checkBox.text())
      #    Course_filter+=self.ui.checkBox.text()
        search_results = helpers.scan(self.es, index="nptel", query={
	"query": {
		"bool":	
					{"must":
							[{"bool":{
								
										"should":query,
									}
								},{"wildcard":{"title":search_txt+'*'}}]
                                							
		}					
				}})
        self.ui.listWidget.clear()
        for search_result in search_results:
           self.ui.listWidget.addItem(search_result['_source']['title'])
        
    def getCourseDetail(self,item):
        course=item.text()
     
      
        self.course=ElasticCourseFunc.MyWindow()
        self.course.show()
        details=helpers.scan(self.es,index="nptel", query={"query":{"match_phrase":{"title":course}}})
        for detail in details:
            self.course.ui.label.setText(detail['_source']["title"])
            self.course.ui.label_2.setText(detail['_source']["University"])
            self.course.ui.label_3.setText(detail['_source']["Professor"])
            self.course.ui.textEdit_2.setText(detail['_source']['description'])
            self.course.ui.label_13.setText(detail['_source']["Course Status :"])
            self.course.ui.label_14.setText(detail['_source']["Course Type :"])
            self.course.ui.label_15.setText(detail['_source']["Duration :"])
            self.course.ui.label_16.setText(detail['_source']["Start Date :"])
            self.course.ui.label_17.setText(detail['_source']["End Date :"])
            self.course.ui.label_18.setText(detail['_source']["Exam Date :"])
            self.course.ui.label_19.setText(detail['_source']["Category :"])
            print(detail['_source']["Category :"])
            self.course.ui.label_20.setText(detail['_source']["Level :"])
            self.course.ui.textEdit.setText(detail['_source']['COURSE LAYOUT'])
        
if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())