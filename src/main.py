import cv2

cap = cv2.VideoCapture("./test.mp4")

fps = 30
codec = int(cv2.VideoWriter_fourcc(*'mp4v'))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('fps=', fps, 'size=', width, height)
output = cv2.VideoWriter('./output.mp4', codec, fps, (width, height), False)

while True:
    try:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output.write(gray)

    except:
        break

cap.release()
output.release()
