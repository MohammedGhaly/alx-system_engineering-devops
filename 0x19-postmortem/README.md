# Incident Postmortem: Website Downtime

## Incident Overview
**Date and Time**: 10th Oct 2023 . 21:45 GMT+3\
**Duration**: 1h 55m\
**Impact**: The website was inaccessible for about *2 hours*, affecting *1000* users.\
**Root Cause**: A misconfiguration in the load balancer's settings.

---
---
## Timeline of events

- **[21:45]**: Users reported that the website was slow.

- **[22:05]**: The website became completely unresponsive.
- **[22:08]**: The incident response team was alerted.
- **[22:20]**: The team initiated an investigation.
- **[23:30]**: The load balancer misconfiguration was identified and corrected.
- **[23:40]**: The website was fully restored to normal operation.

---
---
## Root cause and resolution

*Upon detecting the issue, the incident response team took the following immediate actions:*

- Verified the reported issues.
- Checked the server logs for errors.
- Monitored network and server performance.
- Identified the misconfiguration in the load balancer's settings.

The **root cause** of the incident was a misconfiguration in the load balancer's settings. Specifically, the load balancer was not distributing traffic properly, causing a bottleneck in the web stack.

The incident led to a 1h 35m -long downtime, affecting 1000 users.\
During this period, users were unable to access the website, resulting in frustration and potential loss of engagement.\
The incident response team worked diligently to resolve the issue and minimize user impact.

---
---
## Recommendations
- Implement real-time monitoring for load balancer performance.
- Establish better incident communication channels with users during downtime.
- Periodically audit and test the load balancer settings for potential misconfigurations.

---
---
## Follow-up Actions

- Load balancer configurations have been reviewed, corrected, and documented.
- Real-time monitoring tools for load balancing have been implemented.
- Incident communication procedures have been updated.
- Incident response team members will undergo additional training.
