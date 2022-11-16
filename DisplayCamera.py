import cv2
import datetime

def check_camera_connection():
    print('[', datetime.datetime.now(), ']', 'searching any camera...')
    true_camera_is = []  # 空の配列を用意

    for camera_number in range(0, 10):
        cap = cv2.VideoCapture(camera_number)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(camera_number)
            print("camera_number", camera_number, "Find!")

        else:
            print("camera_number", camera_number, "None")
    return len(true_camera_is)
 
camera = cv2.VideoCapture(0)                # カメラCh.(ここでは0)を指定
nowCamera = 0
maxCamera = check_camera_connection()
box = -1
 
# 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
while True:
    ret, frame = camera.read()              # フレームを取得
    cv2.imshow('camera', frame)             # フレームを画面に表示

    if box != nowCamera:
        print("Now Camera :", nowCamera)
        box = nowCamera
 
    key = cv2.waitKey(100)
    print("             :", key)
    # キー操作があればwhileループを抜ける
    if key == ord('d'):
        print("     STOP")
        break

    elif key == ord('s'):
        print("     >>")
        if nowCamera == maxCamera-1:
            nowCamera = 0
        else :
            nowCamera = nowCamera + 1
        camera = cv2.VideoCapture(nowCamera)

    elif key == ord('a'):
        print("     <<")
        if nowCamera == 0:
            nowCamera = maxCamera-1
        else :
            nowCamera = nowCamera - 1
        camera = cv2.VideoCapture(nowCamera)
        

    
 
# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()


"""
- [OpenCVで使われるwaitkeyとは?定義から実用例をわかりやすく解説!?](https://kuroro.blog/python/8DIolh7Pwggq2pvabysn/)
- [Pythonでカメラを制御する【研究用】](https://qiita.com/opto-line/items/7ade854c26a50a485159)
"""