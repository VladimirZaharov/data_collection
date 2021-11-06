import pandas as pd
from requests import get
import matplotlib.pyplot as plt

#динамика госдолга России

urls = [
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210923T0100-structure-20210923T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210818T0100-structure-20210818T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210716T0100-structure-20210716T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210617T0100-structure-20210617T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210513T0100-structure-20210513T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210415T0100-structure-20210415T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200922T0101-structure-20200922T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200922T0100-structure-20200922T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200819T0100-structure-20200819T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200721T0100-structure-20200721T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200618T0100-structure-20200618T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200519T0100-structure-20200519T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200424T0100-structure-20200424T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200318T0100-structure-20200318T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200221T0100-structure-20200221T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20200124T0100-structure-20200124T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20191218T0100-structure-20191218T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20191119T0100-structure-20191119T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20191018T0100-structure-20191018T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210216T0100-structure-20210216T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210211T0100-structure-20210211T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20210119T0100-structure-20210119T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20201215T0100-structure-20201215T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20201120T0100-structure-20201120T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20201026T0100-structure-20201026T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190918T0100-structure-20190918T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190816T0100-structure-20190816T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190722T0100-structure-20190722T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190618T0100-structure-20190618T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190523T0100-structure-20190523T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190424T0100-structure-20190424T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190321T0100-structure-20190321T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20190221T0100-structure-20190221T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20181221T0100-structure-20181221T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20181123T0100-structure-20181123T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20181023T0100-structure-20181023T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20180918T0100-structure-20180918T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20180817T0100-structure-20180817T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20180720T0100-structure-20180720T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20180619T0100-structure-20180619T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20180524T0100-structure-20180524T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170921T0101-structure-20170921T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170823T0101-structure-20170823T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170721T0101-structure-20170721T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170622T0101-structure-20170622T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170519T0101-structure-20170519T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170421T0101-structure-20170421T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170323T0101-structure-20170323T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170220T0101-structure-20170220T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20170131T0101-structure-20170131T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20161220T0101-structure-20161220T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20161125T0101-structure-20161125T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20161027T0102-structure-20161027T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160926T0102-structure-20160926T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160822T0102-structure-20160822T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160721T0102-structure-20160721T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160527T0102-structure-20160527T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160425T0102-structure-20160425T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160220T0102-structure-20160220T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20160125T0102-structure-20160125T0100.csv',
'https://data.gov.ru/opendata/7710168360-externaldebt/data-20151221T0102-structure-20151221T0100.csv'
]
dict = {}
for url in urls:
    df = pd.read_csv(url,sep=',')
    total = df['Эквивалент млн. евро']
    total = total.map(lambda a: a.replace(' ',''))
    total = total.astype(float)
    name = df['Отчетная дата']
    name = name.iloc[1]
    dict[name] = int(total.sum())
print(dict)