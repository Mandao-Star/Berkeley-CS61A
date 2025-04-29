CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child from parents as a, dogs as b 
  where a.parent = b.name
  order by b.height desc;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, min(b.size) as size from dogs as a, sizes as b
  where
  a.height > b.min and a.height <= b.max
  group by a.name; 


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as sibling1, b.child as sibing2
  from parents as a, parents as b
  where a.parent = b.parent
  and a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || a.sibling1 || " and " || a.sibing2 || ", have the same size: " || b.size
  from siblings as a
  join size_of_dogs as b on b.name = a.sibling1
  join size_of_dogs as c on c.name = a.sibing2
  where c.size = b.size;



CREATE TABLE low_variance AS
  SELECT fur, max(height) - min(height) as height_range
  from dogs
  group by fur
  having min(height) >= 0.7 * avg(height)
  and max(height) <= 1.3 * avg(height);

