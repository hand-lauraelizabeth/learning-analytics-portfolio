# Data Dictionary

All records in this repository are synthetic and were created solely for demonstration.

| Field | Type | Description |
| --- | --- | --- |
| participant_id | string | Synthetic participant identifier. |
| event_date | date | Date of the learning event or associated activity. |
| organization_id | string | Synthetic organization identifier. |
| topic | string | High-level learning topic. |
| delivery_format | string | Delivery mode, currently Virtual or In Person. |
| activity_type | string | Funnel-stage activity: registration, attendance, or completion. |

## Grain

Each row represents one participant activity associated with one learning event date.

A participant can therefore appear multiple times for the same event as they progress through the funnel from registration to attendance to completion.

## Example KPI definitions

**Unique participants**  
Distinct `participant_id` values during the analysis period.

**Active organizations**  
Distinct `organization_id` values with at least one activity record.

**Attendance conversion**  
Distinct participant-event pairs with an attendance record divided by distinct participant-event pairs with a registration record.

**Completion conversion**  
Distinct participant-event pairs with a completion record divided by distinct participant-event pairs with an attendance record.

**Quarter**  
Calendar quarter derived from `event_date`.
