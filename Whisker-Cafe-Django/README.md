# Whisker Café

**Cat Café Reservation and Visitor Management System** built with Django and Python.

Whisker Café is a workspace for a small cat café. Café owners and staff can record customer reservations, note the cat a guest hopes to meet, track the number of guests and preferred session, welcome visitors in arrival order, and follow a consistent visit process.

## Who it helps

Whisker Café is designed for cat café owners, managers, and staff who need one place to organize customer visits. It reduces missed reservation details and confusion about whose turn is next by keeping guest information, the visitor waiting line, staff assignments, and visit stages together. Workspace roles let viewers see information without changing it, while authorized staff can manage reservations and daily operations.

## Visual design

The interface uses a café-inspired editorial layout with a warm ivory canvas, forest-green navigation, terracotta accents, oversized serif headings, and a responsive horizontal menu. The dashboard is organized around a welcome feature, café activity cards, the reservation desk, visitor queue, weekly activity, and team workload. This is a structural redesign of the original Flowdesk interface, not only a color or logo change.

## Main features

- **Reservation management:** Save customer name, email, cat name preference, guest count, visit type, preferred session, visit date, notes, status, and staff host.
- **FIFO visitor queue:** Guests are welcomed in the order they join the line. The next-guest preview and the serve action use the same queue front.
- **Resident cat directory:** A dedicated page introduces the café cats, their personalities, and favorite activities.
- **Visit workflow:** A configurable sequence from reservation received through check-in, lounge session, refreshments, and checkout.
- **Café reports:** Review reservation totals, visit statuses, categories, and staff assignments.
- **Team workspaces and roles:** Keep workspace data separated and preserve owner, manager, agent, and read-only viewer permissions.
- **Responsive layout:** Navigation and content adapt to phone-sized screens.

## Technology

- Python 3.12 or 3.13
- Django 5.2
- SQLite
- HTML, CSS, and JavaScript

## Run on Windows

1. Install Python 3.12 or 3.13 from [python.org](https://www.python.org/). During installation, enable **Add python.exe to PATH**.
2. Extract the project ZIP into a normal folder. Do not run it from inside the ZIP.
3. Open the extracted project folder in File Explorer, type `powershell` in the address bar, and press Enter.
4. Run setup once:

   ```powershell
   .\SETUP.bat
   ```

5. Start the site:

   ```powershell
   .\START.bat --port 8001
   ```

6. Open `http://127.0.0.1:8001/` if the browser does not open automatically. Create an account and use **Whisker Café** as the workspace name.

Keep the PowerShell window open while using the website. Press `Ctrl+C` to stop the server.

## Database migration

The reservation form adds three fields to the original Ticket model: `cat_name`, `guest_count`, and `session_time`. The migration is included at `database/migrations/0003_ticket_cat_reservation_fields.py`. The supplied setup script applies migrations when preparing the database.

## Data structures

### FIFO queue

`backend/dsa/queue.py` uses `collections.deque`. `enqueue()` adds at the rear, while `dequeue()` removes from the front with `popleft()`. `peek()` reads the front without removing it. Enqueue and dequeue are both O(1), and `to_list()` returns a new list in arrival order for database persistence.

### Singly linked list

`backend/dsa/singly_linked_list.py` stores values in `Node` objects. Each node has `data` and one `next` reference. `head` points to the first node, `tail` points to the last node, and `_size` caches the number of nodes. Appending is O(1) because the tail is already known. Reading an arbitrary position is O(n) because the list must follow `next` links from the head until it reaches that position.

## Verification commands

Run these from PowerShell in the project folder:

```powershell
.\RUN_TESTS.bat
.\CHECK_QUEUE.bat
.\CHECK_LINKED_LIST.bat
.\CHECK_ACTIVITY.bat
.\RUN_ALL_CHECKS.bat
```

The final submission should show `RUN_TESTS.bat` passing all 57 application tests and `RUN_ALL_CHECKS.bat` passing the queue and linked-list goal checks. Do not edit `challenge/` or `tests/`.

## Before submitting

- Capture the original baseline evidence before changing code if your instructor requires it. If this was not captured before editing, do not recreate or mislabel screenshots as baseline evidence.
- Capture the visitor queue with three reservations joined in order, then demonstrate that the first one is welcomed first.
- Demonstrate the workflow operations and show the inspector badge **Actual node chain**.
- Capture the transformed dashboard, resident cat directory, reservation form, visitor queue, and a phone-sized screen.
- Include the passing test/checker outputs, this README, and any required contribution table.
- Exclude `.venv/`, `database/data/*.sqlite3`, `__pycache__/`, and secret keys from the submitted ZIP.

## Project concept

Whisker Café is a cat café reservation and visitor management system. The visitor queue represents customers waiting for their lounge session. The linked list represents the ordered steps of a café visit: reservation received, customer check-in, cat lounge session, refreshment service, and checkout and departure.
