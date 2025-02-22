#!/usr/bin/python3
"""
Flask App
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    this method calls .close() on
    the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/100-hbnb/')
def hbnb_filters(the_id=None):
    """
    custom template with states, cities & amentities
    """
    states = storage.all('State').values()
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('100-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    app.run(host=host, port=port)
