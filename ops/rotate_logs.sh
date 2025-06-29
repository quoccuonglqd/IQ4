#!/bin/bash
find /var/log/myapi -name '*.log' -mtime +7 \
  | tar -czf /var/log/archive_$(date +%F).tar.gz -T -