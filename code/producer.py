from kafka import KafkaProducer
from time import sleep
import boto3
import pandas as pd
import os

producer = KafkaProducer(bootstrap_servers='localhost:9092',api_version=(0,1,0))

#filename = "SPY_TICK_TRADE.csv"
#f = open(os.path.join(os.path.dirname(__file__),filename))

df = pd.read_csv('https://raw.githubusercontent.com/Colquida/Parcial3BD/main/SPY_TICK_TRADE.csv')

#VAR = 2315
for valor in df["PRICE"]:
        producer.send('quickstart-events', b'%d'%valor)
        sleep(2)
