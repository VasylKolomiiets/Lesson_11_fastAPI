### film_get_all_from_database
 - app.py commented `read_films`
 - api.films.py 
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

### Depends with get_session()
   - api.films.py
      - import Depends  
      - import get_session() 
      - Session from sqlalchemy.orm
      - modify `read_films()` Depends-style


### models.films.py class structuring
   - models.films.py
      - class FilmCategory(str, Enum) adding
   - settigs.py actualising
      - correct claa object creating

### best practice project's structure
   - api.films.py
      - move function to services.films.py
      - rework rout processing using `class FilmsService` into `Depends` style
      code
   - services.films.py
      - create special class `class FilmsService:` for `Depends` including
      into *api.films.py*
   
   Таким чином 'бізнес-логіка' була відокремлена від обробника шляхів ІПЗ (API)

### films filter magic adding
   - api.films.py
      - optional filter parameter added in api processor call
   - services.films.py
      - optional filter parameter added to class metod
