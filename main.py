import cv2
import time

if __name__ == '__main__':
    video_path = "data\【TAB】ヨルシカ-晴る- 『葬送のフリーレン』　⧸Guitar cover【弾いてみた】.mp4"
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
