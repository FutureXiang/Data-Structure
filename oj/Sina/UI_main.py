import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_UI import *
from Sina import System


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Let's Google the Sina News!")

        self.pushButton.clicked.connect(self.GetText)
        self.textBrowser.setOpenExternalLinks(True)

        self.Sina = System()
        self.ShowHotWords()

    def ShowHotWords(self):
        for item in self.Sina.TopRank:
            for word in item['KeyWords']:
                word_text = word[0]
                score = word[1]
                self.Sina.GlobalStatistic(word_text, score)   # Gen Hot Words
        StatisticList = []
        for item in self.Sina.Statistic:
            StatisticList.append((item, self.Sina.Statistic[item]))
        TopWords = sorted(StatisticList, reverse=True, key = lambda x:x[1])
        
        self.ShowText("Top 10 Hot Words Today are : ")
        for i in range(10):
            if(i % 2 == 0):
                self.ShowText(TopWords[i][0] + "　"*(10 - len(TopWords[i][0])) + TopWords[i+1][0])
        self.ShowText("----------------------")

    def GetText(self):
        TextValue = self.lineEdit.text()
        tmp = self.Sina.SearchEngine(TextValue)
        self.ShowResult(tmp)
    
    def ShowResult(self, content):
        for item in content:
            self.textBrowser.append('<a href="{}">{}</a>'.format(item[4], item[1])) # [ (dist, Title, count, reRank, URL) ]
    def ShowText(self, content):
        self.textBrowser.append(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())