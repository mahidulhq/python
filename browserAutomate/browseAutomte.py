import webbrowser as wb

def webauto():
    chrome_path = '/snap/bin/chromium %s'
    # the default location is for linux & snap. you are in windows you need to find the .exe file
    # then put the location here. %u = opening in new windows, %s = opening in new tabs.


    URLS = (
            "https://www.github.com/mahidulhq",
            "https://mahidulhq.github.io/"
    )
    for url in URLS:
        print("opening : "+ url)

        # -->for manually choosen browser
        # wb.get(chrome_path).open(url)

        wb.open_new_tab(url) 
        # --> open links on your default browser autometically.

webauto()