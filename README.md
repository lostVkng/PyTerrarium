# PyTerrarium
LED Control for Terrarium


Control the LEDs for my terrarium. Written in Python and ran on a Raspberry PI. 

Very bare bones. Works for the time being. Just a few cron jobs. 

*Note* This currently clears all cron jobs.


# Raspberry PI Setup
- Make sure timezone is correct
- set dtparam=spi=on in boot/config/txt


# Python Setup

Install libraries
```python
pip install -r requirements.txt
```


# Start Cron Jobs

Setup the cron jobs (from src dir)
Need sudo GPIO access
```shell
sudo python app.py
```
