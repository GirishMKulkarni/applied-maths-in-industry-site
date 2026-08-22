-- ============================================================================
--  S13B · SQL Essentials — the class database
--
--  This is an exact copy of the database used on our practice site
--  (https://www.sql-practice.online/?mode=scenario&category=select-statements&engine=core-sql)
--  so everything you try in the browser also runs on your own machine.
--
--  Load it once (from this folder):
--      sqlite3 class.db < hr_database.sql
--      sqlite3 class.db          then check with:  .tables
--
--  Three tables, stitched by keys:
--    employees(employee_id PK, first_name, last_name, email, hire_date,
--              job_id FK -> jobs, salary, manager_id FK -> employees,
--              department_id FK -> departments)
--    departments(department_id PK, department_name, location)   5 rows
--    jobs(job_id PK, job_title, min_salary, max_salary)         6 rows
-- ============================================================================

CREATE TABLE departments (
    department_id   INTEGER PRIMARY KEY,
    department_name VARCHAR(50),
    location        VARCHAR(100)
);

INSERT INTO departments VALUES (10, 'IT', 'San Francisco');
INSERT INTO departments VALUES (20, 'HR', 'New York');
INSERT INTO departments VALUES (30, 'Finance', 'Chicago');
INSERT INTO departments VALUES (40, 'Marketing', 'Los Angeles');
INSERT INTO departments VALUES (50, 'Operations', 'Seattle');   -- no employees yet!

CREATE TABLE jobs (
    job_id     VARCHAR(20) PRIMARY KEY,
    job_title  VARCHAR(100),
    min_salary INTEGER,
    max_salary INTEGER
);

INSERT INTO jobs VALUES ('FIN_ANALYST', 'Financial Analyst',   50000,  85000);
INSERT INTO jobs VALUES ('HR_REP',      'HR Representative',   45000,  75000);
INSERT INTO jobs VALUES ('IT_MGR',      'IT Manager',          90000, 150000);
INSERT INTO jobs VALUES ('IT_PROG',     'Software Developer',  60000, 120000);
INSERT INTO jobs VALUES ('MKT_MGR',     'Marketing Manager',   70000, 110000);
INSERT INTO jobs VALUES ('SALES_REP',   'Sales Representative',40000,  80000);

CREATE TABLE employees (
    employee_id   INTEGER PRIMARY KEY,
    first_name    TEXT NOT NULL,
    last_name     TEXT NOT NULL,
    email         TEXT UNIQUE,
    hire_date     TEXT,
    job_id        TEXT REFERENCES jobs(job_id),
    salary        INTEGER CHECK (salary > 0),
    manager_id    INTEGER REFERENCES employees(employee_id),
    department_id INTEGER REFERENCES departments(department_id)
);

INSERT INTO employees VALUES (100,'John','Smith','john.smith@company.com','2020-01-15','IT_MGR',120000,NULL,10);
INSERT INTO employees VALUES (101,'Alice','Johnson','alice.johnson@company.com','2021-03-20','IT_PROG',85000,100,10);
INSERT INTO employees VALUES (102,'Bob','Wilson','bob.wilson@company.com','2021-06-10','IT_PROG',80000,100,10);
INSERT INTO employees VALUES (103,'Carol','Davis','carol.davis@company.com','2019-09-05','HR_REP',60000,NULL,20);
INSERT INTO employees VALUES (104,'David','Brown','david.brown@company.com','2022-02-14','FIN_ANALYST',70000,NULL,30);
INSERT INTO employees VALUES (105,'Emma','Taylor','emma.taylor@company.com','2020-11-30','MKT_MGR',95000,NULL,40);
INSERT INTO employees VALUES (106,'Frank','Green','frank.green@company.com','2021-08-25','SALES_REP',65000,105,40);
INSERT INTO employees VALUES (107,'Grace','White','grace.white@company.com','2019-05-12','IT_PROG',90000,100,10);
INSERT INTO employees VALUES (108,'Henry','Clark','henry.clark@company.com','2022-07-18','HR_REP',55000,103,20);
INSERT INTO employees VALUES (109,'Ivy','Martinez','ivy.martinez@company.com','2023-01-10','FIN_ANALYST',68000,104,30);
