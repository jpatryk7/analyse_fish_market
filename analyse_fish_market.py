import boto3
import pandas as pd
import settings
import uuid


class AnalyseFishMarket:
    def __init__(self) -> None:
        """
        Use _find_fish_files to find all files in python directory in the AWS S3 bucket data-eng-resources that start
        with "fish-". Put all files' content in one dataframe.
        :return:
        """
        self.bucket_name = settings.bucket_name
        self.directory_name = settings.directory_name
        self.filename_prefix = settings.filename_prefix
        self.upload_path = settings.upload_path

        self.s3_client = boto3.client('s3')

        self.fish_market_filepaths = self._find_fish_files()
        self.fish_df = self._read_all_to_df(self.fish_market_filepaths)

    def _find_fish_files(self) -> list[str]:
        """
        Find all files starting with the filename_prefix - default "fish-".
        :return: list with all paths to files starting with the prefix
        """
        path_list = []
        for path in self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=self.directory_name)["Contents"]:
            if path["Key"].split('/')[-1].startswith(self.filename_prefix):
                path_list.append(path["Key"])
        return path_list

    def _read_all_to_df(self, filepath_list: list[str], *, local: bool = False) -> pd.DataFrame:
        """
        Read all .csv given files from the S3 bucket, convert each to dataframe and merge them together vertically.
        :param filepath_list: list with all paths to files starting with the prefix
        :param local: optional parameter - if set to true, function will search local machine for the files
        :return: dataframe with content of all .csv files at paths from the list
        """
        df_list = []
        for path in filepath_list:
            obj = pd.read_csv(path if local else self.s3_client.get_object(Bucket=self.bucket_name, Key=path)["Body"])
            df_list.append(obj)
        df = pd.concat(df_list)
        return df

    def avg_rows(self, key: str = "Species") -> pd.DataFrame:
        """
        Calculate avg value of each row
        :return: dataframe with avg value of each row of self.fish_df
        """
        avg_df = []
        for species in self.fish_df[key].unique():
            avg_df.append(self.fish_df[self.fish_df[key] == species].mean(numeric_only=True))
        return pd.DataFrame(avg_df, index=self.fish_df[key].unique()).transpose()

    def upload_df_as_file(self, df: pd.DataFrame, *, upload: bool = True) -> str:
        """
        Create a .csv file locally and upload it on cloud. Optionally remove the local .csv file after the operation is
        finished.
        :param df: dataframe to upload to the cloud as csv file
        :param upload: setting upload to False suppresses uploading the file to the cloud
        :return:
        """
        local_filename = "csv_dump/" + str(uuid.uuid4()) + ".csv"
        with open(local_filename, "w") as csv_file:
            df.to_csv(local_filename)

        if upload:
            self.s3_client.upload_file(Filename=local_filename, Bucket=self.bucket_name, Key=self.upload_path)

        return local_filename


if __name__ == "__main__":
    fish_market = AnalyseFishMarket()
    fish_market_avg = fish_market.avg_rows()
    fish_market.upload_df_as_file(fish_market_avg)
