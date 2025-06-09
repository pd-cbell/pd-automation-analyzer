"""Core logic for PagerDuty Automation Finder."""

import os
import sys
import json
from dateutil import parser

from pdpyras import APISession

def main(start: str, end: str):
    """
    Main function to execute the PagerDuty scan over the given time range.

    Reads the PAGERDUTY_API_TOKEN environment variable for authentication.
    Pulls incidents from PagerDuty API between start and end ISO datetimes,
    and prints the result as JSON.

    Args:
        start: Start datetime in ISO format.
        end: End datetime in ISO format.
    """
    token = os.getenv("PAGERDUTY_API_TOKEN")
    if not token:
        print("Error: PAGERDUTY_API_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    try:
        since = parser.isoparse(start)
        until = parser.isoparse(end)
    except (ValueError, TypeError) as e:
        print(f"Error parsing dates: {e}", file=sys.stderr)
        sys.exit(1)

    session = APISession(token)
    params = {"since": since.isoformat(), "until": until.isoformat()}

    incidents = []
    for incident in session.list_all("incidents", params=params):
        incidents.append(incident)

    print(json.dumps(incidents, indent=2))
    return incidents