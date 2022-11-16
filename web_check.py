from tkinter import StringVar
from aiohttp import ClientSession
import asyncio
from urllib.parse import urlparse
from requests.exceptions import MissingSchema
import re
import speedtest
import requests


def fill_address_elements(core_address, domain='.com', protocol="https://www."):
    # using the default option
    return protocol + str(core_address) + domain


def check_site_address(site):
    checklist = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(checklist, site) is not None:
        return True
    else:
        return False


def check_site(site) -> bool:
    # response = requests.get(site)
    try:
        response = requests.get(site)
        if 200 <= response.status_code <= 400:
            return True
        else:
            asyncio.run(site_is_online(site))
    except MissingSchema:
        return False


async def site_is_online(site, timeout=2):
    error = Exception('unknown error')
    parser = urlparse(site)
    host = parser.netloc or parser.path.split('/')[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("Timed out")
            except Exception as e:
                error = e
    return False  # alt. raise error


def get_speed(DspeedVar: StringVar, UspeedVar: StringVar):
    speed = speedtest.Speedtest()
    down, up = humansize(speed.download()), humansize(speed.upload())
    DspeedVar.set("Download Speed: " + down)
    UspeedVar.set("Upload Speed: " + up)


def humansize(nbytes: float):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# def main():
#     speed = DoubleVar()
#     print(get_speed(speed))
#
#
# if __name__ == '__main__':
#     main()
