from flask import Flask, request, jsonify, Response
import youtube

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/')
def index():
    return jsonify({
        'message': 'こんにちは、世界！'
    })

@app.route('/youtubeData')
def youtubeData():
    videoID = request.args.get('id')
    caption = youtube.getCaption(videoID=videoID)
    thumbnail = youtube.getThumbnail(videoID=videoID)
    thumbnail = youtube.encode_image_to_base64(thumbnail)
    
    data = {
        "caption": caption,
        "thumbnail": thumbnail
    }
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
