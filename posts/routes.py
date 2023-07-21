from flask import request, jsonify
from . import posts_bp
from .controller import PostController
from ..utils.getTime import get_timestamp
from datetime import datetime


@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    text = data.get('text')
    lat = data.get('lat')
    lon = data.get('lon')
    time = datetime.now()

    if not text or not lat or not lon:
        return jsonify({'error': 'Invalid data provided'}), 400

    post = PostController.create_post(text, "({},{})".format(lat, lon), time)

    print(post)

    return jsonify({'post_id': post.id})


@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    query = request.args.to_dict(flat=False)
    if 'lat' in query.keys():
        lat = query['lat'][0]
    else:
        return jsonify({'error': 'Latitude not provided'}), 400
    if 'lon' in query.keys():
        lon = query['lon'][0]
    else:
        return jsonify({'error': 'Longitude not provided'}), 400

    page = 1
    if 'page' in query.keys():
        page = int(query['page'][0])

    post = PostController.get_posts("({},{})".format(lat, lon), page)

    print(post)

    res = ""
    for p in post:
        timestamp = p.time
        time = get_timestamp(timestamp)
        res += ("Post id : {} text : {} - {}".format(p.id, p.text, time) + "<br>")

    return res
