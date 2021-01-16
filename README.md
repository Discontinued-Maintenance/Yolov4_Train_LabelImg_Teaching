## 標記圖片使用LabelImg

[LabelImg Github](https://github.com/tzutalin/labelImg)

* git clone https://github.com/tzutalin/labelImg.git
* pip install lxml
* pip install pyqt5
* 如遇到`No module named 'libs.resources'`錯誤輸入下列指令

  ```
  pyrcc5 -o ./libs/resources.py resources.qrc
  ```

labelImg\data\predefined_classes.txt是預設類別名稱
如果要直接標記Yolo格式檔的人先把裡面的預設類別清除

<br>

## 開始標記照片

這邊分成兩種標記方式，一個是直接標記yolo專用格式檔
另一個是xml再轉成yolo專用格式檔

---

### 首先教學的是直接標記yolo格式檔

把照片分別放入放入yolo_train、yolo_test底下

