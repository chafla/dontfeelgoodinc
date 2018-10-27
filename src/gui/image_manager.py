from io import BytesIO
import PIL.Image
import cv2


class ImageManger:

    def __init__(self, fp: str):

        self.gain = 0
        self.image = None
        self.fp = fp

    def update_image(self) -> BytesIO:
        """Load the image"""
        # TODO get the actual image from here

        cv2_img = None  # WIll be from the cv2 image

        # Convert openCV image to PIL image so it's easier to work with

        open_cv_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

        pil_im = PIL.Image.fromarray(open_cv_image)

        img_fd = BytesIO()

        pil_im.save(img_fd, format="png")

        # Return to the beginning for the next read
        img_fd.seek(0)

        return img_fd
