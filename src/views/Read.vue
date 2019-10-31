<template>
  <div class="read">
    <Loading v-if="isLoading"/>    
    <h1>Upload Photo Below</h1>
    <div v-for="data in scanned_data">
      
<!--       <div v-if="data.state!=0"> -->
        <input type="text" :value="data.ingredient" disabled>
        <p>{{ data.description }}</p>
        <h3 :class="{'one': data.rating==1, 'two': data.rating==2, 'three': data.rating==3 }">Rating: {{ data.rating }}</h3>
      <!-- </div>         -->

   
    </div>

    <label>File
      <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
    </label>
    
    <button v-on:click="submitFile()">Submit</button>
    <router-link to="home"><button class="back">Back</button></router-link>
  </div>
</template>

<script>
  import Loading from '@/components/Loading.vue'


  export default {
    name: 'read',
    data(){
      return {
        file: '',
        scanned_data: '',
        isLoading: false,
        hypertension: false,
        diabetes: false
      }
    },
    components: {Loading},
    methods: {
      submitFile(){

        this.isLoading = true;

        var navigate = this.$route;


        if (typeof this.hypertensiontypeof == 'undefined' && typeof this.diabetes == 'undefined'){

          this.hypertension = false;
          this.diabetes = false;

        } else {

          this.hypertension = navigate.params.diabetes;
          this.diabetes = navigate.params.hypertension;
        }

        console.log(this.hypertension)
        console.log(this.diabetes)

        function getBase64(file) {

          return new Promise((resolve, reject) => {
            
            const reader = new FileReader();
            
            reader.readAsDataURL(file);
            
            reader.onload = () => {
              let encoded = reader.result.toString().replace(/^data:(.*,)?/, '');
              if ((encoded.length % 4) > 0) {
                encoded += '='.repeat(4 - (encoded.length % 4));
              }
              resolve(encoded);
            };
            reader.onerror = error => {
              this.isLoading = false;
              alert(error);
              reject(error);
            }
          });
        }
        
        getBase64(this.file).then(res =>{

          var encoded = {
            "image": res
          }

          var url = "https://8ev2ii2wnl.execute-api.ap-southeast-1.amazonaws.com/dev/upload"

          this.$http.post(url,
              encoded,
              {
              headers: {
                  'Content-Type': 'multipart/form-data'
              }
            }
          ).then(res => {
            console.log(res);
            this.scanned_data = res.data;
            this.isLoading = false;
          })
          .catch(error => {
            console.log(error);
            this.isLoading = false;
            alert(error)
          });
        })
    
      },

      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>
<style>
  textarea {
    width:100%;
    height:500px;
    border: 1px solid black;
  }

  .back {
    background-color:grey;
    width: 100%;
  }

  .one {
    background-color:#9dfa9b;
  }

  .two {
    background-color:yellow;
  }

  .three {
    background-color:orange;
  }



</style>



