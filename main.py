import cv2
import numpy as np


def show_video(video_path):
    cap = cv2.VideoCapture(video_path)
    # fpsを取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, frame = cap.read()
        if not ret or cv2.waitKey(1) == 27:
            break

        cv2.imshow("frame", frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_path = "data\【TAB】ヨルシカ-晴る- 『葬送のフリーレン』　⧸Guitar cover【弾いてみた】.mp4"
    # video_path = "data\【TAB譜】Magic ⧸ Mrs. GREEN APPLE.mp4"
    # video_path = "data\【TAB譜あり】逆光 (ウタ from ONE PIECE FILM RED) ギター 弾いてみた.mp4"

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    # print(frame.shape)
    cv2.imshow("frame", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(gray)
    # print(type(gray))
    # cv2.imshow("frame", gray)

    # 2値化
    # 0は黒、255は白
    # 240以上は白、240未満は黒にする
    threshold = 240
    ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    # cv2.imshow("frame", binary)

    # 直線検出
    # 垂直方向の直線を検出する
    lines = cv2.HoughLinesP(
        binary,
        rho=1,
        theta=np.pi / 180,
        threshold=100,
        minLineLength=100,
        maxLineGap=10
    )
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imshow("frame", frame)

    cv2.waitKey(0)
