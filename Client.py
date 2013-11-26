#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#
# Copyright 2012 Netsco Inc.
# Copyright 2012 Minsu Kang
# Copyright 2013 Jioh L. Jung

from urllib import quote
from urllib2 import urlopen, Request, HTTPError
from base64 import b64encode

import hmac
import hashlib
import json
import re
import os

UCLOUD_API_KEY = 'YOU_MUST_ENTER_YOUR_API_KEY_HERE_!'
UCLOUD_SECRET  = 'YOU_MUST_ENTER_YOUR_SECRET_KEY_HERE_!'
if "UCLOUD_API_KEY" in os.environ:
    UCLOUD_API_KEY = os.environ["UCLOUD_API_KEY"]
if "UCLOUD_SECRET" in os.environ:
    UCLOUD_SECRET = os.environ["UCLOUD_SECRET"]

UCLOUD_API_URLS = {
    # Server/CloudStack http://developer.ucloudbiz.olleh.com/doc/cloudstack/
    'server' : 'https://api.ucloudbiz.olleh.com/server/v1/client/api',
    # Loadbalancer http://developer.ucloudbiz.olleh.com/doc/loadbalancer/
    'lb'     : 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api',
    # Web Application Firewall http://developer.ucloudbiz.olleh.com/doc/waf/
    'waf'    : 'https://api.ucloudbiz.olleh.com/waf/v1/client/api',
    # Watch http://developer.ucloudbiz.olleh.com/doc/watch/
    'watch'  : 'https://api.ucloudbiz.olleh.com/watch/v1/client/api',
    # Packaging http://developer.ucloudbiz.olleh.com/doc/packaging/
    'package': 'https://api.ucloudbiz.olleh.com/packaging/v1/client/api',
    # AutoScaling http://developer.ucloudbiz.olleh.com/doc/autoscaling/
    'as'     : 'https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api',
    # CDN http://developer.ucloudbiz.olleh.com/doc/CDN/
    'cdn'    : 'https://api.ucloudbiz.olleh.com/cdn/v1/client/api',
    # Messaging http://developer.ucloudbiz.olleh.com/doc/messaging/
    'msg'    : 'https://api.ucloudbiz.olleh.com/messaging/v1/client/api',
    # NAS Service http://developer.ucloudbiz.olleh.com/doc/nas/
    'nas'    : 'https://api.ucloudbiz.olleh.com/nas/v1/client/api',
    # uCloud DB/RDBAAS http://developer.ucloudbiz.olleh.com/doc/DB/
    'db'     : 'https://api.ucloudbiz.olleh.com/db/v1/client/api',
}

class Client(object):
    def __init__(self, api_type = 'server', api_key=UCLOUD_API_KEY, secret=UCLOUD_SECRET):
        self.api_url = UCLOUD_API_URLS[api_type]
        self.api_key = api_key
        self.secret  = secret

    def request(self, command, args={}, post=None, debug=False, resptype="json"):
        if not command:
            raise RuntimeError('Command Missing !!')

        args['command']  = command
        args['response'] = resptype
        args['apiKey']   = self.api_key
        
        # For safty reason, force Quote some character.
        for i in args.keys():
            args[i] = args[i].replace("%", "%26")
            args[i] = args[i].replace("/", "%2f")

        query = '&'.join(
            '='.join([k, quote(args[k])]) for k in sorted(args.keys(), key=str.lower))
        
        signature = b64encode(hmac.new(
                self.secret,
                msg=query.lower(),
                digestmod=hashlib.sha1
        ).digest())

        if debug:
            print "Server: '%s'" % (self.api_url)
            print "Query (for Signiture):"
            print query
            print "Sigature:"
            print signature

        #-------------------------------------------------------
        # reconstruct : command + params + api_key + signature
        #-------------------------------------------------------
        query = '='.join(["command", quote(args["command"])]) + '&'
        args.pop("command")

        api_key = '='.join(["apiKey", quote(args["apiKey"])])
        args.pop("apiKey")

        query += '&'.join(
            '='.join([k, quote(args[k])]) for k in sorted(args.keys()))

        query += '&' + api_key
        query += '&signature=' + quote(signature)

        if debug:
            print "Query (Reconstructed/LEN: %d):" % len(query)
            print query
        #-------------------------------------------------------

        urls = self.api_url + '?' + query
        if post is not None:
            post_enc = '&'.join(
                '='.join([k, quote(post[k])]) for k in sorted(post.keys()))
            req_data = Request(urls, post_enc)
            req_data.add_header('Content-type', 'application/x-www-form-urlencoded')
            if debug:
                print "POST(DICT/LEN: %d): " % (len(post)) , post
                print "POST(Encrypted/LEN: %d): " % (len(post_enc)) , post_enc
                print "HEADERS: ", req_data.headers
        else:
            req_data = Request(urls)

        try:
            response = urlopen(req_data)
        except HTTPError as e:
            # Printing Debugging Indformation.
            print e.read()
            raise RuntimeError("%s" % e)

        content = response.read()

        if resptype != "json":
            return content

        decoded  = json.loads(content)

        # response top node check
        response_header = command.lower() + 'response'
        if not response_header in decoded:
            if 'errorresponse' in decoded:
                raise RuntimeError(
                    "ERROR: " + decoded['errorresponse']['errortext'])

            # try one more thing
            response_header = command + 'response'
            if not response_header in decoded:
                raise RuntimeError("ERROR: Unable to parse the response")

        # return the response content
        return decoded.get(response_header, "")

""" command line : python Client.py command """

if __name__=="__main__":

    import sys

    if len(sys.argv) != 2:
        print "usage: python Client.py command"
        exit(-1)

    command = sys.argv[1]
    client  = Client()
    result  = client.request(command)

    print json.dumps(result, sort_keys=True, indent=4)
