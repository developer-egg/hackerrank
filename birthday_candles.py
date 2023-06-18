def birthday_candles(candles):
    tallest_candle = candles[0]

    for candle in candles:
        if candle > tallest_candle:
            tallest_candle = candle

    tallest_candle_count = 0

    for candle in candles:
        if candle == tallest_candle:
            tallest_candle_count += 1

    return tallest_candle_count

birthday_candles([3, 2, 1, 3])