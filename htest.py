
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance_ez as yf
from yahoo_fin.stock_info import get_live_price
import flask
from flask import Flask, request, jsonify
from yahoo_earnings_calendar import YahooEarningsCalendar
import time

app = flask.Flask(__name__)

app.config["DEBUG"] = True  

yec=YahooEarningsCalendar()

START_DATE='1980-01-01'
END_DATE=str(datetime.now().strftime('%Y-%m-%d'))

def get_stats(stock_data):
	adj_close=clean_data(stock_data,'Adj Close')
	return {
	'last(1 Day Mean)':np.mean(adj_close.tail(1)),
	'short_mean(20 day mean)':np.mean(adj_close.tail(20)),
	'medium_mean (90 day mean)':np.mean(adj_close.tail(90)),
	'long_mean(200 day mean)':np.mean(adj_close.tail(200))
	#'short_rolling':stock_data.rolling(window=20).mean(),
	#'long_rolling':stock_data.rolling(window=200).mean()
	}
def clean_data(stock_data, col):
	weekdays=pd.date_range(start=START_DATE,end=END_DATE)
	clean_data=stock_data[col].reindex(weekdays)
	return clean_data.fillna(method='ffill')
def get_data(ticker):
	try:
		stock_data=data.DataReader(ticker,'yahoo',START_DATE,END_DATE)
		
		return(clean_data(stock_data,'Adj Close'))
	except RemoteDataError:
		print('No data found for{t}'.format(t=ticker))
def get_mean(ticker):
	try:
		stock_data=data.DataReader(ticker,'yahoo',START_DATE,END_DATE)
		return(get_stats(stock_data))
	except RemoteDataError:
		print('no data found for{t}'.format(t=ticker))
def get_info(ticker):
	stinfo=yf.Ticker('ticker')
	return(stinfo.info)
#def create_plot(stock_data,ticker):
	#stats=get_stats(stock_data)
#Equity Prices
microsoft_price=get_live_price('MSFT')
alibaba_price=get_live_price('BABA')
amazon_price=get_live_price('AMZN')
alphabet_price= get_live_price('GOOGL')
facebook_price= get_live_price('FB')
square_price= get_live_price('SQ')
ibm_price=get_live_price('IBM')
apple_price=get_live_price('AAPL')
sony_price=get_live_price('SNE')
dell_price=get_live_price('DELL')
abbott_price=get_live_price('ABT')
abbvie_price=get_live_price('ABBV')
allergan_price=get_live_price('AGN')
astrazeneca_price=get_live_price('AZN')
bristol_price=get_live_price('BMY')
johnson_price=get_live_price('JNJ')
merck_price=get_live_price('MRK')
novartis_price=get_live_price('NVS')
pfizer_price=get_live_price('PFE')
amgen_price=get_live_price('AMGN')
biogen_price=get_live_price('BIIB')
inovio_price=get_live_price('INO')
amd_price=get_live_price('AMD')

#industrials
dow_price=get_live_price('DOW')
honeywell_price=get_live_price('HON')
dupont_price=get_live_price('DD')
caterpilla_price=get_live_price('CAT')
m_price=get_live_price('MMM')
united_price=get_live_price('UTX')
boeing_price=get_live_price('BA')
cisco_price=get_live_price('CSCO')
depot_price=get_live_price('HD')
intel_price=get_live_price('INTC')
proctor_price=get_live_price('PG')
walmart_price=get_live_price('WMT')
raytheon_price=get_live_price('RTX')
#Energy
exxxon_price=get_live_price('XOM')
shell_price=get_live_price('RDS')
chevron_price=get_live_price('CVX')
bp_price=get_live_price('BP')
equinor_price=get_live_price('EQNR')
suncor_price=get_live_price('SU')
nextera_price=get_live_price('NEE')
exelon_price=get_live_price('EXC')
petrochina_price=get_live_price('PTR')
firstsolar_price=get_live_price('FSLR')
solaredge_price=get_live_price('SEDG')
terraform_price=get_live_price('TERP')
brp_price=get_live_price('BEP')
ormat_price=get_live_price('ORA')
#Currencies
eurusd_price=get_live_price('EURUSD=X')
gbpusd_price=get_live_price('GBPUSD=X')
bitcoin_price=get_live_price('BTCUSD=X')
ethereum_price=get_live_price('ETHUSD=X')
audusa_price=get_live_price('AUDUSD=X')
eurjpy_price=get_live_price('EURJPY=X')
jpy_price=get_live_price('JPY=X')
#gbpjpy_price=get_live_price('GPYJPY=X')
#Real Estate
spg_price=get_live_price('SPG')
brookfield_price=get_live_price('BPY')
redwood_price=get_live_price('RWT')
crown_price=get_live_price('CCI')
american_price=get_live_price('AMT')
prologis_price=get_live_price('PLD')
equinix_price=get_live_price('EQIX')
sba_price=get_live_price('SBAC')
#FINTECH
visa_price=get_live_price('V')
paypal_price=get_live_price('PYPL')
goldman_price=get_live_price('GS')
ameritrade_price=get_live_price('AMTD')
interactive_price=get_live_price('IBKR')
jpmorgan_price=get_live_price('JPM')
mastercard_price=get_live_price('MA')
wells_price=get_live_price('WFC-PL')
hsbc_price=get_live_price('HSBC-PA')
boa_price=get_live_price('BAC-PL')
#bankrate_price=get_live_price('RATE')
#firstdata_price=get_live_price('FDC')
amex_price=get_live_price('AXP')
equifax_price=get_live_price('EFX')
fico_price=get_live_price('FICO')
discover_price=get_live_price('NFS')
#worldpay_price=get_live_price('WP')
elevate_price=get_live_price('ELVT')
#experian_price=get_live_price('EXPN')
#envestnet_price=get_live_price('TDLE')
thomson_price=get_live_price('TRI')
aci_price=get_live_price('ACIW')
lendingtree_price=get_live_price('TREE')
nelnet_price=get_live_price('NNI')
ondeck_price=get_live_price('ONDK')

#Tickers
msft=yf.Ticker("MSFT")
amzn=yf.Ticker('AMZN')
aapl=yf.Ticker('AAPL')
fb=yf.Ticker('FB')
sq=yf.Ticker('SQ')
ibm=yf.Ticker('IBM')
dell=yf.Ticker('DELL')
sony=yf.Ticker('SNE')
baba=yf.Ticker('BABA')
goog=yf.Ticker('GOOGL') 
abt=yf.Ticker('ABT')
abbv=yf.Ticker('ABBV')
agn=yf.Ticker('AGN')
azn=yf.Ticker('AZN')
bmy=yf.Ticker('BMY')
jnj=yf.Ticker('JNJ')
mrk=yf.Ticker('MRK')
nvs=yf.Ticker('NVS')
pfe=yf.Ticker('PFE')
hon=yf.Ticker('HON')
dow=yf.Ticker('DOW')
dd=yf.Ticker('DD')
cat=yf.Ticker('CAT')
m=yf.Ticker('MMM')
united=yf.Ticker('UTX')
ba=yf.Ticker('BA')
csco=yf.Ticker('CSCO')
hd=yf.Ticker('HD')
intc=yf.Ticker('INTC')
pg=yf.Ticker('PG')
wmt=yf.Ticker('WMT')
rtx=yf.Ticker('RTX')
xom=yf.Ticker('XOM')
rds=yf.Ticker('RDS')
cvx=yf.Ticker('CVX')
bp=yf.Ticker('BP')
eqnr=yf.Ticker('EQNR')
su=yf.Ticker('SU'),
nee=yf.Ticker('NEE')
exc=yf.Ticker('EXC')
ptr=yf.Ticker('PTR')
spg=yf.Ticker('SPG') 
sectors = [
    {'type': 'tech',
    'companies':[
             {
                'name':'Amazon','ticker':'AMZN','Price': str(amazon_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMZN')))},
                {'name':'Alibaba','ticker':'BABA','Price':str(alibaba_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BABA')))},
                {'name':'Apple', 'ticker':'AAPL','Price':str(amazon_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AAPL')))},                
                {'name':'DELL', 'ticker':'DELL','Price':str(dell_price),'NextEarningsCall':'TBD'},
                {'name':'Microsoft', 'ticker':'MSFT','Price':str(microsoft_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('MSFT')))},
                {'name':'Alphabet', 'ticker':'GOOGL','Price':str(alphabet_price), 'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('GOOGL')))},
                {'name':'Facebook','ticker':'FB','Price':str(facebook_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('FB')))},
                {'name':'SONY', 'ticker':'SNE','Price':str(sony_price),'NextEarningsCall':'TBD'},
                {'name':'International Business Machines', 'ticker':'IBM','Price':str(ibm_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('IBM')))},
                {'name':'Intel','ticker':'INTC','Price':str(intel_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMZN')))},
                {'name':'Advanced Micro Devices','ticker':'AMD','Price':str(amd_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMD')))},             
            ]
        },
    {'type':'fintech',
    'companies':[
     			{'name':'VISA','ticker':'V','Price':str(visa_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('V')))},
     			{'name':'Paypal','ticker':'PYPL','Price':str(paypal_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('PYPL')))},
                {'name':'Goldman Sachs','ticker':'GS','Price':str(goldman_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('GS')))},
                {'name':'TD Ameritrade','ticker':'AMTD','Price':str(ameritrade_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMTD')))},
                {'name':'Interactive Brokers Group','ticker':'IBKR','Price':str(interactive_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('IBKR')))},
                {'name':'JPMorgan and Chase','ticker':'JPM','Price':str(jpmorgan_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('JPM')))},
                {'name':'Mastercard','ticker':'MA','Price':str(mastercard_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('MA')))},
                {'name':'Wells Fargo','ticker':'WFC','Price':str(wells_price),'NextEarningsCall':'N/A'},
                {'name':'HSBC','ticker':'HSBC','Price':str(hsbc_price),'NextEarningsCall':'N/A'},
                {'name':'Bank of America','ticker':'BAC','Price':str(boa_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BAC')))},
                {'name':'Square','ticker':'SQ','Price':str(square_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('SQ')))},
                #{'name':'Bankrate','ticker':'RATE','Price':str(bankrate_price)},
                #{'name':'First Data','ticker':'FDC','Price':str(firstdata_price)},
                {'name':'American Express','ticker':'AXP','Price':str(amex_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AXP')))},
                {'name':'Equifax','ticker':'EFX','Price':str(equifax_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('EFX')))},
                {'name':'FICO','ticker':'FICO','Price':str(fico_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('FICO')))},
                {'name':'Discover','ticker':'DFS','Price':str(discover_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('DFS')))},
                #{'name':'Worldpay','ticker':'WP','Price':str(worldpay_price)},
                {'name':'Elevate','ticker':'ELVT','Price':str(elevate_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ELVT')))},
                #{'name':'Experian','ticker':'EXPN','Price':str(experian_price)},
                #{'name':'Envestnet','ticker':'TDLE','Price':str(envestnet_price)},
                {'name':'Thomson Reuters','ticker':'TRI','Price':str(thomson_price),'NextEarningsCall':'N/A'},
                {'name':'ACI Worldwide','ticker':'ACIW','Price':str(aci_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ACIW')))},
                {'name':'Lending Tree','ticker':'TREE','Price':str(lendingtree_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('TREE')))},
                {'name':'Nelnet','ticker':'NNI','Price':str(nelnet_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('NNI')))},
                {'name':'Ondeck','ticker':'ONDK','Price':str(ondeck_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ONDK')))}
               ]
     },

    {'type': 'biopharma',
    'companies':[
             {
                'name':'Abbott','ticker':'ABT','Price':str(abbott_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ABT')))},
                {'name':'Abbvie','ticker':'ABBV','Price':str(abbvie_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ABBV')))},
                {'name':'Allergan','ticker':'AGN','Price':str(allergan_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AGN')))},
                {'name':'Astrazeneca','ticker':'AZN', 'Price':str(astrazeneca_price),'NextEarningsCall':'N/A'},
                {'name':'Bristol-Meyers','ticker':'BMY','Price': str(astrazeneca_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BMY')))},
                {'name':'Johnson and Johnson','ticker':'JNJ','Price':str(johnson_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('JNJ')))},
				{'name':'Merck','ticker':'MRK','Price':str(merck_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('MRK')))},
                {'name':'Novartis','ticker':'NVS','Price':str(novartis_price),'NextEarningsCall':'N/A'},
                {'name':'Pfizer','ticker':'PFE','Price':str(pfizer_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('PFE')))},
                {'name':'Amgen','ticker':'AMGN','Price':str(amgen_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMGN')))},
            	{'name':'Biogen','ticker':'BIIB','Price':str(biogen_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BIIB')))},
            	{'name':'Inovio','ticker':'INO','Price':str(inovio_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('INO')))}
            ]
    },
    {'type': 'industrials',
    'companies':[
             {  
                'name':'HoneyWell','ticker':'HON','Price':str(honeywell_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('HON')))},
                {'name':'DuPont','ticker':'DD','Price':str(dupont_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('DD')))},
                {'name':'DOW','ticker':'DOW','Price':str(dow_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('DOW')))},
                {'name':'M','ticker':'MMM','Price':str(m_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('MMM')))},
                {'name':'Caterpillar','ticker':'CAT','Price':str(caterpilla_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('CAT')))},
                {'name':'United Technologies','ticker':'UTX','Price':str(united_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('UTX')))},
                {'name':'Boeing','ticker':'BA','Price':str(boeing_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BA')))},
                {'name':'Cisco','ticker':'CSCO','Price':str(cisco_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('CSCO')))},
                {'name':'Home Depot','ticker':'HD','Price':str(depot_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('HD')))},
                {'name':'Proctor and Gamble','ticker':'PG','Price':str(proctor_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('PG')))},
                {'name':'Walmart','ticker':'WMT','Price':str(walmart_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('WMT')))},
                {'NAME':'Raytheon','ticker':'RTX','Price':str(raytheon_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('RTX')))}
                   
            ]
        },

    {'type':'energy',
    'companies':[
            {   
                'name':'Exxon','ticker':'XOM','Price':str(exxxon_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('XOM')))},
                {'name':'British Petroleum','ticker':'BP','Price':str(bp_price),'NextEarningsCall':'N/A'},
                {'name':'NextEra Energy','ticker':'NEE','Price':str(nextera_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('NEE')))},
                {'name':'Chevron','ticker':'CVX','Price':str(chevron_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('CVX')))},
                {'name':'Shell','ticker':'RDS','Price':str(shell_price),'NextEarningsCall':'N/A'},
                {'name':'Equinor','ticket':'EQNR','Price':str(equinor_price),'NextEarningsCall':'N/A'},
                {'name':'Suncor','ticker':'SU','Price':str(suncor_price),'NextEarningsCall':'N/A'},
                {'name':'Exelon','ticker':'EXC','Price':str(exelon_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('EXC')))},
                {'name':'First Solar','ticker':'FSLR','Price':str(firstsolar_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('FSLR')))},
                {'name':'Solar Edge','ticker':'SEDG','Price':str(solaredge_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('SEDG')))},
                {'name':'TerraForm Power','ticker':'TERP','Price':str(terraform_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('TERP')))},
                {'name':'Ormat','ticker':'ORA','Price':str(ormat_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('ORA')))},
                {'name':'Brookfield Renewable Partners','ticker':'BEP','Price':str(brp_price),'NextEarningsCall':'N/A'}

                
            ]
        },

    {'type': 'FOREX',
    'companies':[
                {'name':'EUR/USD','Price':str(eurusd_price)},
                {'name':'JPY','Price':str(jpy_price)},
                {'name':'GBP/USD','Price':str(gbpusd_price)},
                {'name':'AUD/USA','Price':str(audusa_price)},
                {'name':'EUR/JPY','Price':str(eurjpy_price)}
            ]
    },
    {'type':'REIT',
    'companies':[
            {'name':'Simon Property Group','ticker':'SPG','Price':str(spg_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('SPG')))},
            {'name':'Crown Castle','ticker':'CCI','Price':str(crown_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('CCI')))},
            {'name':'SBA','ticker':'SBAC','Price':str(sba_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('SBAC')))},
            {'name':'Brookfield','ticker':'BPY','Price':str(brookfield_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('BPY')))},
            {'name':'American Tower','ticker':'AMT','Price':str(american_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('AMT')))},
            {'name':'Prologis','ticker':'PLD','Price':str(prologis_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('PLD')))},
            {'name':'Equinix','ticker':'EQIX','Price':str(equinix_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('EQIX')))},
            {'name':'Redwood','ticker':'RWT','Price':str(redwood_price),'NextEarningsCall':(datetime.fromtimestamp(yec.get_next_earnings_date('RWT')))}
 
            
        ]
    },
    {'type': 'Crypto',
    'companies':[
    	    {'name':'Bitcoin','Price':str(bitcoin_price)},
            {'name':'Ethereum','Price':str(ethereum_price)}
   		]
    }
 ]
				

Technicals = [

	{'ticker':'AMZN','Stat':'Averages'},{'ticker':'AAPL','Stat':'Averages'},{'ticker':'BABA','Stat':'Averages'},{'ticker':'MSFT','Stat':'Averages'},{'ticker':'DELL','Stat':'Averages'},{'ticker':'FB','Stat':'Averages'},
	{'ticker':'SQ','Stat':'Averages'},{'ticker':'IBM','Stat':'Averages'},{'ticker':'SNE','Stat':'Averages'},{'ticker':'HP','Stat':'Averages'},{'ticker':'GOOG','Stat':'Averages'},{'ticker':'ABT','Stat':'Averages'},{'ticker':'ABBV','Stat':'Averages'},
	{'ticker':'AGN','Stat':'Averages'},{'ticker':'AZN','Stat':'Averages'},{'ticker':'JNJ','Stat':'Averages'},
	{'ticker':'PG','Stat':'Averages'},{'ticker':'BMY','Stat':'Averages'},{'ticker':'MRK','Stat':'Averages'},{'ticker':'NVS','Stat':'Averages'},
	{'ticker':'HON','Stat':'Averages'},{'ticker':'DD','Stat':'Averages'},{'ticker':'DOW','Stat':'Averages'},{'ticker':'PFE','Stat':'Averages'},{'ticker':'CAT','Stat':'Averages'},
	{'ticker':'UTX','Stat':'Averages'},{'ticker':'BA','Stat':'Averages'},{'ticker':'INTC','Stat':'Averages'},{'ticker':'HD','Stat':'Averages'},{'ticker':'WMT','Stat':'Averages'},
	{'ticker':'RTX','Stat':'Averages'},{'ticker':'MMM','Stat':'Averages'},{'ticker':'XOM','Stat':'Averages'},{'ticker':'RDS','Stat':'Averages'},{'ticker':'CVX','Stat':'Averages'},{'ticker':'BP','Stat':'Averages'},{'ticker':'EQNR','Stat':'Averages'},
	{'ticker':'SU','Stat':'Averages'},{'ticker':'NEE','Stat':'Averages'},{'ticker':'EXC','Stat':'Averages'},{'ticker':'AIG','Stat':'Averages'},
	{'ticker':'AXP','Stat':'Averages'},{'ticker':'AAL','Stat':'Averages'},{'ticker':'ALL','Stat':'Averages'},{'ticker':'ATVI','Stat':'Averages'},{'ticker':'ACN','Stat':'Averages'},
	{'ticker':'ALXN','Stat':'Averages'},{'ticker':'ADBE','Stat':'Averages'},{'ticker':'AMD','Stat':'Averages'},{'ticker':'T','Stat':'Averages'},
	{'ticker':'BBY','Stat':'Averages'},{'ticker':'ISRG','Stat':'Averages'},{'ticker':'AMGN','Stat':'Averages'},{'ticker':'APA','Stat':'Averages'},{'ticker':'APTV','Stat':'Averages'},{'ticker':'CSCO','Stat':'Averages'},{'ticker':'V','Stat':'Averages'},{'ticker':'VZ','Stat':'Averages'},{'ticker':'BRK.A','Stat':'Averages'},{'ticker':'PEP','Stat':'Averages'},
	{'ticker':'BIIB','Stat':'Averages'},{'ticker':'BXP','Stat':'Averages'},{'ticker':'AVGO','Stat':'Averages'},{'ticker':'CCL','Stat':'Averages'},{'ticker':'CVX','Stat':'Averages'},{'ticker':'JPM'},{'ticker':'C'},{'ticker':'CMCSA','Stat':'Averages'},{'ticker':'CVS','Stat':'Averages'},{'ticker':'ABT'},{'ticker':'ORCL','Stat':'Averages'},
	{'ticker':'DIS','Stat':'Averages'},{'ticker':'BAC','Stat':'Averages'},{'ticker':'PYPL','Stat':'Averages'},{'ticker':'DVN','Stat':'Averages'},{'ticker':'DAL','Stat':'Averages'},{'ticker':'KO','Stat':'Averages'},{'ticker':'SU'},{'ticker':'FDX','Stat':'Averages'},{'ticker':'EXC','Stat':'Averages'},{'ticker':'NEE','Stat':'Averages'},
	{'ticker':'PTR','Stat':'Averages'},{'ticker':'SPG','Stat':'Averages'},{'ticker':'TSLA','Stat':'Averages'},{'ticker':'FANG','Stat':'Averages'},{'ticker':'D','Stat':'Averages'},{'ticker':'DISH','Stat':'Averages'},{'ticker':'DPZ','Stat':'Averages'},{'ticker':'ETFC','Stat':'Averages'},{'ticker':'EQIX','Stat':'Averages'},{'ticker':'TM','Stat':'Averages'},
	{'ticker':'CRM','Stat':'Averages'},{'ticker':'TMO','Stat':'Averages'},{'ticker':'AMGN','Stat':'Averages'},{'ticker':'CHL','Stat':'Averages'},{'ticker':'COST','Stat':'Averages'},{'ticker':'TMUS','Stat':'Averages'},{'ticker':'NIKE','Stat':'Averages'},{'ticker':'NFLX','Stat':'Averages'},{'ticker':'NVDA','Stat':'Averages'},{'ticker':'TM','Stat':'Averages'},
	{'ticker':'UNH','Stat':'Averages'},{'ticker':'MA','Stat':'Averages'},{'ticker':'TSM','Stat':'Averages'},{'ticker':'WMT','Stat':'Averages'},{'ticker':'WBA'},{'ticker':'MCD','Stat':'Averages'}, {'ticker':'GS','Stat':'Averages'},{'ticker':'TM','Stat':'Averages'}
	]
			


@app.route('/')
def home():
    return "Hello! Welcome to Crisis Alpha. We are cool and smart. For Live Stock Prices by sector, navigate to /sectors/Type of Sector(tech,fintech,biopharma, energy, industrials, REIT, FOREX, Crypto) and then navigate to /company and this will display the live prices for all the prvoided companies in this sector.For Adjusted Close Histories since 1980, navigate to /Technicals/Any stock ticker in CAPITAL LETTERS. For stock price means, navigate to 'Averages' after the ticker. "

@app.route('/sectors/<string:type>')
def get_sector(type):
    for sector in sectors:
        if(sector['type']==type):
            return jsonify(sector['type'])
            return "Hello, this the home page for the Tech Sector. Below you will see live and historical percentage moves in this sector."
    return jsonify({'message:Store not found'})
@app.route('/sectors/<string:type>/company')
def get_sector_companies(type):
        # Check if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        for sector in sectors:
             if (sector['type']==type):
                return jsonify(sector['companies'])
        return jsonify({'message:Sector type not found'})
@app.route('/Technicals')
def tech():
	return "Please Type in a ticker to see Historicals, and then type in Stat if you would like time Averages"
@app.route('/Technicals/<string:ticker>')
def get_history(ticker):
    for Technical in Technicals:
        if(Technical['ticker']==ticker):
            return(str(get_data(Technical['ticker'])))
    return jsonify('no company specified')
@app.route('/Technicals/<string:ticker>/Earnings')
def get_company_book(ticker):
        # Chec if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        for Technical in Technicals:
             if (Technical['ticker']==ticker):
                return jsonify(book['Earnings'])
        return jsonify({'message:company type not found'})
@app.route('/Technicals/<string:ticker>/<string:Stat>')
def get_stat(ticker,Stat):
	for Technical in Technicals:
		if(Technical['ticker']==ticker) and (Technical['Stat']==Stat):
			return(str(get_mean(Technical['ticker'])))
	return jsonify('no stat')
@app.route('/Technicals/<string:ticker>/<string:Stat>/<string:info>')
def get_stock(ticker,Stat,info):
	for Technical in Technicals:
		if(Technical['ticker']==ticker) and (Technical['Stat']==Stat) and (Technical['info']==info):
			return(str(get_info(Technical['ticker'])))
	return jsonify('no info')

if __name__=='__main__':
	app.run()
#print(get_history('MSFT'))




# gstock info

