#An example of a reward function that prioritizes staying within the borders of the track

def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    reward = 1e-3 # Initial small reward

    # Reward for staying on the track
    if all_wheels_on_track:
        if distance_from_center <= track_width/2:
            reward = 1 # Stay within borders
        else:
            reward = 0.5 # Near the border

    return float(reward)

#In the above example, the vehicle is given a base reward of 1 if it is staying within the borders 
#(distance_from_center <= track_width/2), and 0.5 if it is near the border (distance_from_center > track_width/2). 
#If the vehicle goes off track, the reward is set to the initial small value of '1e-3.'
#This incentivizes the vehicle to stay within the borders of the track and not go off track.