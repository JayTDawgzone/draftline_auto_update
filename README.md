# draftline_auto_update
Tools for automatic data entry using Selenium &amp; Python


### Summary

These scripts are for automating data entry tasks in [draftlinesmartsystem.com](https://www.draftlinesmartsystem.com). Some tasks can take several hundred working hours to do manually. There is no access to the back end database to make changes, so the simplest and fastest solution was to use Python and Selenium to update the database through the front end.


### Data Entry Tasks

**account_info_update:**

The database contains 9,000~ accounts, all were manually entered. This caused data inconsistency. For example, some account information was upper-cased, while other accounts were proper cased.

The script loops through all accounts and converts form fields to proper case. It can also other data entry errors depending on what information is given in the .xlsx file.


**cancel_trips:**

When massive route changes are made, there is a chance that trips for the next two weeks could be duplicated.

This script uses VBA to identify duplicated trips, and then cancels the trips in Draftline using Selenium.


**recurring_trip_update:**

This script takes in an xlsx file of route changes and uses Selenium to enter the information into Draftline.
