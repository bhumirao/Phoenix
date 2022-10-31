# Set your Cloudinary credentials
# ==============================
import json
import cloudinary.api
import cloudinary.uploader
import cloudinary
from PIL import Image
from pygraphics import media

cloudinary.config(
  cloud_name="dou3n7mh9", 
  api_key="623647954641815", 
  api_secret="Ie_i3R8I8_ENhAmdPluO7kcQjIU",
  secure=True,)



from cloudinary import CloudinaryImage
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================

# Import to format the JSON responses
# ==============================

# Set configuration parameter: return "https" URLs by setting secure=true
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================


print("****1. Set up and configure the SDK:****\nCredentials: ",
      config.cloud_name, config.api_key, "\n")


def uploadImage():

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new version

    cloudinary.uploader.upload("/home/bhumika/Documents/djEnv/phoenix/static/images/seminars.jpg",
                               public_id="seminars", use_filename=True, unique_filename=False, overwrite=True)
    srcURL = cloudinary.CloudinaryImage("seminars").build_url()

  # Log the image URL to the console.
  # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")

# =======================================


def getAssetInfo():

  # Get and use details of the image
  # ==============================

  # Get image details and save it in the variable 'image_info'.
    image_info = cloudinary.api.resource("seminars")
    print("****3. Get and use details of the image****\nUpload response:\n",
          json.dumps(image_info, indent=2), "\n")

    # Assign tags to the uploaded image based on its width. Save the response to the update in the variable 'update_resp'.
    if image_info["width"] > 900:
        update_resp = cloudinary.api.update(
            "seminars", tags="large")
    elif image_info["width"] > 500:
        update_resp = cloudinary.api.update(
            "seminars", tags="medium")
    else:
        update_resp = cloudinary.api.update(
            "seminars", tags="small")

    # Log the new tag to the console.
    print("New tag: ", update_resp["tags"], "\n")

def createImageTag():

        # Transform the image
        # ==============================

        # Create an image tag with transformations applied to the src URL.

    image_tag=cloudinary.CloudinaryImage("seminars").image(radius="max")

    # Log the image tag to the console
    print("****4. Transform the image****\nTransfrmation URL: ",image_tag,"\n")

def main():
    uploadImage()
    getAssetInfo()
    createImageTag()


main()
