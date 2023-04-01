import pygame as pg

import core.constants as const



def loadImage (path, useAlpha=False, expectedSize=None) :
	try:
		match useAlpha:
			case True  : img = pg.image.load(path).convert_alpha()
			case False : img = pg.image.load(path).convert()

	except FileNotFoundError:
		img = pg.image.load(const.NO_IMAGE_PATH).convert_alpha()

	if expectedSize:
		return pg.transform.scale(img, expectedSize)