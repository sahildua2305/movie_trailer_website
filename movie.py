# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-06-13 03:06:02
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-06-13 04:07:50

class Movie:
  """ Class for representing a movie having a bunch of information """

  def __init__(self, title, poster_url, trailer_url):
    self.title = title
    self.poster_image_url = poster_url
    self.trailer_youtube_url = trailer_url
