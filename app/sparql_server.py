from flask import Flask, request, Response
from rdflib import Graph, plugin
import sys
from config import GRAPH_FILE, GRAPH_FORMAT


app = Flask(__name__)

def resultformat_to_mime(format): 
    if format=='xml': return "application/sparql-results+xml"
    if format=='json': return "application/sparql-results+json"
    if format=='html': return "text/html"
    return "text/plain"

def get_format_and_mimetype(accept_headers, output_format):

    if not output_format:
        output_format = "xml"
        if "text/html" in a:
            output_format = "html"
        if "application/sparql-results+json" in a:
            output_format = "json"
        
    mimetype = resultformat_to_mime(output_format)
    mimetype = request.values.get("force-accept", mimetype)

    return output_format, mimetype

@app.route('/sparql')
def sparql_endpoint():
    query = request.args.get('query')
    accept_headers = request.headers["Accept"]
    output_format = request.values.get("output", None)
    
    output_format, mimetype = get_format_and_mimetype(accept_headers, output_format)

    res = graph.query(query).serialize(format = output_format)
    response = Response(res)
    response.headers["Content-Type"] = mimetype

    return response

if __name__ == "__main__":
    graph = Graph()
    graph.parse(GRAPH_FILE, format=GRAPH_FORMAT)
    app.run(host='0.0.0.0',port=5001)


