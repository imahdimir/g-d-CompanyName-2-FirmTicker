"""

  """

import json

from githubdata import GithubData
from mirutil.df_utils import save_as_prq_wo_index as sprq


class GDUrl :
    with open('gdu.json' , 'r') as fi :
        gj = json.load(fi)

    cur = gj['cur']
    src0 = gj['src0']
    trg = gj['trg']

gu = GDUrl()

class ColName :
    ipojd = 'IPO_JDate'
    ftic = 'FirmTicker'
    btic = 'BaseTicker'
    cnm = 'CompanyName'

c = ColName()

def main() :
    pass

    ##

    gd = GithubData(gu.trg)
    gd.overwriting_clone()
    ##
    df = gd.read_data()
    ##

    gds0 = GithubData(gu.src0)
    gds0.overwriting_clone()
    ##
    ds0 = gds0.read_data()
    ##

    ds0 = ds0[[c.btic, c.ftic]]
    ds0 = ds0.drop_duplicates()
    ##
    ds0 = ds0.set_index(c.btic)
    ##

    df['f'] = df[c.ftic].map(ds0[c.ftic])
    ##
    mks = df['f'].notna()

    df.loc[mks, c.ftic] = df.loc[mks, 'f']
    ##
    df = df.drop(columns=['f'])
    ##
    df = df.drop_duplicates()
    ##

    assert df[c.cnm].is_unique
    ##

    fp = gd.data_fp
    sprq(df, fp)
    ##
    msg = 'gov by: '
    msg += gu.cur
    ##

    gd.commit_and_push(msg)

    ##

    gd.rmdir()
    gds0.rmdir()


    ##


    ##

##
if __name__ == '__main__' :
    main()

##
