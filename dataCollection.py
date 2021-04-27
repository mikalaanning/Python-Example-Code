import cv2
import numpy

# Open the ZED camera
capture = cv2.VideoCapture(1)

# Set the video resolution to HD720 (2560*720)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Set the values of the counters
image_counter_red = 0
image_counter_green = 0
image_counter_yellow = 0
image_counter_nothing = 0

while capture.isOpened():
    # Get a new frame from camera
    _, frame = capture.read()
    # Extract left and right images from side-by-side
    left_right_image = numpy.split(frame, 2, axis=1)
    # Display images
    cv2.imshow("right", left_right_image[0])
    cv2.imshow("left", left_right_image[1])

    key = cv2.waitKey(1)

    # IF waited at least 1 ms AND 'q' is pressed then EXIT the loop.
    if key & 0xFF == ord('q'):
        print('Escape hit, closing...')
        break

    # IF waited at least 1 ms AND '1' is pressed then save the Red frame.
    elif key & 0xFF == ord('1'):
        image_path_red = './bouyData/images_red/{}.png'.format(image_counter_red)
        cv2.imwrite(image_path_red, left_right_image[0])
        image_counter_red += 1
        image_path_red = './bouyData/images_red/{}.png'.format(image_counter_red)
        cv2.imwrite(image_path_red, left_right_image[1])
        image_counter_red += 1
        print('1 key pressed - red bouy image counter: {}'.format(image_counter_red))

    # IF waited at least 1 ms AND '2' is pressed then save the Green frame.
    elif key & 0xFF == ord("2"):
        image_path_green = './bouyData/images_green/{}.png'.format(image_counter_green)
        cv2.imwrite(image_path_green, left_right_image[0])
        image_counter_green += 1
        image_path_green = './bouyData/images_green/{}.png'.format(image_counter_green)
        cv2.imwrite(image_path_green, left_right_image[1])
        image_counter_green += 1
        print('2 key pressed - green bouy image counter: {}'.format(image_counter_green))

    # IF waited at least 1 ms AND '3' is pressed then save the Yellow frame.
    elif key & 0xFF == ord("3"):
        image_path_yellow = './bouyData/images_yellow/{}.png'.format(image_counter_yellow)
        cv2.imwrite(image_path_yellow, left_right_image[0])
        image_counter_yellow += 1
        image_path_yellow = './bouyData/images_yellow/{}.png'.format(image_counter_yellow)
        cv2.imwrite(image_path_yellow, left_right_image[1])
        image_counter_yellow += 1
        print('3 key pressed - yellow bouy image counter: {}'.format(image_counter_yellow))

    # IF waited at least 1 ms AND '4' is pressed then save the Nothing frame.
    elif key & 0xFF == ord("4"):
        image_path_nothing = './bouyData/images_nothing/{}.png'.format(image_counter_nothing)
        cv2.imwrite(image_path_nothing, left_right_image[0])
        image_counter_nothing += 1
        image_path_nothing = './bouyData/images_nothing/{}.png'.format(image_counter_nothing)
        cv2.imwrite(image_path_nothing, left_right_image[1])
        image_counter_nothing += 1
        print('4 key pressed - nothing image counter: {}'.format(image_counter_nothing))

#   Destroy all of windows
cv2.destroyAllWindows()
#   Release the captured frame
capture.release()