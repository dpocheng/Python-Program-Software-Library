#   If today's price is above today's moving average
#       and yesterday's price is not above yesterday's moving average
#       then BUY
#   If today's price is below today's moving average
#       and yesterday's price is not below yesterday's moving average
#       then SELL
#
#   5-day directional indicator ranges from -5 to +5
#   Calculate the direction of change every day (-1, 0 or +1)
#      -1 mean today price is lower than yesterday
#       0 mean no change
#      +1 mean today price is higher than yesterday
#   5-day directional indicator is the sum of the most recent 5 directions of change
#
#   Buy  Threshold +2    BUY  whenever directional indicator crosses above +2
#   Sell Threshold  0    SELL whenever directional indicator crosses below  0

import http.client
import urllib.request
import urllib.error

URL = 'http://ichart.yahoo.com/table.csv?s=GOOG&a=2&b=1&c=2011&d=10&e=30&f=2012&g=d'
stock_list = []

def user_interface() -> None:
    while True:
        #url =  _choose_url()
        url = URL.strip()
        if len(url) == 0:
            return
        else:
            _download_and_print_url(url)
            break

def _choose_url():
    print('Choose a URL to download (press Enter or Return to quit)')
    return input('URL: ').strip()

def _download_and_print_url(url: str) -> None:
    response = None
    try:
        response = urllib.request.urlopen(url)
        _print_url_contents(response)
    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))
        print()
    finally:
        if response != None:
            response.close()

def _print_url_contents(response: http.client.HTTPResponse) -> None:
    content_bytes = response.read()
    content_string = content_bytes.decode(encoding='utf-8')
    content_lines = content_string.splitlines()
    print('Response contains {} line(s) of text'.format(len(content_lines)))
    print()
    for line in content_lines:
        #print(line)
        lines = line.split(',')
        stock_list.append(lines)
    print(stock_list[3][1])
    print()
    print()

if __name__ == '__main__':
    user_interface()
