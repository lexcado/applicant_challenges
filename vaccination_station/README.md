# Corona Vaccination Station

Model and implement a lightweight IT-System for handling the vaccination process in a bavarian corona station.

## Business requirements

The following minimal feature-set must be supported:

### Appointment creation

Patients should be able to create an appointment by registering for a vaccination time-slot. The registration process allows the patients to list available time-slots for a given day and to select one. Patients need to provide their name, birth-date and email address during this process as well.

A time-slot is 15 minutes.

### Appointment cancelation

A doctor should be able to cancel an existing appointment, which will lead to an email being sent to the patient and the appointment being deleted from the system, freeing the slot for another patient.

### Vaccination time-slot creation

Besides the initially given time-slots a doctor should be able to create new time-slots. The initial time-slots are provided in the `initial-time-slots.json` file

### Appointment time-slot notification

If there is no suitable time-slot available, the patient can subscribe for a notification if a time-slot within a defined time-range gets available. The notification happens via email.

## Boundary conditions

- Implement only the backend logic, preferably in python. TypeScript or Java
- You don't need to implement a REST, GraphQl etc. presentation layer exposing the business logic. Functions as entrypoints for the business logic are enough. Nevertheless, structure the business methods in a way that they easily can be called by the presentation layer and tests.
- **Proof that your solution works by providing high-level integration-tests.**
- You are free to use any in-memory persistence method, like hashmaps, in-memory databases, etc. There is no need for persistence across multiple executions of the application.
- The implementation should not be to narrowed and limit the system in its extensibility, as there are upcoming features already planned. Like, for example, the persistent creation of user-profiles, allowing the health department for listing vaccinated persons, sending reminders for booster vaccinations, etc..

## Bonus

If you are familiar with containers, provide a container which can be used to run the application in the command-line.
