pipeline {
   agent {
       docker { image 'python:3.5.1' }
   }

   stages {
      stage('build') {
         steps {
            echo 'building'
         }
      }
      
      stage('testing') {
          steps {
            echo 'testing'
         }
      }
      
      stage('deploying') {
          steps {
            echo 'deploying'
         }
      }
      
      stage('monitoring') {
          steps {
            echo 'monotoring'
         }
      }
      
      stage('loadtest') {
          steps {
            echo 'load test'
         }
      }
   }
   
   post {
       success {
           echo 'this is success report'
       }
       
       failure {
           echo 'this is failure report'
       }
   }
}
