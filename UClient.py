#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright 2012 Netsco Inc.
# Copyright 2013 Jioh L. Jung (ziozzang@gmail.com)

from Client import *
from commands import COMMANDS

class UClient(Client):

    """ UCloud Client """

    def run(self, command, args={}, post=None, debug=False, resptype="json"):
        response = self.request(command, args, post=post, debug=debug, resptype=resptype)
        if response is None:
            raise RuntimeError(
                'Response Error : %s' % json.dumps(response, indent=4))

        if __name__ == '__main__':

            if (command == 'listVirtualMachines'):
                print "%-36s %-36s %-36s %-36s %-15s %-10s %s" % (
                    "ID", "ZONE ID", "TEMPLATE ID", "SERVICE OFFERING ID", "IP", "STATE", "NAME", 
                )
                for idx, vm in enumerate(response['virtualmachine']):
                    print "%36s %36s %36s %36s %-15s %-10s %s" % (
                        vm.get('id', ''),
                        vm.get('zoneid', ''),
                        vm.get('templateid', ''),
                        vm.get('serviceofferingid', ''),
                        vm["nic"][0].get("ipaddress", ""),
                        vm.get('state', ''),
                        vm.get('displayname', '')
                    )
                exit(0)

            if (command == 'listPortForwardingRules'):
                print "%-36s %-36s %-36s %6s %7s %s" % (
                    "RULE ID", "IP ID", "VM ID", "PUBLIC", "PRIVATE", "VM"
                )
                for idx, rule in enumerate(response['portforwardingrule']):
                    print "%36s %36s %36s %6s %7s %s" % (
                        rule.get('id', ''),
                        rule.get('ipaddressid', ''),
                        rule.get('virtualmachineid', ''),
                        rule.get('publicport', ''),
                        rule.get('privateport', ''),
                        rule.get('virtualmachinedisplayname', '')
                    )
                exit(0)

            if (command == 'listPublicIpAddresses'):
                print "%-15s %-36s %s" % (
                    "IP", "ID", "ZONE"
                )
                for idx, rule in enumerate(response['publicipaddress']):
                    print "%-15s %36s %s" % (
                        rule.get('ipaddress'),
                        rule.get('id'),
                        rule.get('zonename')
                    )
                exit(0)

            print json.dumps(response, indent=2)
        return response

""" Command Line Interface """

def usage_out():
    print "usage: python UClient.py api_type command args"
    print "         api_type : server or lb(loadbalancer) or waf or watch or package"

if __name__ == "__main__":
    import sys
    import os

    UCLOUD_RESP_TYPE = "json"
    if "UCLOUD_RESP_TYPE" in os.environ:
        UCLOUD_RESP_TYPE = os.environ["UCLOUD_RESP_TYPE"]

    if len(sys.argv) < 3:
        usage_out()
        exit(-1)

    args = {}
    if len(sys.argv) > 3:
        args = dict(arg.split('=') for arg in sys.argv[3:])

    client  = UClient(api_type=sys.argv[1])

    # command validation
    command = COMMANDS.get(sys.argv[2], None)
    if not command:
        # cannot find Command from command.py
        #raise RuntimeError('invalid command : %s' % sys.argv[2])
        params = {}
        params.update(args)
        
        client.run(sys.argv[2], params, resptype=UCLOUD_RESP_TYPE)

    else:
        # param validation
        params = command["default"]
        params.update(args)

        if not set(command["required"]).issubset(params):
            print command["required"]
            raise RuntimeError('required parameters missing')

        client.run(command['name'], params, resptype=UCLOUD_RESP_TYPE)
    exit(0)
