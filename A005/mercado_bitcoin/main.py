import datetime
from schedule import repeat, every, run_pending
import time
from mercado_bitcoin.ingestors import DaySummaryIngestor
from mercado_bitcoin.writers import DataWriter


#print(DaySummaryAPI('BTC').get_data(date=datetime.datetime(2021, 6, 21)))
#print(TradesAPI('BTC').get_data())
#print(TradesAPI('BTC').get_data(date_from=datetime.datetime(2021, 6, 20)))
#print(TradesAPI('BTC').get_data(date_from=datetime.datetime(2021, 6, 20), date_to=datetime.datetime(2021, 6, 21)))

# data = DaySummaryAPI('BTC').get_data(date=datetime.datetime(2021, 6, 21))
# writer = DataWriter('day_summary.json')
# writer.write(data)

#data = TradesAPI('BTC').get_data()
#writer = DataWriter('trades.json')
#writer.write(data)

if __name__ == "__main__":
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter,
        coins=['BTC', 'ETH'],
        default_start_date=datetime.date(2022,10,1)
    )

    #trades_ingestor = TradesIngestor(...)

    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()
        #trades_ingestor.ingest()

    while True:
        run_pending()
        time.sleep(0.5)