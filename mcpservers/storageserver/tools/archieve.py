import zipfile
import os


def zip_files(files:list, zip_name="study_material.zip"):

    zip_path=os.path.join(
        "storage/generated_files",
        zip_name
    )


    with zipfile.ZipFile(
        zip_path,
        "w"
    ) as z:

        for file in files:
            z.write(
                file,
                os.path.basename(file)
            )


    return {
        "status":"success",
        "zip":zip_path
    }