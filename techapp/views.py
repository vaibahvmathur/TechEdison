from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render_to_response

def index(request):
    final_list = {}
    course_id_list = {}
    course_id_count = {}
    user_video_play = {}
    user_id_list = []
    data_lines = []
    # Read the Log file
    with open('techapp/log.txt', 'rb') as f:
        for line in f:
            data_lines.append(line)
    # Get JSON data from log file
    data_logs = json.loads(json.dumps(data_lines))
    # Loop through JSON data
    for log_unicode in data_logs:
        log_dict = json.loads(log_unicode)
        # Get User ID , Event_type (play_video) and course_id
        user_id = log_dict['context']['user_id']
        event_type = 1 if log_dict['event_type'] == 'play_video' else 0
        course_id = log_dict['context']['course_id']
        # Check if user already exist in user list
        if not user_id in user_id_list:
            if user_id != "":
                #  If new user add to user list
                user_id_list.append(user_id)
                if course_id != "":
                    # update course list for new user
                    course_id_list.update({user_id: [course_id]})
        # If user already in user list
        else:
            if user_id != "":
                if course_id != "":
                    # if new course id wrt user id update course list wrt userid
                    if not course_id in course_id_list[user_id]:
                        course_id_list[user_id].append(course_id)
        # if user in video_play list
        if user_id in user_video_play:
            # if play_video event
            if event_type:
                # update video_play count by 1 for user
                total_play = user_video_play[user_id]
                new_total_play = total_play + 1
                user_video_play[user_id] = new_total_play
        # if New user
        else:
            if user_id != "":
                # if play_video event
                if event_type:
                    new_item = {user_id: int(1)}
                # if play_video event
                else:
                    new_item = {user_id: int(0)}
                # update video_play count wrt user
                user_video_play.update(new_item)
    # get course count for user wrt course list
    for i in course_id_list:
        course_id_count.update({i: len(course_id_list[i])})
    # get data organized for html
    for i in user_id_list:
        temp = []
        temp.append(user_video_play[i])
        temp.append(course_id_count[i])
        final_list.update({i: temp})
    return render_to_response(
            'log.html', {
                'log_data': final_list,
            })