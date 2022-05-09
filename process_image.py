# Python code to find the co-ordinates of
# the contours detected in an image.
import cv2


def parse_image(image: str):
    # file_path: str = "./xray_file.png"
    # Reading image
    font = cv2.FONT_HERSHEY_COMPLEX
    img2 = cv2.imread(image, cv2.IMREAD_COLOR)

    # Reading same image in another
    # variable and converting to gray scale.
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    # edged = cv2.Canny(img, 20, 300)

    # Converting image to a binary image
    # ( black and white only image).
    _, threshold = cv2.threshold(img, 200, 455, cv2.THRESH_BINARY)

    # Detecting contours in image.
    # contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
    #                                cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Going through every contours found in the image.
    for cnt in contours:

        approx = cv2.approxPolyDP(cnt, 0.020 * cv2.arcLength(cnt, True), True)

        # draws boundary of contours.
        # cv2.drawContours(img2, 0, (0, 0, 255), 5)
        # cv2.drawContours(img2, contours, -1, (10, 355, 100), 3)
        cv2.drawContours(img2, contours, 0, (0,255, 0), 3)

        # Used to flatten the array containing
        # the co-ordinates of the vertices.
        values = approx.ravel()
        i = 0

        for _ in values:
            if i % 2 == 0:
                x = values[i]
                y = values[i + 1]

                # String containing the co-ordinates.
                string = f"{str(x)} {str(y)}"

                if i != 0:
                    # text on remaining co-ordinates.
                    cv2.putText(img2, string, (x, y), font, 0.5, (0, 255, 0))
            i = i + 1

    # Saving the image
    cv2.imwrite("./output_image/image.jpg", img2)

