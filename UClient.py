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
                print "%8s %8s %18s %10s %5s %5s %5s" % (
                    "ID", "NAME", "IP", "STATE", "TID", "ZONE", "SID",
                )
                for idx, vm in enumerate(response['virtualmachine']):
                    print "%8s %8s %18s %10s %5s %5s %5s" % (
                        vm.get('id', ''),
                        vm.get('displayname', ''),
                        vm["nic"][0].get("ipaddress", ""),
                        vm.get('state', ''),
                        vm.get('templateid', ''),
                        vm.get('zoneid', ''),
                        vm.get('serviceofferingid', '')
                    )
                exit(0)

            if (command == 'listPortForwardingRules'):
                print "%10s %10s %10s %10s %10s %10s" % (
                    "IP ID", "RULE ID", "PUBLIC", "PRIVATE", "VM", "VM-ID"
                )
                for idx, rule in enumerate(response['portforwardingrule']):
                    print "%10s %10s %10s %10s %10s %10s" % (
                        rule.get('ipaddressid', ''),
                        rule.get('id', ''),
                        rule.get('publicport', ''),
                        rule.get('privateport', ''),
                        rule.get('virtualmachinedisplayname', ''),
                        rule.get('virtualmachineid', '')
                    )
                exit(0)

            print json.dumps(response, indent=2)
        return response

""" Command Line Interface """

def usage_out():
    print "usage: python UClient.py command args"
    exit(-1)

if __name__ == "__main__":

    import sys

    if len(sys.argv) < 2:
        usage_out()

    args = {}
    if len(sys.argv) > 2:
        args = dict(arg.split('=') for arg in sys.argv[2:])

    client  = UClient()

    # command validation
    command = COMMANDS.get(sys.argv[1], None)
    if not command:
        raise RuntimeError('invalid command : %s' % sys.argv[1]) 

    # param validation
    params = command["default"]
    params.update(args)

    if not set(command["required"]).issubset(params):
        raise RuntimeError('required parameters missing')
    client.run(command['name'], params)
    exit(0)
