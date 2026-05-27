import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


# Load image
photo = img.imread(r"try\tasks\sample.jpg")

print("\nImage Details")
print("Shape :", photo.shape)
print("Data Type :", photo.dtype)


# -----------------------------------
# Grayscale Conversion
# -----------------------------------

gray_image = photo.mean(axis=2)


# -----------------------------------
# Brightness Control
# -----------------------------------

bright_version = np.clip(photo + 40, 0, 255)

dark_version = np.clip(photo - 40, 0, 255)


# -----------------------------------
# Image Transformations
# -----------------------------------

flip_left_right = np.fliplr(photo)

flip_up_down = np.flipud(photo)


# -----------------------------------
# Crop Center Area
# -----------------------------------

cropped = photo[80:350, 150:450]


# -----------------------------------
# Simple Blur Effect
# -----------------------------------

blur = photo.copy()

for row in range(1, photo.shape[0] - 1):
    for col in range(1, photo.shape[1] - 1):

        blur[row, col] = np.mean(
            photo[row-1:row+2, col-1:col+2],
            axis=(0, 1)
        )


# -----------------------------------
# Display Results
# -----------------------------------

fig, ax = plt.subplots(2, 4, figsize=(16, 8))


ax[0, 0].imshow(photo)
ax[0, 0].set_title("Original")
ax[0, 0].axis("off")


ax[0, 1].imshow(gray_image, cmap="gray")
ax[0, 1].set_title("Gray")
ax[0, 1].axis("off")


ax[0, 2].imshow(bright_version.astype(np.uint8))
ax[0, 2].set_title("Bright")
ax[0, 2].axis("off")


ax[0, 3].imshow(dark_version.astype(np.uint8))
ax[0, 3].set_title("Dark")
ax[0, 3].axis("off")


ax[1, 0].imshow(flip_left_right)
ax[1, 0].set_title("Horizontal Flip")
ax[1, 0].axis("off")


ax[1, 1].imshow(flip_up_down)
ax[1, 1].set_title("Vertical Flip")
ax[1, 1].axis("off")


ax[1, 2].imshow(cropped)
ax[1, 2].set_title("Cropped")
ax[1, 2].axis("off")


ax[1, 3].imshow(blur.astype(np.uint8))
ax[1, 3].set_title("Blur")
ax[1, 3].axis("off")


plt.tight_layout()

print("\nImage Processing Finished Successfully!")

plt.show()