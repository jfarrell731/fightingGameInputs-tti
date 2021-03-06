from os import sep

import collections

image_path = "assets/lmhp_lmhk.png"
coll = collections.OrderedDict([
                        ('p', (0,0,80,80)),
                        ('lp', (79,0,80,80)),
                        ('mp', (159,0,80,80)),
                        ('hp', (238,0,80,80)),
                        ('2p', (678,0,120,80)),
                        ('lpmp', (318,0,120,80)),
                        ('lphp', (438,0,120,80)),
                        ('mphp', (558,0,120,80)),
                        ('3p', (797,0,120,80)),
                        ('k', (918,0,80,80)),
                        ('lk', (999,0,80,80)),
                        ('mk', (1079,0,80,80)),
                        ('hk', (1158,0,80,80)),
                        ('2k', (1599,0,120,80)),
                        ('lkmk', (1238,0,120,80)),
                        ('lkhk', (1358,0,120,80)),
                        ('mkhk', (1478,0,120,80)),
                        ('3k', (1719,0,120,80))
])

_inputs = {
    image_path: coll
}
