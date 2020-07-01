import gym
import time
import numpy as np
from gym.envs.classic_control import rendering
def repeat_upsample(rgb_array, k=1, l=1, err=[]):
    # repeat kinda crashes if k/l are zero
    if k <= 0 or l <= 0: 
        if not err: 
            print(f"Number of repeats must be larger than 0, k: {k}, l: {l}, returning default array!")
            err.append('logged')
        return rgb_array

    # repeat the pixels k times along the y axis and l times along the x axis
    # if the input image is of shape (m,n,3), the output image will be of shape (k*m, l*n, 3)

    return np.repeat(np.repeat(rgb_array, k, axis=0), l, axis=1)

viewer = rendering.SimpleImageViewer()
env = gym.make('Pong-ram-v0')
env.reset()
action=0
while True:
    rgb = env.render('rgb_array')
    action = 2 # 2 for up, 3 for down
    env.step(3)[0]
    upscaled=repeat_upsample(rgb,5, 5)
    time.sleep(0.01)
    viewer.imshow(upscaled)
    observation, reward, done, info = env.step(action)