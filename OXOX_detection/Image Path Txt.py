import os

def writetxt(f, txtname, path):
    WriteFile = open(os.path.join('cfg', txtname), 'a+', encoding="utf-8")
    WriteFile.write(os.getcwd() + '/' + path + '/' + f)
    WriteFile.write('\n')
    WriteFile.close()

def Allfile(path, files, txtname):
    for f in files:
        fullpath = os.path.join(path, f)
        if os.path.isfile(fullpath):
            if f.startswith('.'):
                pass
            elif f.endswith('.txt'):
                pass
            else:
                writetxt(f, txtname, path)
        elif os.path.isdir(fullpath):
            pass

trainpath = "yolo_train"
testpath = "yolo_test"
train = "train.txt"
test = "test.txt"

trainfiles = os.listdir(trainpath)
testfiles = os.listdir(testpath)

Allfile(trainpath, trainfiles, train)
Allfile(testpath, testfiles, test)
