#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright 2012 Netsco Inc.

from Client import *
from commands import COMMANDS

class UClient(Client):

    """ UCloud Client """

    def run(self, command, args={}):
        response = self.request(command, args)
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
                    "IP ID", "RULE ID", "VM-ID", "PUBLIC", "PRIVATE", "VM"
                )
                for idx, rule in enumerate(response['portforwardingrule']):
                    print "%36s %36s %36s %6s %7s %s" % (
                        rule.get('ipaddressid', ''),
                        rule.get('id', ''),
                        rule.get('virtualmachineid', ''),
                        rule.get('publicport', ''),
                        rule.get('privateport', ''),
                        rule.get('virtualmachinedisplayname', '')
                    )
                exit(0)

            print json.dumps(response, indent=2)
        return response

""" Command Line Interface """

def usage_out():
    print "usage: python UClient.py api_type command args"
    print "         api_type : server or lb(loadbalancer) or waf"
    exit(-1)

if __name__ == "__main__":

    import sys

    if len(sys.argv) < 3:
        usage_out()

    args = {}
    if len(sys.argv) > 3:
        args = dict(arg.split('=') for arg in sys.argv[3:])

    client  = UClient(api_type=sys.argv[1])

    # command validation
    command = COMMANDS.get(sys.argv[2], None)
    if not command:
        raise RuntimeError('invalid command : %s' % sys.argv[2])

    # param validation
    params = command["default"]
    params.update(args)

    if not set(command["required"]).issubset(params):
        print command["required"]
        raise RuntimeError('required parameters missing')
    client.run(command['name'], params)
    exit(0)
