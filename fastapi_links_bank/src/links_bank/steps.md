### film_get_all_from_database
 - app.py commented `read_films`
 - api/films.py 
    - decorator changed to @router.get("/", response_model=list[Film])
    - new /films/ get-function created
    - example of all records from ORM reading added.

### orm_mode_set_to_True  
   - models.films - added parameter 
   ```python
   class Settings:
      orm_mode = True
   ```

### session_close__nd__def_get_session_added
   - api.films.py  
      - added code `session.close()`  !! it was an error !!
   - database.py
      - added function `get_session()` for further including

