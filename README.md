## summary and introduction
this is a simple task management system powered by FastAPI, SQLAlchemy, PostgreSQL and alembic.
main functionalities are a CRUD on a task database with "id", "title", "description", "creation_date", "due_date", "done" columns.

visit it's OpenAPI doc at `root/docs` address.

## features list, current and future
currently it has only some features for retrieveing tasks and a simple CRUD on them

### Current features

 - [ ] CRUD
	 - [ ] create task with title and description and due date (last two are optional)
	 - [ ] update task based on specific id
	 - [ ] delete task based on specific id
	 - [ ] view task, as a list or with specific id
 - [ ] Searching with query params
	 - [ ] search with title
	 - [ ] search with description
	 - [ ] search with a range for creation date
	 - [ ] search with a range for due date
	 - [ ] search with done status

### upcoming features and tasks

 - [ ] implement user functionality and database
 - [ ] implement security with login and JWT for users.
 - [ ] implement best practices based on "clean code", "API design", "FastAPI", "SQLAlchemy", "Postgres" and other used tools.
 - [ ] add build and deploy code with docker and other tools for building proccess
 - [ ] add frontend
 - [ ] add tests with pytest and postman
 - [ ] review and edit docs, add comments to code, edit readme and add runner and required commands for run and view project and and other explanatory texts
