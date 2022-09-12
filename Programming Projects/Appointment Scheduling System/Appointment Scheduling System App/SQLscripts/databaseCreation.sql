create table appt_sign_up_forms (
	sign_up_id int not null auto_increment,
    patient_first_name varchar(50),
    patient_last_name varchar(50),
    patient_dob date,
    patient_email varchar(100),
    patient_phone varchar(12),
    patient_zip varchar(5),
    insurance_name varchar(100),
    group_number varchar(50),
    member_id varchar(50),
    ph_first_name varchar(50),
    ph_last_name varchar(50),
    ph_dob date,
    service varchar(255),
    PRIMARY KEY (sign_up_id)
);

create table appointments (
	appt_id int not null auto_increment,
    appt_time time,
    appt_date date,
    sign_up_id int,
    isVisible int,
    PRIMARY KEY (appt_id),
    constraint unique_appointment unique (appt_time, appt_date) 
);

create table employees (
	emp_id int not null auto_increment,
    emp_first_name varchar(50),
    emp_last_name varchar(50),
    emp_email varchar(100),
    emp_phone varchar(12),
    emp_type_id int,
    active_emp int,
    PRIMARY KEY (emp_id),
    constraint unique_emp unique (emp_first_name, emp_last_name, emp_email)
);

alter table employees
ADD UNIQUE (emp_email);

alter table employees
ADD UNIQUE (emp_phone);

INSERT INTO employees (emp_first_name, emp_last_name, emp_email, emp_phone, emp_type_id, active_emp)
VALUES ('Le', 'Truong', 'smilearchitects@yahoo.com', '281-498-1101', 1, 1);

create table employee_types (
	emp_type_id int not null auto_increment,
    emp_type varchar(50),
    emp_type_description varchar(255),
    PRIMARY KEY (emp_type_id),
    constraint unique_emp_type unique (emp_type)
);

INSERT INTO employee_types (emp_type, emp_type_description)
VALUES ('admin', 'full access');

INSERT INTO employee_types (emp_type, emp_type_description)
VALUES ('read-only', 'read only access');

INSERT INTO employee_types (emp_type, emp_type_description)
VALUES ('read-write', 'read and write access');

create table system_users (
	user_id int not null auto_increment,
    username varchar(50),
    password varchar(500),
    emp_id int,
    PRIMARY KEY (user_id),
    constraint unique_username unique (username)
);

alter table system_users 
ADD CONSTRAINT fk_emp_id FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
ON DELETE CASCADE;

INSERT INTO system_users (username, password, emp_id)
VALUES ('admin', '$2b$10$hbIzLd37XH5pgx8SreDL.O2XFps96zFeaYKvK0jXN1mRmtT2GnnkO', 1);
