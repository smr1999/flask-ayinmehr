from app import app
from mod_blog.forms import SearchForm

@app.context_processor
def inject():
    search_blog_form = SearchForm()
    return dict(search_blog_form=search_blog_form)