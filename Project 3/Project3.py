##  Pok On Cheng 74157306. ICS 32 Lab 1 Project 3

from collections import namedtuple
import datetime
import http.client
import urllib.request
import urllib.error

stock = namedtuple('stock', 'date open high low close volume adj_close')
stock_total = []
date_list = []
close_list = []
today = datetime.datetime.today()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
SIGNAL_MENU = '''
Please select 1 or 2 to preform action:
1. N-day simple moving average
2. N-day directional indicator

Option: '''

def user_interface() -> None:
    while True:
        SYMBOL = input("\nPlease enter the ticker symbol: ").strip().upper()
        if _check_empty(SYMBOL):
            continue
        url = _customize_url(SYMBOL)
        _download_and_store_url(url)
        break
    stock_total.sort()
    for lines in stock_total:
        date_list.append(lines.date)
        close_list.append(lines.close)
    if _check_data_exist(stock_total):
        while True:
            option = input(SIGNAL_MENU)
            if _check_option(option):
                continue
            _execute_option_and_print_final_report(SYMBOL, option)
            break
        print("\nThank you for using stock analysis program!\nGoodbye!")
    
def _customize_url(SYMBOL: str):
    while True:
        START_DATE = input("\nPlease enter the start date(YYYY-MM-DD): ").strip()
        if _check_empty(START_DATE) or _check_date_format(START_DATE) or _check_start_date(START_DATE):
            continue
        START_DATE_LIST = START_DATE.split('-')
        START_MONTH = int(START_DATE_LIST[1]) - 1
        START_DAY = int(START_DATE_LIST[2])
        START_YEAR = int(START_DATE_LIST[0])
        break
    while True:
        END_DATE = input("\nPlease enter the end date(YYYY-MM-DD): ").strip()
        if _check_empty(END_DATE) or _check_date_format(END_DATE) or _check_end_date(START_DATE, END_DATE):
            continue
        END_DATE_LIST = END_DATE.split('-')
        END_MONTH = int(END_DATE_LIST[1]) - 1
        END_DAY = int(END_DATE_LIST[2])
        END_YEAR = int(END_DATE_LIST[0])
        break
    URL = "http://ichart.yahoo.com/table.csv?s="+str(SYMBOL)+"&a="+str(START_MONTH)+"&b="+str(START_DAY)+"&c="+str(START_YEAR)+"&d="+str(END_MONTH)+"&e="+str(END_DAY)+"&f="+str(END_YEAR)+"&g=d"
    return URL

def _check_empty(in_put: str) -> bool:
    if not in_put:
        print("It's empty input. Please try again.")
        return True
    return False

def _check_date_format(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("The date you entered is invalid. Please enter as 'YYYY-MM-DD'.")
        return True
    return False

def _check_start_date(start_date: str) -> bool:
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    if start_date >= today:
        print("The start date you entered should be on or before today's date. Please try again.")
        return True
    return False

def _check_end_date(start_date: str, end_date: str) -> bool:
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    if (end_date >= today) or (end_date <= start_date):
        print("The start date you entered should be on or before today's date, and should be later than the start date. Please try again.")
        return True
    return False


def _check_option(option: str) -> bool:
    if option == "1":
        return False
    elif option == "2":
        return False
    else:
        print("The option you entered is invalid. Please try again.")
        return True

def _check_data_exist(stock_list: list) -> bool:
    if stock_list == []:
        return False
    return True

def _download_and_store_url(url: str) -> None:
    response = None
    try:
        response = urllib.request.urlopen(url)
        _store_url_contents(response)
    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}\n'.format(e.code))
    finally:
        if response != None:
            response.close()

def _store_url_contents(response: http.client.HTTPResponse) -> None:
    content_bytes = response.read()
    content_string = content_bytes.decode(encoding='utf-8')
    content_lines = content_string.splitlines()
    for line in content_lines:
        lines = line.split(',')
        if lines[0] != "Date":
            stock_total.append(stock(*lines))

class Indicator:
    def simple_moving_average(self, day) -> list:
        indicator_list = []
        for c1 in range(len(close_list)):
            if c1 <= day-2:
                indicator_list.append(" ")
            else:
                d1 = c1
                total = 0
                average = 0
                for i1 in range(day):
                    total += float(close_list[d1])
                    d1 -= 1
                average = total / day
                indicator_list.append(average)
        return indicator_list

    def directional_indicator(self, day) -> list:
        indicator_list = []
        indicator_list.append(0)
        temp_list = []
        temp_list.append("0")
        for t2 in range(len(close_list)):
            if t2 > 0:
                if close_list[t2] > close_list[t2-1]:
                    temp_list.append("+1")
                elif close_list[t2] < close_list[t2-1]:
                    temp_list.append("-1")
                elif close_list[t2] == close_list[t2-1]:
                    temp_list.append("0")
        n = 0
        for c2 in range(len(close_list)):
            if c2 > 0:
                m = ""
                if temp_list[c2] == "+1":
                    if n != day:
                        n += 1
                    if n == 0:
                        n += 1
                    indicator_list.append(n)
                elif temp_list[c2] == "-1":
                    if n != -day:
                        n -= 1
                    if n == 0:
                        n -= 1
                    indicator_list.append(n)
                elif temp_list[c2] == "0":
                    indicator_list.append(n)
        return indicator_list

class Signal:
    def simple_moving_average(self, indicator_list) -> list:
        signal_list = []
        buy_list = []
        sell_list = []
        for i1 in range(len(indicator_list)):
            if i1 > 0 and indicator_list[i1-1] != " ":
                if close_list[i1] > str(indicator_list[i1]) and close_list[i1-1] < str(indicator_list[i1-1]):
                    buy_list.append(i1)
                elif close_list[i1] < str(indicator_list[i1]) and close_list[i1-1] > str(indicator_list[i1-1]):
                    sell_list.append(i1)
            signal_list.append(" ")
        for b1 in buy_list:
            signal_list[b1] = "BUY"
        for s1 in sell_list:
            signal_list[s1] = "SELL"
        return signal_list

    def directional_indicator(self, indicator_list, buy, sell):
        signal_list = []
        buy_list = []
        sell_list = []
        for i2 in range(len(indicator_list)):
            if indicator_list[i2] > buy:
                if indicator_list[i2-1] <= buy:
                    buy_list.append(i2)
            elif indicator_list[i2] < sell:
                if indicator_list[i2-1] > sell:
                    sell_list.append(i2)
            signal_list.append(" ")
        for b2 in buy_list:
            signal_list[b2] = "BUY"
        for s2 in sell_list:
            signal_list[s2] = "SELL"
        return signal_list

i = Indicator()
s = Signal()

def _execute_option_and_print_final_report(SYMBOL: str, option: str) -> None:
    indicator_list = []
    signal_list = []
    if option == "1":
        while True:
            try:
                day = int(input("\nPlease enter the number of day for N: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")
        indicator_list = i.simple_moving_average(day)
        signal_list = s.simple_moving_average(indicator_list)
        print("\nSYMBOL: " + SYMBOL)
        print("STRATEGY: Simple moving average (" + str(day) + "-day)")
        print()
        print("{0:10} {1:10} {2:10} {3:10}".format("DATE", "CLOSE", "INDICATOR", "SIGNAL"))
        for p1 in range(len(date_list)):
            if indicator_list[p1] != " ":
                print("{0:10} {1:10} {2:3.2f}     {3:10}".format(date_list[p1], close_list[p1], float(indicator_list[p1]), signal_list[p1]))
            else:
                print("{0:10} {1:10} {2:10} {3:10}".format(date_list[p1], close_list[p1], indicator_list[p1], signal_list[p1]))

    elif option == "2":
        while True:
            try:
                day = int(input("\nPlease enter the number of day for N: "))
                buy = int(input("\nPlease enter a number for buy thresholds: "))
                sell = int(input("\nPlease enter a number for sell thresholds: "))
                break
            except ValueError:
                print("Invalid number. Please try again.")
        indicator_list = i.directional_indicator(day)
        signal_list = s.directional_indicator(indicator_list, buy, sell)
        for il in range(len(indicator_list)):
            instr = ""
            if indicator_list[il] > 0:
                instr = instr + "+" + str(indicator_list[il])
                indicator_list[il] = instr
        print("\nSYMBOL: " + SYMBOL)
        print("STRATEGY: Directional (" + str(day) + "-day), buy above +" + str(buy) + ", sell below " + str(sell))
        print()
        print("{0:10} {1:10} {2:10} {3:10}".format("DATE", "CLOSE", "INDICATOR", "SIGNAL"))
        for p2 in range(len(date_list)):
            print("{0:10} {1:10} {2:<10} {3:10}".format(date_list[p2], close_list[p2], indicator_list[p2], signal_list[p2]))

if __name__ == '__main__':
    user_interface()
