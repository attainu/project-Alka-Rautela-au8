import datetime


def convertTime(epoch):
    l = len(epoch)
    new_timestamp = epoch
    if l > 10:
        new_timestamp = epoch[: 10] + '.'
        i = 10
        while i < l:
            new_timestamp += epoch[i]
            i += 1
    converted_time = datetime.datetime.fromtimestamp(
        float(new_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return converted_time
