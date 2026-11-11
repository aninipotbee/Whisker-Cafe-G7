# Whisker Café: Project Concept

## Purpose
Whisker Café is a cat café reservation and visitor management system. It helps café owners, managers, and staff organize guest reservations and manage the flow of visitors who want to spend time in the cat lounge.

## Users
- **Owner:** manages the café workspace, staff, reservations, and reports.
- **Manager:** oversees reservations, staff assignments, and daily operations.
- **Agent / café staff:** records reservations, manages the visitor line, and updates visit progress.
- **Viewer:** can inspect café information without editing records.

## Queue mapping
The ServiceQueue is the visitor waiting line. When reservations are added in order A, B, and C, the next guest must be A. This is FIFO (first in, first out). The next-guest preview uses `peek()`, and welcoming the next guest uses `dequeue()`.

## Linked-list mapping
The SinglyLinkedList stores the visit stages in order:
1. Reservation received
2. Customer check-in
3. Cat lounge session
4. Refreshment service
5. Checkout and departure

The inspector displays the actual node chain using each node's `next` reference.

## New business features
1. **Reservation details:** cat name preference, number of guests, and preferred session time are stored with each reservation. Guest count is validated from 1 through 12.
2. **Resident cat directory:** a dedicated page introduces the café cats and lets staff or customers refer to a cat when creating a reservation.
3. **Visit date and host assignment:** reservations can include a visit date and assigned café staff member.

## Who it helps and what problem it solves
Cat café owners and staff may receive bookings through several channels and can lose track of guest details or the order in which visitors should be welcomed. Whisker Café keeps reservation information, visitor order, staff assignments, and visit stages in one shared workspace. This makes the daily guest flow easier to follow while keeping cat comfort and availability in mind.
