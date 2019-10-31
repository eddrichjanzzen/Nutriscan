<template>
  <div class="profile">
     <h1>CREATE YOUR PROFILE</h1>
      <h3>GENERAL INFORMATION</h3>
      
      <input type="text" placeholder="Age" required>
      
      <select name="" id="">
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>

      <input type="text" placeholder="Weight (in kg)" required>
      <input type="text" placeholder="Height (in cm)" required>
      <input type="text" placeholder="Allegies">


      <h3>FAMILY HISTORY OF DISEASES</h3>
      <h4>(Please check all that apply)</h4>

      <input v-model="diabetes" type="checkbox" name="diabetes">Diabetes
      <input v-model="hypertension" type="checkbox" name="hypertension">Hypertension
      <input type="checkbox" name="cancer">Cancer
      <input type="checkbox" name="others">Others

      <router-link to="home"><button class="back">Back</button></router-link>
      <button @click="submit" class="submit">Submit</button>

  </div>
</template>
<style scoped>
  .submit, .back {
    float: left;
    width: 49%;
  }

  .back {
    background-color:grey;
    margin-right:2%;
  }

  select {
    width:100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }

</style>
<script>

  

  export default {
    name: 'profile',
    data() {
      return {
        diabetes: false,
        hypertension: false

      }
    },
    methods: {
      submit: function(){

        var navigate = this.$router;

        navigate.push({name: 'read', params: { diabetes: this.diabetes, hypertension: this.hypertension }})


      }
    }
  }


</script>



