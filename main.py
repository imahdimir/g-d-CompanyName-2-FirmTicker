"""

  """

import json

from githubdata import GithubData


class GDUrl :
    with open('gdu.json' , 'r') as fi :
        gj = json.load(fi)

    cur = gj['cur']
    trg = gj['trg']

gu = GDUrl()

class ColName :
    ipojd = 'IPO_JDate'
    ftic = 'FirmTicker'

c = ColName()

def main() :
    pass

    ##

    gd = GithubData(gu.trg)
    gd.overwriting_clone()
    ##
    df = gd.read_data()
    ##

    assert df[c.ftic].is_unique
    ##

    fp = gd.data_fp
    df.to_csv(fp , index = False)
    ##
    msg = 'gov by: '
    msg += gu.cur
    ##

    gd.commit_and_push(msg)

    ##


    gd.rmdir()


    ##


    ##

##
if __name__ == '__main__' :
    main()

##
