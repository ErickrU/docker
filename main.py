import web
render= web.template.render("templates/")
urls = (
    '/','inicio',
    '/docker','docker',
    '/ubuntu','ubuntu'
)
app = web.application(urls, globals())

class inicio:
    def GET(self):
        return render.index()

class docker:
    def GET(self):
        return render.docker()

class ubuntu:
    def GET(self):
        return render.ubuntu()

if __name__ == "__main__":
    app.run()