from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 配置 MySQL 连接信息
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:CodeJump5@localhost/blog"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# 定义文章模型
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

# 创建数据库表（首次运行）
with app.app_context():
    db.create_all()

# 获取所有文章
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": p.id, "title": p.title} for p in posts])

# 获取单篇文章
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "文章不存在"}), 404
    return jsonify({"id": post.id, "title": post.title, "content": post.content})

# 创建新文章
@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(title=data["title"], content=data["content"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "文章创建成功"}), 201

# 运行服务器
if __name__ == '__main__':
    app.run(debug=True)
