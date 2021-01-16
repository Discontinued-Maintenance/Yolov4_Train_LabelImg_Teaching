### 標記圖片使用LabelImg

[LabelImg Github](https://github.com/tzutalin/labelImg)

* git clone https://github.com/tzutalin/labelImg.git
* pip install lxml
* pip install pyqt5
* 如遇到`No module named 'libs.resources'`錯誤輸入下列指令

  ```
  pyrcc5 -o ./libs/resources.py resources.qrc
  ```

<br>

### 接著創建一個名為images的資料夾並在此資料夾並在此資料夾底下創建兩個新資料夾分別為

<br>

**test**     將20％ 的圖片數量放到test資料夾內(包含標記過後對應的XML檔)

**train**    將80％ 的圖片數量放到train資料夾內(包含標記過後對應的XML檔)