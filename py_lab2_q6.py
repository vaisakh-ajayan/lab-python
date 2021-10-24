import collections
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
d = dict(collections.OrderedDict(sorted(color_dict.items())))
print(d)