import re


def will_get_news(yesterday, day_before):
    yesterday_close_price = float(yesterday['4. close'])
    day_before_close_price = float(day_before['4. close'])
    percent_diff = (yesterday_close_price - day_before_close_price) / day_before_close_price
    return percent_diff


# as per recommendation from @freylis, compile once only
# CLEANR = re.compile('<.*?>')
def cleanhtml(raw_html):
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext


def get_msg_content(percent_diff, headline, brief):
    if percent_diff > 0.1:
        msg_content = f"TSLA: 🔺{percent_diff*100}%\n" \
                      f"Headline: {headline}\n" \
                      f"Brief: {brief}"
        return msg_content
    elif percent_diff < -0.1:
        msg_content = f"TSLA: 🔻{percent_diff*-100}%\n" \
                      f"Headline: {headline}\n" \
                      f"Brief: {brief}"
        return msg_content
    else:
        return -1
