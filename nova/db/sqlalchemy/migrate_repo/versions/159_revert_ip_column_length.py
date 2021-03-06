# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 IBM Corp.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from sqlalchemy import MetaData, String, Table
from sqlalchemy.dialects import postgresql

TABLE_COLUMNS = [
    # table name, column name
    ('instances', 'access_ip_v4'),
    ('instances', 'access_ip_v6'),
    ('networks', 'gateway'),
    ('networks', 'gateway_v6'),
    ('networks', 'netmask'),
    ('networks', 'netmask_v6'),
    ('networks', 'broadcast'),
    ('networks', 'dns1'),
    ('networks', 'dns2'),
    ('networks', 'vpn_public_address'),
    ('networks', 'vpn_private_address'),
    ('networks', 'dhcp_start'),
    ('fixed_ips', 'address'),
    ('floating_ips', 'address'),
    ('console_pools', 'address')]


def upgrade(migrate_engine):
    dialect = migrate_engine.url.get_dialect()

    # NOTE(maurosr): this just affects mysql; postgresql uses INET
    # type and sqlite doesn't goes fine with alter tables, so it should be done
    # manually. This way we'll be able to keep UCs like the one inserted on
    # version 158 which would get lost cause sqlite is not migrated as mysql or
    # pgsql, it copies the column and data instead of execute an alter table
    # command.
    if dialect is not postgresql.dialect:
        meta = MetaData(bind=migrate_engine)
        for table, column in TABLE_COLUMNS:
            t = Table(table, meta, autoload=True)
            getattr(t.c, column).alter(type=String(39))


def downgrade(migrate_engine):
    """Convert columns back to the larger String(43) defined in version 149."""
    dialect = migrate_engine.url.get_dialect()
    if dialect is not postgresql.dialect:
        meta = MetaData(bind=migrate_engine)
        for table, column in TABLE_COLUMNS:
            t = Table(table, meta, autoload=True)
            getattr(t.c, column).alter(type=String(43))
