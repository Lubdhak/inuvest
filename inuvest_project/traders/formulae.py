import pandas as pd

# c high
# d low
# e close



def tr(df):
    # =MAX((C3 - D3), ABS(C3 - E2), ABS(D3 - E2))
    i = 0
    TR_l = [0]
    while i < df.index[-1]:
        TR = max(df.loc[i + 1, 'High'], df.loc[i, 'Close']) - min(df.loc[i + 1, 'Low'], df.loc[i, 'Close'])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l,name='TR')
    return TR_s

def pdm1(df):
        # =IF(
        # (C4-C3)>(D3-D4),
        # MAX((C4-C3),0)
        # ,0)
    i = 0
    pdm1_l = []
    while i < df.index[-1]:
        if (df.loc[i + 1, 'High'] - df.loc[i, 'High']) > (df.loc[i, 'Low'] - df.loc[i + 1, 'Low']):
            pdm1_l.append(df.loc[i + 1, 'High'] - df.loc[i, 'High'])
        else :
            pdm1_l.append(max((df.loc[i + 1, 'High'] - df.loc[i, 'High']),0))
        i = i + 1
    pdm1_s = pd.Series(pdm1_l, name='+DM1')
    return pdm1_s




