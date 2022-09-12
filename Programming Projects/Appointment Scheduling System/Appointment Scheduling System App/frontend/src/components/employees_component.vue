<template>
    <div id="employeesComponentBody" style="min-width: 1400px;">
        <div class="bg-dark text-white" style="height: 60px; width: 100%; margin-top: 35px; border-radius: 10px; box-shadow: 0 3px 5px rgb(0 0 0 / 0.4);">
            <p class="mx-3" style="padding-top: 12px; font-weight: bold; font-size: 25px;">Employee Profiles</p>
        </div>
        <div class="row mt-4">
            <div> 
                <input type="text" id="searchBar" style="display: inline-block; width: 90%; border-radius: 0px;" class="form-control" placeholder="Filter employees by any field..." v-model="filter">
                <div align="center" class="form-control" style="display: inline-block; width: 10%; border-radius: 0px; border-left:none;">
                    <i class="fa-solid fa-magnifying-glass fa-xl"></i>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="overflow-auto mt-4" style="max-height: 870px; border-style: solid; border-left: none; border-right: none; border-bottom: none; max-width: 100%;">
                    <table class="table table-striped table-hover" style="">
                        <thead class="thead-dark bg-light sticky-top" style="box-shadow: 0 1px 4px rgb(0 0 0 / 0.4); z-index: 1;">
                            <tr>
                                <th @click="sortByFirstName()">First Name</th>
                                <th @click="sortByLastName()">Last Name</th>
                                <th @click="sortByEmail()">Email</th>
                                <th @click="sortByPhone()">Phone</th>
                                <th @click="sortByActive()">Active</th>
                                <th @click="sortByPermissions()">Permissions</th>
                                <th>
                                    <button v-if="this.adminPrivileges == 'true'" @click="toggleAddEmployee()" class="btn btn-primary" style="margin-left: 8px;" id="addEmployee"><div id="addEmployeeText">Add Employee</div></button>
                                    <button class="btn mx-2" style="opacity: 0;">filler</button>
                                </th>
                            </tr>
                        </thead>
                        <tbody v-if="this.filter !=''">
                            <tr v-for="employee in employees" :key="employee._id">
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.firstName }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.lastName }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.email }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.phoneNumber }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.active }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">{{ employee.permissions }}</td>
                                <td v-if="employee['lastName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['firstName'].toLowerCase().includes(this.filter.toLowerCase()) || employee['email'].toLowerCase().includes(this.filter.toLowerCase()) || employee['phoneNumber'].toLowerCase().includes(this.filter.toLowerCase()) || employee['active'].toLowerCase().includes(this.filter.toLowerCase()) || employee['permissions'].toLowerCase().includes(this.filter.toLowerCase())">
                                <button v-if="this.adminPrivileges == 'true'" @click="toggleEditEmployeeInformation(); selectEmployee()" class="btn btn-dark mx-2" id="editButton">Edit</button>
                                <button class="btn mx-2" style="opacity: 0;">filler</button>
                                </td>
                            </tr>
                        </tbody>
                        <tbody v-if="this.filter ==''">
                            <tr v-for="employee in employees" :key="employee._id">
                                <td>{{ employee.firstName }}</td>
                                <td>{{ employee.lastName }}</td>
                                <td>{{ employee.email }}</td>
                                <td>{{ employee.phoneNumber }}</td>
                                <td>{{ employee.active }}</td>
                                <td>{{ employee.permissions }}</td>
                                <td>
                                <button v-if="this.adminPrivileges == 'true'" class="btn btn-dark mx-2" id="editButton"
                                 @click="toggleEditEmployeeInformation(); 
                                 this.selectedEmployeefirstName = employee.firstName;
                                 this.selectedEmployeelastName = employee.lastName;
                                 this.selectedEmployeeEmail = employee.email;
                                 this.selectedEmployeePhoneNumber = employee.phoneNumber;
                                 this.selectedEmployeeActive = employee.active;
                                 this.selectedEmployeeAdmin = employee.permissions;
                                 this.editEmployeeInfoTarget.currentEmployeePhoneNumber = employee.phoneNumber
                                 this.editEmployeeInfoTarget.currentEmployeeEmail = employee.email
                                 "
                                >Edit</button>
                                <button class="btn mx-2" style="opacity: 0;">filler</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div v-if="this.showAddEmployee == true" class="col-md-auto" style="margin-top: 1.9em">
                <div class="bg-dark text-white" style="height: 50px; width: 100%; min-width: 326px; max-width: 345px; border-radius: 10px; box-shadow: 0 3px 5px rgb(0 0 0 / 0.4);">
                    <p class="mx-3" style="padding-top: 12px; font-weight: bold; font-size: 20px;">Add new employee<i class="fa-solid fa-xmark" id="togglerIcon" @click="closeSideMenu()" style="margin-left: 5em"></i> </p>
                </div>  
                <div style="padding-left: 25px; padding-right: 25px;">
                    <form onsubmit="return false">
                        <div class="mb-4 mt-4">
                            <label for="username" class="form-label">First Name</label>
                            <input type="text" class="form-control" style="max-width: 300px;" v-model="newEmployee.firstName" required>
                        </div>
                        <div class="mb-4">
                            <label for="username" class="form-label">Last Name</label>
                            <input type="text" class="form-control" style="max-width: 300px;" v-model="newEmployee.lastName" required>
                        </div>
                        <div class="mb-4">
                            <label for="username" class="form-label">Email</label>
                            <input type="text" class="form-control" style="max-width: 300px;" pattern="[^@\s]+@[^@\s]+\.com" aria-describedby="emailHelpBlock" v-model="newEmployee.email" required>
                            <small id="emailHelpBlock" class="form-text text-muted">
                                Ex. email@email.com
                            </small>
                        </div>
                        <div class="mb-3">
                            <label for="username" class="form-label">Phone</label>
                            <input type="text" class="form-control" style="max-width: 300px;" pattern="^\d{3}-\d{3}-\d{4}$" aria-describedby="phoneHelpBlock" v-model="newEmployee.phoneNumber" required>
                            <small id="phoneHelpBlock" class="form-text text-muted">
                                Ex. xxx-xxx-xxxx
                            </small>
                        </div> 
                        <p class="fw-bold" style="">Employee Credentials</p>
                        <div class="mb-4">
                            <label class="form-label">Username</label>
                            <input class="form-control" style="max-width: 300px;" v-model="newEmployee.username" required>
                        </div>
                        <div class="mb-4">
                            <label class="form-label">Password</label>
                            <input class="form-control" style="max-width: 300px;" v-model="newEmployee.password" required>
                        </div>
                        <div class="">
                            <input class="form-check-input" type="radio" name="newEmployeePermissions" id="newEmployeeAdminAccess">
                            <label class="px-1 form-check-label">
                                Admin access
                            </label>
                        </div>
                        <div class="">
                            <input class="form-check-input" type="radio" name="newEmployeePermissions" id="newEmployeeReadWriteAccess">
                            <label class="px-1 form-check-label">
                                Read-write access
                            </label>
                        </div>
                        <div class="mb-3">
                            <input class="form-check-input" type="radio"  name="newEmployeePermissions" id="newEmployeeReadOnlyAccess" checked>
                            <label class="px-1 form-check-label">
                                Read-only access
                            </label>
                        </div>
                        <button @click="createNewEmployee();" class="btn btn-dark w-100 mt-2" id="saveChangesButton" style="max-width: 300px;">Submit</button>
                    </form>
                </div>
            </div>


            <div v-if="this.showEditEmployeeInformation == true" class="col-md-auto" style="margin-top: 1.9em">
                <div class="bg-dark text-white" style="height: 50px; width: 100%; max-width: 345px; border-radius: 10px; box-shadow: 0 3px 5px rgb(0 0 0 / 0.4);">
                    <p class="mx-3" style="padding-top: 12px; font-weight: bold; font-size: 20px;">Edit employee information<i class="fa-solid fa-xmark" id="togglerIcon" @click="closeSideMenu()" style="margin-left: 1.5em"></i> </p>
                </div>  
                <div style="padding-left: 25px; padding-right: 25px;">
                    <form onsubmit="return false">
                        <div class="mb-4 mt-4">
                            <label for="username" class="form-label">First Name</label>
                            <input type="text" class="form-control" style="max-width: 300px;" v-model="selectedEmployeefirstName" required>
                        </div>
                        <div class="mb-4">
                            <label for="username" class="form-label">Last Name</label>
                            <input type="text" class="form-control" style="max-width: 300px;" v-model="selectedEmployeelastName" required>
                        </div>
                        <div class="mb-4">
                            <label for="username" class="form-label">Email</label>
                            <input type="text" class="form-control" style="max-width: 300px;" pattern="[^@\s]+@[^@\s]+\.com" aria-describedby="emailHelpBlock" v-model="selectedEmployeeEmail" required>
                            <small id="emailHelpBlock" class="form-text text-muted">
                                Ex. email@email.com
                            </small>
                        </div>
                        <div class="mb-4">
                            <label for="username" class="form-label">Phone</label>
                            <input type="text" class="form-control" style="max-width: 300px;" pattern="^\d{3}-\d{3}-\d{4}$" aria-describedby="phoneHelpBlock" v-model="selectedEmployeePhoneNumber" required>
                            <small id="phoneHelpBlock" class="form-text text-muted">
                                Ex. xxx-xxx-xxxx
                            </small>
                        </div> 
                        <p class="fw-bold" style="">Employee Credentials</p>
                        <div v-if="this.selectedEmployeeActive == 'Yes'" class="mb-4">
                            <input class="form-check-input" type="checkbox" value="" id="employeeActiveCheckbox" checked>
                            <label class="px-1 form-check-label" for="employeeActiveCheckbox">
                                Active Employee
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeActive == 'No'" class="mb-4">
                            <input class="form-check-input" type="checkbox" value="" id="employeeActiveCheckbox">
                            <label class="px-1 form-check-label" for="employeeActiveCheckbox">
                                Active Employee
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin == 'Administrator'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions" id="editEmployeeAdminAccess" checked>
                            <label class="px-1 form-check-label">
                                Admin access
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin != 'Administrator'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions"  id="editEmployeeAdminAccess">
                            <label class="px-1 form-check-label">
                                Admin access
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin == 'Read-only'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions" id="editEmployeeReadOnlyAccess" checked>
                            <label class="px-1 form-check-label">
                                Read-only access
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin != 'Read-only'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions" id="editEmployeeReadOnlyAccess">
                            <label class="px-1 form-check-label">
                                Read-only access
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin == 'Read-write'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions" id="editEmployeeReadWriteAccess" checked>
                            <label class="px-1 form-check-label">
                                Read-write access
                            </label>
                        </div>
                        <div v-if="this.selectedEmployeeAdmin != 'Read-write'" class="">
                            <input class="form-check-input" type="radio" name="editEmployeePermissions" id="editEmployeeReadWriteAccess">
                            <label class="px-1 form-check-label">
                                Read-write access
                            </label>
                        </div>
                        <button @click="editEmployeeInformation()" class="btn btn-dark w-100 mt-4" id="saveChangesButton" style="max-width: 300px;">Save Changes</button>
                        <button @click="deleteEmployeeInformation()" class="btn btn-danger w-100 mt-4" id="deleteEmployeeButton" style="max-width: 300px;">Delete Employee</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
        name: 'employees_component',
        data() {
            return {
                editEmployeeInfoTarget: {
                    currentEmployeePhoneNumber: '',
                    currentEmployeeEmail: ''
                },
                selectedEmployeefirstName: '',
                selectedEmployeelastName: '',
                selectedEmployeeEmail: '',
                selectedEmployeePhoneNumber: '',
                selectedEmployeeActive: '',
                selectedEmployeeAdmin: '',
                newEmployee: {
                    firstName: '',
                    lastName: '',
                    email: '',
                    phoneNumber: '',
                    username: '',
                    password: '',
                    permissions: ''
                },
                filter: '',
                showAddEmployee: false,
                showEditEmployeeInformation: false,
                adminPrivileges: window.sessionStorage.getItem('adminPrivileges'),
                employees: null,
                firstNameSort: -1,
                lastNameSort: -1,
                emailSort: -1,
                phoneSort: -1,
                activeSort: -1,
                permissionsSort: -1
            }
        },
        created() {
            let apiURL = 'http://localhost:3000/dashboard/employees';
            axios.get(apiURL).then(res => {
                this.employees = res.data;
                }).catch(error => {
                console.log(error)
            })
        },
        methods: {
            sortByFirstName() {
                if (this.firstNameSort == -1) {
                    this.employees.sort((a, b) => (a.firstName > b.firstName) ? 1 : - 1)
                    this.firstNameSort = 1
                    return
                }
                if (this.firstNameSort == 1) {
                    this.employees.sort((a, b) => (a.firstName < b.firstName) ? 1: - 1)
                    this.firstNameSort = -1
                    return
                }
            },
            sortByLastName() {
                if (this.lastNameSort == -1) {
                    this.employees.sort((a, b) => (a.lastName > b.lastName) ? 1 : - 1)
                    this.lastNameSort = 1
                    return
                }
                if (this.lastNameSort == 1) {
                    this.employees.sort((a, b) => (a.lastName < b.lastName) ? 1: - 1)
                    this.lastNameSort = -1
                    return
                }
            },
            sortByEmail() {
                if (this.emailSort == -1) {
                    this.employees.sort((a, b) => (a.email > b.email) ? 1 : - 1)
                    this.emailSort = 1
                    return
                }
                if (this.emailSort == 1) {
                    this.employees.sort((a, b) => (a.email < b.email) ? 1: - 1)
                    this.emailSort = -1
                    return
                }
            },
            sortByPhone() {
                if (this.phoneSort == -1) {
                    this.employees.sort((a, b) => a.phoneNumber > b.phoneNumber ? 1 : - 1)
                    this.phoneSort = 1
                    return
                }
                if (this.phoneSort == 1) {
                    this.employees.sort((a, b) => (a.phoneNumber < b.phoneNumber) ? 1: - 1)
                    this.phoneSort = -1
                    return
                }
            },
            sortByActive() {
                if (this.activeSort == -1) {
                    this.employees.sort((a, b) => a.active > b.active ? 1 : - 1)
                    this.activeSort = 1
                    return
                }
                if (this.activeSort == 1) {
                    this.employees.sort((a, b) => (a.active < b.active) ? 1: - 1)
                    this.activeSort = -1
                    return
                }
            },
            sortByPermissions() {
                if (this.permissionsSort == -1) {
                    this.employees.sort((a, b) => a.permissions > b.permissions ? 1 : - 1)
                    this.permissionsSort = 1
                    return
                }
                if (this.permissionsSort == 1) {
                    this.employees.sort((a, b) => (a.permissions < b.permissions) ? 1: - 1)
                    this.permissionsSort = -1
                    return
                }
            },
            toggleEditEmployeeInformation() {
                if (this.showAddEmployee == true) {
                    this.showAddEmployee = false
                }
                if (this.showEditEmployeeInformation == false) {
                    this.showEditEmployeeInformation = true
                }
            },
            toggleAddEmployee() {
                if (this.showEditEmployeeInformation == true) {
                    this.showEditEmployeeInformation = false
                }
                if (this.showAddEmployee == false) {
                    this.showAddEmployee = true
                }
            },
            closeSideMenu() {
                if (this.showEditEmployeeInformation == true) {
                    this.showEditEmployeeInformation = false
                }
                if (this.showAddEmployee == true) {
                    this.showAddEmployee = false
                }
            },
            checkAdminActive() {
                if (this.selectedEmployeeActive  == 'Yes') {
                        document.getElementById('employeeActiveCheckbox').checked === true
                    }
                    if (this.selectedEmployeeAdmin == 'Yes') {
                        document.getElementById('employeeAdminCheckbox').checked === true
                }
            },
            createNewEmployee() {
                if (document.getElementById('newEmployeeAdminAccess').checked === true) {
                    this.newEmployee.permissions = 1
                }
                if (document.getElementById('newEmployeeReadWriteAccess').checked === true) {
                    this.newEmployee.permissions = 3
                }
                if (document.getElementById('newEmployeeReadOnlyAccess').checked === true) {
                    this.newEmployee.permissions = 2
                }
                if (this.newEmployee.firstName != '' && this.newEmployee.lastName != '' && this.newEmployee.email != '' &&
                    this.newEmployee.phoneNumber != '' && this.newEmployee.username != '' && this.newEmployee.password != '' && /[^@\s]+@[^@\s]+\.com/.test(this.newEmployee.email) && /^\d{3}-\d{3}-\d{4}$/.test(this.newEmployee.phoneNumber))  {
                        let apiURL = 'http://localhost:3000/dashboard/employees'
                        axios.post(apiURL, this.newEmployee).then(res => {
                            console.log(res)
                            if (res.data == 'email and username already exist.') {
                                alert("An employee with that email and username already exists.")
                            }
                            if (res.data == 'email and phone number already exist.') {
                                alert("An employee with that email and phone number already exists.")
                            }
                            if (res.data == 'username and phone number already exist.') {
                                alert("An employee with that username and phone number already exists.")
                            }
                            if (res.data == 'username already exists.') {
                                alert("An employee with that username already exists.")
                            }
                            if (res.data == 'email already exists.') {
                                alert("An employee with that email already exists.")
                            }
                            if (res.data == 'phone number already exists.') {
                                alert("An employee with that phone number already exists.")
                            }
                            if (res.data == 'email, phone number, and username already exist.') {
                                alert("An employee with that email, phone number, and username already exists.")
                            }
                            axios.get(apiURL).then(res => {
                                this.employees = res.data;
                                }).catch(error => {
                                console.log(error)
                            })
                        })
                    }
            },
            editEmployeeInformation() {
                var emp_active = null
                var emp_type_id = null
                if (document.getElementById('employeeActiveCheckbox').checked === true) {
                    emp_active = 1
                }
                if (document.getElementById('employeeActiveCheckbox').checked === false) {
                    emp_active = 0
                }
                if (document.getElementById('editEmployeeAdminAccess').checked === true) {
                    emp_type_id = 1
                }
                if (document.getElementById('editEmployeeReadOnlyAccess').checked === true) {
                    emp_type_id = 2
                }
                if (document.getElementById('editEmployeeReadWriteAccess').checked === true) {
                    emp_type_id = 3
                }
                if (this.selectedEmployeefirstName != '' && this.selectedEmployeelastName != '' && this.selectedEmployeeEmail != '' && this.selectedEmployeePhoneNumber != ''
                    && /[^@\s]+@[^@\s]+\.com/.test(this.selectedEmployeeEmail) && /^\d{3}-\d{3}-\d{4}$/.test(this.selectedEmployeePhoneNumber)) {
                    let apiURL = 'http://localhost:3000/dashboard/employees'
                    var updatedEmployeeInfo = {
                        emp_first_name: this.selectedEmployeefirstName, 
                        emp_last_name: this.selectedEmployeelastName, 
                        emp_email: this.selectedEmployeeEmail, 
                        emp_phone: this.selectedEmployeePhoneNumber,
                        emp_type_id: emp_type_id,
                        emp_active: emp_active,
                        current_employee_email: this.editEmployeeInfoTarget.currentEmployeeEmail,
                        current_employee_phone: this.editEmployeeInfoTarget.currentEmployeePhoneNumber
                    }  
                    var emailMatch = false 
                    var phoneMatch = false
                    for (let i = 0; i < this.employees.length; i++) {
                        if (this.selectedEmployeeEmail == this.employees[i].email) {
                            emailMatch = true
                        }
                        if (this.selectedEmployeePhoneNumber == this.employees[i].phoneNumber) {
                            phoneMatch = true
                        }
                    }

                    if (emailMatch == true && phoneMatch == false) {
                        alert('Email not upated. The entered email is already in use by this employee or another employee.')
                    }
                    if (phoneMatch == true && emailMatch == false) {
                        alert('Phone number not updated. The entered phone number is already in use by this employee or another employee.')
                    } 
                    if (phoneMatch == true && emailMatch == true) {
                        alert('Email and phone number not updated. The entered email and phone number are already in use by this employee or another employee.')
                    } 
                    if (phoneMatch == false && emailMatch == false) {
                        alert('Employee record updated successfully')
                    }                
                    axios.put(apiURL, updatedEmployeeInfo).then(res => { 
                        if (res.data == 'update failed') {
                            axios.get(apiURL).then(res => {
                            this.employees = res.data;
                            }).catch(error => {
                            console.log(error)
                            })
                        }
                        if (res.data[0] == 'update successful') {      
                            this.editEmployeeInfoTarget.currentEmployeeEmail = res.data[1]
                            axios.get(apiURL).then(res => {
                                this.employees = res.data;
                                }).catch(error => {
                                console.log(error)
                                })
                        }
                    }) 
                }
            },
            deleteEmployeeInformation() {
                if(confirm("Are you certain you want to delete this employee? This action is irreversible.") == true) {
                    let apiURL = `http://localhost:3000/dashboard/employees/${this.selectedEmployeeEmail}/${this.selectedEmployeePhoneNumber}`
                    axios.delete(apiURL).then(res => {
                        console.log(res)
                        axios.get('http://localhost:3000/dashboard/employees').then(res => {
                            this.employees = res.data;
                            this.closeSideMenu()
                        })

                    }).catch(error => { 
                        console.log(error)
                    })
                }
            }
        }
}
</script>

<style scoped>
#searchBar:focus::-webkit-input-placeholder 
{
    color: transparent;
}

#searchBar:focus {
    border-color:#292b2c;
    outline: 0px;
    box-shadow: none;
}

#addEmployee {
    background: rgb(57,130,224);
    background: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
}

#addEmployee:hover #addEmployeeText {
    opacity: 40%;
    transition: 0.3s;
}

#editButton:hover {
    opacity: 90%;
}

#deleteButton:hover {
    opacity: 90%;
}

#saveChangesButton:hover {
    opacity: 90%;
}

#togglerIcon:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
}

::-webkit-scrollbar {
    width: 15px;
}

::-webkit-scrollbar-thumb {
background:#292b2c;
border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
background:rgb(54, 56, 58); 
}
</style>