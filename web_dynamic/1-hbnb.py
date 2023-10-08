#!/usr/bin/python3
"""
Integrates with static HTML Template
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after the request, this method calls .close() to close
    current SQLAlchemy Session
    """
    storage.close()


@app.route('/1-hbnb')
def hbnb_filters(the_id=None):
    """
    this function handles request to
    templates with states, cities & amentities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    app run on port
    """
    app.run(host=host, port=port)
