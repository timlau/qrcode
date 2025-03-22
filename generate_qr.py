from pathlib import Path

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.svg import (  # noqa: F401
    SvgFragmentImage,
    SvgImage,
    SvgPathFillImage,
    SvgPathImage,
)

# from qrcode.image.styles.colormasks import RadialGradiantColorMask


def generate_qr_code(url):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    images = [
        qr.make_image(fill="black", back_color="white"),
        qr.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer()
        ),
        qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            embeded_image_path="images/Junkyard-Drive-Logo.jpg",
        ),
        qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            embeded_image_path="images/junkyard_01.webp",
        ),
        # Save the image to a file
        qr.make_image(
            image_factory=SvgPathFillImage,
        ),
        # Save the image to a file
        qr.make_image(
            image_factory=SvgPathImage,
        ),
    ]
    for ndx, image in enumerate(images):
        match ndx + 1:
            case 5 | 6:
                ext = "svg"
            case _:
                ext = "png"
        out_path = Path(f"output/qrcode{ndx + 1}.{ext}")
        image.save(out_path)
    print("QR codes generated")


if __name__ == "__main__":
    url = "https://www.facebook.com/groups/470668463436266/"
    generate_qr_code(url)
