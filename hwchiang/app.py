from flask import Flask, render_template


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/interests')
def interests():
    photos = [
        {'href': 'https://www.flickr.com/photos/johnmay0629/27001286083/in/album-72157668740523070/', 'filename': '001.jpg', 'caption': '黑部水壩'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/27511001622/in/album-72157668740523070/', 'filename': '002.jpg', 'caption': '馬籠宿'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/27000443114/in/album-72157668740523070/', 'filename': '003.jpg', 'caption': '飛驒牛壽司'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/27576694866/in/album-72157668740523070/', 'filename': '004.jpg', 'caption': '高山陣屋'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/27576783726/in/album-72157668740523070/', 'filename': '005.jpg', 'caption': '河童橋'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/27001449223/in/album-72157668740523070/', 'filename': '006.jpg', 'caption': '白川鄉 天守閣 展望台'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/25642761653/in/album-72157650241007415/', 'filename': '007.jpg', 'caption': '中正公園'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/23053158129/in/album-72157661844238785/', 'filename': '008.jpg', 'caption': '獅球嶺'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/23113079740/in/album-72157661844238785/', 'filename': '009.jpg', 'caption': '獅球嶺'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/21730761646/in/album-72157656831096854/', 'filename': '010.jpg', 'caption': '猴硐貓村'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/21134156074/in/album-72157656831096854/', 'filename': '011.jpg', 'caption': '猴硐貓村'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/21570012639/in/album-72157656831096854/', 'filename': '012.jpg', 'caption': '猴硐貓村'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/21568861250/in/album-72157656831096854/', 'filename': '013.jpg', 'caption': '猴硐貓村'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/21756843815/in/album-72157656831096854/', 'filename': '014.jpg', 'caption': '猴硐貓村'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/19040851945/in/album-72157652565299134/', 'filename': '015.jpg', 'caption': '奇美博物館'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/17275119851/in/album-72157650241007415/', 'filename': '016.jpg', 'caption': '台北某餐館'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/17112375307/in/album-72157650241007415/', 'filename': '017.jpg', 'caption': '基隆海洋廣場'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/16619700665/in/album-72157650978911651/', 'filename': '018.jpg', 'caption': '木柵動物園'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/16026663127/in/album-72157647883932934/', 'filename': '019.jpg', 'caption': '上野動物園'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/16025132820/in/album-72157647883932934/', 'filename': '020.jpg', 'caption': '上野動物園'},
        {'href': 'https://www.flickr.com/photos/johnmay0629/15590078734/in/album-72157647883932934/', 'filename': '021.jpg', 'caption': '上野動物園'},
    ]
    return render_template('interests.html', photos=photos)
