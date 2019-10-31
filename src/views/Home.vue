<template>
  <div class="home">

  <img src="../assets/Logo2.png" class="avatar">
    <div class="container-box">
      <div class="bg"></div>  
      <div class="ite">
        <h1 class="txt">Calories Remaining</h1>
        <p class="txt">2460 + 0 + 2 = 2462</p>
      </div>


      <div class="ite">
        <h1>Breakfast</h1>
        <h3>ADD FOOD</h3>
      </div>

      <div class="ite">
        <h1>Lunch</h1>
        <h3>ADD FOOD</h3>
      </div>

      <div class="ite">
        <h1>Dinner</h1>
        <h3>ADD FOOD</h3>
      </div>

    </div>

    <div class="container">
      <button @click="logout" class="item scan">Logout</button>
      <button @click="scan" class="item">Scan</button>
      <button @click="profile" class="item scan">Profile</button>
    </div>

  </div>
</template>

<style scoped>
  textarea {
    width:100%;
    height:530px;
    border: 1px solid black;
  }
  
  img.avatar {
    width: 40%;
  }
  
  .container {
    display:flex;
    margin-top: 0;
    margin-bottom: 0;
    height:100%;

  }

  .container-box {
    display:flex;
    flex-direction: column;
    text-align: left;
    height:550px;
    border: 1px solid black;
    align-items: stretch;
    background-image: url(../assets/background.jpeg);
    opacity: 1;

  }
 

  .ite {
    flex: 1;
    background-color:white;
    opacity:0.6;

  }

  .item {
    flex-grow:1;
    /*padding:25px;*/
    /*height:100%;*/
  }

  .scan {
    background-color:grey;
  }


  .home {
     background-image: url(../assets/background.jpeg) center center;
     z-index: -100;
  }

</style>
<script>
  export default {
    name: 'home',
    data() {
      return {
        diabetes: false,
        hypertension: false

      }
    },
    methods: {
      scan: function(){
        var navigate = this.$router;
        navigate.push({name: 'read'})
      },
      profile: function(){
        var navigate = this.$router;
        navigate.push({name: 'profile'})
      },
      logout: function(){
        var navigate = this.$router;
        navigate.push({name: 'login'})
      }
    }
  }  


</script>
