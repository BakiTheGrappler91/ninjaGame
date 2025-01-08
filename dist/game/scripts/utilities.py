import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path): # load single image function
    img = pygame.image.load(BASE_IMG_PATH + path).convert() # load an image
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path): # listdir method lists the files in the folder given by path
        images.append(load_image(path + '/' + img_name)) # adds each individual image file to image list
    return images

class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False # if we don't want to continue our loop at any point
        self.frame = 0 # keeps track of where we are in our animation loop

    def copy(self): # function returns copy of images to be used for in-game animation
        return Animation(self.images, self.img_duration, self.loop) # getting

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
            # self.frame increases by 1 every frame. % prevents the self.frame from becoming larger than the length of self.images. having an index in the img function larger than the length of the list will throw an error
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            # min takes two values and returns the lower of the two
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self): # function returns images for particular animation
        return self.images[int(self.frame / self.img_duration)] # [] gives integer which selects image from self images. as number of frames increase, index will increase and the next image in the list will be selected giving th appearance of animation