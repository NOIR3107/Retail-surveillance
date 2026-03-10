import cv2

def draw_transparent_box(frame, box, color, alpha=0.3):
    """
    Draws a semi-transparent rectangle on the frame.
    box: (x1, y1, x2, y2)
    color: (B, G, R)
    alpha: transparency level
    """
    x1, y1, x2, y2 = box
    overlay = frame.copy()
    cv2.rectangle(overlay, (x1, y1), (x2, y2), color, -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
