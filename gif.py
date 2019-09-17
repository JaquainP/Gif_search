from flask import Flask, render_template, request as flask_request, json
import requests
app = Flask(__name__)



@app.route('/')
def user_input():
    return render_template("form.html")


@app.route("/response", methods=["post"])
def response():
    search_term = flask_request.form.get("input")
    # set the apikey and limit
    apikey = "92MYINMWHIXI"  # test value
    lmt = 8

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = r.json()['results']
        gif_urls = []
        for gif_response in top_8gifs:
            gif_urls.append(gif_response['media'][0]['gif']['url'])

        return render_template('image_template.html', gif_urls=gif_urls)
        #return top_8gifs
    else:
        top_8gifs = None
        return "No gifs returned"

if __name__ == "__main__":
    app.run(debug=True)
