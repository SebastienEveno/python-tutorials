import csv
import matplotlib.pyplot as plt
from datetime import datetime

if __name__ == "__main__":
    # filename = 'data/sitka_weather_07-2018_simple.csv'
    filename = 'data/sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get high temperatures from this file
        highs = []
        dates = []
        lows = []
        for row in reader:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            highs.append(int(row[5]))
            lows.append(int(row[6]))
        print(highs)
    
    # Plot the high temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    plt.title("Daily high temperatures, 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()