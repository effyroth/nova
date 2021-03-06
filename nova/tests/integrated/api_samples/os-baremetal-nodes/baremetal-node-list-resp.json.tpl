{
    "nodes": [{
        "service_host": "host",
        "cpus": 8,
        "memory_mb": 8192,
        "local_gb": 128,
        "pm_address": "10.1.2.3",
        "pm_user": "pm_user",
        "prov_mac_address": "12:34:56:78:90:ab",
        "terminal_port": 8000,
        "instance_uuid": null,
        "id": %(node_id)s,
        "interfaces": [{
            "id": %(interface_id)s,
            "address": "%(address)s",
            "datapath_id": null,
            "port_no": null
        }]
    }]
}
