import httpx
from dataclasses import dataclass, field
from typing import List
from random import choice

@dataclass
class Scraper:
    useragent: List[str] = field(default_factory=lambda: [
        'Mozilla/5.0 (Wayland; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.137 Safari/537.36 Ubuntu/22.04 (5.0.2497.35-1) Vivaldi/5.0.2497.35',
        'Mozilla/5.0 (Wayland; Linux x86_64; System76 Galago Pro (galp2)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36 Ubuntu/22.04 (5.0.2497.48-1) Vivaldi/5.0.2497.48',
        'Mozilla/5.0 (Wayland; Linux x86_64; System76 Galago Pro (galp2)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36 Ubuntu/22.04 (5.0.2497.51-1) Vivaldi/5.0.2497.51,',
        'Mozilla/5.0 (Wayland; Linux x86_64; System76) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36 Ubuntu/22.04 (5.2.2623.34-1) Vivaldi/5.2.2623.39',
        'Mozilla/5.0 (Wayland; Linux x86_64; System76) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.92 Safari/537.36 Ubuntu/22.04 (5.2.2623.34-1) Vivaldi/5.2.2623.34'
    ])
    def fetch(self, url):
        child_headers = {
            'User-Agent': choice(self.useragent),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://health.usnews.com/best-hospitals/search',
            # 'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjY3MTM0NiIsImFwIjoiMTgzNDgzMjkwOSIsImlkIjoiMTgyNjcwNThiNjJiMmQ3YSIsInRyIjoiMDFkY2I2ZDI3ZjVkYmMzZTU0OTczMmRiOGU2NmI2MjAiLCJ0aSI6MTY3OTUxNzU5NDY0Mn19',
            # 'traceparent': '00-01dcb6d27f5dbc3e549732db8e66b620-18267058b62b2d7a-01',
            # 'tracestate': '671346@nr=0-1-671346-1834832909-18267058b62b2d7a----1679517594642',
            'Connection': 'keep-alive',
            # 'Cookie': 'usn_visitor_id=65090572254d0000375c1b64dc020000340e0000; _abck=6B2B5F561BC7DFC9D0AAC5B52EE53E3C~0~YAAQZQkFcv7JP+SGAQAA0V/0Cgl9rDyK6M1a5JdOdM8FMiTLFgPBqefo2nAnluXOum9lR7+bRve4Z5XGacLs8vkXaS95LQHwGFu+q/iu3+3vTGYpn1tzHAVLEZZ9Y5hnisoGjKRu6UCPNHWyXvZhFlSUhdmafYdXNoCPaHSvXlbd5cMhgrkHGBxtyQbcG+9yKggf9hWiJ0Yskx92+zMa9GxvRV3sYg8Q0rlRUNCmfzJGSCuNq+dktQQHqT0O53nE+P+uAD6fFp06BufnfkiXzBLXpb7GdO+XqV5z4RyV7k50YMfCySD4zdp51hdv6jqI6VveMeqw/dsLDi1zcChmhsX3xVudtlAjuMopsGm2VP+i2SNds10kDEXXjh7X4/x/zxUG4HhREDuPZNH4fmJBpVoCDgRqHF0V~-1~-1~-1; ak_bmsc=194D065CAD45EBE2D2706CBBB511BBAE~000000000000000000000000000000~YAAQZQkFckTAP+SGAQAAwFPgChPhMp7w/hab1rAgCdDWade4GcD5la/PnXpYnc5+A8ZVoeYwwNM71ZdrSh6d88ASHvKWY6LSSLsrXw0XQ6HH0DWZLZSpGW2YsyWs+z3AR1Ly3qGlOncG8QK6BOD5lTfQ0J/OV0u5OP+wFmGs9QO3gghuwG+z1/gHQixXT1IQiPH9JYeCy60faFzaXWOuRjQgNNWpzhpATCW6iM+R30mDxLbfRHi360KvllsPILyqRq7+8txB8PO/H0SUcexZvS53G1MQGat4hnC9Od4ubU7AvQ8qIFgA7eT1ryN2q/zzlUdZvV2b4kBFT60PEH3rLz2kwDzddjGwycS+N645E7zJxl5nIGjtegTSqpzSR/u8Z4CzWWMUXkwEIpp0uxXZkJzUT6Ca19hY7F8RFyUIC5NTweoW3WPvwiUjMviF+vEaMwCKTerbt1vaFLoTglNhL+YJfNef7VPYyzg227oZkmXW1O6i7bQUthh7sg==; bm_sz=C676EDDA236EBC711706B24538352E7D~YAAQZQkFcibAP+SGAQAAtDngChNu4UhZ416k0g91Yaf2m/gFSjOvEs44IqQ6hthtKUqNJzGwbpkPVSIQDBSUQZWjaVBNhwdez9/6DUNk7hKgNz5IVBBUBrpm2oCsudhYOUhts14vyqWr+GtQs5Yed0llNCjtygyTXTpr0Db8sOWoNrNco1yEpAkgRyaTAQRi9dHZ8CVWKksKwg6iq50D6Z8s8oZ4Nw+wMnXwA+XgRquadpC365dSE2dhJTuL03FDanD/ixRhsQ70vDDfj8xgfRCH9rW8dncaKTD2xSAc07PQhcs=~3752752~4404279; usn_session_id=7951468507630963; cogv=health; utag_main=v_id:01870ae04f4300161660ff7e00520504e002f01100bd0$_sn:1$_ss:0$_pn:4%3Bexp-session$_st:1679518794101$ses_id:1679514685251%3Bexp-session$_prevpage:health.usnews.com%2Fbest-hospitals%2Fsearch%3Bexp-1679520594551; usprivacy=1YNY; _pbjs_userid_consent_data=3524755945110770; ntvSession={"id":7509533,"placementID":989621,"lastInteraction":1679516998136,"sessionStart":1679516998136,"sessionEndDate":1679590800000,"experiment":""}; ntv_as_us_privacy=1YNY; sailthru_pageviews=10; _ga_BFX9FJ22W4=GS1.1.7951468507630963.1.1.1679516996.0.0.0; _ga=GA1.2.1668083877.1679514687; RT="z=1&dm=usnews.com&si=90eadfd7-5934-4f5b-83ba-8c4bd4cb4d93&ss=lfk3ocl2&sl=4&tt=1ov9&bcn=%2F%2F684d0d4a.akstat.io%2F"; _gid=GA1.2.617764431.1679514688; _pubcid=31de6dba-7e86-4265-8667-3e054a553279; permutive-id=4b596f57-f929-49bb-b669-8a4cadc7c628; _ntv_uid=d5470338-09b5-49e5-8a36-8d03b3a193a2; _lr_retry_request=true; _lr_env_src_ats=false; cto_bundle=XP3QY19WRWxhTnZqSlpJMXhQSTNVT203WlpPMzVzQ3dYZWduQzlZYW84RlJuMTlUb3djV1FEMk1NZnBEbEtwaW9aaGFmUWd5d0NVOEglMkZrUGU2aWlPUEIwQ3VmZmJUbiUyRmxaNVZMSUxLb0hKSiUyRllDSUhRUm9MZHdEQ1pLZEZxNHh6MXNJQ0lCTWtNWHBtU3ZKc0tRQmFjT0VkR0ElM0QlM0Q; cto_bidid=g2nVml96aEMySGZ0VWxTMU1aNnljYndKTzN0bVd5WFREb09kbUNlUE5JdXQlMkJyJTJCYVQwTjBIWGdjclRhcSUyRlpxalR3dWIzVktGWUZFJTJGdE5HRjBHRHY4NTZzcU9HWHpyM3E3TG11U3ZESEU3dk9WN0owJTNE; panoramaId_expiry=1679601089842; _cc_id=d2e24d07578551a7fd830055be974e2d; pbjs-unifiedid=%7B%22TDID%22%3A%228cf201f5-1d15-46a2-9f07-22ab9e84cdd2%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-03-22T19%3A51%3A29%22%7D; _ce.s=v~d5b37410da19354696316fdcf90f0be3dff3ff2d~vpv~0~v11.cs~9709~v11nv~-4~v11.sla~1679517594632~v11.s~f206ae60-c8ea-11ed-9096-afa65ed6b0ce; cebs=1; oaudjs={"timestamp":1679516995133,"counter":4,"audiences":{"4":{"count":1,"propensity":0.5,"timestamp":1679514730446},"7":{"count":4,"propensity":1,"timestamp":1679516995133},"9":{"count":4,"propensity":1,"timestamp":1679516995133},"11":{"count":4,"propensity":1,"timestamp":1679516995133}}}; _ce.clock_event=1; _lr_geo_location=ID; _ce.clock_data=99%2C114.10.119.223%2C1; cebsp_=4; __gads=ID=7023e9e147e6cc79:T=1679514693:S=ALNI_MaOg1j6cXiUSii6OtlWfyXHROdGsQ; __gpi=UID=00000bde99fb62a1:T=1679514693:RT=1679514693:S=ALNI_MZ2ZvN8XcCvXGkKg1y0tQjdpG1aRg; _lr_sampling_rate=100; g_state={"i_p":1679521902171,"i_l":1}; bm_sv=00244DCDA42A21B1B1424CFB8752D250~YAAQZQkFcuHSP+SGAQAA+IYDCxPcva/7cNGB2GpYGKf5uBNog5xSTKRICX6LTIHiTJnSMBchLjneLwa0hQoP7ueJozSi5g2KPdt/P1JUTog6Q1FsRU0MJa728Br/ObY5eGUeBwC3o+qhAHbezv+o9I/silurKAlkMJjYOgO+5dQNq9qrDCGYtXovG/ZXB8yGQg3GhHtoHKo5je2ZmBkyTvwcWfx1uj2cDXbLmrd1WpDt1VtlL5tYAJUJmwperJzM~1; sailthru_visitor=e4a73e51-a118-4772-9277-9e06e8e4779b',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        parent_headers = {

        }


        with httpx.Client() as client:
            response = client.get(url, headers=child_headers)
        return response.json()

if __name__ == '__main__':
    s=Scraper()
    result = s.fetch('https://health.usnews.com/best-hospitals/search-data?page=1')
    print(result)