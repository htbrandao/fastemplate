:warning: | **WORK IN PROGRESS** | :warning:
:---: | :---: | :---:

# FasTemplate

REST API example built using FastAPI.

# # Why?

I have reasons to believe that my cat is always adding more and more tuna to my groceries cart.

So I created this API to edit my shopcart and keep him on the outside. I also made a special endpoint to catch him!

# # What?

I wrote this as a **follow up** after your ['Hello, wolrd'](https://fastapi.tiangolo.com/tutorial/first-steps/) app.

I recommend that you use this repo as a reading material to go along with the official User Guide ([Tutorial](https://fastapi.tiangolo.com/tutorial/) and [Advanced](https://fastapi.tiangolo.com/advanced/))

The code here already uses a lot of tools and functionalities provided by the framework, it's well documented, it has **custom exceptions**, **test cases** and python code written using good practices while it ranges from simple `for loops` to (custom) `decorators`. I believe it is good material to go along whether you are just starting or close enough to a mid level fluency in Python.

The *main* dependencies are:

- `FastAPI`: Build the actual API endpoints
- `Sphinx`: Create our project documentation
- `Uvicorn` or `GUnicorn`: Launches our API
- `Pytest`: Run our tests

# # Content

This template covers the following features from the [main docs](https://fastapi.tiangolo.com/):

- Tutorial - User Guide

Template | Topic
:---: | :---
|✅| Tutorial - User Guide - Intro |
|✅| First Steps |
|✅| Path Parameters |
|✅| Query Parameters |
|✅| Request Body |
|✅| Query Parameters and String Validations |
|✅| Path Parameters and Numeric Validations |
|✅| Body - Multiple Parameters |
|✅| Body - Fields |
|✅| Body - Nested Models |
|✅| Declare Request Example Data |
|✅| Extra Data Types |
|✅| Cookie Parameters |
|✅| Header Parameters |
|✅| Response Model |
|✅| Extra Models |
|✅| Response Status Code |
|✅| Form Data |
|✅| Request Files |
|✅| Request Forms and Files |
|✅| Handling Errors |
|✅| Path Operation Configuration |
|✅| JSON Compatible Encoder |
|✅| Body - Updates |
|✅| Dependencies |
|✅| Security |
|✅| Middleware |
|✅| CORS (Cross-Origin Resource Sharing) |
|❌| SQL (Relational) Databases |
|✅| Bigger Applications - Multiple Files |
|❌| Background Tasks |
|✅| Metadata and Docs URLs |
|✅| Static Files |
|✅| Testing |
|✅| Debugging |

- Advanced User Guide

Template | Topic
:---: | :---
|✅| Advanced User Guide - Intro |
|✅| Path Operation Advanced Configuration |
|✅| Additional Status Codes |
|✅| Return a Response Directly |
|✅| Custom Response - HTML, Stream, File, others |
|❌| Additional Responses in OpenAPI |
|❌| Response Cookies |
|✅| Response Headers |
|❌| Response - Change Status Code |
|❌| Advanced Dependencies |
|❌| Advanced Security |
|✅| Using the Request Directly |
|✅| Using Dataclasses |
|✅| Advanced Middleware |
|❌| SQL (Relational) Databases with Peewee |
|❌| Async SQL (Relational) Databases |
|❌| NoSQL (Distributed / Big Data) Databases |
|❌| Sub Applications - Mounts |
|❌| Behind a Proxy |
|✅| Templates |
|❌| GraphQL |
|❔| WebSockets |
|❌| Events: startup - shutdown |
|❌| Custom Request and APIRoute class |
|❔| Testing WebSockets |
|❔| Testing Events: startup - shutdown |
|❔| Testing Dependencies with Overrides |
|❔| Testing a Database |
|❔| Async Tests |
|✅| Settings and Environment Variables |
|❌| Conditional OpenAPI |
|❔| Extending OpenAPI |
|❔| OpenAPI Callbacks |
|❌| Including WSGI - Flask, Django, others |

Description:

Symbol | Meaning
:--: | :--
❌| Not covered
✅ | Covered 
❔| Not yet

# # How?

- Clone:
```bash
git clone https://github.com/htbrandao/fastemplate.git
cd fastemplate/
```

- Prepare:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

- Run:
    - Uvicorn:
        ```bash
        uvicorn fastemplate:app --host 0.0.0.0 --port 8000 --reload
        ```
    - Docker:
        ```
        docker build . -t fastemplate:0.0.1 # only needed once
        docker run -p 8000:8000 -n fastemplate -d fastemplate:0.0.1
        ```

- Use:

Naviage to [`localhost:8000`](localhost:8000) and you will see some basic info:
```
{
    "APPLICATION":"FASTEMPLATE",
    "VERSION":"0.0.1",
    "API VERSION":"v1",
    "DOCUMENTATION":"/index.html",
    "@TIMESTAMP":"16-07-2021T11:48:31"
}
```

To interact with the API, go to **[localhost:8000/docs](localhost:8000)**, which will look like this:

![swagger](docs/_static/swagger_ex.png)

Check out both the documentation and source code on [localhost:8000/index.html](localhost:8000/index.html) or open `docs/_build/html/index.html`:

- Documentation

![docs](docs/_static/docs_ex.png)

- Source

![source](docs/_static/source_code_ex.png)

- Post usage:

You can and might use this as a template (or stepping stone) for **your** future projects.

Take over eveything and make it fit your needs.

Remember to update the **`Sphinx docs`** and your **`test cases`**!

# # TODO & FIXME:

- [ ] Create something using websocket
- [ ] Write test cases
- [ ] Update README images
- [ ] Update docs
