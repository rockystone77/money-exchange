def exchange(currency = "usd", date_ = "2021-07-23"):
    ## korean bank site that shows exchange data
    url = "https://kebhana.com/cms/rate/wpfxd651_01i_01.do"
    ## payload data 
    payload = {"ajax": "true",
            "curCd": "",
            "tmpInqStrDt": "2021-09-06",
            "pbldDvCd": "0",
            "pbldSqn": "",
            "hid_key_data": "",
            "inqStrDt": "20210906",
            "inqKindCd": "1",
            "hid_enc_data": "",
            "requestTarget": "searchContentDiv"}
    ## add date to the payload
    payload['tmpInqStrDt'] = date_
    ## add date to the payload
    payload['inqStrDt'] = date_.replace("-", "")
    ## request from the website
    r = requests.post(url, data=payload)
    ## panda the html 
    a = pd.read_html(r.text)[0]
    ## get rid of stacked columns
    a.columns = ["_".join(set(x)) for x in a.columns]
    ## return the exchange rate using a mask 
    return a[a['통화'].str.contains(currency.upper())]['매매기준율'].values[0]
