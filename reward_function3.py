#An example of a reward function that prioritizes preventing zig-zagging

def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])

    reward = 1e-3 # Initial small reward

    # Reward for staying on the track
    if all_wheels_on_track:
        if speed > 5 and steering_angle > 30:
            reward = 0.5 # Penalize sharp turns when going fast
        else:
            reward = 1 # Smooth driving

    return float(reward)

#In this example, the vehicle is given a base reward of 1 for smooth driving 
# (speed <= 5 or steering_angle <= 30), and 0.5 for sharp turns when going fast 
# (speed > 5 and steering_angle > 30). If the vehicle goes off track, 
# the reward is set to the initial small value of 1e-3. 
# This incentivizes the vehicle to avoid sharp turns when going fast and prevent zig-zagging.