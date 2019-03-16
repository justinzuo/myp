
if __name__ == '__main__':
    pass
    try :
        mfile = open(r"C:\Users\筱阿玉\PycharmProjects\myp\day5\liu","r")
    except OSError :
        print("OSerror")
    except Exception :
        print("Exception")
    else :
        mstr = mfile.read()
        print(mstr)
        mfile.close()
