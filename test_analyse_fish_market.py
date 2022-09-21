import unittest
from analyse_fish_market import *


class TestAnalyseFishMarket(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fish_market_filepaths_start_with(self) -> None:
        """
        Test if all filepaths start with settings.filename_prefix (default: "fish-")
        :return:
        """
        pass

    def test_fish_market_filepaths_count(self) -> None:
        """
        Test if all filepaths start with settings.filename_prefix were found
        :return:
        """
        pass

    def test_fish_df_col_count(self) -> None:
        """
        Test if all columns were written to the dataframe
        :return:
        """
        pass

    def test_fish_df_col_names(self) -> None:
        """
        Check for correct column names
        :return:
        """
        pass

    def test_fish_df_row_count(self) -> None:
        """
        Test if all rows were written to the dataframe
        :return:
        """
        pass

    def test_avg_rows_col_count(self) -> None:
        """
        Test if all columns were written to the dataframe
        :return:
        """
        pass

    def test_avg_rows_col_names(self) -> None:
        """
        Check for correct column names
        :return:
        """
        pass

    def test_avg_rows_row_count(self) -> None:
        """
        Test if all rows were written to the dataframe
        :return:
        """
        pass

    def test_upload_df_as_file_on_cloud(self) -> None:
        """
        Check if the uploaded file exists on cloud in correct directory
        :return:
        """
        pass

    def test_upload_df_as_file_delete_local_true(self) -> None:
        """
        Check if the file was deleted in the project directory
        :return:
        """
        pass

    def test_upload_df_as_file_delete_local_false(self) -> None:
        """
        Check if the file exists locally
        :return:
        """
        pass
