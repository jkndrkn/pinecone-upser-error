# pinecone-upsert-error

Code sample that exposes an error that happens when using the LangChain Pinecone vectorstore.


# Installation

1. Install Miniconda: https://docs.anaconda.com/free/miniconda/index.html

2. Install `python`, `pip`, and Python packages

   ```
   ./install.sh
   ```

3. Activate your Conda environment:

   ```
   conda activate pinecone-upsert-error
   ```

4. Create a Pinecone index with 768 dimensions and cosine metric for use with HuggingFace embeddings

5. Edit your `config.sh` to point to the correct Pinecone credentials.

# Testing

```
./load_documents.sh
```

When attempting trial 30 the following error is returned:

```
Traceback (most recent call last):
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 793, in urlopen
    response = self._make_request(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 491, in _make_request
    raise new_e
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 467, in _make_request
    self._validate_conn(conn)
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 1099, in _validate_conn
    conn.connect()
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connection.py", line 616, in connect
    self.sock = sock = self._new_conn()
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connection.py", line 205, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x7fe2590b3e80>: Failed to resolve 'answers-dev-jde-test-768-REDACTED.svc.us-east-1-aws.pinecone.io' ([Errno 8] nodename nor servname provided, or not known)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/jeriksen/bamboohr/ai-labs/pinecone-upsert-error/load_document.py", line 23, in <module>
    PineconeStore.from_documents(docs, embedder, index_name=INDEX_NAME)
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/langchain_core/vectorstores.py", line 508, in from_documents
    return cls.from_texts(texts, embedding, metadatas=metadatas, **kwargs)
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/langchain_community/vectorstores/pinecone.py", line 434, in from_texts
    pinecone.add_texts(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/langchain_community/vectorstores/pinecone.py", line 157, in add_texts
    [res.get() for res in async_res]
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/langchain_community/vectorstores/pinecone.py", line 157, in <listcomp>
    [res.get() for res in async_res]
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/multiprocessing/pool.py", line 774, in get
    raise self._value
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/multiprocessing/pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/pinecone/core/client/api_client.py", line 195, in __call_api
    response_data = self.request(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/pinecone/core/client/api_client.py", line 454, in request
    return self.rest_client.POST(url,
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/pinecone/core/client/rest.py", line 301, in POST
    return self.request("POST", url,
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/pinecone/core/client/rest.py", line 178, in request
    r = self.pool_manager.request(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/_request_methods.py", line 144, in request
    return self.request_encode_body(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/_request_methods.py", line 279, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/poolmanager.py", line 444, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 877, in urlopen
    return self.urlopen(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 877, in urlopen
    return self.urlopen(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 877, in urlopen
    return self.urlopen(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
  File "/Users/jeriksen/opt/anaconda3/envs/pinecone-upsert-error/lib/python3.10/site-packages/urllib3/util/retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='answers-dev-jde-test-768-REDACTED.svc.us-east-1-aws.pinecone.io', port=443): Max retries exceeded with url: /vectors/upsert (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7fe2590b3e80>: Failed to resolve 'answers-dev-jde-test-768-REDACTED.svc.us-east-1-aws.pinecone.io' ([Errno 8] nodename nor servname provided, or not known)"))
```
