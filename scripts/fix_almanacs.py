"""
fix_almanacs.py

This script will iterate over each almanac in ../pelican/content/almanacs
and do various things to clean up almanac pages and remove unused files.
"""


HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ALMANACS = os.path.join(ROOT, 'pelican', 'content', 'almanacs')


gamedirs = sorted(glob.glob(os.path.join(ALMANACS, '*')))
for k, gamedir in enumerate(gamedirs):

    almanac_name = gamedir.split("/")[-1]

    print(f"Filtering almanac {almanac_name}")

    # File removal tasks:
    # - remove top level index.html

    # BeautifulSoup Tasks:
    # - filter game log page
    # - filter box score page

    # pelican theme tasks:
    # move the css hard-coded in index.html into a new css file
    # tinker with their styles.css in place, then copy to new file too when ready

    # game log page tasks:
    # - remove script sorttable.js
    # - replace their css with our own css
    #     - trim down their styles.css
    #     - include our slate/custom after their styles
    #     - include lobster font
    # - modify <table> (which contains... all page contents?)
    #     - removing a <tr> element
    #     - inserting our own custom content (???)
    #     - include a <header> just like on index.html page




    break

