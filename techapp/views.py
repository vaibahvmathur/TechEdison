from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render_to_response

def index(request):
    log_data = []
    final_list = {}
    course_id_list = {}
    course_id_count = {}
    user_video_play = {}
    user_id_list = []
    data_lines = []
    with open('techapp/log.txt', 'rb') as f:
        for line in f:
            data_lines.append(line)
    data_logs = json.loads(json.dumps(data_lines))
    for log_unicode in data_logs:
        log_dict = json.loads(log_unicode)
        user_id = log_dict['context']['user_id']
        event_type = 1 if log_dict['event_type'] == 'play_video' else 0
        course_id = log_dict['context']['course_id']
        if not user_id in user_id_list:
            if user_id != "":
                user_id_list.append(user_id)
                if course_id != "":
                    course_id_list.update({user_id: [course_id]})
        else:
            if user_id != "":
                if course_id != "":
                    if not course_id in course_id_list[user_id]:
                        course_id_list[user_id].append(course_id)
        if user_id in user_video_play:
            if event_type:
                total_play = user_video_play[user_id]
                new_total_play = total_play + 1
                user_video_play[user_id] = new_total_play
        else:
            if user_id != "":
                if event_type:
                    new_item = {user_id: int(1)}
                else:
                    new_item = {user_id: int(0)}
                user_video_play.update(new_item)
    for i in course_id_list:
        course_id_count.update({i: len(course_id_list[i])})
    for i in user_id_list:
        temp = []
        temp.append(user_video_play[i])
        temp.append(course_id_count[i])
        final_list.update({i: temp})
    log_data.append(final_list)
    return render_to_response(
            'log.html', {
                'log_data': final_list,
            })