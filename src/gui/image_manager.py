from io import BytesIO
import PIL.Image
import cv2
import imageio
from src.schmengies.DesImage import DesImage


class ImageManager:

    def __init__(self, fp: str):

        self._gain = 0
        self._chunk_size = 0
        self.image = DesImage(fp)
        self._original_fp = fp

        self._last_animation = None

    def update_image(self, override=False) -> BytesIO:
        """
        Load the image.
        If override is set to True, then the DesTheImage instance image will be corrupted and overridden.
        If false, then the image returned will be corrupted, but any subsequent calls.
        """
        # TODO get the actual image from here

        cv2_img = self.image.DesTheImage(self._gain, override=override)

        # cv2_img = self.image.ReturnImage()  # WIll be from the cv2 image

        # Convert openCV image to PIL image so it's easier to work with

        open_cv_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

        pil_im = PIL.Image.fromarray(open_cv_image)

        img_fd = BytesIO()

        pil_im.save(img_fd, format="png")

        # Return to the beginning for the next read
        img_fd.seek(0)

        return img_fd

    def reset(self):
        """Reload, attempting to check the new chunk sizes"""
        self.image = DesImage(self._original_fp, self.chunk_size, self.chunk_size)

    @property
    def gain(self) -> int:
        return self._gain

    @gain.setter
    def gain(self, new_value: int):
        """Assuming it's going to be coming in from 0-100, so let's scale it appropriately"""
        # https://stackoverflow.com/questions/929103/convert-a-number-range-to-another-range-maintaining-ratio
        scaled_value = (new_value * 20) / 100

        self._gain = int(scaled_value)

    @property
    def chunk_size(self) -> int:
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, value: int):
        self._chunk_size = value
        self.reset()

    def create_animation(self, file_path: str):
        images = []
        original_gain = self.gain

        for i in reversed(range(1, 101, 5)):

            # TODO This is going to cause many issues down the line
            self.gain = i
            new_img_fd = self.update_image()
            img = imageio.imread(new_img_fd)
            images.append(img)

        imageio.mimsave(file_path, images, duration=0.1, loop=1)
        self.gain = original_gain
        return file_path
        # Hacky


