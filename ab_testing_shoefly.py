##import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

views_from_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()
print(views_from_source)

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.is_click.head())

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns="is_click", index="utm_source", values="user_id").reset_index()
print(clicks_pivot)

clicks_pivot["percent_clicked"] = clicks_pivot.apply(lambda row: (float(row[True])/(row[True] + row[False])) * 100, axis=1)
print(clicks_pivot)

experimental_group_count = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(experimental_group_count)

experimental_group_percent = ad_clicks.groupby(["is_click", "experimental_group"]).user_id.count().reset_index()
print(experimental_group_percent)

experimental_group_percent_pivot = experimental_group_percent.pivot(columns="is_click", index="experimental_group", values="user_id").reset_index()
print(experimental_group_percent_pivot)

experimental_group_percent_pivot["percent_clicked"] = experimental_group_percent_pivot.apply(lambda row: (float(row[True])/(row[True] + row[False])) * 100, axis=1)
print(experimental_group_percent_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index(drop=True)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index(drop=True)
print(a_clicks.head())
print(b_clicks.head())

a_clicks_count = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()
print(a_clicks_count)

a_clicks_pivot = a_clicks_count.pivot(columns="is_click", index="day", values="user_id").reset_index()
a_clicks_pivot["percent_click"] = a_clicks_pivot.apply(lambda row: (float(row[True])/(row[True] + row[False])) * 100, axis=1)
print(a_clicks_pivot)

b_clicks_count = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()
print(b_clicks_count)

b_clicks_pivot = b_clicks_count.pivot(columns="is_click", index="day", values="user_id").reset_index()
b_clicks_pivot["percent_click"] = b_clicks_pivot.apply(lambda row: (float(row[True])/(row[True] + row[False])) * 100, axis=1)
print(b_clicks_pivot)
