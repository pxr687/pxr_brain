import nibabel as nib
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import os

# get the username from the current pc
USER = os.environ.get("USERNAME")

# load the image and get the data
brain_vol = nib.load("C:/Users/"+USER+"/pxr_brain_nii_file/T1_vol.nii")
brain_vol_data = brain_vol.get_fdata()

# show the data and save the image as .jpg
plt.figure(figsize = (10, 10))
plt.imshow(ndi.rotate(brain_vol_data[105], 90), cmap="bone")
plt.axis("off")
plt.savefig("pxr_brain.jpg", format="jpg", dpi = 1200)
plt.show()