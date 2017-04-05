from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import urllib2
from PIL import Image
import requests
from StringIO import StringIO
import numpy as np
import matplotlib.pyplot as plt

 
app = Flask(__name__)
 
@app.route('/')
def hi():
    return 'hello' 

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print request.form['MediaUrl0']

    response = requests.get(request.form['MediaUrl0'])
    img = Image.open(StringIO(response.content))
    img2 = np.array(img)
    
    print img2
    # making edits aw yeah
    img2[:,:,2] = 0

    plt.imshow(img2)

    # bin_counts, bin_edges = np.histogram(img2[:,:,0],10)
    # NOT WORKING
    bin_counts,bin_edges,patches = plt.hist(img2[:,:,0].ravel(),10)

    plt.show()
    
    resp = MessagingResponse()
    resp.message('Hello {}, we got your picture!'.format(number))

    return str(resp)
 
if __name__ == '__main__':
    app.run()