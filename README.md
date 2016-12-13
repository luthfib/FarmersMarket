This is an example of a simple web API implemented using
[Flask](http://flask.pocoo.org/) and
[Flask-RESTful](http://flask-restful.readthedocs.org/en/latest/).

To run it:

1. Install required dependencies:
   ```
   $ pip install -r requirements.txt
   ``` 
   [Flask](http://flask.pocoo.org/docs/0.10/installation/#installation)
   and
   [Flask-RESTful](http://flask-restful.readthedocs.org/en/latest/installation.html) to run `server.py` 
   and [RDFLib](http://rdflib.readthedocs.org/en/latest/) and [JSONLD for RDFLib](https://github.com/RDFLib/rdflib-jsonld) to run the `extractdata.py` script or the `another-server.py` service.

2. Run the helpdesk server:
   ```
   $ python server.py
   ```
   Alternatively, you can access the service running here: http://aeshin.org:5555/requests
   
3. Use the `extractdata.py` script to examine the triples found in various representations of the helpdesk resources.
   
   RDFa/microdata for the list of help requests:
   ```
   $ python extractdata.py http://aeshin.org:5555/requests
   ```
   JSON-LD for the list of help requests:
   ```
   $ python extractdata.py http://aeshin.org:5555/requests.json
   ```
   RDFa/microdata for an individual help request:
   ```
   $ python extractdata.py http://aeshin.org:5555/request/fhs6jo
   ```
   JSON-LD for an individual help request:
   ```
   $ python extractdata.py http://aeshin.org:5555/request/fhs6jo.json
   ```

4. Run the contacts server for an example of a service calling another service:
   ```
   $ python another-server.py
   ```
   Alternatively, you can access the service running here: http://aeshin.org:5556/contacts.json
   
   
   
   Types and Properties: 
   
   title/Local Businesss : This describes a schema defintion under place that describes a local businesss  http://schema.org/LocalBusiness
   
   description: Description of the obejct, in the case a farm market http://schema.org/description
   
   time: Time in which the farm resouce was created  http://schema.org/dateCreated
   
   item: Any offered product or service.In this case it is the items being sold by the farm  https://schema.org/Product
   
   
   Classes
   
   Create: Used a create classs that was used to create farms and producs
   
   Create-button-class was used to create new instances of the product text field so that farmers can add mulitple things to thier farm
   
   
   
   
   
