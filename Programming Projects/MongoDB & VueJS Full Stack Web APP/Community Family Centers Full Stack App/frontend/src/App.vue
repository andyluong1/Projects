
<template>

  <div>
    <!-- Navigation bar -->
    <nav class="navbar navbar-expand navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand float-left " href="/"> Community Family Centers - CIS 4339: Group 20</a>
        <ul class="nav navbar-nav mr-auto" >
          <li class="nav-item">
            <router-link class="nav-link" to="/create">Create Clients</router-link>
          </li>

          <li class="nav-item">
            <router-link class="nav-link" to="/view">View Clients</router-link>
          </li>

          <li class="nav-item">
            <router-link class="nav-link" to="/programs">View Programs</router-link>
          </li>

          <li class="nav-item">
            <router-link class="nav-link" to="/ProgramChart">Analysis</router-link>
          </li>
          
          <li class="nav-item">
            <router-link class="nav-link" to="/about">About</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Router view -->
    <div class="container mt-5">
      <router-view></router-view>
    </div>
  </div> 
</template>