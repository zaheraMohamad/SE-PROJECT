Securities Trading System version 2.0 11/05/2018

General Usage notes:
---------------------------------------------
-This aplication written in python 3
-This system stores all the information using files which must be supplied as arguments when the system is invoked
-It may be used by Traders(staff in the firm) or Clients(of the firm) by way of a command line tool to submit order to 
the market for execution.

----------------------------------------------
Installation notes:
-The following four files are needed for the correct execution of the system:
1-Config file: alpha.conf to configure the market data source(or server).In order to access the server you need own API:
https:www.alphavantage.co/

2-Clients file: clients.txt this file contains information about all clients.The format of the data is:
client_id:Client_name:email:positions
and	each	position	contains	the	following	format:	symbol|quantity|acquisition_date|modification_date 
An	example	entry	is	as	below:	 
1:Adil AlYasiri:A.AlYasiri@Salford.ac.uk:GOOG|516|2018/02/01|2018/05/01,MSFT|320|2018/02/01|2018/03/03,AAPL|375|2018/02/22|2018/02/22

3-Transaction file: trans.txt this file contains records of all transactions executed by the system
date_and_time|client_id|trans_type|symbol|ask_price|quantity 
Below	is	an	example:	
2018-02-22 22:41:46.243791|1|1|GOOG |1100.0000|201

4-Companies file: comanylist.txt this	file	contains	a	tab	separated	information	about	the	companies	enlisted	on	the	NASDAQ	stock	market.	The	first	line	of	the	file	contains	header	information.Example:	
Symbol	Name	Sector	industry
-Install pip using the commaned line:
Python -m pip install reQuests
 -Instal Pandas using the commaned line:
 pip install pandas
 ----------------------------------------------------------
 Phone: 0987767644
 Email: abc@edue.salford.co.uk