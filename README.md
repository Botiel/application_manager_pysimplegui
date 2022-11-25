# application_manager_pysimplegui

 - An in-house gui app manager using pysimplegui for all the scripts i created at my current job (used daily by all the R&amp;D teams).

- This project includes only the gui setup and mock functions without the actual scripts that are running on it.

- I used an oop approach with this project for scalability and making it a breeze to add more apps in the future.

How It Works:
- each app has its class which includes layout, functions, and an event loop function.
- the main app controls the flow and instantiates an object of each app in a dictionary(name of the app as a key and the app object as a value).
- the main_loop creates the layout and controls the flow of the app (switching between layouts and events)
