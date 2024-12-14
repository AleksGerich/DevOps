pipeline {
  agent any

  stages {
    stage('Install') {
      steps {
        ansiblePlaybook(
          playbook: './ansible/Playbook.yml',
          inventory: './ansible/inventory/inventory',
          tags: 'install'
        )
      }
    }
    stage('Clone') {
      steps {
        ansiblePlaybook(
          playbook: './ansible/Playbook.yml',
          inventory: './ansible/inventory/inventory',
          tags: 'clone'
        )
      }
    }
    stage('Start') {
      steps {
        ansiblePlaybook(
          playbook: './ansible/Playbook.yml',
          inventory: './ansible/inventory/inventory',
          tags: 'start'
        )
      }
    }
  }
}
  
