def make_df(cols, ind):
    """Quicklu make a DataFrame"""
    data = {c: [str(c)+str(i) for i in ind]
               for c in cols}
    return pd.DataFrame(data, ind)
# make_df('ABC', range(3))


dic = {}
for c in 'ABC':
    dic[c] = [str(c) + str(i) for i in range(3)]
    print(dic)