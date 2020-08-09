How to run:  

  python images.py  

Output contains obtained images data:  

{
  'fead82e39189d8aab9f8': {   'author': 'Taut Bonus',
                              'camera': 'Leica M10',
                              'cropped_picture': 'http://interview.agileengine.com/pictures/cropped/1206036548_72965063.jpg',
                              'full_picture': 'http://interview.agileengine.com/pictures/full_size/1206036548_72965063.jpg',
                              'tags': '#wonderfulday #nature #whataview '
                                      '#beautifulday #wonderfullife #view '
                                      '#beauty '},

  . . . . .

  'fec4da37d718dd330130': {   'author': 'Tremendous Culture',
                              'camera': 'Nikon D4s',
                              'cropped_picture': 'http://interview.agileengine.com/pictures/cropped/1203855847_72.jpg',
                              'full_picture': 'http://interview.agileengine.com/pictures/full_size/1203855847_72.jpg',
                              'tags': '#today #beautifulday #photography '
                                      '#wonderfulday #wonderfullife #photo '}
}

The images data are stored in the internal cache (no special DB is used)

Search endpoint (requirements item 7) is not implemented.
