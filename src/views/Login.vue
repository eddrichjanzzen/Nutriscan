<template>
  <div class="login">

    <h1>LOG IN</h1>

    <div class="imgcontainer">
      <img src="../assets/Logo1.png" class="avatar">
    </div>

    <div class="container">
      <input name="uname" type="text" placeholder="Email">
      <input name="pwd" type="password" placeholder="Password">
      <router-link to="profile"><button type="submit">Log in</button></router-link>
    </div>
    <p><b>Don't have an account?</b> <router-link to="signup">Register Here</router-link></p>
  </div>
</template>
<style>

  /* Avatar image */
  img.avatar {
    width: 55%;
  }

</style>

