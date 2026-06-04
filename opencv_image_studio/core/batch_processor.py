import os
import cv2


class BatchProcessor:

    VALID_EXTENSIONS = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp"
    )

    @staticmethod
    def process_folder(

        input_folder,

        output_folder,

        pipeline_manager,

        plugins

    ):

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        processed_count = 0

        for file in os.listdir(
            input_folder
        ):

            if not file.lower().endswith(
                BatchProcessor.VALID_EXTENSIONS
            ):
                continue

            image_path = (
                os.path.join(
                    input_folder,
                    file
                )
            )

            image = cv2.imread(
                image_path
            )

            if image is None:
                continue

            result = (
                pipeline_manager.execute(
                    image,
                    plugins
                )
            )

            name, ext = (
                os.path.splitext(
                    file
                )
            )

            output_path = (
                os.path.join(
                    output_folder,
                    f"{name}_processed{ext}"
                )
            )

            cv2.imwrite(
                output_path,
                result
            )

            processed_count += 1

        return processed_count