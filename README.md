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

## 開始標記照片

這邊分成兩種標記方式，一個是直接標記yolo專用格式檔
另一個是xml再轉成yolo專用格式檔

---

### 首先教學的是直接標記yolo格式檔

把照片分別放入放入yolo_train、yolo_test底下，數量為80%:20%

labelImg設定好讀取圖片檔案資料夾、儲存標記檔資料夾，就可以開始標記

* 標記完成後打開Command OR Terminal並輸入以下指令
  * cd 至 XOXO(您的專案名稱)_detection檔案資料夾底下
  * key入 `python Image Path Txt.py`

當您完成上述步驟會在test、train資料夾內出現對應圖片檔名稱的txt也就是for yolo的標記檔

在cfg資料夾內會出現test.txt、train.txt檔

有出現上述兩個檔案內容表示完成配置您標記和訓練檔路徑了！

---

### 接著開始教學xml格式轉成yolo用格式方法

把照片分別放入放入xml_train、xml_test底下的image，數量為80%:20%

labelImg設定好讀取圖片檔案資料夾、儲存標記檔資料夾(格別資料夾底下的xml資料夾)，就可以開始標記

* 標記完成後打開Command OR Terminal並輸入以下指令
  * cd 至 XOXO(您的專案名稱)_detection檔案資料夾底下
  * 更改PASCAL VOC xml to txt.py檔案內的57~61行，如下圖
    ![PASCAL VOC xml to txt.py](https://github.com/TsaiRongFu/Yolov4_Train_LabelImg_Teaching/blob/main/ReadmePicture/PASCAL%20VOC%20xml%20to%20txt.JPG)
  * 對應到test和train，所以說下列指令要做兩次，分別為跟改test後和train後
  * key入 `python PASCAL VOC xml to txt.py`

  * 如遇到`No module named 'beautifulsoup4'`錯誤輸入下列指令

    ```
    pip3 install beautifulsoup4
    ```

  * 如遇到`lxml錯誤`輸入下列指令

    ```
    pip3 install lxml
    ```

當您完成上述步驟會在test、train資料夾內出現對應圖片檔名稱的txt也就是for yolo的標記檔，還有從image資料夾內複製的圖片

在cfg資料夾內會出現test.txt、train.txt檔

有出現上述兩個檔案內容表示完成配置您標記和訓練檔路徑了！

## 接著開始建置Darknet

[Darknet](https://github.com/AlexeyAB/darknet)

* git clone https://github.com/AlexeyAB/darknet.git
* cd darknet && make

---

### windows 建置環境可以參考下列教學

* [CUDA 與 CuDNN 安裝](https://medium.com/ching-i/win10-%E5%AE%89%E8%A3%9D-cuda-cudnn-%E6%95%99%E5%AD%B8-c617b3b76deb)

* [window Darknet make](https://ithelp.ithome.com.tw/articles/10231950)

---

### Linux、Ubuntu 安裝Darknet 較為簡單

* cd至Darknet資料夾底下，打開Makefile跟改下列四行，由0變成1
* 改為1是為了讓GPU可以運算0的話則為CPU運算
* 更改完儲存後直接key入
* `make`

* 如遇到`遇到nvcc not found`錯誤輸入下列指令(下列路徑要替換成自己系統的路徑)

  ```
  export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}} export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}}:/home/itriedgetpunpust/anaconda3/envs/YOLO/lib
  ```

* 如遇到`No package 'opencv' found to the PKG_CONFIG_PATH environment variable`錯誤輸入下列指令(下列路徑要替換成自己系統的路徑)

  ```
  export  PKG_CONFIG_PATH=/home/itriedgetpunpust/anaconda3/envs/YOLO/lib/pkgconfig
  ```

---

### 因為方便各位訓練因此這次我們會使用Colaboratory來建置訓練環境

[Colaboratory官方網站](https://colab.research.google.com/notebooks/intro.ipynb)

[此次YOLO Colaboratory範例檔](https://colab.research.google.com/drive/1HuI37F6vfSFb7UK3_wnQDru5-zmh0mtg?usp=sharing)

更改為GPU資源運算-->點選「執行階段」-「變更執行階段類型」

更多操作指令參考

[Google Colab相關設定](https://hackmd.io/@wiimax/HJuUPnPQr)

複製darknet/cfg/yolov4-tiny-custom.cfg  到cfg資料夾底下

```
yolov4 偵測的濾鏡(filter) 大小為 (A+5)*B
B 是每個Feature Map可以偵測的bndBox數量，這裡設定為3
5 是bndBox輸出的5個預測值: x,y,w,h 以及 Confidence
A 是類別數量
filters=(classes + 5)*3  # 因為是一個類別，所以filters更改為 18
classes=1  
```
修改預設 anchors 值，可以使用以下指令 (記得更改參數 cfg/face.data, num_of_clusters, width, height)，是由 Darknet 官方寫好可以自動算出 anchors 值

