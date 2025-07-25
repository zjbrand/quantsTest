import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成所有日期（2010-01-01 至 2024-12-31）
start_date = datetime(2010, 1, 1)
end_date = datetime(2024, 12, 31)
date_list = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# 设定周末休市（默认周六、周日不开市）
df = pd.DataFrame({'calendarDate': [d.strftime('%Y-%m-%d') for d in date_list]})
df['weekday'] = [d.weekday() for d in date_list]  # 0=周一, 6=周日
df['isOpen'] = np.where(df['weekday'] >= 5, 0, 1)  # 5=周六, 6=周日 -> 休市

# 设定中国主要节假日（2010-2024）
china_holidays = {
    "2010-01-01", "2010-02-13", "2010-02-14", "2010-02-15", "2010-02-16", "2010-02-17",
    "2011-01-01", "2011-02-02", "2011-02-03", "2011-02-04", "2011-02-05", "2011-02-06",
    "2012-01-01", "2012-01-22", "2012-01-23", "2012-01-24", "2012-01-25",
    "2013-01-01", "2013-02-09", "2013-02-10", "2013-02-11", "2013-02-12", "2013-02-13",
    "2014-01-01", "2014-01-31", "2014-02-01", "2014-02-02", "2014-02-03", "2014-02-04",
    "2015-01-01", "2015-02-18", "2015-02-19", "2015-02-20", "2015-02-21", "2015-02-22",
    "2016-01-01", "2016-02-07", "2016-02-08", "2016-02-09", "2016-02-10",
    "2017-01-01", "2017-01-27", "2017-01-28", "2017-01-29", "2017-01-30",
    "2018-01-01", "2018-02-15", "2018-02-16", "2018-02-17", "2018-02-18",
    "2019-01-01", "2019-02-04", "2019-02-05", "2019-02-06", "2019-02-07",
    "2020-01-01", "2020-01-24", "2020-01-25", "2020-01-26", "2020-01-27",
    "2021-01-01", "2021-02-11", "2021-02-12", "2021-02-13", "2021-02-14",
    "2022-01-01", "2022-01-31", "2022-02-01", "2022-02-02", "2022-02-03",
    "2023-01-01", "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24",
    "2024-01-01", "2024-02-09", "2024-02-10", "2024-02-11", "2024-02-12"
}

# 设定节假日休市
df.loc[df['calendarDate'].isin(china_holidays), 'isOpen'] = 0

# 移除辅助列
df = df[['calendarDate', 'isOpen']]

# 保存为 CSV
csv_filename = "china_stock_market_calendar.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"CSV 文件已生成: {csv_filename}")
