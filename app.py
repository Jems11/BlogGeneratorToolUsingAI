from flask import Flask,render_template,request
import blog

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():

    if request.method == "POST":
        if 'form1' in request.form:
            blogTopicprompt = request.form["blogTopic"]
            blogT = blog.GenerateBlogTopiocs(blogTopicprompt)
            blogTopicIdeas = blogT.replace('\n','<br>')

        elif 'form2' in request.form:
            blogSectionprompt = request.form["blogSection"]
            blogT = blog.GenerateBlogSections(prompt=blogSectionprompt)
            blogSectionIdeas = blogT.replace('\n','<br>')
        
        elif 'form3' in request.form:
            blogSectionContentprompt = request.form["blogSectionContent"]
            blogT = blog.GenerateBlogContent(blogSectionContentprompt)
            blogSectionContent = blogT.replace('\n','<br>')

    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(port=8888,debug=True)
