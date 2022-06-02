# reading a from file.


def video():
    vid1 = open('writename.txt', 'r')

    print(vid1.readline())

    vid1.close()


video()
