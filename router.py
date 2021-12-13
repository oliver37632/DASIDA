
from flask import Blueprint
from flask_restful import Api

bp = Blueprint("gramo", __name__, url_prefix="")
api_basic = Api(bp)

from view.auth import Login
api_basic.add_resource(Login, "/login")

from view.auth import Auth
api_basic.add_resource(Auth, "/auth")

from view.auth import SigUp
api_basic.add_resource(SigUp, "/signup")

from view.post import Post
api_basic.add_resource(Post, "/post")

from view.post import DeletePost
api_basic.add_resource(DeletePost, "/post/<int:id>")

from view.post import GetPosts
api_basic.add_resource(GetPosts, "/post")

from view.comment import PostComment
api_basic.add_resource(PostComment, "/comment_post")

from view.comment import GetComment
api_basic.add_resource(GetComment, "/comment_get")

from view.post import PutPost
api_basic.add_resource(PutPost, "/post/<int:id>")