import { defineStore } from "pinia";

import axios from "axios";

export const useAuthStore = defineStore("auth", {

  state: () => ({

    user: null,

    isAuthenticated: false,

    loading: true

  }),

  actions: {

    // REGISTER
    async register(formData){

      const response = await axios.post(

        "/api/auth/register",

        formData,

        {
          withCredentials: true
        }

      )

      return response.data

    },


    // LOGIN
    async login(formData){

      const response = await axios.post(

        "/api/auth/login",

        formData,

        {
          withCredentials: true
        }

      )

      this.user = response.data.user

      this.isAuthenticated = true

      return response.data

    },


    // GET AUTHENTICATED USER
    async getAuthenticatedUser(){

      try{

        const response = await axios.get(

          "/api/auth/get-authenticated-user",

          {
            withCredentials: true
          }

        )

        this.user = response.data.user

        this.isAuthenticated = true

      }

      catch(error){

        console.log(error)

        this.user = null

        this.isAuthenticated = false

      }

      finally{

        this.loading = false

      }

    },


    // LOGOUT
    logout(){

      this.user = null

      this.isAuthenticated = false

    }

  }

})