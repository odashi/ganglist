# -*- coding: utf-8; indent-tabs-mode: t; tab-width: 4 -*-
#
# settings.py
#

class Options:
	# default values for command-line options
	DEFAULT_WIDTH = 30
	DEFAULT_HEIGHT = 5
	DEFAULT_INTERVAL = 60
	DEFAULT_SHOWUSERS = True
	DEFAULT_INLINE = False

	# minimum values for command-line options
	MIN_WIDTH = 1
	MIN_HEIGHT = 1
	MIN_INTERVAL = 10

	# maximum values for command-line options
	MAX_WIDTH = 100
	MAX_HEIGHT = 100
	MAX_INTERVAL = 600


class Environment:
	# data directory
	DATADIR = '/project/nakamura-lab01/ganglist'

	# host list
	HOSTS = [
		"ahcclust01.naist.jp", "ahcclust02.naist.jp", "ahcclust03.naist.jp",
		"ahcclust04.naist.jp", "ahcclust05.naist.jp", "ahcclust06.naist.jp",
		"ahcclust07.naist.jp", "ahcclust08.naist.jp", "ahcclust09.naist.jp",
		"ahcclust10.naist.jp", "ahcclust11.naist.jp", "ahcclust12.naist.jp",
	]

