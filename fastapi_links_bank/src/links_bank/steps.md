### film_get_all_from_database
 - app.py commented `read_films`
 - api/films.py 
    - decorator changed to @router.get("/", response_model=list[Film])
    - new /films/ get-function created
    - example of all records from ORM reading added.

 
