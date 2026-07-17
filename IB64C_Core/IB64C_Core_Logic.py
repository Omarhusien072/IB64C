import base64, os

def createFile(encoded_imgs: dict, output_directory: str):
    output_directory = output_directory.replace("\\", "/")
    lines = []
    base_name = "Images"
    file_ext = "py"
    file_counter = 1
    file_name = f"{base_name}.{file_ext}"

    while os.path.exists(f"{output_directory}/{file_name}"):
        file_name = f"{base_name}_{file_counter}.{file_ext}"
        file_counter += 1

    with open(f"{output_directory}/{file_name}", "w", encoding="utf-8") as python_file:
        python_file.write("# This file is auto-generated. Do not edit manually.\n\n")
        for name, img in encoded_imgs.items():
            # Using triple quotes and a backslash to handle multi-line strings correctly
            lines.append(f'{name} = """\\\n{img}"""\n\n')
        python_file.writelines(lines)
        return True, f"{file_name}"

    with open(
        f"{output_directory}/{file_name}.{file_ext}", "w", encoding="utf-8"
    ) as python_file:
        python_file.write("# This file is auto-generated. Do not edit manually.\n\n")
        for name, img in encoded_imgs.items():
            # Using triple quotes and a backslash to handle multi-line strings correctly
            lines.append(f'{name} = """\\\n{img}"""\n\n')
        python_file.writelines(lines)
    return True, f"{file_name}"


def convertToBase64(imgs: dict, output_directory: str):
    encoded_strings = {}

    for name, img in imgs.items():
        try:
            with open(img, "rb") as image_file:
                # 1. Convert binary to base64 string
                raw_base64 = base64.b64encode(image_file.read()).decode("utf-8")

                # 2. Break it into 80-character chunks so your editor doesn't lag
                chunked_base64 = "\n".join(
                    [raw_base64[i : i + 80] for i in range(0, len(raw_base64), 80)]
                )

                encoded_strings[name] = chunked_base64
        except FileNotFoundError:
            encoded_strings[""] = ""

    is_created, file_name = createFile(
        encoded_imgs=encoded_strings, output_directory=output_directory
    )
    if is_created:
        return True, file_name


def SearchDirectory(directory_path: str, file_type: str):
    if not directory_path.endswith("/") and not directory_path.endswith("\\"):
        directory_path += "/"
    file_type = file_type.lower()
    
    imgs = {}
    imgs_names = []
    imgs_paths = []
    img_types = ["png", "jpg", "jpeg", "gif", "bmp", "webp", "svg"]
    special_characters = [
        " ", "-", ".",
        "(", ")", "[",
        "]", "{", "}",
        "@", "#", "$", 
        "%", "^", "&",
        "*", "+", "=",
        "~", "`", "!",
        "?", "<", ">",
        "|", "\\", "/",
    ]

    if file_type.upper() == "ALL":
        directory_path = directory_path.replace("\\", "/")
        imgs_paths = [
            os.path.join(root, file)
            for root, dirs, files in os.walk(directory_path)
            for file in files
            if file.endswith(tuple(f"{img_type}" for img_type in img_types))
        ]

        if not (len(imgs_paths) > 0):
            return False

        file_names = [os.path.basename(file) for file in imgs_paths]
        for img_name in file_names:
            if img_name[:1].isdigit():
                img_name = f"_{img_name}"

            for char in special_characters:
                img_name: str = img_name.replace(char, "_")
            imgs_names.append(f"{img_name}")

        for name, path in zip(imgs_names, imgs_paths):
            imgs[name] = path
        return imgs

    directory_path = directory_path.replace("\\", "/")
    imgs_paths = [
        os.path.join(root, file)
        for root, dirs, files in os.walk(directory_path)
        for file in files
        if file.endswith(file_type)
    ]

    if not (len(imgs_paths) > 0):
        return False

    file_names = [os.path.basename(file) for file in imgs_paths]
    for img_name in file_names:
        img_name = os.path.splitext(img_name)[0]
        if img_name[:1].isdigit():
            img_name = f"_{img_name}"

        for char in special_characters:
            img_name = img_name.replace(char, "_")
        imgs_names.append(f"{img_name}_{file_type}")

    for name, path in zip(imgs_names, imgs_paths):
        imgs[name] = path
    return imgs
