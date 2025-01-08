import random

class Cloud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        # gets position of rendered clouds. *self.depth gives parallax effect as offset is reduced
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))
        # blits cloud onto surface. % allows looping effect for graphics. cloud will go off one side of screen and appear on the other

class Clouds: # class stores all of our clouds
    def __init__(self, cloud_images, count=16):
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))
        # add clouds to self.clouds. position in the x and y are random, random choice of cloud images for each cloud, speed range: 0.05 - 0.1, depth range 0.2 - 0.8 close clouds move faster than distant clouds due to offset * self.depth
        self.clouds.sort(key=lambda x: x.depth)
        # sort(key) renders clouds closest to the foreground first

    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)