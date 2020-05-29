# SPARQL-Endpoint
A simple and lightweight flask app to host your RDF graphs over a SPARQL Endpoint inspired from [rdflib-web](http://https://github.com/RDFLib/rdflib-web.com)
- Any input format of graph supported (see below)
- Tried and Tested with popular sparqlclients
    - [SPARQL-wrapper (python)](https://github.com/RDFLib/sparqlwrapper)
    - [Apache JENA Fuseki (ruby)](https://jena.apache.org/documentation/fuseki2/soh.html)
- Run natively or using docker
- Works for python3

## Graph Formats
The following graph formats are supported:  `html`, `hturtle`, `mdata`, `microdata`, `n3`, `nquads`, `nt`, `rdfa`, `rdfa1.0`, `trix`, `turtle/ttl`, `xml`.

## Starting the Server
Once you start your server using the below methods, your sparql endpoint will be available at `http:127.0.01:5001/sparql` and also your host address.

### Running Natively
You will have to set two environment variables:
- `GRAPH_FILE` as path to your rdf file.  
- `GRAPH_FORMAT` as format of your rdf file.

Then run the following commands.

```bash
pip install -r requirement.txt
python3 graph.py
```

### Running using Docker
```bash
 docker build -t sparqlserver .
 docker run -d -p 5001:5001 -e GRAPH_FILE=`path_to_your_rdf_file` -e GRAPH_FORMAT=`format_of_rdf_file` sparqlserver
```
