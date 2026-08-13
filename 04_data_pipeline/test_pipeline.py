from pathlib import Path
import unittest
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent


class TestDataPipeline(unittest.TestCase):

    def test_csv_exists(self):
        self.assertTrue((BASE_DIR / "synthetic_data.csv").exists())

    def test_plot_exists(self):
        self.assertTrue((BASE_DIR / "synthetic_data_plot.png").exists())

    def test_data_is_numeric(self):
        data = pd.read_csv(BASE_DIR / "synthetic_data.csv")

        self.assertTrue(pd.api.types.is_numeric_dtype(data["x"]))
        self.assertTrue(pd.api.types.is_numeric_dtype(data["y"]))

    def test_slope_and_intercept(self):
        data = pd.read_csv(BASE_DIR / "synthetic_data.csv")

        x = data["x"]
        y = data["y"]

        measured_m, measured_b = np.polyfit(x, y, 1)

        # Allow some tolerance because the data contains noise
        self.assertAlmostEqual(measured_m, 2, delta=0.2)
        self.assertAlmostEqual(measured_b, 5, delta=0.5)


if __name__ == "__main__":
    unittest.main()
