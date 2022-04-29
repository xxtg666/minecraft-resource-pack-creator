import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_mrpcg import Ui_MainWindow
import webbrowser as wb
import mrpccore as mrc
import zipfile
from PIL import Image
import time
import shutil

def zipDir(dirpath, outFullName):
    z = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            z.write(os.path.join(path, filename), os.path.join(fpath, filename))
    z.close()
class mrpc(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initp()
        self.s1_p.clicked.connect(self.f_s1_p)
        self.s2_p.clicked.connect(self.f_s2_p)
        self.s1_d.clicked.connect(self.f_s1_d)
        self.nextstep.clicked.connect(self.f_nextstep)
        self.pushButton.clicked.connect(self.f_start)
        self.show()
    def initp(self):
        self.stepnow=1
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
    def f_s1_p(self):
        self.s1_l.setText(QFileDialog.getOpenFileName(self, "选择packzip-mc-resource-pack-creator.zip", "","mrpc-zip (packzip-mc-resource-pack-creator.zip)")[0])
    def f_s1_d(self):
        wb.open("https://xxtg666.lanzout.com/iWReO03z24xi")
    def f_s2_p(self):
        self.s2_l.setText(QFileDialog.getOpenFileName(self, "选择png图片文件", "","图片文件 (*.png)")[0])
    def f_nextstep(self):
        if self.stepnow==1:
            if not os.path.exists(self.s1_l.text()):
                QMessageBox.warning(self,"Step 1 Warning","packzip-mc-resource-pack-creator.zip文件不存在")
                return 
            if not self.s1_l.text().endswith("packzip-mc-resource-pack-creator.zip"):
                QMessageBox.warning(self,"Step 1 Warning","请选择packzip-mc-resource-pack-creator.zip")
                return 
            self.stepnow=2
            self.packpath=self.s1_l.text()
            self.groupBox_2.setEnabled(True)
            self.groupBox.setEnabled(False)
            self.step.setText("Step 2")
            return 
        if self.stepnow==2:
            if not os.path.exists(self.s2_l.text()):
                QMessageBox.warning(self,"Step 2 Warning","png图片文件不存在")
                return 
            if not self.s2_l.text().endswith(".png"):
                QMessageBox.warning(self,"Step 2 Warning","请选择png图片文件")
                return 
            self.stepnow=3
            self.pngpath=self.s2_l.text()
            self.groupBox_2.setEnabled(False)
            self.groupBox_3.setEnabled(True)
            self.nextstep.setEnabled(False)
            self.step.setText("Step 3")
            return 
    def f_start(self):
        QMessageBox.information(self,"Step 3","制作需要一定时间，程序会未响应，请耐心等待，按OK开始")
        try:
            file = zipfile.ZipFile(self.packpath,'r')
            try:
                shutil.rmtree("pack_temp")
            except:
                pass
            for f in file.namelist():
                file.extract(f,"pack_temp/")
            mrc.example=Image.open(self.pngpath)
            mrc.rep("pack_temp")
            outputname="pack-output-"+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())+".zip"
            zipDir("pack_temp",outputname)
            try:
                shutil.rmtree("pack_temp")
            except:
                pass
            QMessageBox.information(self,"Step 3","制作完成，已生成"+outputname+"资源包")
            sys.exit(0)
        except Exception as e:
            QMessageBox.critical(self,"Step 3 Error",e+"\n请将错误信息发给作者以反馈……")
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mrpc()
    sys.exit(app.exec_())
