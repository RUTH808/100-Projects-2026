import numpy as np


class ImageStatistics:

    @staticmethod
    def get_stats(img):

        if img is None:
            return {}

        h, w = img.shape[:2]

        channels = (
            img.shape[2]
            if len(img.shape) == 3
            else 1
        )

        return {

            "Width":
                w,

            "Height":
                h,

            "Channels":
                channels,

            "Mean":
                round(
                    float(
                        np.mean(img)
                    ),
                    2
                ),

            "Std Dev":
                round(
                    float(
                        np.std(img)
                    ),
                    2
                ),

            "Min":
                int(
                    np.min(img)
                ),

            "Max":
                int(
                    np.max(img)
                )
        }