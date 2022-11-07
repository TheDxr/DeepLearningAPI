from flask_restful import Resource
from flask import render_template


class TestView(Resource):
    def post(self):
        # if 'file' not in request.files:
        #     return redirect(request.url)
        # file = request.files.get('file')
        # if not file:
        #     return
        # img_bytes = file.read()
        # class_id, class_name = get_prediction(image_bytes=img_bytes)
        # class_name = format_class_name(class_name)
        # return render_template('result.html', class_id=class_id,
        #                        class_name=class_name)
        return render_template('index.html')
