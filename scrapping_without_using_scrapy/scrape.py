import argparse
import csv
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def get_funds_links(page):
    print('Getting all funds links...')
    links = set()
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'fund.aspx?id=' in url:
                links.add('http://www.funder.co.il/' + url)
    return links


def get_string(soup, str_id):
    res = soup.find('span', attrs={'id': 'ctl00_ContentPlaceHolder1_' + str_id})
    return res.text.strip()


def parse_fund(url, data):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    name = get_string(soup, 'fundName')
    num = get_string(soup, 'fundNum')
    daily = get_string(soup, 'day1')
    monthly = get_string(soup, 'monthB')
    yearly = get_string(soup, 'yearB')
    since_2016 = get_string(soup, 'LabelYear2016')
    since_2015 = get_string(soup, 'LabelYear2015')
    since_2014 = get_string(soup, 'LabelYear2014')
    since_2013 = get_string(soup, 'LabelYear2013')
    since_2012 = get_string(soup, 'LabelYear2012')
    since_2011 = get_string(soup, 'LabelYear2011')
    since_2010 = get_string(soup, 'LabelYear2010')
    since_2009 = get_string(soup, 'LabelYear2009')
    since_2008 = get_string(soup, 'LabelYear2008')
    last_7_days = get_string(soup, 'day7')
    last_14_days = get_string(soup, 'day14')
    last_30_days = get_string(soup, 'day30')
    last_90_days = get_string(soup, 'day90')
    last_180_days = get_string(soup, 'day180')
    last_365_days = get_string(soup, 'day365')
    last_730_days = get_string(soup, 'day730')
    last_1095_days = get_string(soup, 'day1095')
    cost = get_string(soup, 'Label4')
    sharp = get_string(soup, 'Label14')
    exposure = get_string(soup, 'Label6')

    data.append((name, num, daily, monthly, yearly,
                 since_2016, since_2015, since_2014, since_2013, since_2012, since_2011, since_2010, since_2009,
                 since_2008, last_7_days, last_14_days, last_30_days, last_90_days, last_180_days, last_365_days,
                 last_730_days, last_1095_days, cost, sharp, exposure))


def export_to_csv(csv_file, data):
    print('Exporting to csv...')
    with open(csv_file, 'a', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(
            ['name', 'num', 'daily', 'monthly', 'yearly', 'since_2016', 'since_2015', 'since_2014', 'since_2013',
             'since_2012', 'since_2011', 'since_2010', 'since_2009', 'since_2008', 'last_7_days', 'last_14_days',
             'last_30_days', 'last_90_days', 'last_180_days', 'last_365_days', 'last_730_days', 'last_1095_days',
             'cost', 'sharp', 'exposure'])
        for row in data:
            writer.writerow(make_csv_row(row))
    print('DONE!')


def make_csv_row(elements):
    row = list()
    for obj in elements:
        if isinstance(obj, dict):
            row += obj.values()
        else:
            row.append(obj)
    return row


def get_funds_data(urls_set):
    data = []
    for url in urls_set:
        print('Parsing...' + url)
        parse_fund(url, data)
    print('Finishing parsing ' + str(len(urls_set)) + ' Funds!')
    return data


def scrape_mutual_funds(output=None):
    page = BeautifulSoup(requests.get('http://www.funder.co.il/allInOne.aspx').text, 'html.parser')
    urls_set = get_funds_links(page)
    if output is not None:
        export_to_csv(output, get_funds_data(urls_set))
    else:
        print(get_funds_data(urls_set))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse all mutual funds in Funder!')
    parser.add_argument('-o', '--output_csv', help='Output CSV File', required=False)
    args = vars(parser.parse_args())
    scrape_mutual_funds(args['output_csv'])
