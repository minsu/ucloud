#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright 2012 Netsco Inc.
# Copyright 2013 Jioh L. Jung (ziozzang@gmail.com)

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
            "serviceofferingid" : "c504e367-20d6-47c6-a82c-183b12d357f2",
            "templateid"        : "142bf958-39a8-4e2e-973a-464ad814da96",
            "zoneid"            : "9845bd17-d438-4bde-816d-1b12f37d5080",
            "diskofferingid"    : "87c0a6f6-c684-4fbe-a393-d8412bcf788d",
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
        "default"  : {
            "zoneid": "9845bd17-d438-4bde-816d-1b12f37d5080"
        },
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
        "required" : (),
    },

    "listVolumes": {
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
        "default"  : {
            "zoneid" : "9845bd17-d438-4bde-816d-1b12f37d5080",
        },
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




    #-------------------------------------------------------
    # Load Balancer API
    #-------------------------------------------------------

    #-------------------------------------------------------
    # LoadBalancer
    #-------------------------------------------------------
    "createLoadBalancer": {
        "name"     : "createLoadBalancer",
        "default"  : {
            "bandwidth" : "100",
            "loadbalanceroption": "roundrobin",
        },
        "required" : (
            "name",
            "bandwidth",
            "loadbalanceroption",
            "serviceport",
            "infourl",
        ),
    },

    "deleteLoadBalancer": {
        "name"     : "deleteLoadBalancer",
        "default"  : {},
        "required" : (
            "loadbalancerid",
        ),
    },

    "listLoadBalancers": {
        "name"     : "listLoadBalancers",
        "default"  : {},
        "required" : (),
    },

    "updateLoadBalancer": {
        "name"     : "updateLoadBalancer",
        "default"  : {
            "loadbalanceroption" : "roundrobin",
        },
        "required" : (
            "loadbalancerid",
            "loadbalanceroption",
        ),
    },

    #-------------------------------------------------------
    # Service Resource
    #-------------------------------------------------------
    "addLoadBalancerWebServer": {
        "name"     : "addLoadBalancerWebServer",
        "default"  : {},
        "required" : (
            "loadbalancerid",
            "virtualmachineid",
            "ipaddressid",
            "publicport",
            "privateport",
        ),
    },

    "listLoadBalancerWebServers": {
        "name"     : "listLoadBalancerWebServers",
        "default"  : {},
        "required" : (
            "loadbalancerid",
        ),
    },

    "removeLoadBalancerWebServer": {
        "name"     : "removeLoadBalancerWebServer",
        "default"  : {},
        "required" : (
            "serviceid",
        ),
    },




    #-------------------------------------------------------
    # WAF API
    #-------------------------------------------------------

    #-------------------------------------------------------
    # WAF
    #-------------------------------------------------------
    "createWAF": {
        "name"     : "createWAF",
        "default"  : {
            "type": "single",   # single | dual
            "spec": "basic",    # basic | standard | advanced | premium
            "waf1consoleport": "5950",
            "waf1SSHport": "5951",
            "waf1DBport": "5952",
        },
        "required" : (
            "name",
            "type",
            "spec",
            "zoneid",
            "waf1consoleport",
            "waf1SSHport",
            "waf1DBport",
        ),
    },

    "deleteWAF": {
        "name"     : "deleteWAF",
        "default"  : {},
        "required" : (
            "id",
        ),
    },

    "listWAFs": {
        "name"     : "listWAFs",
        "default"  : {},
        "required" : (),
    },

    #-------------------------------------------------------
    # Web Server Resource
    #-------------------------------------------------------
    "addWAFWebServer": {
        "name"     : "addWAFWebServer",
        "default"  : {
            "sslMode": "disabled",  # disabled | sslthru | sslterm
        },
        "required" : (
            "id",
            "virtualmachineid",
            "webServerPort",
            "proxyPort1",
            "sslMode",
        ),
    },

    "listWAFWebServers": {
        "name"     : "listWAFWebServers",
        "default"  : {},
        "required" : (
            "id",
        ),
    },

    "removeWAFWebServer": {
        "name"     : "removeWAFWebServer",
        "default"  : {},
        "required" : (
            "id",
            "webserverid",
        ),
    },

    #-------------------------------------------------------
    # Web Site Resource
    #-------------------------------------------------------
    "addWAFWebSite": {
        "name"     : "addWAFWebSite",
        "default"  : {},
        "required" : (
            "id",
            "sitename",
            "port",
            "policyNum",    # 0 | 1 | 2 | 3
        ),
    },

    "listWAFWebSites": {
        "name"     : "listWAFWebSites",
        "default"  : {},
        "required" : (
            "id",
        ),
    },

    "removeWAFWebSite": {
        "name"     : "removeWAFWebSite",
        "default"  : {},
        "required" : (
            "id",
            "websiteid",
        ),
    },

    #-------------------------------------------------------
    # Package Resource
    #-------------------------------------------------------
    "listPackages": {
        "name"     : "listPackages",
        "default"  : {},
        "required" : (),
    },

    "createPackage": {
        "name"     : "createPackage",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "deletePackage": {
        "name"     : "deletePackage",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "describePackages": {
        "name"     : "describePackages",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "describePackageEvents": {
        "name"     : "describePackageEvents",
        "default"  : {},
        "required" : (),
    },

    "describePackageResources": {
        "name"     : "describePackageResources",
        "default"  : {},
        "required" : (),
    },

    "getTemplate": {
        "name"     : "getTemplate",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "listPackageResources": {
        "name"     : "listPackageResources",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "registerUserSignal": {
        "name"     : "registerUserSignal",
        "default"  : {},
        "required" : (
            "PackageName",
        ),
    },

    "listTemplates": {
        "name"     : "listTemplates",
        "default"  : {},
        "required" : (),
    },

    "describeTemplate": {
        "name"     : "describeTemplate",
        "default"  : {},
        "required" : (
            "TemplateId",
        ),
    },

    "deleteTemplate": {
        "name"     : "deleteTemplate",
        "default"  : {},
        "required" : (
            "TemplateId",
        ),
    },

    "uploadTemplate": {
        "name"     : "uploadTemplate",
        "default"  : {},
        "required" : (
            "TemplateName",
            "TemplateBody",
        ),
    },

    "validateTemplate": {
        "name"     : "validateTemplate",
        "default"  : {},
        "required" : (
            "TemplateId",
        ),
    },
}
