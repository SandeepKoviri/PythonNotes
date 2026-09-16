
import qrcode


def qr_code():
    # Take input from the user
    data = input("Enter text, URL, or any data: ").strip()

    # Check if input is empty
    if not data:
        print("Please enter some data.")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR image
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Ask for filename
    filename = input(
        "Enter the filename to save QR code: "
    ).strip()

    if not filename:
        filename = "my_qrcode"

    # Save image
    image.save(f"{filename}.png")

    print("QR code generated successfully!")
    print(f"Saved as: {filename}.png")