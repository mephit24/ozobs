from page_objects.price import Price

link = "https://www.ozon.ru/product/15-6-noutbuk-maibenben-m555-amd-ryzen-5-5500u-2-1-ggts-ram-16-gb-ssd-512-gb-amd-radeon-graphics-973977704/?advert=SLplb50v3sRdm3Ydd-m4GtwbCpCy5KgVgPE8Zpgds-bFgVXg0N_g-UDoG6wkebEOaiy7WbJ_sBSu-F_kBetg4h9IndY1ckWQhK_9x0_fchcumOsGfRg6Tpyu-MpmWRpMj_GRdwcwixjG5AkejPSz69gYnbQ9aY2Ofk620hcFuJNI0TD60EPFrFkyyAJJIEGxJI8exNxPM9U1qT9ea0zBwZ310M4J8JPL57cV6rK9xgAu7j9PooFmekA&avtc=1&avte=2&avts=1687080154&sh=5fg7IIMqqw"

# sum = 0   
# for i in range(10):   
#     t1 = time.time()
z = Price("https://ya.ru")
print(z.now)
#     t2 = time.time()
#     sum = sum + (t2 - t1)
#     time.sleep(10)
# print(sum / 10)