import boto3
import pandas as pd


class AnalyseFishMarket:
    def __init__(self) -> None:
        """
        Use _find_fish_files to find all files in python directory in the AWS S3 bucket data-eng-resources that start
        with "fish-". Put all files' content in one dataframe.
        :return:
        """
        self.fish_market_filepaths = []
        self.fish_df = pd.DataFrame()
        pass

    def _find_fish_files(self) -> list[str]:
        """
        Find all files starting with the filename_prefix - default "fish-".
        :return: list with all paths to files starting with the prefix
        """
        return [""]

    def _read_all_to_df(self, filepath_list: list[str]) -> pd.DataFrame:
        """
        Read all .csv given files from the S3 bucket, convert each to dataframe and merge them together vertically.
        :param filepath_list: list with all paths to files starting with the prefix
        :return: dataframe with content of all .csv files at paths from the list
        """
        return pd.DataFrame()

    def avg_rows(self) -> pd.DataFrame:
        """
        Calculate avg value of each row
        :return: dataframe with avg value of each row of self.fish_df
        """
        return pd.DataFrame()

    def upload_df_as_file(self, df: pd.DataFrame, delete_local: bool = False) -> None:
        """
        Create a .csv file locally and upload it on cloud. Optionally remove the local .csv file after the operation is
        finished.
        :param df: dataframe to upload to the cloud as csv file
        :param delete_local: optional flag that specifies if the locally created .csv should be removed after the
        opeartion is done
        :return:
        """
        pass
