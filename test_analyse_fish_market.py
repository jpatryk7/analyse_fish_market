import unittest
import os
from analyse_fish_market import *


class TestAnalyseFishMarket(unittest.TestCase):
    def setUp(self) -> None:
        # settings variables
        self.bucket_name = settings.bucket_name
        self.directory_name = settings.directory_name
        self.filename_prefix = settings.filename_prefix
        self.upload_path = settings.upload_path

        # boto3
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
        self.files_at_the_dir = [o["Key"] for o in self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.directory_name
        )["Contents"]]

        # AnalyseFishMarket class' object
        self.fish = AnalyseFishMarket()
        self.avg_data_df = self.fish.avg_rows()

    def test_fish_market_filepaths_path_format(self) -> None:
        """
        Test if each entry is a string of format "path/to/the-file-etc.csv"
        :return:
        """
        expected = {
            "slash_count": self.directory_name.count("/") + 1,
            "dash_count": self.filename_prefix.count("-"),
            "file_extension": ".csv"
        }
        for actual in self.fish.fish_market_filepaths:
            self.assertIsInstance(actual, str)
            self.assertEqual(expected["slash_count"], actual.count("/"))
            self.assertTrue(expected["dash_count"] <= actual.split("/")[-1].count("-"))
            self.assertIn(expected["file_extension"], actual.split("/")[-1])

    def test_fish_market_filepaths_starts_with(self) -> None:
        """
        Test if all filepaths start with settings.filename_prefix (default: "fish-")
        :return:
        """
        expected = self.filename_prefix
        for actual in [path.split('/')[-1] for path in self.fish.fish_market_filepaths]:
            self.assertIn(expected, actual)

    def test_fish_market_filepaths_duplicates(self) -> None:
        """
        Test if there are any duplicates in the fish_market_filepaths list
        :return:
        """
        expected = 0
        actual = len(self.fish.fish_market_filepaths) - len(set(self.fish.fish_market_filepaths))
        self.assertEqual(expected, actual)

    def test_fish_market_filepaths_match(self) -> None:
        """
        Test if paths in fish_market_filepaths are also in self.files_at_the_dir
        :return:
        """
        expected = self.files_at_the_dir
        for actual in self.fish.fish_market_filepaths:
            self.assertIn(actual, expected)

    def test_upload_df_as_file_local(self) -> None:
        """
        Check if the file exists locally
        :return:
        """
        local_filename = self.fish.upload_df_as_file(
            self.avg_data_df,
            upload=False
        )
        self.assertTrue(os.path.exists(local_filename))


if __name__ == "__main__":
    unittest.main()
