# Customer Support Ticket – TKT-1042

## Customer Profile
- Customer: Sarah
- Customer ID: sarah_eng_01
- Role: Lead Engineer
- Environment: Node.js backend hosted on AWS

## Issue
Sarah reported outbound API request timeouts from her Node.js application hosted on AWS.

## Root Cause
Restrictive AWS security group rules were blocking required outbound IP ranges.

## Troubleshooting
- Reviewed outbound network connectivity.
- Checked AWS security group rules.
- Identified restrictive firewall rules.
- Reviewed the required IP ranges.

## Resolution
- Allowlisted the required IP ranges.
- Removed the restrictive deny rules.

## Status
Resolved

## Key Information to Remember
Sarah previously experienced API authentication issues and now has encountered outbound connectivity problems.

Her application runs on Node.js hosted on AWS. Her support history should be considered when investigating future issues.
