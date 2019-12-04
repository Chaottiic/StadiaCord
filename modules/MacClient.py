import appscript
def Client():
    urls = appscript.app('Google Chrome').windows.tabs.URL()
    for r in urls:
        for t in r:
            if "https://stadia.google.com" in t:
                t = t.split('/')[-1]
                return t
