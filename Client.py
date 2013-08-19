#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#
# Copyright 2012 Netsco Inc.
# Copyright 2012 Minsu Kang

from urllib import quote as quote
from urllib2 import urlopen, HTTPError
from base64 import b64encode

import hmac
import hashlib
import json
import re

UCLOUD_API_KEY = 'YOU_MUST_ENTER_YOUR_API_KEY_HERE_!'
UCLOUD_SECRET  = 'YOU_MUST_ENTER_YOUR_SECRET_KEY_HERE_!'
UCLOUD_API_URLS = {
    'server' : 'https://api.ucloudbiz.olleh.com/server/v1/client/api',
    'lb'     : 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api',
    'waf'    : 'https://api.ucloudbiz.olleh.com/waf/v1/client/api',
    'watch'  : 'https://api.ucloudbiz.olleh.com/watch/v1/client/api',
    'package': 'https://api.ucloudbiz.olleh.com/packaging/v1/client/api',
}

class Client(object):
    def __init__(self, api_type = 'server', api_key=UCLOUD_API_KEY, secret=UCLOUD_SECRET):
        self.api_url = UCLOUD_API_URLS[api_type]
        self.api_key = api_key
        self.secret  = secret

    def request(self, command, args={}):
        if not command:
            raise RuntimeError('Command Missing !!')

        args['command']  = command
        args['response'] = 'json'
        args['apiKey']   = self.api_key

        query = '&'.join(
            '='.join([k, quote(args[k])]) for k in sorted(args.keys(), key=str.lower))
        
        signature = b64encode(hmac.new(
                self.secret,
                msg=query.lower(),
                digestmod=hashlib.sha1
        ).digest())

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
        #-------------------------------------------------------

        try:
            response = urlopen(self.api_url + '?' + query)
        except HTTPError as e:
            raise RuntimeError("%s" % e)

        decoded  = json.loads(response.read())

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
