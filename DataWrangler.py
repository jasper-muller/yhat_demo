import pandas as pd


class DataWrangler(object):

    def read_data(self, some_id):
        """Reads the csv for some_id into a pandas DataFrame. Sets the index
        to type DateTimeIndex.
        """

        if not type(some_id) == str:
            some_id = str(some_id)

        filename = '{ID}.csv'.format(ID=some_id)
        df = pd.read_csv(filename)

        return self._set_datetime_index(df)

    def group_and_normalise(self, df):
        """Wrapper to group and normalise a DataFrame."""
        df = self.group_by_weekday(df)
        df['value'] = self.normalise(df)

        return df

    def normalise(self, df):
        """ Normalise a DataFrame."""
        v_max = max(df.value)
        v_min = min(df.value)

        return (df.value - v_min) / (v_max - v_min) * 100

    def group_by_weekday(self, df):
        """Group a DataFrame on weekday, hour, minute."""
        weekday_times = self._weekday_times(df)
        df_grouped = (df.groupby(weekday_times)
                        .median()
                        .reset_index()
                        .rename(columns={'level_0': 'day_of_week',
                                         'level_1': 'hour',
                                         'level_2': 'minute'}
                                )
                      )

        return df_grouped

    def _weekday_times(self, df):
        """Extract weekday, hour, and minute from DataFrame index."""
        return [df.index.weekday, df.index.hour, df.index.minute]

    def _set_datetime_index(self, df):
        """Set the timestamp column of a pandas Dataframe to be its index."""
        df['ts'] = pd.to_datetime(df['ts'], format='')
        df = df.set_index('ts')

        return df
