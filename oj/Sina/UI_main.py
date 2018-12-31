import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_UI import *
from Sina import System
import jieba
import re


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Let's Google the Sina News!")

        self.pushButton.clicked.connect(self.GetText)
        self.textBrowser.setOpenExternalLinks(True)

        self.Sina = System()
        self.ShowHotWords()
        jieba.lcut("哈", cut_all = False)

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
        self.textBrowser.clear()
        
        for item in content:
            self.textBrowser.append('<a href="{}"><font size="4" color="#1a0dab">{}</font></a>'.format(item[4], item[1])) # [ (dist, Title, count, reRank, URL) ]
            self.textBrowser.append('<font color="#006621">{}</font>'.format(item[4]))

            date = re.match(r".*(20[0-9]{2}-[0-9]{2}-[0-9]{2}).*", item[4])
            date = date.group(1).split("-")
            date = date[0] + "年" + date[1] + "月" + date[2] + "日  -  "
            date = '<font color="#808080">{}</font>'.format(date)

            self.textBrowser.append(date + " ".join(self.Sina.GetAllText(item[4])[:140].split()) + "......")
            self.textBrowser.append("")
        self.textBrowser.append("")

    def ShowText(self, content):
        self.textBrowser.append(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())