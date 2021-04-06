# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from com.dev.webCraw.service.crawService import crawService

# test-Func.
def hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# web-Crawler Func.
def getSite(site):
    craw = crawService(site)
    craw.crawler()

# Main Func.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hi('PyCharm')
    getSite('bugs')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
