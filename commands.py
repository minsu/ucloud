#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright 2012 Netsco Inc.

COMMANDS = {

    #-------------------------------------------------------
    # Virtual machine provisioning
    #-------------------------------------------------------

    "listVirtualMachines": {
        "name"     : "listVirtualMachines",
        "default"  : {},
        "required" : (),
    },

    "deployVirtualMachine": {
        "name"     : "deployVirtualMachine",
        "default"  : {
            "serviceofferingid" : '75',
            "templateid"        : '845',
            "zoneid"            : '2',
            "diskofferingid"    : '38',
            "usageplantype"     : 'hourly',
        },
        "required" : (
            "serviceofferingid",
            "templateid",
            "zoneid",
            "diskofferingid",
            "usageplantype"
        ),
    },

    "destroyVirtualMachine": {
        "name"     : "destroyVirtualMachine",
        "default"  : {},
        "required" : ("id",),
    },

    "startVirtualMachine": {
        "name"     : "startVirtualMachine",
        "default"  : {},
        "required" : ("id",),
    },

    "stopVirtualMachine": {
        "name"     : "stopVirtualMachine",
        "default"  : {},
        "required" : ("id",),
    },

    "rebootVirtualMachine": {
        "name"     : "rebootVirtualMachine",
        "default"  : {},
        "required" : ("id",),
    },

    "listAvailableProductTypes": {
        "name"     : "listAvailableProductTypes",
        "default"  : {},
        "required" : (),
    },

    #-------------------------------------------------------
    # Volume
    #-------------------------------------------------------

    "attachVolume": {
        "name"     : "attachVolume",
        "default"  : {},
        "required" : ("id", "virtualmachineid"),
    },

    "createVolume": {
        "name"     : "createVolume",
        "default"  : {"zoneid": 2},
        "required" : ("name", "zoneid", "diskofferingid"),
    },

    "deleteVolume": {
        "name"     : "deleteVolume",
        "default"  : {},
        "required" : ("id",),
    },

    "detachVolume": {
        "name"     : "detachVolume",
        "default"  : {},
        "required" : ("id", "virtualmachineid"),
    },

    "listVolume": {
        "name"     : "listVolumes",
        "default"  : {},
        "required" : (),
    },

    #-------------------------------------------------------
    # Load Balanacing
    #-------------------------------------------------------

    "assignToLoadBalancerRule": {
        "name"     : "assignToLoadBalancerRule",
        "default"  : {},
        "required" : ("id", "virtualmachineids"),
    },

    "createLoadBalancerRule": {
        "name"     : "createLoadBalancerRule",
        "default"  : {"algorithm": "roundrobin"},
        "required" : (
            "algorithm",
            "name",
            "privateport",
            "publicipid",
            "publicport"
        ),
    },

    "deleteLoadBalancerRule": {
        "name"     : "deleteLoadBalancerRule",
        "default"  : {},
        "required" : ("id",),
    },

    "listLoadBalancerRuleInstances": {
        "name"     : "listLoadBalancerRuleInstances",
        "default"  : {},
        "required" : ("id",),
    },

    "listLoadBalancerRules": {
        "name"     : "listLoadBalancerRules",
        "default"  : {},
        "required" : (),
    },

    "removeFromLoadBalancerRule": {
        "name"     : "removeFromLoadBalancerRule",
        "default"  : {},
        "required" : ("id", "virtualmachineids"),
    },

    "updateLoadBalancerRule": {
        "name"     : "updateLoadBalancerRule",
        "default"  : {},
        "required" : ("id",),
    },

    #-------------------------------------------------------
    # Address
    #-------------------------------------------------------

    "associateIpAddress": {
        "name"     : "associateIpAddress",
        "default"  : {},
        "required" : ("zoneid",),
    },

    "disassociateIpAddress": {
        "name"     : "disassociateIpAddress",
        "default"  : {},
        "required" : ("id",),
    },

    "listPublicIpAddresses": {
        "name"     : "listPublicIpAddresses",
        "default"  : {},
        "required" : (),
    },

    #-------------------------------------------------------
    # Account
    #-------------------------------------------------------

    "listAccounts": {
        "name"     : "listAccounts",
        "default"  : {},
        "required" : (),
    },

    #-------------------------------------------------------
    # Firewall
    #-------------------------------------------------------

    "listPortForwardingRules": {
        "name"     : "listPortForwardingRules",
        "default"  : {},
        "required" : (),
    },

    "createPortForwardingRule": {
        "name"     : "createPortForwardingRule",
        "default"  : {'protocol': 'TCP'},
        "required" : (
            "ipaddressid",
            "publicport",
            "privateport",
            "virtualmachineid",
            "protocol"
        ),
    },

    "deletePortForwardingRule": {
        "name"     : "deletePortForwardingRule",
        "default"  : {},
        "required" : ("id",),
    },

    #-------------------------------------------------------
    # ETC
    #-------------------------------------------------------

    "listEvents": {
        "name"     : "listEvents",
        "default"  : {},
        "required" : (),
    },

    "queryAsyncJobResult": {
        "name"     : "queryAsyncJobResult",
        "default"  : {},
        "required" : ("jobid",),
    },
}
