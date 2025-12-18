# Geobet
A python script that uses n2y0's api to let you predict the next pass of a satellite!

## Setup

1. Get a free API key from [N2YO](https://www.n2yo.com/api/)
2. Enter info like location and back-up NORAD (at the top of `Geobet.py`)
3. Ensure you have python 3.6+ installed
4. Install required dependencies: `requests` (`time` and `datetime` are built-in pyhton modules)
5. Run: `python Geobet.py`

## How to Play

1. Enter info like location and back-up NORAD (at the top of Geobet.py)
2. Run script
3. Enter API key and satellite's NORAD ID
4. Enter prediction
5. Viola!

## Example  
   
   Welcome to GeoBet!  
  
Please input your n2y0 API Key: YOUR_API_KEY  
Please input satellites NORAD ID (backup ID is: 25544):   
No NORAD ID was added, used 25544  
Please input what time you think the pass will occur...  
Year: 2025  
Month: 12  
Month day: 19  
Hour: 14  
Minute: 30  
Second: 0  

## Notices

-All times are in UTC  
-The script filters for passes with at least 11° elevation above the horizon  
-This program is not affiliated with www.n2yo.com or its API. It simply utilizes their free API access.  
