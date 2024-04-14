# Exercise 2

## Business Process Description

These Tables hold room details and event details. They are used for assigning events to rooms. The room dimension describes the room's attributes such as chairs. The event dimension has attributes of event such as capacity, start and end time. This allows meeting/event planners to see which events have been assigned to rooms.


## Fact Table

| Column Name | Type | Description |
| --- | --- | --- |
| event_id | UUID | The primary key for unique event |
| room_id | UUID | Foreign key that points to room dimension |

## Dimension

Room Dimension
| Column Name | Type | Description |
| --- | --- | --- |
| room_id | UUID | Primary Key unique to room  |
| capacity | int | room capacity |
| yoga_mats | int | number of yoga mat available |
| desks | int | number of yoga mat available |
| chairs | int | number of chairs available |
| room_details | varchar | room description |

Event Dimension
| Column Name | Type | Description |
| --- | --- | --- |
| event_id | UUID | Primary key unique to event|
| cost | DECIMAL  | cost of event |
| start_time | datetime | start time of event in local timezone |
| end_time | dateTime | end time of event in local timezone |
| capacity | INT | number of people allowed into event |

