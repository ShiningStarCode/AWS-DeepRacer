#This reward function implements the suggestions by penalizing the agent for going off-track, 
# rewarding the agent for driving at high speeds, rewarding the agent for following the center line, 
# and decreasing the penalty for sharp turns when going fast. Note that the values used here 
# (e.g. the penalties, bonuses, and multipliers) are just examples, and you may need to adjust them 
# based on the specifics of your race track and the behavior of your agent.

def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    
    reward = 1e-3
    
    # penalty for going off-track
    if not all_wheels_on_track:
        reward = -1.0
        
    # bonus for high speed
    elif speed > 10:
        reward += 0.5 * (speed - 10)
        
    # bonus for following the center line
    elif distance_from_center <= track_width/2:
        reward += 0.5 * (track_width/2 - distance_from_center)
        
    # decrease the penalty for sharp turns
    elif speed > 5 and steering_angle > 30:
        reward *= 1.5
    
    return float(reward)

